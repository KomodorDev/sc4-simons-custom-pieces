---
title: "Testing — DD RHW-4 — Compact Y-Junction — Diagonal Stem — Reversed Traffic"
summary: "Reproduce reversed-traffic resource checks and record separate human observations."
audience: "contributors and testers"
document_type: "reference"
---

# Testing — DD RHW-4 — Compact Y-Junction — Diagonal Stem — Reversed Traffic

<!-- ASSEMBLY TESTING LAYOUT: 1 -->

[Assembly overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

This counterpart uses the original southwest, northwest, and east arm positions, with all six directed journeys reversed. A is outgoing on the upper deck, and B and C are incoming. The lower directions are opposite. Both B↔C links descend from 15 m to 7.5 m. Yellow stays on the driver's left. The [source review](evidence/source-verification.jsonc), [native measurements](evidence/native-design-inputs.jsonc), and [support source](checks/support-solids.jsonc) belong specifically to this variant.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Human game checks use only 0° CCW; supported construction states and software rotation checks remain separate.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `external-1` | road / 1 / primary | in | [-24.0, -35.2, 7.5]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `external-2` | road / 1 / primary | out | [-24.0, -35.2, 15.0]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `external-3` | road / 1 / primary | in | [-24.0, -28.8, 7.5]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `external-4` | road / 1 / primary | out | [-24.0, -28.8, 15.0]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `external-5` | road / 1 / primary | out | [-24.0, 28.8, 7.5]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `external-6` | road / 1 / primary | in | [-24.0, 28.8, 15.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `external-7` | road / 1 / primary | out | [-24.0, 35.2, 7.5]; [-0.7071067811865119, 0.7071067811865831]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `external-8` | road / 1 / primary | in | [-24.0, 35.2, 15.0]; [0.7071067811865119, -0.7071067811865831]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `external-9` | road / 1 / primary | out | [56.0, -2.5, 7.5]; [1.0, 0.0]; 0.0 | `path-interface-b2fe320b9e0bb31bdb27` |
| `external-10` | road / 1 / primary | in | [56.0, -2.5, 15.0]; [-1.0, 0.0]; 0.0 | `path-interface-02def3c4ce1dd299e969` |
| `external-11` | road / 1 / primary | out | [56.0, 2.5, 7.5]; [1.0, 0.0]; 0.0 | `path-interface-fddc704c2b84d595ec6f` |
| `external-12` | road / 1 / primary | in | [56.0, 2.5, 15.0]; [-1.0, 0.0]; 0.0 | `path-interface-991f143956c37b818e99` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `external-10` → `external-2` | primary |
| road | `external-12` → `external-7` | primary |
| road | `external-1` → `external-9` | primary |
| road | `external-3` → `external-5` | primary |
| road | `external-6` → `external-4` | primary |
| road | `external-8` → `external-11` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `external-1` | road / `external-2` | not reachable in the saved placed encoded-route graph |
| road / `external-1` | road / `external-4` | not reachable in the saved placed encoded-route graph |
| road / `external-1` | road / `external-5` | not reachable in the saved placed encoded-route graph |
| road / `external-1` | road / `external-7` | not reachable in the saved placed encoded-route graph |
| road / `external-1` | road / `external-11` | not reachable in the saved placed encoded-route graph |
| road / `external-3` | road / `external-2` | not reachable in the saved placed encoded-route graph |
| road / `external-3` | road / `external-4` | not reachable in the saved placed encoded-route graph |
| road / `external-3` | road / `external-7` | not reachable in the saved placed encoded-route graph |
| road / `external-3` | road / `external-9` | not reachable in the saved placed encoded-route graph |
| road / `external-3` | road / `external-11` | not reachable in the saved placed encoded-route graph |
| road / `external-6` | road / `external-2` | not reachable in the saved placed encoded-route graph |
| road / `external-6` | road / `external-5` | not reachable in the saved placed encoded-route graph |
| road / `external-6` | road / `external-7` | not reachable in the saved placed encoded-route graph |
| road / `external-6` | road / `external-9` | not reachable in the saved placed encoded-route graph |
| road / `external-6` | road / `external-11` | not reachable in the saved placed encoded-route graph |
| road / `external-8` | road / `external-2` | not reachable in the saved placed encoded-route graph |
| road / `external-8` | road / `external-4` | not reachable in the saved placed encoded-route graph |
| road / `external-8` | road / `external-5` | not reachable in the saved placed encoded-route graph |
| road / `external-8` | road / `external-7` | not reachable in the saved placed encoded-route graph |
| road / `external-8` | road / `external-9` | not reachable in the saved placed encoded-route graph |
| road / `external-10` | road / `external-4` | not reachable in the saved placed encoded-route graph |
| road / `external-10` | road / `external-5` | not reachable in the saved placed encoded-route graph |
| road / `external-10` | road / `external-7` | not reachable in the saved placed encoded-route graph |
| road / `external-10` | road / `external-9` | not reachable in the saved placed encoded-route graph |
| road / `external-10` | road / `external-11` | not reachable in the saved placed encoded-route graph |
| road / `external-12` | road / `external-2` | not reachable in the saved placed encoded-route graph |
| road / `external-12` | road / `external-4` | not reachable in the saved placed encoded-route graph |
| road / `external-12` | road / `external-5` | not reachable in the saved placed encoded-route graph |
| road / `external-12` | road / `external-9` | not reachable in the saved placed encoded-route graph |
| road / `external-12` | road / `external-11` | not reachable in the saved placed encoded-route graph |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Run commands from the repository root with the [Python dependencies](../../../../docs/BUILD_AND_INSTALL.md#31-python-setup-for-a-checkout-or-source-zip) installed. Native builds read the exact supported NAM 50 right-hand-traffic resources from private local settings. Keep proprietary game archives, personal paths, and raw native logs outside Git.

Coordinates are east, north, and height in metres. Saved S3D models instead use east, height, and south. Source cell (column,row) has centre (16 × column, −16 × row). Each tile edge is 8 m from its centre. The fixed assembly display reference is (−32,−48) m; display X = (east + 32) / 16, and display Y = (north + 48) / 16. The owned rectangle is 6 × 7 tiles, or 96 × 112 m, with 21 occupied cells. P01, P02, and P03 references are (X0,Y2), (X0,Y6), and (X1,Y3), respectively. P02's reference is unowned. Native sockets are (X0,Y1), (X0,Y5), and (X6,Y3).

Use a disposable flat test city, deliberately install the selected candidate, restart the game, and place all three reversed components afresh. Preserve the original Y and every other installed type. A selected three-piece development build is not a complete replacement for a larger existing installation; an additive installation must retain the old files and combine the controller and menu without losing old resources.

## 3. Software checks

### 3.1 Compile and verify the actual resources

Choose an unused output directory. Run:

```sh
python3 -B custom-pieces/scp.py build --include ddrhw-y-reversed-diagonal-stem-split --include ddrhw-y-reversed-diagonal-branch --include ddrhw-y-reversed-orthogonal-core --output custom-pieces/dist/ddrhw-y-reversed-native
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/ddrhw-y-reversed-native
python3 -B custom-pieces/domains/highway/tools/freeze_y_junction_connectors.py custom-pieces/dist/ddrhw-y-reversed-native --variant reversed
python3 -B -m scp_highway.connections --root custom-pieces --build custom-pieces/dist/ddrhw-y-reversed-native --include-assemblies
```

The independent checks read actual saved traffic paths and indexed models. They cover all six journeys, twelve native endpoints, four proper rotations, 21 unique city-cell owners, elevated traffic with `UseElevation=1`, native joins, pavement support, full-width body depth, car clearance, closed road and barrier shells, 66 support prisms, and 39 slab contacts. Seven model-only cells have explicitly empty traffic paths. The car envelope is 2.5 m wide and 3.8 m high; this geometric strip does not model every long vehicle's overhang or animation.

A **donor pose** rotates an original NAM model inside the new component by a number of clockwise quarter turns: pose 0 means 0°, pose 1 means 90° clockwise, and pose 3 means 270° clockwise. Assembly placements use their separately labelled counterclockwise convention; the internal donor poses do not change the table's 0° component placements.

The reversed A/B diagonal helper is `57530200` at donor poses 0 and 3, with `57530900` peers. C uses `57530000` at pose 1. A/B native roof heights are nominal 15 m and 7.5 m; authored collars have floors at 14 m and 6.5 m, with finite steps to the middle datum. Every authored route centreline and the C underside through east coordinate 56 m remain checked. The strict native-source certificates distinguish literal inherited faces from authored ones and bind exact source, pose, material, UV coordinates, and winding. These scopes must be reported by the actual compiled verification; no original variant exception is inherited automatically.

### 3.2 Refresh exports, pictures, and the menu

After extraction, write only the three new reviewed connector declarations:

```sh
python3 -B - <<'PY'
from pathlib import Path
from scp_highway.connections import write_connector_groups
write_connector_groups(Path('custom-pieces'), [
    'ddrhw-y-reversed-diagonal-stem-split',
    'ddrhw-y-reversed-diagonal-branch',
    'ddrhw-y-reversed-orthogonal-core',
])
PY
```

In the next commands, replace `/path/to/SimCity 4/Plugins` with the existing folder containing your audited NAM pavement textures, and keep the quotation marks. The folder is read only. Refresh the exports and connector pictures, then check them:

```sh
python3 -B custom-pieces/scp.py connectors refresh --domain highway --piece ddrhw-y-reversed-diagonal-stem-split --piece ddrhw-y-reversed-diagonal-branch --piece ddrhw-y-reversed-orthogonal-core --build dist/ddrhw-y-reversed-native --plugins '/path/to/SimCity 4/Plugins'
python3 -B custom-pieces/scp.py connectors check --domain highway --piece ddrhw-y-reversed-diagonal-stem-split --piece ddrhw-y-reversed-diagonal-branch --piece ddrhw-y-reversed-orthogonal-core --build dist/ddrhw-y-reversed-native --plugins '/path/to/SimCity 4/Plugins'
python3 -B -m scp.preview --root custom-pieces --output custom-pieces/dist/ddrhw-y-reversed-native --plugins '/path/to/SimCity 4/Plugins' --catalog --views angled top --include ddrhw-y-reversed-diagonal-stem-split --include ddrhw-y-reversed-diagonal-branch --include ddrhw-y-reversed-orthogonal-core
python3 -B custom-pieces/domains/highway/tools/render_compact_assembly.py --build custom-pieces/dist/ddrhw-y-reversed-native --assembly ddrhw-compact-diagonal-y-junction-reversed --output-dir custom-pieces/local/review-workspaces/ddrhw-y-reversed-art --plugins '/path/to/SimCity 4/Plugins'
```

Inspect all six staged assembly pictures, then follow the [artwork promotion workflow](../../../../docs/WORKFLOW_DOCUMENTATION_GENERATION.md#7-assembly-picture-set-and-in-picture-identification) to promote their unchanged PNG bytes and portable provenance. The construction view must use 30% ownership fill, occupied-cell outlines, actual model projection outlines, and the same fixed city grid. Do not overwrite an earlier staging directory; choose an unused suffix when repeating a render.

After the guides, pictures, connector exports, and image-review bindings are current, compile a fresh normal selection and prepare a fresh assembly-menu candidate:

```sh
python3 -B custom-pieces/scp.py assembly-menu --domain highway --layout ddrhw-compact-diagonal-y-junction-reversed --source custom-pieces/dist/ddrhw-y-reversed-native --output custom-pieces/dist/ddrhw-y-reversed-menu
```

The separate button contains exactly three components. Tab and Shift+Tab change the selected component, and each click places only that component. Packaging and installing are separate actions.

### 3.3 Regressions and marking direction

Run:

```sh
python3 -B -m unittest discover -s custom-pieces/domains/highway/tests -p 'test_y_junction*.py' -v
python3 -B custom-pieces/scp.py docs-check
python3 -B tools/run_tests.py
```

Controls must reject missing floors, missing outerwalls, wrong native poses or texture coordinates, invalid ownership, changed routes, and unsupported construction states. A separate pixel audit reads actual pinned pavement textures and saved UV coordinates, and measures yellow relative to the directed lanes. Its accepted sample counts and exact limits belong in compiled evidence. Samples at route interiors and native ends do not prove continuous paint through every fork and merge. Proprietary-input tests report explicit skips when their inputs are absent; report those skips separately from passing native tests.

To reproduce the marking audit from your verified three-piece build, first extract the unchanged saved model and PATH bytes. The following command creates a new ignored local folder. If that folder already exists, choose an unused suffix and change the later `--saved` and `--output` paths to match:

```sh
python3 -B - <<'PY'
from pathlib import Path
import json
import sys
root = Path('custom-pieces').resolve()
sys.path.insert(0, str(root / 'framework'))
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0, SourcePackages(root))
from scp.track_paths import S3D, PATH
from scp.verify import strict_dbpf
build = root / 'dist/ddrhw-y-reversed-native'
destination = root / 'local/review-workspaces/ddrhw-y-reversed-marking-01'
manifest = json.loads((build / 'manifest.json').read_text())
expected = {
    'ddrhw-y-reversed-diagonal-stem-split',
    'ddrhw-y-reversed-diagonal-branch',
    'ddrhw-y-reversed-orthogonal-core',
}
if len(manifest['pieces']) != 3 or {p['id'] for p in manifest['pieces']} != expected:
    raise ValueError('Use the exact verified three-piece reversed build')
destination.mkdir(parents=True, exist_ok=False)
for piece in manifest['pieces']:
    resources = strict_dbpf((build / piece['asset_file']).read_bytes())
    directory = destination / piece['id']
    directory.mkdir()
    for cell, tile in zip(piece['cells'], piece['tile_ids']):
        for extension, kind in (('s3d', S3D), ('path', PATH)):
            raw = resources[(*kind, int(tile, 16))]
            (directory / f'{cell[0]}-{cell[1]}.{extension}').write_bytes(raw)
print('Extracted 21 saved models and 21 saved PATHs.')
PY
```

Run the maintained independent reader against those files. Replace the quoted texture-folder placeholder as in section 3.2. `--native-build` supplies the build's recorded pinned native archive, and the reader checks both real texture pixels and directed saved lanes:

```sh
python3 -B custom-pieces/domains/highway/tools/verify_y_junction_markings.py --saved custom-pieces/local/review-workspaces/ddrhw-y-reversed-marking-01 --native-build custom-pieces/dist/ddrhw-y-reversed-native --plugins '/path/to/SimCity 4/Plugins' --output custom-pieces/local/review-workspaces/ddrhw-y-reversed-marking-01/marking-audit.jsonc
```

## 4. Game checks

1. Open **Transportation → Highways → SCP → Assemblies**, and select **SCP | ASSEMBLY | DD RHW-4 — Compact Y-Junction — Diagonal Stem — Reversed Traffic**. Confirm Tab cycles P01→P02→P03, Shift+Tab reverses the cycle, and the original Y's button still works.
2. Follow the [exact placement table](README.md#3-placements). Inspect the sparse owned shapes, P02's unowned reference, both decks, all native sockets, textures, barriers, and supports. Check yellow on the driver's left on every travel deck.
3. Check automatic ordinary native-tile appearance, outward native dragging, and connection to prebuilt matching DD approaches separately at A, B, and C. Leave the staggered neighbouring native cells available.
4. Supply demand from all arms. Check A→B, B→A, A→C, C→A, B→C, and C→B separately with Route Query and an actual moving car. Verify the deck changes, both descents, one lane per journey, and absence of U-turns or unintended transfers.
5. Inspect every zoom and camera orientation, redraw adjacent native highways, demolish and replace one component, save, exit, reload, and repeat the six journeys. Check other proper rotations separately. Record exact observations in the generated cases below.

## 5. Results and known issues

On **4 November 2026**, Simon confirmed that the assembly rendered correctly in SimCity 4. He also confirmed that Route Query and visible traffic passed for all six permitted directions between the three arms. The [test checklist](#test-checklist) records the thirteen passes under its reference-layout cases. Simon did not specify a separate rotation.

The first normal three-DAT build passes its saved-resource checks. All 21 canonical model/PATH pairs exactly match the independently accepted saved snapshot, and all five zoom models match their corresponding checked model bytes. The [compiled verification](evidence/compiled-verification.jsonc) binds the actual archives, source fingerprints, ownership, and marking evidence. Packaging and installation are separate later captures. No human pass of this reversed variant's six complete journeys is recorded.

The [current definition bridge](evidence/definition-bridge-02.jsonc) verifies the corrected clockwise donor-pose terminology in a fresh current-source build. All three complete DAT byte sequences remain identical to the first checked build. This metadata correction changes no model, traffic path, component placement, or native donor pose.

Complete [physical verification](evidence/physical-verification.jsonc) passes 166,869 actual saved triangles, all six journeys, twelve native endpoints, four proper rotations, 4,995 authored-only vehicle-spine segments, 32 native vehicle segments, 66 support prisms, and 39 slab contacts. All 15,919 full-width underside patches pass; the largest admitted true three-dimensional distance is 3.992189 µm, below the unchanged 4 µm limit. A micrometre, or µm, is one millionth of a metre. The finite-floor reader includes actual edge-contact triangles and retains every positive patch for a bounded geometric proof. It rejects the old 4.0638 µm thin-body witness, a 9 µm floor hole, a raised floor, an unrelated triangle plane, and a substituted native reference floor.

The new A/B helper-body skin scope requires actual saved roof and authored-floor coverage over all 24 removed finite wall footprints, including their shoulder portions outside the vehicle strips. Removing three real outerwall triangles still fails closure while the source certificates and all 24 burial proofs remain valid. The C closure proof includes only already-rendered, source-certified native pavement and barrier fragments in the finite east interval 55.99899959564209–56 m and north interval −8–8 m; it supplies zero native body reference faces. Every authored C underside remains required through east coordinate 56 m. The [native interface certificate](evidence/native-owned-interface-verification.jsonc) records the exact parents, pose, materials, UV coordinates, winding, and intrinsic native roof-under-own-barrier trim. Literal source-certified south-fringe faces retain their separate bounded native-only external-skin scope. No original borrowed-spine or shallow-peer-floor allowance is transferred.

All six canonical assembly pictures are rendered from the checked DATs and inspected for complete models, correct cameras, readable names, fixed coordinates, ownership colours, 30% fills, and actual model outlines. [Compiled render provenance](evidence/compiled-render-paint-join-20261104.jsonc) binds their unchanged promoted PNG bytes. This software presentation review records no human image approval or game observation.

The final focused Y suite passes **99 tests with zero skips** against the configured native inputs. The three reversed connector exports and all 13 boundary cards pass their data and artwork freshness checks: 22 service groups and 28 directed ports. The original three connector exports are also current, while their three card images, canonical pictures, icons, manual records, and accepted contracts remain byte-identical.

The required full repository command passes all four suites. The [software verification receipt](evidence/software-verification.jsonc) records **2,301 reported tests and 95 explicit skips**, plus the separate configured 99-test native Y sweep and 53 passing installer-service tests. The full run uses an immutable maintained-source copy without private game inputs or staged builds; skipped native cases remain unverified. The documentation check passes 201 documents and 28,888 local links, retaining 152 legacy subject layouts. A first run found one outdated capability-test expectation; the corrected final full run passes.

The [final development package receipt](evidence/final-development-package.jsonc) identifies the fresh normal build, single-button assembly menu, binary ZIP, and source ZIP. The [independent archive audit](evidence/archive-verification.jsonc) passes the exact five installable DATs, one three-member cycle, documentation and artwork closure, archive integrity, and private-input exclusions. These archives are frozen pre-install captures; the later deployment record is separate.

On **3 November 2026**, the [additive installation and independent post-install audit](evidence/additive-installation-20261103.jsonc) confirm that the three new component DATs reached the active managed Plugins folder. The shared menu and controller were updated, and all **228 existing piece DATs retained their bytes, file identities, sizes, and modification times**. The installed selection now contains 231 types. All 664 existing menu payloads and their cycles remain intact, with four new payloads for the separate reversed assembly button. RUL1 and NetworkINI remain byte-identical, and a complete external rollback backup is verified. The private transaction and parser regression suite passes 20 tests with zero skips. That installation capture supplies no human game observation; restart the game before testing fresh placements.

Later on **3 November 2026**, the user reported a deep terrain hole when the mirrored DD-to-L0 transition is placed close enough to connect beside a diagonal arm of this junction. The right-hand straight arm reportedly works, as does placing farther away and then connecting manually. See the transition's [bounded close-placement failure report and screenshot](../../00_pieces/ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile-mirrored/evidence/game-close-placement-20261103.jsonc), [known-issue discussion](../../00_pieces/ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile-mirrored/TESTING.md#5-results-and-known-issues), and [three retest controls](../../00_pieces/ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile-mirrored/TESTING.md#44-close-placement-terrain-regression). Which diagonal arm failed, the rotation, separation, and terrain conditions remain unspecified. The mirrored transition has a confirmed missing construction-height constraint, but its causal role in the pictured failure is inferred and the runtime correction remains unverified.

The [original preservation control](evidence/original-dat-preservation.jsonc) passes: a fresh original three-piece build produces exactly the same three complete DAT byte sequences as the accepted original package. This checks preservation of the working original independently of the new variant's model acceptance.

The [saved marking audit](evidence/saved-marking-verification-02.jsonc) passes 85 sampled yellow positions: 67 single-lane ramp cross-sections across all six journeys and 18 native cross-sections across all six arm/deck ends. Yellow is on the driver's left in every accepted sample and clears both native lane centres. The two deliberately reversed texture-coordinate controls are rejected. All 42 saved model/PATH fingerprints are bound to the report. The saved marking audit samples stripe orientation. Complete paint continuity through forks, merges, shoulder tapers, and material transitions was outside the scope of that audit. The maintained reader is [verify_y_junction_markings.py](../../tools/verify_y_junction_markings.py). The earlier [candidate 01 marking capture](evidence/saved-marking-verification-01.jsonc) remains frozen; candidate 02 retains small nonzero city-cut fragments that the first model omitted, with unchanged yellow positions and unchanged traffic paths.

The verified revised DATs align the outer yellow and white lines at all six sampled reversed arm and deck joins. The 6 m blend carries each stripe from the DD fan into the single-lane texture field and limits the white line position to the available asphalt. The revision retains the gap between native centre dashes at the handoff and preserves the traffic path bytes and native model joins. The earlier driver-left marking audit remains a record of its own saved capture. See the [saved DAT verification](evidence/paint-join-verification-20261104.jsonc) and the [shared marking contract](../../NETWORK_SPEC.md#173-paint-alignment-at-the-dd-to-mis-joins).

The DD-to-MIS material transition can show a tone seam. The two links remain intentionally steep compact game geometry; these checks do not establish structural engineering capacity or traffic capacity. Custom cast shadows are disabled, native automatic placement is experimental, and reflected or second-alignment layouts are outside this variant. The original installed Y's general “works” report does not cover this counterpart.

The mirrored transition's later [controller-only terrain correction](../../00_pieces/ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile-mirrored/evidence/terrain-correction-installation-20261103.jsonc) is installed and independently audited. It preserves this assembly's models, traffic paths, native helpers, and construction rules, along with all existing piece DATs. Its effect on the reported close-diagonal excavation still requires the [three fresh-placement controls](../../00_pieces/ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile-mirrored/TESTING.md#44-close-placement-terrain-regression).

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Human game checks are required only at 0° CCW. Supported construction orientations and software rotation checks retain their separate scope; these human cases do not establish observations at the other orientations.

Current totals: unverified: 41, passed: 13, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/01_assemblies/ddrhw-compact-diagonal-y-junction-reversed/checks/manual-tests.json --observation custom-pieces/domains/highway/01_assemblies/ddrhw-compact-diagonal-y-junction-reversed/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-a0045479dcaf4b437fc5">[ ] unverified</a> | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-a0045479dcaf4b437fc5"></a>

**General: unverified** — `software_resources-a0045479dcaf4b437fc5`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-a0045479dcaf4b437fc5">[ ] unverified</a> | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-a0045479dcaf4b437fc5"></a>

**General: unverified** — `software_connectivity-a0045479dcaf4b437fc5`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-1eddce0b9ae85ad884c7">[x] passed</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-1eddce0b9ae85ad884c7"></a>

**0° CCW: passed** — `in_game_render-1eddce0b9ae85ad884c7`.

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
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-1eddce0b9ae85ad884c7">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-1eddce0b9ae85ad884c7"></a>

**0° CCW: unverified** — `in_game_placement-1eddce0b9ae85ad884c7`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-1eddce0b9ae85ad884c7">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-1eddce0b9ae85ad884c7"></a>

**0° CCW: unverified** — `in_game_demolition-1eddce0b9ae85ad884c7`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-1eddce0b9ae85ad884c7">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-1eddce0b9ae85ad884c7"></a>

**0° CCW: unverified** — `in_game_save_reload-1eddce0b9ae85ad884c7`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 6 cases; passed: 6</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: external-10>external-2; entry: external-10; exit: external-2 | — | <a href="#case-in_game_route_query-ed6697a6188f6d8fe31e">[x] passed</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-12>external-7; entry: external-12; exit: external-7 | — | <a href="#case-in_game_route_query-6975b9e0a8028159ad14">[x] passed</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-1>external-9; entry: external-1; exit: external-9 | — | <a href="#case-in_game_route_query-d8a66df811018497e13a">[x] passed</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-3>external-5; entry: external-3; exit: external-5 | — | <a href="#case-in_game_route_query-1a2cdc3a3552f2e342c8">[x] passed</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-6>external-4; entry: external-6; exit: external-4 | — | <a href="#case-in_game_route_query-2a2a2c6c876befa9fdc4">[x] passed</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-8>external-11; entry: external-8; exit: external-11 | — | <a href="#case-in_game_route_query-5ace0d9ea2329ac06ba1">[x] passed</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: external-10>external-2; entry: external-10; exit: external-2</summary>

<a id="case-in_game_route_query-ed6697a6188f6d8fe31e"></a>

**0° CCW: passed** — `in_game_route_query-ed6697a6188f6d8fe31e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-10>external-2; entry: external-10; exit: external-2.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-04; evidence: [Simon reported “now update the tests for our DD RHW junction: render, path, and traffic render all pass”., Simon confirmed “Both the original and reversed-traffic versions”., When asked about Route Query and visible traffic in all six directions, Simon confirmed “Yes, all six directions for both checks”., The installed component DATs and construction rules match this record’s resource fingerprints.]; environment: platform: Windows SimCity 4 through Wine on macOS (current installed test setup); game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50, right-hand traffic; installed manifest sha256: 8d962d444d76d0f122e516f4b63793399f7d09ffb093983731f282638d086288; note: Recorded in this assembly’s reference-layout cases. The user confirmed rendering and all six permitted journeys for both Route Query and visible traffic. No separate rotation was reported.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-12>external-7; entry: external-12; exit: external-7</summary>

<a id="case-in_game_route_query-6975b9e0a8028159ad14"></a>

**0° CCW: passed** — `in_game_route_query-6975b9e0a8028159ad14`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-12>external-7; entry: external-12; exit: external-7.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-04; evidence: [Simon reported “now update the tests for our DD RHW junction: render, path, and traffic render all pass”., Simon confirmed “Both the original and reversed-traffic versions”., When asked about Route Query and visible traffic in all six directions, Simon confirmed “Yes, all six directions for both checks”., The installed component DATs and construction rules match this record’s resource fingerprints.]; environment: platform: Windows SimCity 4 through Wine on macOS (current installed test setup); game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50, right-hand traffic; installed manifest sha256: 8d962d444d76d0f122e516f4b63793399f7d09ffb093983731f282638d086288; note: Recorded in this assembly’s reference-layout cases. The user confirmed rendering and all six permitted journeys for both Route Query and visible traffic. No separate rotation was reported.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-1>external-9; entry: external-1; exit: external-9</summary>

<a id="case-in_game_route_query-d8a66df811018497e13a"></a>

**0° CCW: passed** — `in_game_route_query-d8a66df811018497e13a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-1>external-9; entry: external-1; exit: external-9.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-04; evidence: [Simon reported “now update the tests for our DD RHW junction: render, path, and traffic render all pass”., Simon confirmed “Both the original and reversed-traffic versions”., When asked about Route Query and visible traffic in all six directions, Simon confirmed “Yes, all six directions for both checks”., The installed component DATs and construction rules match this record’s resource fingerprints.]; environment: platform: Windows SimCity 4 through Wine on macOS (current installed test setup); game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50, right-hand traffic; installed manifest sha256: 8d962d444d76d0f122e516f4b63793399f7d09ffb093983731f282638d086288; note: Recorded in this assembly’s reference-layout cases. The user confirmed rendering and all six permitted journeys for both Route Query and visible traffic. No separate rotation was reported.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-3>external-5; entry: external-3; exit: external-5</summary>

<a id="case-in_game_route_query-1a2cdc3a3552f2e342c8"></a>

**0° CCW: passed** — `in_game_route_query-1a2cdc3a3552f2e342c8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-3>external-5; entry: external-3; exit: external-5.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-04; evidence: [Simon reported “now update the tests for our DD RHW junction: render, path, and traffic render all pass”., Simon confirmed “Both the original and reversed-traffic versions”., When asked about Route Query and visible traffic in all six directions, Simon confirmed “Yes, all six directions for both checks”., The installed component DATs and construction rules match this record’s resource fingerprints.]; environment: platform: Windows SimCity 4 through Wine on macOS (current installed test setup); game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50, right-hand traffic; installed manifest sha256: 8d962d444d76d0f122e516f4b63793399f7d09ffb093983731f282638d086288; note: Recorded in this assembly’s reference-layout cases. The user confirmed rendering and all six permitted journeys for both Route Query and visible traffic. No separate rotation was reported.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-6>external-4; entry: external-6; exit: external-4</summary>

<a id="case-in_game_route_query-2a2a2c6c876befa9fdc4"></a>

**0° CCW: passed** — `in_game_route_query-2a2a2c6c876befa9fdc4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-6>external-4; entry: external-6; exit: external-4.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-04; evidence: [Simon reported “now update the tests for our DD RHW junction: render, path, and traffic render all pass”., Simon confirmed “Both the original and reversed-traffic versions”., When asked about Route Query and visible traffic in all six directions, Simon confirmed “Yes, all six directions for both checks”., The installed component DATs and construction rules match this record’s resource fingerprints.]; environment: platform: Windows SimCity 4 through Wine on macOS (current installed test setup); game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50, right-hand traffic; installed manifest sha256: 8d962d444d76d0f122e516f4b63793399f7d09ffb093983731f282638d086288; note: Recorded in this assembly’s reference-layout cases. The user confirmed rendering and all six permitted journeys for both Route Query and visible traffic. No separate rotation was reported.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-8>external-11; entry: external-8; exit: external-11</summary>

<a id="case-in_game_route_query-5ace0d9ea2329ac06ba1"></a>

**0° CCW: passed** — `in_game_route_query-5ace0d9ea2329ac06ba1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-8>external-11; entry: external-8; exit: external-11.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-04; evidence: [Simon reported “now update the tests for our DD RHW junction: render, path, and traffic render all pass”., Simon confirmed “Both the original and reversed-traffic versions”., When asked about Route Query and visible traffic in all six directions, Simon confirmed “Yes, all six directions for both checks”., The installed component DATs and construction rules match this record’s resource fingerprints.]; environment: platform: Windows SimCity 4 through Wine on macOS (current installed test setup); game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50, right-hand traffic; installed manifest sha256: 8d962d444d76d0f122e516f4b63793399f7d09ffb093983731f282638d086288; note: Recorded in this assembly’s reference-layout cases. The user confirmed rendering and all six permitted journeys for both Route Query and visible traffic. No separate rotation was reported.

</details>

</details>

<details>
<summary>Visible travel — road — 6 cases; passed: 6</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: external-10>external-2; entry: external-10; exit: external-2 | — | <a href="#case-in_game_visible_travel-ed6697a6188f6d8fe31e">[x] passed</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-12>external-7; entry: external-12; exit: external-7 | — | <a href="#case-in_game_visible_travel-6975b9e0a8028159ad14">[x] passed</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-1>external-9; entry: external-1; exit: external-9 | — | <a href="#case-in_game_visible_travel-d8a66df811018497e13a">[x] passed</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-3>external-5; entry: external-3; exit: external-5 | — | <a href="#case-in_game_visible_travel-1a2cdc3a3552f2e342c8">[x] passed</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-6>external-4; entry: external-6; exit: external-4 | — | <a href="#case-in_game_visible_travel-2a2a2c6c876befa9fdc4">[x] passed</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-8>external-11; entry: external-8; exit: external-11 | — | <a href="#case-in_game_visible_travel-5ace0d9ea2329ac06ba1">[x] passed</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-10>external-2; entry: external-10; exit: external-2</summary>

<a id="case-in_game_visible_travel-ed6697a6188f6d8fe31e"></a>

**0° CCW: passed** — `in_game_visible_travel-ed6697a6188f6d8fe31e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-10>external-2; entry: external-10; exit: external-2.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-04; evidence: [Simon reported “now update the tests for our DD RHW junction: render, path, and traffic render all pass”., Simon confirmed “Both the original and reversed-traffic versions”., When asked about Route Query and visible traffic in all six directions, Simon confirmed “Yes, all six directions for both checks”., The installed component DATs and construction rules match this record’s resource fingerprints.]; environment: platform: Windows SimCity 4 through Wine on macOS (current installed test setup); game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50, right-hand traffic; installed manifest sha256: 8d962d444d76d0f122e516f4b63793399f7d09ffb093983731f282638d086288; note: Recorded in this assembly’s reference-layout cases. The user confirmed rendering and all six permitted journeys for both Route Query and visible traffic. No separate rotation was reported.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-12>external-7; entry: external-12; exit: external-7</summary>

<a id="case-in_game_visible_travel-6975b9e0a8028159ad14"></a>

**0° CCW: passed** — `in_game_visible_travel-6975b9e0a8028159ad14`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-12>external-7; entry: external-12; exit: external-7.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-04; evidence: [Simon reported “now update the tests for our DD RHW junction: render, path, and traffic render all pass”., Simon confirmed “Both the original and reversed-traffic versions”., When asked about Route Query and visible traffic in all six directions, Simon confirmed “Yes, all six directions for both checks”., The installed component DATs and construction rules match this record’s resource fingerprints.]; environment: platform: Windows SimCity 4 through Wine on macOS (current installed test setup); game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50, right-hand traffic; installed manifest sha256: 8d962d444d76d0f122e516f4b63793399f7d09ffb093983731f282638d086288; note: Recorded in this assembly’s reference-layout cases. The user confirmed rendering and all six permitted journeys for both Route Query and visible traffic. No separate rotation was reported.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-1>external-9; entry: external-1; exit: external-9</summary>

<a id="case-in_game_visible_travel-d8a66df811018497e13a"></a>

**0° CCW: passed** — `in_game_visible_travel-d8a66df811018497e13a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-1>external-9; entry: external-1; exit: external-9.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-04; evidence: [Simon reported “now update the tests for our DD RHW junction: render, path, and traffic render all pass”., Simon confirmed “Both the original and reversed-traffic versions”., When asked about Route Query and visible traffic in all six directions, Simon confirmed “Yes, all six directions for both checks”., The installed component DATs and construction rules match this record’s resource fingerprints.]; environment: platform: Windows SimCity 4 through Wine on macOS (current installed test setup); game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50, right-hand traffic; installed manifest sha256: 8d962d444d76d0f122e516f4b63793399f7d09ffb093983731f282638d086288; note: Recorded in this assembly’s reference-layout cases. The user confirmed rendering and all six permitted journeys for both Route Query and visible traffic. No separate rotation was reported.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-3>external-5; entry: external-3; exit: external-5</summary>

<a id="case-in_game_visible_travel-1a2cdc3a3552f2e342c8"></a>

**0° CCW: passed** — `in_game_visible_travel-1a2cdc3a3552f2e342c8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-3>external-5; entry: external-3; exit: external-5.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-04; evidence: [Simon reported “now update the tests for our DD RHW junction: render, path, and traffic render all pass”., Simon confirmed “Both the original and reversed-traffic versions”., When asked about Route Query and visible traffic in all six directions, Simon confirmed “Yes, all six directions for both checks”., The installed component DATs and construction rules match this record’s resource fingerprints.]; environment: platform: Windows SimCity 4 through Wine on macOS (current installed test setup); game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50, right-hand traffic; installed manifest sha256: 8d962d444d76d0f122e516f4b63793399f7d09ffb093983731f282638d086288; note: Recorded in this assembly’s reference-layout cases. The user confirmed rendering and all six permitted journeys for both Route Query and visible traffic. No separate rotation was reported.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-6>external-4; entry: external-6; exit: external-4</summary>

<a id="case-in_game_visible_travel-2a2a2c6c876befa9fdc4"></a>

**0° CCW: passed** — `in_game_visible_travel-2a2a2c6c876befa9fdc4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-6>external-4; entry: external-6; exit: external-4.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-04; evidence: [Simon reported “now update the tests for our DD RHW junction: render, path, and traffic render all pass”., Simon confirmed “Both the original and reversed-traffic versions”., When asked about Route Query and visible traffic in all six directions, Simon confirmed “Yes, all six directions for both checks”., The installed component DATs and construction rules match this record’s resource fingerprints.]; environment: platform: Windows SimCity 4 through Wine on macOS (current installed test setup); game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50, right-hand traffic; installed manifest sha256: 8d962d444d76d0f122e516f4b63793399f7d09ffb093983731f282638d086288; note: Recorded in this assembly’s reference-layout cases. The user confirmed rendering and all six permitted journeys for both Route Query and visible traffic. No separate rotation was reported.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-8>external-11; entry: external-8; exit: external-11</summary>

<a id="case-in_game_visible_travel-5ace0d9ea2329ac06ba1"></a>

**0° CCW: passed** — `in_game_visible_travel-5ace0d9ea2329ac06ba1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-8>external-11; entry: external-8; exit: external-11.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: Simon (user); confirmed at: 2026-11-04; evidence: [Simon reported “now update the tests for our DD RHW junction: render, path, and traffic render all pass”., Simon confirmed “Both the original and reversed-traffic versions”., When asked about Route Query and visible traffic in all six directions, Simon confirmed “Yes, all six directions for both checks”., The installed component DATs and construction rules match this record’s resource fingerprints.]; environment: platform: Windows SimCity 4 through Wine on macOS (current installed test setup); game version: SimCity 4 Deluxe 1.1.641 (Windows); nam profile: NAM 50, right-hand traffic; installed manifest sha256: 8d962d444d76d0f122e516f4b63793399f7d09ffb093983731f282638d086288; note: Recorded in this assembly’s reference-layout cases. The user confirmed rendering and all six permitted journeys for both Route Query and visible traffic. No separate rotation was reported.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 30 cases; unverified: 30</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Forbidden transfer**<br>from port: external-1; to port: external-2; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-2f83c4e48ededb78f622">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-1; to port: external-4; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-db97304c4ca44135b89e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-1; to port: external-5; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-e78a608055f9740a9eb3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-1; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ef9418f7cf3504e8495d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-1; to port: external-11; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-8a9e38685a53189cec04">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-3; to port: external-2; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ab9563f3678c208c59c0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-3; to port: external-4; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-7c78354135f7f82c6ff2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-3; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f05ee6a992d161f6221a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-3; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-775461730fb0320b7551">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-3; to port: external-11; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-21f0af52fa38ac599df5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-2; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-354f50d5fea62fff400a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-5; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-04db0894dd5d861747e0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-19ced577cedd85227b3a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-badd8cd070c2dd575a25">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-11; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-feb29abc0175d7339a97">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-8; to port: external-2; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f56e7ad8bc073217ae55">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-8; to port: external-4; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ae056abfbc2304ecf62e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-8; to port: external-5; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-feaa3d0cb98512f3ecf3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-8; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-38bda43d0ca7c349dc2f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-8; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-8e9d08b139bb4ecd061c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-10; to port: external-4; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-769623c9f01ca95cceea">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-10; to port: external-5; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-82c75dbf8c3f7dc8e190">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-10; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-fdcc5be28a1bb3cfd543">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-10; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-705f63bbf795196a35bf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-10; to port: external-11; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-cdc4505b6d31cd4005e0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-2; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ae4212e277ae316758e4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-4; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-876d1ac7e53bc6e82963">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-5; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-8cb8dbeb79827efa2f4e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-0c54f40751b6b87bf998">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-12; to port: external-11; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-9ac60b007bece4aac7eb">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: external-1; to port: external-2; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-2f83c4e48ededb78f622"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2f83c4e48ededb78f622`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-1; to port: external-2; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-1; to port: external-4; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-db97304c4ca44135b89e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-db97304c4ca44135b89e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-1; to port: external-4; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-1; to port: external-5; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-e78a608055f9740a9eb3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e78a608055f9740a9eb3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-1; to port: external-5; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-1; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ef9418f7cf3504e8495d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ef9418f7cf3504e8495d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-1; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-1; to port: external-11; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-8a9e38685a53189cec04"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8a9e38685a53189cec04`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-1; to port: external-11; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-3; to port: external-2; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ab9563f3678c208c59c0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ab9563f3678c208c59c0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-3; to port: external-2; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-3; to port: external-4; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-7c78354135f7f82c6ff2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7c78354135f7f82c6ff2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-3; to port: external-4; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-3; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f05ee6a992d161f6221a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f05ee6a992d161f6221a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-3; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-3; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-775461730fb0320b7551"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-775461730fb0320b7551`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-3; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-3; to port: external-11; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-21f0af52fa38ac599df5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-21f0af52fa38ac599df5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-3; to port: external-11; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-2; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-354f50d5fea62fff400a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-354f50d5fea62fff400a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-2; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-5; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-04db0894dd5d861747e0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-04db0894dd5d861747e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-5; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-19ced577cedd85227b3a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-19ced577cedd85227b3a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-badd8cd070c2dd575a25"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-badd8cd070c2dd575a25`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-11; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-feb29abc0175d7339a97"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-feb29abc0175d7339a97`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-11; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-8; to port: external-2; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f56e7ad8bc073217ae55"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f56e7ad8bc073217ae55`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-8; to port: external-2; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-8; to port: external-4; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ae056abfbc2304ecf62e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ae056abfbc2304ecf62e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-8; to port: external-4; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-8; to port: external-5; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-feaa3d0cb98512f3ecf3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-feaa3d0cb98512f3ecf3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-8; to port: external-5; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-8; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-38bda43d0ca7c349dc2f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-38bda43d0ca7c349dc2f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-8; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-8; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-8e9d08b139bb4ecd061c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8e9d08b139bb4ecd061c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-8; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-10; to port: external-4; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-769623c9f01ca95cceea"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-769623c9f01ca95cceea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-10; to port: external-4; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-10; to port: external-5; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-82c75dbf8c3f7dc8e190"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-82c75dbf8c3f7dc8e190`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-10; to port: external-5; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-10; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-fdcc5be28a1bb3cfd543"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fdcc5be28a1bb3cfd543`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-10; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-10; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-705f63bbf795196a35bf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-705f63bbf795196a35bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-10; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-10; to port: external-11; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-cdc4505b6d31cd4005e0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cdc4505b6d31cd4005e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-10; to port: external-11; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-2; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ae4212e277ae316758e4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ae4212e277ae316758e4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-2; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-4; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-876d1ac7e53bc6e82963"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-876d1ac7e53bc6e82963`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-4; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-5; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-8cb8dbeb79827efa2f4e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8cb8dbeb79827efa2f4e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-5; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-0c54f40751b6b87bf998"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0c54f40751b6b87bf998`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-12; to port: external-11; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-9ac60b007bece4aac7eb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9ac60b007bece4aac7eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-12; to port: external-11; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 6 cases; unverified: 6</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-compact-diagonal-y-junction-reversed:clean-southeast | <a href="#case-preview_review-3ceae587e3496164e28a">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-compact-diagonal-y-junction-reversed:clean-top | <a href="#case-preview_review-f226ad626a053a908cfb">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-compact-diagonal-y-junction-reversed:named-northwest | <a href="#case-preview_review-e302955743c37796c422">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-compact-diagonal-y-junction-reversed:named-southeast | <a href="#case-preview_review-48cf1916dea5243a75a0">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-compact-diagonal-y-junction-reversed:named-top | <a href="#case-preview_review-a49a33506a5623207d49">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-compact-diagonal-y-junction-reversed:tile-ownership | <a href="#case-preview_review-7c0b6837a9beaf6db064">[ ] unverified</a> | — |


<details>
<summary>Preview review — Image: image:ddrhw-compact-diagonal-y-junction-reversed:clean-southeast</summary>

<a id="case-preview_review-3ceae587e3496164e28a"></a>

**General: unverified** — `preview_review-3ceae587e3496164e28a`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-compact-diagonal-y-junction-reversed:clean-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-compact-diagonal-y-junction-reversed:clean-top</summary>

<a id="case-preview_review-f226ad626a053a908cfb"></a>

**General: unverified** — `preview_review-f226ad626a053a908cfb`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-compact-diagonal-y-junction-reversed:clean-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-compact-diagonal-y-junction-reversed:named-northwest</summary>

<a id="case-preview_review-e302955743c37796c422"></a>

**General: unverified** — `preview_review-e302955743c37796c422`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-compact-diagonal-y-junction-reversed:named-northwest.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-compact-diagonal-y-junction-reversed:named-southeast</summary>

<a id="case-preview_review-48cf1916dea5243a75a0"></a>

**General: unverified** — `preview_review-48cf1916dea5243a75a0`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-compact-diagonal-y-junction-reversed:named-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-compact-diagonal-y-junction-reversed:named-top</summary>

<a id="case-preview_review-a49a33506a5623207d49"></a>

**General: unverified** — `preview_review-a49a33506a5623207d49`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-compact-diagonal-y-junction-reversed:named-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-compact-diagonal-y-junction-reversed:tile-ownership</summary>

<a id="case-preview_review-7c0b6837a9beaf6db064"></a>

**General: unverified** — `preview_review-7c0b6837a9beaf6db064`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-compact-diagonal-y-junction-reversed:tile-ownership.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The user requested another variant with yellow on the opposite physical side and clarified that yellow must remain on the driver's left. This implementation reverses all directed journeys at the original arm positions and uses a separate native phase, component identities, and menu cycle. The original junction and its human observations remain separate.

Follow the [shared observation procedure](../../../../docs/TESTING.md). Copy the exact case ID, record the installed candidate, pose, environment, and evidence, and describe the behavior actually observed. Software renders, saved-resource checks, and filesystem installation do not mark a human game case as passed.
