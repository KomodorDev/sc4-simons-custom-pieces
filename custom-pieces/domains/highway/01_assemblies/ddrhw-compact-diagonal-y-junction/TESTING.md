---
title: "DD RHW-4 compact diagonal Y-junction testing"
summary: "Check the three compiled components, their native approaches, the complete six-journey assembly, and the remaining human game cases."
audience: "Piece authors and reviewers"
document_type: "reference"
---

# DD RHW-4 compact diagonal Y-junction testing

<!-- ASSEMBLY TESTING LAYOUT: 1 -->

[Assembly overview ↗ (README)](README.md)

<!-- BEGIN DOCUMENT NAVIGATION -->
[1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)
<!-- END DOCUMENT NAVIGATION -->

## 1. Test scope

This document covers the [registered compact diagonal Y-junction](README.md): southwest arm A, northwest arm B, and east arm C. The [assembly definition](assembly.jsonc) owns the three placements, the 21-cell ownership, and the 6 × 7 construction rectangle. The [design brief](checks/design-brief.jsonc) retains the accepted six single-lane journeys and source experiment. Its historical source-stage registration flag is not the current assembly registry.

All three native ends are DD RHW-4, with two opposing decks at PATH heights 7.5 m and 15 m. A↔B and A↔C remain level, while B→C and C→B rise from the lower deck to the upper deck on separate corridors. U-turns are excluded. Actual saved lane paths, physical model faces, native approach rules, connector exports, and controller resources are software checks; menu behavior, game appearance, Route Query, and moving cars are separate human observations.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Human game checks use only 0° CCW; supported construction states and software rotation checks remain separate.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `external-1` | road / 1 / primary | out | [-24.0, -35.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `external-2` | road / 1 / primary | in | [-24.0, -35.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `external-3` | road / 1 / primary | out | [-24.0, -28.8, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `external-4` | road / 1 / primary | in | [-24.0, -28.8, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `external-5` | road / 1 / primary | in | [-24.0, 28.8, 7.5]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `external-6` | road / 1 / primary | out | [-24.0, 28.8, 15.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `external-7` | road / 1 / primary | in | [-24.0, 35.2, 7.5]; [0.7071067811865119, -0.7071067811865831]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `external-8` | road / 1 / primary | out | [-24.0, 35.2, 15.0]; [-0.7071067811865119, 0.7071067811865831]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `external-9` | road / 1 / primary | in | [56.0, -2.5, 7.5]; [-1.0, 0.0]; 0.0 | `path-interface-00480ef66d1c683adb2c` |
| `external-10` | road / 1 / primary | out | [56.0, -2.5, 15.0]; [1.0, 0.0]; 0.0 | `path-interface-aef756dec28195473947` |
| `external-11` | road / 1 / primary | in | [56.0, 2.5, 7.5]; [-1.0, 0.0]; 0.0 | `path-interface-28cd03e10e6e40a3c0fa` |
| `external-12` | road / 1 / primary | out | [56.0, 2.5, 15.0]; [1.0, 0.0]; 0.0 | `path-interface-c5c8334a7156c02c488c` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `external-11` → `external-8` | primary |
| road | `external-2` → `external-10` | primary |
| road | `external-4` → `external-6` | primary |
| road | `external-5` → `external-3` | primary |
| road | `external-7` → `external-12` | primary |
| road | `external-9` → `external-1` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `external-2` | road / `external-1` | not reachable in the saved placed encoded-route graph |
| road / `external-2` | road / `external-3` | not reachable in the saved placed encoded-route graph |
| road / `external-2` | road / `external-6` | not reachable in the saved placed encoded-route graph |
| road / `external-2` | road / `external-8` | not reachable in the saved placed encoded-route graph |
| road / `external-2` | road / `external-12` | not reachable in the saved placed encoded-route graph |
| road / `external-4` | road / `external-1` | not reachable in the saved placed encoded-route graph |
| road / `external-4` | road / `external-3` | not reachable in the saved placed encoded-route graph |
| road / `external-4` | road / `external-8` | not reachable in the saved placed encoded-route graph |
| road / `external-4` | road / `external-10` | not reachable in the saved placed encoded-route graph |
| road / `external-4` | road / `external-12` | not reachable in the saved placed encoded-route graph |
| road / `external-5` | road / `external-1` | not reachable in the saved placed encoded-route graph |
| road / `external-5` | road / `external-6` | not reachable in the saved placed encoded-route graph |
| road / `external-5` | road / `external-8` | not reachable in the saved placed encoded-route graph |
| road / `external-5` | road / `external-10` | not reachable in the saved placed encoded-route graph |
| road / `external-5` | road / `external-12` | not reachable in the saved placed encoded-route graph |
| road / `external-7` | road / `external-1` | not reachable in the saved placed encoded-route graph |
| road / `external-7` | road / `external-3` | not reachable in the saved placed encoded-route graph |
| road / `external-7` | road / `external-6` | not reachable in the saved placed encoded-route graph |
| road / `external-7` | road / `external-8` | not reachable in the saved placed encoded-route graph |
| road / `external-7` | road / `external-10` | not reachable in the saved placed encoded-route graph |
| road / `external-9` | road / `external-3` | not reachable in the saved placed encoded-route graph |
| road / `external-9` | road / `external-6` | not reachable in the saved placed encoded-route graph |
| road / `external-9` | road / `external-8` | not reachable in the saved placed encoded-route graph |
| road / `external-9` | road / `external-10` | not reachable in the saved placed encoded-route graph |
| road / `external-9` | road / `external-12` | not reachable in the saved placed encoded-route graph |
| road / `external-11` | road / `external-1` | not reachable in the saved placed encoded-route graph |
| road / `external-11` | road / `external-3` | not reachable in the saved placed encoded-route graph |
| road / `external-11` | road / `external-6` | not reachable in the saved placed encoded-route graph |
| road / `external-11` | road / `external-10` | not reachable in the saved placed encoded-route graph |
| road / `external-11` | road / `external-12` | not reachable in the saved placed encoded-route graph |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Run source commands from the repository root with the [Python dependencies](../../../../docs/BUILD_AND_INSTALL.md#31-python-setup-for-a-checkout-or-source-zip) installed. Pillow renders images, NumPy performs numerical geometry work, and Shapely constructs and checks planar pavement unions. Native builds require the exact supported NAM 50 right-hand-traffic inputs in private local settings; use the [input setup](../../../../docs/BUILD_AND_INSTALL.md#3-prepare-local-development-inputs). Keep game archives, personal paths, build outputs, and raw native audit logs outside Git.

Layout and PATH coordinates are east, north, and height in metres. Saved S3D model coordinates instead run east, height, and south; south is the negative of north. A source cell (column, row) has centre (16 × column, −16 × row), and tile edges are 8 m from its centre. The assembly's fixed southwest display reference is (−32, −48) m, so display X = (east + 32) / 16 and display Y = (north + 48) / 16. The full owned construction ranges are X0–X5 and Y0–Y6; the extra native C socket is at X6, Y3. P01, P02, and P03 have displayed references (X0, Y2), (X0, Y6), and (X1, Y3), respectively. P02's reference is unowned by the custom component and may contain its ordinary native B approach.

Use a disposable flat test city for the first deliberate installation. Close SimCity 4 before changing plugin DATs, keep one combined SCP controller for the installed selection, restart the game, and place all three components afresh. An old placement does not establish the behavior of new models, PATHs, or controller rules. The three-piece review selection contains only this junction; include every other SCP type you intend to retain in the normal source build before preparing a complete replacement installation. Follow the [assembly placement table](README.md#3-placements), reserving the native sockets (X0, Y1), (X0, Y5), and (X6, Y3), plus their outward continuation corridors.

Only the first native diagonal phase is implemented. Four proper rotations are in the software scope. A reflected layout and another relative grid alignment require their own measured interfaces and implementation; they are not supplied by cycling the repeated construction orientations.

## 3. Software checks

### 3.1 Build the three actual components

Run the exact selected build, then check the saved DAT resources. Keep earlier candidates: if an output directory below already exists, choose an unused suffix, such as `-02`, and use that revised name consistently in every later command that refers to it.

```sh
python3 -B custom-pieces/scp.py build --include ddrhw-y-diagonal-stem-split --include ddrhw-y-diagonal-branch --include ddrhw-y-orthogonal-core --output custom-pieces/dist/ddrhw-y-junction-native
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/ddrhw-y-junction-native
```

Each component contains real S3D game models and elevated SC4PATHS with `UseElevation=1`. Seven model-only cells have explicitly empty PATH resources; they do not gain artificial traffic lanes. The verifier reads indexed saved faces, positions, UV coordinates, materials, active paths, construction rules, native resources, and all five zoom models. A **UV coordinate** selects a point in a material's texture image. A saved preview must equal the union of the component's saved cell models.

### 3.2 Check the complete assembly and freeze actual boundaries

After the ordinary build passes, run the independent whole-assembly check and freeze complete connector measurements:

```sh
python3 -B custom-pieces/domains/highway/tools/freeze_y_junction_connectors.py custom-pieces/dist/ddrhw-y-junction-native
python3 -B -m scp_highway.connections --root custom-pieces --build custom-pieces/dist/ddrhw-y-junction-native --include-assemblies
```

The freeze tool checks all six directed journeys, cell ownership, actual native boundaries, and the complete saved physical assembly before accepting per-cell PATH fingerprints. A **fingerprint** is a SHA-256 value identifying exact file bytes. This binds later extraction to the checked resources. Complete physical checks include actual pavement support, vehicle width and height clearance, road and barrier shells, finite native-profile contact, and closed support solids. The declared route corridor is 2.5 m wide and 3.8 m high. These strip checks do not model the finite length or turning overhang of every vehicle; actual cars, longer vehicles, and animation remain game checks. The [support source](checks/support-solids.jsonc) supplies independent finite prism bounds and served-road attachment claims; it does not claim civil-engineering structural capacity.

Native profiles retain their measured heights, cross-sections, materials, and texture coordinates. Donors `57530000` and `57530900` place pavement approximately 1 mm above nominal PATH height; `57530200` uses nominal roof height. Each diagonal approach extends its exact profile through a three-metre collar; C retains literal original core faces through its own three-metre collar. The C texture coordinates retain their explicitly checked one-repeat phase. Only explicitly bounded float32 quantization contacts are admitted by the physical checker; a real geometric gap requires correcting the writer. **Float32** is the game's 32-bit floating-point coordinate representation.

The unchanged diagonal native helper supplies approximately 1.415 mm of each exterior PATH's endpoint before the authored underside begins. Pavement and vehicle checks still cover that entire endpoint prefix using the actual pinned native faces; the closed authored underside claim begins at its measured physical contact. Likewise, original native pavement buried beneath its own barrier remains in the DAT and rendering. The external-shell analysis excludes only those inherited interior roof regions after an independent native geometry, material, UV, and winding certificate. Neither exception applies to arbitrary authored pavement or a missing road face. The finite original `57530200` shoulder roofs are nominal 15 m or 7.5 m, above authored floors at 14.001000404 m or 6.500999928 m. Their approximately 0.998999596 m or 0.999000072 m depths are exact native-phase geometry outside the car spines, rather than numerical noise. All served car spines retain the one-metre authored underside check.

The diagonal owners share four inserted native marker-solution rows, while the orthogonal owner reuses four original rows. Original native continuation rules remain unchanged. The checked dependencies include original DD model, PATH, and exemplar resources, including the staggered diagonal continuation tile. These checks establish saved-resource agreement, rather than successful game dragging.

C’s new body closes inside its owned cell. The approximately 1 mm literal native roof and skirt beyond that cell keep the original open-bottom geometry. Only those independently source-certified outside fragments are excluded from closed external-skin analysis; the actual DAT faces, native source certificate, interference checks, and every C PATH underside check retain their full scope.

The diagonal peer’s original body wall is approximately 1.4158 mm inside its pavement perimeter. New outer walls close the actual pavement perimeter to the authored underside. Only the precisely source-certified old wall portion buried below nominal pavement is excluded from external-skin analysis; its raised 1 mm strip stays. Every original face remains in the DAT and the full interference checks. A missing new outer wall remains a shell failure.

The standard outer deck width is 6 m, including two 0.828125 m integral barrier bands, leaving 4.34375 m of clear asphalt. The inner edge of each graded link tapers to a 2.25 m half-width near a grade end, giving a 5.25 m minimum deck and 3.59375 m clear asphalt. The inner barrier base stays 1.421875 m from the route centre, compared with the declared 1.25 m corridor half-width. Actual saved faces must still pass every clearance and support check after these width changes.

### 3.3 Regenerate documentation and prepare the single menu button

After actual-resource extraction, write the reviewed connector declarations through `scp_highway.connections.write_connector_groups()`. The current declarations are included. Refresh and check all three exact types with these commands. Replace `/path/to/SimCity 4/Plugins` with the existing directory containing your audited NAM textures, keeping the quotation marks. The texture directory is read only.

```sh
python3 -B custom-pieces/scp.py connectors refresh --domain highway --piece ddrhw-y-diagonal-stem-split --piece ddrhw-y-diagonal-branch --piece ddrhw-y-orthogonal-core --build dist/ddrhw-y-junction-native --plugins '/path/to/SimCity 4/Plugins'
python3 -B custom-pieces/scp.py connectors check --domain highway --piece ddrhw-y-diagonal-stem-split --piece ddrhw-y-diagonal-branch --piece ddrhw-y-orthogonal-core --build dist/ddrhw-y-junction-native --plugins '/path/to/SimCity 4/Plugins'
```

Canonical standalone pictures come from `scp.preview --catalog --views angled top` using the verified build. The six assembly pictures come from `domains/highway/tools/render_compact_assembly.py --assembly ddrhw-compact-diagonal-y-junction`, with staging outside the build. Inspect all six, then promote the unchanged staged PNGs and portable provenance. The construction image must use the actual top-view models, 30% ownership fill, occupied-tile boundaries, actual model projection outlines, and the same fixed X/Y grid as every other view.

After the final documents, pictures, and observation-image bindings are current, rebuild the normal selection and prepare its menu package:

```sh
python3 -B custom-pieces/scp.py assembly-menu --domain highway --layout ddrhw-compact-diagonal-y-junction --source custom-pieces/dist/ddrhw-y-junction-native --output custom-pieces/dist/ddrhw-y-junction-menu
```

This packages one assembly button with a three-member Tab/Shift+Tab cycle. It does not combine three placements into one click or install the package. Retain the ordinary checked build as the source candidate.

### 3.4 Regression and documentation checks

Run the focused source, native-approach, and saved-resource regression suites, followed by the required repository checks:

```sh
python3 -B -m unittest discover -s custom-pieces/domains/highway/tests -p 'test_y_junction*.py' -v
python3 -B -m unittest discover -s custom-pieces/domains/highway/tests -p test_ddrhw_y_design.py -v
python3 -B custom-pieces/scp.py docs-check
python3 -B tools/run_tests.py
```

The tests include rejection controls for moved native boundaries, changed route heights, invalid ownership, missing saved routes, and unsupported construction states. Native-dependent tests report explicit skips when the proprietary inputs are absent. A passing portable suite does not establish a native test that was skipped. Actual command outcomes and candidate fingerprints belong in the implementation evidence; manual game results remain unchanged by every software command.

## 4. Game checks

No human game result is recorded for this new junction. Use the generated cases below as the authoritative record, and follow the [shared observation procedure](../../../../docs/TESTING.md). Do not convert a software render, agent review, or saved PATH pass into a game pass.

1. Restart after deliberately installing the selected package. Open **Transportation → Highways → SCP → Assemblies**, select the assembly's exact name, and verify that **Tab** cycles P01→P02→P03 and **Shift+Tab** reverses the cycle. Check every component's tooltip and four proper rotations.
2. Place the three components using the [exact placement table](README.md#3-placements). Confirm the sparse occupied shapes, the unowned P02 reference, both decks, every graded link, and all three unowned native sockets. Inspect for leftover construction markers, gaps, duplicate surfaces, missing textures, flickering pavement, and incorrect barriers or supports.
3. For each arm, check fresh optional-native-tile placement, extension outward with NAM's RealHighway tool, and connection to a separately prebuilt DD RHW-4 approach. Keep these observations separate. Inspect the diagonal staggered neighbour cells and confirm that no custom component replaced them.
4. Connect each arm to a test network that can generate demand. Check A→B, B→A, A→C, C→A, B→C, and C→B individually. Record **Route Query** and an actual moving car completing each journey as separate observations. Confirm one lane per journey, the correct entering and leaving deck, and no U-turn or unintended transfer.
5. Inspect both decks and both graded links at every zoom and camera orientation. Check whether active paths retain 7.5 m and 15 m heights, and whether moving cars follow the ramps without visible jumps. Custom projected shadows are disabled for this candidate; observe actual game lighting and shadow behavior separately.
6. Redraw adjacent native highways, demolish one component without damaging neighbours, replace it at the same reference, save, exit, reload, and repeat all six journey checks. Repeat the construction and connection checks for the other three proper rotations. Reflections and another grid phase remain outside this candidate.

## 5. Results and known issues

On **4 November 2026**, Simon confirmed that the assembly rendered correctly in SimCity 4. He also confirmed that Route Query and visible traffic passed for all six permitted directions between the three arms. The [test checklist](#test-checklist) records the thirteen passes under its reference-layout cases. Simon did not specify a separate rotation.

The ordinary three-piece DAT build and the complete actual-DAT assembly check pass. All 21 canonical S3D/PATH pairs are byte-identical to the independently accepted final cell snapshot. The checks cover six journeys, twelve native end members, four rotations, 4,987 complete route strips and undersides, 24 native car segments, 66 support prisms, 39 slab contacts, and both rail-interference guards. The actual missing-wall mutation is rejected while the original native certificates remain valid. See [compiled verification](evidence/compiled-verification.jsonc) for exact resources, source fingerprints, scopes, and counts. At that build capture, installation, human game appearance, traffic, and native dragging were unverified.

The six canonical assembly pictures are rendered from the checked DATs and reviewed for the required cameras, labels, and construction overlays; [render provenance](evidence/compiled-render-paint-join-20261104.jsonc) binds their exact bytes. Three standalone angled/top image sets and all three connector exports and cards are current. The 51 focused Y tests pass with no skips, and three additional render-caption regressions pass.

A later [additive installation](evidence/additive-installation-20261103.jsonc) is now verified on the filesystem: the three Y DATs were added, the shared controller and menu were updated, and all 225 existing piece DATs retained their exact contents, file identities, and modification times. The installation now contains 228 types. The prior installation and receipt have a verified rollback backup. The earlier development archives remain frozen pre-install captures. On **3 November 2026**, the user reported **“okay good it works.”** about the original installed junction. The [general human report](evidence/human-general-operation-20261103.jsonc) binds that statement to the installed compound manifest, receipt, and exact Y DAT files. That 3 November report was general and did not establish individual cases.

The earlier installed capture can show a tone seam where the DD material meets the single-lane MIS ramp material. Its outer yellow stripe steps sideways at the fan handoff, and the outer white stripe can end where the MIS texture places it beneath the barrier. The verified revised DATs align the outer yellow and white lines at all six sampled original arm and deck joins and blend into the lane texture over 6 m. The revised mapping constrains the white line to the available asphalt and retains the existing native centre-dash gap at the handoff. The saved comparison confirms the original traffic path bytes and native model joins are preserved. See the [saved DAT verification](evidence/paint-join-verification-20261104.jsonc) and the [shared marking contract](../../NETWORK_SPEC.md#173-paint-alignment-at-the-dd-to-mis-joins).

The graded links are intentionally steep compact game geometry. The road and support checks prove the declared geometric envelopes and saved-resource contracts, rather than structural engineering, real-world highway suitability, or traffic capacity. Native helper placement is experimental. The assembly is disabled in default build selections and must be selected explicitly. No reflected or second-alignment variant is included.

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Human game checks are required only at 0° CCW. Supported construction orientations and software rotation checks retain their separate scope; these human cases do not establish observations at the other orientations.

Current totals: unverified: 42, passed: 13, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/01_assemblies/ddrhw-compact-diagonal-y-junction/checks/manual-tests.json --observation custom-pieces/domains/highway/01_assemblies/ddrhw-compact-diagonal-y-junction/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-2da37c4d9ad7ac7307fe">[ ] unverified</a> | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-2da37c4d9ad7ac7307fe"></a>

**General: unverified** — `software_resources-2da37c4d9ad7ac7307fe`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-2da37c4d9ad7ac7307fe">[ ] unverified</a> | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-2da37c4d9ad7ac7307fe"></a>

**General: unverified** — `software_connectivity-2da37c4d9ad7ac7307fe`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-465a700caf670d0de617">[x] passed</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-465a700caf670d0de617"></a>

**0° CCW: passed** — `in_game_render-465a700caf670d0de617`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-04; evidence: [Simon reported “now update the tests for our DD RHW junction: render, path, and traffic render all pass”., Simon confirmed “Both the original and reversed-traffic versions”., When asked about Route Query and visible traffic in all six directions, Simon confirmed “Yes, all six directions for both checks”., The installed component DATs and construction rules match this record’s resource fingerprints.]; environment: platform: Windows SimCity 4 through Wine on macOS (current installed test setup); game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50, right-hand traffic; installed manifest sha256: 8d962d444d76d0f122e516f4b63793399f7d09ffb093983731f282638d086288; note: Recorded in this assembly’s reference-layout cases. The user confirmed rendering and all six permitted journeys for both Route Query and visible traffic. No separate rotation was reported.

</details>

</details>

<details>
<summary>Placement — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-465a700caf670d0de617">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-465a700caf670d0de617"></a>

**0° CCW: unverified** — `in_game_placement-465a700caf670d0de617`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-465a700caf670d0de617">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-465a700caf670d0de617"></a>

**0° CCW: unverified** — `in_game_demolition-465a700caf670d0de617`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-465a700caf670d0de617">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-465a700caf670d0de617"></a>

**0° CCW: unverified** — `in_game_save_reload-465a700caf670d0de617`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 6 cases; passed: 6</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: external-11>external-8; entry: external-11; exit: external-8 | — | <a href="#case-in_game_route_query-43cd4b114ba16db01787">[x] passed</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-2>external-10; entry: external-2; exit: external-10 | — | <a href="#case-in_game_route_query-b25d963a622411d235d9">[x] passed</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-4>external-6; entry: external-4; exit: external-6 | — | <a href="#case-in_game_route_query-0c893f7b6eb5ef69293a">[x] passed</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3 | — | <a href="#case-in_game_route_query-45093b97a30e304435a4">[x] passed</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-7>external-12; entry: external-7; exit: external-12 | — | <a href="#case-in_game_route_query-c87e6848ddfffc9a497f">[x] passed</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-9>external-1; entry: external-9; exit: external-1 | — | <a href="#case-in_game_route_query-56a9183bc6dd760de5ed">[x] passed</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: external-11>external-8; entry: external-11; exit: external-8</summary>

<a id="case-in_game_route_query-43cd4b114ba16db01787"></a>

**0° CCW: passed** — `in_game_route_query-43cd4b114ba16db01787`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-11>external-8; entry: external-11; exit: external-8.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-04; evidence: [Simon reported “now update the tests for our DD RHW junction: render, path, and traffic render all pass”., Simon confirmed “Both the original and reversed-traffic versions”., When asked about Route Query and visible traffic in all six directions, Simon confirmed “Yes, all six directions for both checks”., The installed component DATs and construction rules match this record’s resource fingerprints.]; environment: platform: Windows SimCity 4 through Wine on macOS (current installed test setup); game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50, right-hand traffic; installed manifest sha256: 8d962d444d76d0f122e516f4b63793399f7d09ffb093983731f282638d086288; note: Recorded in this assembly’s reference-layout cases. The user confirmed rendering and all six permitted journeys for both Route Query and visible traffic. No separate rotation was reported.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-2>external-10; entry: external-2; exit: external-10</summary>

<a id="case-in_game_route_query-b25d963a622411d235d9"></a>

**0° CCW: passed** — `in_game_route_query-b25d963a622411d235d9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-2>external-10; entry: external-2; exit: external-10.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-04; evidence: [Simon reported “now update the tests for our DD RHW junction: render, path, and traffic render all pass”., Simon confirmed “Both the original and reversed-traffic versions”., When asked about Route Query and visible traffic in all six directions, Simon confirmed “Yes, all six directions for both checks”., The installed component DATs and construction rules match this record’s resource fingerprints.]; environment: platform: Windows SimCity 4 through Wine on macOS (current installed test setup); game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50, right-hand traffic; installed manifest sha256: 8d962d444d76d0f122e516f4b63793399f7d09ffb093983731f282638d086288; note: Recorded in this assembly’s reference-layout cases. The user confirmed rendering and all six permitted journeys for both Route Query and visible traffic. No separate rotation was reported.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-4>external-6; entry: external-4; exit: external-6</summary>

<a id="case-in_game_route_query-0c893f7b6eb5ef69293a"></a>

**0° CCW: passed** — `in_game_route_query-0c893f7b6eb5ef69293a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-4>external-6; entry: external-4; exit: external-6.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-04; evidence: [Simon reported “now update the tests for our DD RHW junction: render, path, and traffic render all pass”., Simon confirmed “Both the original and reversed-traffic versions”., When asked about Route Query and visible traffic in all six directions, Simon confirmed “Yes, all six directions for both checks”., The installed component DATs and construction rules match this record’s resource fingerprints.]; environment: platform: Windows SimCity 4 through Wine on macOS (current installed test setup); game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50, right-hand traffic; installed manifest sha256: 8d962d444d76d0f122e516f4b63793399f7d09ffb093983731f282638d086288; note: Recorded in this assembly’s reference-layout cases. The user confirmed rendering and all six permitted journeys for both Route Query and visible traffic. No separate rotation was reported.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3</summary>

<a id="case-in_game_route_query-45093b97a30e304435a4"></a>

**0° CCW: passed** — `in_game_route_query-45093b97a30e304435a4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-04; evidence: [Simon reported “now update the tests for our DD RHW junction: render, path, and traffic render all pass”., Simon confirmed “Both the original and reversed-traffic versions”., When asked about Route Query and visible traffic in all six directions, Simon confirmed “Yes, all six directions for both checks”., The installed component DATs and construction rules match this record’s resource fingerprints.]; environment: platform: Windows SimCity 4 through Wine on macOS (current installed test setup); game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50, right-hand traffic; installed manifest sha256: 8d962d444d76d0f122e516f4b63793399f7d09ffb093983731f282638d086288; note: Recorded in this assembly’s reference-layout cases. The user confirmed rendering and all six permitted journeys for both Route Query and visible traffic. No separate rotation was reported.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-7>external-12; entry: external-7; exit: external-12</summary>

<a id="case-in_game_route_query-c87e6848ddfffc9a497f"></a>

**0° CCW: passed** — `in_game_route_query-c87e6848ddfffc9a497f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-7>external-12; entry: external-7; exit: external-12.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-04; evidence: [Simon reported “now update the tests for our DD RHW junction: render, path, and traffic render all pass”., Simon confirmed “Both the original and reversed-traffic versions”., When asked about Route Query and visible traffic in all six directions, Simon confirmed “Yes, all six directions for both checks”., The installed component DATs and construction rules match this record’s resource fingerprints.]; environment: platform: Windows SimCity 4 through Wine on macOS (current installed test setup); game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50, right-hand traffic; installed manifest sha256: 8d962d444d76d0f122e516f4b63793399f7d09ffb093983731f282638d086288; note: Recorded in this assembly’s reference-layout cases. The user confirmed rendering and all six permitted journeys for both Route Query and visible traffic. No separate rotation was reported.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-9>external-1; entry: external-9; exit: external-1</summary>

<a id="case-in_game_route_query-56a9183bc6dd760de5ed"></a>

**0° CCW: passed** — `in_game_route_query-56a9183bc6dd760de5ed`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-9>external-1; entry: external-9; exit: external-1.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-04; evidence: [Simon reported “now update the tests for our DD RHW junction: render, path, and traffic render all pass”., Simon confirmed “Both the original and reversed-traffic versions”., When asked about Route Query and visible traffic in all six directions, Simon confirmed “Yes, all six directions for both checks”., The installed component DATs and construction rules match this record’s resource fingerprints.]; environment: platform: Windows SimCity 4 through Wine on macOS (current installed test setup); game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50, right-hand traffic; installed manifest sha256: 8d962d444d76d0f122e516f4b63793399f7d09ffb093983731f282638d086288; note: Recorded in this assembly’s reference-layout cases. The user confirmed rendering and all six permitted journeys for both Route Query and visible traffic. No separate rotation was reported.

</details>

</details>

<details>
<summary>Visible travel — road — 6 cases; passed: 6</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: external-11>external-8; entry: external-11; exit: external-8 | — | <a href="#case-in_game_visible_travel-43cd4b114ba16db01787">[x] passed</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-2>external-10; entry: external-2; exit: external-10 | — | <a href="#case-in_game_visible_travel-b25d963a622411d235d9">[x] passed</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-4>external-6; entry: external-4; exit: external-6 | — | <a href="#case-in_game_visible_travel-0c893f7b6eb5ef69293a">[x] passed</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3 | — | <a href="#case-in_game_visible_travel-45093b97a30e304435a4">[x] passed</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-7>external-12; entry: external-7; exit: external-12 | — | <a href="#case-in_game_visible_travel-c87e6848ddfffc9a497f">[x] passed</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-9>external-1; entry: external-9; exit: external-1 | — | <a href="#case-in_game_visible_travel-56a9183bc6dd760de5ed">[x] passed</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-11>external-8; entry: external-11; exit: external-8</summary>

<a id="case-in_game_visible_travel-43cd4b114ba16db01787"></a>

**0° CCW: passed** — `in_game_visible_travel-43cd4b114ba16db01787`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-11>external-8; entry: external-11; exit: external-8.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-04; evidence: [Simon reported “now update the tests for our DD RHW junction: render, path, and traffic render all pass”., Simon confirmed “Both the original and reversed-traffic versions”., When asked about Route Query and visible traffic in all six directions, Simon confirmed “Yes, all six directions for both checks”., The installed component DATs and construction rules match this record’s resource fingerprints.]; environment: platform: Windows SimCity 4 through Wine on macOS (current installed test setup); game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50, right-hand traffic; installed manifest sha256: 8d962d444d76d0f122e516f4b63793399f7d09ffb093983731f282638d086288; note: Recorded in this assembly’s reference-layout cases. The user confirmed rendering and all six permitted journeys for both Route Query and visible traffic. No separate rotation was reported.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-2>external-10; entry: external-2; exit: external-10</summary>

<a id="case-in_game_visible_travel-b25d963a622411d235d9"></a>

**0° CCW: passed** — `in_game_visible_travel-b25d963a622411d235d9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-2>external-10; entry: external-2; exit: external-10.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-04; evidence: [Simon reported “now update the tests for our DD RHW junction: render, path, and traffic render all pass”., Simon confirmed “Both the original and reversed-traffic versions”., When asked about Route Query and visible traffic in all six directions, Simon confirmed “Yes, all six directions for both checks”., The installed component DATs and construction rules match this record’s resource fingerprints.]; environment: platform: Windows SimCity 4 through Wine on macOS (current installed test setup); game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50, right-hand traffic; installed manifest sha256: 8d962d444d76d0f122e516f4b63793399f7d09ffb093983731f282638d086288; note: Recorded in this assembly’s reference-layout cases. The user confirmed rendering and all six permitted journeys for both Route Query and visible traffic. No separate rotation was reported.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-4>external-6; entry: external-4; exit: external-6</summary>

<a id="case-in_game_visible_travel-0c893f7b6eb5ef69293a"></a>

**0° CCW: passed** — `in_game_visible_travel-0c893f7b6eb5ef69293a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-4>external-6; entry: external-4; exit: external-6.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-04; evidence: [Simon reported “now update the tests for our DD RHW junction: render, path, and traffic render all pass”., Simon confirmed “Both the original and reversed-traffic versions”., When asked about Route Query and visible traffic in all six directions, Simon confirmed “Yes, all six directions for both checks”., The installed component DATs and construction rules match this record’s resource fingerprints.]; environment: platform: Windows SimCity 4 through Wine on macOS (current installed test setup); game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50, right-hand traffic; installed manifest sha256: 8d962d444d76d0f122e516f4b63793399f7d09ffb093983731f282638d086288; note: Recorded in this assembly’s reference-layout cases. The user confirmed rendering and all six permitted journeys for both Route Query and visible traffic. No separate rotation was reported.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3</summary>

<a id="case-in_game_visible_travel-45093b97a30e304435a4"></a>

**0° CCW: passed** — `in_game_visible_travel-45093b97a30e304435a4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-5>external-3; entry: external-5; exit: external-3.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-04; evidence: [Simon reported “now update the tests for our DD RHW junction: render, path, and traffic render all pass”., Simon confirmed “Both the original and reversed-traffic versions”., When asked about Route Query and visible traffic in all six directions, Simon confirmed “Yes, all six directions for both checks”., The installed component DATs and construction rules match this record’s resource fingerprints.]; environment: platform: Windows SimCity 4 through Wine on macOS (current installed test setup); game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50, right-hand traffic; installed manifest sha256: 8d962d444d76d0f122e516f4b63793399f7d09ffb093983731f282638d086288; note: Recorded in this assembly’s reference-layout cases. The user confirmed rendering and all six permitted journeys for both Route Query and visible traffic. No separate rotation was reported.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-7>external-12; entry: external-7; exit: external-12</summary>

<a id="case-in_game_visible_travel-c87e6848ddfffc9a497f"></a>

**0° CCW: passed** — `in_game_visible_travel-c87e6848ddfffc9a497f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-7>external-12; entry: external-7; exit: external-12.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-04; evidence: [Simon reported “now update the tests for our DD RHW junction: render, path, and traffic render all pass”., Simon confirmed “Both the original and reversed-traffic versions”., When asked about Route Query and visible traffic in all six directions, Simon confirmed “Yes, all six directions for both checks”., The installed component DATs and construction rules match this record’s resource fingerprints.]; environment: platform: Windows SimCity 4 through Wine on macOS (current installed test setup); game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50, right-hand traffic; installed manifest sha256: 8d962d444d76d0f122e516f4b63793399f7d09ffb093983731f282638d086288; note: Recorded in this assembly’s reference-layout cases. The user confirmed rendering and all six permitted journeys for both Route Query and visible traffic. No separate rotation was reported.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-9>external-1; entry: external-9; exit: external-1</summary>

<a id="case-in_game_visible_travel-56a9183bc6dd760de5ed"></a>

**0° CCW: passed** — `in_game_visible_travel-56a9183bc6dd760de5ed`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-9>external-1; entry: external-9; exit: external-1.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-04; evidence: [Simon reported “now update the tests for our DD RHW junction: render, path, and traffic render all pass”., Simon confirmed “Both the original and reversed-traffic versions”., When asked about Route Query and visible traffic in all six directions, Simon confirmed “Yes, all six directions for both checks”., The installed component DATs and construction rules match this record’s resource fingerprints.]; environment: platform: Windows SimCity 4 through Wine on macOS (current installed test setup); game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50, right-hand traffic; installed manifest sha256: 8d962d444d76d0f122e516f4b63793399f7d09ffb093983731f282638d086288; note: Recorded in this assembly’s reference-layout cases. The user confirmed rendering and all six permitted journeys for both Route Query and visible traffic. No separate rotation was reported.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 30 cases; unverified: 30</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Forbidden transfer**<br>from port: external-2; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-b1d731177041e6b6a2a2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-c5b03c092c50638d2d5f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-6; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-54f06858f62feb7ed51f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-a28ed6e6ed70d51f6391">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-e16a323fc244e5f82504">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-6af83903a68ce8016fd2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-a3489bb7f0024115630e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-76a99da4f12f8780c1d0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-c42f7ebfc416b0b485d6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f5571ef39326d49443fe">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-a77ab27f193b9306851f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-6; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f23915b0a74bf3a96501">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-94fab5af3bd61bd9d753">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f973763b324c6bfa4d8a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-0b8a7675ba74e1f2ff93">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-7; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-a0bf81e5cd4716bbee05">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-7; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ee3e2ce78f340e0a6a5e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-7; to port: external-6; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-fc81d48fb897a4419fe8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-7; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-31725baaf3e50fce72b7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-7; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-bc14f5590e9972943cf2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-9; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-822d599b5ac726c3a054">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-9; to port: external-6; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-84ee9177920704615e46">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-9; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-4e0bb33e22d53a3e9eaa">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-9; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-cb82de06d20f783873cd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-9; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-498f33631ff14a70224a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ac52c2f6fb17a4da916e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-0b69825467445cfb42c2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-6; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-4b0cbfa27a443564bcd5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-aacccceb4827941747cf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-40017744d2a72dcbcf1a">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-b1d731177041e6b6a2a2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b1d731177041e6b6a2a2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-c5b03c092c50638d2d5f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c5b03c092c50638d2d5f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-6; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-54f06858f62feb7ed51f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-54f06858f62feb7ed51f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-6; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-a28ed6e6ed70d51f6391"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a28ed6e6ed70d51f6391`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-e16a323fc244e5f82504"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e16a323fc244e5f82504`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-6af83903a68ce8016fd2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6af83903a68ce8016fd2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-a3489bb7f0024115630e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a3489bb7f0024115630e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-76a99da4f12f8780c1d0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-76a99da4f12f8780c1d0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-c42f7ebfc416b0b485d6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c42f7ebfc416b0b485d6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f5571ef39326d49443fe"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f5571ef39326d49443fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-a77ab27f193b9306851f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a77ab27f193b9306851f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-6; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f23915b0a74bf3a96501"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f23915b0a74bf3a96501`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-6; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-94fab5af3bd61bd9d753"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-94fab5af3bd61bd9d753`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f973763b324c6bfa4d8a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f973763b324c6bfa4d8a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-0b8a7675ba74e1f2ff93"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0b8a7675ba74e1f2ff93`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-7; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-a0bf81e5cd4716bbee05"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a0bf81e5cd4716bbee05`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-7; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-7; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ee3e2ce78f340e0a6a5e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ee3e2ce78f340e0a6a5e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-7; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-7; to port: external-6; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-fc81d48fb897a4419fe8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fc81d48fb897a4419fe8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-7; to port: external-6; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-7; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-31725baaf3e50fce72b7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-31725baaf3e50fce72b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-7; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-7; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-bc14f5590e9972943cf2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bc14f5590e9972943cf2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-7; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-9; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-822d599b5ac726c3a054"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-822d599b5ac726c3a054`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-9; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-9; to port: external-6; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-84ee9177920704615e46"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-84ee9177920704615e46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-9; to port: external-6; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-9; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-4e0bb33e22d53a3e9eaa"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4e0bb33e22d53a3e9eaa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-9; to port: external-8; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-9; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-cb82de06d20f783873cd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cb82de06d20f783873cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-9; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-9; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-498f33631ff14a70224a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-498f33631ff14a70224a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-9; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ac52c2f6fb17a4da916e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ac52c2f6fb17a4da916e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-0b69825467445cfb42c2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0b69825467445cfb42c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-6; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-4b0cbfa27a443564bcd5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4b0cbfa27a443564bcd5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-6; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-aacccceb4827941747cf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-aacccceb4827941747cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-40017744d2a72dcbcf1a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-40017744d2a72dcbcf1a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 7 cases; unverified: 7</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-compact-diagonal-y-junction:clean-southeast | <a href="#case-preview_review-6e9637da6baaa504c0c1">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-compact-diagonal-y-junction:clean-top | <a href="#case-preview_review-a82a1fdc67259b10e04d">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-compact-diagonal-y-junction:named-northwest | <a href="#case-preview_review-2680b6c541b8b6e48b98">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-compact-diagonal-y-junction:named-southeast | <a href="#case-preview_review-276ae131cbef4f194360">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-compact-diagonal-y-junction:named-top | <a href="#case-preview_review-711ee7e5b6d579c69422">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-compact-diagonal-y-junction:source-schematic | <a href="#case-preview_review-1aeb33fe04885f5c62da">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-compact-diagonal-y-junction:tile-ownership | <a href="#case-preview_review-aa75e44a78941093e3b5">[ ] unverified</a> | — |


<details>
<summary>Preview review — Image: image:ddrhw-compact-diagonal-y-junction:clean-southeast</summary>

<a id="case-preview_review-6e9637da6baaa504c0c1"></a>

**General: unverified** — `preview_review-6e9637da6baaa504c0c1`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-compact-diagonal-y-junction:clean-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-compact-diagonal-y-junction:clean-top</summary>

<a id="case-preview_review-a82a1fdc67259b10e04d"></a>

**General: unverified** — `preview_review-a82a1fdc67259b10e04d`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-compact-diagonal-y-junction:clean-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-compact-diagonal-y-junction:named-northwest</summary>

<a id="case-preview_review-2680b6c541b8b6e48b98"></a>

**General: unverified** — `preview_review-2680b6c541b8b6e48b98`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-compact-diagonal-y-junction:named-northwest.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-compact-diagonal-y-junction:named-southeast</summary>

<a id="case-preview_review-276ae131cbef4f194360"></a>

**General: unverified** — `preview_review-276ae131cbef4f194360`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-compact-diagonal-y-junction:named-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-compact-diagonal-y-junction:named-top</summary>

<a id="case-preview_review-711ee7e5b6d579c69422"></a>

**General: unverified** — `preview_review-711ee7e5b6d579c69422`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-compact-diagonal-y-junction:named-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-compact-diagonal-y-junction:source-schematic</summary>

<a id="case-preview_review-1aeb33fe04885f5c62da"></a>

**General: unverified** — `preview_review-1aeb33fe04885f5c62da`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-compact-diagonal-y-junction:source-schematic.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-compact-diagonal-y-junction:tile-ownership</summary>

<a id="case-preview_review-aa75e44a78941093e3b5"></a>

**General: unverified** — `preview_review-aa75e44a78941093e3b5`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-compact-diagonal-y-junction:tile-ownership.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The agreed brief on 2026-11-03 corrected the stem to southwest, the diagonal branch to northwest, and the orthogonal branch to east. After the lane-direction explanation, the user accepted the two separate deck-changing B↔C connections and requested implementation. The vehicle heading changes are 90° for A↔B and 45° for A↔C and B↔C. The geometric outward rays of A–C and B–C are each 135° apart.

The initial source-only experiment remains in [source geometry](evidence/design-geometry.jsonc), [independent source verification](evidence/source-verification.jsonc), [native measurements](evidence/native-design-inputs.jsonc), and the [source schematic](previews/source-schematic.png). Its [workflow checkpoint](evidence/workflow-checkpoint.jsonc) binds that historical stage. The exact original checkpoint inputs, including the original source-stage guides, are preserved in the Git repository at `evidence/history/initial-source-design.zip`; development and source distribution ZIPs omit that historical archive. Those records do not verify the current compiled implementation.

Physical construction required retaining the staggered native barrier profiles and two shoulder ownership cells beyond the provisional source strips. The provisional source partition had 21 cells. Physical collars first needed 23; relocating a literal 1 mm native C corner to its correct C owner removed an otherwise unnecessary northwest-component cell, leaving 22. Closing the authored C fan at its actual owned northern boundary removed a second empty fringe cell, leaving the final 21 cells. This measured mask differs from the provisional 21-cell mask. The final mask preserves the accepted six source routes and all remaining allocated identities. The native collars remain 3 m long, C retains its measured approximately 1 mm native phase extension, and each city tile has exactly one custom owner. The final construction reference is (−32, −48) m; the historical source schematic used a different drawing frame and is not a placement plan.

A private source parameter experiment shortened C by one tile and left too little provisional physical margin. The retained C approach is one tile farther out. No minimum-footprint proof or additional alignment is claimed. The first measured phase is implemented before any decision to produce another phase, under the [staged alignment rule](../../../../docs/WORKFLOW_PIECE_CREATION.md#alignment-production-order).
