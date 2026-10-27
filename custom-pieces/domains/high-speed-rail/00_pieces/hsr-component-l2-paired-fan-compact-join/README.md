# HSR L2 Compact Paired Fan Join

<!-- PIECE README LAYOUT: 1 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [4. Testing](#4-testing)

This reusable High Speed Rail (HSR) piece connects one north-facing pair of tracks to two curved branch ends. At the authored 0° orientation, traffic entering from the north leaves through the western branch; traffic entering from the eastern branch continues north. Both directions remain at nominal Level 2 (L2), with a train-path height of 15.5 m.

**Status: experimental.** Human image approval and operation inside SimCity 4 require their own recorded observations. The permanent type ID is `hsr-component-l2-paired-fan-compact-join`; its existing game-resource identifiers are retained. This guide describes the reusable type independently of any assembly placement label.

## 1. Views

Both clean pictures show the same complete saved model at the authored 0° orientation. North is up in the top view; X increases eastward, Y increases northward, and each city tile measures 16 × 16 m. The standalone grid belongs to this piece. It does not use an interchange's placement positions or rotations.

<!-- BEGIN PIECE VIEWS -->

![HSR L2 Compact Paired Fan Join — Clean angled view](previews/preview.png)

![HSR L2 Compact Paired Fan Join — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

The generated connection overview in chapter 3 identifies complete joining boundaries and their required channels. Its cards report the measured facts for the saved model. Software pictures show geometry and selected textures; they do not establish game appearance or train operation.

## 2. Piece and placement

<!-- BEGIN PIECE OVERVIEW -->

Two opposite-direction flat L2 fan arms join the native paired north mouth to matched oblique mainline branches, using the Short Mainline Diverge Core angles and six explicitly owned supports.

Exact reusable identifier: `hsr-component-l2-paired-fan-compact-join`.

Footprint: **7 × 5 tiles**. Exact menu name: **HSR L2 Compact Paired Fan Join**.

<!-- END PIECE OVERVIEW -->

### Function and complete joining boundaries

The fan separates the two directions of paired HSR into their respective curved connections. Its two branch routes do not transfer into each other. The current branch angles are designed together with the adjoining opposed merge and the existing Short Mainline Diverge Core; the exact saved-resource endpoints and permitted movements belong in the generated sections below.

The north-facing boundary carries both directions of ordinary paired L2 HSR. Each curved branch has its own directed connection, whose position, heading, deck, walls, and train clearance must all match its neighbour. A shared height alone does not establish a complete join. The library does not supply automatic compatibility discovery.

The paired structure remains **15 m wide** through the straight approach and the start of the fork. The shoulder taper now begins 48 m along each authored sweep and ends at 72 m, after the tracks have begun separating. This removes the earlier unexplained narrowing without changing the train paths, track radii, visible rails, joining cuts, or six supports. The [saved-model width audit](evidence/fan-width-audit.json) records cross-sections, exact rail identity, and unchanged PATH resources.

The permanent construction definition is [piece.json](piece.json), and the authoring geometry is [geometry.json](geometry.json). Source cells use [column, row], with columns increasing eastward and rows increasing southward; the picture's Y axis increases northward. Use the generated coordinate conversion rather than reading a source row as a picture Y label.

Keep the complete construction rectangle clear, including cells without a visible train route. This is a sparse piece: an apparently empty cell can be its software construction reference, and that reference has not been confirmed as the game's mouse-click anchor.

### Place and rotate the piece

After following the [separate build and installation procedure](../../../../docs/BUILD_AND_INSTALL.md), use a disposable flat test city. A proper rotation turns the entire component and all its travel directions together; it does not reflect the component or reverse a one-way route.

1. Open **Transportation → Rail**, hover over the SCP buttons, and select **HSR L2 Compact Paired Fan Join**. An installed assembly may instead include this same type within its declared Tab/Shift+Tab cycle.
2. Move the cursor preview over clear terrain. Press **Home** or **End** to rotate the whole piece; on the documented Mac keyboard, **Fn + ←** and **Fn + →** provide those keys. Use only the supported construction states listed in the generated connection section.
3. At 0°, identify the north-facing paired end and the two curved branch ends in the top picture. Align the complete cursor preview with the intended joining boundaries; a normal cardinal straight cannot replace either custom curved branch.
4. Click once to place the component. Supply matching outside connections and travel demand. Inspect the rails, decks, walls, supports, and shadows, then test the permitted journeys and forbidden movements separately.

The [trumpet blueprint](../../01_assemblies/straight-stem-trumpet/README.md) is one documented use of this type. Its assembly position, neighbours, and end-to-end evidence do not approve every other use of this reusable piece.

## 3. Connection matrix

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](#case-in_game_render-2953a796038b1c66047b) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](#test-checklist).

| Entrance ↓ / Exit → | **HSR · South exit**<br>`Wout` | **HSR · North exit**<br>`Nout` |
| --- | --- | --- |
| **HSR · North entrance**<br>`Nin` | **Saved PATH:** [✅](#case-software_connectivity-bc65ebc1e8aece8c8a6d)<br>**Route Query:** [?](#case-in_game_route_query-efa01c69d3d0a595addc)<br>**Visible train travel:** [?](#case-in_game_visible_travel-efa01c69d3d0a595addc) | **Forbidden**<br>**Saved PATH:** [✅](#case-software_connectivity-bc65ebc1e8aece8c8a6d)<br>In-game check: [?](#case-in_game_forbidden_transfer-3ad08e7a19456cd90fd0) |
| **HSR · South entrance**<br>`Ein` | **Forbidden**<br>**Saved PATH:** [✅](#case-software_connectivity-bc65ebc1e8aece8c8a6d)<br>In-game check: [?](#case-in_game_forbidden_transfer-97aa23dd677c7b8c9e3c) | **Saved PATH:** [✅](#case-software_connectivity-bc65ebc1e8aece8c8a6d)<br>**Route Query:** [?](#case-in_game_route_query-65a9b6549c48f167a40e)<br>**Visible train travel:** [?](#case-in_game_visible_travel-65a9b6549c48f167a40e) |

Source: [connections.json](connections.json).

<!-- END PIECE CONNECTION MATRIX -->

<!-- BEGIN CONNECTOR OVERVIEW -->

### Connection overview

Generated from this piece's source-bound connector metadata and the current compiled model; marker letters refer to the boundary cards below.

![Complete connection overview](previews/connection-overview.png)

[Rendering sources and verification scope](evidence/connection-overview.json).

Headings: 0° = North, 90° = East, 180° = South, and 270° = West; clockwise in plan view, pointing out of the piece.

Coordinates [E,N,H] = [east,north,height] in metres. Source cells [column,row] increase east and south.

Display grid: X = source column − (1); Y = 4 − source row.

Slope is measured outward at the joining edge; the interior may differ. Offsets are + left and − right facing out of the tile edge.

Member offsets use the section origin. Counts distinguish physical channels / edge cuts / directed members; modes do not multiply channels.

Incoming flow enters this piece; outgoing flow leaves it. Letters identify boundary cards; source IDs remain the stable identities.

Not declared means no section origin or offset was authored. Its marker uses an actual member endpoint; the measured intersections remain authoritative.

#### Boundary A: `cell-1-4-south`

This service group is required at this edge.

##### Service group 1 / 1: HSR — Level 2 (15.5 m)

| Field | Value |
| --- | --- |
| End / component | `west-curved-cut` / `paired-fan` |
| Network / game class / role | hsr / Monorail (7); primary |
| Source cell / edge | `[1,4]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Level 2 (15.5 m) |
| Outward heading | 248.011° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | rail |
| Traffic modes | monorail |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `west-curved-cut-wout` / `Wout` | `north-to-west-track` / `west-curved-cut-north-to-west-track-cut` / monorail | Outgoing | `[22.3985,-72,15.5]` | Not declared | 248.011° | 0 |

#### Boundary B: `cell-3-0-north`

This service group is required at this edge.

##### Service group 1 / 1: HSR — Level 2 (15.5 m)

| Field | Value |
| --- | --- |
| End / component | `north-paired-end` / `paired-fan` |
| Network / game class / role | hsr / Monorail (7); primary |
| Source cell / edge | `[3,0]` / North |
| Section origin [E,N] (m) | `[48,8]` |
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
| `north-paired-end-nin` / `Nin` | `north-to-west-track` / `north-paired-end-north-to-west-track-cut` / monorail | Incoming | `[46,8,15.5]` | +2 | 0° | 0 |
| `north-paired-end-nout` / `Nout` | `east-to-north-track` / `north-paired-end-east-to-north-track-cut` / monorail | Outgoing | `[50,8,15.5]` | -2 | 0° | 0 |

#### Boundary C: `cell-5-4-south`

This service group is required at this edge.

##### Service group 1 / 1: HSR — Level 2 (15.5 m)

| Field | Value |
| --- | --- |
| End / component | `east-curved-cut` / `paired-fan` |
| Network / game class / role | hsr / Monorail (7); primary |
| Source cell / edge | `[5,4]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Level 2 (15.5 m) |
| Outward heading | 111.989° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | rail |
| Traffic modes | monorail |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `east-curved-cut-ein` / `Ein` | `east-to-north-track` / `east-curved-cut-east-to-north-track-cut` / monorail | Incoming | `[73.6015,-72,15.5]` | Not declared | 111.989° | 0 |

Rendering checks source metadata, current compiled resource identities, and model structure. It does not re-extract PATHs or evaluate placement; physical seams, construction clearance, collisions, and game operation remain unverified.

<!-- END CONNECTOR OVERVIEW -->

## 4. Testing

A case is one exact check under stated conditions. Software resource validation, human preview review, game appearance, Route Query, and visible train travel are separate observations. A Route Query line does not prove that a train visibly completed the journey; a software build does not approve either game observation.

Follow the [shared observation procedure](../../../../docs/TESTING.md#record-one-observation) using this piece's [authoritative manual record](checks/manual-tests.json). Record the direction, rotation, platform, game version, NAM profile, and actual evidence for each game result. Only explicit human confirmation records a manual pass. Keep failures, stale results, and historical observations with their original scope.

The generated sections below supply the exact saved-resource interfaces, supported states, current checklist, and recording command. They do not establish compatibility with an arbitrary neighbour.

### Engineering sources and limits

The construction rectangle remains **7 × 5 tiles**, with **11 owned cells** and **six supports**. Its outer source columns 0 and 6 are empty, while its authoring anchor and retained resource identifiers remain fixed. A structural cell contains physical geometry without a train path; the two current structural cells must remain reserved.

The two fan arms retain opposite travel directions and share the branch angles of the Short Mainline Diverge Core. Their north-facing ends form one paired boundary. Their southern cuts meet curved continuations obliquely, so they have no declared paired-straight profile, section origin, or section offset. The connection cards preserve each cut’s measured endpoint, outward heading, path height, and direction without inventing a centred section.

The [geometry source](geometry.json) owns route samples, physical sweeps, selected cells, and support positions. Independent software contracts inspect encoded endpoints, direction, L2 height, route continuity, curvature, bed coverage, visible rail alignment, supports, and model budgets. These checks do not approve arbitrary neighbours, terrain behaviour, game appearance, or train operation. The generated matrix and checklist retain the scope and current state of each measured or observed result.

Actual saved-resource software checks are recorded in [the current resource-check report](evidence/saved-resource-checks.json). Current canonical picture provenance belongs in [angled-view evidence](evidence/preview.json), [top-view evidence](evidence/preview-top.json), and [connection-overview evidence](evidence/connection-overview.json). The [earlier combined preview report](evidence/design-history/preview-before-junction-rework.json) is preserved as historical evidence for the geometry before this redesign. It does not describe the current pictures.

### Reproduce this piece’s software checks

Run these commands from the repository root, the folder containing `custom-pieces/`, after completing the [shared dependency and native-input preparation](../../../../docs/BUILD_AND_INSTALL.md). Replace `/path/to/Plugins` with the existing NAM Plugins directory, and keep the quotation marks if its path contains spaces. Use a new output directory so an earlier build remains available for comparison.

```sh
python3 -B custom-pieces/scp.py build --include hsr-component-l2-paired-fan-compact-join --output custom-pieces/dist/hsr-l2-paired-fan-review --plugins '/path/to/Plugins'
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/hsr-l2-paired-fan-review
```

Building writes a local development build; verification inspects its saved resources. Neither command installs files or records a game pass. After changing actual resources, follow the [documented extraction, connector, and picture refresh sequence](../../../../docs/WORKFLOW_DOCUMENTATION_GENERATION.md#before-refreshing) for this exact type before using regenerated documentation.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 2/3 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Route Query: 0/8 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/8 applicable cases passed; 0 failed, 0 stale.

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
| `Wout` | hsr / 7 / primary | out | [22.398519, -72.0, 15.5]; [-0.9272548089646255, -0.3744309272108488]; 0.0 | `path-interface-0f4b8204e68941486c48` |
| `Nin` | hsr / 7 / primary | in | [46.0, 8.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Nout` | hsr / 7 / primary | out | [50.0, 8.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Ein` | hsr / 7 / primary | in | [73.601481, -72.0, 15.5]; [-0.9272548089646255, 0.3744309272108488]; 0.0 | `path-interface-d819a6d05c5e43d11db7` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Nin` → `Wout` | primary |
| hsr | `Ein` → `Nout` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| hsr / `Nin` | hsr / `Nout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Ein` | hsr / `Wout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 41, passed: 4, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-l2-paired-fan-compact-join/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-l2-paired-fan-compact-join/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-bc65ebc1e8aece8c8a6d">[x] passed</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-bc65ebc1e8aece8c8a6d"></a>

**General: passed** — `software_resources-bc65ebc1e8aece8c8a6d`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: verify_hsr_trumpet_v4.py plus current compiled-resource checks; confirmed at: 2026-10-20T11:45:51.432103+00:00; evidence: [../../01_assemblies/straight-stem-trumpet-v4/evidence/validation.json]; environment: {}
- result: passed; authority: software; reviewer: Normal saved-build verifier with independent compact-fan PATH and model contracts; confirmed at: 2026-10-27T18:29:02.017861+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}
- result: passed; authority: software; reviewer: Normal saved-build verifier with independent compact-fan PATH and model contracts; confirmed at: 2026-10-27T18:41:49.586746+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}
- result: passed; authority: software; reviewer: Actual final normal 13-piece saved-build verification; registered independent PATH, model, construction, menu, and shadow checks; confirmed at: 2026-10-27T21:57:25.376326+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-bc65ebc1e8aece8c8a6d">[x] passed</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-bc65ebc1e8aece8c8a6d"></a>

**General: passed** — `software_connectivity-bc65ebc1e8aece8c8a6d`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: verify_hsr_trumpet_v4.py plus current compiled-resource checks; confirmed at: 2026-10-20T11:45:51.438799+00:00; evidence: [../../01_assemblies/straight-stem-trumpet-v4/evidence/validation.json]; environment: {}
- result: passed; authority: software; reviewer: Normal saved-build verifier with independent compact-fan PATH and model contracts; confirmed at: 2026-10-27T18:29:02.017861+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}
- result: passed; authority: software; reviewer: Normal saved-build verifier with independent compact-fan PATH and model contracts; confirmed at: 2026-10-27T18:41:49.586746+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}
- result: passed; authority: software; reviewer: Actual final normal 13-piece saved-build verification; registered independent PATH, model, construction, menu, and shadow checks; confirmed at: 2026-10-27T21:57:25.376326+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 1, passed: 2</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:hsr-component-l2-paired-fan-compact-join:canonical-southeast | <a href="#case-preview_review-3cb6c2661802b929620d">[x] passed</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-l2-paired-fan-compact-join:canonical-top | <a href="#case-preview_review-f59bcfa100a7ff0db938">[x] passed</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-l2-paired-fan-compact-join:connection-overview | <a href="#case-preview_review-407c1640d6da76516db5">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:hsr-component-l2-paired-fan-compact-join:canonical-southeast</summary>

<a id="case-preview_review-3cb6c2661802b929620d"></a>

**General: passed** — `preview_review-3cb6c2661802b929620d`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:hsr-component-l2-paired-fan-compact-join:canonical-southeast.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-10-27T21:48:27.631996+00:00; evidence: [evidence/fan-width-audit.json]; environment: observation type: software-rendered image review; note: Explicit user approval of the unchanged clean angled and top fan-width review images: yeah looks good. go ahead and rerender the trumpet assembly, refresh the geometry audit. No game observation was supplied.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-l2-paired-fan-compact-join:canonical-top</summary>

<a id="case-preview_review-f59bcfa100a7ff0db938"></a>

**General: passed** — `preview_review-f59bcfa100a7ff0db938`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:hsr-component-l2-paired-fan-compact-join:canonical-top.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-10-27T21:48:27.631996+00:00; evidence: [evidence/fan-width-audit.json]; environment: observation type: software-rendered image review; note: Explicit user approval of the unchanged clean angled and top fan-width review images: yeah looks good. go ahead and rerender the trumpet assembly, refresh the geometry audit. No game observation was supplied.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-l2-paired-fan-compact-join:connection-overview</summary>

<a id="case-preview_review-407c1640d6da76516db5"></a>

**General: unverified** — `preview_review-407c1640d6da76516db5`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:hsr-component-l2-paired-fan-compact-join:connection-overview.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-2953a796038b1c66047b">[ ] unverified</a> | <a href="#case-in_game_render-9f1c3339be8608575afb">[ ] unverified</a> | <a href="#case-in_game_render-3ebb754476ae4beaee16">[ ] unverified</a> | <a href="#case-in_game_render-aa233b7e5bab139363c3">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-2953a796038b1c66047b"></a>

**0° CCW: unverified** — `in_game_render-2953a796038b1c66047b`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-9f1c3339be8608575afb"></a>

**90° CCW: unverified** — `in_game_render-9f1c3339be8608575afb`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-3ebb754476ae4beaee16"></a>

**180° CCW: unverified** — `in_game_render-3ebb754476ae4beaee16`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-aa233b7e5bab139363c3"></a>

**270° CCW: unverified** — `in_game_render-aa233b7e5bab139363c3`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-2953a796038b1c66047b">[ ] unverified</a> | <a href="#case-in_game_placement-9f1c3339be8608575afb">[ ] unverified</a> | <a href="#case-in_game_placement-3ebb754476ae4beaee16">[ ] unverified</a> | <a href="#case-in_game_placement-aa233b7e5bab139363c3">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-2953a796038b1c66047b"></a>

**0° CCW: unverified** — `in_game_placement-2953a796038b1c66047b`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-9f1c3339be8608575afb"></a>

**90° CCW: unverified** — `in_game_placement-9f1c3339be8608575afb`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-3ebb754476ae4beaee16"></a>

**180° CCW: unverified** — `in_game_placement-3ebb754476ae4beaee16`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-aa233b7e5bab139363c3"></a>

**270° CCW: unverified** — `in_game_placement-aa233b7e5bab139363c3`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-2953a796038b1c66047b">[ ] unverified</a> | <a href="#case-in_game_demolition-9f1c3339be8608575afb">[ ] unverified</a> | <a href="#case-in_game_demolition-3ebb754476ae4beaee16">[ ] unverified</a> | <a href="#case-in_game_demolition-aa233b7e5bab139363c3">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-2953a796038b1c66047b"></a>

**0° CCW: unverified** — `in_game_demolition-2953a796038b1c66047b`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-9f1c3339be8608575afb"></a>

**90° CCW: unverified** — `in_game_demolition-9f1c3339be8608575afb`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-3ebb754476ae4beaee16"></a>

**180° CCW: unverified** — `in_game_demolition-3ebb754476ae4beaee16`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-aa233b7e5bab139363c3"></a>

**270° CCW: unverified** — `in_game_demolition-aa233b7e5bab139363c3`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-2953a796038b1c66047b">[ ] unverified</a> | <a href="#case-in_game_save_reload-9f1c3339be8608575afb">[ ] unverified</a> | <a href="#case-in_game_save_reload-3ebb754476ae4beaee16">[ ] unverified</a> | <a href="#case-in_game_save_reload-aa233b7e5bab139363c3">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-2953a796038b1c66047b"></a>

**0° CCW: unverified** — `in_game_save_reload-2953a796038b1c66047b`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-9f1c3339be8608575afb"></a>

**90° CCW: unverified** — `in_game_save_reload-9f1c3339be8608575afb`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-3ebb754476ae4beaee16"></a>

**180° CCW: unverified** — `in_game_save_reload-3ebb754476ae4beaee16`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-aa233b7e5bab139363c3"></a>

**270° CCW: unverified** — `in_game_save_reload-aa233b7e5bab139363c3`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout | — | <a href="#case-in_game_route_query-efa01c69d3d0a595addc">[ ] unverified</a> | <a href="#case-in_game_route_query-f0765824bce6e2085023">[ ] unverified</a> | <a href="#case-in_game_route_query-accf1bc882028a242b30">[ ] unverified</a> | <a href="#case-in_game_route_query-6168c4cc5136e21b2f7b">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout | — | <a href="#case-in_game_route_query-65a9b6549c48f167a40e">[ ] unverified</a> | <a href="#case-in_game_route_query-fe64d25bac6aea848487">[ ] unverified</a> | <a href="#case-in_game_route_query-89e5e4b7f562bc923192">[ ] unverified</a> | <a href="#case-in_game_route_query-cec0cc3b6c354f5dbbcf">[ ] unverified</a> |


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout</summary>

<a id="case-in_game_route_query-efa01c69d3d0a595addc"></a>

**0° CCW: unverified** — `in_game_route_query-efa01c69d3d0a595addc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_route_query-f0765824bce6e2085023"></a>

**90° CCW: unverified** — `in_game_route_query-f0765824bce6e2085023`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_route_query-accf1bc882028a242b30"></a>

**180° CCW: unverified** — `in_game_route_query-accf1bc882028a242b30`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_route_query-6168c4cc5136e21b2f7b"></a>

**270° CCW: unverified** — `in_game_route_query-6168c4cc5136e21b2f7b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout</summary>

<a id="case-in_game_route_query-65a9b6549c48f167a40e"></a>

**0° CCW: unverified** — `in_game_route_query-65a9b6549c48f167a40e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

<a id="case-in_game_route_query-fe64d25bac6aea848487"></a>

**90° CCW: unverified** — `in_game_route_query-fe64d25bac6aea848487`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

<a id="case-in_game_route_query-89e5e4b7f562bc923192"></a>

**180° CCW: unverified** — `in_game_route_query-89e5e4b7f562bc923192`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

<a id="case-in_game_route_query-cec0cc3b6c354f5dbbcf"></a>

**270° CCW: unverified** — `in_game_route_query-cec0cc3b6c354f5dbbcf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout | — | <a href="#case-in_game_visible_travel-efa01c69d3d0a595addc">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f0765824bce6e2085023">[ ] unverified</a> | <a href="#case-in_game_visible_travel-accf1bc882028a242b30">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6168c4cc5136e21b2f7b">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout | — | <a href="#case-in_game_visible_travel-65a9b6549c48f167a40e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-fe64d25bac6aea848487">[ ] unverified</a> | <a href="#case-in_game_visible_travel-89e5e4b7f562bc923192">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cec0cc3b6c354f5dbbcf">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout</summary>

<a id="case-in_game_visible_travel-efa01c69d3d0a595addc"></a>

**0° CCW: unverified** — `in_game_visible_travel-efa01c69d3d0a595addc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_visible_travel-f0765824bce6e2085023"></a>

**90° CCW: unverified** — `in_game_visible_travel-f0765824bce6e2085023`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_visible_travel-accf1bc882028a242b30"></a>

**180° CCW: unverified** — `in_game_visible_travel-accf1bc882028a242b30`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_visible_travel-6168c4cc5136e21b2f7b"></a>

**270° CCW: unverified** — `in_game_visible_travel-6168c4cc5136e21b2f7b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout</summary>

<a id="case-in_game_visible_travel-65a9b6549c48f167a40e"></a>

**0° CCW: unverified** — `in_game_visible_travel-65a9b6549c48f167a40e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

<a id="case-in_game_visible_travel-fe64d25bac6aea848487"></a>

**90° CCW: unverified** — `in_game_visible_travel-fe64d25bac6aea848487`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

<a id="case-in_game_visible_travel-89e5e4b7f562bc923192"></a>

**180° CCW: unverified** — `in_game_visible_travel-89e5e4b7f562bc923192`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

<a id="case-in_game_visible_travel-cec0cc3b6c354f5dbbcf"></a>

**270° CCW: unverified** — `in_game_visible_travel-cec0cc3b6c354f5dbbcf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3ad08e7a19456cd90fd0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4d4bf82777d040a92574">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f8a6e6bba23dded7d7ae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-690df8549dc3f5fda576">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Ein; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-97aa23dd677c7b8c9e3c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cf602616988bd0a9a85a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c35a186b255281e199c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c046e5e0bc2afa332fca">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3ad08e7a19456cd90fd0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3ad08e7a19456cd90fd0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4d4bf82777d040a92574"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4d4bf82777d040a92574`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f8a6e6bba23dded7d7ae"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f8a6e6bba23dded7d7ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-690df8549dc3f5fda576"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-690df8549dc3f5fda576`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Ein; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-97aa23dd677c7b8c9e3c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-97aa23dd677c7b8c9e3c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cf602616988bd0a9a85a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cf602616988bd0a9a85a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c35a186b255281e199c9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c35a186b255281e199c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c046e5e0bc2afa332fca"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c046e5e0bc2afa332fca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
