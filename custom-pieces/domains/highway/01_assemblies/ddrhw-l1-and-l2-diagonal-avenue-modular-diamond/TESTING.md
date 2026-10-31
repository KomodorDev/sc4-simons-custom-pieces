---
title: "Testing: DD RHW-4 — Modular Diagonal Avenue Diamond"
summary: "Check the separately placed highway stamp, ramp profiles, Avenue terminals, adaptive pavement, and scoped game observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — Modular Diagonal Avenue Diamond

<!-- ASSEMBLY TESTING LAYOUT: 1 -->

[Assembly overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

The default layout in [assembly.jsonc](assembly.jsonc) uses one 27-cell highway-and-slip-lane stamp, four separately attached ramps, and two separately placed ground Avenue terminals. Its seven placements own 62 distinct tiles within a 10 × 10-tile rectangle. The lower and upper decks are 7.5 m and 15 m above the ground pavement datum. The Avenue, its car routes, and its pedestrian routes remain at 0 m. Read the [component and placement tables](README.md#2-pieces) before testing.

Check all eight required car movements: southwest → northeast and northeast → southwest on their respective highway decks, northwest → southeast and southeast → northwest on the Avenue, and the four adjacent-carriageway ramp turns listed in the README. Reject the four cross-Avenue ramp movements: northeast → southeast, southeast → southwest, southwest → northwest, and northwest → northeast. Both directed pedestrian journeys along the Avenue require separate observations.

The source construction supports four proper rotations: 0°, 90°, 180°, and 270° counterclockwise. A proper rotation turns the whole layout without reflecting traffic. The initial manual layout is the unrotated 0° arrangement; observations at that orientation do not approve the others. The six compact alternatives retain their own profiles and observations; their layout is distinct from the default R40 graph.

Software checks inspect actual saved traffic routes, indexed visible model faces, exclusive tile ownership, complete joining profiles, ground texture/prop rotation, and construction resources. A **PATH** is a saved traffic-route resource, and an **S3D** is a saved visible model. A successful software check cannot establish in-game placement, visible travel, or adaptive sidewalk appearance.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Human game checks use only 0° CCW; supported construction states and software rotation checks remain separate.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `external-1` | road / 1 / primary | out | [-8.0, -147.2, 7.5]; [-0.7071067811865479, -0.7071067811865472]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `external-2` | road / 1 / primary | in | [-8.0, -147.2, 15.0]; [0.7071067811865479, 0.7071067811865472]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `external-3` | road / 1 / primary | out | [-8.0, -140.8, 7.5]; [-0.7071067811865467, -0.7071067811865483]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `external-4` | road / 1 / primary | in | [-8.0, -140.8, 15.0]; [0.7071067811865467, 0.7071067811865483]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `external-5` | road / 1 / primary | in | [8.0, -19.2, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `external-6` | road / 1 / primary | in | [8.0, -12.8, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `external-7` | road / 1 / primary | out | [12.8, -8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `external-8` | road / 1 / primary | out | [19.2, -8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `external-9` | road / 1 / primary | out | [124.8, -136.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `external-10` | road / 1 / primary | out | [131.2, -136.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `external-11` | road / 1 / primary | in | [136.0, -131.2, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `external-12` | road / 1 / primary | in | [136.0, -124.8, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `external-13` | road / 1 / primary | in | [140.8, 8.0, 7.5]; [-0.7071067811865483, -0.7071067811865467]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `external-14` | road / 1 / primary | out | [140.8, 8.0, 15.0]; [0.7071067811865483, 0.7071067811865467]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `external-15` | road / 1 / primary | in | [147.2, 8.0, 7.5]; [-0.7071067811865472, -0.7071067811865479]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `external-16` | road / 1 / primary | out | [147.2, 8.0, 15.0]; [0.7071067811865472, 0.7071067811865479]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `external-17` | pedestrian / 2 / primary | in | [8.0, -23.3, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `external-18` | pedestrian / 2 / primary | out | [23.3, -8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |
| `external-19` | pedestrian / 2 / primary | out | [120.7, -136.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |
| `external-20` | pedestrian / 2 / primary | in | [136.0, -120.7, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |

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

The target is Windows SimCity 4 with NAM 50 and right-hand traffic, including the Windows game running through Wine or CrossOver. Record the actual game version, compatibility layer where used, NAM selection, and installed experimental build for each observation. The original native macOS game is outside this experiment's target.

1. Save a disposable test city, and quit SimCity 4 before changing installed test files. Follow the [shared build and installation procedure](../../../../docs/BUILD_AND_INSTALL.md); a build or preview command does not install files.
2. Select the `ddrhw-modular-ramp-kit` collection when building. It contains the seven new default component types and six retained compact alternatives. The assembly-menu version cycles through the seven default types; the compact alternatives keep their individual menu buttons.
3. Prepare a flat, empty 10 × 10-tile site. Use the README's [placement table](README.md#3-placements), placing P01 once and P02–P07 separately. Do not place two components on the same owned tile. A visible model can overhang a tile without granting a second construction owner.
4. Use X0–X9 and Y0–Y9 throughout the test. X increases east/right, Y increases north/up, and (X0, Y0) is the southwest tile centre. The diagram reference is fixed across all views. Source model coordinates instead use east/north/height in metres, and local source rows increase south; do not substitute those row numbers for the display's north-increasing Y labels.
5. Extend matching diagonal NAM DD RHW-4 at the southwest and northeast highway boundaries, and ordinary diagonal Avenue at the northwest and southeast ground boundaries. Connect real origins and destinations outside the assembly so each intended route has travel demand. Keep native approach joining, placement over an Avenue, and dragging through occupied cells as separate observations.
6. Check the default R40 arrangement first. To test the compact alternative, remove the relevant R40 ramp pair and its terminal, keep the highway stamp, and use the complete matching compact group from the README. Record that layout separately.

## 3. Software checks

The independent [retained-stamp contract](../ddrhw-l1-and-l2-diagonal-avenue-diamond/checks/stamp-reference.jsonc) pins the source model and PATH fingerprints before candidate checking. Twenty-five stamp models and all 27 stamp PATHs retain their accepted bytes. Two Avenue-only core models restore independently pinned pristine native pavement, removing ground apron remnants from the old compact layout. These scoped ground changes leave the high branch geometry and sloped ramp cuts intact.

The actual saved checks pass for both the [seven-placement R40 assembly](evidence/saved-assembly-check.json) and the [same stamp with the six retained compact alternatives](evidence/saved-compact-alternative-check.json). Their source manifest is SHA-256 `99d984feb1899a4c9de39e504997451b94dd6a4f2066fd1860525fd52d3e6144`. The R40 layout has 62 owned cells and 204 saved route fragments; the compact alternative has 53 owned cells and 172 fragments. Both preserve 20 external native channels, ten native through-lane and sidewalk journeys, all eight required arm movements, and exclusion of all four cross-Avenue ramp movements. Their saved traffic graphs pass in all four proper rotations. These reports also retain their sampled pavement/profile joins and support checks; neither reports a game-operation pass.

The R40 model projection includes 92 indexed native triangle projections in two otherwise unowned interior cells: source-layout (column 0, row 2) and (column 2, row 0), which are displayed as (X4, Y3) and (X6, Y5). Each receives 46 projections from retained highway pavement and barrier faces. The exception is bound to the exact frozen stamp-model hashes in the saved report; it is not a general allowance for authored geometry outside its owner. Every new R40 attachment's actual physical projection stays within that attachment's declared owned cells. The compact alternative owns these two cells through its retained grade components.

The separate ramp authoring checks have run successfully with nine reported tests and no skips:

```sh
python3 -B -m unittest discover -s custom-pieces/domains/highway/tests -p test_modular_ramp_geometry.py -v
```

Those focused tests check literal cell ownership, all 18 retained branch cells' exact source triangles, preserved high-end PATH and mesh samples, flat cardinal ground ports, encoded tile seams, the 30% grade bound, actual R40 bends, same-side Avenue access, and the accepted highway joins' longitudinal texture phase. The upper ramp's retained high collar has a measured minimum radius of approximately 29.50 m; new circular sections are R40. A one-metre flat collar supplies a genuinely flat finite joining chord at each new ground port.

The [saved-resource atomization drawing](previews/modular-atomization.png), [editable SVG](previews/modular-atomization.svg), and [measurement evidence](evidence/modular-atomization.json) show the actual indexed pavement and structural faces, directed saved routes, all eight selected component cuts, exclusive ownership cells, and four saved ramp height profiles. C1–C4 retain the sloped high interfaces; C5–C8 are the newly implemented flat grade/terminal interfaces. Top-view geometry uses equal east/north scales. The profile panels explicitly use independent horizontal and vertical scales, and label every run and height in metres.

Use the project-wide runner for the complete framework, domain, and assembly suite, and report its actual skip entries without converting them into passed tests:

```sh
python3 -B tools/run_tests.py
```

After preparing native inputs through the shared workflow, the selected normal build and its verification can be reproduced with:

```sh
python3 -B custom-pieces/scp.py build --set ddrhw-modular-ramp-kit --output custom-pieces/dist/ddrhw-modular-ramp-kit
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/ddrhw-modular-ramp-kit
```

The selected build must pass independent saved-resource checks for the stamp, four grades, and two terminals before resource extraction, connector-card generation, or rendering. Check complete boundary bundles, rather than only a matching ramp centreline. Ground terminals retain both Avenue carriageways and pedestrian services; no ramp can silently discard a shared service to make a join fit. Native MIS attachment, arbitrary native FLEX overrides, and draggable ramp construction are separate mechanisms outside this static modular kit.

The menu artwork is the canonical four-state strip at [icon.png](icon.png), with source-route provenance in [evidence/icon.json](evidence/icon.json). The new assembly's six model pictures use the shared trumpet presentation and a 30% ownership-colour layer over the real model in the construction view. Their renderer accepts an additive assembly selector; its default still targets the retained compact assembly:

```sh
python3 -B custom-pieces/domains/highway/tools/render_compact_assembly.py --assembly ddrhw-l1-and-l2-diagonal-avenue-modular-diamond --build custom-pieces/dist/ddrhw-modular-ramp-kit --output-dir custom-pieces/local/modular-diamond-render --prefix reviewed-modular-diamond
```

This command requires the selected verified build and configured native texture inputs. It stages images in the ignored `local/` directory. Follow the shared [review and promotion procedure](../../../../docs/WORKFLOW_DOCUMENTATION_GENERATION.md#81-promote-the-staged-assembly-pictures) to inspect all six actual images beside their corresponding trumpet references, copy unchanged image bytes into `previews/`, and retain portable render evidence. Rendering cannot tick a manual image-review or game case.

## 4. Game checks

1. Open **Transportation → Highways**, and locate **SCP | ASSEMBLY | DD RHW-4 — Modular Diagonal Avenue Diamond**. Press **Tab** through all seven default types, then **Shift+Tab** through the reverse order. Confirm the preview and tooltip identify the intended type. Check the six compact alternative buttons separately.
2. Place P01 once. Confirm that both highway decks, all four auxiliary-lane openings, and the ground Avenue appear. Confirm that the four external ramp bodies and their terminals have not appeared with P01. Place P02–P07 one by one, confirming that each click adds only the selected component and that existing neighbours remain present.
3. Inspect all four sloped stamp/ramp joins from both oblique camera directions and the top view. Look for pavement cracks, barrier gaps, sudden changes in white-stripe width, mismatched dark wheel tracks, and terrain or supports intersecting the road. Inspect the four flat ramp/terminal joins and both Avenue approaches as separate seams.
4. Repeat construction in the other three supported orientations. Confirm that the highway decks, ground Avenue, ramps, and props rotate together. Record preview orientation separately from the placed result; the earlier adaptive experiment showed why a correct cursor preview alone is insufficient.
5. Connect the ordinary diagonal Avenue at each outer terminal boundary. Observe pavement beside developed zones and undeveloped ground, allow the Avenue to redraw, and inspect the resulting sidewalk artwork. Check pedestrian routes independently from visible paving. Different density, wealth, sidewalk replacement, and save/reload appearances require their own observations.
6. For each required car journey, inspect the game's Route Query, then separately observe a vehicle completing that direction. Provide destinations that make the relevant ramp useful. Confirm that vehicles use the adjacent Avenue carriageway and do not cross the Avenue to make any forbidden ramp turn. Repeat the two pedestrian through journeys with appropriate pedestrian demand.
7. Inspect shadows at more than one camera angle. Save the city, reload it, and inspect the default layout again. In the disposable city, bulldoze one selected ramp component, inspect its connected neighbours, and replace it at the same reference position. Complete-piece demolition and single-tile removal are different checks; use the shared [connected-survivor procedure](../../../../docs/TESTING.md#2-investigate-single-tile-demolition-and-connected-survivors) when investigating partial removal.

Record only human-confirmed observations of the exact case, direction, rotation, layout, and environment. Use the [shared recording procedure](../../../../docs/TESTING.md#4-record-one-observation) with this subject's record:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/checks/manual-tests.json --observation custom-pieces/domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/checks/observation.json
```

## 5. Results and known issues

The default components are experimental. Source checks establish their declared geometry and ownership; saved-resource evidence and manual cases retain their own scopes. No game observation of this new seven-part layout is inherited from the earlier adaptive sidewalk probe or the retained compact assembly.

Current saved-resource results pass for the [R40 layout](evidence/saved-assembly-check.json) and [compact alternative](evidence/saved-compact-alternative-check.json), including their four-rotation traffic graphs, sampled physical seams, and support checks. The retained native overhang at (X4, Y3) and (X6, Y5) remains visible and explicitly measured; those two cells stay outside R40 construction ownership. Matching complete saved boundaries and model fingerprints does not confirm mouse-click placement, native outside-network joining, visible traffic, adaptive pavement, demolition, or save/reload in the game.

The initial choice is finite: use the R40 ramp-and-terminal families shown in the six main pictures, or the six retained compact alternatives in their matching groups. Arbitrary slopes, freely selectable heights, native MIS extensions, and native FLEX/draggable ramps are not supplied by this first kit. The current construction system cannot move a slope piece freely upward or downward; every reusable slope has fixed measured endpoint heights.

The upper ramp's retained collar remains tighter than R40. The 30% maximum is an experimental game-geometry bound, and the new lower grade reaches approximately 25.43%; the longer shape does not imply that every local segment is gentler than the retained compact grade. Visible adaptive pavement is distinct from working pedestrian travel. Keep any observed failure, including placement conflicts, stale appearance, or lost neighbouring geometry after demolition, tied to its actual build and layout below.

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Human game checks are required only at 0° CCW. Supported construction orientations and software rotation checks retain their separate scope; these human cases do not establish observations at the other orientations.

Current totals: unverified: 127, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/checks/manual-tests.json --observation custom-pieces/domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-4f7cd219751f98fe28d6">[ ] unverified</a> | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-4f7cd219751f98fe28d6"></a>

**General: unverified** — `software_resources-4f7cd219751f98fe28d6`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-4f7cd219751f98fe28d6">[ ] unverified</a> | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-4f7cd219751f98fe28d6"></a>

**General: unverified** — `software_connectivity-4f7cd219751f98fe28d6`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-0c0c36dadab6af0fb0a7">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-0c0c36dadab6af0fb0a7"></a>

**0° CCW: unverified** — `in_game_render-0c0c36dadab6af0fb0a7`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-0c0c36dadab6af0fb0a7">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-0c0c36dadab6af0fb0a7"></a>

**0° CCW: unverified** — `in_game_placement-0c0c36dadab6af0fb0a7`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-0c0c36dadab6af0fb0a7">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-0c0c36dadab6af0fb0a7"></a>

**0° CCW: unverified** — `in_game_demolition-0c0c36dadab6af0fb0a7`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-0c0c36dadab6af0fb0a7">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-0c0c36dadab6af0fb0a7"></a>

**0° CCW: unverified** — `in_game_save_reload-0c0c36dadab6af0fb0a7`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: external-11>external-7; entry: external-11; exit: external-7 | — | <a href="#case-in_game_route_query-15666051e4b7612e28d4">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-12>external-16; entry: external-12; exit: external-16 | — | <a href="#case-in_game_route_query-46fbb6b9cdad81416738">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-12>external-8; entry: external-12; exit: external-8 | — | <a href="#case-in_game_route_query-4a4126f25851cc497054">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-13>external-3; entry: external-13; exit: external-3 | — | <a href="#case-in_game_route_query-f7b0ee5dc31ef4eb3b30">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-13>external-8; entry: external-13; exit: external-8 | — | <a href="#case-in_game_route_query-173fa22edb651b27ccd8">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-15>external-1; entry: external-15; exit: external-1 | — | <a href="#case-in_game_route_query-133875e31f029041f9b3">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-2>external-16; entry: external-2; exit: external-16 | — | <a href="#case-in_game_route_query-3dec403284fe91d87129">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-2>external-9; entry: external-2; exit: external-9 | — | <a href="#case-in_game_route_query-f40919dd6af22e158e52">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-4>external-14; entry: external-4; exit: external-14 | — | <a href="#case-in_game_route_query-6548ff85569527986ac0">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3 | — | <a href="#case-in_game_route_query-b619b468ab7724499c99">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9 | — | <a href="#case-in_game_route_query-bcc4377a74b9cfcedb97">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-6>external-10; entry: external-6; exit: external-10 | — | <a href="#case-in_game_route_query-cd4d47a150b5d4076d21">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: external-11>external-7; entry: external-11; exit: external-7</summary>

<a id="case-in_game_route_query-15666051e4b7612e28d4"></a>

**0° CCW: unverified** — `in_game_route_query-15666051e4b7612e28d4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-11>external-7; entry: external-11; exit: external-7.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-12>external-16; entry: external-12; exit: external-16</summary>

<a id="case-in_game_route_query-46fbb6b9cdad81416738"></a>

**0° CCW: unverified** — `in_game_route_query-46fbb6b9cdad81416738`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-12>external-16; entry: external-12; exit: external-16.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-12>external-8; entry: external-12; exit: external-8</summary>

<a id="case-in_game_route_query-4a4126f25851cc497054"></a>

**0° CCW: unverified** — `in_game_route_query-4a4126f25851cc497054`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-12>external-8; entry: external-12; exit: external-8.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-13>external-3; entry: external-13; exit: external-3</summary>

<a id="case-in_game_route_query-f7b0ee5dc31ef4eb3b30"></a>

**0° CCW: unverified** — `in_game_route_query-f7b0ee5dc31ef4eb3b30`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-13>external-3; entry: external-13; exit: external-3.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-13>external-8; entry: external-13; exit: external-8</summary>

<a id="case-in_game_route_query-173fa22edb651b27ccd8"></a>

**0° CCW: unverified** — `in_game_route_query-173fa22edb651b27ccd8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-13>external-8; entry: external-13; exit: external-8.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-15>external-1; entry: external-15; exit: external-1</summary>

<a id="case-in_game_route_query-133875e31f029041f9b3"></a>

**0° CCW: unverified** — `in_game_route_query-133875e31f029041f9b3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-15>external-1; entry: external-15; exit: external-1.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-2>external-16; entry: external-2; exit: external-16</summary>

<a id="case-in_game_route_query-3dec403284fe91d87129"></a>

**0° CCW: unverified** — `in_game_route_query-3dec403284fe91d87129`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-2>external-16; entry: external-2; exit: external-16.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-2>external-9; entry: external-2; exit: external-9</summary>

<a id="case-in_game_route_query-f40919dd6af22e158e52"></a>

**0° CCW: unverified** — `in_game_route_query-f40919dd6af22e158e52`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-2>external-9; entry: external-2; exit: external-9.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-4>external-14; entry: external-4; exit: external-14</summary>

<a id="case-in_game_route_query-6548ff85569527986ac0"></a>

**0° CCW: unverified** — `in_game_route_query-6548ff85569527986ac0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-4>external-14; entry: external-4; exit: external-14.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3</summary>

<a id="case-in_game_route_query-b619b468ab7724499c99"></a>

**0° CCW: unverified** — `in_game_route_query-b619b468ab7724499c99`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9</summary>

<a id="case-in_game_route_query-bcc4377a74b9cfcedb97"></a>

**0° CCW: unverified** — `in_game_route_query-bcc4377a74b9cfcedb97`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-6>external-10; entry: external-6; exit: external-10</summary>

<a id="case-in_game_route_query-cd4d47a150b5d4076d21"></a>

**0° CCW: unverified** — `in_game_route_query-cd4d47a150b5d4076d21`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-6>external-10; entry: external-6; exit: external-10.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: external-11>external-7; entry: external-11; exit: external-7 | — | <a href="#case-in_game_visible_travel-15666051e4b7612e28d4">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-12>external-16; entry: external-12; exit: external-16 | — | <a href="#case-in_game_visible_travel-46fbb6b9cdad81416738">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-12>external-8; entry: external-12; exit: external-8 | — | <a href="#case-in_game_visible_travel-4a4126f25851cc497054">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-13>external-3; entry: external-13; exit: external-3 | — | <a href="#case-in_game_visible_travel-f7b0ee5dc31ef4eb3b30">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-13>external-8; entry: external-13; exit: external-8 | — | <a href="#case-in_game_visible_travel-173fa22edb651b27ccd8">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-15>external-1; entry: external-15; exit: external-1 | — | <a href="#case-in_game_visible_travel-133875e31f029041f9b3">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-2>external-16; entry: external-2; exit: external-16 | — | <a href="#case-in_game_visible_travel-3dec403284fe91d87129">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-2>external-9; entry: external-2; exit: external-9 | — | <a href="#case-in_game_visible_travel-f40919dd6af22e158e52">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-4>external-14; entry: external-4; exit: external-14 | — | <a href="#case-in_game_visible_travel-6548ff85569527986ac0">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3 | — | <a href="#case-in_game_visible_travel-b619b468ab7724499c99">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9 | — | <a href="#case-in_game_visible_travel-bcc4377a74b9cfcedb97">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-6>external-10; entry: external-6; exit: external-10 | — | <a href="#case-in_game_visible_travel-cd4d47a150b5d4076d21">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-11>external-7; entry: external-11; exit: external-7</summary>

<a id="case-in_game_visible_travel-15666051e4b7612e28d4"></a>

**0° CCW: unverified** — `in_game_visible_travel-15666051e4b7612e28d4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-11>external-7; entry: external-11; exit: external-7.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-12>external-16; entry: external-12; exit: external-16</summary>

<a id="case-in_game_visible_travel-46fbb6b9cdad81416738"></a>

**0° CCW: unverified** — `in_game_visible_travel-46fbb6b9cdad81416738`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-12>external-16; entry: external-12; exit: external-16.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-12>external-8; entry: external-12; exit: external-8</summary>

<a id="case-in_game_visible_travel-4a4126f25851cc497054"></a>

**0° CCW: unverified** — `in_game_visible_travel-4a4126f25851cc497054`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-12>external-8; entry: external-12; exit: external-8.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-13>external-3; entry: external-13; exit: external-3</summary>

<a id="case-in_game_visible_travel-f7b0ee5dc31ef4eb3b30"></a>

**0° CCW: unverified** — `in_game_visible_travel-f7b0ee5dc31ef4eb3b30`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-13>external-3; entry: external-13; exit: external-3.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-13>external-8; entry: external-13; exit: external-8</summary>

<a id="case-in_game_visible_travel-173fa22edb651b27ccd8"></a>

**0° CCW: unverified** — `in_game_visible_travel-173fa22edb651b27ccd8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-13>external-8; entry: external-13; exit: external-8.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-15>external-1; entry: external-15; exit: external-1</summary>

<a id="case-in_game_visible_travel-133875e31f029041f9b3"></a>

**0° CCW: unverified** — `in_game_visible_travel-133875e31f029041f9b3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-15>external-1; entry: external-15; exit: external-1.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-2>external-16; entry: external-2; exit: external-16</summary>

<a id="case-in_game_visible_travel-3dec403284fe91d87129"></a>

**0° CCW: unverified** — `in_game_visible_travel-3dec403284fe91d87129`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-2>external-16; entry: external-2; exit: external-16.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-2>external-9; entry: external-2; exit: external-9</summary>

<a id="case-in_game_visible_travel-f40919dd6af22e158e52"></a>

**0° CCW: unverified** — `in_game_visible_travel-f40919dd6af22e158e52`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-2>external-9; entry: external-2; exit: external-9.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-4>external-14; entry: external-4; exit: external-14</summary>

<a id="case-in_game_visible_travel-6548ff85569527986ac0"></a>

**0° CCW: unverified** — `in_game_visible_travel-6548ff85569527986ac0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-4>external-14; entry: external-4; exit: external-14.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3</summary>

<a id="case-in_game_visible_travel-b619b468ab7724499c99"></a>

**0° CCW: unverified** — `in_game_visible_travel-b619b468ab7724499c99`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9</summary>

<a id="case-in_game_visible_travel-bcc4377a74b9cfcedb97"></a>

**0° CCW: unverified** — `in_game_visible_travel-bcc4377a74b9cfcedb97`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-6>external-10; entry: external-6; exit: external-10</summary>

<a id="case-in_game_visible_travel-cd4d47a150b5d4076d21"></a>

**0° CCW: unverified** — `in_game_visible_travel-cd4d47a150b5d4076d21`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-6>external-10; entry: external-6; exit: external-10.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — pedestrian — 2 cases; unverified: 2</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Route Query**<br>Service: pedestrian; role: primary; journey: external-17>external-19; entry: external-17; exit: external-19 | — | <a href="#case-in_game_route_query-f58ba8fc53514f0efc27">[ ] unverified</a> |
| **Route Query**<br>Service: pedestrian; role: primary; journey: external-20>external-18; entry: external-20; exit: external-18 | — | <a href="#case-in_game_route_query-52d5e6376733daad505b">[ ] unverified</a> |


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: external-17>external-19; entry: external-17; exit: external-19</summary>

<a id="case-in_game_route_query-f58ba8fc53514f0efc27"></a>

**0° CCW: unverified** — `in_game_route_query-f58ba8fc53514f0efc27`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: external-17>external-19; entry: external-17; exit: external-19.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: external-20>external-18; entry: external-20; exit: external-18</summary>

<a id="case-in_game_route_query-52d5e6376733daad505b"></a>

**0° CCW: unverified** — `in_game_route_query-52d5e6376733daad505b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: external-20>external-18; entry: external-20; exit: external-18.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — pedestrian — 2 cases; unverified: 2</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: external-17>external-19; entry: external-17; exit: external-19 | — | <a href="#case-in_game_visible_travel-f58ba8fc53514f0efc27">[ ] unverified</a> |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: external-20>external-18; entry: external-20; exit: external-18 | — | <a href="#case-in_game_visible_travel-52d5e6376733daad505b">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: external-17>external-19; entry: external-17; exit: external-19</summary>

<a id="case-in_game_visible_travel-f58ba8fc53514f0efc27"></a>

**0° CCW: unverified** — `in_game_visible_travel-f58ba8fc53514f0efc27`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: external-17>external-19; entry: external-17; exit: external-19.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: external-20>external-18; entry: external-20; exit: external-18</summary>

<a id="case-in_game_visible_travel-52d5e6376733daad505b"></a>

**0° CCW: unverified** — `in_game_visible_travel-52d5e6376733daad505b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: external-20>external-18; entry: external-20; exit: external-18.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 52 cases; unverified: 52</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Forbidden transfer**<br>from port: external-2; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-1e9998b050d26530b1ae">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-8f84b0fbc0d11e150b0e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-4959d5d12e8020a762d1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-0c6ad5317c6dce3f4ac1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-c222c0a5b3ffdb1876c7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-0fbf968c03853cef5058">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-3294baecff92b5d80d2f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-1af3eda52dc45cbd5036">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-cd4a9dad3ed1b8dc5e0a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-06b3ca9f5a1a34c67380">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-7bcb11ce981eaea43788">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-7f89eede7aa8831e01ab">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-5dbc7bbc1ded5459e2c3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-75df08fc73af47f59e87">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-fa10901ea5060453e145">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-a8ca046409563ea62674">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-c13e9c01658de236c78a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-c202463a907fa12e80d6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-73b0518de116beaa3a14">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f4f3684794c789e725ad">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-e77e963c96f0038556db">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-8ccce177f9b5ad723f71">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-d54cc3da132a513444e5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-1ca05fbe9de086721974">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-25013e59050ed9175eb1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-343277e823b183a7fa75">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-d39743956c9f8c700f87">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-60fecb2683e1e6b5598d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-931d2d759f6cad65d300">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-16f11d419ecd8b53158a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-869fcb69cee5396ba1ec">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-de1cf8e52147c4b086f7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-42611599a1393603ee3e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-2465aff1d6a1a11a2f2a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-d0b4af99eb3569543044">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ffe3fdac827c007b3406">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-d6041a82abf4df169f18">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-13c77830e1d98bc9bc4c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-50f24ef68efa0367c298">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-9e5db5cc6f82d86e9158">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-c9c6092105c88ec2b0ba">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-8b14dfb4fe69403e0f69">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-4efdf2af43bcfcbbc1f7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-5ab918464fc68d957871">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ce703b550d0eb8dd35ac">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-8508440c04df3edf7b5b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-5775f51f961aab6bc590">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-4c9f70219511b633fe89">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-e57ca92cba18004e032c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-2e6c7f0917a0c67b629e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-90de71f61789de439338">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-6eeb914fb7a4b7885973">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-1e9998b050d26530b1ae"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1e9998b050d26530b1ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-8f84b0fbc0d11e150b0e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8f84b0fbc0d11e150b0e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-4959d5d12e8020a762d1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4959d5d12e8020a762d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-0c6ad5317c6dce3f4ac1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0c6ad5317c6dce3f4ac1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-c222c0a5b3ffdb1876c7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c222c0a5b3ffdb1876c7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-0fbf968c03853cef5058"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0fbf968c03853cef5058`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-3294baecff92b5d80d2f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3294baecff92b5d80d2f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-1af3eda52dc45cbd5036"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1af3eda52dc45cbd5036`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-cd4a9dad3ed1b8dc5e0a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cd4a9dad3ed1b8dc5e0a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-06b3ca9f5a1a34c67380"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-06b3ca9f5a1a34c67380`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-7bcb11ce981eaea43788"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7bcb11ce981eaea43788`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-7f89eede7aa8831e01ab"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7f89eede7aa8831e01ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-5dbc7bbc1ded5459e2c3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5dbc7bbc1ded5459e2c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-75df08fc73af47f59e87"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-75df08fc73af47f59e87`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-fa10901ea5060453e145"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fa10901ea5060453e145`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-a8ca046409563ea62674"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a8ca046409563ea62674`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-c13e9c01658de236c78a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c13e9c01658de236c78a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-c202463a907fa12e80d6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c202463a907fa12e80d6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-73b0518de116beaa3a14"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-73b0518de116beaa3a14`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f4f3684794c789e725ad"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f4f3684794c789e725ad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-e77e963c96f0038556db"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e77e963c96f0038556db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-8ccce177f9b5ad723f71"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8ccce177f9b5ad723f71`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-d54cc3da132a513444e5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d54cc3da132a513444e5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-1ca05fbe9de086721974"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1ca05fbe9de086721974`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-25013e59050ed9175eb1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-25013e59050ed9175eb1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-343277e823b183a7fa75"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-343277e823b183a7fa75`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-d39743956c9f8c700f87"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d39743956c9f8c700f87`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-60fecb2683e1e6b5598d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-60fecb2683e1e6b5598d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-931d2d759f6cad65d300"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-931d2d759f6cad65d300`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-16f11d419ecd8b53158a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-16f11d419ecd8b53158a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-869fcb69cee5396ba1ec"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-869fcb69cee5396ba1ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-de1cf8e52147c4b086f7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-de1cf8e52147c4b086f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-42611599a1393603ee3e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-42611599a1393603ee3e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-2465aff1d6a1a11a2f2a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2465aff1d6a1a11a2f2a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-d0b4af99eb3569543044"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d0b4af99eb3569543044`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ffe3fdac827c007b3406"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ffe3fdac827c007b3406`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-d6041a82abf4df169f18"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d6041a82abf4df169f18`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-13c77830e1d98bc9bc4c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-13c77830e1d98bc9bc4c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-50f24ef68efa0367c298"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-50f24ef68efa0367c298`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-9e5db5cc6f82d86e9158"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9e5db5cc6f82d86e9158`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-c9c6092105c88ec2b0ba"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c9c6092105c88ec2b0ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-8b14dfb4fe69403e0f69"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8b14dfb4fe69403e0f69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-4efdf2af43bcfcbbc1f7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4efdf2af43bcfcbbc1f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-5ab918464fc68d957871"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5ab918464fc68d957871`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ce703b550d0eb8dd35ac"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ce703b550d0eb8dd35ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-8508440c04df3edf7b5b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8508440c04df3edf7b5b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-5775f51f961aab6bc590"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5775f51f961aab6bc590`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-4c9f70219511b633fe89"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4c9f70219511b633fe89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-e57ca92cba18004e032c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e57ca92cba18004e032c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-2e6c7f0917a0c67b629e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2e6c7f0917a0c67b629e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-90de71f61789de439338"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-90de71f61789de439338`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-6eeb914fb7a4b7885973"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6eeb914fb7a4b7885973`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → pedestrian — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Forbidden transfer**<br>from port: external-2; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-e6c8aba5afabb9b8ce92">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-47d0e62e8b3596b5885e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-6744115467c873c0eb6a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-bed4f3b314f7dfcf0339">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-47611a374b23870e90a8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-76e9ba174ec850c62aa3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-c15a1f00655c737bb10a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f907224652854050b259">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-62b9e157e8769c455e2f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-5e3f33b0b1706094cd9a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ef9035d64800b80aa539">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-cb421b546be34a54e81f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-5b1fdc1b3f0f55e8a67a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-c888e2538af59af4b575">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-2dbe392663e03b4244c8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-3b5b1f3daaae99d56ea7">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-e6c8aba5afabb9b8ce92"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e6c8aba5afabb9b8ce92`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-47d0e62e8b3596b5885e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-47d0e62e8b3596b5885e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-6744115467c873c0eb6a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6744115467c873c0eb6a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-bed4f3b314f7dfcf0339"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bed4f3b314f7dfcf0339`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-47611a374b23870e90a8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-47611a374b23870e90a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-76e9ba174ec850c62aa3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-76e9ba174ec850c62aa3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-c15a1f00655c737bb10a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c15a1f00655c737bb10a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f907224652854050b259"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f907224652854050b259`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-62b9e157e8769c455e2f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-62b9e157e8769c455e2f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-5e3f33b0b1706094cd9a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5e3f33b0b1706094cd9a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ef9035d64800b80aa539"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ef9035d64800b80aa539`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-cb421b546be34a54e81f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cb421b546be34a54e81f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-5b1fdc1b3f0f55e8a67a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5b1fdc1b3f0f55e8a67a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-c888e2538af59af4b575"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c888e2538af59af4b575`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-2dbe392663e03b4244c8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2dbe392663e03b4244c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-3b5b1f3daaae99d56ea7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3b5b1f3daaae99d56ea7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → road — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Forbidden transfer**<br>from port: external-17; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-9203e110a5a8bb1c2c6d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-17; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-836739521f81beedace0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-17; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-efc466768b1174a1814e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-17; to port: external-8; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-69fae782306fcfa057ce">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-17; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ae62b88afec1d7dd251c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-17; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-33c75f3b5d6fd15da3b7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-17; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-4de1c43dc3257b4adcf4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-17; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-6cc9c57f5cecfe7dd984">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-0a00c33fb988a33af597">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-324a87db63709c767de3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-2a5a5c5168daa0e1007e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-8; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-05271c5b9188c2b31ea7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-fc0da0630a12950703ac">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-91e9e9f849018b036f24">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-0fc58a32cd6af3a85213">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-7dba03633d94b19c3ac3">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-9203e110a5a8bb1c2c6d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9203e110a5a8bb1c2c6d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-836739521f81beedace0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-836739521f81beedace0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-efc466768b1174a1814e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-efc466768b1174a1814e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-8; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-69fae782306fcfa057ce"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-69fae782306fcfa057ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-8; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ae62b88afec1d7dd251c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ae62b88afec1d7dd251c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-33c75f3b5d6fd15da3b7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-33c75f3b5d6fd15da3b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-4de1c43dc3257b4adcf4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4de1c43dc3257b4adcf4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-6cc9c57f5cecfe7dd984"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6cc9c57f5cecfe7dd984`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-0a00c33fb988a33af597"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0a00c33fb988a33af597`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-324a87db63709c767de3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-324a87db63709c767de3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-2a5a5c5168daa0e1007e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2a5a5c5168daa0e1007e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-8; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-05271c5b9188c2b31ea7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-05271c5b9188c2b31ea7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-8; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-fc0da0630a12950703ac"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fc0da0630a12950703ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-91e9e9f849018b036f24"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-91e9e9f849018b036f24`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-0fc58a32cd6af3a85213"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0fc58a32cd6af3a85213`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-7dba03633d94b19c3ac3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7dba03633d94b19c3ac3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → pedestrian — 2 cases; unverified: 2</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Forbidden transfer**<br>from port: external-17; to port: external-18; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-e56e9ef71becf10d4afd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-19; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-a44afa549adbaf7c155e">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-18; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-e56e9ef71becf10d4afd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e56e9ef71becf10d4afd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-18; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-19; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-a44afa549adbaf7c155e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a44afa549adbaf7c155e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-19; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 7 cases; unverified: 7</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-modular-diamond:clean-southeast | <a href="#case-preview_review-c428bc761d4e735487c3">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-modular-diamond:clean-top | <a href="#case-preview_review-f18eb39925a9e4eb9afb">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-modular-diamond:modular-atomization | <a href="#case-preview_review-8cdfaec82f2a1b3edb64">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-modular-diamond:named-northwest | <a href="#case-preview_review-161e794a9838084929e5">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-modular-diamond:named-southeast | <a href="#case-preview_review-0ea5a2b252247ca41d0d">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-modular-diamond:named-top | <a href="#case-preview_review-3010860368091d1d9b13">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-modular-diamond:tile-ownership | <a href="#case-preview_review-3725a0c081f16fb33cc7">[ ] unverified</a> | — |


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-modular-diamond:clean-southeast</summary>

<a id="case-preview_review-c428bc761d4e735487c3"></a>

**General: unverified** — `preview_review-c428bc761d4e735487c3`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-modular-diamond:clean-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-modular-diamond:clean-top</summary>

<a id="case-preview_review-f18eb39925a9e4eb9afb"></a>

**General: unverified** — `preview_review-f18eb39925a9e4eb9afb`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-modular-diamond:clean-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-modular-diamond:modular-atomization</summary>

<a id="case-preview_review-8cdfaec82f2a1b3edb64"></a>

**General: unverified** — `preview_review-8cdfaec82f2a1b3edb64`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-modular-diamond:modular-atomization.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-modular-diamond:named-northwest</summary>

<a id="case-preview_review-161e794a9838084929e5"></a>

**General: unverified** — `preview_review-161e794a9838084929e5`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-modular-diamond:named-northwest.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-modular-diamond:named-southeast</summary>

<a id="case-preview_review-0ea5a2b252247ca41d0d"></a>

**General: unverified** — `preview_review-0ea5a2b252247ca41d0d`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-modular-diamond:named-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-modular-diamond:named-top</summary>

<a id="case-preview_review-3010860368091d1d9b13"></a>

**General: unverified** — `preview_review-3010860368091d1d9b13`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-modular-diamond:named-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-modular-diamond:tile-ownership</summary>

<a id="case-preview_review-3725a0c081f16fb33cc7"></a>

**General: unverified** — `preview_review-3725a0c081f16fb33cc7`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-modular-diamond:tile-ownership.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The experiment branched from the retained compact diamond at source `06d3d430d515df230f20802872b14eb836f31a69` onto `codex/ddrhw-modular-ramp-kit`. The original branch, `codex/double-decker-diagonal-highway`, retains the earlier development. The user explicitly selected the existing HSR-style slope and angle connection cards as the basis for modular joins; flat highway-side ports are not a prerequisite.

The agreed implementation makes the highway the single stamp and leaves all four ramp bodies separately placeable. The stamp consolidates retained highway, slip-lane, and required crossing cells without absorbing the independent grades or Avenue terminals. Its two Avenue-only cells restore pristine native pavement so the larger R40 terminals do not inherit unused compact ground apron stubs.

The new grades retain at least 2 m of their existing high-end curve and physical cross-section, then use straight, R40 circular, and straight sections to reach flat orthogonal ground ends. Separate R40 ground terminals complete 45° curves into the adjacent Avenue carriageways. The accepted native material fields and a constant texture-station correction preserve the high join's wheel-track phase even when an entrance route becomes longer. One narrow support under each new grade meets the actual sloped underside.

The [network proposal](../../NETWORK_SPEC.md#10-proposed-modular-ramp-standards) records the wider direction, radius, and joining-grade families, along with NAM, HSR, and real Japanese expressway inspiration. This first implementation selects a small demonstrated subset rather than generating every proposed combination. The retained [compact assembly history](../ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#6-design-history) preserves the earlier pavement, barrier, marking, sidewalk, and rotation findings with their original scope.
