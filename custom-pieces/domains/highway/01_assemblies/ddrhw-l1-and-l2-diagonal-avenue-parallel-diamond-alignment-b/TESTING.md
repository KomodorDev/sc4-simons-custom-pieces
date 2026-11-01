---
title: "Testing: DD RHW-4 \u2014 Parallel Diagonal Avenue Diamond \u2014 Alignment B"
summary: "Inspect this assembly\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — Parallel Diagonal Avenue Diamond — Alignment B

<!-- ASSEMBLY TESTING LAYOUT: 1 -->

[Assembly overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Test the complementary grid alignment of the [parallel diagonal diamond](README.md): 15 B component types, 34 custom-owned tiles in a 9 × 9 rectangle, four directed ramps, both straight highway decks, and the two-way Avenue with pedestrian routes. The physical layout moves 8 m east and 8 m north relative to A, while the DD highway remains on its original phase. This source relationship does not transfer A's software reports or human observations to B.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Human game checks use only 0° CCW; supported construction states and software rotation checks remain separate.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `external-1` | road / 1 / primary | out | [8.0, -147.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `external-2` | road / 1 / primary | in | [8.0, -147.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `external-3` | road / 1 / primary | out | [8.0, -140.8, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `external-4` | road / 1 / primary | in | [8.0, -140.8, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `external-5` | road / 1 / primary | in | [44.8, -56.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `external-6` | road / 1 / primary | in | [51.2, -56.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `external-7` | road / 1 / primary | out | [56.0, -51.2, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `external-8` | road / 1 / primary | out | [56.0, -44.8, 0.0]; [-0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `external-9` | road / 1 / primary | out | [88.0, -99.2, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `external-10` | road / 1 / primary | out | [88.0, -92.8, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `external-11` | road / 1 / primary | in | [92.8, -88.0, 0.0]; [-0.7071067811865476, 0.7071067811865475]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `external-12` | road / 1 / primary | in | [99.2, -88.0, 0.0]; [-0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-668896c488171c19873d` |
| `external-13` | road / 1 / primary | in | [140.8, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `external-14` | road / 1 / primary | out | [140.8, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `external-15` | road / 1 / primary | in | [147.2, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `external-16` | road / 1 / primary | out | [147.2, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `external-17` | pedestrian / 2 / primary | in | [40.7, -56.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |
| `external-18` | pedestrian / 2 / primary | out | [56.0, -40.7, 0.0]; [-0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `external-19` | pedestrian / 2 / primary | out | [88.0, -103.3, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `external-20` | pedestrian / 2 / primary | in | [103.3, -88.0, 0.0]; [-0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-2ec6b824afff9b450810` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `external-11` → `external-7` | primary |
| road | `external-12` → `external-16` | primary |
| road | `external-12` → `external-8` | primary |
| road | `external-13` → `external-3` | primary |
| road | `external-13` → `external-8` | primary |
| road | `external-15` → `external-1` | primary |
| pedestrian | `external-17` → `external-19` | primary |
| pedestrian | `external-20` → `external-18` | primary |
| road | `external-2` → `external-16` | primary |
| road | `external-2` → `external-9` | primary |
| road | `external-4` → `external-14` | primary |
| road | `external-5` → `external-3` | primary |
| road | `external-5` → `external-9` | primary |
| road | `external-6` → `external-10` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `external-2` | road / `external-1` | not reachable in the saved placed encoded-route graph |
| road / `external-2` | road / `external-3` | not reachable in the saved placed encoded-route graph |
| road / `external-2` | road / `external-7` | not reachable in the saved placed encoded-route graph |
| road / `external-2` | road / `external-8` | not reachable in the saved placed encoded-route graph |
| road / `external-2` | road / `external-10` | not reachable in the saved placed encoded-route graph |
| road / `external-2` | road / `external-14` | not reachable in the saved placed encoded-route graph |
| road / `external-2` | pedestrian / `external-18` | not reachable in the saved placed encoded-route graph |
| road / `external-2` | pedestrian / `external-19` | not reachable in the saved placed encoded-route graph |
| road / `external-4` | road / `external-1` | not reachable in the saved placed encoded-route graph |
| road / `external-4` | road / `external-3` | not reachable in the saved placed encoded-route graph |
| road / `external-4` | road / `external-7` | not reachable in the saved placed encoded-route graph |
| road / `external-4` | road / `external-8` | not reachable in the saved placed encoded-route graph |
| road / `external-4` | road / `external-9` | not reachable in the saved placed encoded-route graph |
| road / `external-4` | road / `external-10` | not reachable in the saved placed encoded-route graph |
| road / `external-4` | road / `external-16` | not reachable in the saved placed encoded-route graph |
| road / `external-4` | pedestrian / `external-18` | not reachable in the saved placed encoded-route graph |
| road / `external-4` | pedestrian / `external-19` | not reachable in the saved placed encoded-route graph |
| road / `external-5` | road / `external-1` | not reachable in the saved placed encoded-route graph |
| road / `external-5` | road / `external-7` | not reachable in the saved placed encoded-route graph |
| road / `external-5` | road / `external-8` | not reachable in the saved placed encoded-route graph |
| road / `external-5` | road / `external-10` | not reachable in the saved placed encoded-route graph |
| road / `external-5` | road / `external-14` | not reachable in the saved placed encoded-route graph |
| road / `external-5` | road / `external-16` | not reachable in the saved placed encoded-route graph |
| road / `external-5` | pedestrian / `external-18` | not reachable in the saved placed encoded-route graph |
| road / `external-5` | pedestrian / `external-19` | not reachable in the saved placed encoded-route graph |
| road / `external-6` | road / `external-1` | not reachable in the saved placed encoded-route graph |
| road / `external-6` | road / `external-3` | not reachable in the saved placed encoded-route graph |
| road / `external-6` | road / `external-7` | not reachable in the saved placed encoded-route graph |
| road / `external-6` | road / `external-8` | not reachable in the saved placed encoded-route graph |
| road / `external-6` | road / `external-9` | not reachable in the saved placed encoded-route graph |
| road / `external-6` | road / `external-14` | not reachable in the saved placed encoded-route graph |
| road / `external-6` | road / `external-16` | not reachable in the saved placed encoded-route graph |
| road / `external-6` | pedestrian / `external-18` | not reachable in the saved placed encoded-route graph |
| road / `external-6` | pedestrian / `external-19` | not reachable in the saved placed encoded-route graph |
| road / `external-11` | road / `external-1` | not reachable in the saved placed encoded-route graph |
| road / `external-11` | road / `external-3` | not reachable in the saved placed encoded-route graph |
| road / `external-11` | road / `external-8` | not reachable in the saved placed encoded-route graph |
| road / `external-11` | road / `external-9` | not reachable in the saved placed encoded-route graph |
| road / `external-11` | road / `external-10` | not reachable in the saved placed encoded-route graph |
| road / `external-11` | road / `external-14` | not reachable in the saved placed encoded-route graph |
| road / `external-11` | road / `external-16` | not reachable in the saved placed encoded-route graph |
| road / `external-11` | pedestrian / `external-18` | not reachable in the saved placed encoded-route graph |
| road / `external-11` | pedestrian / `external-19` | not reachable in the saved placed encoded-route graph |
| road / `external-12` | road / `external-1` | not reachable in the saved placed encoded-route graph |
| road / `external-12` | road / `external-3` | not reachable in the saved placed encoded-route graph |
| road / `external-12` | road / `external-7` | not reachable in the saved placed encoded-route graph |
| road / `external-12` | road / `external-9` | not reachable in the saved placed encoded-route graph |
| road / `external-12` | road / `external-10` | not reachable in the saved placed encoded-route graph |
| road / `external-12` | road / `external-14` | not reachable in the saved placed encoded-route graph |
| road / `external-12` | pedestrian / `external-18` | not reachable in the saved placed encoded-route graph |
| road / `external-12` | pedestrian / `external-19` | not reachable in the saved placed encoded-route graph |
| road / `external-13` | road / `external-1` | not reachable in the saved placed encoded-route graph |
| road / `external-13` | road / `external-7` | not reachable in the saved placed encoded-route graph |
| road / `external-13` | road / `external-9` | not reachable in the saved placed encoded-route graph |
| road / `external-13` | road / `external-10` | not reachable in the saved placed encoded-route graph |
| road / `external-13` | road / `external-14` | not reachable in the saved placed encoded-route graph |
| road / `external-13` | road / `external-16` | not reachable in the saved placed encoded-route graph |
| road / `external-13` | pedestrian / `external-18` | not reachable in the saved placed encoded-route graph |
| road / `external-13` | pedestrian / `external-19` | not reachable in the saved placed encoded-route graph |
| road / `external-15` | road / `external-3` | not reachable in the saved placed encoded-route graph |
| road / `external-15` | road / `external-7` | not reachable in the saved placed encoded-route graph |
| road / `external-15` | road / `external-8` | not reachable in the saved placed encoded-route graph |
| road / `external-15` | road / `external-9` | not reachable in the saved placed encoded-route graph |
| road / `external-15` | road / `external-10` | not reachable in the saved placed encoded-route graph |
| road / `external-15` | road / `external-14` | not reachable in the saved placed encoded-route graph |
| road / `external-15` | road / `external-16` | not reachable in the saved placed encoded-route graph |
| road / `external-15` | pedestrian / `external-18` | not reachable in the saved placed encoded-route graph |
| road / `external-15` | pedestrian / `external-19` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-17` | road / `external-1` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-17` | road / `external-3` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-17` | road / `external-7` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-17` | road / `external-8` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-17` | road / `external-9` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-17` | road / `external-10` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-17` | road / `external-14` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-17` | road / `external-16` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-17` | pedestrian / `external-18` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-20` | road / `external-1` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-20` | road / `external-3` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-20` | road / `external-7` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-20` | road / `external-8` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-20` | road / `external-9` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-20` | road / `external-10` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-20` | road / `external-14` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-20` | road / `external-16` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-20` | pedestrian / `external-19` | not reachable in the saved placed encoded-route graph |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use **Windows SimCity 4 with NAM 50 and right-hand traffic**, including the intended Wine or CrossOver setup. Keep the audited native DD RHW, MIS, controller, and adaptive Avenue inputs described in the [build guide](../../../../docs/BUILD_AND_INSTALL.md). The nested menu additionally requires the Submenus DLL, SC4ResourceLoadingHooks DLL version 2.0.1 or later, and `submenu-essentials.dat`. Private inputs and game resources remain local.

A **DAT** is the game's resource archive. **S3D** resources contain visible model triangles, and **PATH** resources contain directed traffic data. A **T21** binds a visible model prop to a network tile. Adaptive native Avenue textures supply the ground pavement, and retained rotating props supply the elevated highway and ramps. Those mechanisms, pedestrian routes, and visible vehicle movement need separate checks.

1. Preserve the original city. Open a disposable city, pause it, and flatten at least a 15 × 15-tile test area: the 9 × 9 core plus three extra tiles on each side for outside approaches.
2. Follow the B [placement table](README.md#3-placements), starting with P01, P02, and P03 in that order. These sources use local helpers [0,0], [0,0], and [1,1], respectively. Leave P03's future native centre X6, Y4 empty until P03 is placed.
3. Connect ordinary diagonal Avenue, including its untouched southeast centre at X6, Y4, and working NAM double-decker highway approaches. Keep the outside tiles separate from the 34 custom-owned cells.
4. For a future installation, close SimCity 4 completely before replacing files, install the complete verified candidate through the shared receipt procedure, and restart. B uses new identifiers, so an existing A diamond does not become B after reload. Use fresh B controls; test any older installed objects separately.

## 3. Software checks

Run the commands below from the repository root after the exact candidate has been built. The first native candidate is `parallel-diamond-alignment-b-native-01`; match its exact manifest to the saved evidence. A missing or differently fingerprinted build is not a pass.

```sh
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/parallel-diamond-alignment-b-native-01
python3 -B custom-pieces/domains/highway/tools/verify_parallel_alignment_b_assembly.py --build custom-pieces/dist/parallel-diamond-alignment-b-native-01 --evidence custom-pieces/domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/evidence/saved-assembly.jsonc
python3 -B custom-pieces/scp.py docs-check --assembly ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b
python3 -B tools/run_tests.py
```

The required resource checks cover each whole-cell B owner, all native through and ramp fragments, native Avenue car and pedestrian boundaries, active PATH height retention, source-fixed model poses, the eight adaptive cells, and absence of shadow carriers or fixed network shadows. The unowned southeast centre is an ordinary native Avenue tile; all six incident native car/pedestrian members must match it. Checking only one half or one lane is insufficient.

The [actual saved-assembly report](evidence/saved-assembly.jsonc) passes the allocated layout against native build **parallel-diamond-alignment-b-native-01**, manifest SHA-256 `d68b9041c139954133c260980258d729f3dc26c8b4f2674ee30e642f992d4e8a`. Its actual archive checks cover 15 components, 34 owned cells, all four proper PATH rotations, 20 complete directed native boundary channels, 124 matched directed lane seams, four permitted ramp transfers, and no forbidden cross-Avenue transfer. Ten native lane/sidewalk through-journeys retain constant height; the highway directions have straight witnesses with every ramp present, so an avenue detour cannot substitute for the bridge. The two native DD outside approaches are checked separately from live draggable behavior.

The same report checks 2,332 actual B car-support segments, a 2.5 m-wide by 3.8 m-high vehicle corridor, 1,720 fixed-world native deck surface samples, all eight physical functional cuts, four authored ramp piers, and four native centre piers. The narrowed mouths retain the 6 m-to-3.5 m taper over 3 m. The twenty saved DD/MIS texture-seam pairs pass their existing bounds: transverse tolerance 0.0001 and phase tolerance 0.001 repeats. The native tyre-wear field keeps its separate 5 × 10⁻⁶ vertex/sample UV bound. These measurements establish the checked saved surfaces and texture coordinates; game filtering, visible colour, structural capacity, and actual traffic remain outside that proof.

The ordinary build separately passed all fifteen per-piece model/PATH checks, active adaptive heights on eight Avenue cells, and disabled-shadow resource checks. Every one of its 234,694 indexed model triangles was inspected, its five saved zoom models agree, and it retains no custom shadow carrier resources or T21 carrier references. Final assembly-menu preparation separately checks the Highway parent 0x31, nested assembly buttons, isolated component families, retained rotations, hidden member buttons, and unchanged unrelated menu families. Its package has its own manifest. Building, rendering, menu preparation, and packaging do not install files or record a game pass.

The [frozen accepted connector measurements](checks/accepted-connector-contracts.jsonc) bind all fifteen types to the same native manifest. Independent package, saved PATH/model, and assembly checks passed before freezing those numeric records. The unchanged shared assembly graph finds **20 external ports, 14 complete directed journeys, and 90 directed piece joins**, with no internal access-cut port exposed as an outside entrance. These piece-level graph counts differ from the 124 individual directed lane seams checked above. The contract retains complete native channels, including the six members at the ordinary southeast Avenue centre. It does not claim arbitrary-neighbour compatibility or any game observation.

The connector measurements preserve independently reviewed finite-chord headings alongside `sampled_tangent`, `actual_saved_tangent`, and `actual_saved_grade`. A finite chord is the straight segment between consecutive PATH samples. Full nine-decimal saved coordinates supply the precise published grade for this B contract; the shared graph’s six-decimal endpoint keys remain unchanged. This avoids a false slope mismatch on a very short boundary chord without moving routes or enlarging tolerances. The [shared precision lesson](../../../../docs/CONNECTOR_METADATA.md#5-matching-procedure-and-evidence) owns the general rule.

## 4. Game checks

1. Open **Transportation → Highways → SCP | DD RHW-4 — Parallel Diagonal Avenue Diamond**. Confirm separate Alignment A and Alignment B buttons. Select B, press Tab through all 15 named B components and back to P01, then press Shift+Tab through the reverse order. Confirm it never enters the A cycle. Select A separately, and confirm its own cycle remains available.
2. Place the complete B layout using its reference table. Repeat in four proper rotations with Home or End before placement. Confirm the Avenue remains perpendicular to both highway decks, and that props, ramp mouths, and piers rotate with it. Camera rotation alone is not another construction orientation.
3. Connect an existing draggable DD highway at both ends, and ordinary diagonal Avenue at both ground mouths, including southeast centre X6, Y4 in the reference orientation. Test both placement orders in separate copies. A visible join or Route Query line alone does not establish vehicle passage.
4. Supply origins and destinations beyond the highway and Avenue ends. Follow actual cars through both straight decks and all four permitted ramp journeys. Record Route Query separately from visible travel. Confirm that ramp traffic never crosses to the opposing Avenue carriageway.
5. Develop the land beside the Avenue and let the simulation run. Record whether native pavement changes appear on P01–P03 and through the ordinary southeast centre. Follow pedestrians through the ground route and driveway crossings; connecting Avenue alone does not guarantee developed pavement.
6. At Medium and High shadow quality, inspect every camera view and zoom for unwanted custom shadows on the crossing, slip sections, departures, and grades. Preserve the distinction between the requested no-shadow policy and an observed no-shadow result.
7. Save, quit completely, reopen, and repeat representative traffic and pavement checks. In a separate saved copy, demolish one component at a time, inspect neighbouring ordinary tiles and attachments, replace the component, and retest.

Record only explicit observations for the exact candidate, orientation, placement order, and environment using the [shared procedure](../../../../docs/TESTING.md#4-record-one-observation). Keep a no-ramp through-highway control separate from the complete diamond; A's reported control result is not a B observation.

## 5. Results and known issues

**Current human acceptance, 2026-11-01:** after installing the complete 225-type candidate, the user stated, **“for the diamon parallel all checks pass.”** This aggregate confirmation covers the current parallel diamond alignments A and B. The installed manifest SHA-256 is `cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0`, on the established Windows SimCity 4 Deluxe 1.1.641.0, NAM 50, right-hand-traffic Wine or CrossOver setup. The exact runtime version, city name, fresh-versus-existing placement state, per-case screenshots, and individual graphics-setting results were not restated. Each authoritative observation preserves the actual confirmation and its current dependency fingerprint rather than inventing those details.

For this Alignment B record, **118 current in-game cases pass at the required 0° assembly orientation**: placement, appearance, demolition, save/reload, 14 Route Query journeys, 14 visible-travel journeys, and 86 forbidden transfers. Its seven preview-image reviews and two software-check cases retain their previous unverified record states; the separate saved-resource reports above retain their own actual software results. No standalone component case or additional assembly orientation inherits a pass. All 530 recorded fingerprint entries match the installed candidate's relevant resources, retained construction states and adaptive rules, assembly poses, graph, and current images. The later documentation refresh changes no installed game resource.

The first allocated B native build and its [complete saved-assembly proof](evidence/saved-assembly.jsonc) passed the resource, ownership, construction, route, physical support, native deck, barrier, pier, mouth, and texture-coordinate checks described above. The normal build also checked the eight adaptive cells and absence of custom shadow resources. This remains software evidence for its exact native manifest. The final combined menu candidate retained the relevant B resources and construction states, was installed through the receipt-based procedure, and received the later human confirmation above; those stages retain their distinct evidence.

The eight custom adaptive cells exclude the ordinary southeast centre. Its six native incident car and pedestrian members, the complete outside DD boundary, and the proper construction rotations are acceptance requirements. A sidewalk replacement that changes only original native texture IDs does not automatically replace copied custom texture families. The retained steep ramp grades are experimental game geometry, not real-road design standards.

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Human game checks are required only at 0° CCW. Supported construction orientations and software rotation checks retain their separate scope; these human cases do not establish observations at the other orientations.

Current totals: unverified: 9, passed: 118, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/checks/manual-tests.json --observation custom-pieces/domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-b985615e2714486d4959">[ ] unverified</a> | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-b985615e2714486d4959"></a>

**General: unverified** — `software_resources-b985615e2714486d4959`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-b985615e2714486d4959">[ ] unverified</a> | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-b985615e2714486d4959"></a>

**General: unverified** — `software_connectivity-b985615e2714486d4959`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-5ff8c8499c1d17798d46">[x] passed</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-5ff8c8499c1d17798d46"></a>

**0° CCW: passed** — `in_game_render-5ff8c8499c1d17798d46`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>

</details>

<details>
<summary>Placement — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-5ff8c8499c1d17798d46">[x] passed</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-5ff8c8499c1d17798d46"></a>

**0° CCW: passed** — `in_game_placement-5ff8c8499c1d17798d46`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-5ff8c8499c1d17798d46">[x] passed</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-5ff8c8499c1d17798d46"></a>

**0° CCW: passed** — `in_game_demolition-5ff8c8499c1d17798d46`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-5ff8c8499c1d17798d46">[x] passed</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-5ff8c8499c1d17798d46"></a>

**0° CCW: passed** — `in_game_save_reload-5ff8c8499c1d17798d46`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>

</details>

<details>
<summary>Route Query — road — 12 cases; passed: 12</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: external-11>external-7; entry: external-11; exit: external-7 | — | <a href="#case-in_game_route_query-b72cc2026a9586c58955">[x] passed</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-12>external-16; entry: external-12; exit: external-16 | — | <a href="#case-in_game_route_query-acb55d5615cc0e49fc6a">[x] passed</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-12>external-8; entry: external-12; exit: external-8 | — | <a href="#case-in_game_route_query-02c79016dc094030b00a">[x] passed</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-13>external-3; entry: external-13; exit: external-3 | — | <a href="#case-in_game_route_query-c1c3b1d6cc9de4863dc6">[x] passed</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-13>external-8; entry: external-13; exit: external-8 | — | <a href="#case-in_game_route_query-2deeb28ff4012c1f7c60">[x] passed</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-15>external-1; entry: external-15; exit: external-1 | — | <a href="#case-in_game_route_query-ac401416d74d1eb1e22a">[x] passed</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-2>external-16; entry: external-2; exit: external-16 | — | <a href="#case-in_game_route_query-edb7331e14f74b0ef127">[x] passed</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-2>external-9; entry: external-2; exit: external-9 | — | <a href="#case-in_game_route_query-020c39ec9b0178edbe88">[x] passed</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-4>external-14; entry: external-4; exit: external-14 | — | <a href="#case-in_game_route_query-0613136e337e8c8b42df">[x] passed</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3 | — | <a href="#case-in_game_route_query-5c83bbe0fc8e886fb0e8">[x] passed</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9 | — | <a href="#case-in_game_route_query-76146d065cc9bb77cf16">[x] passed</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-6>external-10; entry: external-6; exit: external-10 | — | <a href="#case-in_game_route_query-3e5a6e0114213701f9d3">[x] passed</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: external-11>external-7; entry: external-11; exit: external-7</summary>

<a id="case-in_game_route_query-b72cc2026a9586c58955"></a>

**0° CCW: passed** — `in_game_route_query-b72cc2026a9586c58955`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-11>external-7; entry: external-11; exit: external-7.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-12>external-16; entry: external-12; exit: external-16</summary>

<a id="case-in_game_route_query-acb55d5615cc0e49fc6a"></a>

**0° CCW: passed** — `in_game_route_query-acb55d5615cc0e49fc6a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-12>external-16; entry: external-12; exit: external-16.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-12>external-8; entry: external-12; exit: external-8</summary>

<a id="case-in_game_route_query-02c79016dc094030b00a"></a>

**0° CCW: passed** — `in_game_route_query-02c79016dc094030b00a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-12>external-8; entry: external-12; exit: external-8.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-13>external-3; entry: external-13; exit: external-3</summary>

<a id="case-in_game_route_query-c1c3b1d6cc9de4863dc6"></a>

**0° CCW: passed** — `in_game_route_query-c1c3b1d6cc9de4863dc6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-13>external-3; entry: external-13; exit: external-3.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-13>external-8; entry: external-13; exit: external-8</summary>

<a id="case-in_game_route_query-2deeb28ff4012c1f7c60"></a>

**0° CCW: passed** — `in_game_route_query-2deeb28ff4012c1f7c60`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-13>external-8; entry: external-13; exit: external-8.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-15>external-1; entry: external-15; exit: external-1</summary>

<a id="case-in_game_route_query-ac401416d74d1eb1e22a"></a>

**0° CCW: passed** — `in_game_route_query-ac401416d74d1eb1e22a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-15>external-1; entry: external-15; exit: external-1.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-2>external-16; entry: external-2; exit: external-16</summary>

<a id="case-in_game_route_query-edb7331e14f74b0ef127"></a>

**0° CCW: passed** — `in_game_route_query-edb7331e14f74b0ef127`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-2>external-16; entry: external-2; exit: external-16.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-2>external-9; entry: external-2; exit: external-9</summary>

<a id="case-in_game_route_query-020c39ec9b0178edbe88"></a>

**0° CCW: passed** — `in_game_route_query-020c39ec9b0178edbe88`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-2>external-9; entry: external-2; exit: external-9.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-4>external-14; entry: external-4; exit: external-14</summary>

<a id="case-in_game_route_query-0613136e337e8c8b42df"></a>

**0° CCW: passed** — `in_game_route_query-0613136e337e8c8b42df`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-4>external-14; entry: external-4; exit: external-14.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3</summary>

<a id="case-in_game_route_query-5c83bbe0fc8e886fb0e8"></a>

**0° CCW: passed** — `in_game_route_query-5c83bbe0fc8e886fb0e8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9</summary>

<a id="case-in_game_route_query-76146d065cc9bb77cf16"></a>

**0° CCW: passed** — `in_game_route_query-76146d065cc9bb77cf16`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-6>external-10; entry: external-6; exit: external-10</summary>

<a id="case-in_game_route_query-3e5a6e0114213701f9d3"></a>

**0° CCW: passed** — `in_game_route_query-3e5a6e0114213701f9d3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-6>external-10; entry: external-6; exit: external-10.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>

</details>

<details>
<summary>Visible travel — road — 12 cases; passed: 12</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: external-11>external-7; entry: external-11; exit: external-7 | — | <a href="#case-in_game_visible_travel-b72cc2026a9586c58955">[x] passed</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-12>external-16; entry: external-12; exit: external-16 | — | <a href="#case-in_game_visible_travel-acb55d5615cc0e49fc6a">[x] passed</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-12>external-8; entry: external-12; exit: external-8 | — | <a href="#case-in_game_visible_travel-02c79016dc094030b00a">[x] passed</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-13>external-3; entry: external-13; exit: external-3 | — | <a href="#case-in_game_visible_travel-c1c3b1d6cc9de4863dc6">[x] passed</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-13>external-8; entry: external-13; exit: external-8 | — | <a href="#case-in_game_visible_travel-2deeb28ff4012c1f7c60">[x] passed</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-15>external-1; entry: external-15; exit: external-1 | — | <a href="#case-in_game_visible_travel-ac401416d74d1eb1e22a">[x] passed</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-2>external-16; entry: external-2; exit: external-16 | — | <a href="#case-in_game_visible_travel-edb7331e14f74b0ef127">[x] passed</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-2>external-9; entry: external-2; exit: external-9 | — | <a href="#case-in_game_visible_travel-020c39ec9b0178edbe88">[x] passed</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-4>external-14; entry: external-4; exit: external-14 | — | <a href="#case-in_game_visible_travel-0613136e337e8c8b42df">[x] passed</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3 | — | <a href="#case-in_game_visible_travel-5c83bbe0fc8e886fb0e8">[x] passed</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9 | — | <a href="#case-in_game_visible_travel-76146d065cc9bb77cf16">[x] passed</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-6>external-10; entry: external-6; exit: external-10 | — | <a href="#case-in_game_visible_travel-3e5a6e0114213701f9d3">[x] passed</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-11>external-7; entry: external-11; exit: external-7</summary>

<a id="case-in_game_visible_travel-b72cc2026a9586c58955"></a>

**0° CCW: passed** — `in_game_visible_travel-b72cc2026a9586c58955`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-11>external-7; entry: external-11; exit: external-7.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-12>external-16; entry: external-12; exit: external-16</summary>

<a id="case-in_game_visible_travel-acb55d5615cc0e49fc6a"></a>

**0° CCW: passed** — `in_game_visible_travel-acb55d5615cc0e49fc6a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-12>external-16; entry: external-12; exit: external-16.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-12>external-8; entry: external-12; exit: external-8</summary>

<a id="case-in_game_visible_travel-02c79016dc094030b00a"></a>

**0° CCW: passed** — `in_game_visible_travel-02c79016dc094030b00a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-12>external-8; entry: external-12; exit: external-8.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-13>external-3; entry: external-13; exit: external-3</summary>

<a id="case-in_game_visible_travel-c1c3b1d6cc9de4863dc6"></a>

**0° CCW: passed** — `in_game_visible_travel-c1c3b1d6cc9de4863dc6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-13>external-3; entry: external-13; exit: external-3.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-13>external-8; entry: external-13; exit: external-8</summary>

<a id="case-in_game_visible_travel-2deeb28ff4012c1f7c60"></a>

**0° CCW: passed** — `in_game_visible_travel-2deeb28ff4012c1f7c60`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-13>external-8; entry: external-13; exit: external-8.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-15>external-1; entry: external-15; exit: external-1</summary>

<a id="case-in_game_visible_travel-ac401416d74d1eb1e22a"></a>

**0° CCW: passed** — `in_game_visible_travel-ac401416d74d1eb1e22a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-15>external-1; entry: external-15; exit: external-1.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-2>external-16; entry: external-2; exit: external-16</summary>

<a id="case-in_game_visible_travel-edb7331e14f74b0ef127"></a>

**0° CCW: passed** — `in_game_visible_travel-edb7331e14f74b0ef127`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-2>external-16; entry: external-2; exit: external-16.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-2>external-9; entry: external-2; exit: external-9</summary>

<a id="case-in_game_visible_travel-020c39ec9b0178edbe88"></a>

**0° CCW: passed** — `in_game_visible_travel-020c39ec9b0178edbe88`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-2>external-9; entry: external-2; exit: external-9.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-4>external-14; entry: external-4; exit: external-14</summary>

<a id="case-in_game_visible_travel-0613136e337e8c8b42df"></a>

**0° CCW: passed** — `in_game_visible_travel-0613136e337e8c8b42df`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-4>external-14; entry: external-4; exit: external-14.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3</summary>

<a id="case-in_game_visible_travel-5c83bbe0fc8e886fb0e8"></a>

**0° CCW: passed** — `in_game_visible_travel-5c83bbe0fc8e886fb0e8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9</summary>

<a id="case-in_game_visible_travel-76146d065cc9bb77cf16"></a>

**0° CCW: passed** — `in_game_visible_travel-76146d065cc9bb77cf16`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-6>external-10; entry: external-6; exit: external-10</summary>

<a id="case-in_game_visible_travel-3e5a6e0114213701f9d3"></a>

**0° CCW: passed** — `in_game_visible_travel-3e5a6e0114213701f9d3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-6>external-10; entry: external-6; exit: external-10.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>

</details>

<details>
<summary>Route Query — pedestrian — 2 cases; passed: 2</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Route Query**<br>Service: pedestrian; role: primary; journey: external-17>external-19; entry: external-17; exit: external-19 | — | <a href="#case-in_game_route_query-82170d5876aed4b95935">[x] passed</a> |
| **Route Query**<br>Service: pedestrian; role: primary; journey: external-20>external-18; entry: external-20; exit: external-18 | — | <a href="#case-in_game_route_query-850a9cc79024893244f1">[x] passed</a> |


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: external-17>external-19; entry: external-17; exit: external-19</summary>

<a id="case-in_game_route_query-82170d5876aed4b95935"></a>

**0° CCW: passed** — `in_game_route_query-82170d5876aed4b95935`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: external-17>external-19; entry: external-17; exit: external-19.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: external-20>external-18; entry: external-20; exit: external-18</summary>

<a id="case-in_game_route_query-850a9cc79024893244f1"></a>

**0° CCW: passed** — `in_game_route_query-850a9cc79024893244f1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: external-20>external-18; entry: external-20; exit: external-18.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>

</details>

<details>
<summary>Visible travel — pedestrian — 2 cases; passed: 2</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: external-17>external-19; entry: external-17; exit: external-19 | — | <a href="#case-in_game_visible_travel-82170d5876aed4b95935">[x] passed</a> |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: external-20>external-18; entry: external-20; exit: external-18 | — | <a href="#case-in_game_visible_travel-850a9cc79024893244f1">[x] passed</a> |


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: external-17>external-19; entry: external-17; exit: external-19</summary>

<a id="case-in_game_visible_travel-82170d5876aed4b95935"></a>

**0° CCW: passed** — `in_game_visible_travel-82170d5876aed4b95935`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: external-17>external-19; entry: external-17; exit: external-19.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: external-20>external-18; entry: external-20; exit: external-18</summary>

<a id="case-in_game_visible_travel-850a9cc79024893244f1"></a>

**0° CCW: passed** — `in_game_visible_travel-850a9cc79024893244f1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: external-20>external-18; entry: external-20; exit: external-18.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 52 cases; passed: 52</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Forbidden transfer**<br>from port: external-2; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-45ad715584c7027f6711">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-a77cacd316fb734e83b8">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-997f06fae33cebaa1bba">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-3b4d31a4e149e5ee2d08">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-aed85a94d17132a210a8">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-2583769cd77483c2883a">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-acfbb83678dd3407f723">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-473d2a4f893950ff86b9">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-b60af015437751194651">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-0a97efebee45123a1e62">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-5b7cbc42d54b1e0ba11b">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-d3045568f7b1495db89e">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f3675c4192f7350911b4">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-351113ba5e8f8ded70ae">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-7858c881e83ff20f1c40">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-645728b68fb83f114753">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-4ae1d027219d754f9fcb">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-b0fac8f5179eecb61cb5">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-b4315caca5ac1e8cbd1b">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-7eea6cc413d2f1f613af">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-8692d74b9eecf7961fc6">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-53c43e75429f0d04ff63">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-9eb2e941f2ef98bc9fb8">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-abb98f6c56cfe60bb726">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-83526822b692eedd2ac2">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-61fa54d4178c1f80bb2b">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ff686f11ceb1c7cd6f8c">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-e712e38d3365547f5654">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-2ff2463ff14c23ec7ac0">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-b2838c72770f04ca46ec">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-0dc43774a73db706779e">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-6e47c8640b0d0a1c0fb5">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-843f5a320697189f1af5">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-658c873316076cfbe823">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-1d174ffc59b710083491">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-3cbcb436084b4ccb4a86">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ed7af852362f7907deb9">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-4a98898a848bd58e5e9c">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-27f36f8cf7193ce8f9c3">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-9d3a7a47058ee56867d4">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-aea9e1fa9d6be23c86a9">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-e41f2edf6ec73c225404">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-65330cd9e33b4d3c23cf">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-93182a30f1f0db101ca9">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-e3f268d2e1901de73aaf">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-a4e788e1b020258465c3">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-eb279ae09c5a74f5eca2">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-8af843873794784c501f">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-caedf1401db3c83aa758">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f878eb592942017fc963">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-09f07564353ba7d7b07b">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-cfd02f2b0457e0f59485">[x] passed</a> |


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-45ad715584c7027f6711"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-45ad715584c7027f6711`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-a77cacd316fb734e83b8"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-a77cacd316fb734e83b8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-997f06fae33cebaa1bba"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-997f06fae33cebaa1bba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-3b4d31a4e149e5ee2d08"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-3b4d31a4e149e5ee2d08`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-aed85a94d17132a210a8"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-aed85a94d17132a210a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-2583769cd77483c2883a"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-2583769cd77483c2883a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-acfbb83678dd3407f723"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-acfbb83678dd3407f723`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-473d2a4f893950ff86b9"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-473d2a4f893950ff86b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-b60af015437751194651"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-b60af015437751194651`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-0a97efebee45123a1e62"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-0a97efebee45123a1e62`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-5b7cbc42d54b1e0ba11b"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-5b7cbc42d54b1e0ba11b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-d3045568f7b1495db89e"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-d3045568f7b1495db89e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f3675c4192f7350911b4"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-f3675c4192f7350911b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-351113ba5e8f8ded70ae"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-351113ba5e8f8ded70ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-7858c881e83ff20f1c40"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-7858c881e83ff20f1c40`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-645728b68fb83f114753"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-645728b68fb83f114753`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-4ae1d027219d754f9fcb"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-4ae1d027219d754f9fcb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-b0fac8f5179eecb61cb5"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-b0fac8f5179eecb61cb5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-b4315caca5ac1e8cbd1b"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-b4315caca5ac1e8cbd1b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-7eea6cc413d2f1f613af"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-7eea6cc413d2f1f613af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-8692d74b9eecf7961fc6"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-8692d74b9eecf7961fc6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-53c43e75429f0d04ff63"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-53c43e75429f0d04ff63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-9eb2e941f2ef98bc9fb8"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-9eb2e941f2ef98bc9fb8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-abb98f6c56cfe60bb726"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-abb98f6c56cfe60bb726`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-83526822b692eedd2ac2"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-83526822b692eedd2ac2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-61fa54d4178c1f80bb2b"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-61fa54d4178c1f80bb2b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ff686f11ceb1c7cd6f8c"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-ff686f11ceb1c7cd6f8c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-e712e38d3365547f5654"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-e712e38d3365547f5654`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-2ff2463ff14c23ec7ac0"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-2ff2463ff14c23ec7ac0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-b2838c72770f04ca46ec"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-b2838c72770f04ca46ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-0dc43774a73db706779e"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-0dc43774a73db706779e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-6e47c8640b0d0a1c0fb5"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-6e47c8640b0d0a1c0fb5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-843f5a320697189f1af5"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-843f5a320697189f1af5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-658c873316076cfbe823"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-658c873316076cfbe823`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-1d174ffc59b710083491"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-1d174ffc59b710083491`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-3cbcb436084b4ccb4a86"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-3cbcb436084b4ccb4a86`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ed7af852362f7907deb9"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-ed7af852362f7907deb9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-4a98898a848bd58e5e9c"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-4a98898a848bd58e5e9c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-27f36f8cf7193ce8f9c3"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-27f36f8cf7193ce8f9c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-9d3a7a47058ee56867d4"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-9d3a7a47058ee56867d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-aea9e1fa9d6be23c86a9"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-aea9e1fa9d6be23c86a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-e41f2edf6ec73c225404"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-e41f2edf6ec73c225404`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-65330cd9e33b4d3c23cf"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-65330cd9e33b4d3c23cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-93182a30f1f0db101ca9"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-93182a30f1f0db101ca9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-e3f268d2e1901de73aaf"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-e3f268d2e1901de73aaf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-a4e788e1b020258465c3"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-a4e788e1b020258465c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-eb279ae09c5a74f5eca2"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-eb279ae09c5a74f5eca2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-8af843873794784c501f"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-8af843873794784c501f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-caedf1401db3c83aa758"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-caedf1401db3c83aa758`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f878eb592942017fc963"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-f878eb592942017fc963`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-09f07564353ba7d7b07b"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-09f07564353ba7d7b07b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-cfd02f2b0457e0f59485"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-cfd02f2b0457e0f59485`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>

</details>

<details>
<summary>Forbidden transfer — road → pedestrian — 16 cases; passed: 16</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Forbidden transfer**<br>from port: external-2; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-1d47fcdee69ba5689f8d">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-8b5cb47978474841bd54">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-8dd1e4db54569bb1adfc">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-9315643818b6f354d335">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-c0b230d65678bdae0b6d">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-6af10681b1a5f67b542c">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-c2b79c99ec7d99386b84">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-472fff7d2758203da1d4">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ec498c73e7e194e344b5">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-d1720e6d7c4b8f94ef75">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-c7a60dfc29b37c910df2">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ff082942fa88dc2ea488">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-a3b74e7f3ffbbb613acb">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-5206bd309c49938fae13">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-925eedf3c49ebaa7b19c">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-71e8eb7c594d8f0c7c8a">[x] passed</a> |


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-1d47fcdee69ba5689f8d"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-1d47fcdee69ba5689f8d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-8b5cb47978474841bd54"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-8b5cb47978474841bd54`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-8dd1e4db54569bb1adfc"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-8dd1e4db54569bb1adfc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-9315643818b6f354d335"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-9315643818b6f354d335`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-c0b230d65678bdae0b6d"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-c0b230d65678bdae0b6d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-6af10681b1a5f67b542c"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-6af10681b1a5f67b542c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-c2b79c99ec7d99386b84"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-c2b79c99ec7d99386b84`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-472fff7d2758203da1d4"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-472fff7d2758203da1d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ec498c73e7e194e344b5"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-ec498c73e7e194e344b5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-d1720e6d7c4b8f94ef75"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-d1720e6d7c4b8f94ef75`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-c7a60dfc29b37c910df2"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-c7a60dfc29b37c910df2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ff082942fa88dc2ea488"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-ff082942fa88dc2ea488`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-a3b74e7f3ffbbb613acb"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-a3b74e7f3ffbbb613acb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-5206bd309c49938fae13"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-5206bd309c49938fae13`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-925eedf3c49ebaa7b19c"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-925eedf3c49ebaa7b19c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-71e8eb7c594d8f0c7c8a"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-71e8eb7c594d8f0c7c8a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → road — 16 cases; passed: 16</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Forbidden transfer**<br>from port: external-17; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-5f0ecaf6019a10588a09">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-17; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-31ca69ef25c5e9d69014">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-17; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-bd9465e22624ad682f7d">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-17; to port: external-8; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-5498c3f09d9b26d7f361">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-17; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-8425d37ead1a47178473">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-17; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-e32c40d6f8592a10431f">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-17; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-11d634fa7068f33bd4a1">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-17; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-e244bf9d35f91c27a676">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-33743e69248a46885340">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-189a807ee875a5bea24c">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-93f6a5089580c15b28e5">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-8; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-5749326780672e90e156">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-397f463190f368206765">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-68ea96a6295cac406818">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-356df5b50ffa28ba4748">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ba53d4350b178517e2a6">[x] passed</a> |


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-5f0ecaf6019a10588a09"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-5f0ecaf6019a10588a09`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-31ca69ef25c5e9d69014"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-31ca69ef25c5e9d69014`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-bd9465e22624ad682f7d"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-bd9465e22624ad682f7d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-8; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-5498c3f09d9b26d7f361"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-5498c3f09d9b26d7f361`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-8; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-8425d37ead1a47178473"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-8425d37ead1a47178473`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-e32c40d6f8592a10431f"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-e32c40d6f8592a10431f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-11d634fa7068f33bd4a1"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-11d634fa7068f33bd4a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-e244bf9d35f91c27a676"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-e244bf9d35f91c27a676`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-33743e69248a46885340"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-33743e69248a46885340`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-189a807ee875a5bea24c"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-189a807ee875a5bea24c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-93f6a5089580c15b28e5"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-93f6a5089580c15b28e5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-8; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-5749326780672e90e156"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-5749326780672e90e156`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-8; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-397f463190f368206765"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-397f463190f368206765`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-68ea96a6295cac406818"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-68ea96a6295cac406818`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-356df5b50ffa28ba4748"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-356df5b50ffa28ba4748`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ba53d4350b178517e2a6"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-ba53d4350b178517e2a6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → pedestrian — 2 cases; passed: 2</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Forbidden transfer**<br>from port: external-17; to port: external-18; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-5e765a60841caa762486">[x] passed</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-19; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-d9fd58ae0cc5058f4026">[x] passed</a> |


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-18; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-5e765a60841caa762486"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-5e765a60841caa762486`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-18; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-19; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-d9fd58ae0cc5058f4026"></a>

**0° CCW: passed** — `in_game_forbidden_transfer-d9fd58ae0cc5058f4026`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-19; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-11-01; evidence: [Explicit user confirmation: "for the diamon parallel all checks pass.", The confirmation follows installation of the complete 225-type candidate; manifest SHA-256 cb3cdeba4ef030b5de275f96d9c8fceb1046c30aa370d904bc7e5a1c049068b0.]; environment: platform: Windows SimCity 4 through Wine or CrossOver; game version: SimCity 4 Deluxe 1.1.641.0; nam profile: NAM 50, right-hand traffic; note: Aggregate user confirmation for the installed parallel diamond alignments A and B, applied to the current required 0-degree assembly game cases. No per-case screenshot, city name, placement-state description, or separate runtime version was supplied. Preview reviews, software checks, and standalone component checks retain their separate evidence.

</details>

</details>

<details>
<summary>Preview review — Images — 7 cases; unverified: 7</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b:alignment-comparison | <a href="#case-preview_review-f619430eedf789218422">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b:clean-southeast | <a href="#case-preview_review-53d685ffdc64b58852a9">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b:clean-top | <a href="#case-preview_review-35ec34206eb5ae88cd3f">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b:named-northwest | <a href="#case-preview_review-ae647b0933a321cc58b2">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b:named-southeast | <a href="#case-preview_review-5e8941bfdc954301779f">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b:named-top | <a href="#case-preview_review-96bdb69933ce3c3697c2">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b:tile-ownership | <a href="#case-preview_review-abfc0698ca38f7e4b423">[ ] unverified</a> | — |


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b:alignment-comparison</summary>

<a id="case-preview_review-f619430eedf789218422"></a>

**General: unverified** — `preview_review-f619430eedf789218422`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b:alignment-comparison.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b:clean-southeast</summary>

<a id="case-preview_review-53d685ffdc64b58852a9"></a>

**General: unverified** — `preview_review-53d685ffdc64b58852a9`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b:clean-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b:clean-top</summary>

<a id="case-preview_review-35ec34206eb5ae88cd3f"></a>

**General: unverified** — `preview_review-35ec34206eb5ae88cd3f`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b:clean-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b:named-northwest</summary>

<a id="case-preview_review-ae647b0933a321cc58b2"></a>

**General: unverified** — `preview_review-ae647b0933a321cc58b2`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b:named-northwest.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b:named-southeast</summary>

<a id="case-preview_review-5e8941bfdc954301779f"></a>

**General: unverified** — `preview_review-5e8941bfdc954301779f`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b:named-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b:named-top</summary>

<a id="case-preview_review-96bdb69933ce3c3697c2"></a>

**General: unverified** — `preview_review-96bdb69933ce3c3697c2`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b:named-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b:tile-ownership</summary>

<a id="case-preview_review-abfc0698ca38f7e4b423"></a>

**General: unverified** — `preview_review-abfc0698ca38f7e4b423`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b:tile-ownership.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The user accepted the close parallel Alignment A layout, then requested the complementary diagonal grid position after the separate GHSR/DD crossing exposed that shared network-grid issue. B retains the physical close parallel design but recuts whole-cell model and traffic ownership for the adjacent Avenue phase. Fifteen new types keep the accepted A allocations intact. The southeast terminal uses only two custom halves; the ordinary native centre supplies their complete continuation. The shared submenu provides one assembly button per alignment, and the no-shadow preference applies to both.
