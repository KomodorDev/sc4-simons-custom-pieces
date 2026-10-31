---
title: "Testing: DD RHW-4 — Modular Diagonal Avenue Diamond"
summary: "Check straight-stamp ownership, full ramp overhang, traffic fragments, adaptive Avenue terminals, and scoped game observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — Modular Diagonal Avenue Diamond

<!-- ASSEMBLY TESTING LAYOUT: 1 -->

[Assembly overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

The default plan in [assembly.jsonc](assembly.jsonc) uses one completely straight 21-cell highway stamp, four separately placed full ramps owning 4, 4, 6, and 6 cells, and two R40 Avenue terminals owning 9 and 12 cells. These seven placements own 62 distinct tiles in a 10 × 10-tile construction rectangle. The compact alternative uses the same stamp, four full compact ramps, and two retained compact Avenue junctions: seven placements and 53 cells. Both decks, all four curved ramp throats, and the ground Avenue retain their assembled geometry; their construction ownership has changed.

Check all eight required car movements: the two opposing highway directions on their separate decks, both Avenue directions, and the four same-carriageway ramp turns listed in the [README](README.md). Reject the four cross-Avenue ramp movements: northeast → southeast, southeast → southwest, southwest → northwest, and northwest → northeast. Check both pedestrian through journeys independently. Each lower full ramp has four traffic ports and two intrinsic fragments joined through a stamp-owned middle tile; a standalone piece matrix therefore does not describe the entire highway-to-Avenue journey.

Software supports proper rotations of 0°, 90°, 180°, and 270° counterclockwise, without reflecting traffic. The initial human assembly test plan uses the unrotated 0° layout; that observation does not approve other orientations. A **PATH** is a saved traffic-route resource, and an **S3D** is an indexed visible model. Model overhang, traffic ownership, and physical seam fit are different facts, and each needs its corresponding check.

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

The target is Windows SimCity 4 with NAM 50 and right-hand traffic, including Wine or CrossOver. Record the actual game version, compatibility layer, NAM selection, and experimental build for each observation. Native macOS SimCity 4 is outside this target.

1. Save a disposable test city, and quit SimCity 4 before replacing installed test files. Follow the [shared build and installation procedure](../../../../docs/BUILD_AND_INSTALL.md); building and rendering do not install files.
2. Select the `ddrhw-modular-ramp-kit` collection. Its assembly button cycles the seven default R40 types; the four full compact ramps and two compact Avenue junctions have separate buttons outside that cycle. The old grade-only pieces are retained historical types, rather than complete attachments for this stamp.
3. Prepare flat, clear terrain. Use the README's [component and placement tables](README.md#3-placements), with one stamp and six separate attachments. Construction ownership may never overlap. A ramp model can draw above a stamp-owned tile without creating a second traffic owner.
4. Use X0–X9 and Y0–Y9 throughout. X increases east/right, Y increases north/up, and (X0, Y0) is the southwest tile centre. Source model coordinates use east/north/height in metres; source construction rows increase south. Those source row numbers are not the displayed Y labels.
5. Extend matching native diagonal DD RHW-4 at the southwest and northeast ends, and ordinary diagonal Avenue at the northwest and southeast ends. Provide origins and destinations outside the assembly that make each required movement useful.
6. Test the default R40 plan first. For the compact alternative, remove a matching R40 ramp pair and its terminal, retain the stamp, and use the complete compact group. Keep layout-specific observations separate.

## 3. Software checks

The [independent partition proof](evidence/straight-partition-preservation.json) passed a complete assembled source comparison against the immutable accepted R40 and compact checkpoints. Original material bytes, UVs, triangle winding, and per-world-cell PATH bytes remain unchanged. A moved model vertex is encoded by exactly one float32 translation from its old cell anchor to its new host anchor; the audit checks that exact encoding, rather than accepting an arbitrary geometric tolerance. The [reviewed saved-model contract](checks/straight-partition-models.jsonc) binds the resulting canonical models.

The straight stamp keeps 19 native highway cells and two Avenue-only crossing cells. Six former wing cells move to the corresponding full ramp owners. Native highway pavement and barriers, inside-envelope slip-lane paint, and six centre piers stay in the stamp. All curved ramp slabs, 1 m undersides, barriers, and inset joining bridges move into separately placed ramp models, including their intentional drawing above stamp-owned cells. The two pure Avenue cells retain pristine native pavement, without the obsolete compact apron.

Use the current [saved R40 assembly report](evidence/saved-assembly-check.json) and [saved compact-alternative report](evidence/saved-compact-alternative-check.json) for the selected build's construction, directed graph, physical support, and model checks. Bind both to the same saved manifest used by the pictures and cards. The complete graphs retain 20 external native channels, ten native through-lane and pedestrian journeys, eight required arm movements, and exclusion of all four cross-Avenue ramp movements; the ownership split preserves their routes. Individual component graphs differ because the lower full ramps cross a stamp-owned middle tile.

Two otherwise unowned R40 cells, displayed as (X4, Y3) and (X6, Y5), retain specific native highway overhang. The compact alternative owns them through its full ramps. Separately, the full ramp models deliberately project into highway-owned cells. These are explicit, source-bound exceptions; a drawing outside ownership is not permission to place another network on the same construction tile. The complete assembled model union must support every route across the ownership cuts.

The focused source checks passed: ten ramp-family tests and two straight-partition tests, with no skips. Run them from the repository root:

```sh
python3 -B -m unittest discover -s custom-pieces/domains/highway/tests -p test_modular_ramp_geometry.py -v
python3 -B -m unittest discover -s custom-pieces/domains/highway/tests -p test_straight_stamp_geometry.py -v
```

The first set checks both ownership families, unchanged high samples, encoded tile seams, grades below 30%, the new R40 circles, flat cardinal ground joins, same-side Avenue access, texture phase, and separately measured inherited transition kinks. The second verifies that a shared concrete mesh keeps its centre pier while moving a curved bridge, preserves selected XYZ/UV/material bytes and winding, and rejects paint outside the straight native envelope.

Run the complete framework, domain, and assembly suite, and report actual skips separately:

```sh
python3 -B tools/run_tests.py
```

After preparing the pinned native inputs through the shared workflow, build and verify the normal selected set:

```sh
python3 -B custom-pieces/scp.py build --set ddrhw-modular-ramp-kit --output custom-pieces/dist/ddrhw-modular-ramp-kit
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/ddrhw-modular-ramp-kit
```

The [atomization PNG](previews/modular-atomization.png), [editable SVG](previews/modular-atomization.svg), and [measurement evidence](evidence/modular-atomization.json) distinguish actual physical mouths from city-tile traffic cuts. The plan uses actual indexed pavement, barriers, supports, and saved route directions. Its four profiles stitch complete saved ramp journeys through the necessary stamp-owned intervals; they do not insert straight chords between disconnected owned fragments. Horizontal and vertical profile scales are explicitly separate.

The six canonical assembly views follow the trumpet order. The construction picture uses the real top-view model, a translucent ownership layer, thick dark ownership boundaries, and thin component-coloured actual-model silhouettes. The icon's provenance is in [evidence/icon.json](evidence/icon.json). Stage model pictures with:

```sh
python3 -B custom-pieces/domains/highway/tools/render_compact_assembly.py --assembly ddrhw-l1-and-l2-diagonal-avenue-modular-diamond --build custom-pieces/dist/ddrhw-modular-ramp-kit --output-dir custom-pieces/local/modular-diamond-render --prefix reviewed-modular-diamond
```

Inspect and promote the six staged pictures using the [shared documentation workflow](../../../../docs/WORKFLOW_DOCUMENTATION_GENERATION.md#81-promote-the-staged-assembly-pictures). Rendering cannot approve a manual preview or game case. Keep native MIS joins, arbitrary height offsets, and draggable/FLEX overrides outside this fixed static kit's claims.

## 4. Game checks

1. Open **Transportation → Highways**, find **SCP | ASSEMBLY | DD RHW-4 — Modular Diagonal Avenue Diamond**, and cycle all seven default types with **Tab**, then backward with **Shift+Tab**. Check the six compact-alternative buttons separately.
2. Place P01 once. Both decks must be completely straight, with inside-highway slip lanes and barrier cutouts. No curved ramp slab, underside, or barrier may appear before an attachment is placed. Confirm that the ground Avenue appears under the crossing.
3. Place P02–P07 one at a time. Each click must add only its full ramp or terminal. Inspect the four flat native-edge physical mouths from both oblique views and above: pavement, underside, Jersey profiles, and bridge strips must fit without cracks or duplicate faces. Inspect the separate traffic tile boundaries, flat R40 terminal joins, and outside Avenue joins too.
4. Use Route Query and a separate observed car journey for every required direction. Each lower ramp must carry traffic through both owned fragments and the intervening stamp-owned tile. Confirm that no ramp car crosses the opposing Avenue carriageway. Check both pedestrian directions with suitable demand.
5. Compare each rotated construction preview with the placed result. The supported resource rotations are four proper turns; record a human result only for the actual orientation inspected. Highway decks, Avenue, ramp bodies, pavement props, and shadows must rotate together.
6. Connect ordinary Avenue approaches, develop nearby zoning, and allow the Avenue to redraw. Inspect sidewalk artwork separately from pedestrian travel. Different density, wealth, sidewalk replacements, and save/reload appearances require their own observations.
7. Inspect shadows, save the city, close it, and reload it. In the disposable city, remove one full ramp, confirm that the straight stamp remains, and replace the ramp at the same reference. Whole-piece demolition and single-tile removal are distinct; use the [connected-survivor procedure](../../../../docs/TESTING.md#2-investigate-single-tile-demolition-and-connected-survivors) for partial-removal investigation.

Record the exact case, direction, pose, layout, and environment using the [shared recording procedure](../../../../docs/TESTING.md#4-record-one-observation):

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/checks/manual-tests.json --observation custom-pieces/domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/checks/observation.json
```

## 5. Results and known issues

The independent source-partition audit passed. Saved-resource reports, renderer provenance, and human observations retain their separate scopes; no game result is inherited from the earlier adaptive sidewalk probe, compact assembly, or rejected 27-cell stamp. The corrected layout remains experimental until explicit matching observations establish placement, native outside-network joining, visible traffic, adaptive pavement, demolition, and save/reload.

R40 applies only to newly authored circular sections. The complete retained high-prefix traffic centre-lines contain sampled minimum radii of approximately 1.735 m for the lower routes and 3.500 m for the upper routes. The retained upper graded collar also includes approximately R29.50. These unchanged local transitions are limitations of the inherited route, not newly authored R40 geometry. The new lower grade reaches approximately 25.43%, and the upper route retains approximately 29.61%, within the experimental 30% bound.

Only the two complete documented families are supplied: R40 ramps with R40 terminals, or full compact ramps with their compact Avenue junctions. Arbitrary curves, freely selected slopes and heights, native MIS extensions, and native FLEX/draggable construction are not established. Four lower-ramp traffic ports must stay distinct even though their visible roadway is continuous. Keep every observed defect tied to its exact saved build and layout below.

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

The modular experiment branched from source `06d3d430d515df230f20802872b14eb836f31a69` onto `codex/ddrhw-modular-ramp-kit`; `codex/double-decker-diagonal-highway` retains the previous development. The user chose the existing HSR-style slope and angle cards as the interface reference. A first 27-cell prototype incorrectly kept curved high throats inside the highway stamp.

The corrected partition keeps the highway completely straight and moves every curved high-throat face into separately placed full ramps. Six construction wing cells change owner, while ramp faces can also draw above retained highway-owned tiles. The complete assembled source union remains preserved. New full compact variants combine each old compact grade with its transferred high throat; the original 13 compact subjects and their resources remain untouched.

The R40 continuations retain their accepted high samples, then use straight, circular, and straight sections to reach flat ground ends. Separate R40 terminals complete 45° turns into the adjacent Avenue carriageways. A texture-station correction preserves wheel-track alignment at the retained joins, and each R40 grade has a narrow support seated on its real sloped underside.

The [network proposal](../../NETWORK_SPEC.md#10-proposed-modular-ramp-standards) records the wider angle, radius, and grade families, along with NAM, HSR, and Japanese expressway inspiration. This kit implements a bounded subset. The retained [compact assembly history](../ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#6-design-history) preserves the earlier pavement, barrier, marking, sidewalk, and rotation findings with their original scope.
