---
title: "Testing: DD RHW-4 Level 1 (7.5 m) and Level 2 (15 m) over GHSR Ground (1 m) \u2014 Mixed Crossing \u2014 Both Diagonal 90\u00b0"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 Level 1 (7.5 m) and Level 2 (15 m) over GHSR Ground (1 m) — Mixed Crossing — Both Diagonal 90°

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

This test scope is the two-tile diagonal DD RHW-4/GHSR crossing and its four external native approaches. The [piece overview](README.md) identifies the menu button and its 3 × 2 placement arrangement. The fixed core carries two GHSR directions at 1 m, two car lanes at 7.5 m, and the opposing two car lanes at 15 m. All six directed journeys must remain connected. Rail and highway traffic must stay on their own networks, each highway direction must stay on its own deck, and no same-arm return is intended.

Software checks examine all four proper rotations. The required human test plan also uses fresh copies in all four distinct placement rotations because this new piece must connect two differently marked native networks on four sides. Rotate the city camera separately through its four views after placement; that checks a different operation. Eight menu states repeat the four rotations and do not add mirrored placements.

Keep three results separate for every permitted journey: the route encoded in the saved PATH file, the route shown by Route Query, and actual visible travel. A successful route display does not approve moving cars or moving trains. Test the two build orders below independently, and retain their exact orientation, approach directions, build fingerprints, and city observations.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `lower-lane-01-in` | road / 1 / primary | in | [-8.0, -19.2, 7.5]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `upper-lane-01-out` | road / 1 / primary | out | [-8.0, -19.2, 15.0]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `lower-lane-02-in` | road / 1 / primary | in | [-8.0, -12.8, 7.5]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `upper-lane-02-out` | road / 1 / primary | out | [-8.0, -12.8, 15.0]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `lower-lane-01-out` | road / 1 / primary | out | [8.0, -3.2, 7.5]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `upper-lane-01-in` | road / 1 / primary | in | [8.0, -3.2, 15.0]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `lower-lane-02-out` | road / 1 / primary | out | [8.0, 3.2, 7.5]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `upper-lane-02-in` | road / 1 / primary | in | [8.0, 3.2, 15.0]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `ghsr-track-01-in` | ghsr / 7 / primary | in | [-8.0, -2.9, 1.0]; [0.7071067811865475, -0.7071067811865476]; 0.0 | `path-interface-d13580a5f8b596919466` |
| `ghsr-track-02-out` | ghsr / 7 / primary | out | [-8.0, 2.9, 1.0]; [-0.7139382485962432, 0.7002086668924692]; 0.0 | `path-interface-8d80a0a7d571f164837f` |
| `ghsr-track-01-out` | ghsr / 7 / primary | out | [8.0, -18.9, 1.0]; [0.7139382485962432, -0.7002086668924692]; 0.0 | `path-interface-8d80a0a7d571f164837f` |
| `ghsr-track-02-in` | ghsr / 7 / primary | in | [8.0, -13.1, 1.0]; [-0.7071067811865475, 0.7071067811865476]; 0.0 | `path-interface-d13580a5f8b596919466` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `lower-lane-01-in` → `lower-lane-01-out` | primary |
| road | `lower-lane-02-in` → `lower-lane-02-out` | primary |
| road | `upper-lane-01-in` → `upper-lane-01-out` | primary |
| road | `upper-lane-02-in` → `upper-lane-02-out` | primary |
| ghsr | `ghsr-track-01-in` → `ghsr-track-01-out` | primary |
| ghsr | `ghsr-track-02-in` → `ghsr-track-02-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `lower-lane-01-in` | road / `upper-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `lower-lane-01-in` | road / `upper-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `lower-lane-01-in` | road / `lower-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `lower-lane-01-in` | ghsr / `ghsr-track-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `lower-lane-01-in` | ghsr / `ghsr-track-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `lower-lane-02-in` | road / `upper-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `lower-lane-02-in` | road / `upper-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `lower-lane-02-in` | road / `lower-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `lower-lane-02-in` | ghsr / `ghsr-track-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `lower-lane-02-in` | ghsr / `ghsr-track-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `upper-lane-01-in` | road / `upper-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `upper-lane-01-in` | road / `lower-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `upper-lane-01-in` | road / `lower-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `upper-lane-01-in` | ghsr / `ghsr-track-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `upper-lane-01-in` | ghsr / `ghsr-track-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `upper-lane-02-in` | road / `upper-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `upper-lane-02-in` | road / `lower-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `upper-lane-02-in` | road / `lower-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `upper-lane-02-in` | ghsr / `ghsr-track-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `upper-lane-02-in` | ghsr / `ghsr-track-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `ghsr-track-01-in` | road / `upper-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `ghsr-track-01-in` | road / `upper-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `ghsr-track-01-in` | road / `lower-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `ghsr-track-01-in` | road / `lower-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `ghsr-track-01-in` | ghsr / `ghsr-track-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `ghsr-track-02-in` | road / `upper-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `ghsr-track-02-in` | road / `upper-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `ghsr-track-02-in` | road / `lower-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `ghsr-track-02-in` | road / `lower-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `ghsr-track-02-in` | ghsr / `ghsr-track-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 1.1.641 with the project's audited NAM 50 right-hand-traffic inputs. Wine or CrossOver may run that Windows game; record which environment was actually used. The source dependencies are `NetworkAddonMod_Controller.dat`, `RealHighway_DD_RHW-4.dat`, `RealHighway_Core.dat`, `High Speed Rail.dat`, and the audited native-lighting capture. The [shared build guide](../../../../docs/BUILD_AND_INSTALL.md) owns private input settings, exact dependency auditing, installation, and backups. A completed build does not install itself.

Install with the game fully closed, restart it, and place fresh crossing instances in a disposable flat test city. Fresh placement creates the crossing's new shadow attachments and its native approach markers. Use Medium or High shadow quality for the shadow cases. Retain a screenshot before placement, the exact selected build's manifest, and the game version, NAM version, traffic side, active Plugins selection, and shadow setting used for each observation.

One city tile is 16 m. Technical construction coordinates use column east/right and row south/down. The two owned cells are `(0,0)` and `(0,1)`. The outside helpers are GHSR at `(-1,0)` and `(1,1)`, and DD RHW-4 at `(1,0)` and `(-1,1)`. Thus the construction check reaches columns −1 through 1 and rows 0 through 1, while only the central column belongs to the fixed piece. The canonical preview's southwest-based display labels instead place the north core tile at `(X0,Y1)` and the south core tile at `(X0,Y0)`; its X/Y labels do not change the technical ownership coordinates.

Use the exact native starter selections listed in [README placement](README.md#22-place-a-fresh-crossing-and-extend-both-networks). Before judging this crossing's traffic, establish a control: the surrounding native DD line must already carry moving cars on both decks, and the surrounding GHSR passenger line must already carry moving trains in both directions. Stations, access routes, and travel demand are required for that control; a disconnected line or a city without passengers cannot establish a train-path failure. Keep alternate bypasses away from the crossing so an observed trip must traverse the tested route.

## 3. Software checks

Run these commands from the repository directory containing `custom-pieces/`, after preparing the Python environment and private inputs described in the build guide. The checked source build is `dist/ghsr-under-ddrhw-diagonal-source-01`, relative to the library. The first command audits the native inputs; the remaining commands inspect that build, its source-bound records, and the repository tests. They do not install files or create human game observations.

```sh
python3 -B custom-pieces/scp.py doctor --include ddrhw-l1-and-l2-over-ghsr-ground-mixed-crossing-diagonal-90deg
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/ghsr-under-ddrhw-diagonal-source-01
python3 -B custom-pieces/scp.py connectors check --domain highway --piece ddrhw-l1-and-l2-over-ghsr-ground-mixed-crossing-diagonal-90deg --build dist/ghsr-under-ddrhw-diagonal-source-01
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-l1-and-l2-over-ghsr-ground-mixed-crossing-diagonal-90deg
python3 -B tools/run_tests.py
```

The owning recipe is [ghsr_crossing.py](../../implementation/scp_highway/ghsr_crossing.py), and the independent saved-resource contract is [ghsr_crossing_verify.py](../../implementation/scp_highway/ghsr_crossing_verify.py). The native approaches are declared in [ghsr_approaches.py](../../implementation/scp_highway/ghsr_approaches.py). Check the current build report for complete directed lane seams, exact native-helper endpoints and headings, preserved model buffers and textures, packed vertex format `80004001`, explicit PATH height retention, and correct construction selection in every proper rotation. Independent shadow checks must also cover the two hosts, all four relative-pose masks per host, and all sixteen object/camera combinations.

The [frozen native contract](evidence/native-contract.jsonc) identifies the actual source build and DAT fingerprints, independently checked mesh streams and routes, native helper resources and rules, measured rail transition, and shadow reports. Its targeted independent-verifier run passed 23 tests with no skips, including original-native integration. That recorded run is separate from any later full-suite result and from all pending game observations.

The measured train corridor is 5 m wide and 5 m high above the 1 m GHSR route. Its roof is therefore 6 m above ground. The lowest DD structure is 6.5 m above ground, leaving 0.5 m geometrically. The selected DD meshes have no ground-reaching pillars. This is a project geometry envelope; it is not a measured collision box for every replacement train. Check actual moving vehicles separately.

Ordinary diagonal GHSR has an asymmetric native 2.8/2.9 m PATH chord. Only the two internal 2.8 m endpoints are moved to matching 2.9 m seam positions. Every rail route has four nodes: a 3 m exterior collar aligned to its actual complementary native helper, a short interior blend, and a 1 m collar meeting the shared seam at exactly 45°. The greatest lateral displacement from an original source chord is approximately 0.070020866689 m; the changed internal endpoints move by 0.1 m. Visible native track geometry remains unchanged. The [network specification](../../NETWORK_SPEC.md#15-diagonal-ghsr-beneath-dd-rhw-4) records the exact source and construction contract.

The fifth PATH header line is `UseElevation`; this crossing explicitly writes `1` so the game retains authored 1 m, 7.5 m, and 15 m routes. Its two fixed cells carry both actual DirtRoad and Monorail network flags. Four outside dynamic helper cells provide the native override seeds. The build adds narrow RUL1 solutions for those seeds and preserves native RUL2 byte for byte; matching models alone would not establish that draggable construction can continue.

## 4. Game checks

### 4.1 Crossing first, then draggable approaches

1. Follow [README placement](README.md#22-place-a-fresh-crossing-and-extend-both-networks) on empty flat land. Place a fresh 0° crossing, and leave all four approach squares available. Record whether placement succeeds and whether the two fixed tiles and four native approaches match the reference table.
2. Use **RealHighway (RHW-2)** from each DD approach to draw at least three diagonal squares outward. Check that both stacked decks continue. Use **Monorail** from each GHSR approach to draw at least three diagonal squares outward. Check that the railway stays at ground level.
3. Join the four extensions to the already working control lines. Let the simulation run until those lines carry trips through this site. Use Route Query on each highway deck and the railway, and record the exact through direction displayed.
4. Follow actual cars across the complete upper and lower bridges, then follow actual trains in both ground-rail directions. Watch the four native-to-fixed joins and the internal seam. Record stops, disappearance, wrong heights, direction reversals, and visible road/rail gaps separately from the query result.
5. Repeat with fresh pieces at 90°, 180°, and 270°. Record each orientation separately rather than treating another camera view as a newly rotated placement.

### 4.2 Native approaches first, then the crossing

1. Prepare a second flat area. Use **Transportation → Rail → Ground High Speed Rail (GHSR)**, select its **Ground High Speed Rail Starter Piece**, and use **Monorail** to draw the two diagonal ground-rail arms toward the northwest and southeast approach squares in the README table.
2. Use **Transportation → Highways → RealHighway (RHW) Starter Pieces**, press **Tab** to select **Double-Decker RHW-4 Starter Piece (Upper Deck: Level 2, Lower Deck: Level 1)**, and use **RealHighway (RHW-2)** to draw the two diagonal highway arms toward the northeast and southwest approach squares. Keep both fixed central squares empty. Compare the upper/lower highway travel directions with the crossing's arrows and connection cards before placement.
3. Select the SCP crossing, align its two fixed squares with that central gap, and click once. Record whether the preview accepts the layout and whether placement preserves all four native approaches. The helpers are optional dynamic network cells; actual acceptance over an existing approach remains a game test.
4. Continue or redraw each native line outward from its approach, then repeat the six directed through journeys with both Route Query and visible travel. Repeat this build order in the other three distinct placement rotations.

### 4.3 Heights, shadows, and object lifetime

1. Rotate the city camera through all four views around a fresh crossing. Check that GHSR stays below the lower deck, the lower and upper highway lanes stay at their own levels, and the highway and rail models rotate together. Inspect native ground-bed overhangs and the seam between the two fixed tiles.
2. Set shadows to **Medium**, inspect the crossing from all camera views and zoom levels, and repeat with **High**. Check for shadows cut at tile boundaries, detached triangles, missing deck shadows, or a phantom neighbouring structure. Low shadow quality does not use this native prop-shadow path.
3. Save the city, quit the game completely, reopen that saved city, and repeat the visible-height, approach, shadow, and travel checks. Save/reload is a separate observation from successful first placement.
4. In the disposable area, demolish the crossing, inspect both former fixed squares for leftover model or shadow objects, and inspect the four native approaches separately. Record which native approach tiles remain and whether each remaining line can still be redrawn. Rebuild a fresh crossing, and repeat the connection check.
5. Test a small terrain edit beside the real road and rail geometry, beyond the fixed tiles. Record whether an invisible shadow carrier unexpectedly prevents the edit; the carrier's terrain-filter exemption does not establish every possible terrain behaviour.

Use [the shared observation workflow](../../../../docs/TESTING.md) to record the exact current cases for `ddrhw-l1-and-l2-over-ghsr-ground-mixed-crossing-diagonal-90deg`. Preserve build fingerprints, screenshots, and failures. A software check or a report about an earlier Avenue crossing cannot approve this mixed crossing's manual cases.

## 5. Results and known issues

This is a new experimental piece. All human game checks remain open until an explicit matching observation is recorded. The native source measurements, encoded journeys, model preservation, and projected shadow checks have their own software evidence; they do not establish live placement, draggable continuation, moving cars, moving trains, shadows, terrain behaviour, demolition, or save/reload.

The native GHSR track bed extends approximately 0.989332 m below the ground datum and 1.989332 m above it. The isolated software view can expose below-ground side faces, while the track's long horizontal projection can also look steep in the angled camera. Its saved vertices do not contain a tall vertical track curtain. Actual terrain occlusion and train appearance remain part of the game rendering check. The exact 0.5 m geometric roof margin is also not a promise that every custom train model fits.

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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-l1-and-l2-over-ghsr-ground-mixed-crossing-diagonal-90deg/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-l1-and-l2-over-ghsr-ground-mixed-crossing-diagonal-90deg/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-e8ed3d694b629f212561">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-e8ed3d694b629f212561"></a>

**General: unverified** — `software_resources-e8ed3d694b629f212561`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-e8ed3d694b629f212561">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-e8ed3d694b629f212561"></a>

**General: unverified** — `software_connectivity-e8ed3d694b629f212561`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-over-ghsr-ground-mixed-crossing-diagonal-90deg:canonical-southeast | <a href="#case-preview_review-91a46f707ca45c1febca">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-over-ghsr-ground-mixed-crossing-diagonal-90deg:canonical-top | <a href="#case-preview_review-e762595d65419106b3cc">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-over-ghsr-ground-mixed-crossing-diagonal-90deg:connection-overview | <a href="#case-preview_review-ec3d14e5b6f5c6cc8104">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-over-ghsr-ground-mixed-crossing-diagonal-90deg:canonical-southeast</summary>

<a id="case-preview_review-91a46f707ca45c1febca"></a>

**General: unverified** — `preview_review-91a46f707ca45c1febca`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-l1-and-l2-over-ghsr-ground-mixed-crossing-diagonal-90deg:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-over-ghsr-ground-mixed-crossing-diagonal-90deg:canonical-top</summary>

<a id="case-preview_review-e762595d65419106b3cc"></a>

**General: unverified** — `preview_review-e762595d65419106b3cc`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-l1-and-l2-over-ghsr-ground-mixed-crossing-diagonal-90deg:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-over-ghsr-ground-mixed-crossing-diagonal-90deg:connection-overview</summary>

<a id="case-preview_review-ec3d14e5b6f5c6cc8104"></a>

**General: unverified** — `preview_review-ec3d14e5b6f5c6cc8104`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-l1-and-l2-over-ghsr-ground-mixed-crossing-diagonal-90deg:connection-overview.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-e798ee95402b3e1c87d5">[ ] unverified</a> | <a href="#case-in_game_render-f2cd8ab81d8361391f87">[ ] unverified</a> | <a href="#case-in_game_render-7853aa4c7d1f09d6262f">[ ] unverified</a> | <a href="#case-in_game_render-0ddb499d50d481730c32">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-e798ee95402b3e1c87d5"></a>

**0° CCW: unverified** — `in_game_render-e798ee95402b3e1c87d5`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-f2cd8ab81d8361391f87"></a>

**90° CCW: unverified** — `in_game_render-f2cd8ab81d8361391f87`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-7853aa4c7d1f09d6262f"></a>

**180° CCW: unverified** — `in_game_render-7853aa4c7d1f09d6262f`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-0ddb499d50d481730c32"></a>

**270° CCW: unverified** — `in_game_render-0ddb499d50d481730c32`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-e798ee95402b3e1c87d5">[ ] unverified</a> | <a href="#case-in_game_placement-f2cd8ab81d8361391f87">[ ] unverified</a> | <a href="#case-in_game_placement-7853aa4c7d1f09d6262f">[ ] unverified</a> | <a href="#case-in_game_placement-0ddb499d50d481730c32">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-e798ee95402b3e1c87d5"></a>

**0° CCW: unverified** — `in_game_placement-e798ee95402b3e1c87d5`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-f2cd8ab81d8361391f87"></a>

**90° CCW: unverified** — `in_game_placement-f2cd8ab81d8361391f87`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-7853aa4c7d1f09d6262f"></a>

**180° CCW: unverified** — `in_game_placement-7853aa4c7d1f09d6262f`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-0ddb499d50d481730c32"></a>

**270° CCW: unverified** — `in_game_placement-0ddb499d50d481730c32`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-e798ee95402b3e1c87d5">[ ] unverified</a> | <a href="#case-in_game_demolition-f2cd8ab81d8361391f87">[ ] unverified</a> | <a href="#case-in_game_demolition-7853aa4c7d1f09d6262f">[ ] unverified</a> | <a href="#case-in_game_demolition-0ddb499d50d481730c32">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-e798ee95402b3e1c87d5"></a>

**0° CCW: unverified** — `in_game_demolition-e798ee95402b3e1c87d5`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-f2cd8ab81d8361391f87"></a>

**90° CCW: unverified** — `in_game_demolition-f2cd8ab81d8361391f87`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-7853aa4c7d1f09d6262f"></a>

**180° CCW: unverified** — `in_game_demolition-7853aa4c7d1f09d6262f`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-0ddb499d50d481730c32"></a>

**270° CCW: unverified** — `in_game_demolition-0ddb499d50d481730c32`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-e798ee95402b3e1c87d5">[ ] unverified</a> | <a href="#case-in_game_save_reload-f2cd8ab81d8361391f87">[ ] unverified</a> | <a href="#case-in_game_save_reload-7853aa4c7d1f09d6262f">[ ] unverified</a> | <a href="#case-in_game_save_reload-0ddb499d50d481730c32">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-e798ee95402b3e1c87d5"></a>

**0° CCW: unverified** — `in_game_save_reload-e798ee95402b3e1c87d5`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-f2cd8ab81d8361391f87"></a>

**90° CCW: unverified** — `in_game_save_reload-f2cd8ab81d8361391f87`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-7853aa4c7d1f09d6262f"></a>

**180° CCW: unverified** — `in_game_save_reload-7853aa4c7d1f09d6262f`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-0ddb499d50d481730c32"></a>

**270° CCW: unverified** — `in_game_save_reload-0ddb499d50d481730c32`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out | — | <a href="#case-in_game_route_query-50007a8a544067632df8">[ ] unverified</a> | <a href="#case-in_game_route_query-aa996420a65ef96043cb">[ ] unverified</a> | <a href="#case-in_game_route_query-b0eaf8dec5b0fd80952b">[ ] unverified</a> | <a href="#case-in_game_route_query-1211672a95d2d4362be6">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out | — | <a href="#case-in_game_route_query-44b900d2419028db3d9c">[ ] unverified</a> | <a href="#case-in_game_route_query-29c1afbd6a548d090e9e">[ ] unverified</a> | <a href="#case-in_game_route_query-8ccc987288ddc2a079b8">[ ] unverified</a> | <a href="#case-in_game_route_query-34ea0fcc80492f29af5a">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out | — | <a href="#case-in_game_route_query-7347234933817d8bc777">[ ] unverified</a> | <a href="#case-in_game_route_query-88ccccc6a1fed2bf7844">[ ] unverified</a> | <a href="#case-in_game_route_query-524b89e91556ac4aa8a7">[ ] unverified</a> | <a href="#case-in_game_route_query-f1c3d5903b118f13b235">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out | — | <a href="#case-in_game_route_query-1c93d9ac8ff075b3ae9f">[ ] unverified</a> | <a href="#case-in_game_route_query-a0a6268e972c5f5f9205">[ ] unverified</a> | <a href="#case-in_game_route_query-23338840e03f48985a5b">[ ] unverified</a> | <a href="#case-in_game_route_query-8ebc71043d02be97846b">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out</summary>

<a id="case-in_game_route_query-50007a8a544067632df8"></a>

**0° CCW: unverified** — `in_game_route_query-50007a8a544067632df8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-aa996420a65ef96043cb"></a>

