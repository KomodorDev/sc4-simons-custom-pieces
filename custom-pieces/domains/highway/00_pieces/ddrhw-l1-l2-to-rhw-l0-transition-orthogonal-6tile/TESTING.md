---
title: "Testing: DD RHW-4 \u2014 L1/L2 \u2194 RHW-4 L0 \u2014 Orthogonal Combined Transition \u2014 6 Tiles"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — L1/L2 ↔ RHW-4 L0 — Orthogonal Combined Transition — 6 Tiles

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

This scope covers the twelve owned cells of one orthogonal DD RHW-4 to ground RHW-4 transition, measuring 32 m wide × 96 m long, plus its three adjacent unowned native approach sockets. The upper DD direction begins at 15 m, moves west as it descends, and exits south on the west ground carriageway. The opposing direction enters from the east ground carriageway and climbs to the 7.5 m lower DD deck. Check two lanes in each direction: four complete directed journeys and eight exterior directional members, without lane changes, U-turns, or carriageway transfers.

The [README](README.md) defines the canonical north-up arrangement, the exact tools, and both construction orders. Require all four proper placement rotations and separate city-camera rotations. The eight cursor states repeat four physical orientations; reflections are not supported. A successful software preview or Route Query line does not establish actual game appearance, native dragging, or a moving car completing a journey.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `upper-lane-01-out` | road / 1 / primary | out | [-2.5, -88.0, 0.0]; [0.0, -1.0]; 0.0 | `path-interface-a980347eab2bc32dd576` |
| `upper-lane-02-out` | road / 1 / primary | out | [2.5, -88.0, 0.0]; [0.0, -1.0]; 0.0 | `path-interface-3cd860990d731c95fb5e` |
| `lower-lane-02-in` | road / 1 / primary | in | [13.5, -88.0, 0.0]; [0.0, 1.0]; 0.0 | `path-interface-d977a84d7a911bc0048d` |
| `lower-lane-02-out` | road / 1 / primary | out | [13.5, 8.0, 7.5]; [0.0, 1.0]; 0.0 | `path-interface-00480ef66d1c683adb2c` |
| `upper-lane-01-in` | road / 1 / primary | in | [13.5, 8.0, 15.0]; [0.0, -1.0]; 0.0 | `path-interface-aef756dec28195473947` |
| `lower-lane-01-in` | road / 1 / primary | in | [18.5, -88.0, 0.0]; [0.0, 1.0]; 0.0 | `path-interface-57700a60d1579dc24dce` |
| `lower-lane-01-out` | road / 1 / primary | out | [18.5, 8.0, 7.5]; [0.0, 1.0]; 0.0 | `path-interface-28cd03e10e6e40a3c0fa` |
| `upper-lane-02-in` | road / 1 / primary | in | [18.5, 8.0, 15.0]; [0.0, -1.0]; 0.0 | `path-interface-c5c8334a7156c02c488c` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `lower-lane-02-in` → `lower-lane-02-out` | primary |
| road | `upper-lane-01-in` → `upper-lane-01-out` | primary |
| road | `lower-lane-01-in` → `lower-lane-01-out` | primary |
| road | `upper-lane-02-in` → `upper-lane-02-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `lower-lane-02-in` | road / `upper-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-02-in` | road / `upper-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-02-in` | road / `lower-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-01-in` | road / `upper-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-01-in` | road / `lower-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-01-in` | road / `lower-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-01-in` | road / `upper-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-01-in` | road / `upper-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-01-in` | road / `lower-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-02-in` | road / `upper-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-02-in` | road / `lower-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-02-in` | road / `lower-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 1.1.641 with the audited NAM 50 right-hand-traffic dependencies. Record the actual Windows, Wine, or CrossOver environment used. The [shared build and input guide](../../../../docs/BUILD_AND_INSTALL.md) explains original-resource requirements and keeps building separate from installing. This piece requires the native DD RHW-4, RHW-4, RHW core, controller, and RHW-4 texture inputs declared in [piece.jsonc](piece.jsonc); personal input paths and native binary payloads do not belong in public evidence.

After a separately approved installation with the game fully closed, start a disposable flat test city. Reserve the README's 2 × 8 clear arrangement and at least three straight tiles beyond each native socket. Prepare a known working DD control using the normal RealHighway DD starter, and a known working opposing pair of L0 RHW-4 controls. Extend both with **RealHighway (RHW-2)**. Confirm actual traffic on those controls before using them to judge the custom adapter. The rail-based DDRHW starter and the Avenue drawing tool are outside this test.

## 3. Software checks

