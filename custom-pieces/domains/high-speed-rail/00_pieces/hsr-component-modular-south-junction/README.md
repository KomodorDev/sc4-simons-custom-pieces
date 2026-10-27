# HSR Modular Symmetric Split and Return

<!-- PIECE README LAYOUT: 1 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [4. Testing](#4-testing)

This reusable High Speed Rail (HSR) junction splits one travel direction into two outlets and merges two entrances into the opposite return direction. Every train path remains at nominal Level 2 (L2), measured at 15.5 m. The pictured fork is one component assembled with further tracks; it is not a complete one-click interchange.

**Status: experimental.** Software pictures and saved-resource checks do not establish human preview approval, game appearance, or train operation. The exact menu name is **HSR Modular Symmetric Split and Return**, and the permanent type ID is `hsr-component-modular-south-junction`.

## 1. Views

Both clean pictures show the same complete saved model at its authored 0° orientation. North is up in the top view; X increases eastward, Y increases northward, and each city tile measures 16 × 16 m. The local picture grid belongs to this reusable type. Its software reference is not a certified mouse-click anchor.

<!-- BEGIN PIECE VIEWS -->

![HSR Modular Symmetric Split and Return — Clean angled view](previews/preview.png)

![HSR Modular Symmetric Split and Return — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

The [angled-view evidence](evidence/preview.json) and [top-view evidence](evidence/preview-top.json) identify the actual saved model, textures, camera, captions, and image fingerprints. The connection overview in chapter 3 adds measured boundary cards to that same reusable type.

## 2. Piece and placement

<!-- BEGIN PIECE OVERVIEW -->

Flat L2 paired split and return with three northern outlets for native paired or centred one-way HSR and one southern native paired connection.

Exact reusable identifier: `hsr-component-modular-south-junction`.

Footprint: **3 × 6 tiles**. Exact menu name: **HSR Modular Symmetric Split and Return**.

<!-- END PIECE OVERVIEW -->

### Function and complete joining boundaries

At the authored 0° orientation, the southern paired end connects to a shorter paired end facing north and two separated outer northern ends. The left outer track enters the piece and joins the southbound track. The right outer track leaves the piece from the northbound track. The central paired end continues the two mainline directions. These four permitted journeys are intrinsic to the piece, and the matrix reports them separately from forbidden transfers.

A paired boundary contains both opposite-direction tracks and must continue them together. The southern paired end and the recessed central northern paired end use the native Level 2 paired section. Each outer northern end contains one centred directed track. Its measured centre, height, travel direction, and physical model still require a complete comparison before another piece is accepted as a continuation. The empty tiles around the recessed northern end are not additional declared attachment points.

The permanent construction definition is [piece.json](piece.json), and its geometry belongs in [geometry.json](geometry.json). The [authored connector groups](connector-groups.jsonc), [resolved export](connector-data.json), and [measured connections](connections.json) describe this piece’s intrinsic boundaries and journeys. The library does not supply automatic compatibility discovery, and this guide does not publish a neighbour shortlist.

### Place and rotate the piece

After following the [separate installation procedure](../../../../docs/BUILD_AND_INSTALL.md), use a disposable flat test city. A proper rotation turns the whole piece and all its travel directions together; it does not reflect the piece or reverse a directed track.

1. Open **Transportation → Rail**, hover over the SCP buttons, and select **HSR Modular Symmetric Split and Return**. An assembly can expose the same reusable type through its Tab/Shift+Tab component cycle.
2. Move the complete cursor preview onto clear terrain. Press **Home** or **End** to rotate; on the documented Mac keyboard, **Fn + ←** and **Fn + →** provide those keys. Use only the supported construction states listed below.
3. At 0°, identify the southern paired end, the recessed central paired end facing north, and the two outer northern single-track ends. The left outer end receives traffic; the right outer end sends traffic. Keep the 3 × 6 tile construction rectangle clear for the first trial.
4. Click once to place the component. Supply matching outside connections and travel demand. Inspect tracks, decks, walls, supports, and shadows, then check the permitted journeys and unavailable movements separately.

## 3. Connection matrix

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](#case-in_game_render-c8a33b58b9fbd61e4079) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](#test-checklist).

| Entrance ↓ / Exit → | **HSR · South exit**<br>`Sout` | **HSR · North exit**<br>`Nout` | **HSR · North exit**<br>`Rout` |
| --- | --- | --- | --- |
| **HSR · North entrance**<br>`Lin` | **Saved PATH:** [✅](#case-software_connectivity-8d7f9e5f7613da7f657b)<br>**Route Query:** [?](#case-in_game_route_query-cf0d19c93952223d47d1)<br>**Visible train travel:** [?](#case-in_game_visible_travel-cf0d19c93952223d47d1) | **Forbidden**<br>**Saved PATH:** [✅](#case-software_connectivity-8d7f9e5f7613da7f657b)<br>In-game check: [?](#case-in_game_forbidden_transfer-cebd07ace4c23e3b0b40) | **Forbidden**<br>**Saved PATH:** [✅](#case-software_connectivity-8d7f9e5f7613da7f657b)<br>In-game check: [?](#case-in_game_forbidden_transfer-9cc44127a3b0a3f352f1) |
| **HSR · North entrance**<br>`Nin` | **Saved PATH:** [✅](#case-software_connectivity-8d7f9e5f7613da7f657b)<br>**Route Query:** [?](#case-in_game_route_query-591b8068a7af8a82744c)<br>**Visible train travel:** [?](#case-in_game_visible_travel-591b8068a7af8a82744c) | **Forbidden**<br>**Saved PATH:** [✅](#case-software_connectivity-8d7f9e5f7613da7f657b)<br>In-game check: [?](#case-in_game_forbidden_transfer-0d1db4aa8702d16edfa7) | **Forbidden**<br>**Saved PATH:** [✅](#case-software_connectivity-8d7f9e5f7613da7f657b)<br>In-game check: [?](#case-in_game_forbidden_transfer-b1c116c697c9ef2bdbe6) |
| **HSR · South entrance**<br>`Sin` | **Forbidden**<br>**Saved PATH:** [✅](#case-software_connectivity-8d7f9e5f7613da7f657b)<br>In-game check: [?](#case-in_game_forbidden_transfer-0f95ab42ea20b9fade96) | **Saved PATH:** [✅](#case-software_connectivity-8d7f9e5f7613da7f657b)<br>**Route Query:** [?](#case-in_game_route_query-3e9107af6496c7d3ac4a)<br>**Visible train travel:** [?](#case-in_game_visible_travel-3e9107af6496c7d3ac4a) | **Saved PATH:** [✅](#case-software_connectivity-8d7f9e5f7613da7f657b)<br>**Route Query:** [?](#case-in_game_route_query-abb9d42e6ab5a4275279)<br>**Visible train travel:** [?](#case-in_game_visible_travel-abb9d42e6ab5a4275279) |

Source: [connections.json](connections.json).

<!-- END PIECE CONNECTION MATRIX -->

<!-- BEGIN CONNECTOR OVERVIEW -->

### Connection overview

Generated from this piece's source-bound connector metadata and the current compiled model; marker letters refer to the boundary cards below.

![Complete connection overview](previews/connection-overview.png)

[Rendering sources and verification scope](evidence/connection-overview.json).

Headings: 0° = North, 90° = East, 180° = South, and 270° = West; clockwise in plan view, pointing out of the piece.

Coordinates [E,N,H] = [east,north,height] in metres. Source cells [column,row] increase east and south.

Display grid: X = source column − (0); Y = 5 − source row.

Slope is measured outward at the joining edge; the interior may differ. Offsets are + left and − right facing out of the tile edge.

Member offsets use the section origin. Counts distinguish physical channels / edge cuts / directed members; modes do not multiply channels.

Incoming flow enters this piece; outgoing flow leaves it. Letters identify boundary cards; source IDs remain the stable identities.

#### Boundary A: `cell-0-0-north`

This service group is required at this edge.

##### Service group 1 / 1: HSR — Level 2 (15.5 m)

| Field | Value |
| --- | --- |
| End / component | `left-northern-end` / `symmetric-split-return` |
| Network / game class / role | hsr / Monorail (7); primary |
| Source cell / edge | `[0,0]` / North |
| Section origin [E,N] (m) | `[0,8]` |
| Centring / section offset | Centred; 0 m |
| Level (path height) | Level 2 (15.5 m) |
| Outward heading | 0° (North) |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | rail |
| Traffic modes | monorail |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `left-northern-end-lin` / `Lin` | `left-return-branch` / `left-northern-end-left-return-branch-cut` / monorail | Incoming | `[0,8,15.5]` | +0 | 0° | 0 |

#### Boundary B: `cell-1-2-north`

This service group is required at this edge.

##### Service group 1 / 1: HSR — Level 2 (15.5 m)

| Field | Value |
| --- | --- |
| End / component | `north-paired-end` / `symmetric-split-return` |
| Network / game class / role | hsr / Monorail (7); primary |
| Source cell / edge | `[1,2]` / North |
| Section origin [E,N] (m) | `[16,-24]` |
| Centring / section offset | Centred; 0 m |
| Level (path height) | Level 2 (15.5 m) |
| Outward heading | 0° (North) |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 2 / 2 / 2 |
| Traffic arrangement / running | 1 incoming; 1 outgoing; Right-hand running |
| Channel spacing | 4 m |
| Channel kinds | rail |
| Traffic modes | monorail |
| Profile | `hsr-l2-orth-scp-paired15-t2-opposed-rhd-v1` |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `north-paired-end-nin` / `Nin` | `southbound-mainline` / `north-paired-end-southbound-mainline-cut` / monorail | Incoming | `[14,-24,15.5]` | +2 | 0° | 0 |
| `north-paired-end-nout` / `Nout` | `northbound-mainline` / `north-paired-end-northbound-mainline-cut` / monorail | Outgoing | `[18,-24,15.5]` | -2 | 0° | 0 |

#### Boundary C: `cell-1-5-south`

This service group is required at this edge.

##### Service group 1 / 1: HSR — Level 2 (15.5 m)

| Field | Value |
| --- | --- |
| End / component | `south-paired-end` / `symmetric-split-return` |
| Network / game class / role | hsr / Monorail (7); primary |
| Source cell / edge | `[1,5]` / South |
| Section origin [E,N] (m) | `[16,-88]` |
| Centring / section offset | Centred; 0 m |
| Level (path height) | Level 2 (15.5 m) |
| Outward heading | 180° (South) |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 2 / 2 / 2 |
| Traffic arrangement / running | 1 incoming; 1 outgoing; Right-hand running |
| Channel spacing | 4 m |
| Channel kinds | rail |
| Traffic modes | monorail |
| Profile | `hsr-l2-orth-scp-paired15-t2-opposed-rhd-v1` |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `south-paired-end-sin` / `Sin` | `northbound-mainline` / `south-paired-end-northbound-mainline-cut` / monorail | Incoming | `[18,-88,15.5]` | +2 | 180° | 0 |
| `south-paired-end-sout` / `Sout` | `southbound-mainline` / `south-paired-end-southbound-mainline-cut` / monorail | Outgoing | `[14,-88,15.5]` | -2 | 180° | 0 |

#### Boundary D: `cell-2-0-north`

This service group is required at this edge.

##### Service group 1 / 1: HSR — Level 2 (15.5 m)

| Field | Value |
| --- | --- |
| End / component | `right-northern-end` / `symmetric-split-return` |
| Network / game class / role | hsr / Monorail (7); primary |
| Source cell / edge | `[2,0]` / North |
| Section origin [E,N] (m) | `[32,8]` |
| Centring / section offset | Centred; 0 m |
| Level (path height) | Level 2 (15.5 m) |
| Outward heading | 0° (North) |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | rail |
| Traffic modes | monorail |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `right-northern-end-rout` / `Rout` | `right-departure-branch` / `right-northern-end-right-departure-branch-cut` / monorail | Outgoing | `[32,8,15.5]` | +0 | 0° | 0 |

Rendering checks source metadata, current compiled resource identities, and model structure. It does not re-extract PATHs or evaluate placement; physical seams, construction clearance, collisions, and game operation remain unverified.

<!-- END CONNECTOR OVERVIEW -->

## 4. Testing

A case is one exact check under stated conditions. Saved-resource software checks, human preview review, game appearance, Route Query, and visible train travel are separate observations. A Route Query line does not prove that a train visibly completed a journey. Only explicit human confirmation can record a manual pass.

Follow the [shared observation procedure](../../../../docs/TESTING.md#record-one-observation) with this piece’s [authoritative test record](checks/manual-tests.json). Preserve failures, stale observations, and their original scope. The generated sections below provide the exact recording command and case identifiers.

### Engineering contract

The construction rectangle is 3 × 6 tiles, containing fourteen occupied cells and eight authored supports. Two occupied cells carry structure without a traffic path; the other empty positions remain absent from the owned-cell mask. Source [column,row] cells increase eastward and southward, while picture X/Y increase eastward and northward. Use the generated grid conversion to identify the recessed central connection rather than treating a source row as a picture Y label.

The current documentation uses the unchanged compiled piece from a verified source build. [Saved-resource evidence](evidence/saved-resource-checks.json) identifies the source DAT and the exact software-report scope; refreshing a guide does not claim another game test. Construction, traffic demand, demolition, shadows, and save/reload remain separate game checks.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/3 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Route Query: 0/16 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/16 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.json) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `Lin` | hsr / 7 / primary | in | [0.0, 8.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-365752af76285c80cd0b` |
| `Sout` | hsr / 7 / primary | out | [14.0, -88.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Nin` | hsr / 7 / primary | in | [14.0, -24.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Sin` | hsr / 7 / primary | in | [18.0, -88.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Nout` | hsr / 7 / primary | out | [18.0, -24.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Rout` | hsr / 7 / primary | out | [32.0, 8.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-ac60d237d23f01143255` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Lin` → `Sout` | primary |
| hsr | `Nin` → `Sout` | primary |
| hsr | `Sin` → `Nout` | primary |
| hsr | `Sin` → `Rout` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| hsr / `Lin` | hsr / `Nout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Lin` | hsr / `Rout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Nin` | hsr / `Nout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Nin` | hsr / `Rout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Sin` | hsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 71, passed: 2, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-modular-south-junction/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-modular-south-junction/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-8d7f9e5f7613da7f657b">[x] passed</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-8d7f9e5f7613da7f657b"></a>

**General: passed** — `software_resources-8d7f9e5f7613da7f657b`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: Actual final normal 13-piece saved-build verification; registered independent PATH, model, construction, menu, and shadow checks; confirmed at: 2026-10-27T21:57:25.376326+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-8d7f9e5f7613da7f657b">[x] passed</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-8d7f9e5f7613da7f657b"></a>

**General: passed** — `software_connectivity-8d7f9e5f7613da7f657b`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: Actual final normal 13-piece saved-build verification; registered independent PATH, model, construction, menu, and shadow checks; confirmed at: 2026-10-27T21:57:25.376326+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:hsr-component-modular-south-junction:canonical-southeast | <a href="#case-preview_review-8219039bd1a0abdc25dc">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-modular-south-junction:canonical-top | <a href="#case-preview_review-90d1cf88eac08860d51c">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-modular-south-junction:connection-overview | <a href="#case-preview_review-ebf8d0f8e2241af4df75">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:hsr-component-modular-south-junction:canonical-southeast</summary>

<a id="case-preview_review-8219039bd1a0abdc25dc"></a>

**General: unverified** — `preview_review-8219039bd1a0abdc25dc`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:hsr-component-modular-south-junction:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-modular-south-junction:canonical-top</summary>

<a id="case-preview_review-90d1cf88eac08860d51c"></a>

**General: unverified** — `preview_review-90d1cf88eac08860d51c`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:hsr-component-modular-south-junction:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-modular-south-junction:connection-overview</summary>

<a id="case-preview_review-ebf8d0f8e2241af4df75"></a>

**General: unverified** — `preview_review-ebf8d0f8e2241af4df75`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:hsr-component-modular-south-junction:connection-overview.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-c8a33b58b9fbd61e4079">[ ] unverified</a> | <a href="#case-in_game_render-83ce8d8482bf01462b30">[ ] unverified</a> | <a href="#case-in_game_render-2c791739a570cb0cb251">[ ] unverified</a> | <a href="#case-in_game_render-e105e9ecce2223cd9f80">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-c8a33b58b9fbd61e4079"></a>

**0° CCW: unverified** — `in_game_render-c8a33b58b9fbd61e4079`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-83ce8d8482bf01462b30"></a>

**90° CCW: unverified** — `in_game_render-83ce8d8482bf01462b30`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-2c791739a570cb0cb251"></a>

**180° CCW: unverified** — `in_game_render-2c791739a570cb0cb251`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-e105e9ecce2223cd9f80"></a>

**270° CCW: unverified** — `in_game_render-e105e9ecce2223cd9f80`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-c8a33b58b9fbd61e4079">[ ] unverified</a> | <a href="#case-in_game_placement-83ce8d8482bf01462b30">[ ] unverified</a> | <a href="#case-in_game_placement-2c791739a570cb0cb251">[ ] unverified</a> | <a href="#case-in_game_placement-e105e9ecce2223cd9f80">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-c8a33b58b9fbd61e4079"></a>

**0° CCW: unverified** — `in_game_placement-c8a33b58b9fbd61e4079`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-83ce8d8482bf01462b30"></a>

**90° CCW: unverified** — `in_game_placement-83ce8d8482bf01462b30`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-2c791739a570cb0cb251"></a>

**180° CCW: unverified** — `in_game_placement-2c791739a570cb0cb251`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-e105e9ecce2223cd9f80"></a>

**270° CCW: unverified** — `in_game_placement-e105e9ecce2223cd9f80`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-c8a33b58b9fbd61e4079">[ ] unverified</a> | <a href="#case-in_game_demolition-83ce8d8482bf01462b30">[ ] unverified</a> | <a href="#case-in_game_demolition-2c791739a570cb0cb251">[ ] unverified</a> | <a href="#case-in_game_demolition-e105e9ecce2223cd9f80">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-c8a33b58b9fbd61e4079"></a>

**0° CCW: unverified** — `in_game_demolition-c8a33b58b9fbd61e4079`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-83ce8d8482bf01462b30"></a>

**90° CCW: unverified** — `in_game_demolition-83ce8d8482bf01462b30`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-2c791739a570cb0cb251"></a>

**180° CCW: unverified** — `in_game_demolition-2c791739a570cb0cb251`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-e105e9ecce2223cd9f80"></a>

**270° CCW: unverified** — `in_game_demolition-e105e9ecce2223cd9f80`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-c8a33b58b9fbd61e4079">[ ] unverified</a> | <a href="#case-in_game_save_reload-83ce8d8482bf01462b30">[ ] unverified</a> | <a href="#case-in_game_save_reload-2c791739a570cb0cb251">[ ] unverified</a> | <a href="#case-in_game_save_reload-e105e9ecce2223cd9f80">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-c8a33b58b9fbd61e4079"></a>

**0° CCW: unverified** — `in_game_save_reload-c8a33b58b9fbd61e4079`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-83ce8d8482bf01462b30"></a>

**90° CCW: unverified** — `in_game_save_reload-83ce8d8482bf01462b30`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-2c791739a570cb0cb251"></a>

**180° CCW: unverified** — `in_game_save_reload-2c791739a570cb0cb251`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-e105e9ecce2223cd9f80"></a>

**270° CCW: unverified** — `in_game_save_reload-e105e9ecce2223cd9f80`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — hsr — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Lin>Sout; entry: Lin; exit: Sout | — | <a href="#case-in_game_route_query-cf0d19c93952223d47d1">[ ] unverified</a> | <a href="#case-in_game_route_query-99a86489e9fc55d03118">[ ] unverified</a> | <a href="#case-in_game_route_query-1af95c8b8bd42ddd5cf3">[ ] unverified</a> | <a href="#case-in_game_route_query-bebbb44b56b8a04d8932">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout | — | <a href="#case-in_game_route_query-591b8068a7af8a82744c">[ ] unverified</a> | <a href="#case-in_game_route_query-3aa7411072ac6311c728">[ ] unverified</a> | <a href="#case-in_game_route_query-7f7a05c21e7430a434d9">[ ] unverified</a> | <a href="#case-in_game_route_query-b952d326e1ae3d4859d5">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_route_query-3e9107af6496c7d3ac4a">[ ] unverified</a> | <a href="#case-in_game_route_query-4fcbc6382af0ddca4f05">[ ] unverified</a> | <a href="#case-in_game_route_query-1031f63a625910d37042">[ ] unverified</a> | <a href="#case-in_game_route_query-4bc1a9ed3b5f661138ac">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Sin>Rout; entry: Sin; exit: Rout | — | <a href="#case-in_game_route_query-abb9d42e6ab5a4275279">[ ] unverified</a> | <a href="#case-in_game_route_query-0da4374c45481e6e306e">[ ] unverified</a> | <a href="#case-in_game_route_query-9cdb0e38746c7f11a766">[ ] unverified</a> | <a href="#case-in_game_route_query-63f9dff6f384ed46d433">[ ] unverified</a> |


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Lin>Sout; entry: Lin; exit: Sout</summary>

<a id="case-in_game_route_query-cf0d19c93952223d47d1"></a>

**0° CCW: unverified** — `in_game_route_query-cf0d19c93952223d47d1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Lin>Sout; entry: Lin; exit: Sout.

No observation recorded.

<a id="case-in_game_route_query-99a86489e9fc55d03118"></a>

**90° CCW: unverified** — `in_game_route_query-99a86489e9fc55d03118`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Lin>Sout; entry: Lin; exit: Sout.

No observation recorded.

<a id="case-in_game_route_query-1af95c8b8bd42ddd5cf3"></a>

**180° CCW: unverified** — `in_game_route_query-1af95c8b8bd42ddd5cf3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Lin>Sout; entry: Lin; exit: Sout.

No observation recorded.

<a id="case-in_game_route_query-bebbb44b56b8a04d8932"></a>

**270° CCW: unverified** — `in_game_route_query-bebbb44b56b8a04d8932`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Lin>Sout; entry: Lin; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout</summary>

<a id="case-in_game_route_query-591b8068a7af8a82744c"></a>

**0° CCW: unverified** — `in_game_route_query-591b8068a7af8a82744c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_route_query-3aa7411072ac6311c728"></a>

**90° CCW: unverified** — `in_game_route_query-3aa7411072ac6311c728`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_route_query-7f7a05c21e7430a434d9"></a>

**180° CCW: unverified** — `in_game_route_query-7f7a05c21e7430a434d9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_route_query-b952d326e1ae3d4859d5"></a>

**270° CCW: unverified** — `in_game_route_query-b952d326e1ae3d4859d5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_route_query-3e9107af6496c7d3ac4a"></a>

**0° CCW: unverified** — `in_game_route_query-3e9107af6496c7d3ac4a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_route_query-4fcbc6382af0ddca4f05"></a>

**90° CCW: unverified** — `in_game_route_query-4fcbc6382af0ddca4f05`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_route_query-1031f63a625910d37042"></a>

**180° CCW: unverified** — `in_game_route_query-1031f63a625910d37042`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_route_query-4bc1a9ed3b5f661138ac"></a>

**270° CCW: unverified** — `in_game_route_query-4bc1a9ed3b5f661138ac`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Sin>Rout; entry: Sin; exit: Rout</summary>

<a id="case-in_game_route_query-abb9d42e6ab5a4275279"></a>

**0° CCW: unverified** — `in_game_route_query-abb9d42e6ab5a4275279`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Rout; entry: Sin; exit: Rout.

No observation recorded.

<a id="case-in_game_route_query-0da4374c45481e6e306e"></a>

**90° CCW: unverified** — `in_game_route_query-0da4374c45481e6e306e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Rout; entry: Sin; exit: Rout.

No observation recorded.

<a id="case-in_game_route_query-9cdb0e38746c7f11a766"></a>

**180° CCW: unverified** — `in_game_route_query-9cdb0e38746c7f11a766`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Rout; entry: Sin; exit: Rout.

No observation recorded.

<a id="case-in_game_route_query-63f9dff6f384ed46d433"></a>

**270° CCW: unverified** — `in_game_route_query-63f9dff6f384ed46d433`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Rout; entry: Sin; exit: Rout.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — hsr — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Lin>Sout; entry: Lin; exit: Sout | — | <a href="#case-in_game_visible_travel-cf0d19c93952223d47d1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-99a86489e9fc55d03118">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1af95c8b8bd42ddd5cf3">[ ] unverified</a> | <a href="#case-in_game_visible_travel-bebbb44b56b8a04d8932">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout | — | <a href="#case-in_game_visible_travel-591b8068a7af8a82744c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3aa7411072ac6311c728">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7f7a05c21e7430a434d9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b952d326e1ae3d4859d5">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_visible_travel-3e9107af6496c7d3ac4a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4fcbc6382af0ddca4f05">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1031f63a625910d37042">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4bc1a9ed3b5f661138ac">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Sin>Rout; entry: Sin; exit: Rout | — | <a href="#case-in_game_visible_travel-abb9d42e6ab5a4275279">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0da4374c45481e6e306e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9cdb0e38746c7f11a766">[ ] unverified</a> | <a href="#case-in_game_visible_travel-63f9dff6f384ed46d433">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Lin>Sout; entry: Lin; exit: Sout</summary>

<a id="case-in_game_visible_travel-cf0d19c93952223d47d1"></a>

**0° CCW: unverified** — `in_game_visible_travel-cf0d19c93952223d47d1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Lin>Sout; entry: Lin; exit: Sout.

No observation recorded.

<a id="case-in_game_visible_travel-99a86489e9fc55d03118"></a>

**90° CCW: unverified** — `in_game_visible_travel-99a86489e9fc55d03118`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Lin>Sout; entry: Lin; exit: Sout.

No observation recorded.

<a id="case-in_game_visible_travel-1af95c8b8bd42ddd5cf3"></a>

**180° CCW: unverified** — `in_game_visible_travel-1af95c8b8bd42ddd5cf3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Lin>Sout; entry: Lin; exit: Sout.

No observation recorded.

<a id="case-in_game_visible_travel-bebbb44b56b8a04d8932"></a>

**270° CCW: unverified** — `in_game_visible_travel-bebbb44b56b8a04d8932`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Lin>Sout; entry: Lin; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout</summary>

<a id="case-in_game_visible_travel-591b8068a7af8a82744c"></a>

**0° CCW: unverified** — `in_game_visible_travel-591b8068a7af8a82744c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_visible_travel-3aa7411072ac6311c728"></a>

**90° CCW: unverified** — `in_game_visible_travel-3aa7411072ac6311c728`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_visible_travel-7f7a05c21e7430a434d9"></a>

**180° CCW: unverified** — `in_game_visible_travel-7f7a05c21e7430a434d9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_visible_travel-b952d326e1ae3d4859d5"></a>

**270° CCW: unverified** — `in_game_visible_travel-b952d326e1ae3d4859d5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_visible_travel-3e9107af6496c7d3ac4a"></a>

**0° CCW: unverified** — `in_game_visible_travel-3e9107af6496c7d3ac4a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_visible_travel-4fcbc6382af0ddca4f05"></a>

**90° CCW: unverified** — `in_game_visible_travel-4fcbc6382af0ddca4f05`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_visible_travel-1031f63a625910d37042"></a>

**180° CCW: unverified** — `in_game_visible_travel-1031f63a625910d37042`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_visible_travel-4bc1a9ed3b5f661138ac"></a>

**270° CCW: unverified** — `in_game_visible_travel-4bc1a9ed3b5f661138ac`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Sin>Rout; entry: Sin; exit: Rout</summary>

<a id="case-in_game_visible_travel-abb9d42e6ab5a4275279"></a>

**0° CCW: unverified** — `in_game_visible_travel-abb9d42e6ab5a4275279`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Rout; entry: Sin; exit: Rout.

No observation recorded.

<a id="case-in_game_visible_travel-0da4374c45481e6e306e"></a>

**90° CCW: unverified** — `in_game_visible_travel-0da4374c45481e6e306e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Rout; entry: Sin; exit: Rout.

No observation recorded.

<a id="case-in_game_visible_travel-9cdb0e38746c7f11a766"></a>

**180° CCW: unverified** — `in_game_visible_travel-9cdb0e38746c7f11a766`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Rout; entry: Sin; exit: Rout.

No observation recorded.

<a id="case-in_game_visible_travel-63f9dff6f384ed46d433"></a>

**270° CCW: unverified** — `in_game_visible_travel-63f9dff6f384ed46d433`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Rout; entry: Sin; exit: Rout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 20 cases; unverified: 20</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Lin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cebd07ace4c23e3b0b40">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6af57208b707bbb8e7c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f2c013174b190ad8b2e5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-64e5d198fa7cc0119c64">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Lin; to port: Rout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9cc44127a3b0a3f352f1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-af3a0f5fb09ced1d69f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c82342e14491e73e5037">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bbeb843b0c323e9069db">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0d1db4aa8702d16edfa7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-20e86055ec33ded7deac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-005550f717d3e9b45afb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-47ced1859cc3164352a1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Nin; to port: Rout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b1c116c697c9ef2bdbe6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7424b989a88c17338451">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b2fc295f6a8a69b769cd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9373805b37c05012014b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0f95ab42ea20b9fade96">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-97dbc0b5c378dc5ed20f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8f2892e0d17c7c4dcfbd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-86fde97704dd30bcc3b3">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Lin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cebd07ace4c23e3b0b40"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cebd07ace4c23e3b0b40`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Lin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6af57208b707bbb8e7c9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6af57208b707bbb8e7c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Lin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f2c013174b190ad8b2e5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f2c013174b190ad8b2e5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Lin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-64e5d198fa7cc0119c64"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-64e5d198fa7cc0119c64`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Lin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Lin; to port: Rout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9cc44127a3b0a3f352f1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9cc44127a3b0a3f352f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Lin; to port: Rout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-af3a0f5fb09ced1d69f8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-af3a0f5fb09ced1d69f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Lin; to port: Rout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c82342e14491e73e5037"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c82342e14491e73e5037`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Lin; to port: Rout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bbeb843b0c323e9069db"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bbeb843b0c323e9069db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Lin; to port: Rout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0d1db4aa8702d16edfa7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0d1db4aa8702d16edfa7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-20e86055ec33ded7deac"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-20e86055ec33ded7deac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-005550f717d3e9b45afb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-005550f717d3e9b45afb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-47ced1859cc3164352a1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-47ced1859cc3164352a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Nin; to port: Rout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b1c116c697c9ef2bdbe6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b1c116c697c9ef2bdbe6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Rout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7424b989a88c17338451"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7424b989a88c17338451`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Rout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b2fc295f6a8a69b769cd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b2fc295f6a8a69b769cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Rout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9373805b37c05012014b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9373805b37c05012014b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Rout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0f95ab42ea20b9fade96"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0f95ab42ea20b9fade96`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-97dbc0b5c378dc5ed20f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-97dbc0b5c378dc5ed20f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8f2892e0d17c7c4dcfbd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8f2892e0d17c7c4dcfbd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-86fde97704dd30bcc3b3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-86fde97704dd30bcc3b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