**90° CCW: unverified** — `in_game_route_query-aa996420a65ef96043cb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-b0eaf8dec5b0fd80952b"></a>

**180° CCW: unverified** — `in_game_route_query-b0eaf8dec5b0fd80952b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-1211672a95d2d4362be6"></a>

**270° CCW: unverified** — `in_game_route_query-1211672a95d2d4362be6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out</summary>

<a id="case-in_game_route_query-44b900d2419028db3d9c"></a>

**0° CCW: unverified** — `in_game_route_query-44b900d2419028db3d9c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-29c1afbd6a548d090e9e"></a>

**90° CCW: unverified** — `in_game_route_query-29c1afbd6a548d090e9e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-8ccc987288ddc2a079b8"></a>

**180° CCW: unverified** — `in_game_route_query-8ccc987288ddc2a079b8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-34ea0fcc80492f29af5a"></a>

**270° CCW: unverified** — `in_game_route_query-34ea0fcc80492f29af5a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out</summary>

<a id="case-in_game_route_query-7347234933817d8bc777"></a>

**0° CCW: unverified** — `in_game_route_query-7347234933817d8bc777`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-88ccccc6a1fed2bf7844"></a>

**90° CCW: unverified** — `in_game_route_query-88ccccc6a1fed2bf7844`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-524b89e91556ac4aa8a7"></a>

**180° CCW: unverified** — `in_game_route_query-524b89e91556ac4aa8a7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-f1c3d5903b118f13b235"></a>