The saved native candidate `dist/orthogonal-ddrhw-l0-native-01` passed its independent resource checks on 1 November 2026. The [saved verification record](evidence/saved-native-verification.jsonc) identifies the exact package and checking sources: 106 resources across three DATs, twelve canonical cells, 26 PATH fragments, four complete lane journeys in all four proper rotations, all five model zooms, and the actual placement preview. It verifies 36,797 indexed triangles, fourteen complete support solids, 1,546 continuous lane segments, the complete native barriers and deck bodies, the independently reconstructed asphalt atlas, and absence of custom shadow resources. The [native input contract](evidence/native-contract.jsonc) owns the original socket and archive pins; the [accepted connector measurements](checks/accepted-connector-contract.jsonc) bind all twelve canonical PATH hashes to eight directional ports, four journeys, and twelve forbidden transfers. These are software results; human game observations are recorded separately in [chapter 5](#5-results-and-known-issues).

The native approach adapter has been checked against the original NAM 50 bytes: the DD and ground starter markers select eight existing RUL1 solutions, and eight inspected RUL2 rows continue the native highways. A transition-only helper proof preserves the original RUL1 bytes and inserts no extra solution. The five endpoint dependencies are the DD model, PATH, and network exemplar, plus the direct ground model and PATH. The measured ground lookup has no network exemplar; an installed exemplar with that target is rejected in any group. These helper checks do not establish the full compiled transition or any live-game result.

The [mirrored counterpart's test record](../ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile-mirrored/TESTING.md) owns the newer paired candidate and its exact saved-resource evidence. That candidate also checks this original type against the native joining PATHs and retains this type's resource identities and payload. Its native lane-by-lane audit covers the DD boundary and both ground carriageways in all four rotations. The original first-candidate evidence above remains retained with its original scope. Matching human game observations for each type remain separate from that software evidence; the current user confirmation is recorded in [chapter 5](#5-results-and-known-issues).

The resource author is [orthogonal_transition.py](../../implementation/scp_highway/orthogonal_transition.py), with its [geometry source](../../implementation/scp_highway/orthogonal_transition_geometry.py). The [independent verifier](../../implementation/scp_highway/orthogonal_transition_verify.py) reconstructs the lane curves and city-cell cuts separately. The [native socket adapter](../../implementation/scp_highway/orthogonal_approaches.py) and [shared helper framework](../../../../framework/scp/native_approaches.py) own the bounded construction and existing-rule contracts. Actual saved-resource acceptance must check the complete canonical PATHs, all four proper rotations, vehicle envelopes, model bodies and supports, native end seams, UV and texture transitions, construction addresses, and disabled shadow resources.

Run the following commands from the repository root. Replace `BUILD_NAME` with the exact candidate folder being reviewed. The build command writes that folder; verification and connector checking inspect the same saved candidate, without installing it. Use `python` instead of `python3` in an activated Windows Python environment.

```sh
python3 -B custom-pieces/scp.py build --include ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile --output custom-pieces/dist/BUILD_NAME
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/BUILD_NAME
python3 -B custom-pieces/scp.py connectors check --domain highway --piece ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile --build dist/BUILD_NAME
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile
python3 -B tools/run_tests.py
```

The source has 3 m minimum flat native collars. The lower descent and upper sideways movement finish at station 69 m, leaving 27 m of level lower roadway; the upper descent finishes at station 93 m. Source maximum lane-grade calculations are approximately 19.08% upper and 17.05% lower, within the declared 20% experimental ceiling. The saved-PATH verifier must measure the encoded maxima separately and retain every authored height through `UseElevation=1`. The northwest core cell `[0,0]` has a visible model and an intentionally empty PATH, rather than an invented route for capacity. Its construction still owns that cell.

## 4. Game checks

### 4.1 Fresh placement and draggable continuation

1. Place a fresh adapter on clear flat ground in the authored 0° arrangement. Inspect the single north DD socket and both south ground sockets. Cancel the tool with **Esc**, select the normal **RealHighway (RHW-2)** tool, and drag straight outward from each socket for at least three tiles. Record whether the native network continues, keeps the correct width and levels, and joins without gaps.
2. Repeat at a second site using prebuilt controls: leave the twelve core cells empty between a DD line on the north and two correctly directed ground carriageways on the south, then place the adapter in that gap. Record this result separately from drawing outward from a new piece.
3. At a third site, place the adapter facing prebuilt native approaches with short straight gaps. Start **RealHighway (RHW-2)** on an existing approach, and drag through its gap to the adjacent native socket outside the fixed core. Repeat for the DD socket and both ground sockets. Record inward dragging independently of the first two construction orders, including whether a socket fails to adopt the correct native network or a core cell changes unexpectedly.
4. Use **Home** and **End** to test 90°, 180°, and 270° placements with appropriately rotated control lines. Check that all three native sockets rotate with the model, that the two ground directions remain complementary, and that the eight cursor states repeat the same four proper arrangements. When both types are selected, use **Tab** and **Shift+Tab** to test the mirrored counterpart separately; the placement-query name must identify the selected shape.

### 4.2 Route Query and actual moving cars

1. Join the control lines to occupied development and useful destinations on each side, and allow the simulation to run. Confirm that the native control lines still show actual moving traffic.
2. Select **Route Query**, click each relevant carriageway, and record the displayed routes separately for both directions. The upper DD direction must continue to the west ground carriageway; the east ground direction must continue to the lower DD deck in the authored frame. Translate those directions with the chosen piece rotation.
3. Follow actual cars from the last native tile into the adapter, through the full descent or climb, and into the next native tile. Inspect both lanes in each direction. Record the exact cell and rotation if a car stops, disappears, follows the wrong deck, changes height abruptly, or clips a barrier or support. A coloured route alone cannot pass this step.
4. Check that cars cannot U-turn, transfer to the opposing carriageway, or switch to a different lane inside the fixed adapter. Repeat the allowed journeys after rotating the piece through all four proper orientations.

### 4.3 Appearance, shadows, and object lifetime

1. Inspect every zoom and all four city-camera views. Look for a continuous asphalt transition, correctly aligned lane markings, joined native end barriers, complete support solids, and adequate separation between the two carriageways. Distinguish camera rotation from placement rotation.
2. Compare Medium and High shadow settings. The adapter intentionally supplies no cast shadows, so record any detached triangle, residual deck-shaped shadow, or phantom structure separately from shadows cast by neighbouring objects. The absence of shadows in a low-quality view alone does not pass the other settings.
3. Save the disposable city, quit the game fully, reopen it, and repeat the route, moving-car, height, and shadow checks. Redraw the native approaches and check that the custom core remains intact.
4. Demolish the adapter, then inspect the twelve former owned cells and the three native sockets separately. Record any leftover model, marker, or shadow. Rebuild the native controls, place a fresh adapter, and repeat a journey in each direction.

Record only explicit matching observations through [the shared testing procedure](../../../../docs/TESTING.md). Earlier tests of a diagonal diamond, a GHSR crossing, or a sidewalk probe cannot pass this adapter's game cases.

## 5. Results and known issues

The transition retains its experimental source status. The saved native checks establish the bounded software results in [chapter 3](#3-software-checks), including the original rule and dependency contract, the complete saved geometry, and its lane paths. The user’s game confirmation below is separate evidence, bound to this original transition’s own cases and resources.

The 96 m length and steep source profiles are compact game-design choices. They are not road-design recommendations or proof of real structural capacity. The independent car envelope is 2.5 m wide × 3.8 m high; geometric checks against that declared envelope do not measure every replacement vehicle. This piece has no Avenue, pedestrian route, adaptive sidewalk, or internal interchangeable ramp socket.

On 1 November 2026, the user explicitly reported: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”. This is recorded as aggregate acceptance of the declared game checks for both six-tile transition shapes in installed candidate `dist/all-pieces-hsr-highway-menu-02`, manifest SHA-256 `cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0`. This subject’s 96 current game cases cover its four declared proper placement rotations and retain their individual directions, services, and dependency fingerprints. The tested setup is Windows SimCity 4 Deluxe 1.1.641 with NAM 50 and right-hand traffic through Wine/CrossOver on macOS; this confirmation does not distinguish the compatibility layer further. No individual case narrative, screenshot, city name, or old-instance cleanup result was supplied. Preview-image reviews and software-case observations are outside this human game confirmation and retain their previous states. The authoritative [observation record](checks/manual-tests.json) preserves the exact statement and build binding for every recorded case.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/3 applicable cases passed; 0 failed, 0 stale.
- [x] In-game rendering: 4/4 applicable cases passed; 0 failed, 0 stale.
- [x] Route Query: 16/16 applicable cases passed; 0 failed, 0 stale.
- [x] Visible travel: 16/16 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 5, passed: 96, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-9cc2be9312108b11e410">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-9cc2be9312108b11e410"></a>

**General: unverified** — `software_resources-9cc2be9312108b11e410`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-9cc2be9312108b11e410">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-9cc2be9312108b11e410"></a>

**General: unverified** — `software_connectivity-9cc2be9312108b11e410`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile:canonical-southeast | <a href="#case-preview_review-163c8cee529a68ec555c">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile:canonical-top | <a href="#case-preview_review-d76067c5f36774ccbc60">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile:connection-overview | <a href="#case-preview_review-a97c776bf96cd886aae7">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile:canonical-southeast</summary>

<a id="case-preview_review-163c8cee529a68ec555c"></a>

**General: unverified** — `preview_review-163c8cee529a68ec555c`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile:canonical-top</summary>

<a id="case-preview_review-d76067c5f36774ccbc60"></a>

**General: unverified** — `preview_review-d76067c5f36774ccbc60`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile:connection-overview</summary>

<a id="case-preview_review-a97c776bf96cd886aae7"></a>

**General: unverified** — `preview_review-a97c776bf96cd886aae7`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile:connection-overview.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; passed: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-82d7c3784103b584b40a">[x] passed</a> | <a href="#case-in_game_render-c1d128032d9ca5cf979a">[x] passed</a> | <a href="#case-in_game_render-069c51581858ce31329c">[x] passed</a> | <a href="#case-in_game_render-34a29357ca44d9f2d5e3">[x] passed</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-82d7c3784103b584b40a"></a>

**0° CCW: passed** — `in_game_render-82d7c3784103b584b40a`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_render-c1d128032d9ca5cf979a"></a>

**90° CCW: passed** — `in_game_render-c1d128032d9ca5cf979a`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_render-069c51581858ce31329c"></a>

**180° CCW: passed** — `in_game_render-069c51581858ce31329c`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_render-34a29357ca44d9f2d5e3"></a>

**270° CCW: passed** — `in_game_render-34a29357ca44d9f2d5e3`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; passed: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-82d7c3784103b584b40a">[x] passed</a> | <a href="#case-in_game_placement-c1d128032d9ca5cf979a">[x] passed</a> | <a href="#case-in_game_placement-069c51581858ce31329c">[x] passed</a> | <a href="#case-in_game_placement-34a29357ca44d9f2d5e3">[x] passed</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-82d7c3784103b584b40a"></a>

**0° CCW: passed** — `in_game_placement-82d7c3784103b584b40a`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_placement-c1d128032d9ca5cf979a"></a>

**90° CCW: passed** — `in_game_placement-c1d128032d9ca5cf979a`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_placement-069c51581858ce31329c"></a>

**180° CCW: passed** — `in_game_placement-069c51581858ce31329c`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_placement-34a29357ca44d9f2d5e3"></a>

**270° CCW: passed** — `in_game_placement-34a29357ca44d9f2d5e3`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; passed: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-82d7c3784103b584b40a">[x] passed</a> | <a href="#case-in_game_demolition-c1d128032d9ca5cf979a">[x] passed</a> | <a href="#case-in_game_demolition-069c51581858ce31329c">[x] passed</a> | <a href="#case-in_game_demolition-34a29357ca44d9f2d5e3">[x] passed</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-82d7c3784103b584b40a"></a>

**0° CCW: passed** — `in_game_demolition-82d7c3784103b584b40a`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_demolition-c1d128032d9ca5cf979a"></a>

**90° CCW: passed** — `in_game_demolition-c1d128032d9ca5cf979a`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_demolition-069c51581858ce31329c"></a>

**180° CCW: passed** — `in_game_demolition-069c51581858ce31329c`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_demolition-34a29357ca44d9f2d5e3"></a>

**270° CCW: passed** — `in_game_demolition-34a29357ca44d9f2d5e3`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; passed: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-82d7c3784103b584b40a">[x] passed</a> | <a href="#case-in_game_save_reload-c1d128032d9ca5cf979a">[x] passed</a> | <a href="#case-in_game_save_reload-069c51581858ce31329c">[x] passed</a> | <a href="#case-in_game_save_reload-34a29357ca44d9f2d5e3">[x] passed</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-82d7c3784103b584b40a"></a>

**0° CCW: passed** — `in_game_save_reload-82d7c3784103b584b40a`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_save_reload-c1d128032d9ca5cf979a"></a>

**90° CCW: passed** — `in_game_save_reload-c1d128032d9ca5cf979a`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_save_reload-069c51581858ce31329c"></a>

**180° CCW: passed** — `in_game_save_reload-069c51581858ce31329c`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_save_reload-34a29357ca44d9f2d5e3"></a>

**270° CCW: passed** — `in_game_save_reload-34a29357ca44d9f2d5e3`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

</details>

</details>

<details>
<summary>Route Query — road — 16 cases; passed: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out | — | <a href="#case-in_game_route_query-40232bbf2761771185ec">[x] passed</a> | <a href="#case-in_game_route_query-1c53ec57e8bf659ca320">[x] passed</a> | <a href="#case-in_game_route_query-8c9d9dd6c8279432b9af">[x] passed</a> | <a href="#case-in_game_route_query-d202487d98df62c16618">[x] passed</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out | — | <a href="#case-in_game_route_query-6799b7ff56e0c66614ef">[x] passed</a> | <a href="#case-in_game_route_query-bbbe71572e9fe268d0a1">[x] passed</a> | <a href="#case-in_game_route_query-b5a809bc72621b03af9f">[x] passed</a> | <a href="#case-in_game_route_query-32fbab435e52cd956255">[x] passed</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out | — | <a href="#case-in_game_route_query-5c0670b5c7127cba6c58">[x] passed</a> | <a href="#case-in_game_route_query-fb9ca6bdad68d76ea338">[x] passed</a> | <a href="#case-in_game_route_query-b2962a423ee6571b86cb">[x] passed</a> | <a href="#case-in_game_route_query-498acc6774b20173b671">[x] passed</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out | — | <a href="#case-in_game_route_query-0ee7de8c4d85354d08d7">[x] passed</a> | <a href="#case-in_game_route_query-50dd2a2f4ecb1eb1833c">[x] passed</a> | <a href="#case-in_game_route_query-559ed58f87000f5a69df">[x] passed</a> | <a href="#case-in_game_route_query-5d7c61ac47e61fcf0a7b">[x] passed</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out</summary>

<a id="case-in_game_route_query-40232bbf2761771185ec"></a>

**0° CCW: passed** — `in_game_route_query-40232bbf2761771185ec`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_route_query-1c53ec57e8bf659ca320"></a>

**90° CCW: passed** — `in_game_route_query-1c53ec57e8bf659ca320`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_route_query-8c9d9dd6c8279432b9af"></a>

**180° CCW: passed** — `in_game_route_query-8c9d9dd6c8279432b9af`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_route_query-d202487d98df62c16618"></a>

**270° CCW: passed** — `in_game_route_query-d202487d98df62c16618`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out</summary>

<a id="case-in_game_route_query-6799b7ff56e0c66614ef"></a>

**0° CCW: passed** — `in_game_route_query-6799b7ff56e0c66614ef`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_route_query-bbbe71572e9fe268d0a1"></a>

**90° CCW: passed** — `in_game_route_query-bbbe71572e9fe268d0a1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_route_query-b5a809bc72621b03af9f"></a>

**180° CCW: passed** — `in_game_route_query-b5a809bc72621b03af9f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_route_query-32fbab435e52cd956255"></a>

**270° CCW: passed** — `in_game_route_query-32fbab435e52cd956255`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out</summary>

<a id="case-in_game_route_query-5c0670b5c7127cba6c58"></a>

**0° CCW: passed** — `in_game_route_query-5c0670b5c7127cba6c58`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_route_query-fb9ca6bdad68d76ea338"></a>

**90° CCW: passed** — `in_game_route_query-fb9ca6bdad68d76ea338`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_route_query-b2962a423ee6571b86cb"></a>

**180° CCW: passed** — `in_game_route_query-b2962a423ee6571b86cb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_route_query-498acc6774b20173b671"></a>

**270° CCW: passed** — `in_game_route_query-498acc6774b20173b671`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out</summary>

<a id="case-in_game_route_query-0ee7de8c4d85354d08d7"></a>

**0° CCW: passed** — `in_game_route_query-0ee7de8c4d85354d08d7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_route_query-50dd2a2f4ecb1eb1833c"></a>

**90° CCW: passed** — `in_game_route_query-50dd2a2f4ecb1eb1833c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_route_query-559ed58f87000f5a69df"></a>

**180° CCW: passed** — `in_game_route_query-559ed58f87000f5a69df`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_route_query-5d7c61ac47e61fcf0a7b"></a>

**270° CCW: passed** — `in_game_route_query-5d7c61ac47e61fcf0a7b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

</details>

</details>

<details>
<summary>Visible travel — road — 16 cases; passed: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out | — | <a href="#case-in_game_visible_travel-40232bbf2761771185ec">[x] passed</a> | <a href="#case-in_game_visible_travel-1c53ec57e8bf659ca320">[x] passed</a> | <a href="#case-in_game_visible_travel-8c9d9dd6c8279432b9af">[x] passed</a> | <a href="#case-in_game_visible_travel-d202487d98df62c16618">[x] passed</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out | — | <a href="#case-in_game_visible_travel-6799b7ff56e0c66614ef">[x] passed</a> | <a href="#case-in_game_visible_travel-bbbe71572e9fe268d0a1">[x] passed</a> | <a href="#case-in_game_visible_travel-b5a809bc72621b03af9f">[x] passed</a> | <a href="#case-in_game_visible_travel-32fbab435e52cd956255">[x] passed</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out | — | <a href="#case-in_game_visible_travel-5c0670b5c7127cba6c58">[x] passed</a> | <a href="#case-in_game_visible_travel-fb9ca6bdad68d76ea338">[x] passed</a> | <a href="#case-in_game_visible_travel-b2962a423ee6571b86cb">[x] passed</a> | <a href="#case-in_game_visible_travel-498acc6774b20173b671">[x] passed</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out | — | <a href="#case-in_game_visible_travel-0ee7de8c4d85354d08d7">[x] passed</a> | <a href="#case-in_game_visible_travel-50dd2a2f4ecb1eb1833c">[x] passed</a> | <a href="#case-in_game_visible_travel-559ed58f87000f5a69df">[x] passed</a> | <a href="#case-in_game_visible_travel-5d7c61ac47e61fcf0a7b">[x] passed</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out</summary>

<a id="case-in_game_visible_travel-40232bbf2761771185ec"></a>

**0° CCW: passed** — `in_game_visible_travel-40232bbf2761771185ec`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_visible_travel-1c53ec57e8bf659ca320"></a>

**90° CCW: passed** — `in_game_visible_travel-1c53ec57e8bf659ca320`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_visible_travel-8c9d9dd6c8279432b9af"></a>

**180° CCW: passed** — `in_game_visible_travel-8c9d9dd6c8279432b9af`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_visible_travel-d202487d98df62c16618"></a>

**270° CCW: passed** — `in_game_visible_travel-d202487d98df62c16618`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out</summary>

<a id="case-in_game_visible_travel-6799b7ff56e0c66614ef"></a>

**0° CCW: passed** — `in_game_visible_travel-6799b7ff56e0c66614ef`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_visible_travel-bbbe71572e9fe268d0a1"></a>

**90° CCW: passed** — `in_game_visible_travel-bbbe71572e9fe268d0a1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_visible_travel-b5a809bc72621b03af9f"></a>

**180° CCW: passed** — `in_game_visible_travel-b5a809bc72621b03af9f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_visible_travel-32fbab435e52cd956255"></a>

**270° CCW: passed** — `in_game_visible_travel-32fbab435e52cd956255`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out</summary>

<a id="case-in_game_visible_travel-5c0670b5c7127cba6c58"></a>

**0° CCW: passed** — `in_game_visible_travel-5c0670b5c7127cba6c58`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_visible_travel-fb9ca6bdad68d76ea338"></a>

**90° CCW: passed** — `in_game_visible_travel-fb9ca6bdad68d76ea338`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_visible_travel-b2962a423ee6571b86cb"></a>

**180° CCW: passed** — `in_game_visible_travel-b2962a423ee6571b86cb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_visible_travel-498acc6774b20173b671"></a>

**270° CCW: passed** — `in_game_visible_travel-498acc6774b20173b671`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out</summary>

<a id="case-in_game_visible_travel-0ee7de8c4d85354d08d7"></a>

**0° CCW: passed** — `in_game_visible_travel-0ee7de8c4d85354d08d7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_visible_travel-50dd2a2f4ecb1eb1833c"></a>

**90° CCW: passed** — `in_game_visible_travel-50dd2a2f4ecb1eb1833c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_visible_travel-559ed58f87000f5a69df"></a>

**180° CCW: passed** — `in_game_visible_travel-559ed58f87000f5a69df`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_visible_travel-5d7c61ac47e61fcf0a7b"></a>

**270° CCW: passed** — `in_game_visible_travel-5d7c61ac47e61fcf0a7b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 48 cases; passed: 48</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-21ccc86ba4330692e461">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-98b2d356ad84c4256034">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-0625d2ce9cb3cec91ba0">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-27a9d06dfd64151fac3b">[x] passed</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2552a31910f97d383d4d">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-d1725eb8953a4ca81a49">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-51fb350030201974d91f">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-3f0bb3372d2901c75eca">[x] passed</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c140df69d24caf867419">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-a0c51b39059eb0f6e7ec">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-4d95adede625aebb47b5">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-7988e97095ea9386e463">[x] passed</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dcfb5ce89b33c2bf3755">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-e0aaae3da63814847507">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-ceeff5aa4c2c15f3b9b9">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-da3a05b067f77f373a7e">[x] passed</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e7a07bb3b4f03741298a">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-4877bff976545a81ed82">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-142cfbbed56b86378008">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-98dd34937dafe194d813">[x] passed</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7e9ec79bb046aa92c461">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-f0a15d6e912ef24b719c">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-49a6199945ea093b7dd0">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-c75b7fa22067fda61e1d">[x] passed</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6305b8695458c22c1b49">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-63d0cbcd49a147e00e0d">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-302a5691267d593b567a">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-aadc3e76c993e41aa9ff">[x] passed</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6ab7264e7a0a47a279c9">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-ba0482901ce033baa159">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-242bc4aeaa8da545dc97">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-5b146b15df3b2e83df9f">[x] passed</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c48e3bc5a7e670ff4db9">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-fb1ddcd9388d4cf0fc7e">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-e8b6883fa432f62f9b7c">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-8ee52cd8cb702ac96840">[x] passed</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ba1487ac29580cf0b9a6">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-4ab4a168bf516c3dfde1">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-0882e342914e68ed2cf2">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-2f989640bccd95d344f2">[x] passed</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-063c7f4087ae5435a8c7">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-33af33808c2bcc644b3e">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-f9b4ff997969284a2627">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-9871e8305d6a004622b0">[x] passed</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-95feddc024406ea84348">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-3706bcb07ef7994c484e">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-d5a3384086361647725a">[x] passed</a> | <a href="#case-in_game_forbidden_transfer-3ec1ba7306a3fa6ec668">[x] passed</a> |


<details>
<summary>Forbidden transfer — from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-21ccc86ba4330692e461"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-21ccc86ba4330692e461`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-98b2d356ad84c4256034"></a>

**90° CCW: passed** — `in_game_forbidden_transfer-98b2d356ad84c4256034`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-0625d2ce9cb3cec91ba0"></a>

**180° CCW: passed** — `in_game_forbidden_transfer-0625d2ce9cb3cec91ba0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-27a9d06dfd64151fac3b"></a>

**270° CCW: passed** — `in_game_forbidden_transfer-27a9d06dfd64151fac3b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2552a31910f97d383d4d"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-2552a31910f97d383d4d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-d1725eb8953a4ca81a49"></a>

**90° CCW: passed** — `in_game_forbidden_transfer-d1725eb8953a4ca81a49`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-51fb350030201974d91f"></a>

**180° CCW: passed** — `in_game_forbidden_transfer-51fb350030201974d91f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-3f0bb3372d2901c75eca"></a>

**270° CCW: passed** — `in_game_forbidden_transfer-3f0bb3372d2901c75eca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c140df69d24caf867419"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-c140df69d24caf867419`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-a0c51b39059eb0f6e7ec"></a>

**90° CCW: passed** — `in_game_forbidden_transfer-a0c51b39059eb0f6e7ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-4d95adede625aebb47b5"></a>

**180° CCW: passed** — `in_game_forbidden_transfer-4d95adede625aebb47b5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-7988e97095ea9386e463"></a>

**270° CCW: passed** — `in_game_forbidden_transfer-7988e97095ea9386e463`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dcfb5ce89b33c2bf3755"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-dcfb5ce89b33c2bf3755`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-e0aaae3da63814847507"></a>

**90° CCW: passed** — `in_game_forbidden_transfer-e0aaae3da63814847507`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-ceeff5aa4c2c15f3b9b9"></a>

**180° CCW: passed** — `in_game_forbidden_transfer-ceeff5aa4c2c15f3b9b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-da3a05b067f77f373a7e"></a>

**270° CCW: passed** — `in_game_forbidden_transfer-da3a05b067f77f373a7e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e7a07bb3b4f03741298a"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-e7a07bb3b4f03741298a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-4877bff976545a81ed82"></a>

**90° CCW: passed** — `in_game_forbidden_transfer-4877bff976545a81ed82`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-142cfbbed56b86378008"></a>

**180° CCW: passed** — `in_game_forbidden_transfer-142cfbbed56b86378008`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-98dd34937dafe194d813"></a>

**270° CCW: passed** — `in_game_forbidden_transfer-98dd34937dafe194d813`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7e9ec79bb046aa92c461"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-7e9ec79bb046aa92c461`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-f0a15d6e912ef24b719c"></a>

**90° CCW: passed** — `in_game_forbidden_transfer-f0a15d6e912ef24b719c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-49a6199945ea093b7dd0"></a>

**180° CCW: passed** — `in_game_forbidden_transfer-49a6199945ea093b7dd0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-c75b7fa22067fda61e1d"></a>

**270° CCW: passed** — `in_game_forbidden_transfer-c75b7fa22067fda61e1d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6305b8695458c22c1b49"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-6305b8695458c22c1b49`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-63d0cbcd49a147e00e0d"></a>

**90° CCW: passed** — `in_game_forbidden_transfer-63d0cbcd49a147e00e0d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-302a5691267d593b567a"></a>

**180° CCW: passed** — `in_game_forbidden_transfer-302a5691267d593b567a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-aadc3e76c993e41aa9ff"></a>

**270° CCW: passed** — `in_game_forbidden_transfer-aadc3e76c993e41aa9ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6ab7264e7a0a47a279c9"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-6ab7264e7a0a47a279c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-ba0482901ce033baa159"></a>

**90° CCW: passed** — `in_game_forbidden_transfer-ba0482901ce033baa159`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-242bc4aeaa8da545dc97"></a>

**180° CCW: passed** — `in_game_forbidden_transfer-242bc4aeaa8da545dc97`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-5b146b15df3b2e83df9f"></a>

**270° CCW: passed** — `in_game_forbidden_transfer-5b146b15df3b2e83df9f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c48e3bc5a7e670ff4db9"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-c48e3bc5a7e670ff4db9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-fb1ddcd9388d4cf0fc7e"></a>

**90° CCW: passed** — `in_game_forbidden_transfer-fb1ddcd9388d4cf0fc7e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-e8b6883fa432f62f9b7c"></a>

**180° CCW: passed** — `in_game_forbidden_transfer-e8b6883fa432f62f9b7c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-8ee52cd8cb702ac96840"></a>

**270° CCW: passed** — `in_game_forbidden_transfer-8ee52cd8cb702ac96840`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ba1487ac29580cf0b9a6"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-ba1487ac29580cf0b9a6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-4ab4a168bf516c3dfde1"></a>

**90° CCW: passed** — `in_game_forbidden_transfer-4ab4a168bf516c3dfde1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-0882e342914e68ed2cf2"></a>

**180° CCW: passed** — `in_game_forbidden_transfer-0882e342914e68ed2cf2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-2f989640bccd95d344f2"></a>

**270° CCW: passed** — `in_game_forbidden_transfer-2f989640bccd95d344f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-063c7f4087ae5435a8c7"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-063c7f4087ae5435a8c7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-33af33808c2bcc644b3e"></a>

**90° CCW: passed** — `in_game_forbidden_transfer-33af33808c2bcc644b3e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-f9b4ff997969284a2627"></a>

**180° CCW: passed** — `in_game_forbidden_transfer-f9b4ff997969284a2627`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-9871e8305d6a004622b0"></a>

**270° CCW: passed** — `in_game_forbidden_transfer-9871e8305d6a004622b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-95feddc024406ea84348"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-95feddc024406ea84348`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-3706bcb07ef7994c484e"></a>

**90° CCW: passed** — `in_game_forbidden_transfer-3706bcb07ef7994c484e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-d5a3384086361647725a"></a>

**180° CCW: passed** — `in_game_forbidden_transfer-d5a3384086361647725a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

<a id="case-in_game_forbidden_transfer-3ec1ba7306a3fa6ec668"></a>

**270° CCW: passed** — `in_game_forbidden_transfer-3ec1ba7306a3fa6ec668`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-01; evidence: [Explicit user report on 1 November 2026: “for the DD RHW to l0 RHW all checks pass as well. same for diagonal DD RHW over GHSR”., Installed candidate manifest SHA-256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0. Its saved piece resources and canonical construction fingerprints match this current case record.]; environment: platform: Windows SimCity 4 through Wine/CrossOver on macOS; existing installed test setup; compatibility layer not further distinguished in this confirmation; game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50; right-hand traffic; installed manifest sha256: cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0; note: Aggregate all-checks confirmation for this requested subject and its delivered variants, applied to the declared game case. No individual case narrative, screenshot, city name, or more specific compatibility-layer identification was supplied. This observation does not approve preview images, software cases, other game environments, or cleanup of older saved instances.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The user requested a compact combined transition that changes width while lowering both DD directions into adjacent ground RHW-4 carriageways. The accepted six-tile proposal keeps both movements within a 2 × 6 core, retains the native DD travel directions, and uses normal native highway sockets at its three exposed ends. The upper carriageway's vertical profile compensates for its lateral curve and lane offsets, so the complete adapter is the reusable unit. Arbitrary intermediate cuts would require new standard slope, curvature, and height interfaces before they could become a modular ramp kit.

The implementation measures orthogonal native donors `57530000` and `57030000` independently of the earlier diagonal crossing work. It reuses the original NAM starter marker solutions, introduces no native RUL2 override, retains four proper rotations, and follows the current no-shadow highway policy. The owning [network specification](../../NETWORK_SPEC.md#16-orthogonal-dd-rhw-4-to-ground-rhw-4-transition) records the measured interfaces and reuse limits.
