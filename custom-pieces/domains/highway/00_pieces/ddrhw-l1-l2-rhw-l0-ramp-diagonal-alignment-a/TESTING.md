---
title: "Testing: DD RHW-4 — L1/L2 ↔ RHW-4 L0 — Diagonal Ramp — Alignment A"
summary: "Check this first diagonal alignment’s exact geometry, native interfaces, artifacts, and separately unverified game behavior."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — L1/L2 ↔ RHW-4 L0 — Diagonal Ramp — Alignment A

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Check this independently named first-A diagonal type, not a 45° picture of an orthogonal type. Preserve two lanes on each opposing DD deck, native L1/L2 heights of 7.5/15 m, all four same-lane journeys, all eight directed exterior members, native ground classes 1/2, DD classes 0/1, and driver-left yellow markings. Require all four proper rotations, exact finite native collars, full physical models and support solids, and the correctly constrained custom terrain mask.

In source pose 0°, the DD end is northeast with **upper southwest in at 15 m and lower northeast out at 7.5 m**. The upper ground road is on the **northwest** side of the lower road, carrying traffic **southwest out of the adapter**. The lower ground road carries traffic **northeast into the adapter**. Physical upper-road side, traffic direction, actual native half phase, and relative grid alignment are separate properties.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `upper-lane-01-out` | road / 1 / primary | out | [12.8, -72.0, 0.0]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `upper-lane-02-out` | road / 1 / primary | out | [19.2, -72.0, 0.0]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `lower-lane-02-in` | road / 1 / primary | in | [28.8, -88.0, 0.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `lower-lane-01-in` | road / 1 / primary | in | [35.2, -88.0, 0.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `lower-lane-01-out` | road / 1 / primary | out | [104.0, -19.2, 7.5]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `upper-lane-02-in` | road / 1 / primary | in | [104.0, -19.2, 15.0]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `lower-lane-02-out` | road / 1 / primary | out | [104.0, -12.8, 7.5]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `upper-lane-01-in` | road / 1 / primary | in | [104.0, -12.8, 15.0]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `lower-lane-02-in` → `lower-lane-02-out` | primary |
| road | `lower-lane-01-in` → `lower-lane-01-out` | primary |
| road | `upper-lane-02-in` → `upper-lane-02-out` | primary |
| road | `upper-lane-01-in` → `upper-lane-01-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `lower-lane-02-in` | road / `upper-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-02-in` | road / `upper-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-02-in` | road / `lower-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-01-in` | road / `upper-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-01-in` | road / `upper-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-01-in` | road / `lower-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-02-in` | road / `upper-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-02-in` | road / `lower-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-02-in` | road / `lower-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-01-in` | road / `upper-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-01-in` | road / `lower-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-01-in` | road / `lower-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 Deluxe 1.1.641 with the audited NAM 50 right-hand-traffic profile. Record whether Windows runs directly or through Wine/CrossOver. Use a disposable flat city and an independently checked candidate containing this exact registered identity. Close the game before replacing Plugins, restart afterward, and use a fresh placement. Preserve the four orthogonal types and their observations; a small development build is not a complete replacement for a larger managed selection.

Source positions use east, north, and height in metres. City-cell centres are (16 × column, −16 × row). The DD mouth centre is (8,0), its cut is east = 8 m, and the southwest longitudinal unit vector is (−1,−1)/√2. The southeast transverse unit is (1,−1)/√2. The fixed DD/lower-road axis is **east − north = 8 m**; the upper ground axis is **east − north = −24 m**, with mouth centre **(−80, −56) m**. The lower ground mouth centre is **(−64,−72) m**. Both ground mouths use horizontal north-edge cuts. The registered local origin is source cell **(-6,-1)**; its checked host mask has 24 cells in an **8 × 6** bounding rectangle, not a filled rectangle. The saved adapter divides those hosts into 15 routed cells and nine model-only cells, with 39 distinct terrain-corner vertices in the checked flat-base group.

| Boundary | Joining source core cell | Unowned source socket | Native donor / clockwise pose | Required directed service |
| --- | --- | --- | --- | --- |
| Northeast DD | (0,0) | (1,0) | `57530900` / 2 | upper southwest in at 15 m and lower northeast out at 7.5 m |
| Northwest upper-linked ground | (-5,3) | (-5,4) | `57030900` / 2 | Two lanes southwest out of the adapter, at 0 m |
| Main-axis lower-linked ground | (−4,4) | (-4,5) | `57030200` / 2 | Two lanes northeast into the adapter, at 0 m |

Both native diagonal halves must be checked together. The DD socket’s outward peer is source cell (1,−1), donor `57530200` at pose 0. The upper ground peer is (-6,4), donor `57030200` at pose 0, and the lower ground peer is (-5,5), donor `57030900` at pose 0. Preserve their native continuations and the [README’s clear approach corridors](README.md#21-reserve-the-core-and-native-approaches). Poses are clockwise donor quarter turns; full placement rotations have their separately labelled convention.

## 3. Software checks

### 3.1 Build and inspect the four first-A choices

All four first-A choices are registered and have passed the complete ordinary saved-DAT checks. The commands below reproduce a development build and selected artifacts; they do not install it or record a game pass. From the repository root, follow the [Python setup](../../../../docs/BUILD_AND_INSTALL.md#31-python-setup-for-a-checkout-or-source-zip), replace `BUILD_NAME` with an unused output name, and run:

```sh
python3 -B custom-pieces/scp.py build --include ddrhw-l1-l2-rhw-l0-ramp-diagonal-alignment-a --include ddrhw-l1-l2-rhw-l0-ramp-diagonal-mirrored-alignment-a --include ddrhw-l1-l2-rhw-l0-ramp-diagonal-opposite-alignment-a --include ddrhw-l1-l2-rhw-l0-ramp-diagonal-opposite-mirrored-alignment-a --output custom-pieces/dist/BUILD_NAME
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/BUILD_NAME
python3 -B custom-pieces/domains/highway/tools/freeze_diagonal_transition_connectors.py custom-pieces/dist/BUILD_NAME
python3 -B -m scp_highway.connections --root custom-pieces --build custom-pieces/dist/BUILD_NAME --piece ddrhw-l1-l2-rhw-l0-ramp-diagonal-alignment-a --piece ddrhw-l1-l2-rhw-l0-ramp-diagonal-mirrored-alignment-a --piece ddrhw-l1-l2-rhw-l0-ramp-diagonal-opposite-alignment-a --piece ddrhw-l1-l2-rhw-l0-ramp-diagonal-opposite-mirrored-alignment-a
```

The freezer’s default selects the four exact first-A identities and verifies the complete saved build once before preparing their contracts. It must not accept an orthogonal identity, a mixed variant, an unregistered type, or an unbuilt second alignment. Actual extraction must decode every lane, cell cut, native endpoint, class, direction, edge grade, and complete joining boundary. Require `UseElevation=1`, including genuinely empty model-only PATHs. Promote DD source classes 0/1 to native ground classes 1/2 only on the correct exterior ground-boundary fragments. Verify all four proper rotations and complete journeys without lane or carriageway transfers.

Saved model acceptance must independently check every indexed face, material, texture coordinate, winding, native shoulder and collar, authored deck body, barrier, support, zoom, and combined preview. A native full paired road is nominally 16 m wide; one tile half is not its complete cross-section. Preserve the finite source phases and approximately millimetre-scale shifts rather than substituting a symmetric band. Require full swept 2.5 m × 3.8 m vehicle clearance, all complete closed support solids and their real deck contact, and no body, barrier, or support intruding into the opposing road. Do not inherit an orthogonal or Y-junction overhang, buried-body, or missing-underside exception.

Inspect the actual construction resource and native continuation rules. The native sockets and peers remain unowned, and the custom cell mask must agree with the saved models and PATHs. Verify the complete `#` flat-base constraint group in each rotation. Compare every retained orthogonal definition and complete DAT against the accepted baseline; a source-only assertion does not prove byte preservation.

### 3.2 Generate only checked documentation artifacts

After the contracts and selected extraction pass, write this type’s source-bound connector declarations through the owning library API:

```sh
python3 -B - <<'PYDOC'
from pathlib import Path
from scp_highway.connections import write_connector_groups
write_connector_groups(Path('custom-pieces'), ['ddrhw-l1-l2-rhw-l0-ramp-diagonal-alignment-a'])
PYDOC
```

Replace `/path/to/SimCity 4/Plugins` below with the existing audited texture folder, retaining the quotation marks. The folder is read only. The piece’s own authored texture resources must be taken from its checked DAT before external NAM textures are resolved.

```sh
python3 -B custom-pieces/scp.py connectors refresh --domain highway --piece ddrhw-l1-l2-rhw-l0-ramp-diagonal-alignment-a --build dist/BUILD_NAME --plugins '/path/to/SimCity 4/Plugins'
python3 -B custom-pieces/scp.py connectors check --domain highway --piece ddrhw-l1-l2-rhw-l0-ramp-diagonal-alignment-a --build dist/BUILD_NAME --plugins '/path/to/SimCity 4/Plugins'
python3 -B -m scp.preview --catalog --root custom-pieces --output custom-pieces/dist/BUILD_NAME --plugins '/path/to/SimCity 4/Plugins' --include ddrhw-l1-l2-rhw-l0-ramp-diagonal-alignment-a --views angled top
python3 -B custom-pieces/scp.py observations refresh-images --piece ddrhw-l1-l2-rhw-l0-ramp-diagonal-alignment-a
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-l1-l2-rhw-l0-ramp-diagonal-alignment-a
python3 -B -m unittest discover -s custom-pieces/domains/highway/tests -p 'test_diagonal_transition*.py' -v
python3 -B tools/run_tests.py
```

Inspect the actual angled, top, thumbnail, and connection-overview PNGs for complete geometry, readable full names, correct source/picture coordinates, native directions, and driver-left yellow. Verify final fingerprints, and refresh shared classes and inventories through their owning selected workflow. Preserve all retained subject files unless a specific bounded provenance refresh is separately authorized. Report real test totals, failures, and proprietary-input skips; a skipped native test does not pass. Do not freeze accepted contracts or generate canonical production artwork before saved-resource acceptance.

## 4. Game checks

### 4.1 Family menu, fresh placement, and native construction

1. Open **Transportation → Highways → SCP → Pieces**, select the new first-A original family button when included, and use **Tab** or **Shift+Tab** until the query names **DD RHW-4 — L1/L2 ↔ RHW-4 L0 — Diagonal Ramp — Alignment A**. Confirm one family button, four distinct first-A choices, and no accidental replacement of the retained orthogonal types.
2. Follow the [exact source-pose setup](README.md#2-piece-and-placement), place a fresh adapter on a flat base, and inspect every owned custom cell. Require no hole, ridge, wrong native half, or leftover temporary construction tile. Keep the socket and peer cells outside the fixed ownership.
3. Test drawing outward from the placed sockets, drawing inward from working prebuilt controls, and placing beside completed matching approaches as separate orders. Keep the DD axis and both ground axes in the declared native lattice. Record every gap in native half cells, the actual donor phase, and the adapter rotation.
4. If testing a nearby fixed junction, first establish the complete native continuation and correct DD traffic directions on an ordinary control. Compare close placement and a farther placement followed by manual dragging. Do not infer a complete junction-to-adapter compatibility result from one touching lane or a similar-looking model.
5. Repeat at 90°, 180°, and 270° using **Home** and **End**. Four proper rotations are distinct from four city-camera views, a reflection, and the repeated states in an eight-state cursor cycle.

### 4.2 Route Query, visible travel, and forbidden transfers

1. Establish moving traffic on the ordinary native DD and ground controls before judging this adapter. Connect useful origins and destinations, run the simulation, and record the test environment.
2. Use **Route Query** for each of the two upper lanes and two lower lanes through the complete adapter, including both native joining cells and every height change. Record those four displayed routes separately.
3. Follow an actual car through each complete lane journey. Check the correct deck, no height drop, no reversal, no lane swap, and yellow on the driver’s left throughout. A displayed route is not visible-travel evidence.
4. Check that no lane change, U-turn, or transfer between the opposing carriageways occurs inside the core. Test the twelve declared forbidden entrance-to-exit transfers using the exact current case IDs in the extracted matrix.

### 4.3 Appearance, redraw, and lifetime

Inspect every zoom and all four city-camera views for continuous pavement, native phase contact, complete barriers and supports, correctly phased markings, and proper ground transparency. Compare Medium and High shadow settings; the experimental DD policy supplies no custom cast shadows. Redraw each ordinary approach, replace the adapter, save, quit fully, reload, and repeat native joining and all four lane journeys. Demolish the adapter, and inspect its former core and sockets for leftovers. Use the [shared observation procedure](../../../../docs/TESTING.md), preserving the exact candidate, alignment, rotation, environment, and construction order.

## 5. Results and known issues

This is a **registered, independently checked experimental type**. The [compiled-verification record](evidence/compiled-verification.jsonc) binds the actual DAT in `dist/ddrhw-diagonal-transitions-a-native-03`, its source guard, complete saved PATH/model checks, and equality of all four retained orthogonal DATs. This type uses construction root `F889`, 24 owned cells, 15 routed cells, and nine genuinely empty model-only PATHs. The saved graph contains four complete same-lane journeys and eight native boundary members in all four proper rotations, with no lane or carriageway transfers. Software acceptance supplies no human game result.

The source uses a 101.823376 m longitudinal run, 22.627417 m ground-axis separation, a 66 m sideways-curve run, and 8 m upper-grade easing. The complete DD profile projects up to 5.656854586667169 m beyond its nominal mouth; the chosen flat envelope is therefore **8.656854586667169 m**, preserving a literal additional 3 m before the new curve or grade begins. The sampled source peaks are approximately **18.95182% upper and 17.04542% lower**, and the conservative upper normalization bound is approximately **18.95264%**. These are measured source facts, rather than inherited orthogonal grades or saved-model acceptance.

The actual saved-model checks cover continuous 2.5 m-wide × 3.8 m-high lane corridors, complete finite pavement and underside fields, raw roof and floor contacts, barrier-to-slab and barrier-to-barrier clearance, full native profiles, all five identical zoom models, and the combined preview. All fourteen complete support solids and their opposing-road clearance pass. The combined positive-depth road skin is closed; source-native ground sheets with zero depth have their explicitly separate scope. These results are finite software geometry checks, not a structural-capacity rating or a vehicle test in SimCity 4.

The ground collars retain actual indexed native outlines. Literal native fragments are cut into free cells in the 24-host mask; a fragment in a reserved native approach cell may keep its owned source host only with its exact source-parent, pose, material, UV, and finite-ROI certificate. DD profile continuations and their finite closing lips are authored surfaces strictly inside custom ownership. The hybrid native/custom external-skin check removes only proven internal original-source surfaces, after complete authored floor and outer-wall proof; it preserves authored required faces and retains raw interference checks. No orthogonal or Y-junction exception transfers automatically.

The checked flat DD body uses a common authored underside of 14 m upper and 6.5 m lower. Native 302 roofs remain at 15 m and 7.5 m; native 309 roofs retain their measured approximately +1 mm datum. Flat authored depth is therefore 1 m to approximately 1.001 m, without an artificial underside step. The named 1 m bridge starts at station 8.656854586667169 m and reaches the complete curved/graded middle ring at station 9.656854586667169 m. Ground bridges use the final 1 m before the exact ground collars. The middle underside follows its driving roof minus 1 m, clamped at height 0 m. Actual saved-face checks cover these full-width fields and finite joining profiles; no missing-underside allowance is used.

The [actual normal-DAT marking audit](evidence/native-markings-verification.jsonc) checks twelve driver-left yellow samples for this type and rejects two encoded wrong-side UV controls, one for native mappings and one for the authored atlas. Across the four choices, that is 48 samples and eight controls. Dense finite join samples retain small nonzero native-to-atlas colour differences and a few yellow-threshold disagreements at ground paint edges. These are reported limits, not a proof of perfectly continuous paint or game appearance. Each published result binds the complete actual DAT resource hashes and the native source inputs.

Complete ordinary saved-resource acceptance and sampled driver-left checks have passed. The generated views and connection matrix below remain bound to their own actual resource and image fingerprints. The [metadata-normalization record](evidence/source-metadata-normalization-20261104.jsonc) distinguishes later comment/header/provenance corrections from the unchanged compiled payloads. Installation and all human game cases remain unverified at this capture. Native automatic placement, close-placement terrain, four placement rotations, actual moving traffic, redraw, demolition, and save/reload require their own explicit observations. Earlier orthogonal observations are not results for this new identity.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/3 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Route Query: 0/16 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/16 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 101, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-l1-l2-rhw-l0-ramp-diagonal-alignment-a/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-l1-l2-rhw-l0-ramp-diagonal-alignment-a/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-ea8a7568f06d9c81741a">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-ea8a7568f06d9c81741a"></a>

**General: unverified** — `software_resources-ea8a7568f06d9c81741a`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-ea8a7568f06d9c81741a">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-ea8a7568f06d9c81741a"></a>

**General: unverified** — `software_connectivity-ea8a7568f06d9c81741a`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-eb58ba7be84f155deab1">[ ] unverified</a> | <a href="#case-in_game_render-ccdbf4c09d8299170ea3">[ ] unverified</a> | <a href="#case-in_game_render-fed7e405bd577e847337">[ ] unverified</a> | <a href="#case-in_game_render-88dfeeb59f1004e06dab">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-eb58ba7be84f155deab1"></a>

**0° CCW: unverified** — `in_game_render-eb58ba7be84f155deab1`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-ccdbf4c09d8299170ea3"></a>

**90° CCW: unverified** — `in_game_render-ccdbf4c09d8299170ea3`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-fed7e405bd577e847337"></a>

**180° CCW: unverified** — `in_game_render-fed7e405bd577e847337`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-88dfeeb59f1004e06dab"></a>

**270° CCW: unverified** — `in_game_render-88dfeeb59f1004e06dab`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-eb58ba7be84f155deab1">[ ] unverified</a> | <a href="#case-in_game_placement-ccdbf4c09d8299170ea3">[ ] unverified</a> | <a href="#case-in_game_placement-fed7e405bd577e847337">[ ] unverified</a> | <a href="#case-in_game_placement-88dfeeb59f1004e06dab">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-eb58ba7be84f155deab1"></a>

**0° CCW: unverified** — `in_game_placement-eb58ba7be84f155deab1`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-ccdbf4c09d8299170ea3"></a>

**90° CCW: unverified** — `in_game_placement-ccdbf4c09d8299170ea3`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-fed7e405bd577e847337"></a>

**180° CCW: unverified** — `in_game_placement-fed7e405bd577e847337`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-88dfeeb59f1004e06dab"></a>

**270° CCW: unverified** — `in_game_placement-88dfeeb59f1004e06dab`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-eb58ba7be84f155deab1">[ ] unverified</a> | <a href="#case-in_game_demolition-ccdbf4c09d8299170ea3">[ ] unverified</a> | <a href="#case-in_game_demolition-fed7e405bd577e847337">[ ] unverified</a> | <a href="#case-in_game_demolition-88dfeeb59f1004e06dab">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-eb58ba7be84f155deab1"></a>

**0° CCW: unverified** — `in_game_demolition-eb58ba7be84f155deab1`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-ccdbf4c09d8299170ea3"></a>

**90° CCW: unverified** — `in_game_demolition-ccdbf4c09d8299170ea3`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-fed7e405bd577e847337"></a>

**180° CCW: unverified** — `in_game_demolition-fed7e405bd577e847337`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-88dfeeb59f1004e06dab"></a>

**270° CCW: unverified** — `in_game_demolition-88dfeeb59f1004e06dab`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-eb58ba7be84f155deab1">[ ] unverified</a> | <a href="#case-in_game_save_reload-ccdbf4c09d8299170ea3">[ ] unverified</a> | <a href="#case-in_game_save_reload-fed7e405bd577e847337">[ ] unverified</a> | <a href="#case-in_game_save_reload-88dfeeb59f1004e06dab">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-eb58ba7be84f155deab1"></a>

**0° CCW: unverified** — `in_game_save_reload-eb58ba7be84f155deab1`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-ccdbf4c09d8299170ea3"></a>

**90° CCW: unverified** — `in_game_save_reload-ccdbf4c09d8299170ea3`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-fed7e405bd577e847337"></a>

**180° CCW: unverified** — `in_game_save_reload-fed7e405bd577e847337`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-88dfeeb59f1004e06dab"></a>

**270° CCW: unverified** — `in_game_save_reload-88dfeeb59f1004e06dab`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out | — | <a href="#case-in_game_route_query-b9e13730c82f3127ae0d">[ ] unverified</a> | <a href="#case-in_game_route_query-d76fb192b8cf2d9e878a">[ ] unverified</a> | <a href="#case-in_game_route_query-487519a6ab9b80a711d6">[ ] unverified</a> | <a href="#case-in_game_route_query-90aa56ee9656fc694b75">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out | — | <a href="#case-in_game_route_query-da3b4a1d0418a4e9417d">[ ] unverified</a> | <a href="#case-in_game_route_query-cff03f24250785ed034f">[ ] unverified</a> | <a href="#case-in_game_route_query-248c37f7d92fcc39cbbd">[ ] unverified</a> | <a href="#case-in_game_route_query-264d84766e017bde9cb5">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out | — | <a href="#case-in_game_route_query-5a8e00bd218591a83d6f">[ ] unverified</a> | <a href="#case-in_game_route_query-ad98e619e86396077b13">[ ] unverified</a> | <a href="#case-in_game_route_query-a6bbd2741cf3f6e00254">[ ] unverified</a> | <a href="#case-in_game_route_query-3f25aab8c7c7b4e6f253">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out | — | <a href="#case-in_game_route_query-655cdc147848524fec3e">[ ] unverified</a> | <a href="#case-in_game_route_query-339e33837029e0d15c01">[ ] unverified</a> | <a href="#case-in_game_route_query-9305ada947a32bab8b39">[ ] unverified</a> | <a href="#case-in_game_route_query-6423bee71a5a8c81a703">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out</summary>

<a id="case-in_game_route_query-b9e13730c82f3127ae0d"></a>

**0° CCW: unverified** — `in_game_route_query-b9e13730c82f3127ae0d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-d76fb192b8cf2d9e878a"></a>

**90° CCW: unverified** — `in_game_route_query-d76fb192b8cf2d9e878a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-487519a6ab9b80a711d6"></a>

**180° CCW: unverified** — `in_game_route_query-487519a6ab9b80a711d6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-90aa56ee9656fc694b75"></a>

**270° CCW: unverified** — `in_game_route_query-90aa56ee9656fc694b75`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out</summary>

<a id="case-in_game_route_query-da3b4a1d0418a4e9417d"></a>

**0° CCW: unverified** — `in_game_route_query-da3b4a1d0418a4e9417d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-cff03f24250785ed034f"></a>

**90° CCW: unverified** — `in_game_route_query-cff03f24250785ed034f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-248c37f7d92fcc39cbbd"></a>

**180° CCW: unverified** — `in_game_route_query-248c37f7d92fcc39cbbd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-264d84766e017bde9cb5"></a>

**270° CCW: unverified** — `in_game_route_query-264d84766e017bde9cb5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out</summary>

<a id="case-in_game_route_query-5a8e00bd218591a83d6f"></a>

**0° CCW: unverified** — `in_game_route_query-5a8e00bd218591a83d6f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-ad98e619e86396077b13"></a>

**90° CCW: unverified** — `in_game_route_query-ad98e619e86396077b13`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-a6bbd2741cf3f6e00254"></a>

**180° CCW: unverified** — `in_game_route_query-a6bbd2741cf3f6e00254`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-3f25aab8c7c7b4e6f253"></a>

**270° CCW: unverified** — `in_game_route_query-3f25aab8c7c7b4e6f253`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out</summary>

<a id="case-in_game_route_query-655cdc147848524fec3e"></a>

**0° CCW: unverified** — `in_game_route_query-655cdc147848524fec3e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-339e33837029e0d15c01"></a>

**90° CCW: unverified** — `in_game_route_query-339e33837029e0d15c01`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-9305ada947a32bab8b39"></a>

**180° CCW: unverified** — `in_game_route_query-9305ada947a32bab8b39`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-6423bee71a5a8c81a703"></a>

**270° CCW: unverified** — `in_game_route_query-6423bee71a5a8c81a703`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out | — | <a href="#case-in_game_visible_travel-b9e13730c82f3127ae0d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d76fb192b8cf2d9e878a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-487519a6ab9b80a711d6">[ ] unverified</a> | <a href="#case-in_game_visible_travel-90aa56ee9656fc694b75">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out | — | <a href="#case-in_game_visible_travel-da3b4a1d0418a4e9417d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cff03f24250785ed034f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-248c37f7d92fcc39cbbd">[ ] unverified</a> | <a href="#case-in_game_visible_travel-264d84766e017bde9cb5">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out | — | <a href="#case-in_game_visible_travel-5a8e00bd218591a83d6f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ad98e619e86396077b13">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a6bbd2741cf3f6e00254">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3f25aab8c7c7b4e6f253">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out | — | <a href="#case-in_game_visible_travel-655cdc147848524fec3e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-339e33837029e0d15c01">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9305ada947a32bab8b39">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6423bee71a5a8c81a703">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out</summary>

<a id="case-in_game_visible_travel-b9e13730c82f3127ae0d"></a>

**0° CCW: unverified** — `in_game_visible_travel-b9e13730c82f3127ae0d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-d76fb192b8cf2d9e878a"></a>

**90° CCW: unverified** — `in_game_visible_travel-d76fb192b8cf2d9e878a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-487519a6ab9b80a711d6"></a>

**180° CCW: unverified** — `in_game_visible_travel-487519a6ab9b80a711d6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-90aa56ee9656fc694b75"></a>

**270° CCW: unverified** — `in_game_visible_travel-90aa56ee9656fc694b75`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out</summary>

<a id="case-in_game_visible_travel-da3b4a1d0418a4e9417d"></a>

**0° CCW: unverified** — `in_game_visible_travel-da3b4a1d0418a4e9417d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-cff03f24250785ed034f"></a>

**90° CCW: unverified** — `in_game_visible_travel-cff03f24250785ed034f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-248c37f7d92fcc39cbbd"></a>

**180° CCW: unverified** — `in_game_visible_travel-248c37f7d92fcc39cbbd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-264d84766e017bde9cb5"></a>

**270° CCW: unverified** — `in_game_visible_travel-264d84766e017bde9cb5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out</summary>

<a id="case-in_game_visible_travel-5a8e00bd218591a83d6f"></a>

**0° CCW: unverified** — `in_game_visible_travel-5a8e00bd218591a83d6f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-ad98e619e86396077b13"></a>

**90° CCW: unverified** — `in_game_visible_travel-ad98e619e86396077b13`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-a6bbd2741cf3f6e00254"></a>

**180° CCW: unverified** — `in_game_visible_travel-a6bbd2741cf3f6e00254`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-3f25aab8c7c7b4e6f253"></a>

**270° CCW: unverified** — `in_game_visible_travel-3f25aab8c7c7b4e6f253`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out</summary>

<a id="case-in_game_visible_travel-655cdc147848524fec3e"></a>

**0° CCW: unverified** — `in_game_visible_travel-655cdc147848524fec3e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-339e33837029e0d15c01"></a>

**90° CCW: unverified** — `in_game_visible_travel-339e33837029e0d15c01`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-9305ada947a32bab8b39"></a>

**180° CCW: unverified** — `in_game_visible_travel-9305ada947a32bab8b39`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-6423bee71a5a8c81a703"></a>

**270° CCW: unverified** — `in_game_visible_travel-6423bee71a5a8c81a703`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 48 cases; unverified: 48</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7d88586bd5b042877030">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b906edd6fbd7f0e6f59d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2ac3c0a8c2f2f2270913">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-59e21d9e7e81843458c9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0e211754ba7ec3753091">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-289c07e4674940e74577">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c11939d5440505510131">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e397b3a8ee188f7baf6a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-863d84a8b86370c38f6e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-32b48349644c8ca50789">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b63f454d0fed18932a51">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-92d4b57eca5dc34eb557">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7ae53f8b3a461f8a10e6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f662f9255f45ce76e911">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3d95438da3d40fbbbcbe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e529ab1f84fad67d265b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bf85877b3662955423c8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0d126939f049d3adfe09">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d9ffe423d91ebc261e05">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-39551947cb8bb546a539">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1afbd35dee36961ae03d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-33f68c376f9c2531ce32">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c01d0110b8130e7fe053">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-949ba12719fba8365878">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7200a4bd8b38a577c078">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-60ce7cd234e288b4f08d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9ed31a7f6b396853d21c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-edbaa7eb3a34e9eb74cd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-09de1a5640d7f1d39a27">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a4f74bd710951650abe5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-efdf3b3b795341e35fa2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ed99380fedfdb0653c26">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-13f24e94ce15f308cf5a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7eb639c124bdcbf33042">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8159a09ff38705d108ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ab37386bbefbf2802363">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7f9b31634fac9400e1f0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9bdaae68fefa22ddec4d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6f5f5b8a1d60e1078763">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4f285484c84e91e72687">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b4328978845bf7066fdc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9e1a3117301534ed1ab0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2452a08d2ad56d62b925">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a286cd12ec4bcf3d95b0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9d3b25c643c494ee07c7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d2d6811fb49cade1bcc4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8ae1f297cd490e017698">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d5f08705ee82a6e5422d">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7d88586bd5b042877030"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7d88586bd5b042877030`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b906edd6fbd7f0e6f59d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b906edd6fbd7f0e6f59d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2ac3c0a8c2f2f2270913"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2ac3c0a8c2f2f2270913`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-59e21d9e7e81843458c9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-59e21d9e7e81843458c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0e211754ba7ec3753091"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0e211754ba7ec3753091`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-289c07e4674940e74577"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-289c07e4674940e74577`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c11939d5440505510131"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c11939d5440505510131`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e397b3a8ee188f7baf6a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e397b3a8ee188f7baf6a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-863d84a8b86370c38f6e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-863d84a8b86370c38f6e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-32b48349644c8ca50789"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-32b48349644c8ca50789`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b63f454d0fed18932a51"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b63f454d0fed18932a51`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-92d4b57eca5dc34eb557"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-92d4b57eca5dc34eb557`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7ae53f8b3a461f8a10e6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7ae53f8b3a461f8a10e6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f662f9255f45ce76e911"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f662f9255f45ce76e911`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3d95438da3d40fbbbcbe"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3d95438da3d40fbbbcbe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e529ab1f84fad67d265b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e529ab1f84fad67d265b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bf85877b3662955423c8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bf85877b3662955423c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0d126939f049d3adfe09"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0d126939f049d3adfe09`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d9ffe423d91ebc261e05"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d9ffe423d91ebc261e05`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-39551947cb8bb546a539"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-39551947cb8bb546a539`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1afbd35dee36961ae03d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1afbd35dee36961ae03d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-33f68c376f9c2531ce32"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-33f68c376f9c2531ce32`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c01d0110b8130e7fe053"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c01d0110b8130e7fe053`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-949ba12719fba8365878"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-949ba12719fba8365878`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7200a4bd8b38a577c078"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7200a4bd8b38a577c078`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-60ce7cd234e288b4f08d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-60ce7cd234e288b4f08d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9ed31a7f6b396853d21c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9ed31a7f6b396853d21c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-edbaa7eb3a34e9eb74cd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-edbaa7eb3a34e9eb74cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-09de1a5640d7f1d39a27"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-09de1a5640d7f1d39a27`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a4f74bd710951650abe5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a4f74bd710951650abe5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-efdf3b3b795341e35fa2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-efdf3b3b795341e35fa2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ed99380fedfdb0653c26"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ed99380fedfdb0653c26`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-13f24e94ce15f308cf5a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-13f24e94ce15f308cf5a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7eb639c124bdcbf33042"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7eb639c124bdcbf33042`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8159a09ff38705d108ba"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8159a09ff38705d108ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ab37386bbefbf2802363"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ab37386bbefbf2802363`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7f9b31634fac9400e1f0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7f9b31634fac9400e1f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9bdaae68fefa22ddec4d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9bdaae68fefa22ddec4d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6f5f5b8a1d60e1078763"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6f5f5b8a1d60e1078763`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4f285484c84e91e72687"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4f285484c84e91e72687`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b4328978845bf7066fdc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b4328978845bf7066fdc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9e1a3117301534ed1ab0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9e1a3117301534ed1ab0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2452a08d2ad56d62b925"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2452a08d2ad56d62b925`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a286cd12ec4bcf3d95b0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a286cd12ec4bcf3d95b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9d3b25c643c494ee07c7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9d3b25c643c494ee07c7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d2d6811fb49cade1bcc4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d2d6811fb49cade1bcc4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8ae1f297cd490e017698"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8ae1f297cd490e017698`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d5f08705ee82a6e5422d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d5f08705ee82a6e5422d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-l1-l2-rhw-l0-ramp-diagonal-alignment-a:canonical-southeast | <a href="#case-preview_review-528dcf7d78fbceb7d816">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-l1-l2-rhw-l0-ramp-diagonal-alignment-a:canonical-top | <a href="#case-preview_review-89c7e45b4b19595722e7">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-l1-l2-rhw-l0-ramp-diagonal-alignment-a:connection-overview | <a href="#case-preview_review-cd8ee735463ad8e4e83b">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-l1-l2-rhw-l0-ramp-diagonal-alignment-a:canonical-southeast</summary>

<a id="case-preview_review-528dcf7d78fbceb7d816"></a>

**General: unverified** — `preview_review-528dcf7d78fbceb7d816`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-l2-rhw-l0-ramp-diagonal-alignment-a:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-l2-rhw-l0-ramp-diagonal-alignment-a:canonical-top</summary>

<a id="case-preview_review-89c7e45b4b19595722e7"></a>

**General: unverified** — `preview_review-89c7e45b4b19595722e7`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-l2-rhw-l0-ramp-diagonal-alignment-a:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-l2-rhw-l0-ramp-diagonal-alignment-a:connection-overview</summary>

<a id="case-preview_review-cd8ee735463ad8e4e83b"></a>

**General: unverified** — `preview_review-cd8ee735463ad8e4e83b`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-l2-rhw-l0-ramp-diagonal-alignment-a:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The user requested diagonal counterparts of all four existing orthogonal side/traffic combinations. A direct 45° copy would leave the old 16 m ground-axis separation off the native diagonal lattice. Legal native axes differ by 16/√2 m perpendicular steps; the selected two-step 22.627417 m separation accommodates two complete nominal 16 m roads. Actual 302/309 PATHs, lane classes, profile datums, and finite model/UV outlines are measured anew.

**Alignment A** fixes the northeast DD mouth on east = 8 m and the two ground mouths on the declared horizontal north edges. A successive legal longitudinal native half-cut is not supplied by rotating this type. The next native half-cut is a distinct longitudinal placement phase; no second alignment is allocated or produced here. If another alignment is required, its production remains **WAITING — explicit user acceptance of the exact first-A candidate**, under the [staged alignment rule](../../../../docs/WORKFLOW_PIECE_CREATION.md#alignment-production-order). Planning that requirement supplies neither its implementation nor a human game pass.

Keep actual source, saved-resource, artwork, installation, and human observations separate. Once current cases exist, record only the behavior explicitly observed through the [shared procedure](../../../../docs/TESTING.md). Preserve unverified, failed, and stale results rather than turning source calculations or previews into approvals.