**270° CCW: unverified** — `in_game_route_query-f1c3d5903b118f13b235`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out</summary>

<a id="case-in_game_route_query-1c93d9ac8ff075b3ae9f"></a>

**0° CCW: unverified** — `in_game_route_query-1c93d9ac8ff075b3ae9f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-a0a6268e972c5f5f9205"></a>

**90° CCW: unverified** — `in_game_route_query-a0a6268e972c5f5f9205`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-23338840e03f48985a5b"></a>

**180° CCW: unverified** — `in_game_route_query-23338840e03f48985a5b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-8ebc71043d02be97846b"></a>

**270° CCW: unverified** — `in_game_route_query-8ebc71043d02be97846b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out | — | <a href="#case-in_game_visible_travel-50007a8a544067632df8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-aa996420a65ef96043cb">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b0eaf8dec5b0fd80952b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1211672a95d2d4362be6">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out | — | <a href="#case-in_game_visible_travel-44b900d2419028db3d9c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-29c1afbd6a548d090e9e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8ccc987288ddc2a079b8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-34ea0fcc80492f29af5a">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out | — | <a href="#case-in_game_visible_travel-7347234933817d8bc777">[ ] unverified</a> | <a href="#case-in_game_visible_travel-88ccccc6a1fed2bf7844">[ ] unverified</a> | <a href="#case-in_game_visible_travel-524b89e91556ac4aa8a7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f1c3d5903b118f13b235">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out | — | <a href="#case-in_game_visible_travel-1c93d9ac8ff075b3ae9f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a0a6268e972c5f5f9205">[ ] unverified</a> | <a href="#case-in_game_visible_travel-23338840e03f48985a5b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8ebc71043d02be97846b">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out</summary>

<a id="case-in_game_visible_travel-50007a8a544067632df8"></a>

**0° CCW: unverified** — `in_game_visible_travel-50007a8a544067632df8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-aa996420a65ef96043cb"></a>

