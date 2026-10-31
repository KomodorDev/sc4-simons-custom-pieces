---
title: "Testing: DD RHW-4 — Parallel Diagonal Avenue Diamond"
summary: "Verify the exact compact parallel diamond while retaining unverified human game observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — Parallel Diagonal Avenue Diamond

<!-- ASSEMBLY TESTING LAYOUT: 1 -->

[Assembly overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

The registered assembly **ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond** places fifteen distinct functional types once each. The construction union contains **31 disjoint city tiles inside 8 × 8**, with the exact poses in [assembly.jsonc](assembly.jsonc). Required software coverage includes complete native L1/L2 through traffic, two-way Avenue and pedestrian routes, all four permitted right-turn access journeys, forbidden cross-Avenue transfers, 6 m elevated ramp pavement, the terminal taper from 6 m to 3.5 m, 1 m undersides, native Jersey barrier profiles, physical joining sections, eight piers, texture mapping, all nine adaptive Avenue cells, and all four proper rotations. Every PATH, permanent identifier, owned cell, R6 turn centreline, and 6 m grade interface is retained by this ground-mouth revision.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Human game checks use only 0° CCW; supported construction states and software rotation checks remain separate.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `external-1` | road / 1 / primary | out | [8.0, -131.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `external-2` | road / 1 / primary | in | [8.0, -131.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `external-3` | road / 1 / primary | out | [8.0, -124.8, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `external-4` | road / 1 / primary | in | [8.0, -124.8, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `external-5` | road / 1 / primary | in | [40.0, -51.2, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `external-6` | road / 1 / primary | in | [40.0, -44.8, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `external-7` | road / 1 / primary | out | [44.8, -40.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `external-8` | road / 1 / primary | out | [51.2, -40.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `external-9` | road / 1 / primary | out | [88.0, -99.2, 0.0]; [0.7071067811865475, -0.7071067811865477]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `external-10` | road / 1 / primary | out | [88.0, -92.8, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `external-11` | road / 1 / primary | in | [92.8, -88.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `external-12` | road / 1 / primary | in | [99.2, -88.0, 0.0]; [-0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-668896c488171c19873d` |
| `external-13` | road / 1 / primary | in | [124.8, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `external-14` | road / 1 / primary | out | [124.8, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `external-15` | road / 1 / primary | in | [131.2, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `external-16` | road / 1 / primary | out | [131.2, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `external-17` | pedestrian / 2 / primary | in | [40.0, -55.3, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `external-18` | pedestrian / 2 / primary | out | [55.3, -40.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |
| `external-19` | pedestrian / 2 / primary | out | [88.0, -103.3, 0.0]; [0.7071067811865477, -0.7071067811865475]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
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

Use **Windows SimCity 4 with NAM 50 and right-hand traffic**, including supported Wine or CrossOver execution. Native macOS SimCity 4 is outside this DLL-dependent setup. Keep the exact audited DD RHW, MIS, controller, preview donor, and adaptive Avenue capture inputs specified in the [build guide](../../../../docs/BUILD_AND_INSTALL.md). Private paths and captured game files remain local; no native texture images are supplied by these public sources.

A **DAT** is a game-resource archive. An **S3D** resource contains an indexed visible model, and a **PATH** resource contains directed traffic data. Car transport is class 1, and pedestrian transport is class 2. A native Avenue texture supplies visible ground appearance; a rotated retained model supplies elevated highway and ramp geometry. Neither appearance nor a preview establishes a working traffic connection.

**Adaptive ground** means that the visible Avenue pavement can follow the game's native development-dependent appearance rules. A **prop** is an attached three-dimensional model, and a **T21** is the network-tile attachment record that places it. In this implementation, native ground textures supply the changing pavement; rotating props supply the retained highway and ramp geometry. A pedestrian PATH supplies the possible walking route. These are three separate resources, and all three are implemented for their declared roles.

For a game test, install only the matching verified selection using the shared build/install procedure, with SimCity 4 fully closed during file replacement. The final component-cycle menu is prepared separately from the ordinary fifteen-piece build. Compiling, verifying, rendering, and packaging do not install files. Preserve the existing R40/compact installations or saved cities independently rather than treating the new identifiers as automatic replacements.

1. Open a disposable city, pause the simulation, and flatten enough land for the 8 × 8 core plus outside approaches. A 14 × 14 flat test area gives three extra tiles on each side; those approach reserves are not part of the 31-cell core count.
2. Use a north-up camera for the first layout. The reference picture labels tile centres **X0–X9** eastward and **Y0–Y9** northward. The occupied core lies at **X1–X8/Y1–Y8**. A 16 m tile's sides lie 8 m from its centre; keep this display grid distinct from the source's columns-east/rows-south coordinates.
3. Follow the [complete placement table](README.md#3-placements), using P02, P01, and P03 first, then P04–P15. The temporary local [1,1] handles are clear in that order. Check the exact occupied squares before every click; two different model silhouettes may overlap without sharing a construction owner.
4. Extend normal diagonal Avenue outward from the northwest and southeast mouths. Match every L1/L2 native DD RHW-4 boundary before testing external highway approaches. The exact native starter/drag sequence and external in-game compatibility still require observation; do not infer them from a software image or one matching lane.
5. Save this fresh reference layout before changing pavement development, testing redraw, or demolishing components. Use separate copies for each destructive test so failures remain reproducible.

## 3. Software checks

Run these commands from the repository directory containing `custom-pieces/`. The first command inspects the existing ordinary build; the second independently checks the saved complete layout, and the third checks current documentation. A missing build or report is not a pass. Successful software checks never record a human game observation.

```sh
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/ddrhw-parallel-diamond-slip-lanes-02
python3 -B custom-pieces/domains/highway/tools/verify_parallel_assembly.py --build custom-pieces/dist/ddrhw-parallel-diamond-slip-lanes-02 --output custom-pieces/domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/evidence/saved-assembly.json
python3 -B custom-pieces/scp.py docs-check --assembly ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond
python3 -B tools/run_tests.py
```

The current slip-lane revision targets the distinct measured build `ddrhw-parallel-diamond-slip-lanes-02`. The [complete saved-assembly report](evidence/saved-assembly.json) identifies its exact source manifest, decoded traffic-fragment count, and actual pass fields; match that source to the current revision before using its result. The check covers the 31-cell union, every saved traffic fragment, all four proper rotations, continuous car support, each authored pavement width, eight functional physical cuts, and all eight piers. A report for `ddrhw-parallel-diamond-parts-01` or `ddrhw-parallel-diamond-pedestrian-mouths-01` establishes only its own earlier geometry. Naming the new target does not assert that its verification has already passed.

The shoulder revision retains the physical ramp meshes and every route point outside the native 8 m deck edge. Within the deck, each lower access route starts 6.788225 m farther upstream, tapers smoothly sideways over 8 m, and runs straight along the shoulder for 4 m. Each upper access route keeps its old outer port, tapers over 5 m, and runs straight for 1 m. These are 12 m lower and 6 m upper shoulder sections, measured along the straight highway axis from the through lane toward the ramp; an on-ramp travels through them in reverse. The remaining smooth join meets the retained outside-deck route with its previous direction. The upper owned-cell arrangement cannot supply the lower 12 m profile without adding traffic cells, so the shorter upper profile preserves the approved 31-cell/8 × 8 footprint. Both auxiliary centres are 5.5 m from the highway axis. A checked 2.5 m car corridor reaches 6.75 m from that axis and leaves 0.421875 m to the native barrier foot at 7.171875 m on the straight section. The white markings follow the revised routes; the native through routes, physical openings, separate departures, grades, and narrower ground mouths remain in their previous positions.

The [historical visual reassignment proof](evidence/native-visual-transfer.json) covers the earlier 106,350-triangle highway/paint/pier reassignment, with its original material, texture-coordinate, winding, and approximately 0.548 micrometre coordinate-drift results. A micrometre is one millionth of a metre. Its older manifest identifies that historical scope; it does not establish texture-coordinate preservation for the later shoulder revision, which intentionally changes the native tyre-wear phase. The [current native-slip preservation report](evidence/native-slip-preservation.json) is the separate evidence for this revision: unchanged non-DD model bodies, native texture coordinates outside the allowed shoulder mask, strict forward coverage within 2 micrometres, and source-certified positive fragments filling an earlier native-coverage hole. Each such fill must lie on its independently identified original raw native face; it cannot be justified by a general increase in tolerance. Match the report's exact manifest and actual pass fields before claiming that result. The [native highway/ramp texture-seam check](evidence/native-wheeltrack-seam-uv.json) separately records its own twenty saved joins and phase-reset negative control. Neither preservation evidence nor a software render supplies a human game pass.

Texture coordinates, labelled U and V, select a position within an existing native texture image. The owning verifier reconstructs the exact approved route positions independently of the writer, checks every emitted native/access fragment, and tests the complete layout through four proper rotations. Actual indexed triangles establish continuous car support and intrusion checks, each section's authored pavement width, sampled undersides and barrier profiles, and the eight separately owned physical cuts. Bounded native float32 edge certificates address encoding residuals without broadening the road or moving a PATH. At an external native entrance collar, part of the native road width can lie beyond the owned core and must be supplied by the adjoining highway; the report identifies those bounded omissions while retaining the applicable authored width at every ramp section. Material and texture checks inspect saved flags and UV coordinates, not a renderer's colour choices. Structural load capacity and filtered game appearance remain outside these software checks.

The visible terminal asphalt is 6 m wide at the unchanged grade joining section and narrows smoothly to 3.5 m over the first 3 m toward the Avenue. It stays 3.5 m through the remainder of the R6 quarter-turn and its native-lane joining collar. The ramp centreline crosses the retained pedestrian-route centreline 3.258752 m from that grade join, approximately 0.259 m after the taper ends. This measures the two route centrelines, not the first asphalt contact: the pavement footprint already crosses the pedestrian route while the taper narrows. The checked car corridor is 2.5 m wide; the narrow asphalt leaves 0.5 m on either side of that corridor. Where the terminal road and an Avenue pedestrian centreline run alongside each other, the asphalt edge is approximately 1.149 m away. This last value excludes the driveway crossings and does not measure a complete sidewalk's width.

The adaptive-sidewalk resource implementation covers **P01, P02, and P03, with three Avenue cells each**. Each resolved native Avenue tile receives all four captured appearance variants at all five zoom levels. The ground Avenue meshes are removed from its attached prop, allowing those native textures to remain visible. The prop retains the highway, barriers, supports, and terminal asphalt that belong above the ground; its full-geometry rotation setting and compensated tile pose keep that model aligned as the construction rotates. The retained directed car and pedestrian PATHs are bound separately to the resolved Avenue tiles. The native rule flags, T21 selectors, and temporary local [1,1] construction helper complete that resource chain. This is implemented resource behaviour, rather than an unimplemented sidewalk placeholder.

The game chooses a pavement variant according to its native surroundings and development rules; connecting ordinary Avenue alone does not force a developed sidewalk variant. The ground-mouth revision preserves the nine native texture families and the rotating-prop mechanism, and adds no fixed sidewalk slab. A driveway necessarily cuts across the retained pedestrian route before joining the adjacent carriageway. The native sidewalk can remain visible beside that driveway, while the crossing itself remains road asphalt. Actual sidewalk appearance, moving pedestrians through the crossing, overlay rotation, redraw, and persistence still require observations of this new assembly. A sidewalk replacement mod that changes only the original native texture IDs does not automatically replace the copied custom IDs; its compatibility needs its own check.

A chord is the straight segment between two consecutive traffic-route points. These PATHs store coordinates to nine decimal places, while the shared connection graph samples them to six decimal places. Rounding a short segment can noticeably change its calculated direction. The reviewed `tangent` therefore retains the independently approved source-chord direction; `sampled_tangent` and the signed grade retain the actual shared-engine measurements separately. The [accepted connector measurements](checks/accepted-connector-contracts.jsonc) record the current incident full-precision saved chords and their individual nine-decimal coordinate-rounding bounds. Their exact counts and largest errors belong to the current accepted record; the earlier mouth revision's values do not establish this changed shoulder profile. No shared joining tolerance is relaxed to make the new access routes pass.

Regenerate the supplementary implemented drawing only from a matching saved build, after its checks pass:

```sh
python3 -B custom-pieces/domains/highway/tools/draw_parallel_atomization.py --build custom-pieces/dist/ddrhw-parallel-diamond-slip-lanes-02
```

The drawing's [PNG](previews/parallel-atomization.png) and [resource provenance](evidence/parallel-atomization.json) retain actual traffic lines, ownership, model projections, structural obstacles, and selected physical cuts. The optional editable `previews/parallel-atomization.svg` is available in a Git checkout; portable source archives include the PNG and drawing generator under the existing export policy. They supplement the canonical six views rather than replacing them. The exact 15-type decomposition is crossing 3 tiles, terminals 3 tiles each, slip sections 2 tiles each, lateral departures 1 tile each, lower grades 2 tiles each, and upper grades 3 tiles each: **3 + 6 + 8 + 4 + 4 + 6 = 31**.

The assembly-cycle layout is **parallel-diagonal-diamond**. Prepare its current menu candidate from the measured `custom-pieces/dist/ddrhw-parallel-diamond-slip-lanes-02` resources and the matching final documentation, following [Prepare the assembly menu](../../../../docs/BUILD_AND_INSTALL.md#8-prepare-the-assembly-menu). The first revision's `ddrhw-parallel-diamond-parts-01`, `ddrhw-parallel-diamond-parts-final`, and `ddrhw-parallel-diamond-menu-final` outputs, and the later `ddrhw-parallel-diamond-pedestrian-mouths-01` build, retain their original geometry and provenance. Their names do not identify this longer-slip-lane revision. Building the matching menu package remains separate from installation and game observation.

## 4. Game checks

### 4.1 Native highway connection test

This test covers the experimental outside native approaches described in [the network specification](../../NETWORK_SPEC.md#12-native-highway-approach-experiment). A **construction request** runs when a component is placed; it does not run again just because a city is loaded. Preserve the existing city, and use a disposable test city for these steps. The software checks do not establish the following game results.

1. Open **Transportation → Highways**, choose **SCP | ASSEMBLY | DD RHW-4 — Parallel Diagonal Avenue Diamond**, and press **Tab** until you reach **P06 — L2 Exit Slip Lanes — Parallel**. Place a fresh copy on empty, flat land with one clear city square immediately beyond its exposed highway end. Repeat with **P07 — L2 Entry Slip Lanes — Parallel**. In the pictured 0° layout, the outside squares are (X0, Y1) beyond P06 and (X8, Y9) beyond P07. Inspect whether a native double-decker continuation appears in each outside square. Record a missing tile, a wrong angle, or an incorrect upper/lower direction separately.
2. Use an already working NAM DDRHW-4 highway, as in the reported failing case. Extend its existing diagonal end towards the newly created outside tile with the ordinary RealHighway drawing tool. Release the mouse at the native approach tile; the fixed custom junction is not the drag target. Record whether the native DD appearance reaches the seam and remains after releasing the mouse. Repeat at the other end.
3. In a separate empty area, reverse the order: extend an existing diagonal DD highway first, then place the fresh custom end beside it. Keep its declared outside approach square available to the native highway. Record placement acceptance and any change to the existing highway separately from step 2.
4. Repeat fresh placement at all four orientations using **Home** or **End** before clicking. Check the upper and lower deck directions against the native highway, rather than checking the road angle alone. Turning the city camera does not count as placing another orientation. An opposite-flow native highway is a separate unsupported case until tested.
5. Supply car origins and destinations beyond both highway ends. Use **Route Query** to inspect each deck, and observe an actual moving car through each seam. A road that looks joined does not establish traffic continuity. Repeat the assembly's four ramp journeys and the adaptive-sidewalk checks below.
6. Save the test city, quit the game completely, reopen the city, and repeat the seam and representative traffic checks. In a separate saved copy, demolish and replace the end component, inspect the outside native tile, and repeat joining. Record whether the native continuation survives or needs reconstruction.
7. In another disposable copy, occupy the helper square with a protected custom piece before attempting placement. Record whether placement is rejected without changing that neighbour. Do not treat the word `optional` in the source as an overwrite guarantee. Keep this collision case separate from joining to an ordinary draggable native DD tile.

Record the exact build, component, orientation, placement order, deck direction, and observed outcome using [the shared observation procedure](../../../../docs/TESTING.md#4-record-one-observation). These cases remain unverified until a matching human observation is recorded.

### 4.2 Retained assembly checks


All game observations below are unverified for this new assembly until the user confirms their exact cases. The older adaptive-sidewalk experiment established its own recorded observations; it does not approve this kit's new placement bounds, new terminal geometry, or new external connections.

1. **Menu and placement:** find **SCP | ASSEMBLY | DD RHW-4 — Parallel Diagonal Avenue Diamond** in **Transportation → Highways**. Cycle all fifteen exact names forward with Tab and backward with Shift+Tab. Place each component once using the table, beginning P02 → P01 → P03, and confirm that no temporary Road helper remains.
2. **Occupied neighbours and redraw:** in a separate saved copy, try P02 after P01 has already occupied its helper corner, try the other adaptive owners beside existing pieces, try placement over an already built normal Avenue, and try dragging Avenue through the completed ground corridor. Record each outcome separately; do not count the conservative first sequence as proof of these other behaviours.
3. **Orientation:** repeat fresh placement in all four distinct proper rotations. Confirm that the highway remains perpendicular to the Avenue in each one. Rotate the camera separately after placement, and inspect both sides of the highway, each ramp opening, the longer lower and shorter upper shoulder markings, the small right turns, the eight piers, and all shadows.
4. **Adaptive sidewalks and driveways:** first inspect the newly placed Avenue on undeveloped ground. Connect Avenue outside both ends, develop nearby zones until the ordinary adjoining Avenue changes its native pavement variant, and compare P01, P02, and P03. Connecting Avenue alone is not the appearance-change trigger. Check that the highway and ramp overlays remain at the correct angle while the visible ground pavement updates. Inspect the four narrow ground mouths from above: each should keep its 6 m grade join, narrow to 3.5 m, and expose native ground beside its turn. Inspect the actual pedestrian driveway crossings separately; road asphalt at those crossings is part of this design, rather than a promise of an uninterrupted pavement slab. Record each visible appearance separately from pedestrian Route Query and visible walking.
5. **Through journeys:** provide matching outside approaches and actual origins/destinations. Check Route Query and visible travel separately for southwest → northeast on L2, northeast → southwest on L1, northwest → southeast on the Avenue, southeast → northwest on the Avenue, and the two pedestrian Avenue directions.
6. **Right-turn ramp journeys:** test northeast highway → northwest Avenue through the lower exit; northwest Avenue → southwest highway through the lower entry; southwest highway → southeast Avenue through the upper exit; and southeast Avenue → northeast highway through the upper entry. Record the query and observed moving car for every route.
7. **Forbidden transfers:** confirm that northeast highway → southeast Avenue, southeast Avenue → southwest highway, southwest highway → northwest Avenue, and northwest Avenue → northeast highway are unavailable. Check that no upper/lower-deck transfer or car/pedestrian transport change appears merely because two models overlap.
8. **Persistence and demolition:** save, quit completely, reload, and repeat representative traffic and pavement checks. In a separate copy, demolish each component, inspect the neighbouring roads for leftover models or removed Avenue cells, replace it, and save/reload again.

Use [the shared observation workflow](../../../../docs/TESTING.md) to record the exact assembly **ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond**, its current cases, and the matching source/environment. A visible sidewalk is not a pedestrian-travel pass, Route Query is not visible car travel, and a rotation of the camera is not fresh placement in another orientation.

## 5. Results and known issues

Current generated records below retain exact evidence and observation states. No new human game pass is asserted. Resource compilation, saved route verification, actual model support, source-bound connector cards, and software renders have distinct scopes; none establishes native game placement, sidewalk appearance, external draggable connections, or moving traffic.

**Placement crash recorded on 2026-10-31:** the user reported that **L1 Exit Slip Lanes — Parallel** (`f84a`) crashes Windows SimCity 4 1.1.641.0 with NAM 50 under Wine, both on clear ground and beside the Avenue. Both preserved reports fault at `0x00803E2E`; their exact candidate fingerprint and the identified packed vertex-format mismatch are retained in [the frozen crash record](evidence/placement-crash-20261031.json). The construction orientation and the mapping of each report to its location are unknown, so this does not assign a failure to an individual rotation case. The corrective encoding change still requires a fresh human placement retest; software checks and previews do not establish that the crash is fixed.

The geometry is deliberately compressed. Each high departure moves sideways over 17 m along the highway at full deck height; descent starts only when its complete 6 m width lies outside the native deck. The straight grades are 44.872251 m lower and 56.185959 m upper, with approximately 17.911624% and 28.202932% peak source slopes, respectively. The experimental limit is 30%. The R6 terminals are custom geometry, not a claim that an existing NAM ramp has those dimensions. Fixed grade modules do not acquire arbitrary height offsets or adapt to sloping terrain.

The revised shoulder sections are also constrained by this footprint. Measured along the straight highway axis, lower routes have 8 m of sideways taper and 4 m straight at the shoulder, while upper routes have 5 m and 1 m. The straight auxiliary centre is 5.5 m from the highway axis. Its 0.421875 m checked car-corridor clearance to the native barrier foot is a specific geometric measurement, not a general vehicle-size, speed, or real-road safety guarantee. The roadway beyond the native deck edge, physical barrier openings, and separate ramp modules are retained. The lower upstream extension uses an already owned highway tile; the upper section cannot be lengthened to match without expanding the traffic footprint.

The three-cell crossing is the smallest coherent mixed-network owner in this layout, but it also stores upper ground-turn fragments crossing those same city tiles. The straight grade owners similarly retain PATHs in native highway half-cells traversed by outside-deck access traffic. The visible native halves, their white paint, and their centre piers belong to the adjacent slip-lane models by overhang, so the grade models remain pure ramps and the crossing/slip models form the complete straight highway stem. Consequently, none of the four ordinary highway halves from the wider study is an unchanged full-cell substitute here. Every saved traffic fragment retains one city-tile owner, while each complete curved departure or straight grade model belongs to its functional component and can overhang that boundary.

All nine Avenue cells have the complete native adaptive texture variants, retained car and pedestrian paths, rotating model props, and rule bindings. Each sparse 2 × 2 adaptive owner has a removable helper at local [1,1]. The narrower terminal overlays leave more native ground visible beside the driveway, while its actual pedestrian crossing remains asphalt. The pinned DLL's helper removal does not itself prove that the game will accept every occupied-neighbour cursor situation. Avenue texture variants, redraw, overlay rotation, pedestrians, car transfer between resolved Avenue and fixed highway networks, demolition, and persistence need the focused game tests above. No successful observation of the older adaptive probe is promoted to a pass for this assembly.

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
python3 -m scp.content record --record custom-pieces/domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/checks/manual-tests.json --observation custom-pieces/domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-3fc282b2535ab544443e">[ ] unverified</a> | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-3fc282b2535ab544443e"></a>

**General: unverified** — `software_resources-3fc282b2535ab544443e`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-3fc282b2535ab544443e">[ ] unverified</a> | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-3fc282b2535ab544443e"></a>

**General: unverified** — `software_connectivity-3fc282b2535ab544443e`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-df9ef4e05aeff6621a5b">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-df9ef4e05aeff6621a5b"></a>

**0° CCW: unverified** — `in_game_render-df9ef4e05aeff6621a5b`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-df9ef4e05aeff6621a5b">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-df9ef4e05aeff6621a5b"></a>

**0° CCW: unverified** — `in_game_placement-df9ef4e05aeff6621a5b`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-df9ef4e05aeff6621a5b">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-df9ef4e05aeff6621a5b"></a>

**0° CCW: unverified** — `in_game_demolition-df9ef4e05aeff6621a5b`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-df9ef4e05aeff6621a5b">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-df9ef4e05aeff6621a5b"></a>

**0° CCW: unverified** — `in_game_save_reload-df9ef4e05aeff6621a5b`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: external-11>external-7; entry: external-11; exit: external-7 | — | <a href="#case-in_game_route_query-594632d4fe383ea9b612">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-12>external-16; entry: external-12; exit: external-16 | — | <a href="#case-in_game_route_query-545e048a7dadf0fa6bae">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-12>external-8; entry: external-12; exit: external-8 | — | <a href="#case-in_game_route_query-0aa7a738ca4dcce53666">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-13>external-3; entry: external-13; exit: external-3 | — | <a href="#case-in_game_route_query-13fed700a7fd0118fd92">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-13>external-8; entry: external-13; exit: external-8 | — | <a href="#case-in_game_route_query-6b716472071f40b2272b">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-15>external-1; entry: external-15; exit: external-1 | — | <a href="#case-in_game_route_query-02d98a532d3f3a6e919c">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-2>external-16; entry: external-2; exit: external-16 | — | <a href="#case-in_game_route_query-0416e38938bce251b0fd">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-2>external-9; entry: external-2; exit: external-9 | — | <a href="#case-in_game_route_query-88ff90dc63dafe7621dd">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-4>external-14; entry: external-4; exit: external-14 | — | <a href="#case-in_game_route_query-534cfa7b2ac7ff969472">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3 | — | <a href="#case-in_game_route_query-217f36d98365ba353cd5">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9 | — | <a href="#case-in_game_route_query-48cae13231dfa2e77099">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-6>external-10; entry: external-6; exit: external-10 | — | <a href="#case-in_game_route_query-480ef7ca711e6f036c2e">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: external-11>external-7; entry: external-11; exit: external-7</summary>

<a id="case-in_game_route_query-594632d4fe383ea9b612"></a>

**0° CCW: unverified** — `in_game_route_query-594632d4fe383ea9b612`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-11>external-7; entry: external-11; exit: external-7.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-12>external-16; entry: external-12; exit: external-16</summary>

<a id="case-in_game_route_query-545e048a7dadf0fa6bae"></a>

**0° CCW: unverified** — `in_game_route_query-545e048a7dadf0fa6bae`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-12>external-16; entry: external-12; exit: external-16.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-12>external-8; entry: external-12; exit: external-8</summary>

<a id="case-in_game_route_query-0aa7a738ca4dcce53666"></a>

**0° CCW: unverified** — `in_game_route_query-0aa7a738ca4dcce53666`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-12>external-8; entry: external-12; exit: external-8.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-13>external-3; entry: external-13; exit: external-3</summary>

<a id="case-in_game_route_query-13fed700a7fd0118fd92"></a>

**0° CCW: unverified** — `in_game_route_query-13fed700a7fd0118fd92`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-13>external-3; entry: external-13; exit: external-3.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-13>external-8; entry: external-13; exit: external-8</summary>

<a id="case-in_game_route_query-6b716472071f40b2272b"></a>

**0° CCW: unverified** — `in_game_route_query-6b716472071f40b2272b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-13>external-8; entry: external-13; exit: external-8.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-15>external-1; entry: external-15; exit: external-1</summary>

<a id="case-in_game_route_query-02d98a532d3f3a6e919c"></a>

**0° CCW: unverified** — `in_game_route_query-02d98a532d3f3a6e919c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-15>external-1; entry: external-15; exit: external-1.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-2>external-16; entry: external-2; exit: external-16</summary>

<a id="case-in_game_route_query-0416e38938bce251b0fd"></a>

**0° CCW: unverified** — `in_game_route_query-0416e38938bce251b0fd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-2>external-16; entry: external-2; exit: external-16.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-2>external-9; entry: external-2; exit: external-9</summary>

<a id="case-in_game_route_query-88ff90dc63dafe7621dd"></a>

**0° CCW: unverified** — `in_game_route_query-88ff90dc63dafe7621dd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-2>external-9; entry: external-2; exit: external-9.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-4>external-14; entry: external-4; exit: external-14</summary>

<a id="case-in_game_route_query-534cfa7b2ac7ff969472"></a>

**0° CCW: unverified** — `in_game_route_query-534cfa7b2ac7ff969472`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-4>external-14; entry: external-4; exit: external-14.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3</summary>

<a id="case-in_game_route_query-217f36d98365ba353cd5"></a>

**0° CCW: unverified** — `in_game_route_query-217f36d98365ba353cd5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9</summary>

<a id="case-in_game_route_query-48cae13231dfa2e77099"></a>

**0° CCW: unverified** — `in_game_route_query-48cae13231dfa2e77099`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-6>external-10; entry: external-6; exit: external-10</summary>

<a id="case-in_game_route_query-480ef7ca711e6f036c2e"></a>

**0° CCW: unverified** — `in_game_route_query-480ef7ca711e6f036c2e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-6>external-10; entry: external-6; exit: external-10.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: external-11>external-7; entry: external-11; exit: external-7 | — | <a href="#case-in_game_visible_travel-594632d4fe383ea9b612">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-12>external-16; entry: external-12; exit: external-16 | — | <a href="#case-in_game_visible_travel-545e048a7dadf0fa6bae">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-12>external-8; entry: external-12; exit: external-8 | — | <a href="#case-in_game_visible_travel-0aa7a738ca4dcce53666">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-13>external-3; entry: external-13; exit: external-3 | — | <a href="#case-in_game_visible_travel-13fed700a7fd0118fd92">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-13>external-8; entry: external-13; exit: external-8 | — | <a href="#case-in_game_visible_travel-6b716472071f40b2272b">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-15>external-1; entry: external-15; exit: external-1 | — | <a href="#case-in_game_visible_travel-02d98a532d3f3a6e919c">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-2>external-16; entry: external-2; exit: external-16 | — | <a href="#case-in_game_visible_travel-0416e38938bce251b0fd">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-2>external-9; entry: external-2; exit: external-9 | — | <a href="#case-in_game_visible_travel-88ff90dc63dafe7621dd">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-4>external-14; entry: external-4; exit: external-14 | — | <a href="#case-in_game_visible_travel-534cfa7b2ac7ff969472">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3 | — | <a href="#case-in_game_visible_travel-217f36d98365ba353cd5">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9 | — | <a href="#case-in_game_visible_travel-48cae13231dfa2e77099">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-6>external-10; entry: external-6; exit: external-10 | — | <a href="#case-in_game_visible_travel-480ef7ca711e6f036c2e">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-11>external-7; entry: external-11; exit: external-7</summary>

<a id="case-in_game_visible_travel-594632d4fe383ea9b612"></a>

**0° CCW: unverified** — `in_game_visible_travel-594632d4fe383ea9b612`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-11>external-7; entry: external-11; exit: external-7.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-12>external-16; entry: external-12; exit: external-16</summary>

<a id="case-in_game_visible_travel-545e048a7dadf0fa6bae"></a>

**0° CCW: unverified** — `in_game_visible_travel-545e048a7dadf0fa6bae`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-12>external-16; entry: external-12; exit: external-16.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-12>external-8; entry: external-12; exit: external-8</summary>

<a id="case-in_game_visible_travel-0aa7a738ca4dcce53666"></a>

**0° CCW: unverified** — `in_game_visible_travel-0aa7a738ca4dcce53666`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-12>external-8; entry: external-12; exit: external-8.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-13>external-3; entry: external-13; exit: external-3</summary>

<a id="case-in_game_visible_travel-13fed700a7fd0118fd92"></a>

**0° CCW: unverified** — `in_game_visible_travel-13fed700a7fd0118fd92`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-13>external-3; entry: external-13; exit: external-3.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-13>external-8; entry: external-13; exit: external-8</summary>

<a id="case-in_game_visible_travel-6b716472071f40b2272b"></a>

**0° CCW: unverified** — `in_game_visible_travel-6b716472071f40b2272b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-13>external-8; entry: external-13; exit: external-8.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-15>external-1; entry: external-15; exit: external-1</summary>

<a id="case-in_game_visible_travel-02d98a532d3f3a6e919c"></a>

**0° CCW: unverified** — `in_game_visible_travel-02d98a532d3f3a6e919c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-15>external-1; entry: external-15; exit: external-1.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-2>external-16; entry: external-2; exit: external-16</summary>

<a id="case-in_game_visible_travel-0416e38938bce251b0fd"></a>

**0° CCW: unverified** — `in_game_visible_travel-0416e38938bce251b0fd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-2>external-16; entry: external-2; exit: external-16.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-2>external-9; entry: external-2; exit: external-9</summary>

<a id="case-in_game_visible_travel-88ff90dc63dafe7621dd"></a>

**0° CCW: unverified** — `in_game_visible_travel-88ff90dc63dafe7621dd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-2>external-9; entry: external-2; exit: external-9.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-4>external-14; entry: external-4; exit: external-14</summary>

<a id="case-in_game_visible_travel-534cfa7b2ac7ff969472"></a>

**0° CCW: unverified** — `in_game_visible_travel-534cfa7b2ac7ff969472`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-4>external-14; entry: external-4; exit: external-14.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3</summary>

<a id="case-in_game_visible_travel-217f36d98365ba353cd5"></a>

**0° CCW: unverified** — `in_game_visible_travel-217f36d98365ba353cd5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9</summary>

<a id="case-in_game_visible_travel-48cae13231dfa2e77099"></a>

**0° CCW: unverified** — `in_game_visible_travel-48cae13231dfa2e77099`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-6>external-10; entry: external-6; exit: external-10</summary>

<a id="case-in_game_visible_travel-480ef7ca711e6f036c2e"></a>

**0° CCW: unverified** — `in_game_visible_travel-480ef7ca711e6f036c2e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-6>external-10; entry: external-6; exit: external-10.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — pedestrian — 2 cases; unverified: 2</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Route Query**<br>Service: pedestrian; role: primary; journey: external-17>external-19; entry: external-17; exit: external-19 | — | <a href="#case-in_game_route_query-5d6ba3ff2feb9ca427f3">[ ] unverified</a> |
| **Route Query**<br>Service: pedestrian; role: primary; journey: external-20>external-18; entry: external-20; exit: external-18 | — | <a href="#case-in_game_route_query-7df6e910902e03b4a1bb">[ ] unverified</a> |


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: external-17>external-19; entry: external-17; exit: external-19</summary>

<a id="case-in_game_route_query-5d6ba3ff2feb9ca427f3"></a>

**0° CCW: unverified** — `in_game_route_query-5d6ba3ff2feb9ca427f3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: external-17>external-19; entry: external-17; exit: external-19.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: external-20>external-18; entry: external-20; exit: external-18</summary>

<a id="case-in_game_route_query-7df6e910902e03b4a1bb"></a>

**0° CCW: unverified** — `in_game_route_query-7df6e910902e03b4a1bb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: external-20>external-18; entry: external-20; exit: external-18.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — pedestrian — 2 cases; unverified: 2</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: external-17>external-19; entry: external-17; exit: external-19 | — | <a href="#case-in_game_visible_travel-5d6ba3ff2feb9ca427f3">[ ] unverified</a> |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: external-20>external-18; entry: external-20; exit: external-18 | — | <a href="#case-in_game_visible_travel-7df6e910902e03b4a1bb">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: external-17>external-19; entry: external-17; exit: external-19</summary>

<a id="case-in_game_visible_travel-5d6ba3ff2feb9ca427f3"></a>

**0° CCW: unverified** — `in_game_visible_travel-5d6ba3ff2feb9ca427f3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: external-17>external-19; entry: external-17; exit: external-19.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: external-20>external-18; entry: external-20; exit: external-18</summary>

<a id="case-in_game_visible_travel-7df6e910902e03b4a1bb"></a>

**0° CCW: unverified** — `in_game_visible_travel-7df6e910902e03b4a1bb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: external-20>external-18; entry: external-20; exit: external-18.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 52 cases; unverified: 52</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Forbidden transfer**<br>from port: external-2; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-7f9e8270fd8608916edd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-910caed083a20d7e7a84">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-2f1a48847e162e808115">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-05d825d26f483a28ec48">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-8ef7ff39f5b07466a89e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-d35d728eaee9116ea7e6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f861eab51510e615fbc1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-c5f8357eed78bb1c9018">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-84b251491b8c8723652e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-c5d655d3ab1d53609d5a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-494de8c83840c260f40a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-b65dc552d3e459b7572d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-3e32693ab51750277bd4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-dd677a089c7b76830be0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-a52b495f5c7b9680bebc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-8d7b64e3610ef561d8fe">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-a6ab9b04533e16595eb5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-59dbae0d5c744076c467">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ea53b93312075c8b3e43">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-500048f800080c70936f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-c7ad449f3590bef45213">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-0a0baceeec1e2068912f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f105ff8e4cc155e5a23e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-4e0108db99a20a28e256">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-393ad8265653d5da19bb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-5a5b89414c09a60faea8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-4b749d5278607f375735">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-a2d173d460731f7d2887">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ec62f170003cbad03fb7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-d0b94d8a02d0a4a7bb49">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-44b01327ac6e3b44510a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-c4a123078a21cc6b5ac8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-01ef4f06792dbd69c981">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-edb7d19ca3838e25f80a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-c343aaf62757b3db3833">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-7691e455744785d013ca">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-fc20335b86e977287192">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-de5d0669e19d6d68c51f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-48d49f94217543254123">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-d095d1a070f57fdaeb74">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-79ae4fdfc85b7e8377be">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-80cce82366ed76335490">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-567a807e5990af8dd441">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-1d14f02ac0e4a99f749c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-493f7ab41ee394612115">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-7cae2bb5ef4d85c8a0ea">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-0355f07d646b92191ff7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-a1dfe98f161f16e086fe">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ca71dba7164134ec8224">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-9315f4bfd55474f2545b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-d06969267f03389dd704">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-b68ca5ef7b59736ee401">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-7f9e8270fd8608916edd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7f9e8270fd8608916edd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-910caed083a20d7e7a84"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-910caed083a20d7e7a84`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-2f1a48847e162e808115"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2f1a48847e162e808115`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-05d825d26f483a28ec48"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-05d825d26f483a28ec48`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-8ef7ff39f5b07466a89e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8ef7ff39f5b07466a89e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-d35d728eaee9116ea7e6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d35d728eaee9116ea7e6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f861eab51510e615fbc1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f861eab51510e615fbc1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-c5f8357eed78bb1c9018"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c5f8357eed78bb1c9018`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-84b251491b8c8723652e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-84b251491b8c8723652e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-c5d655d3ab1d53609d5a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c5d655d3ab1d53609d5a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-494de8c83840c260f40a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-494de8c83840c260f40a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-b65dc552d3e459b7572d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b65dc552d3e459b7572d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-3e32693ab51750277bd4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3e32693ab51750277bd4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-dd677a089c7b76830be0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dd677a089c7b76830be0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-a52b495f5c7b9680bebc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a52b495f5c7b9680bebc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-8d7b64e3610ef561d8fe"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8d7b64e3610ef561d8fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-a6ab9b04533e16595eb5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a6ab9b04533e16595eb5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-59dbae0d5c744076c467"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-59dbae0d5c744076c467`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ea53b93312075c8b3e43"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ea53b93312075c8b3e43`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-500048f800080c70936f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-500048f800080c70936f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-c7ad449f3590bef45213"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c7ad449f3590bef45213`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-0a0baceeec1e2068912f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0a0baceeec1e2068912f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f105ff8e4cc155e5a23e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f105ff8e4cc155e5a23e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-4e0108db99a20a28e256"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4e0108db99a20a28e256`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-393ad8265653d5da19bb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-393ad8265653d5da19bb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-5a5b89414c09a60faea8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5a5b89414c09a60faea8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-4b749d5278607f375735"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4b749d5278607f375735`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-a2d173d460731f7d2887"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a2d173d460731f7d2887`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ec62f170003cbad03fb7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ec62f170003cbad03fb7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-d0b94d8a02d0a4a7bb49"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d0b94d8a02d0a4a7bb49`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-44b01327ac6e3b44510a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-44b01327ac6e3b44510a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-c4a123078a21cc6b5ac8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c4a123078a21cc6b5ac8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-01ef4f06792dbd69c981"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-01ef4f06792dbd69c981`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-edb7d19ca3838e25f80a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-edb7d19ca3838e25f80a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-c343aaf62757b3db3833"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c343aaf62757b3db3833`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-7691e455744785d013ca"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7691e455744785d013ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-fc20335b86e977287192"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fc20335b86e977287192`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-de5d0669e19d6d68c51f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-de5d0669e19d6d68c51f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-48d49f94217543254123"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-48d49f94217543254123`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-d095d1a070f57fdaeb74"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d095d1a070f57fdaeb74`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-79ae4fdfc85b7e8377be"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-79ae4fdfc85b7e8377be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-80cce82366ed76335490"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-80cce82366ed76335490`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-567a807e5990af8dd441"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-567a807e5990af8dd441`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-1d14f02ac0e4a99f749c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1d14f02ac0e4a99f749c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-493f7ab41ee394612115"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-493f7ab41ee394612115`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-7cae2bb5ef4d85c8a0ea"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7cae2bb5ef4d85c8a0ea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-0355f07d646b92191ff7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0355f07d646b92191ff7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-a1dfe98f161f16e086fe"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a1dfe98f161f16e086fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ca71dba7164134ec8224"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ca71dba7164134ec8224`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-9315f4bfd55474f2545b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9315f4bfd55474f2545b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-d06969267f03389dd704"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d06969267f03389dd704`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-b68ca5ef7b59736ee401"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b68ca5ef7b59736ee401`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → pedestrian — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Forbidden transfer**<br>from port: external-2; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-6e1efa5b4b947b5b6dc0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-83c76f96b8119c034736">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f252402a2244d6131807">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-7a21f18ccce8e9de534c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-4cf06ae83c629354b94e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-5b866caaa0c61ecdc0d5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-8dd1c84805e5d5c726bc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-5de555cead3127945fff">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-1616203b91c2d54b0075">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-cd06d722d8ca78a789f9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-6370c5cb63101708857a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-25cd376dd31421a6cc21">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-b632a7b7546989fcf45a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-679a5a3b778272f8ef59">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-8dbb3121520d0a8d3e2c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-c5447ce11e3e0325993d">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-6e1efa5b4b947b5b6dc0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6e1efa5b4b947b5b6dc0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-83c76f96b8119c034736"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-83c76f96b8119c034736`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f252402a2244d6131807"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f252402a2244d6131807`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-7a21f18ccce8e9de534c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7a21f18ccce8e9de534c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-4cf06ae83c629354b94e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4cf06ae83c629354b94e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-5b866caaa0c61ecdc0d5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5b866caaa0c61ecdc0d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-8dd1c84805e5d5c726bc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8dd1c84805e5d5c726bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-5de555cead3127945fff"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5de555cead3127945fff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-1616203b91c2d54b0075"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1616203b91c2d54b0075`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-cd06d722d8ca78a789f9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cd06d722d8ca78a789f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-6370c5cb63101708857a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6370c5cb63101708857a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-25cd376dd31421a6cc21"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-25cd376dd31421a6cc21`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-b632a7b7546989fcf45a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b632a7b7546989fcf45a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-679a5a3b778272f8ef59"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-679a5a3b778272f8ef59`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-8dbb3121520d0a8d3e2c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8dbb3121520d0a8d3e2c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-18; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-c5447ce11e3e0325993d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c5447ce11e3e0325993d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-19; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → road — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Forbidden transfer**<br>from port: external-17; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-5702418065504b6eb596">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-17; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-c4c4c0785240cde9a4fc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-17; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-8fdead2eb6e2c62d63cc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-17; to port: external-8; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f612ca9d35694d63bbeb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-17; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-4f4dbc86163b7b9ad7f6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-17; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f22fc4afcc75fd2177b0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-17; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-d687f106963d0d31dc69">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-17; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-1d0388f9771e4ccdbb29">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-954053c7b47ae2346922">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ca655d0204a0ff63812f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-6ecb5f36752967e79171">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-8; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-47852064fac6c2cc841e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-5088a39bae5dae73d8af">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-9f817da07504ea143e86">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-1ff4227b2e5b65ab4738">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-26c1b51262e5bbb666f5">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-5702418065504b6eb596"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5702418065504b6eb596`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-c4c4c0785240cde9a4fc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c4c4c0785240cde9a4fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-8fdead2eb6e2c62d63cc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8fdead2eb6e2c62d63cc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-8; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f612ca9d35694d63bbeb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f612ca9d35694d63bbeb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-8; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-4f4dbc86163b7b9ad7f6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4f4dbc86163b7b9ad7f6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f22fc4afcc75fd2177b0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f22fc4afcc75fd2177b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-d687f106963d0d31dc69"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d687f106963d0d31dc69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-1d0388f9771e4ccdbb29"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1d0388f9771e4ccdbb29`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-954053c7b47ae2346922"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-954053c7b47ae2346922`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ca655d0204a0ff63812f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ca655d0204a0ff63812f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-6ecb5f36752967e79171"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6ecb5f36752967e79171`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-8; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-47852064fac6c2cc841e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-47852064fac6c2cc841e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-8; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-5088a39bae5dae73d8af"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5088a39bae5dae73d8af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-9f817da07504ea143e86"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9f817da07504ea143e86`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-1ff4227b2e5b65ab4738"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1ff4227b2e5b65ab4738`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-26c1b51262e5bbb666f5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-26c1b51262e5bbb666f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → pedestrian — 2 cases; unverified: 2</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Forbidden transfer**<br>from port: external-17; to port: external-18; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-01b6d8f4ed53c9d67704">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-19; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-dd290fc0f38d14f3cd5d">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: external-17; to port: external-18; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-01b6d8f4ed53c9d67704"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-01b6d8f4ed53c9d67704`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-17; to port: external-18; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-19; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-dd290fc0f38d14f3cd5d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dd290fc0f38d14f3cd5d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-19; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 7 cases; unverified: 7</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond:clean-southeast | <a href="#case-preview_review-9028223d7cbd64da1385">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond:clean-top | <a href="#case-preview_review-3ed9b50a27ed2fd609d1">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond:named-northwest | <a href="#case-preview_review-1093207b94856d9920b5">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond:named-southeast | <a href="#case-preview_review-6684c022a126bcb95988">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond:named-top | <a href="#case-preview_review-7adf623bde2278257523">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond:parallel-atomization | <a href="#case-preview_review-e29d04b9a965b39aae7f">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond:tile-ownership | <a href="#case-preview_review-efc2059eab2ca9c8cbec">[ ] unverified</a> | — |


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond:clean-southeast</summary>

<a id="case-preview_review-9028223d7cbd64da1385"></a>

**General: unverified** — `preview_review-9028223d7cbd64da1385`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond:clean-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond:clean-top</summary>

<a id="case-preview_review-3ed9b50a27ed2fd609d1"></a>

**General: unverified** — `preview_review-3ed9b50a27ed2fd609d1`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond:clean-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond:named-northwest</summary>

<a id="case-preview_review-1093207b94856d9920b5"></a>

**General: unverified** — `preview_review-1093207b94856d9920b5`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond:named-northwest.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond:named-southeast</summary>

<a id="case-preview_review-6684c022a126bcb95988"></a>

**General: unverified** — `preview_review-6684c022a126bcb95988`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond:named-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond:named-top</summary>

<a id="case-preview_review-7adf623bde2278257523"></a>

**General: unverified** — `preview_review-7adf623bde2278257523`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond:named-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond:parallel-atomization</summary>

<a id="case-preview_review-e29d04b9a965b39aae7f"></a>

**General: unverified** — `preview_review-e29d04b9a965b39aae7f`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond:parallel-atomization.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond:tile-ownership</summary>

<a id="case-preview_review-efc2059eab2ca9c8cbec"></a>

**General: unverified** — `preview_review-efc2059eab2ca9c8cbec`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond:tile-ownership.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The human-approved [source proposal](../ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/TESTING.md#32-close-parallel-ramps-and-perpendicular-avenue-approaches) moved the ramps close and parallel to the highway, required perpendicular Avenue approaches, and selected the inward upper sockets. This new assembly implements that approved geometry while retaining the earlier [R40/compact modular blueprint](../ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/README.md) and its frozen evidence unchanged.

The new split follows real functions: central crossing, straight slip sections, flat curved departures, straight grades, and ground right-turn terminals. Minimum construction ownership remains constrained by every complete traffic cell, not only the visible road centreline. The implementation and the [saved-model atomization drawing](previews/parallel-atomization.png) preserve that distinction for future replacement ramps and fixed-height profiles.

The earlier ground-mouth revision narrowed only the terminal asphalt from 6 m to 3.5 m after a 3 m smooth taper, preserving the 6 m grade interfaces, R6 route centrelines, and its traffic PATHs. The later slip-lane revision keeps those mouths and changes the native-shoulder access PATHs and white markings: lower shoulder sections are 12 m, upper sections are 6 m, and only the lower high ports move upstream. All fifteen permanent identifiers and the 31-cell/8 × 8 ownership remain unchanged. The original measured `parts-01` and `pedestrian-mouths-01` build identities keep their earlier scopes. `ddrhw-parallel-diamond-slip-lanes-02` measures this revision independently; its own source-bound reports and refreshed artwork are required, and no human game result is inherited.
