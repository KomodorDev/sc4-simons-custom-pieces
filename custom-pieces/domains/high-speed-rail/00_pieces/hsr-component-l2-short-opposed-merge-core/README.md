# HSR L2 Short Opposed Merge Core

<!-- PIECE README LAYOUT: 1 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [4. Testing](#4-testing)

This reusable High Speed Rail (HSR) junction carries a paired mainline and receives two directed curved branches. The mainline and branch traffic remain at nominal Level 2 (L2), with a train-path height of 15.5 m. A placed copy is one component; a complete interchange needs additional pieces.

**Status: experimental.** Human image approval and operation inside SimCity 4 require their own recorded observations. The permanent type ID is `hsr-component-l2-short-opposed-merge-core`; its existing game-resource identifiers are retained. This guide describes the reusable type independently of any assembly placement label.

## 1. Views

Both clean pictures show the same complete saved model at the authored 0° orientation. North is up in the top view; X increases eastward, Y increases northward, and each city tile measures 16 × 16 m. The standalone grid belongs to this piece. It does not use an interchange's placement positions or rotations.

<!-- BEGIN PIECE VIEWS -->

![HSR L2 Short Opposed Merge Core — Clean angled view](previews/preview.png)

![HSR L2 Short Opposed Merge Core — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

The generated connection overview in chapter 3 identifies complete joining boundaries and their required channels. Its cards report the measured facts for the saved model. Software pictures show geometry and selected textures; they do not establish game appearance or train operation.

## 2. Piece and placement

<!-- BEGIN PIECE OVERVIEW -->

Flat native L2 mainline with opposed one-way merges; the northern merge shares the retained Short Mainline Diverge Core branch angle, while the southern direct-slip route remains unchanged.

Exact reusable identifier: `hsr-component-l2-short-opposed-merge-core`.

Footprint: **5 × 1 tiles**. Exact menu name: **HSR L2 Short Opposed Merge Core**.

<!-- END PIECE OVERVIEW -->

### Function and complete joining boundaries

The two ordinary mainline ends continue paired HSR, while the directed branch entrances merge into their declared mainline directions. The current fan-facing branch is reworked to share the branch-angle policy of the paired fan and existing Short Mainline Diverge Core. The complete permitted entrance-to-exit movements come from the actual saved traffic resources, shown in the generated matrix below.

A joining boundary is the complete tile edge where this piece meets its neighbour. Both directions of the paired mainline need the matching paired profile. The curved branch entrances have specific positions, headings, physical deck shapes, and train-clearance requirements; matching only the 15.5 m height does not establish a valid join. The library does not supply automatic compatibility discovery.

The permanent construction definition is [piece.json](piece.json), and the authoring geometry is [geometry.json](geometry.json). Source cells use [column, row], with columns increasing eastward and rows increasing southward; the picture's Y axis increases northward. Use the generated coordinate conversion rather than reading a source row as a picture Y label.

Use the occupied-cell and structural-cell definitions in piece.json to understand the footprint. Keep the full construction rectangle clear for the first trial, and align the whole model rather than assuming that a software reference coordinate is a certified mouse-click anchor.

### Place and rotate the piece

After following the [separate build and installation procedure](../../../../docs/BUILD_AND_INSTALL.md), use a disposable flat test city. A proper rotation turns the entire component and all its travel directions together; it does not reflect the component or reverse a one-way route.

1. Open **Transportation → Rail**, hover over the SCP buttons, and select **HSR L2 Short Opposed Merge Core**. An installed assembly may instead include this same type within its declared Tab/Shift+Tab cycle.
2. Move the cursor preview over clear terrain. Press **Home** or **End** to rotate the whole piece; on the documented Mac keyboard, **Fn + ←** and **Fn + →** provide those keys. Use only the supported construction states listed in the generated connection section.
3. At 0°, identify the paired mainline ends and both branch entrances in the top picture. Align the complete cursor preview so that every required channel agrees with its neighbour; a curved branch needs its matching continuation.
4. Click once to place the component. Supply matching outside connections and travel demand. Inspect the rails, decks, walls, supports, and shadows, then test the permitted journeys and forbidden movements separately.

The [trumpet blueprint](../../01_assemblies/straight-stem-trumpet/README.md) is one documented use of this type. Its assembly position, neighbours, and end-to-end evidence do not approve every other use of this reusable piece.

## 3. Connection matrix

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](#case-in_game_render-5fa20a2de78ef24ee969) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](#test-checklist).

| Entrance ↓ / Exit → | **HSR · West exit**<br>`Wout` | **HSR · East exit**<br>`Eout` |
| --- | --- | --- |
| **HSR · West entrance**<br>`Win` | **Forbidden**<br>**Saved PATH:** [✅](#case-software_connectivity-bb298338ce132e94abe3)<br>In-game check: [?](#case-in_game_forbidden_transfer-207270803a527230f629) | **Saved PATH:** [✅](#case-software_connectivity-bb298338ce132e94abe3)<br>**Route Query:** [?](#case-in_game_route_query-893c5139b52951b645b6)<br>**Visible train travel:** [?](#case-in_game_visible_travel-893c5139b52951b645b6) |
| **HSR · South entrance**<br>`Sin` | **Forbidden**<br>**Saved PATH:** [✅](#case-software_connectivity-bb298338ce132e94abe3)<br>In-game check: [?](#case-in_game_forbidden_transfer-7dd99ef9226dd9ae5cc2) | **Saved PATH:** [✅](#case-software_connectivity-bb298338ce132e94abe3)<br>**Route Query:** [?](#case-in_game_route_query-4f0cf575be97d46acd86)<br>**Visible train travel:** [?](#case-in_game_visible_travel-4f0cf575be97d46acd86) |
| **HSR · North entrance**<br>`Nin` | **Saved PATH:** [✅](#case-software_connectivity-bb298338ce132e94abe3)<br>**Route Query:** [?](#case-in_game_route_query-60ecb293929e38cf3d1f)<br>**Visible train travel:** [?](#case-in_game_visible_travel-60ecb293929e38cf3d1f) | **Forbidden**<br>**Saved PATH:** [✅](#case-software_connectivity-bb298338ce132e94abe3)<br>In-game check: [?](#case-in_game_forbidden_transfer-a430fa085cdc293296ca) |
| **HSR · East entrance**<br>`Ein` | **Saved PATH:** [✅](#case-software_connectivity-bb298338ce132e94abe3)<br>**Route Query:** [?](#case-in_game_route_query-207ef3949b9f1fa27c42)<br>**Visible train travel:** [?](#case-in_game_visible_travel-207ef3949b9f1fa27c42) | **Forbidden**<br>**Saved PATH:** [✅](#case-software_connectivity-bb298338ce132e94abe3)<br>In-game check: [?](#case-in_game_forbidden_transfer-5c49c60a8ee59fd1e7fb) |

Source: [connections.json](connections.json).

<!-- END PIECE CONNECTION MATRIX -->

<!-- BEGIN CONNECTOR OVERVIEW -->

### Connection overview

Generated from this piece's source-bound connector metadata and the current compiled model; marker letters refer to the boundary cards below.

![Complete connection overview](previews/connection-overview.png)

[Rendering sources and verification scope](evidence/connection-overview.json).

Headings: 0° = North, 90° = East, 180° = South, and 270° = West; clockwise in plan view, pointing out of the piece.

Coordinates [E,N,H] = [east,north,height] in metres. Source cells [column,row] increase east and south.

Display grid: X = source column − (0); Y = 0 − source row.

Slope is measured outward at the joining edge; the interior may differ. Offsets are + left and − right facing out of the tile edge.

Member offsets use the section origin. Counts distinguish physical channels / edge cuts / directed members; modes do not multiply channels.

Incoming flow enters this piece; outgoing flow leaves it. Letters identify boundary cards; source IDs remain the stable identities.

Not declared means no section origin or offset was authored. Its marker uses an actual member endpoint; the measured intersections remain authoritative.

#### Boundary A: `cell-0-0-west`

This service group is required at this edge.

##### Service group 1 / 1: HSR — Level 2 (15.5 m)

| Field | Value |
| --- | --- |
| End / component | `west-paired-end` / `opposed-merge` |
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
| `west-paired-end-win` / `Win` | `eastbound-mainline` / `west-paired-end-eastbound-mainline-cut` / monorail | Incoming | `[-8,-2,15.5]` | +2 | 270° | 0 |
| `west-paired-end-wout` / `Wout` | `westbound-mainline` / `west-paired-end-westbound-mainline-cut` / monorail | Outgoing | `[-8,2,15.5]` | -2 | 270° | 0 |

#### Boundary B: `cell-2-0-south`

This service group is required at this edge.

##### Service group 1 / 1: HSR — Level 2 (15.5 m)

| Field | Value |
| --- | --- |
| End / component | `south-curved-cut` / `opposed-merge` |
| Network / game class / role | hsr / Monorail (7); primary |
| Source cell / edge | `[2,0]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Level 2 (15.5 m) |
| Outward heading | 248.011° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | rail |
| Traffic modes | monorail |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `south-curved-cut-sin` / `Sin` | `south-branch` / `south-curved-cut-south-branch-cut` / monorail | Incoming | `[25.6015,-8,15.5]` | Not declared | 248.011° | 0 |

#### Boundary C: `cell-3-0-north`

This service group is required at this edge.

##### Service group 1 / 1: HSR — Level 2 (15.5 m)

| Field | Value |
| --- | --- |
| End / component | `north-curved-cut` / `opposed-merge` |
| Network / game class / role | hsr / Monorail (7); primary |
| Source cell / edge | `[3,0]` / North |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Level 2 (15.5 m) |
| Outward heading | 68.0109° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | rail |
| Traffic modes | monorail |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `north-curved-cut-nin` / `Nin` | `north-branch` / `north-curved-cut-north-branch-cut` / monorail | Incoming | `[54.3985,8,15.5]` | Not declared | 68.0109° | 0 |

#### Boundary D: `cell-4-0-east`

This service group is required at this edge.

##### Service group 1 / 1: HSR — Level 2 (15.5 m)

| Field | Value |
| --- | --- |
| End / component | `east-paired-end` / `opposed-merge` |
| Network / game class / role | hsr / Monorail (7); primary |
| Source cell / edge | `[4,0]` / East |
| Section origin [E,N] (m) | `[72,0]` |
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
| `east-paired-end-ein` / `Ein` | `westbound-mainline` / `east-paired-end-westbound-mainline-cut` / monorail | Incoming | `[72,2,15.5]` | +2 | 90° | 0 |
| `east-paired-end-eout` / `Eout` | `eastbound-mainline` / `east-paired-end-eastbound-mainline-cut` / monorail | Outgoing | `[72,-2,15.5]` | -2 | 90° | 0 |

Rendering checks source metadata, current compiled resource identities, and model structure. It does not re-extract PATHs or evaluate placement; physical seams, construction clearance, collisions, and game operation remain unverified.

<!-- END CONNECTOR OVERVIEW -->

## 4. Testing

A case is one exact check under stated conditions. Software resource validation, human preview review, game appearance, Route Query, and visible train travel are separate observations. A Route Query line does not prove that a train visibly completed the journey; a software build does not approve either game observation.

Follow the [shared observation procedure](../../../../docs/TESTING.md#record-one-observation) using this piece's [authoritative manual record](checks/manual-tests.json). Record the direction, rotation, platform, game version, NAM profile, and actual evidence for each game result. Only explicit human confirmation records a manual pass. Keep failures, stale results, and historical observations with their original scope.

The generated sections below supply the exact saved-resource interfaces, supported states, current checklist, and recording command. They do not establish compatibility with an arbitrary neighbour.

### Engineering sources and limits

The construction rectangle contains **5 × 1 tiles**, and all **five cells** are owned. Five supports remain centred along the mainline at 16 m intervals. Both paired mainline ends are ordinary, flat L2 boundaries; the northern and southern branch entrances are custom oblique cuts.

The northern merge reuses the Short Mainline Diverge Core’s branch samples after reflecting the north/south coordinate and reversing travel. Both mainline routes, the direct southern route fragments, and each analytic context’s southern deck retain their earlier source values. The branch tracks are separate physical channels until their measured internal journeys merge into the appropriate mainline track; assigning them one component does not permit extra transfers.

The [geometry source](geometry.json) owns route samples, physical sweeps, selected cells, and support positions. Independent software contracts inspect encoded endpoints, direction, L2 height, route continuity, curvature, bed coverage, visible rail alignment, supports, and model budgets. These checks do not approve arbitrary neighbours, terrain behaviour, game appearance, or train operation. The generated matrix and checklist retain the scope and current state of each measured or observed result.

Actual saved-resource software checks are recorded in [the current resource-check report](evidence/saved-resource-checks.json). Current canonical picture provenance belongs in [angled-view evidence](evidence/preview.json), [top-view evidence](evidence/preview-top.json), and [connection-overview evidence](evidence/connection-overview.json). The [earlier combined preview report](evidence/design-history/preview-before-junction-rework.json) is preserved as historical evidence for the geometry before this redesign. It does not describe the current pictures.

### Reproduce this piece’s software checks

Run these commands from the repository root, the folder containing `custom-pieces/`, after completing the [shared dependency and native-input preparation](../../../../docs/BUILD_AND_INSTALL.md). Replace `/path/to/Plugins` with the existing NAM Plugins directory, and keep the quotation marks if its path contains spaces. Use a new output directory so an earlier build remains available for comparison.

```sh
python3 -B custom-pieces/scp.py build --include hsr-component-l2-short-opposed-merge-core --output custom-pieces/dist/hsr-l2-opposed-merge-review --plugins '/path/to/Plugins'
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/hsr-l2-opposed-merge-review
```

Building writes a local development build; verification inspects its saved resources. Neither command installs files or records a game pass. After changing actual resources, follow the [documented extraction, connector, and picture refresh sequence](../../../../docs/WORKFLOW_DOCUMENTATION_GENERATION.md#before-refreshing) for this exact type before using regenerated documentation.

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
| `Win` | hsr / 7 / primary | in | [-8.0, -2.0, 15.5]; [1.0, 0.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Wout` | hsr / 7 / primary | out | [-8.0, 2.0, 15.5]; [-1.0, 0.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Sin` | hsr / 7 / primary | in | [25.601481, -8.0, 15.5]; [0.9272548089646255, 0.3744309272108488]; 0.0 | `path-interface-0f4b8204e68941486c48` |
| `Nin` | hsr / 7 / primary | in | [54.398519, 8.0, 15.5]; [-0.9272548089646255, -0.3744309272108488]; 0.0 | `path-interface-0f4b8204e68941486c48` |
| `Eout` | hsr / 7 / primary | out | [72.0, -2.0, 15.5]; [1.0, 0.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Ein` | hsr / 7 / primary | in | [72.0, 2.0, 15.5]; [-1.0, 0.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Win` → `Eout` | primary |
| hsr | `Sin` → `Eout` | primary |
| hsr | `Nin` → `Wout` | primary |
| hsr | `Ein` → `Wout` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| hsr / `Win` | hsr / `Wout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Sin` | hsr / `Wout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Nin` | hsr / `Eout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Ein` | hsr / `Eout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 67, passed: 2, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-l2-short-opposed-merge-core/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-l2-short-opposed-merge-core/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-bb298338ce132e94abe3">[x] passed</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-bb298338ce132e94abe3"></a>

**General: passed** — `software_resources-bb298338ce132e94abe3`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: verify_hsr_trumpet_v4.py plus independent staged build resource checks; confirmed at: 2026-10-20T10:42:34.956270+00:00; evidence: [../../01_assemblies/straight-stem-trumpet-v4/evidence/validation.json]; environment: {}
- result: passed; authority: software; reviewer: Normal saved-build verifier with independent atomic opposed-merge PATH and model contracts; confirmed at: 2026-10-27T18:29:44.936700+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}
- result: passed; authority: software; reviewer: Normal saved-build verifier with independent atomic opposed-merge PATH and model contracts; confirmed at: 2026-10-27T18:41:49.788201+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}
- result: passed; authority: software; reviewer: Actual final normal 13-piece saved-build verification; registered independent PATH, model, construction, menu, and shadow checks; confirmed at: 2026-10-27T21:57:25.376326+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-bb298338ce132e94abe3">[x] passed</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-bb298338ce132e94abe3"></a>

**General: passed** — `software_connectivity-bb298338ce132e94abe3`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: verify_hsr_trumpet_v4.py plus independent staged build resource checks; confirmed at: 2026-10-20T10:42:34.964878+00:00; evidence: [../../01_assemblies/straight-stem-trumpet-v4/evidence/validation.json]; environment: {}
- result: passed; authority: software; reviewer: Normal saved-build verifier with independent atomic opposed-merge PATH and model contracts; confirmed at: 2026-10-27T18:29:44.936700+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}
- result: passed; authority: software; reviewer: Normal saved-build verifier with independent atomic opposed-merge PATH and model contracts; confirmed at: 2026-10-27T18:41:49.788201+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}
- result: passed; authority: software; reviewer: Actual final normal 13-piece saved-build verification; registered independent PATH, model, construction, menu, and shadow checks; confirmed at: 2026-10-27T21:57:25.376326+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:hsr-component-l2-short-opposed-merge-core:canonical-southeast | <a href="#case-preview_review-82efb43975086d8a2c0f">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-l2-short-opposed-merge-core:canonical-top | <a href="#case-preview_review-7b1a76173037cf9da141">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-l2-short-opposed-merge-core:connection-overview | <a href="#case-preview_review-348a0bea35fd99141ff0">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:hsr-component-l2-short-opposed-merge-core:canonical-southeast</summary>

<a id="case-preview_review-82efb43975086d8a2c0f"></a>

**General: unverified** — `preview_review-82efb43975086d8a2c0f`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:hsr-component-l2-short-opposed-merge-core:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-l2-short-opposed-merge-core:canonical-top</summary>

<a id="case-preview_review-7b1a76173037cf9da141"></a>

**General: unverified** — `preview_review-7b1a76173037cf9da141`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:hsr-component-l2-short-opposed-merge-core:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-l2-short-opposed-merge-core:connection-overview</summary>

<a id="case-preview_review-348a0bea35fd99141ff0"></a>

**General: unverified** — `preview_review-348a0bea35fd99141ff0`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:hsr-component-l2-short-opposed-merge-core:connection-overview.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-5fa20a2de78ef24ee969">[ ] unverified</a> | <a href="#case-in_game_render-44036cf5ca9c219e69b6">[ ] unverified</a> | <a href="#case-in_game_render-e0bbb6e7f63828f7273a">[ ] unverified</a> | <a href="#case-in_game_render-64d5cec7500a6a74eb63">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-5fa20a2de78ef24ee969"></a>

**0° CCW: unverified** — `in_game_render-5fa20a2de78ef24ee969`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-44036cf5ca9c219e69b6"></a>

**90° CCW: unverified** — `in_game_render-44036cf5ca9c219e69b6`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-e0bbb6e7f63828f7273a"></a>

**180° CCW: unverified** — `in_game_render-e0bbb6e7f63828f7273a`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-64d5cec7500a6a74eb63"></a>

**270° CCW: unverified** — `in_game_render-64d5cec7500a6a74eb63`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-5fa20a2de78ef24ee969">[ ] unverified</a> | <a href="#case-in_game_placement-44036cf5ca9c219e69b6">[ ] unverified</a> | <a href="#case-in_game_placement-e0bbb6e7f63828f7273a">[ ] unverified</a> | <a href="#case-in_game_placement-64d5cec7500a6a74eb63">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-5fa20a2de78ef24ee969"></a>

**0° CCW: unverified** — `in_game_placement-5fa20a2de78ef24ee969`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-44036cf5ca9c219e69b6"></a>

**90° CCW: unverified** — `in_game_placement-44036cf5ca9c219e69b6`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-e0bbb6e7f63828f7273a"></a>

**180° CCW: unverified** — `in_game_placement-e0bbb6e7f63828f7273a`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-64d5cec7500a6a74eb63"></a>

**270° CCW: unverified** — `in_game_placement-64d5cec7500a6a74eb63`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-5fa20a2de78ef24ee969">[ ] unverified</a> | <a href="#case-in_game_demolition-44036cf5ca9c219e69b6">[ ] unverified</a> | <a href="#case-in_game_demolition-e0bbb6e7f63828f7273a">[ ] unverified</a> | <a href="#case-in_game_demolition-64d5cec7500a6a74eb63">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-5fa20a2de78ef24ee969"></a>

**0° CCW: unverified** — `in_game_demolition-5fa20a2de78ef24ee969`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-44036cf5ca9c219e69b6"></a>

**90° CCW: unverified** — `in_game_demolition-44036cf5ca9c219e69b6`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-e0bbb6e7f63828f7273a"></a>

**180° CCW: unverified** — `in_game_demolition-e0bbb6e7f63828f7273a`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-64d5cec7500a6a74eb63"></a>

**270° CCW: unverified** — `in_game_demolition-64d5cec7500a6a74eb63`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-5fa20a2de78ef24ee969">[ ] unverified</a> | <a href="#case-in_game_save_reload-44036cf5ca9c219e69b6">[ ] unverified</a> | <a href="#case-in_game_save_reload-e0bbb6e7f63828f7273a">[ ] unverified</a> | <a href="#case-in_game_save_reload-64d5cec7500a6a74eb63">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-5fa20a2de78ef24ee969"></a>

**0° CCW: unverified** — `in_game_save_reload-5fa20a2de78ef24ee969`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-44036cf5ca9c219e69b6"></a>

**90° CCW: unverified** — `in_game_save_reload-44036cf5ca9c219e69b6`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-e0bbb6e7f63828f7273a"></a>

**180° CCW: unverified** — `in_game_save_reload-e0bbb6e7f63828f7273a`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-64d5cec7500a6a74eb63"></a>

**270° CCW: unverified** — `in_game_save_reload-64d5cec7500a6a74eb63`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — hsr — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout | — | <a href="#case-in_game_route_query-893c5139b52951b645b6">[ ] unverified</a> | <a href="#case-in_game_route_query-12f69b3b913acae8201d">[ ] unverified</a> | <a href="#case-in_game_route_query-f3b3573e8f7ace23cff4">[ ] unverified</a> | <a href="#case-in_game_route_query-f8e53ac8ceee4f799d4b">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout | — | <a href="#case-in_game_route_query-4f0cf575be97d46acd86">[ ] unverified</a> | <a href="#case-in_game_route_query-19c54ca56f8042daf844">[ ] unverified</a> | <a href="#case-in_game_route_query-7d3a33b068031438fb81">[ ] unverified</a> | <a href="#case-in_game_route_query-bc99ac36a202cb86cb74">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout | — | <a href="#case-in_game_route_query-60ecb293929e38cf3d1f">[ ] unverified</a> | <a href="#case-in_game_route_query-6cc0dfabda71d80528f1">[ ] unverified</a> | <a href="#case-in_game_route_query-603647f229b7499b2763">[ ] unverified</a> | <a href="#case-in_game_route_query-5edf5624208c8e5ae91e">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout | — | <a href="#case-in_game_route_query-207ef3949b9f1fa27c42">[ ] unverified</a> | <a href="#case-in_game_route_query-0b0d18e5a4ca71cf43fe">[ ] unverified</a> | <a href="#case-in_game_route_query-3ef4c192a77b513915a5">[ ] unverified</a> | <a href="#case-in_game_route_query-1925b8fbd5168e2e637d">[ ] unverified</a> |


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout</summary>

<a id="case-in_game_route_query-893c5139b52951b645b6"></a>

**0° CCW: unverified** — `in_game_route_query-893c5139b52951b645b6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_route_query-12f69b3b913acae8201d"></a>

**90° CCW: unverified** — `in_game_route_query-12f69b3b913acae8201d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_route_query-f3b3573e8f7ace23cff4"></a>

**180° CCW: unverified** — `in_game_route_query-f3b3573e8f7ace23cff4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_route_query-f8e53ac8ceee4f799d4b"></a>

**270° CCW: unverified** — `in_game_route_query-f8e53ac8ceee4f799d4b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout</summary>

<a id="case-in_game_route_query-4f0cf575be97d46acd86"></a>

**0° CCW: unverified** — `in_game_route_query-4f0cf575be97d46acd86`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_route_query-19c54ca56f8042daf844"></a>

**90° CCW: unverified** — `in_game_route_query-19c54ca56f8042daf844`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_route_query-7d3a33b068031438fb81"></a>

**180° CCW: unverified** — `in_game_route_query-7d3a33b068031438fb81`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_route_query-bc99ac36a202cb86cb74"></a>

**270° CCW: unverified** — `in_game_route_query-bc99ac36a202cb86cb74`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout</summary>

<a id="case-in_game_route_query-60ecb293929e38cf3d1f"></a>

**0° CCW: unverified** — `in_game_route_query-60ecb293929e38cf3d1f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_route_query-6cc0dfabda71d80528f1"></a>

**90° CCW: unverified** — `in_game_route_query-6cc0dfabda71d80528f1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_route_query-603647f229b7499b2763"></a>

**180° CCW: unverified** — `in_game_route_query-603647f229b7499b2763`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_route_query-5edf5624208c8e5ae91e"></a>

**270° CCW: unverified** — `in_game_route_query-5edf5624208c8e5ae91e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout</summary>

<a id="case-in_game_route_query-207ef3949b9f1fa27c42"></a>

**0° CCW: unverified** — `in_game_route_query-207ef3949b9f1fa27c42`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_route_query-0b0d18e5a4ca71cf43fe"></a>

**90° CCW: unverified** — `in_game_route_query-0b0d18e5a4ca71cf43fe`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_route_query-3ef4c192a77b513915a5"></a>

**180° CCW: unverified** — `in_game_route_query-3ef4c192a77b513915a5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_route_query-1925b8fbd5168e2e637d"></a>

**270° CCW: unverified** — `in_game_route_query-1925b8fbd5168e2e637d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — hsr — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout | — | <a href="#case-in_game_visible_travel-893c5139b52951b645b6">[ ] unverified</a> | <a href="#case-in_game_visible_travel-12f69b3b913acae8201d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f3b3573e8f7ace23cff4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f8e53ac8ceee4f799d4b">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout | — | <a href="#case-in_game_visible_travel-4f0cf575be97d46acd86">[ ] unverified</a> | <a href="#case-in_game_visible_travel-19c54ca56f8042daf844">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7d3a33b068031438fb81">[ ] unverified</a> | <a href="#case-in_game_visible_travel-bc99ac36a202cb86cb74">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout | — | <a href="#case-in_game_visible_travel-60ecb293929e38cf3d1f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6cc0dfabda71d80528f1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-603647f229b7499b2763">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5edf5624208c8e5ae91e">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout | — | <a href="#case-in_game_visible_travel-207ef3949b9f1fa27c42">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0b0d18e5a4ca71cf43fe">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3ef4c192a77b513915a5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1925b8fbd5168e2e637d">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout</summary>

<a id="case-in_game_visible_travel-893c5139b52951b645b6"></a>

**0° CCW: unverified** — `in_game_visible_travel-893c5139b52951b645b6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_visible_travel-12f69b3b913acae8201d"></a>

**90° CCW: unverified** — `in_game_visible_travel-12f69b3b913acae8201d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_visible_travel-f3b3573e8f7ace23cff4"></a>

**180° CCW: unverified** — `in_game_visible_travel-f3b3573e8f7ace23cff4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_visible_travel-f8e53ac8ceee4f799d4b"></a>

**270° CCW: unverified** — `in_game_visible_travel-f8e53ac8ceee4f799d4b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout</summary>

<a id="case-in_game_visible_travel-4f0cf575be97d46acd86"></a>

**0° CCW: unverified** — `in_game_visible_travel-4f0cf575be97d46acd86`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_visible_travel-19c54ca56f8042daf844"></a>

**90° CCW: unverified** — `in_game_visible_travel-19c54ca56f8042daf844`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_visible_travel-7d3a33b068031438fb81"></a>

**180° CCW: unverified** — `in_game_visible_travel-7d3a33b068031438fb81`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_visible_travel-bc99ac36a202cb86cb74"></a>

**270° CCW: unverified** — `in_game_visible_travel-bc99ac36a202cb86cb74`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout</summary>

<a id="case-in_game_visible_travel-60ecb293929e38cf3d1f"></a>

**0° CCW: unverified** — `in_game_visible_travel-60ecb293929e38cf3d1f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_visible_travel-6cc0dfabda71d80528f1"></a>

**90° CCW: unverified** — `in_game_visible_travel-6cc0dfabda71d80528f1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_visible_travel-603647f229b7499b2763"></a>

**180° CCW: unverified** — `in_game_visible_travel-603647f229b7499b2763`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_visible_travel-5edf5624208c8e5ae91e"></a>

**270° CCW: unverified** — `in_game_visible_travel-5edf5624208c8e5ae91e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout</summary>

<a id="case-in_game_visible_travel-207ef3949b9f1fa27c42"></a>

**0° CCW: unverified** — `in_game_visible_travel-207ef3949b9f1fa27c42`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_visible_travel-0b0d18e5a4ca71cf43fe"></a>

**90° CCW: unverified** — `in_game_visible_travel-0b0d18e5a4ca71cf43fe`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_visible_travel-3ef4c192a77b513915a5"></a>

**180° CCW: unverified** — `in_game_visible_travel-3ef4c192a77b513915a5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_visible_travel-1925b8fbd5168e2e637d"></a>

**270° CCW: unverified** — `in_game_visible_travel-1925b8fbd5168e2e637d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-207270803a527230f629">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c1fed664bf7e79661bb7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4901a3adbd023156c295">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0bd4ea3cffdeb32f0a21">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Sin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7dd99ef9226dd9ae5cc2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ace301d7d331012dfac3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6da1e63af5bcd9339cee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-56a3d4e78c3526c29ef4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Nin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a430fa085cdc293296ca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-598f3f16a8f1a7e76b1b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-217ae4d152ecfd03acbb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a96f320a3615ec1876f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5c49c60a8ee59fd1e7fb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c5d8a576cb782858ec32">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d91ca221aae8c94f0245">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6546640b65f44fc33f06">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-207270803a527230f629"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-207270803a527230f629`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c1fed664bf7e79661bb7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c1fed664bf7e79661bb7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4901a3adbd023156c295"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4901a3adbd023156c295`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0bd4ea3cffdeb32f0a21"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0bd4ea3cffdeb32f0a21`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Sin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7dd99ef9226dd9ae5cc2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7dd99ef9226dd9ae5cc2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ace301d7d331012dfac3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ace301d7d331012dfac3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6da1e63af5bcd9339cee"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6da1e63af5bcd9339cee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-56a3d4e78c3526c29ef4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-56a3d4e78c3526c29ef4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Nin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a430fa085cdc293296ca"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a430fa085cdc293296ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-598f3f16a8f1a7e76b1b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-598f3f16a8f1a7e76b1b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-217ae4d152ecfd03acbb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-217ae4d152ecfd03acbb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a96f320a3615ec1876f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7a96f320a3615ec1876f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5c49c60a8ee59fd1e7fb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5c49c60a8ee59fd1e7fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c5d8a576cb782858ec32"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c5d8a576cb782858ec32`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d91ca221aae8c94f0245"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d91ca221aae8c94f0245`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6546640b65f44fc33f06"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6546640b65f44fc33f06`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