**90° CCW: unverified** — `in_game_visible_travel-aa996420a65ef96043cb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-b0eaf8dec5b0fd80952b"></a>

**180° CCW: unverified** — `in_game_visible_travel-b0eaf8dec5b0fd80952b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-1211672a95d2d4362be6"></a>

**270° CCW: unverified** — `in_game_visible_travel-1211672a95d2d4362be6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out</summary>

<a id="case-in_game_visible_travel-44b900d2419028db3d9c"></a>

**0° CCW: unverified** — `in_game_visible_travel-44b900d2419028db3d9c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-29c1afbd6a548d090e9e"></a>

**90° CCW: unverified** — `in_game_visible_travel-29c1afbd6a548d090e9e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-8ccc987288ddc2a079b8"></a>

**180° CCW: unverified** — `in_game_visible_travel-8ccc987288ddc2a079b8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-34ea0fcc80492f29af5a"></a>

**270° CCW: unverified** — `in_game_visible_travel-34ea0fcc80492f29af5a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out</summary>

<a id="case-in_game_visible_travel-7347234933817d8bc777"></a>

**0° CCW: unverified** — `in_game_visible_travel-7347234933817d8bc777`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-88ccccc6a1fed2bf7844"></a>

**90° CCW: unverified** — `in_game_visible_travel-88ccccc6a1fed2bf7844`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-524b89e91556ac4aa8a7"></a>

**180° CCW: unverified** — `in_game_visible_travel-524b89e91556ac4aa8a7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-f1c3d5903b118f13b235"></a>

