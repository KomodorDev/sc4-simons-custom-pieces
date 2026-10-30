---
title: "Highway network specification"
summary: "Record measured native DD RHW-4 donors, distinguish provisional design geometry, and identify the missing game implementation."
audience: "Highway authors and reviewers"
document_type: "reference"
---

# Highway network specification

<!-- BEGIN DOCUMENT NAVIGATION -->
[1. Implementation status](#1-implementation-status) · [2. Measured native inputs](#2-measured-native-inputs) · [3. Prototype geometry](#3-prototype-geometry) · [4. Requirements before registration](#4-requirements-before-registration)
<!-- END DOCUMENT NAVIGATION -->

## 1. Implementation status

This domain has a reproducible [diagonal diamond geometry prototype](01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/README.md), but no registered highway game pieces, build adapter, or independently verified highway DAT output. A **DAT** is a SimCity 4 resource archive. A **PATH** resource stores directed traffic paths, while an **S3D** resource stores a visible model. The prototype tools create sampled road geometry and schematic pictures; they do not create either game resource.

The domain registry deliberately retains `implementation: null`, empty piece and assembly lists, and zero game menu types. This design uses `design.jsonc` as a supported input to its own prototype tools. It is not an `assembly.json` registration, an ID reservation, or a source of connector exports. The existing HSR implementation must not be used as a highway implementation.

## 2. Measured native inputs

The initial audit reads the user's installed NAM resources and original game archive without copying their binary payloads into the repository. The portable [native audit](01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/evidence/native-audit.json) records archive fingerprints, resource identities, path samples, and coverage limits. These facts describe the audited bytes, rather than all NAM versions or an in-game observation.

| Native input | Measured fact | Scope limit |
| --- | --- | --- |
| `RealHighway_DD_RHW-4.dat` | The audited archive contains stacked diagonal car paths at 7.5 m and 15 m. | These are PATH heights; they are not measured deck underside heights or available vehicle clearance. |
| Diagonal DD RHW-4 PATH `296678F7-A966883F-57530200` | Four real car routes represent two lanes on each opposing deck; the resource also includes two explicitly labelled invalid capacity routes. | Exclude the invalid capacity paths from actual journey claims. |
| Diagonal crossing PATH pair `5753A300` and `5753A305`, under type/group `296678F7-A966883F` | Native diagonal DD RHW-4 over diagonal avenue content exists. | These are draggable-network resources; no direct RUL0 construction family was found for this crossing. A new selectable construction cannot be obtained merely by renaming its resource IDs. |
| Reverse-flow crossing pair `5753A380` and `5753A385` | The native data also provides the opposite choice of upper/lower travel direction. | Native placement and complete joining boundaries still require independent checks. |
| `SimCity_1.dat`, PATH `296678F7-69668828-04000200` | A diagonal avenue half has two car routes and a pedestrian route at ground height 0 m. | One half does not establish the complete two-tile avenue boundary or its rotated construction. |

The prototype chooses the upper deck towards northeast and the lower deck towards southwest. In the native `57530200` orientation, the upper paths instead run from east to south and the lower paths reverse them; an eventual implementation must choose and transform the matching native variant deliberately. Do not copy its route coordinates into the prototype without applying the documented orientation and complete paired-cell transforms.

**Right-hand traffic** means vehicles use the right side relative to their own travel direction. The prototype therefore puts upper-deck ramps southeast of the highway and lower-deck ramps northwest of it. No left-hand-traffic compatibility has been established.

## 3. Prototype geometry

The maintained source is [design.jsonc](01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/design.jsonc). Its `geometry` object contains all provisional dimensions. Highway deck heights of 7.5 m and 15 m are native-derived; a 12 m deck width, a 24 m avenue width, and a 6 m ramp width are design assumptions. At the user's request, the compact prototype replaces the former 8% grade assumption with a 40% experimental bound, uses 48 m lower ramps, and keeps the higher ramps longer at 80 m. These dimensions and the grade bound must not be presented as measured NAM profiles or engineering standards. The avenue and highway run on perpendicular diagonal axes, at 45° to the city grid.

A **grade** is height change divided by horizontal travel distance; 30% means a rise of 30 m over a horizontal distance of 100 m. The prototype keeps an upper ramp at full deck height until its entire provisional roadway width has moved outside the lower-deck envelope, then follows a steep height transition. This avoids the obvious error of descending through the lower highway. Peak sampled grades are approximately 35.96% for upper ramps and 32.50% for lower ramps; they exceed the whole-ramp averages because the joining sections are flat. Sampled centre-line checks do not establish clearance for full vehicle bodies, barriers, supports, or native S3D geometry.

The four ramps meet the avenue at two surface intersections. Each has two avenue legs, one incoming off-ramp leg, and one outgoing on-ramp leg. These are four-arm intersections, rather than T junctions. Both avenue directions can reach either highway direction; both highway directions can leave towards either avenue direction. Ground intersections introduce intentional conflict points and need a future traffic-control design.

The [geometry generator](tools/diagonal_diamond_geometry.py), [independent prototype verifier](tools/verify_diagonal_diamond.py), and [schematic renderer](tools/render_diagonal_diamond.py) own these experimental calculations. Their output is not a native connection contract, a compiled-model preview, or a saved-resource verification report. Supports and final smallest-module cuts remain unresolved.

## 4. Requirements before registration

Follow the [shared assembly workflow](../../docs/WORKFLOW_ASSEMBLY_CREATION.md) and [piece workflow](../../docs/WORKFLOW_PIECE_CREATION.md) when advancing this prototype. Measure complete native boundaries, author traffic and visible geometry, prove cuts and unique construction-tile ownership, and implement a highway provider with independent saved-resource checks. Introduce JSONC support in the affected piece and assembly readers and writers before registering new maintained definitions; retain existing subjects' source formats until deliberately migrated.

Only then allocate identifiers, compile resources, check all four proper rotations, verify the entire arrangement, render the actual saved models, and package the one-button component cycle. Building, installing, publishing, and human game observations remain separate stages. No route, placement, or game test becomes passed from a schematic or numerical prototype check.
