---
title: "Highway network specification"
summary: "Record the DD RHW-4 provider, measured native donors, compact module geometry, and verification limits."
audience: "Highway authors and reviewers"
document_type: "reference"
---

# Highway network specification

<!-- BEGIN DOCUMENT NAVIGATION -->
[1. Implementation status](#1-implementation-status) · [2. Measured native inputs](#2-measured-native-inputs) · [3. Prototype geometry](#3-prototype-geometry) · [4. Compiled geometry and verification](#4-compiled-geometry-and-verification)
<!-- END DOCUMENT NAVIGATION -->

## 1. Implementation status

The registered `scp_highway` provider builds a standalone native diagonal DD RHW-4/Avenue crossing and the thirteen reusable types for the [compact diagonal diamond](01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/README.md). A **DAT** is a SimCity 4 resource archive. A **PATH** resource stores directed traffic routes, and an **S3D** resource stores an indexed visible model. Car transport is engine class 1, and pedestrian transport is class 2. Heights are metres above the pavement datum at ground 0 m; no HSR 0.5 m datum is imported.

Implementation entry points are `implementation/scp_highway/native.py` for measured native channel composition, `recipes.py` for resource packaging and explicit construction, `ramp_geometry.py` for authored surfaces and native barrier openings, `ramp_paths.py` for exact tile cuts and the coordinated module partition, `verify.py` for the independent native crossing contract, `ramp_verify.py` for saved pavement and corridor checks, `connections.py` for shared intrinsic extraction, and `menu.py` for the Roads-menu donor. The domain registry explicitly selects this provider. New maintained subjects use JSONC definitions; generated machine evidence remains strict JSON.

The earlier `design.jsonc` remains a reproducible schematic source with its original reports. The actual game modules use measured native lane boundaries and grid-snapped geometry. A schematic test or an actual-resource test cannot establish a human game pass.

## 2. Measured native inputs

The initial audit reads the user's installed NAM resources and original game archive without copying their binary payloads into the repository. The portable [native audit](01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/evidence/native-audit.json) records archive fingerprints, resource identities, path samples, and coverage limits. These facts describe the audited bytes, rather than all NAM versions or an in-game observation.

| Native input | Measured fact | Scope limit |
| --- | --- | --- |
| `RealHighway_DD_RHW-4.dat` | The audited archive contains stacked diagonal car paths at 7.5 m and 15 m. | These are PATH heights; they are not measured deck underside heights or available vehicle clearance. |
| Diagonal DD RHW-4 PATH `296678F7-A966883F-57530200` | Four real car routes represent two lanes on each opposing deck; the resource also includes two explicitly labelled invalid capacity routes. | Exclude the invalid capacity paths from actual journey claims. |
| Diagonal crossing PATH pair `5753A300` and `5753A305`, under type/group `296678F7-A966883F` | Native diagonal DD RHW-4 over diagonal avenue content exists. | These are draggable-network resources; no direct RUL0 construction family was found for this crossing. A new selectable construction cannot be obtained merely by renaming its resource IDs. |
| Reverse-flow crossing pair `5753A380` and `5753A385` | The native data also provides the opposite choice of upper/lower travel direction. | Native placement and complete joining boundaries still require independent checks. |
| `SimCity_1.dat`, PATH `296678F7-69668828-04000200` | A diagonal avenue half has two car routes and a pedestrian route at ground height 0 m. | One half does not establish the complete two-tile avenue boundary or its rotated construction. |

The compiled experiment chooses the upper deck towards northeast and the lower deck towards southwest. In the native `57530200` orientation, the upper paths instead run from east to south and the lower paths reverse them; an eventual implementation must choose and transform the matching native variant deliberately. Do not copy its route coordinates into the prototype without applying the documented orientation and complete paired-cell transforms.

**Right-hand traffic** means vehicles use the right side relative to their own travel direction. The prototype therefore puts upper-deck ramps southeast of the highway and lower-deck ramps northwest of it. No left-hand-traffic compatibility has been established.

## 3. Prototype geometry

The maintained source is [design.jsonc](01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/design.jsonc). Its `geometry` object contains all provisional dimensions. Highway deck heights of 7.5 m and 15 m are native-derived; a 12 m deck width, a 24 m avenue width, and a 6 m ramp width are design assumptions. At the user's request, the compact prototype replaces the former 8% grade assumption with a 40% experimental bound, uses 48 m lower ramps, and keeps the higher ramps longer at 80 m. These dimensions and the grade bound must not be presented as measured NAM profiles or engineering standards. The avenue and highway run on perpendicular diagonal axes, at 45° to the city grid.

A **grade** is height change divided by horizontal travel distance; 30% means a rise of 30 m over a horizontal distance of 100 m. The prototype keeps an upper ramp at full deck height until its entire provisional roadway width has moved outside the lower-deck envelope, then follows a steep height transition. This avoids the obvious error of descending through the lower highway. Peak sampled grades are approximately 35.96% for upper ramps and 32.50% for lower ramps; they exceed the whole-ramp averages because the joining sections are flat. Sampled centre-line checks do not establish clearance for full vehicle bodies, barriers, supports, or native S3D geometry.

The four ramps meet the avenue at two surface intersections. Each has two avenue legs, one incoming off-ramp leg, and one outgoing on-ramp leg. These are four-arm intersections, rather than T junctions. Both avenue directions can reach either highway direction; both highway directions can leave towards either avenue direction. Ground intersections introduce intentional conflict points and need a future traffic-control design.

The [geometry generator](tools/diagonal_diamond_geometry.py), [independent prototype verifier](tools/verify_diagonal_diamond.py), and [schematic renderer](tools/render_diagonal_diamond.py) own these experimental calculations. Their output is not a native connection contract, a compiled-model preview, or a saved-resource verification report. These source-only checks do not establish support geometry or final module cuts; the compiled partition is recorded separately below.

<a id="4-requirements-before-registration"></a>

## 4. Compiled geometry and verification

The current compact partition owns 41 construction tiles inside an 8 × 8-tile bounding rectangle. Thirteen reusable types supply seventeen placements: a coordinated access core, two surface junctions, four highway branch modules, four graded modules, and two complementary native continuation halves. Continuation A is used four times, and continuation B is used twice; two byte-identical native cells were removed from the upper branch modules and reused through continuation A. Shared native and authored services on one city tile have a single owner. Normal builds preserve all selected types; assembly-menu creates one Roads button with Tab/Shift+Tab cycling in a separate build.

Measured native deck width is 16 m, pavement heights are 7.5 m and 15 m, native vertical edge skirts extend approximately 1 m below the pavement, and native barriers rise approximately 1.390625 m above their deck. Some native model faces extend approximately 1.657 m beyond a construction tile; construction ownership and the complete physical envelope are separate measurements. The compact candidate’s native faces touch six additional visual-only corner cells, giving 47 projected cells and an approximately 131.314 × 131.314 m physical envelope. These are retained native overhangs, rather than extra construction placements. Frozen original triangle/material fingerprints, or strictly contained fragments on those original faces, bound the overhang exception; authored ramp faces receive no equivalent exception. Authored ramp surfaces are 6 m wide and are clipped at actual city-tile boundaries. Empty PATH resources are valid only in independently declared model-only shoulder cells; an actual native empty-PATH measurement is retained in the core audit.

The snapped complete lower curve is approximately 50.0395 m: 21.8812 m of level highway joining curve, 24.1583 m of active height transition, and 4 m of level ground landing. The upper curve is approximately 80.4662 m: 35.6331 m level, 40.8331 m graded, and 4 m level. Whole-curve length therefore differs from the short active slope. The authoring bound is 40%; saved PATH grades, rather than source labels, establish the actual candidate’s maximum.

The independent saved-resource verifier reads actual indexed triangles and every encoded car segment. It checks continuous pavement coverage, permitted grade, exact model-only cells, authored atlas pixels, and triangle-face intersections with a 2.5 m-wide, 3.8 m-high graded corridor in all four proper rotations. This is not full solid containment, a complete swept vehicle-body calculation, a structural proof, a native neighbour compatibility catalogue, or a game observation. The native crossing additionally pins its independently composed model and route measurements. Assembly route reachability must be checked at the registered saved poses.

The native donors have no horizontal underside face under the tile centre. The compiled assembly adds six 0.8 m-square concrete column surfaces at the reused continuation tile centres, running from ground 0 m through the lower pavement at 7.5 m to the upper pavement at 15 m; no top cap is placed coplanar with the road. Their saved-face corridor and visual contact checks are separate from structural engineering.

Junction control and game traffic behaviour, steep-grade vehicle animation, terrain behaviour, shadows, placement, demolition, and save/reload require their respective evidence. Human observations stay unverified until explicitly confirmed. Building, installing, publishing, and merging are separate actions; only the human maintainer merges a pull request.