**270° CCW: unverified** — `in_game_visible_travel-f1c3d5903b118f13b235`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out</summary>

<a id="case-in_game_visible_travel-1c93d9ac8ff075b3ae9f"></a>

**0° CCW: unverified** — `in_game_visible_travel-1c93d9ac8ff075b3ae9f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-a0a6268e972c5f5f9205"></a>

**90° CCW: unverified** — `in_game_visible_travel-a0a6268e972c5f5f9205`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-23338840e03f48985a5b"></a>

**180° CCW: unverified** — `in_game_visible_travel-23338840e03f48985a5b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-8ebc71043d02be97846b"></a>

**270° CCW: unverified** — `in_game_visible_travel-8ebc71043d02be97846b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — ghsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: ghsr; role: primary; journey: 7:ghsr-track-01-in>ghsr-track-01-out; entry: ghsr-track-01-in; exit: ghsr-track-01-out | — | <a href="#case-in_game_route_query-f580ac96a57572891d18">[ ] unverified</a> | <a href="#case-in_game_route_query-79997a65b678eaacb23f">[ ] unverified</a> | <a href="#case-in_game_route_query-10353b452c29ea4c591a">[ ] unverified</a> | <a href="#case-in_game_route_query-d16d43c7f29ccf160a19">[ ] unverified</a> |
| **Route Query**<br>Service: ghsr; role: primary; journey: 7:ghsr-track-02-in>ghsr-track-02-out; entry: ghsr-track-02-in; exit: ghsr-track-02-out | — | <a href="#case-in_game_route_query-49a14201b3d53a972e04">[ ] unverified</a> | <a href="#case-in_game_route_query-7ede89e0b72733ff5b51">[ ] unverified</a> | <a href="#case-in_game_route_query-83f76b1e9c918db4845e">[ ] unverified</a> | <a href="#case-in_game_route_query-e0333fb0e7a4097e76d7">[ ] unverified</a> |


<details>
<summary>Route Query — Service: ghsr; role: primary; journey: 7:ghsr-track-01-in>ghsr-track-01-out; entry: ghsr-track-01-in; exit: ghsr-track-01-out</summary>

<a id="case-in_game_route_query-f580ac96a57572891d18"></a>

**0° CCW: unverified** — `in_game_route_query-f580ac96a57572891d18`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-01-in>ghsr-track-01-out; entry: ghsr-track-01-in; exit: ghsr-track-01-out.

No observation recorded.

<a id="case-in_game_route_query-79997a65b678eaacb23f"></a>

**90° CCW: unverified** — `in_game_route_query-79997a65b678eaacb23f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-01-in>ghsr-track-01-out; entry: ghsr-track-01-in; exit: ghsr-track-01-out.

No observation recorded.

<a id="case-in_game_route_query-10353b452c29ea4c591a"></a>

**180° CCW: unverified** — `in_game_route_query-10353b452c29ea4c591a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-01-in>ghsr-track-01-out; entry: ghsr-track-01-in; exit: ghsr-track-01-out.

No observation recorded.

<a id="case-in_game_route_query-d16d43c7f29ccf160a19"></a>

**270° CCW: unverified** — `in_game_route_query-d16d43c7f29ccf160a19`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-01-in>ghsr-track-01-out; entry: ghsr-track-01-in; exit: ghsr-track-01-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: ghsr; role: primary; journey: 7:ghsr-track-02-in>ghsr-track-02-out; entry: ghsr-track-02-in; exit: ghsr-track-02-out</summary>

<a id="case-in_game_route_query-49a14201b3d53a972e04"></a>

**0° CCW: unverified** — `in_game_route_query-49a14201b3d53a972e04`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-02-in>ghsr-track-02-out; entry: ghsr-track-02-in; exit: ghsr-track-02-out.

No observation recorded.

<a id="case-in_game_route_query-7ede89e0b72733ff5b51"></a>

**90° CCW: unverified** — `in_game_route_query-7ede89e0b72733ff5b51`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-02-in>ghsr-track-02-out; entry: ghsr-track-02-in; exit: ghsr-track-02-out.

No observation recorded.

<a id="case-in_game_route_query-83f76b1e9c918db4845e"></a>

**180° CCW: unverified** — `in_game_route_query-83f76b1e9c918db4845e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-02-in>ghsr-track-02-out; entry: ghsr-track-02-in; exit: ghsr-track-02-out.

No observation recorded.

<a id="case-in_game_route_query-e0333fb0e7a4097e76d7"></a>

