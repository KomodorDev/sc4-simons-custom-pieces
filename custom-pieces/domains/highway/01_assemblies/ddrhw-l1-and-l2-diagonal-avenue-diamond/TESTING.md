---
title: "Testing — Compact Diagonal Avenue Diamond"
summary: "Reproduce the prototype geometry checks, inspect native donor evidence, and identify unfinished game implementation and observations."
audience: "Highway authors and reviewers"
document_type: "testing-guide"
---

# Testing — Compact Diagonal Avenue Diamond

[1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

The subject is the unregistered [design.jsonc](design.jsonc) prototype. Its current outputs are seven provisional road surfaces, 26 directed curve segments, twelve journeys between distinct external arms, four height-changing slip lanes, two surface intersections, and four schematic images. The [README connection matrix](README.md#4-connection-matrix) lists each journey separately. The native audit measures existing game inputs; it does not measure a compiled implementation of this new layout.

The independent checker reads saved sampled points without calling the geometry generator. Its coverage is finite coordinates, declared road axes and deck heights, exact internal endpoint connections, reachability between distinct arms, right-side ramps, monotonic height changes, sampled grades, and lateral separation from a provisional mainline envelope before changing height. It does not check complete swept road or vehicle solids, supports, deck thickness, native lane interfaces, encoded PATHs, construction rules, runtime tile addresses, model packing, or shadows.

## 2. Test setup

Run the following commands in a terminal whose current directory is the repository root, meaning the folder containing `custom-pieces/` and the outer README. Prepare Python and dependencies using the [repository setup instructions](../../../../../README.md#2-prepare-python-and-run-the-tests). Geometry generation and verification use Python's standard library and the library's JSONC parser. Rendering additionally requires Pillow and NumPy, which the repository test requirements already include.

The prototype requires flat ground, right-hand traffic, a southwest–northeast double-decker highway, and a northwest–southeast avenue. The upper direction is SW → NE at 15 m; the lower direction is NE → SW at 7.5 m. Widths and the maximum grade are explicit design assumptions in `design.jsonc`, rather than measured native standards. No Plugins directory or game installation is required for the geometric prototype commands below.

## 3. Software checks

First, generate the saved curve coordinates. This reads the maintained source and writes a strict-JSON machine export; it does not build a game DAT:

```sh
python3 -B custom-pieces/domains/highway/tools/diagonal_diamond_geometry.py --design custom-pieces/domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/design.jsonc --output custom-pieces/domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/evidence/geometry.json
```

Second, independently inspect those saved points. The checker rejects a geometry export whose source fingerprint differs from the current design. A **fingerprint** is a hash identifying exact file bytes:

```sh
python3 -B custom-pieces/domains/highway/tools/verify_diagonal_diamond.py --design custom-pieces/domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/design.jsonc --geometry custom-pieces/domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/evidence/geometry.json --output custom-pieces/domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/evidence/geometry-check.json
```

Third, regenerate the top view, opposite angled views, and separate ramp profiles. The renderer samples the same design, projects its actual three-dimensional points, and writes source and image fingerprints to [render.json](evidence/render.json). The profile diagram labels its vertical exaggeration explicitly:

```sh
python3 -B custom-pieces/domains/highway/tools/render_diagonal_diamond.py --design custom-pieces/domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/design.jsonc --output-dir custom-pieces/domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/previews
```

Fourth, run the highway regression tests. They include deliberately damaged saved points, missing turns, disconnected endpoints, incorrect compilation claims, and road/path shape disagreement, so a label or optimistic generator summary cannot substitute for the measured checks:

```sh
python3 -B -m unittest discover -s custom-pieces/domains/highway/tests -v
```

Finally, check library documentation and run the repository's complete framework, domain, and assembly suites:

```sh
python3 -B custom-pieces/scp.py docs-check
python3 -B tools/run_tests.py
```

The documentation command checks registered subjects and maintained shared documents. This prototype is deliberately unregistered, so its source and route checks are supplied by the dedicated tools and highway tests above; a green documentation result does not establish prototype completion or native compatibility.

To repeat the native-donor audit, supply your own existing Plugins directory and original `SimCity_1.dat`. Replace both example placeholders, keeping the quotes around paths containing spaces. The tool checks exact supported archive fingerprints and refuses missing or changed donors. It stores archive basenames, resource identities, and measured data, rather than private paths or imported binary resources:

```sh
python3 -B custom-pieces/domains/highway/tools/audit_diagonal_diamond_native.py --plugins '/path/to/Plugins' --game-dat '/path/to/SimCity_1.dat' --output custom-pieces/domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/evidence/native-audit.json
```

## 4. Game checks

No game checks have run. There is no compiled or installed candidate, no allocated construction, no menu cycle, and no human observation record for this prototype. The existing native donor resources do not supply those missing stages.

After implementing and independently verifying the game components, declare exact test cases under the [shared testing procedure](../../../../docs/TESTING.md). Separately observe placement in every required orientation, all twelve directed journeys with real traffic demand, Route Query, visible travel, forbidden direct transfers, avenue pedestrians, surface-intersection conflicts, shadows, demolition, save/reload, and the specified flat-terrain behaviour. Only matching human confirmation can change those observations.

## 5. Results and known issues

The authoritative prototype result is [geometry-check.json](evidence/geometry-check.json), tied to the current source and sampled-geometry fingerprints. The [native audit](evidence/native-audit.json) separately establishes PATH heights of 7.5 m and 15 m, four genuine diagonal car routes across the decks, existing diagonal avenue-crossing resources, and the scope of an 80-resource native ramp scan. Native invalid capacity routes are excluded from genuine journey counts. The audited native ramps remain at fixed heights; they are not a complete descent to the avenue.

| Current geometric measurement | Result | Meaning |
| --- | --- | --- |
| Highway length | Approximately 174.24 m | Two 87.1183 m half-lengths; not a construction footprint or occupied-tile count. |
| Slip-lane corridor width | At most 62 m | Ramp centres stay within 28 m of the highway axis; each provisional ramp surface is 6 m wide. This excludes the extending avenue arms. |
| Surface-intersection positions | `u=0, v=−28 m` and `u=0, v=+28 m` | Close avenue junctions on opposite sides of the viaduct. |
| Lower ramp horizontal curve length | 48 m, or three tile lengths | Includes the flat joining sections and is measured along the entire curved plan. |
| Upper ramp horizontal curve length | 80 m, or five tile lengths | Extra length accommodates the 15 m deck; it includes the flat joins. |
| Upper slip-lane maximum sampled grade | Approximately 35.960% | Separate 15 m → 0 m and 0 m → 15 m transitions. |
| Lower slip-lane maximum sampled grade | Approximately 32.497% | Separate 7.5 m → 0 m and 0 m → 7.5 m transitions. |
| Ground landing | 4 m per ramp | Flat road before the avenue turn, or after leaving it. |
| Smallest sampled ramp plan radius | Approximately 13.696 m lower; 49.214 m upper | Curve diagnostic checked against independent circumcircle samples; no native highway standard is asserted. |
| New highway regression tests | 23 passed | Geometry checks and deliberately corrupted-output rejection; no game observations. |

The [validation summary](evidence/validation.json) records a complete portable run of `python3 -B tools/run_tests.py`: 1,344 tests, 80 explicit skips, and no failures. The source snapshot excludes ignored private settings, game inputs, and staged builds, as a contributor's clean clone does. Skips cover unavailable native HSR/NAM donors, missing protected or historical saved builds, and three current-ID assembly captures that have not been supplied. All 23 highway tests ran without skips. An additional run with local native inputs was stopped during the unchanged HSR model suite; no complete native-suite pass is claimed. The native-donor audit was separately run against the actual available archives.

The source retains the user's preference for a much smaller layout over the original conservative grade assumption. The final steep-ramp experiment replaces the 8% bound with a provisional 40% bound. It must not be described as a realistic motorway design or a proved game connection. Flat joins make the peak slopes higher than the height divided by the total ramp length: the lower ramp's whole-length average is 15.625%, while its active slope peaks near 32.497%.

A two-tile, 32 m lower-ramp trial with this same cubic shape, clearance, and flat joins needs approximately 53.768% grade, exceeding the chosen 40% prototype bound. Its approximately 2.925 m minimum plan radius is also smaller than the 3 m half-width of its road ribbon, indicating an inner-edge folding risk. This is a finding about that particular candidate, rather than proof that every possible two-tile design is impossible. The current three-tile design avoids those specific failures.

Lower ramps join the highway approximately 51.6113 m before or after the crossing centre, inside the longer upper approach extent. Separate saved approach and departure segments connect those internal branch nodes to the external highway arms. The graph therefore does not pretend that ramps of different lengths begin at the same three-dimensional port.

The prototype has no game-build claim. A highway provider and independent saved-resource verifier are missing. Complete diagonal native boundaries, actual road widths, deck solids, supports, curvature limits, traffic envelopes, junction flags, signals or priorities, native pedestrian channels, terrain behaviour, tile ownership, resource allocation, proper rotations, and the assembly menu remain unresolved. Before registration, JSONC support must be implemented consistently in the affected piece and assembly readers and writers. These are implementation stages, rather than optional game tests.

The candidate module split follows functions, rather than arbitrary model chunks: the three-level central crossing, approach branches, height transitions, and avenue intersections. Routes sharing a construction tile must remain coordinated until a safe cut is demonstrated. No component count, placement map, or neighbour compatibility has been proved. At-grade turning conflicts are intentional, and indirect returns through the avenue remain possible even though no immediate highway U-turn or direct deck-transfer edge is authored.

## 6. Design history

The initial broad schematic used 416 m highway half-lengths and avenue intersections 120 m to either side of the mainline. It demonstrated the requested four ramps but hid the stacked decks in the top view. Separate elevation profiles and crossing insets were added to make each deck's slip-lane height change visible. The user then confirmed NAM's double-decker RHW and requested a very tight, Tokyo-inspired urban layout.

An intermediate revision used a 560 m highway extent, a 70 m slip-lane corridor, and an 8% provisional grade bound. The user then explicitly accepted steeper ramps, suggested four or five tile lengths especially for the lower deck, and reduced that lower-ramp target to two or three tile lengths. The current revision removes the long parallel sections, solves the complete lower curves to 48 m, and keeps the upper curves longer at 80 m. Its 40% experimental grade bound and flat-join lengths are explicit changes to the earlier assumptions. Current dimensions and measured grades belong to `design.jsonc` and `evidence/geometry-check.json`; earlier dimensions are history, rather than retained buildable alternatives or an assertion that the final design is mathematically minimal.
