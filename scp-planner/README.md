---
title: "SCP Planner"
summary: "Discover complete-boundary candidates from fresh library exports, run the separate two-piece placement trial, and understand Planner's input and evidence limits."
audience: "Planner users and developers"
document_type: "guide"
---

# SCP Planner

SCP Planner is the planned browser application for arranging reusable pieces and finding compatible connections. Its current Python tools provide compatibility discovery and a separate two-piece placement trial; the full browser interface is unfinished. A **piece type** is one reusable construction definition, and an **instance** is one placed copy of that type.

## Inputs and ownership

The piece library owns authored declarations, measured game paths, source validation, generated `connector-data.json`, and canonical connection cards. Planner reads those exports through its adapter and owns placement matching, application tests, and private reports. Read the library's [connector reference](../custom-pieces/docs/CONNECTOR_METADATA.md) for the data definitions and [documentation-generation workflow](../custom-pieces/docs/WORKFLOW_DOCUMENTATION_GENERATION.md) when an export is missing or stale.

`pilot.json` selects the library directory, transport domain, two piece IDs, saved compiled build, and trial configuration. The adapter imports shared Python code from that configured source, unless `SCP_CUSTOM_PIECES_ROOT` overrides the code-import root. The trial’s data root comes from `--custom-pieces-root` or `pilot.json`, rather than that environment variable. Keep both selections on the same checkout: update `pilot.json` for both, or set the environment variable and pass `--custom-pieces-root` with the same directory. Keep type definitions and their source geometry separate from instance IDs, anchor positions, and rotations.

The placement pilot selects the HSR modular crossing and tight height-changing curve. HSR means High Speed Rail. Compatibility discovery instead enumerates the selected domain's registered pieces and searches its complete eligible export set. A type becomes eligible only when it has authored `connector-groups.jsonc` and a fresh, validated `connector-data.json` accepted by the library's `load_exports` API. Planner does not obtain compatibility from legacy per-port shortlists, invent missing declarations, or substitute generated data for authored metadata.

## Discover compatible pieces

A **complete boundary** is one exposed tile edge together with every required service, channel, and direction crossing it. For example, an edge containing elevated HSR, Road car lanes, and sidewalks requires all three groups to agree under the same placement. A matching HSR group cannot hide a missing Road group.

1. Prepare or refresh the intended library exports through the library's [documentation-generation workflow](../custom-pieces/docs/WORKFLOW_DOCUMENTATION_GENERATION.md#before-refreshing). Discovery reads those exports; it does not build a piece, extract game resources, refresh a stale export, or modify library files.
2. Open a terminal. On macOS, press **Command + Space**, type **Terminal**, and press **Return**. A **checkout** is your local copy of the repository, and its **root** is the folder containing both `custom-pieces/` and `scp-planner/`. Replace `/path/to/sc4-simons-custom-pieces` below with your checkout's full path, keep the quotation marks so spaces work, and press **Return** to select the Planner directory:

```sh
cd '/path/to/sc4-simons-custom-pieces/scp-planner'
```

3. Search every eligible piece in the registered high-speed rail domain:

```sh
python3 tools/discover_compatibility.py --domain high-speed-rail
```

The command writes `local/compatibility/report.json` and prints the registered, eligible, not-migrated, excluded, and candidate counts. It searches every eligible type pair once, including two instances of the same type. There is no three-candidate limit or other result cap. Each result fixes the first instance at its authored 0° orientation and gives the second instance's relative anchor position and counterclockwise rotation. Several service-group matches at the same boundary pair and pose become one result retaining every `bundle_group_pairs` and `member_pairs` mapping.

4. To search from one piece's north boundary while still considering every eligible counterpart, run:

```sh
python3 tools/discover_compatibility.py --domain high-speed-rail --piece hsr-component-modular-crossing-core --boundary cell-0-0-north --report local/compatibility/crossing-north.json
```

`--piece` is an exact registered type ID. `--boundary` is its complete boundary-bundle ID, such as `cell-0-0-north`; it is not a service-group ID such as `upper-end-b`. Omit `--boundary` to search every boundary of the selected piece. A boundary selection requires a piece selection. Unknown domain, piece, and boundary IDs produce an explicit error.

5. Open the saved JSON report and inspect `piece_eligibility` before interpreting `candidate_placements`:

| Report state or reason | Meaning |
| --- | --- |
| `eligible` | The library accepted the declarations and fresh generated export; the type was searched. |
| `not_migrated` | No authored connector declaration exists. The type's compatibility remains unknown and was not searched. |
| `excluded` / `missing_export` | Declarations exist, but the generated export is missing. |
| `excluded` / `stale_source` or `stale_export` | The library rejected an outdated authored binding, export, or bound input. |
| `excluded` / `invalid_export` | The library rejected the export or its source metadata as invalid. |
| `excluded` / `missing_source` | A source required by the library's validation is unavailable. |
| `excluded` / `validation_failed` | A failure had no structured library reason code; its exact detail is preserved without guessing a category. |

Missing migration, missing inputs, and invalid inputs are coverage states, not an incompatibility verdict. An empty candidate list means that this search found no candidate among its eligible inputs and selected boundaries. A selected piece that is not eligible receives `query.status: "not_eligible"` and no search results. Follow the library's workflow to resolve exclusions; Planner never falls back to old per-port lists or authored-sidecar-only matching.