**270° CCW: unverified** — `in_game_route_query-e0333fb0e7a4097e76d7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-02-in>ghsr-track-02-out; entry: ghsr-track-02-in; exit: ghsr-track-02-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — ghsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: ghsr; role: primary; journey: 7:ghsr-track-01-in>ghsr-track-01-out; entry: ghsr-track-01-in; exit: ghsr-track-01-out | — | <a href="#case-in_game_visible_travel-f580ac96a57572891d18">[ ] unverified</a> | <a href="#case-in_game_visible_travel-79997a65b678eaacb23f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-10353b452c29ea4c591a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d16d43c7f29ccf160a19">[ ] unverified</a> |
| **Visible travel**<br>Service: ghsr; role: primary; journey: 7:ghsr-track-02-in>ghsr-track-02-out; entry: ghsr-track-02-in; exit: ghsr-track-02-out | — | <a href="#case-in_game_visible_travel-49a14201b3d53a972e04">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7ede89e0b72733ff5b51">[ ] unverified</a> | <a href="#case-in_game_visible_travel-83f76b1e9c918db4845e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e0333fb0e7a4097e76d7">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: ghsr; role: primary; journey: 7:ghsr-track-01-in>ghsr-track-01-out; entry: ghsr-track-01-in; exit: ghsr-track-01-out</summary>

<a id="case-in_game_visible_travel-f580ac96a57572891d18"></a>

**0° CCW: unverified** — `in_game_visible_travel-f580ac96a57572891d18`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-01-in>ghsr-track-01-out; entry: ghsr-track-01-in; exit: ghsr-track-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-79997a65b678eaacb23f"></a>

**90° CCW: unverified** — `in_game_visible_travel-79997a65b678eaacb23f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-01-in>ghsr-track-01-out; entry: ghsr-track-01-in; exit: ghsr-track-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-10353b452c29ea4c591a"></a>

**180° CCW: unverified** — `in_game_visible_travel-10353b452c29ea4c591a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-01-in>ghsr-track-01-out; entry: ghsr-track-01-in; exit: ghsr-track-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-d16d43c7f29ccf160a19"></a>

**270° CCW: unverified** — `in_game_visible_travel-d16d43c7f29ccf160a19`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-01-in>ghsr-track-01-out; entry: ghsr-track-01-in; exit: ghsr-track-01-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: ghsr; role: primary; journey: 7:ghsr-track-02-in>ghsr-track-02-out; entry: ghsr-track-02-in; exit: ghsr-track-02-out</summary>

<a id="case-in_game_visible_travel-49a14201b3d53a972e04"></a>

**0° CCW: unverified** — `in_game_visible_travel-49a14201b3d53a972e04`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-02-in>ghsr-track-02-out; entry: ghsr-track-02-in; exit: ghsr-track-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-7ede89e0b72733ff5b51"></a>

**90° CCW: unverified** — `in_game_visible_travel-7ede89e0b72733ff5b51`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-02-in>ghsr-track-02-out; entry: ghsr-track-02-in; exit: ghsr-track-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-83f76b1e9c918db4845e"></a>

**180° CCW: unverified** — `in_game_visible_travel-83f76b1e9c918db4845e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-02-in>ghsr-track-02-out; entry: ghsr-track-02-in; exit: ghsr-track-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-e0333fb0e7a4097e76d7"></a>

