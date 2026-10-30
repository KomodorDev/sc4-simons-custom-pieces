---
title: "Testing: DD RHW-4 \u2014 Compact Diagonal Avenue Diamond"
summary: "Inspect this assembly\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — Compact Diagonal Avenue Diamond

<!-- ASSEMBLY TESTING LAYOUT: 1 -->

[Assembly overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

This assembly contains two opposing elevated highway decks, two avenue directions, four one-way ramps, and two ground-level ramp junctions. Its current source places 13 reusable types in 15 positions, owning 53 tiles inside a 10 × 10-tile rectangle. The required car movements are four through journeys and four adjacent-carriageway right turns; the four cross-avenue left turns are excluded. Inspect the [placement guide](README.md). Saved-resource checks concern encoded traffic paths, actual indexed model triangles, exclusive construction-tile ownership, proper rotations, and menu resources. Human game observations are separate.

The adaptive-ground revision changes the runtime rendering and construction of the access core and the two ramp junctions. Their 15 Avenue tiles select native ground appearance families, and 14 attached props retain the existing decks, ramps, supports, and flat ramp aprons. The remaining ten component types keep their existing construction and artwork. Every canonical model, traffic PATH, and preview remains the geometric reference; the separate active-layer checks establish that the actual resolved Avenue PATHs and prop models preserve it.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Human game checks use only 0° CCW; supported construction states and software rotation checks remain separate.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `external-1` | road / 1 / primary | out | [-8.0, -147.2, 7.5]; [-0.7071067811865475, -0.7071067811865477]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `external-2` | road / 1 / primary | in | [-8.0, -147.2, 15.0]; [0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `external-3` | road / 1 / primary | out | [-8.0, -140.8, 7.5]; [-0.7071067811865475, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `external-4` | road / 1 / primary | in | [-8.0, -140.8, 15.0]; [0.7071067811865475, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `external-5` | road / 1 / primary | in | [24.0, -35.2, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `external-6` | road / 1 / primary | in | [24.0, -28.8, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `external-7` | road / 1 / primary | out | [28.8, -24.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `external-8` | road / 1 / primary | out | [35.2, -24.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `external-9` | road / 1 / primary | out | [104.0, -115.2, 0.0]; [0.7071067811865475, -0.7071067811865477]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `external-10` | road / 1 / primary | out | [104.0, -108.8, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `external-11` | road / 1 / primary | in | [108.8, -104.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `external-12` | road / 1 / primary | in | [115.2, -104.0, 0.0]; [-0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-668896c488171c19873d` |
| `external-13` | road / 1 / primary | in | [140.8, 8.0, 7.5]; [-0.7071067811865476, -0.7071067811865475]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `external-14` | road / 1 / primary | out | [140.8, 8.0, 15.0]; [0.7071067811865476, 0.7071067811865475]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `external-15` | road / 1 / primary | in | [147.2, 8.0, 7.5]; [-0.7071067811865477, -0.7071067811865475]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `external-16` | road / 1 / primary | out | [147.2, 8.0, 15.0]; [0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `external-17` | pedestrian / 2 / primary | in | [24.0, -39.3, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `external-18` | pedestrian / 2 / primary | out | [39.3, -24.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |
| `external-19` | pedestrian / 2 / primary | out | [104.0, -119.3, 0.0]; [0.7071067811865477, -0.7071067811865475]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `external-20` | pedestrian / 2 / primary | in | [119.3, -104.0, 0.0]; [-0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-2ec6b824afff9b450810` |

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

Use the exact native NAM 50 right-hand-traffic archives recorded in `config/profiles/nam50-rhd.jsonc`. Prepare Python with the [repository setup guide](../../../../docs/BUILD_AND_INSTALL.md#31-python-setup-for-a-checkout-or-source-zip). Build into `custom-pieces/dist/`; keep personal Plugins settings under ignored `custom-pieces/local/`. For a human game test, use a disposable flat city and install through the [shared installation guide](../../../../docs/BUILD_AND_INSTALL.md). Building and verification do not install the candidate; an actual installation is recorded separately by its private receipt.

The three adaptive components also require the `adaptive_avenue` capture recorded in the profile and [capture audit](evidence/adaptive-avenue-capture-audit.json). It contains 40 unchanged native texture resources and the native rotating-prop donor. Follow [Prepare adaptive Avenue inputs](../../../../docs/BUILD_AND_INSTALL.md#33-prepare-adaptive-avenue-inputs-for-source-builds) for the exact source command, or let the installer prepare this capture from the pinned NAM texture archive, original `SimCity_4.dat`, and NAM prop archive. Keep the generated capture under ignored local inputs and include that directory as an additional input root for source builds. Do not point a Plugins scan at the entire original game archive directory merely to obtain these resources.

Use Windows SimCity 4 with NAM 50, its NAM DLL and FLEX patch, and right-hand traffic, including a compatible Wine or CrossOver environment. Place fresh components in a disposable city; existing fixed pieces in a saved city do not automatically become the new resolved Avenue tiles. Close the game before changing installed files. Keep the isolated rendering probe's controller outside every active Plugins root when installing this assembly, because both replace shared controller resources.

## 3. Software checks

Run the following commands from the repository root. Building reads your own supported native inputs and creates game archives (DAT files). Verification reopens their saved resources. The menu command creates a separate candidate with one component-cycle button.

```sh
python3 -B custom-pieces/scp.py build --set ddrhw-compact-diagonal-diamond --output custom-pieces/dist/ddrhw-adaptive-diamond-parts-01
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/ddrhw-adaptive-diamond-parts-01
python3 -B custom-pieces/domains/highway/tools/verify_compact_assembly.py --build custom-pieces/dist/ddrhw-adaptive-diamond-parts-01 --output custom-pieces/local/highway-assembly-check.json
python3 -B custom-pieces/scp.py assembly-menu --source custom-pieces/dist/ddrhw-adaptive-diamond-parts-01 --output custom-pieces/dist/ddrhw-adaptive-diamond-menu-01 --domain highway --layout compact-diagonal-diamond
python3 -B custom-pieces/scp.py docs-check --assembly ddrhw-l1-and-l2-diagonal-avenue-diamond
python3 -B tools/run_tests.py
```

If an artwork refresh is requested after the matching native build and verification pass, stage the six actual-model assembly views with `python3 -B custom-pieces/domains/highway/tools/render_compact_assembly.py --build custom-pieces/dist/ddrhw-adaptive-diamond-parts-01 --output-dir custom-pieces/local/highway-assembly-views --prefix reviewed-compact-assembly`. It reads the private Plugins setting for native textures and derives names, positions, rotations, and ownership from the saved models and registered placement plan. Compare every image with the corresponding [trumpet presentation reference](../../../../docs/WORKFLOW_DOCUMENTATION_GENERATION.md#trumpet-presentation-reference), including full-name cards, badges, leaders, colours, filled ownership tiles, and reference diamonds. The staging report records reference hashes, actual cameras, annotations, and the exact six-file canonical order. Review the PNGs before copying their unchanged bytes into `previews/` and retaining their report in [compiled render evidence](evidence/compiled-render.json); preserve [the original schematic render evidence](evidence/render.json) unchanged. This adaptive revision retains the unchanged canonical geometry and existing images; those images do not simulate the selected sidewalk variants.

When the previous fixed-model build is available locally, run `python3 -B custom-pieces/domains/highway/tools/verify_adaptive_diamond.py --build custom-pieces/dist/ddrhw-adaptive-diamond-parts-01 --reference "<previous verified fixed-model build folder>" --output custom-pieces/local/adaptive-ground-preservation.json`. Replace the placeholder with that retained build's directory. This optional baseline comparison checks exact saved resource bytes; a fresh clone can build and independently verify the adaptive source without possessing the earlier private build.

The independent pavement verifier reads saved PATH segments and indexed S3D triangles. It checks continuous pavement support, encoded slopes, declared empty shoulder cells, measured native material references and texture coordinates, and intersections with a 2.5 m-wide, 3.8 m-high car corridor through all four rotations. The [native ramp-material audit](evidence/native-ramp-materials-audit.json) records the actual NAM ramp, highway, barrier, and concrete sources; material checks remain separate from game appearance. This is a triangle-face test, rather than a complete solid or swept-vehicle proof. The earlier [schematic source](design.jsonc), [geometry check](evidence/geometry-check.json), and [schematic render report](evidence/render.json) retain their original source-only scope.

## 4. Game checks

Test these construction and sidewalk questions separately in a disposable city. First place P01–P15 on empty, flat land, then use the normal Avenue tool to extend the two exposed diagonal Avenue ends. In a second empty area, build the complete diagonal Avenue first, then try placing the same components over it. In a third copy, try dragging Avenue through the already placed components. Record placement acceptance, model retention, Route Query, and visible traffic for each sequence; success in one sequence does not establish the others. These cases have not been executed.

On each fresh copy, inspect all 15 Avenue tiles through the core and the two ramp junctions. Compare their pavement with an ordinary Avenue beside the same development, and record the actual density, wealth, and texture mods. A **pedestrian route** is invisible traffic data; a **sidewalk** is visible artwork. The new runtime tiles allow native ground appearance selection beneath separately attached highway and ramp artwork. The isolated rendering experiment's pavement and rotation passes do not pass these complete-assembly cases. Record visible pavement and actual pedestrian travel separately.

Place fresh copies of the access core and both junction components in each of the four Home/End orientations, and compare every placed model with its preview. Rotate the city camera separately. Inspect P01's temporary construction-handle location for an unwanted remaining Road tile. Check the flat ramp aprons for flickering, disappearing pavement, or sidewalks drawn across the turning lane. The software retains those apron surfaces at their original ground height; it does not establish the game's coplanar draw order.

Supply car demand through each elevated deck and all four ramps. Inspect the transitions between the new resolved Avenue tiles and the neighbouring fixed highway tiles, because matching saved routes do not establish that the game accepts those construction-network transitions. Also observe all four highway joins: vehicles should change into or out of the shoulder lane, travel along its parallel section, and use the correct ramp without crossing a barrier. Repeat the appearance and route checks after saving, quitting, and reloading. These game observations remain unverified.

No game observations have been supplied. In a disposable city, place every component in each supported rotation, then supply real traffic demand on all four arms. Observe every generated journey separately with Route Query and visible vehicles. Confirm each of the four permitted right turns with both Route Query and visible vehicles. Confirm that the four cross-avenue left turns stay unavailable, while both avenue through directions and both highway through directions remain usable. Check pedestrians through both surface junctions, vehicles on the grades, and native-texture continuity at the joins. Inspect each ramp opening and the closed opposite upper-deck barrier, then check stopping, junction behaviour, shadows, demolition, replacement, and save/reload. Record exact observations through the [shared testing procedure](../../../../docs/TESTING.md); software checks cannot tick those cases.

## 5. Results and known issues

The current adaptive revision passed saved verification for 1,086 resources in the normal 15-DAT build and 1,038 resources in the prepared 15-DAT assembly-menu build. The latter has one Highways button cycling through all 13 component types and preserves the same RUL1 additions. The [adaptive validation record](evidence/adaptive-ground-validation.json) binds the exact manifests and software results. All 1,453 executed repository tests passed; 82 explicitly skipped cases require unavailable native inputs or retained builds. A separate build and saved verification used the five supported native dependencies, including the exact Avenue capture.

The [direct preservation check](evidence/adaptive-ground-preservation.json) compares the new saved DATs against the previous fixed-model candidate. All 255 canonical zoom models, 51 unique canonical PATHs, 255 shadow resources, 13 complete previews, and their preview effects remain byte-identical. All ten unconverted component DATs and the original separate-menu DAT remain identical. The three changed components add 300 native texture copies, 15 inverse-posed merged PATH aliases, 14 filtered models, 14 props, and 14 T21s, and omit fifteen fixed network-model exemplars. The source slot count is 51 unique component tiles; repeated continuation types bring the placed assembly to 53 tiles.

The [new complete-assembly check](evidence/adaptive-ground-assembly-check.json) independently passes the 53-tile, 15-placement plan, all 172 route fragments and 164 directed lane seams, all eight required arm movements, and the absence of all four cross-Avenue left turns. It rechecks the saved pavement joins and all six columns, and records a maximum car grade of approximately 29.609599%. The separate active-layer verifier confirms that the real Avenue PATH aliases recover every canonical route after rotation and that the prop models retain every non-Avenue mesh. These saved-resource results do not establish game construction, network transitions, pavement selection, or traffic.

The retained pre-adaptive `ddrhw-shoulder-slip-lanes-v3` native build passed static checks for 743 resources in 15 DAT files, covering all 13 reusable component types. Its four audited native input archives remain unchanged. Its models reference six external NAM textures without embedding their image payloads. Saved grades remain approximately 22.6756% lower and 29.6096% upper, within the 30% bound. Complete source driving curves are approximately 70.3287 m lower and 102.2084 m upper, including the auxiliary-lane approaches. The adaptive revision retains the accepted outer ramp paths, all graded samples, and ground turns; the earlier reports below keep their original candidate scope.

The [independent assembly check](evidence/compiled-assembly-check.json) verifies 15 placements, 53 construction tiles, 172 saved PATH fragments, 164 directed lane joins, and 20 native external channels. Of those joins, 70 cross component boundaries. All four saved ramp routes contain a progressive flat lane change and a contiguous auxiliary lane at 5.5 m from the highway axis: lower tapers are 12 m with 4 m parallel runs, and upper tapers are 16 m with 8 m runs. Both native through spines remain beside each parallel run. All eight required arm movements are present, and all four excluded cross-avenue left turns remain absent. Route Query and visible travel require game observations.

The same report checks 320 car-lane pavement samples across component joins, with maximum sampled height difference approximately 1.229 mm. It verifies 6 columns, 48 vertical triangles, 48 pavement contacts, and 10,560 car-segment-to-column comparisons. Minimum conservative planar corridor clearance is approximately 1.578 m. Native overhangs retain the approximately 163.314 × 163.314 m physical envelope, while the construction rectangle remains 160 × 160 m. These checks establish sampled model contacts and conservative corridor clearance; structural engineering and complete vehicle swept volumes remain unverified.

The retained [pre-adaptive validation record](evidence/compiled-validation.json) records 105 passing highway tests with the supported native inputs and no skips. Negative controls reject displaced auxiliary lanes, omitted parallel sections, and displaced native through lanes. An exact saved-edge regression covers the reproduced float32 shoulder-cut crack in all four rotations. All six assembly pictures were reviewed against the corresponding trumpet presentation, and all 13 types have angled and top views. This is a coding-agent artwork review; game appearance remains unverified.

The converted shoulder bands use an unmarked asphalt area of the native DD texture. Their ends show a visible pavement-shade transition in the software previews. The saved car-path support checks pass separately; game lighting and the installed texture pack remain unverified.

The accepted pre-shoulder candidate is retained under [before-shoulder-slip-lanes](evidence/design-history/before-shoulder-slip-lanes/retention.json), including its original saved-resource, material, render, and validation reports. Those reports retain their original results and do not test the new shoulder lanes.

Historical evidence before the extension describes a different candidate: 574 resources in 15 DAT files, 17 placements, 41 construction tiles, 162 saved PATH fragments, 158 directed lane seams, 20 native external channels, and twelve required arm movements. Its maximum saved grades were approximately 33.8474% lower and 38.6269% upper. The frozen earlier [compiled assembly report](evidence/design-history/before-right-turn-extension/compiled-assembly-check.json), [pier contact proof](evidence/design-history/before-right-turn-extension/pier-contact-proof.json), and [compiled validation record](evidence/design-history/before-right-turn-extension/compiled-validation.json) retain their original measured results and source scope. They do not test the changed source.

Use each component’s intrinsic traffic records and the assembly’s generated connection matrix for the exact saved journeys. Full physical connector cards for graded modules remain unsupported pending review. The standalone native crossing has separate boundary evidence.

Game operation remains unverified. The revised 30% bound is an experimental authoring choice for this compact footprint. Vehicle animation, terrain behaviour, native texture appearance, shadows, placement, and the permitted or excluded journeys need their own observations. Concrete pier surfaces and sampled pavement contacts do not establish structural engineering, and corridor face-intersection checks do not establish a complete swept vehicle volume. Native model overhangs are retained. Building, installing, publishing, and human observations are separate actions.

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Human game checks are required only at 0° CCW. Supported construction orientations and software rotation checks retain their separate scope; these human cases do not establish observations at the other orientations.

Current totals: unverified: 130, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/checks/manual-tests.json --observation custom-pieces/domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-0184d6b917d00cb763b7">[ ] unverified</a> | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-0184d6b917d00cb763b7"></a>

**General: unverified** — `software_resources-0184d6b917d00cb763b7`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-0184d6b917d00cb763b7">[ ] unverified</a> | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-0184d6b917d00cb763b7"></a>

**General: unverified** — `software_connectivity-0184d6b917d00cb763b7`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 10 cases; unverified: 10</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:clean-southeast | <a href="#case-preview_review-1078b138a2c094aa07cc">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:clean-top | <a href="#case-preview_review-b02e7ddb83975dfa69a4">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:named-northwest | <a href="#case-preview_review-c4c07979aec5da50d199">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:named-southeast | <a href="#case-preview_review-bc702f29fdf636f1adbb">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:named-top | <a href="#case-preview_review-2f13a8f3bd777cd10246">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:schematic-northwest | <a href="#case-preview_review-41945dab4d14218575f2">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:schematic-profiles | <a href="#case-preview_review-ca10fd6f9f960a69288e">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:schematic-southeast | <a href="#case-preview_review-a27eb7d003ae1a9abb69">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:schematic-top | <a href="#case-preview_review-3fc1532c9931e2deb4e3">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:tile-ownership | <a href="#case-preview_review-a7286a3bc6d0b50ac5e7">[ ] unverified</a> | — |


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:clean-southeast</summary>

<a id="case-preview_review-1078b138a2c094aa07cc"></a>

**General: unverified** — `preview_review-1078b138a2c094aa07cc`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:clean-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:clean-top</summary>

<a id="case-preview_review-b02e7ddb83975dfa69a4"></a>

**General: unverified** — `preview_review-b02e7ddb83975dfa69a4`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:clean-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:named-northwest</summary>

<a id="case-preview_review-c4c07979aec5da50d199"></a>

**General: unverified** — `preview_review-c4c07979aec5da50d199`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:named-northwest.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:named-southeast</summary>

<a id="case-preview_review-bc702f29fdf636f1adbb"></a>

**General: unverified** — `preview_review-bc702f29fdf636f1adbb`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:named-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:named-top</summary>

<a id="case-preview_review-2f13a8f3bd777cd10246"></a>

**General: unverified** — `preview_review-2f13a8f3bd777cd10246`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:named-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:schematic-northwest</summary>

<a id="case-preview_review-41945dab4d14218575f2"></a>

**General: unverified** — `preview_review-41945dab4d14218575f2`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:schematic-northwest.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:schematic-profiles</summary>

<a id="case-preview_review-ca10fd6f9f960a69288e"></a>

**General: unverified** — `preview_review-ca10fd6f9f960a69288e`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:schematic-profiles.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:schematic-southeast</summary>

<a id="case-preview_review-a27eb7d003ae1a9abb69"></a>

**General: unverified** — `preview_review-a27eb7d003ae1a9abb69`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:schematic-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:schematic-top</summary>

<a id="case-preview_review-3fc1532c9931e2deb4e3"></a>

**General: unverified** — `preview_review-3fc1532c9931e2deb4e3`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:schematic-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:tile-ownership</summary>

<a id="case-preview_review-a7286a3bc6d0b50ac5e7"></a>

**General: unverified** — `preview_review-a7286a3bc6d0b50ac5e7`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:tile-ownership.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-d3cfcd278fba6b54f7d5">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-d3cfcd278fba6b54f7d5"></a>

**0° CCW: unverified** — `in_game_render-d3cfcd278fba6b54f7d5`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-d3cfcd278fba6b54f7d5">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-d3cfcd278fba6b54f7d5"></a>

**0° CCW: unverified** — `in_game_placement-d3cfcd278fba6b54f7d5`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-d3cfcd278fba6b54f7d5">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-d3cfcd278fba6b54f7d5"></a>

**0° CCW: unverified** — `in_game_demolition-d3cfcd278fba6b54f7d5`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-d3cfcd278fba6b54f7d5">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-d3cfcd278fba6b54f7d5"></a>

**0° CCW: unverified** — `in_game_save_reload-d3cfcd278fba6b54f7d5`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: external-11>external-7; entry: external-11; exit: external-7 | — | <a href="#case-in_game_route_query-d2f154517af1f34df383">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-12>external-16; entry: external-12; exit: external-16 | — | <a href="#case-in_game_route_query-436733b1aaf8ff9ec9f6">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-12>external-8; entry: external-12; exit: external-8 | — | <a href="#case-in_game_route_query-28af9e63db79bbfe30a1">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-13>external-3; entry: external-13; exit: external-3 | — | <a href="#case-in_game_route_query-fcb5284a8b56ce0a931e">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-13>external-8; entry: external-13; exit: external-8 | — | <a href="#case-in_game_route_query-d8b5edba6be3bd9f2716">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-15>external-1; entry: external-15; exit: external-1 | — | <a href="#case-in_game_route_query-878a5811b90486840d7f">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-2>external-16; entry: external-2; exit: external-16 | — | <a href="#case-in_game_route_query-089b8090f0d1c2d11686">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-2>external-9; entry: external-2; exit: external-9 | — | <a href="#case-in_game_route_query-13159f474c48173fe328">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-4>external-14; entry: external-4; exit: external-14 | — | <a href="#case-in_game_route_query-95326c16946a4571e900">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3 | — | <a href="#case-in_game_route_query-e35bd55025909f0c6ae9">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9 | — | <a href="#case-in_game_route_query-0301aed91499dadd0fc9">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-6>external-10; entry: external-6; exit: external-10 | — | <a href="#case-in_game_route_query-c6e378012e647981855f">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: external-11>external-7; entry: external-11; exit: external-7</summary>

<a id="case-in_game_route_query-d2f154517af1f34df383"></a>

**0° CCW: unverified** — `in_game_route_query-d2f154517af1f34df383`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-11>external-7; entry: external-11; exit: external-7.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-12>external-16; entry: external-12; exit: external-16</summary>

<a id="case-in_game_route_query-436733b1aaf8ff9ec9f6"></a>

**0° CCW: unverified** — `in_game_route_query-436733b1aaf8ff9ec9f6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-12>external-16; entry: external-12; exit: external-16.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-12>external-8; entry: external-12; exit: external-8</summary>

<a id="case-in_game_route_query-28af9e63db79bbfe30a1"></a>

**0° CCW: unverified** — `in_game_route_query-28af9e63db79bbfe30a1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-12>external-8; entry: external-12; exit: external-8.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-13>external-3; entry: external-13; exit: external-3</summary>

<a id="case-in_game_route_query-fcb5284a8b56ce0a931e"></a>

**0° CCW: unverified** — `in_game_route_query-fcb5284a8b56ce0a931e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-13>external-3; entry: external-13; exit: external-3.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-13>external-8; entry: external-13; exit: external-8</summary>

<a id="case-in_game_route_query-d8b5edba6be3bd9f2716"></a>

**0° CCW: unverified** — `in_game_route_query-d8b5edba6be3bd9f2716`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-13>external-8; entry: external-13; exit: external-8.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-15>external-1; entry: external-15; exit: external-1</summary>

<a id="case-in_game_route_query-878a5811b90486840d7f"></a>

**0° CCW: unverified** — `in_game_route_query-878a5811b90486840d7f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-15>external-1; entry: external-15; exit: external-1.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-2>external-16; entry: external-2; exit: external-16</summary>

<a id="case-in_game_route_query-089b8090f0d1c2d11686"></a>

**0° CCW: unverified** — `in_game_route_query-089b8090f0d1c2d11686`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-2>external-16; entry: external-2; exit: external-16.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-2>external-9; entry: external-2; exit: external-9</summary>

<a id="case-in_game_route_query-13159f474c48173fe328"></a>

**0° CCW: unverified** — `in_game_route_query-13159f474c48173fe328`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-2>external-9; entry: external-2; exit: external-9.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-4>external-14; entry: external-4; exit: external-14</summary>

<a id="case-in_game_route_query-95326c16946a4571e900"></a>

**0° CCW: unverified** — `in_game_route_query-95326c16946a4571e900`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-4>external-14; entry: external-4; exit: external-14.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3</summary>

<a id="case-in_game_route_query-e35bd55025909f0c6ae9"></a>

**0° CCW: unverified** — `in_game_route_query-e35bd55025909f0c6ae9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9</summary>

<a id="case-in_game_route_query-0301aed91499dadd0fc9"></a>

**0° CCW: unverified** — `in_game_route_query-0301aed91499dadd0fc9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-6>external-10; entry: external-6; exit: external-10</summary>

<a id="case-in_game_route_query-c6e378012e647981855f"></a>

**0° CCW: unverified** — `in_game_route_query-c6e378012e647981855f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-6>external-10; entry: external-6; exit: external-10.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: external-11>external-7; entry: external-11; exit: external-7 | — | <a href="#case-in_game_visible_travel-d2f154517af1f34df383">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-12>external-16; entry: external-12; exit: external-16 | — | <a href="#case-in_game_visible_travel-436733b1aaf8ff9ec9f6">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-12>external-8; entry: external-12; exit: external-8 | — | <a href="#case-in_game_visible_travel-28af9e63db79bbfe30a1">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-13>external-3; entry: external-13; exit: external-3 | — | <a href="#case-in_game_visible_travel-fcb5284a8b56ce0a931e">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-13>external-8; entry: external-13; exit: external-8 | — | <a href="#case-in_game_visible_travel-d8b5edba6be3bd9f2716">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-15>external-1; entry: external-15; exit: external-1 | — | <a href="#case-in_game_visible_travel-878a5811b90486840d7f">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-2>external-16; entry: external-2; exit: external-16 | — | <a href="#case-in_game_visible_travel-089b8090f0d1c2d11686">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-2>external-9; entry: external-2; exit: external-9 | — | <a href="#case-in_game_visible_travel-13159f474c48173fe328">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-4>external-14; entry: external-4; exit: external-14 | — | <a href="#case-in_game_visible_travel-95326c16946a4571e900">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3 | — | <a href="#case-in_game_visible_travel-e35bd55025909f0c6ae9">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9 | — | <a href="#case-in_game_visible_travel-0301aed91499dadd0fc9">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-6>external-10; entry: external-6; exit: external-10 | — | <a href="#case-in_game_visible_travel-c6e378012e647981855f">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-11>external-7; entry: external-11; exit: external-7</summary>

<a id="case-in_game_visible_travel-d2f154517af1f34df383"></a>

**0° CCW: unverified** — `in_game_visible_travel-d2f154517af1f34df383`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-11>external-7; entry: external-11; exit: external-7.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-12>external-16; entry: external-12; exit: external-16</summary>

<a id="case-in_game_visible_travel-436733b1aaf8ff9ec9f6"></a>

**0° CCW: unverified** — `in_game_visible_travel-436733b1aaf8ff9ec9f6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-12>external-16; entry: external-12; exit: external-16.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-12>external-8; entry: external-12; exit: external-8</summary>

<a id="case-in_game_visible_travel-28af9e63db79bbfe30a1"></a>

**0° CCW: unverified** — `in_game_visible_travel-28af9e63db79bbfe30a1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-12>external-8; entry: external-12; exit: external-8.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-13>external-3; entry: external-13; exit: external-3</summary>

<a id="case-in_game_visible_travel-fcb5284a8b56ce0a931e"></a>

**0° CCW: unverified** — `in_game_visible_travel-fcb5284a8b56ce0a931e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-13>external-3; entry: external-13; exit: external-3.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-13>external-8; entry: external-13; exit: external-8</summary>

<a id="case-in_game_visible_travel-d8b5edba6be3bd9f2716"></a>

**0° CCW: unverified** — `in_game_visible_travel-d8b5edba6be3bd9f2716`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-13>external-8; entry: external-13; exit: external-8.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-15>external-1; entry: external-15; exit: external-1</summary>

<a id="case-in_game_visible_travel-878a5811b90486840d7f"></a>

**0° CCW: unverified** — `in_game_visible_travel-878a5811b90486840d7f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-15>external-1; entry: external-15; exit: external-1.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-2>external-16; entry: external-2; exit: external-16</summary>

<a id="case-in_game_visible_travel-089b8090f0d1c2d11686"></a>

**0° CCW: unverified** — `in_game_visible_travel-089b8090f0d1c2d11686`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-2>external-16; entry: external-2; exit: external-16.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-2>external-9; entry: external-2; exit: external-9</summary>

<a id="case-in_game_visible_travel-13159f474c48173fe328"></a>

**0° CCW: unverified** — `in_game_visible_travel-13159f474c48173fe328`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-2>external-9; entry: external-2; exit: external-9.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-4>external-14; entry: external-4; exit: external-14</summary>

<a id="case-in_game_visible_travel-95326c16946a4571e900"></a>

**0° CCW: unverified** — `in_game_visible_travel-95326c16946a4571e900`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-4>external-14; entry: external-4; exit: external-14.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3</summary>

<a id="case-in_game_visible_travel-e35bd55025909f0c6ae9"></a>

**0° CCW: unverified** — `in_game_visible_travel-e35bd55025909f0c6ae9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9</summary>

<a id="case-in_game_visible_travel-0301aed91499dadd0fc9"></a>

**0° CCW: unverified** — `in_game_visible_travel-0301aed91499dadd0fc9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-6>external-10; entry: external-6; exit: external-10</summary>

<a id="case-in_game_visible_travel-c6e378012e647981855f"></a>

**0° CCW: unverified** — `in_game_visible_travel-c6e378012e647981855f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-6>external-10; entry: external-6; exit: external-10.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — pedestrian — 2 cases; unverified: 2</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Route Query**<br>Service: pedestrian; role: primary; journey: external-17>external-19; entry: external-17; exit: external-19 | — | <a href="#case-in_game_route_query-f17d10cd5202df482809">[ ] unverified</a> |
| **Route Query**<br>Service: pedestrian; role: primary; journey: external-20>external-18; entry: external-20; exit: external-18 | — | <a href="#case-in_game_route_query-f3aa920e0190d1b9428b">[ ] unverified</a> |


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: external-17>external-19; entry: external-17; exit: external-19</summary>

<a id="case-in_game_route_query-f17d10cd5202df482809"></a>

**0° CCW: unverified** — `in_game_route_query-f17d10cd5202df482809`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: external-17>external-19; entry: external-17; exit: external-19.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: external-20>external-18; entry: external-20; exit: external-18</summary>

<a id="case-in_game_route_query-f3aa920e0190d1b9428b"></a>

**0° CCW: unverified** — `in_game_route_query-f3aa920e0190d1b9428b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: external-20>external-18; entry: external-20; exit: external-18.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — pedestrian — 2 cases; unverified: 2</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: external-17>external-19; entry: external-17; exit: external-19 | — | <a href="#case-in_game_visible_travel-f17d10cd5202df482809">[ ] unverified</a> |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: external-20>external-18; entry: external-20; exit: external-18 | — | <a href="#case-in_game_visible_travel-f3aa920e0190d1b9428b">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: external-17>external-19; entry: external-17; exit: external-19</summary>

<a id="case-in_game_visible_travel-f17d10cd5202df482809"></a>

**0° CCW: unverified** — `in_game_visible_travel-f17d10cd5202df482809`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: external-17>external-19; entry: external-17; exit: external-19.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: external-20>external-18; entry: external-20; exit: external-18</summary>

<a id="case-in_game_visible_travel-f3aa920e0190d1b9428b"></a>

**0° CCW: unverified** — `in_game_visible_travel-f3aa920e0190d1b9428b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: external-20>external-18; entry: external-20; exit: external-18.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 52 cases; unverified: 52</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Forbidden transfer**<br>from port: external-2; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-4df5253325d3a5a962f5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ddb4a78290312195656f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-b0d9ea504f5838993d64">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-5014330c9d5a4a52cb11">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-92beb85de3919a9f9e38">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-140ee7e98e4d06df1dc0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-e3f26b8bfed582a472bc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f27e177f3bed406e3c3c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f2a81135215123b6227a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-895ce6abaea73f8a17e0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-600a06c657e4ef3e84d8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-2b811d8d836f123cbdcc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-65313dd337171d04c96d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-614d4acdee2b148f4a12">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-09136b99468fea2ee46b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-3a2fc47b60f9cc340289">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-5f983faebd94d30d9f06">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-5738e475c8093b427958">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-009ecfaa62f094dfae33">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f2702d2408f51ed64baa">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-c5e5229b98fc4fd7d276">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-851dcd531963126d90ae">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-cb4376b570116c5c99cb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-15a3c1721c004d0fc4b3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-fd3e8683ebc19b6b9a6d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ff38f9cccda68adf36c7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-860ff11898ce9da9dd60">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-3e6be5243156fd77aece">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-81e40d16a6fb7ddea32b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-69da7c404c761b3223fc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-59cdf78f61c5c85070d2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f1f4321e731d9b8ef6df">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-1f648c8cad4fb8757c89">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-a617399437f290d64bfa">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-a2b4bf4919859daccec0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-3a6ca43c4e5f07e46529">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-5f7cc94031de147fe741">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f4e4b616f8ea9af9c0ba">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ff2dc60f1e6b5e5a016b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-210d47233ae064107780">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-8f0c6eda05a095b919df">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-2291b13f6fa48e39e6ac">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-705c289bfd8950702a81">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-314c1990d32c0e69c644">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-1877150269648e0194dc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-2fe324b9ddfea7efd735">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-cb152456b8963fd35e67">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-35149ccce45158ec2d18">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-39cc6c6371f04ead37c2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-8710d4a3a76557f4279f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-02e67baeee7acfa73fa6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-d1aa2d95bfe64701a475">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-4df5253325d3a5a962f5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4df5253325d3a5a962f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ddb4a78290312195656f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ddb4a78290312195656f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-b0d9ea504f5838993d64"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b0d9ea504f5838993d64`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-5014330c9d5a4a52cb11"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5014330c9d5a4a52cb11`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-92beb85de3919a9f9e38"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-92beb85de3919a9f9e38`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-140ee7e98e4d06df1dc0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-140ee7e98e4d06df1dc0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-e3f26b8bfed582a472bc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e3f26b8bfed582a472bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f27e177f3bed406e3c3c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f27e177f3bed406e3c3c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f2a81135215123b6227a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f2a81135215123b6227a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-895ce6abaea73f8a17e0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-895ce6abaea73f8a17e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-600a06c657e4ef3e84d8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-600a06c657e4ef3e84d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-2b811d8d836f123cbdcc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2b811d8d836f123cbdcc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-65313dd337171d04c96d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-65313dd337171d04c96d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-614d4acdee2b148f4a12"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-614d4acdee2b148f4a12`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-09136b99468fea2ee46b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-09136b99468fea2ee46b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-3a2fc47b60f9cc340289"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3a2fc47b60f9cc340289`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-5f983faebd94d30d9f06"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5f983faebd94d30d9f06`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-5738e475c8093b427958"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5738e475c8093b427958`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-009ecfaa62f094dfae33"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-009ecfaa62f094dfae33`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f2702d2408f51ed64baa"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f2702d2408f51ed64baa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-c5e5229b98fc4fd7d276"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c5e5229b98fc4fd7d276`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-851dcd531963126d90ae"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-851dcd531963126d90ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-cb4376b570116c5c99cb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cb4376b570116c5c99cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-15a3c1721c004d0fc4b3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-15a3c1721c004d0fc4b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-fd3e8683ebc19b6b9a6d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fd3e8683ebc19b6b9a6d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ff38f9cccda68adf36c7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ff38f9cccda68adf36c7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-860ff11898ce9da9dd60"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-860ff11898ce9da9dd60`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-3e6be5243156fd77aece"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3e6be5243156fd77aece`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-81e40d16a6fb7ddea32b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-81e40d16a6fb7ddea32b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-69da7c404c761b3223fc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-69da7c404c761b3223fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-59cdf78f61c5c85070d2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-59cdf78f61c5c85070d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f1f4321e731d9b8ef6df"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f1f4321e731d9b8ef6df`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-1f648c8cad4fb8757c89"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1f648c8cad4fb8757c89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-a617399437f290d64bfa"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a617399437f290d64bfa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-a2b4bf4919859daccec0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a2b4bf4919859daccec0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-3a6ca43c4e5f07e46529"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3a6ca43c4e5f07e46529`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-5f7cc94031de147fe741"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5f7cc94031de147fe741`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f4e4b616f8ea9af9c0ba"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f4e4b616f8ea9af9c0ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ff2dc60f1e6b5e5a016b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ff2dc60f1e6b5e5a016b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-210d47233ae064107780"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-210d47233ae064107780`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-8f0c6eda05a095b919df"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8f0c6eda05a095b919df`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-2291b13f6fa48e39e6ac"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2291b13f6fa48e39e6ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-705c289bfd8950702a81"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-705c289bfd8950702a81`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-314c1990d32c0e69c644"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-314c1990d32c0e69c644`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-1877150269648e0194dc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1877150269648e0194dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-2fe324b9ddfea7efd735"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2fe324b9ddfea7efd735`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-cb152456b8963fd35e67"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cb152456b8963fd35e67`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-35149ccce45158ec2d18"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-35149ccce45158ec2d18`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-39cc6c6371f04ead37c2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-39cc6c6371f04ead37c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-8710d4a3a76557f4279f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8710d4a3a76557f4279f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-02e67baeee7acfa73fa6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-02e67baeee7acfa73fa6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-d1aa2d95bfe64701a475"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d1aa2d95bfe64701a475`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → pedestrian — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Forbidden transfer**<br>from port: external-2; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-6f964e85ffe9fc05e267">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-178b32f6566a0961d27e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-b5ee10b6728a6ddebc6e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-514360e303d5be6acb85">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-0b4e6f8ac70a36cf84d8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-75a6aae1800a807aff56">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-8124ebb60a084f8eee97">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-6e69021717448af2b78d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f13c6c8629b99dcab52c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-7894c684490be6756b0c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-0a51ee7510ac014c4b1e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-7a60b3c99a06b0931b9d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-9a0796e79791a0914e25">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-a6e94d9fff2f07d76565">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-cde12397e2f6c14e1643">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-85409cc7a7f54617a8d8">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-6f964e85ffe9fc05e267"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6f964e85ffe9fc05e267`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-178b32f6566a0961d27e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-178b32f6566a0961d27e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-b5ee10b6728a6ddebc6e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b5ee10b6728a6ddebc6e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-514360e303d5be6acb85"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-514360e303d5be6acb85`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-0b4e6f8ac70a36cf84d8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0b4e6f8ac70a36cf84d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-75a6aae1800a807aff56"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-75a6aae1800a807aff56`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-8124ebb60a084f8eee97"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8124ebb60a084f8eee97`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-6e69021717448af2b78d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6e69021717448af2b78d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f13c6c8629b99dcab52c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f13c6c8629b99dcab52c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-7894c684490be6756b0c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7894c684490be6756b0c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-0a51ee7510ac014c4b1e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0a51ee7510ac014c4b1e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-7a60b3c99a06b0931b9d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7a60b3c99a06b0931b9d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-9a0796e79791a0914e25"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9a0796e79791a0914e25`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-a6e94d9fff2f07d76565"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a6e94d9fff2f07d76565`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-cde12397e2f6c14e1643"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cde12397e2f6c14e1643`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-85409cc7a7f54617a8d8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-85409cc7a7f54617a8d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → road — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Forbidden transfer**<br>from port: external-17; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-0780a79eb4db8710079f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-17; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-325c8c48bd66821a5ad3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-17; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-eac78f169152de0a0f6c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-17; to port: external-8; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-b894b214d3de2fe5e32b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-17; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-dfdcf0631a3cd2c0a813">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-17; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-bcde64e24a630bf05dbd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-17; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-90385d2019babb4a11a3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-17; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-81111a85a2195e0ed19b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-1212b93cc0f383f87f10">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-b8dd9b963e1fdd62c375">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-bf40b57c560afb13368a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-8; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-8fbbf10899e99de0972a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-c52c358bdea5d3ac4f2c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-6e5230f19d494bf01502">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-993efc9f8d4e533d6f32">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-e2fabb3f0b8a6a4e16f1">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-0780a79eb4db8710079f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0780a79eb4db8710079f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-325c8c48bd66821a5ad3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-325c8c48bd66821a5ad3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-eac78f169152de0a0f6c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-eac78f169152de0a0f6c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-8; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-b894b214d3de2fe5e32b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b894b214d3de2fe5e32b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-8; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-dfdcf0631a3cd2c0a813"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dfdcf0631a3cd2c0a813`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-bcde64e24a630bf05dbd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bcde64e24a630bf05dbd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-90385d2019babb4a11a3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-90385d2019babb4a11a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-81111a85a2195e0ed19b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-81111a85a2195e0ed19b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-1212b93cc0f383f87f10"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1212b93cc0f383f87f10`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-b8dd9b963e1fdd62c375"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b8dd9b963e1fdd62c375`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-bf40b57c560afb13368a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bf40b57c560afb13368a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-8; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-8fbbf10899e99de0972a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8fbbf10899e99de0972a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-8; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-c52c358bdea5d3ac4f2c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c52c358bdea5d3ac4f2c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-6e5230f19d494bf01502"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6e5230f19d494bf01502`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-993efc9f8d4e533d6f32"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-993efc9f8d4e533d6f32`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-e2fabb3f0b8a6a4e16f1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e2fabb3f0b8a6a4e16f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → pedestrian — 2 cases; unverified: 2</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Forbidden transfer**<br>from port: external-17; to port: external-18; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-7b7c79d53c6fdcb2868c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-19; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-68bb0ed5b880e3158c72">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-18; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-7b7c79d53c6fdcb2868c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7b7c79d53c6fdcb2868c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-18; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-19; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-68bb0ed5b880e3158c72"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-68bb0ed5b880e3158c72`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-19; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The earliest design was a source-only schematic with provisional 12 m-wide highway decks, 48 m lower curves, and 80 m upper curves. The measured native DD RHW-4 deck width is 16 m. The first compiled design snapped the paths to native tile-side lanes and used approximately 50.04 m lower curves and 80.47 m upper curves, with 17 placements and unrestricted turns to both avenue directions. The earlier right-turn revision moved the highway ramp joins one diagonal grid step outward, used longer curves, retained 15 component placements, restricted ramp traffic to adjacent-carriageway right turns, closed unused upper-deck barrier openings, and replaced flat swatches with measured native NAM ramp materials. The current shoulder revision adds four functional auxiliary lanes and their native-material markings, retaining those outer ramps and grades. The first compiled candidate’s [render report](evidence/design-history/before-right-turn-extension/compiled-render.json) is retained separately from current render evidence. The [schematic top](previews/schematic-top.png), [opposite angled view](previews/schematic-northwest.png), [profiles](previews/schematic-profiles.png), and [original validation summary](evidence/validation.json) remain historical prototype evidence; they are not tests of the new compiled pieces.