The discovery API is `scp_planner.discover_compatibility(custom_root, domain_id='high-speed-rail', query_piece_id=None, query_boundary_id=None)`. It returns the same report dictionary without writing files. Only the CLI writes a report, and `--report` must remain under `scp-planner/local/`.

### Select the same code and data checkout

Discovery defaults its data root to the configured library code root. An explicit `--custom-pieces-root` must match that code root. Run the following command from the `scp-planner/` directory selected above; `../custom-pieces` means the sibling library directory in the same checkout. Change both occurrences of that path together when selecting another checkout:

```sh
SCP_CUSTOM_PIECES_ROOT='../custom-pieces' python3 tools/discover_compatibility.py --custom-pieces-root '../custom-pieces' --domain high-speed-rail --piece hsr-component-modular-crossing-core --boundary cell-0-0-north --report local/compatibility/crossing-north.json
```

`SCP_CUSTOM_PIECES_ROOT` selects the Python library implementation for that command, and `--custom-pieces-root` selects its data. A mismatch is rejected before discovery. This changes neither `pilot.json` nor the global Python installation. To test just discovery's synthetic consumer cases, run `python3 -B -m unittest discover -s tests -p test_discovery.py -v` from the Planner directory.

Discovery establishes **pairwise complete-boundary metadata and disjoint owned-cell candidates**. It does not establish full-scene fit, agreement at other touching boundaries, mesh seams or collisions, support clearance, terrain construction, or game operation. Those checks remain explicitly `unverified` in every report. A candidate is not a verified construction or a human observation.

## Run the trial

1. Follow the library's [refresh and check procedure](../custom-pieces/docs/WORKFLOW_DOCUMENTATION_GENERATION.md#refresh-and-check-the-two-migrated-pieces) first. It uses existing verified game resources and prepares current exports. Use Python 3.11 or newer with the [project dependencies](../custom-pieces/docs/BUILD_AND_INSTALL.md#build-a-selected-collection).
2. Open a terminal. On macOS, press **Command + Space**, type **Terminal**, and press **Return**.
3. Replace `/path/to/sc4-simons-custom-pieces` below with your checkout's full path, keep the quotation marks, and press **Return**. The checkout root is the folder containing both `custom-pieces/` and `scp-planner/`; this command selects its Planner directory.

```sh
cd '/path/to/sc4-simons-custom-pieces/scp-planner'
```

4. Run the placement trial:

```sh
python3 tools/run_metadata_pilot.py
```

The command reads fresh exports, delegates compiled-resource verification to the source library, checks the two expected placements, and writes `local/pilot/report.json`. That report describes an application trial; it does not change a piece definition, install a plugin, or record a game observation. A missing or stale source is a failure to resolve through the library procedure.

5. Run the application tests:

```sh
python3 -B -m unittest discover -s tests -v
```

## Expected placements

The crossing's anchor remains at `[0,0]` metres. The curve joins its upper route at either of these relative poses:

| Crossing connection | Curve connection | Curve anchor [east, north], metres | Counterclockwise rotation |
| --- | --- | --- | --- |
| `upper-end-b` | `curve-end-a` | `[0,64]` | 0° |
| `upper-end-a` | `curve-end-a` | `[0,-64]` | 180° |

The curve's **Custom (23 m)** end joins neither crossing height directly. The library's [worked placement example](../custom-pieces/docs/CONNECTOR_METADATA.md#84-placing-these-two-pieces-together) explains the coordinates and height comparison. These direct-pair trials are separate from the saved V4 trumpet, whose placements retain five intervening upper straight pieces.

## Placement rules and limits

Apply each instance's permitted rotation and anchor translation to all its paths, boundaries, owned tiles, and model surfaces together. An endpoint cannot slide independently to make a join. Follow the library's [coordinate definitions](../custom-pieces/docs/CONNECTOR_METADATA.md#3-positions-headings-heights-and-slopes-use-one-comparison-frame): outward headings use clockwise angles, while instance rotations use counterclockwise angles.

The current matcher tests proper quarter-turn rotations on the 16 m tile lattice. It compares complete exposed tile-edge segments, physical-channel and cut correspondences, measured geometry, service classifications, and normalized per-mode permissions under one pose. The pair's owned cells must be disjoint. Profile names, presentation-group partitions, or a shared corner alone cannot establish a connection. Internal journeys remain source-defined; an external join creates neither a new turn nor a transfer between the crossing's heights.

The actual compiled examples are paired HSR with flat orthogonal ends. Artificial mixed-network, shifted-position, and shared-mode cases test comparison rules without supplying verified game resources for those source families. Pairwise candidates do not establish full-scene fit, physical seams, support or overhang clearance, terrain-aware construction, or observed game traffic. Free vertical relocation and reflection are unsupported. Keep those evidence states separate and unperformed checks unverified; record explicit human observations through the library's [testing procedure](../custom-pieces/docs/TESTING.md).

Canonical connection artwork belongs beside each library piece. The compatibility launcher `tools/render_metadata_pilot.py` delegates to that library renderer. Application reports and working renders belong under `local/`.