**270° CCW: unverified** — `in_game_visible_travel-e0333fb0e7a4097e76d7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-02-in>ghsr-track-02-out; entry: ghsr-track-02-in; exit: ghsr-track-02-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 48 cases; unverified: 48</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-45f059bf181db717a926">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7fb8ecc5b0ad06e442ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-783447a3a76074de68f3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4f8b46f0ac73a41b0b8f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a7de1380b7962e8558f5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-23a33549ddff6eda1825">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d8265a53c01a23733390">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0ad673d8e71f1b395e76">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f42df378907f4c211abe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-07b241c3b20c7d037744">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-37328acf6c1794fbe632">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-417922daa94de5f026fe">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2724a235ab3f02da74bf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a315e677f61922e9275a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7edb56b850239344232c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fc192aa9bb320963573a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c7ee9e0084c4a78c3b17">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f1f9d7ce08b7811e54e0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-36f49d4920ccf8865ae8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9bfb299e928add8e7732">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-508ac88655ecfebf0cce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ad7b46450168a251c7ab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5086adfe3d3ed943dcb1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a3f647a780c155e45279">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-be6b0868d6028c04575b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-94b13b7ea64a26348f59">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-55563cafe0169857f354">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ecd4ef23c52be71a4ed3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e85de43b6232aced084c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6087b8a46ed255506a1d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f648479b0b205e2e2e6f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e29df64fd67040f9698c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b3b2fa4fc3cbbe7025ac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-581fccf9f9c6cd812f00">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6925fa65e746058f9f40">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0c70dddb10bc4b14d8ae">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cc56eece15cb2745efa7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5666eb7c1739c552e8d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-732bf43f0dcce8278e13">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6e68f7bc992ff4687c8e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-374795d2fe615b8a8fb7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-165fae4dd392f8650c44">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-96a1a3544db88848a31d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a49a36ae5892cb416527">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-65a8b8ce22622a926fee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-206f314788dbb3caa300">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4c4cb84ac4c35c995f61">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c1f8647f343e5c1a2a32">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-45f059bf181db717a926"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-45f059bf181db717a926`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7fb8ecc5b0ad06e442ba"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7fb8ecc5b0ad06e442ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-783447a3a76074de68f3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-783447a3a76074de68f3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4f8b46f0ac73a41b0b8f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4f8b46f0ac73a41b0b8f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a7de1380b7962e8558f5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a7de1380b7962e8558f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-23a33549ddff6eda1825"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-23a33549ddff6eda1825`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d8265a53c01a23733390"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d8265a53c01a23733390`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0ad673d8e71f1b395e76"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0ad673d8e71f1b395e76`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f42df378907f4c211abe"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f42df378907f4c211abe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-07b241c3b20c7d037744"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-07b241c3b20c7d037744`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-37328acf6c1794fbe632"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-37328acf6c1794fbe632`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-417922daa94de5f026fe"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-417922daa94de5f026fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2724a235ab3f02da74bf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2724a235ab3f02da74bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a315e677f61922e9275a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a315e677f61922e9275a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7edb56b850239344232c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7edb56b850239344232c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fc192aa9bb320963573a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fc192aa9bb320963573a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c7ee9e0084c4a78c3b17"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c7ee9e0084c4a78c3b17`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f1f9d7ce08b7811e54e0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f1f9d7ce08b7811e54e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-36f49d4920ccf8865ae8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-36f49d4920ccf8865ae8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9bfb299e928add8e7732"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9bfb299e928add8e7732`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-508ac88655ecfebf0cce"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-508ac88655ecfebf0cce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ad7b46450168a251c7ab"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ad7b46450168a251c7ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5086adfe3d3ed943dcb1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5086adfe3d3ed943dcb1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a3f647a780c155e45279"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a3f647a780c155e45279`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-be6b0868d6028c04575b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-be6b0868d6028c04575b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-94b13b7ea64a26348f59"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-94b13b7ea64a26348f59`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-55563cafe0169857f354"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-55563cafe0169857f354`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ecd4ef23c52be71a4ed3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ecd4ef23c52be71a4ed3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e85de43b6232aced084c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e85de43b6232aced084c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6087b8a46ed255506a1d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6087b8a46ed255506a1d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f648479b0b205e2e2e6f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f648479b0b205e2e2e6f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e29df64fd67040f9698c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e29df64fd67040f9698c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b3b2fa4fc3cbbe7025ac"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b3b2fa4fc3cbbe7025ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-581fccf9f9c6cd812f00"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-581fccf9f9c6cd812f00`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6925fa65e746058f9f40"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6925fa65e746058f9f40`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0c70dddb10bc4b14d8ae"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0c70dddb10bc4b14d8ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cc56eece15cb2745efa7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cc56eece15cb2745efa7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5666eb7c1739c552e8d4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5666eb7c1739c552e8d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-732bf43f0dcce8278e13"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-732bf43f0dcce8278e13`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6e68f7bc992ff4687c8e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6e68f7bc992ff4687c8e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-374795d2fe615b8a8fb7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-374795d2fe615b8a8fb7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-165fae4dd392f8650c44"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-165fae4dd392f8650c44`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-96a1a3544db88848a31d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-96a1a3544db88848a31d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a49a36ae5892cb416527"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a49a36ae5892cb416527`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-65a8b8ce22622a926fee"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-65a8b8ce22622a926fee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-206f314788dbb3caa300"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-206f314788dbb3caa300`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4c4cb84ac4c35c995f61"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4c4cb84ac4c35c995f61`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c1f8647f343e5c1a2a32"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c1f8647f343e5c1a2a32`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → ghsr — 32 cases; unverified: 32</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: lower-lane-01-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a969ca3320f93626d158">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0e89008180679e53b1cc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6041133f0745544a48da">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-24952a295a2cf00404c9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e2fc0e6bcc8302bc0d7e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-524e735ebbdb387ab120">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-27fc2a1c88b8bbe44d84">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9016e9e6a5a0bbf1b2da">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-170853adb921b007819f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9597ff76dfb08b705c40">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9a32551aa774fc3a85c4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e0a1519a5441fbc8a4e8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bd07f2a9933a850f1cda">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6e856ee54aa4351cf7ef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7053132fcabf7df3b9a6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4b2e36e444b8f0455155">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-605614f264283571e5c1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1a6e2e2f651713543496">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-82cb4210d68c55e73afd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6cac06d6ad98d35bb021">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-51e1f870858af73e35d9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-63d34fa507244441ac5c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5b49f10fe35059f7e7b2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-618e2b513213f44be0e2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ea45fba00ba56901ac65">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5b3daa9001d94627b653">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3a2cd675bee71a620bfc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5e3d053ffab4b45771b6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3979105d31e892d07ba0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5b101280e5c73caed147">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-452c33d18f83a2716818">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe5107da0ae0642a81ef">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: lower-lane-01-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a969ca3320f93626d158"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a969ca3320f93626d158`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0e89008180679e53b1cc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0e89008180679e53b1cc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6041133f0745544a48da"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6041133f0745544a48da`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-24952a295a2cf00404c9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-24952a295a2cf00404c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e2fc0e6bcc8302bc0d7e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e2fc0e6bcc8302bc0d7e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-524e735ebbdb387ab120"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-524e735ebbdb387ab120`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-27fc2a1c88b8bbe44d84"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-27fc2a1c88b8bbe44d84`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9016e9e6a5a0bbf1b2da"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9016e9e6a5a0bbf1b2da`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-170853adb921b007819f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-170853adb921b007819f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9597ff76dfb08b705c40"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9597ff76dfb08b705c40`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9a32551aa774fc3a85c4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9a32551aa774fc3a85c4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e0a1519a5441fbc8a4e8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e0a1519a5441fbc8a4e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bd07f2a9933a850f1cda"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bd07f2a9933a850f1cda`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6e856ee54aa4351cf7ef"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6e856ee54aa4351cf7ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7053132fcabf7df3b9a6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7053132fcabf7df3b9a6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4b2e36e444b8f0455155"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4b2e36e444b8f0455155`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-605614f264283571e5c1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-605614f264283571e5c1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1a6e2e2f651713543496"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1a6e2e2f651713543496`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-82cb4210d68c55e73afd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-82cb4210d68c55e73afd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6cac06d6ad98d35bb021"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6cac06d6ad98d35bb021`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-51e1f870858af73e35d9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-51e1f870858af73e35d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-63d34fa507244441ac5c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-63d34fa507244441ac5c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5b49f10fe35059f7e7b2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5b49f10fe35059f7e7b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-618e2b513213f44be0e2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-618e2b513213f44be0e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ea45fba00ba56901ac65"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ea45fba00ba56901ac65`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5b3daa9001d94627b653"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5b3daa9001d94627b653`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3a2cd675bee71a620bfc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3a2cd675bee71a620bfc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5e3d053ffab4b45771b6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5e3d053ffab4b45771b6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3979105d31e892d07ba0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3979105d31e892d07ba0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5b101280e5c73caed147"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5b101280e5c73caed147`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-452c33d18f83a2716818"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-452c33d18f83a2716818`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fe5107da0ae0642a81ef"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fe5107da0ae0642a81ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — ghsr → road — 32 cases; unverified: 32</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: ghsr-track-01-in; to port: upper-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bab76ce828cd6135a04b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7b3e1401a2fee057e86f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d1600339c98f54a7bcd6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-68591a60fa55ad06aef2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: ghsr-track-01-in; to port: upper-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6a41ada2f45097aae57b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d2865b90b33b5181948c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0035791e45adb748913">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b9fde6172340bada223e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: ghsr-track-01-in; to port: lower-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-18a048ff1c8870a9063e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-17dbe555605dcdcc4045">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c2818b836391cd7aa88a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-67d4bef201937528f654">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: ghsr-track-01-in; to port: lower-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a890c4828d37837e9d8b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-46eac06798a1a0de34d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6beae0e5c35d3a652fb1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-74f616326ae5d89c656f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: ghsr-track-02-in; to port: upper-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-282438b99d4e8781b47d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d55925da988b8fdb7b63">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5c9ad66fde37b820db65">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0ae929f071701ab4fb6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: ghsr-track-02-in; to port: upper-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f2339573871c905bc194">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-557b00304de48ed1192a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4d30e014c93483369609">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4ddb02c13e7d0777b29b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: ghsr-track-02-in; to port: lower-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1ec5a0e2b6a5ead1a3d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eff2042b5d4275473f52">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ce2d357c1118df8a91ad">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-64a86fc6d645a1b9b0e9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: ghsr-track-02-in; to port: lower-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-daf6c3f8e24f5b2ac783">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ab6000fbe64458940edc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d7240ef566ca443a8899">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-862c5089ae67d6767304">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: ghsr-track-01-in; to port: upper-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bab76ce828cd6135a04b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bab76ce828cd6135a04b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: upper-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7b3e1401a2fee057e86f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7b3e1401a2fee057e86f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: upper-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d1600339c98f54a7bcd6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d1600339c98f54a7bcd6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: upper-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-68591a60fa55ad06aef2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-68591a60fa55ad06aef2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: upper-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: ghsr-track-01-in; to port: upper-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6a41ada2f45097aae57b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6a41ada2f45097aae57b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: upper-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d2865b90b33b5181948c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d2865b90b33b5181948c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: upper-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0035791e45adb748913"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f0035791e45adb748913`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: upper-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b9fde6172340bada223e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b9fde6172340bada223e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: upper-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: ghsr-track-01-in; to port: lower-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-18a048ff1c8870a9063e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-18a048ff1c8870a9063e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: lower-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-17dbe555605dcdcc4045"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-17dbe555605dcdcc4045`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: lower-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c2818b836391cd7aa88a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c2818b836391cd7aa88a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: lower-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-67d4bef201937528f654"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-67d4bef201937528f654`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: lower-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: ghsr-track-01-in; to port: lower-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a890c4828d37837e9d8b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a890c4828d37837e9d8b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: lower-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-46eac06798a1a0de34d1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-46eac06798a1a0de34d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: lower-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6beae0e5c35d3a652fb1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6beae0e5c35d3a652fb1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: lower-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-74f616326ae5d89c656f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-74f616326ae5d89c656f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: lower-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: ghsr-track-02-in; to port: upper-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-282438b99d4e8781b47d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-282438b99d4e8781b47d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: upper-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d55925da988b8fdb7b63"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d55925da988b8fdb7b63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: upper-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5c9ad66fde37b820db65"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5c9ad66fde37b820db65`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: upper-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0ae929f071701ab4fb6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f0ae929f071701ab4fb6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: upper-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: ghsr-track-02-in; to port: upper-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f2339573871c905bc194"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f2339573871c905bc194`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: upper-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-557b00304de48ed1192a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-557b00304de48ed1192a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: upper-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4d30e014c93483369609"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4d30e014c93483369609`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: upper-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4ddb02c13e7d0777b29b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4ddb02c13e7d0777b29b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: upper-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: ghsr-track-02-in; to port: lower-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1ec5a0e2b6a5ead1a3d1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1ec5a0e2b6a5ead1a3d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: lower-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eff2042b5d4275473f52"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-eff2042b5d4275473f52`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: lower-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ce2d357c1118df8a91ad"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ce2d357c1118df8a91ad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: lower-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-64a86fc6d645a1b9b0e9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-64a86fc6d645a1b9b0e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: lower-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: ghsr-track-02-in; to port: lower-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-daf6c3f8e24f5b2ac783"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-daf6c3f8e24f5b2ac783`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: lower-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ab6000fbe64458940edc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ab6000fbe64458940edc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: lower-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d7240ef566ca443a8899"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d7240ef566ca443a8899`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: lower-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-862c5089ae67d6767304"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-862c5089ae67d6767304`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: lower-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — ghsr → ghsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: ghsr-track-01-in; to port: ghsr-track-02-out; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-12783c955f2e740100bd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4f223f9b824f251f72f5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a2bfc5715ea7b7eba90a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-627aa33501c7ed8f8b7a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: ghsr-track-02-in; to port: ghsr-track-01-out; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-97d70eccf46a65c2ce4f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1b0f713c2c429ef04189">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fbbbc97e401b2b57f0eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-696c986e3efd5a341288">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: ghsr-track-01-in; to port: ghsr-track-02-out; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-12783c955f2e740100bd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-12783c955f2e740100bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: ghsr-track-02-out; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4f223f9b824f251f72f5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4f223f9b824f251f72f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: ghsr-track-02-out; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a2bfc5715ea7b7eba90a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a2bfc5715ea7b7eba90a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: ghsr-track-02-out; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-627aa33501c7ed8f8b7a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-627aa33501c7ed8f8b7a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: ghsr-track-02-out; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: ghsr-track-02-in; to port: ghsr-track-01-out; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-97d70eccf46a65c2ce4f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-97d70eccf46a65c2ce4f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: ghsr-track-01-out; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1b0f713c2c429ef04189"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1b0f713c2c429ef04189`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: ghsr-track-01-out; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fbbbc97e401b2b57f0eb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fbbbc97e401b2b57f0eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: ghsr-track-01-out; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-696c986e3efd5a341288"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-696c986e3efd5a341288`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: ghsr-track-01-out; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The requested function is a diagonal ground railway crossing beneath a diagonal double-decker highway, with native draggable connections on all four arms. It is delivered as one reusable two-tile crossing because both networks occupy both central tiles. Splitting those two services into separate fixed pieces would give the same city squares two owners. The neighbouring native approaches provide expansion without adding custom curves, ramps, or filler types.

The design reuses the six DD meshes from the native `5753A905` and `5753A985` crossing halves and the one valid rendered mesh from ordinary diagonal GHSR `5DC01A00`. It preserves the native visible track and highway surfaces, rather than changing their appearance to hide the measured 0.1 m internal PATH discrepancy. Two complementary DD phases and the separate Rail/Monorail GHSR markers were selected from the actual native continuation resources. Three-metre exterior collars and one-metre internal collars remove heading steps at the independently checked boundaries. The new crossing also reuses the independently checked native shadow-carrier mechanism introduced for the parallel diamond; that earlier subject's human observations are not transferred here.
