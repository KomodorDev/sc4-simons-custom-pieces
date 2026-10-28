---
title: "Straight-stem HSR trumpet: testing"
summary: "Define the trumpet’s test scope, setup, software checks, game checks, results, known issues, and design history."
audience: "Testers, assembly authors, and maintainers"
document_type: "reference"
---

# Straight-stem HSR trumpet: testing

<!-- ASSEMBLY TESTING LAYOUT: 1 -->

[Assembly overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

### Connection checks

The [README](README.md) is the assembly overview: pictures, required piece types, exact placements, and a summary matrix of external connections. This document holds the test procedure, exact cases, observations, failures, and engineering decisions. The chapter order follows the shared [assembly TESTING layout](../../../../docs/WORKFLOW_DOCUMENTATION_GENERATION.md#required-assembly-testing-layout).

A **port** is an entrance to or exit from the assembly. Each matrix row is an entrance, and each column is an exit. The axis labels identify the network service as well as the approach, so an HSR port remains distinct from any future passenger, ground-rail, or other network port at the same approach. West, East, and South name the approaches in the README's north-up plan. West → East and East → West are separate cells and separate directed journeys.

**Game appearance** has one overall status above the matrix. A person inspects the complete placed assembly in the game for missing rails, broken decks, incorrect walls, pillars, and shadows. Generated preview pictures do not establish an in-game appearance pass.

Each permitted connection has three separate checks:

1. **Saved PATH:** software can follow the train routes encoded in the saved game resources from this entrance to this exit. A PATH is a resource that describes permitted vehicle movement. A software pass establishes this routing result; it does not establish what the game displays or simulates.
2. **Route Query:** the game's Route Query tool shows traffic following the specific entrance-to-exit connection. Record the direction, environment, and evidence separately from visible train travel.
3. **Visible train travel:** a person has watched a train travel through the specific entrance-to-exit connection in the game. A Route Query line alone does not satisfy this check. Record the direction, environment, and evidence for the observed train.

The README uses **✅** for a current pass, **❌** for a current failure, and **?** when a current result has not been established. Open its status links for exact evidence, failures, stale results, or missing coverage. A **stale** observation belongs to inputs that have since changed and therefore cannot establish the current result. A forbidden connection is an intentionally prohibited journey; its separate in-game check confirms that the game prevents that travel. The matrix summarizes evidence; it does not discover compatible neighbouring pieces.

Manual game checks use the north-up test layout shown in the README. **0°** identifies that reference orientation in the record; the test plan does not require rebuilding and retesting the whole assembly at 90°, 180°, and 270°. Individual pieces still use the placement table's specified rotations. The independent software checks retain the supported construction rotations and their existing routing requirements.

There is one Route Query case and one visible-travel case for each of the six permitted directions, one whole-assembly appearance case, and one negative case for each of the three forbidden U-turns. Placement, demolition, and save/reload each have one case for the reference layout. The six layout-preview cases and the additional extraction-drawing review case stay separate from actual game appearance. Historical results retain their original scope; no result for a different direction, layout, or environment establishes a current pass.

Use the exact case links in the matrix and the [test checklist](#test-checklist) to record results. A pass covers only its recorded game environment, layout, and inputs. See [4. Game checks](#4-game-checks) for the procedure and [known issues](#known-issues) for the open demolition defect.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Human game checks use only 0° CCW; supported construction states and software rotation checks remain separate.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.json) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `W.in` | hsr / 7 / primary | in | [-120.0, -2.0, 15.5]; [1.0, -0.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `W.out` | hsr / 7 / primary | out | [-120.0, 2.0, 15.5]; [-1.0, -0.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `S.out` | hsr / 7 / primary | out | [-2.0, -216.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `S.in` | hsr / 7 / primary | in | [2.0, -216.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `E.out` | hsr / 7 / primary | out | [200.0, -2.0, 15.5]; [1.0, -0.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `E.in` | hsr / 7 / primary | in | [200.0, 2.0, 15.5]; [-1.0, -0.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `E.in` → `S.out` | primary |
| hsr | `E.in` → `W.out` | primary |
| hsr | `S.in` → `E.out` | primary |
| hsr | `S.in` → `W.out` | primary |
| hsr | `W.in` → `E.out` | primary |
| hsr | `W.in` → `S.out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| hsr / `W.in` | hsr / `W.out` | not reachable in the saved placed encoded-route graph |
| hsr / `S.in` | hsr / `S.out` | not reachable in the saved placed encoded-route graph |
| hsr / `E.in` | hsr / `E.out` | not reachable in the saved placed encoded-route graph |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

<a id="prepare-the-test-layout"></a>

## 2. Test setup

Use the README's [views](README.md#1-views), [piece list](README.md#2-pieces), and [placement table](README.md#3-placements) as the fixed reference. The following sequence prepares a repeatable test layout; it is not evidence that placement or travel has passed in the game.

### Before you start

Follow [Build and install](../../../../docs/BUILD_AND_INSTALL.md#prepare-the-assembly-menu) to prepare the matching one-button assembly candidate and local dependencies. The current whole-assembly input is the verified fourteen-type `custom-pieces/dist/trumpet-fan-core-parts-audit-01` build. The final parts and menu commands use `custom-pieces/dist/trumpet-fan-core-parts-final-01` and `custom-pieces/dist/trumpet-fan-core-menu-final-01`; consult the [package report](evidence/border-piece-integration-package.json) for the actual completed output hashes. Use the current repository README and TESTING documents for the 28-placement rebuild. Preparing or checking a candidate does not install it. Before a game trial, record its actual hashes, platform, game version, NAM profile, and disposable test city; historical reports do not supply a new run’s environment.

### Layout reference

Each city tile measures **16 × 16 m**. On the north-up plan, **X0–X19** increase east/right and **Y0–Y22** increase north/up. The central crossing stays at **(X7, Y13)**. The southwest tile centre is implicitly **(X0, Y0)**; no global origin marker appears. Standalone piece previews use their own local zero-based grid and authored 0° orientation.

The [placement plan](assembly.json) stores authoring positions in metres east and north, with **(0 m, 0 m)** at the central crossing. Its `coordinate_system.conversion` maps those positions to the displayed grid: **X = east metres / 16 + 7**, and **Y = north metres / 16 + 13**. For example, P01's `origin_m` of **(-96 m, 0 m)** becomes **(X1, Y13)**; the southwest tile centre at **(-112 m, -208 m)** becomes **(X0, Y0)**. These labels identify tile centres. Tile boundaries lie **8 m** to either side of a centre, so an external port on a boundary is not a tile-centre placement reference.

A **reference position** is a piece's software reference tile, which can be empty in a sparse piece. The table therefore describes exact model positions rather than certified mouse-click anchors. Align the entire cursor preview with the ownership plan. A rotation is **counterclockwise from the standalone 0° picture**: 270° counterclockwise equals 90° clockwise. Proper rotations turn the route and its direction together; they do not reverse a one-way track.

### Module interfaces

A **port** is a track entrance or exit. Its position, direction, height, deck width, and visible rails must agree with its neighbour. A **native end** accepts the stated ordinary track profile. A **custom curved end** requires its matching curved continuation; height alone is insufficient.

- P22 meets P01's ordinary west end. P01 meets P02 to the east and P03 at its custom branch. P03's ordinary south end meets P24, then P04's western one-way port.
- P04's eastern one-way port meets P25, then P10. P10's custom curved end meets P07. P07's ordinary east end meets P23, then P08. P09 completes the east approach.
- P15 meets P26, which owns the ordinary western approach at (X9, Y13). P26 meets P07's new ordinary west end at the boundary between (X9, Y13) and (X10, Y13); P07 owns only the four cells through (X13, Y13).
- P04's paired end meets P05, which rises from 15.5 m to 30.5 m and meets P13. P11 carries upper north/south HSR over lower east/west HSR without a level transfer.
- P12 and P16–P19 extend the upper stem. P20 and P21 join at 23 m. P21 descends through matching recessed-web straight P06A, then another copy P06B, into fan core P06. Its custom curved ends meet P07 and P08. The inherited native-curve web transition is separately closed and verified in the extraction audit; matching height alone is not a full-profile claim.

Each linked piece README lists its declared ports; these declarations do not establish complete compatibility with a neighbouring piece. The curves use their declared custom interfaces and the centred 8 m one-way profile at their southern ends.

### Placement sequence

Open **Transportation → Rail** and select **SCP | ASSEMBLY | HSR Trumpet** once. In the steps below, **select** means press **Tab** or **Shift+Tab** on that assembly button until the named component appears. Each click places that component; it does not stamp the complete assembly.

Use clear, flat terrain for the first game test and keep the full **20 × 23 tile** rectangle clear. A **cursor preview** is the complete shape attached to your pointer before you click. Press **Home** or **End** to rotate it; on keyboards without dedicated Home and End keys, check the keyboard mapping; some Mac keyboards use **Fn + ←** and **Fn + →**. Align all occupied tiles with the plan; reference positions are not certified click anchors.

1. Select **HSR Modular One-Tile Two-Level Crossing**. Place P11 at **(X7, Y13)**, 0°, with upper track north/south.
2. Select **HSR L4 Two-Track Straight** and place P12/P13 at **(X7, Y14)** and **(X7, Y12)**, both 0°. Select **HSR L2 Two-Track Straight**, rotate 270°, and place P14/P15 at **(X6, Y13)** and **(X8, Y13)**.
3. Place P05 **HSR Modular Two-Track L2 to L4 Climb** at **(X7, Y11)** and P04 **HSR Modular Symmetric Split and Return** at **(X6, Y5)**, both 0°. Match the climb's high end to P13 and its low end to P04.
4. Place upper straights P16–P19 at **(X7, Y15)** through **(X7, Y18)**, all 0°. Place P20 **HSR Tight Two-Track Corner 30.5 to 23 Metres** at **(X7, Y22)**, 0°, and P21 **HSR Tight Two-Track Corner 23 to 15.5 Metres** at **(X14, Y22)**, 270°.
5. Select **HSR Level 2 Paired Straight with Recessed Web**, and place P06A at **(X14, Y18)** and P06B at **(X14, Y17)**, both 0°. Select **HSR Level 2 Compact Paired Fan Core**, and place P06 at **(X12, Y16)**, 0°. Place the four-tile P07 **HSR L2 Short Opposed Merge Core** at **(X10, Y13)**, 0°. Select **HSR L2 Short Mainline Diverge Core**, rotate it to **180°**, and place P08 at **(X18, Y13)**. Match the complete paired profiles and both custom curved fan cuts to the picture.
6. Select **HSR L2 Two-Track Straight**, rotate 270°, and place **P26 (X9, Y13)**, **P23 (X14, Y13)**, and **P09 (X19, Y13)**. P26 supplies the western tile formerly included in P07; the remaining four P07 tiles keep their world positions. P08 already owns the four eastern core tiles; no separate straight is placed at (X15, Y13).
7. Place P01 **HSR L2 Short Mainline Diverge Core** at **(X1, Y13)**, 0°. Use the same paired straight at 270° for **P22 (X0, Y13)** and **P02 (X5, Y13)**.
8. Place P03 **HSR L2 Shortened One-Way Departure Curve** at **(X2, Y12)** and P10 **HSR L2 Shortened One-Way Return Curve** at **(X8, Y12)**, both 0°.
9. Select **One-Way HSR L2 Eight-Metre Straight**. Place **P24 (X6, Y6)** at **180°**, pointing south, and **P25 (X8, Y6)** at **0°**, pointing north. These complete the two connections between the curves and P04; select the same cycle component at the two specified rotations.
10. Extend compatible ordinary paired HSR beyond the west edge of X0, east edge of X19, and south edge of Y0. All three outside connections have their train path at **15.5 m**. Supply travel demand and test every journey below using separate Route Query and visible-train observations.

The selected pieces support proper **0°, 90°, 180°, and 270°** rotations in their construction rules. For this game test, use each placement at the rotation specified in the README. Keyboard response, cursor anchors, terrain behaviour, and actual train operation still require human observations. Plop & Paint does not stamp this complete blueprint.

### Directed routes under test

**Service:** HSR, using the game's Monorail traffic class. Each direction is a separate journey. P11 appears twice in South → West because that journey passes first above and later along the mainline; no transfer occurs inside the crossing.

| Journey | Placement sequence |
| --- | --- |
| West → East | P22 → P01 → P02 → P14 → P11 → P15 → P26 → P07 → P23 → P08 → P09 |
| East → West | P09 → P08 → P23 → P07 → P26 → P15 → P11 → P14 → P02 → P01 → P22 |
| West → South | P22 → P01 → P03 → P24 → P04 |
| South → East | P04 → P25 → P10 → P07 → P23 → P08 → P09 |
| South → West | P04 → P05 → P13 → P11 → P12 → P16 → P17 → P18 → P19 → P20 → P21 → P06A → P06B → P06 → P07 → P26 → P15 → P11 → P14 → P02 → P01 → P22 |
| East → South | P09 → P08 → P06 → P06B → P06A → P21 → P20 → P19 → P18 → P17 → P16 → P12 → P11 → P13 → P05 → P04 |

U-turns and transfers between the two crossing levels are forbidden. The separate Route Query and visible-travel cases come from this assembly’s authoritative record and appear in [5. Results and known issues](#5-results-and-known-issues).

<a id="software-verification"></a>

## 3. Software checks

The current arrangement uses **28 placements of 14 types**, within the unchanged **20 × 23 tile** rectangle, with **105 occupied tiles**, **74 support positions**, **715,251 actual placed-tile triangles**, and **166 encoded PATH fragments**. The [current validation](evidence/validation.json), [immutable initial integration gate](evidence/border-piece-integration-initial-validation.json), and [current integration record](checks/border-piece-integration.json) bind the actual saved fourteen-type candidate and complete physical checks. These software results establish neither a human picture approval nor an installed or observed game result.

The current [test report](evidence/border-piece-integration-tests.json) separates each executed source/native scope and its explicit skips. The [package report](evidence/border-piece-integration-package.json) identifies the actual final parts, one-button menu, and delivery outputs; it is kept outside its own hashed delivery archive. Older numerical test and extraction results below retain their original run scope.

The preceding four-tile-merge capture used **26 placements of 13 types**, with the existing paired straight replacing the former western merge tile. Its preserved [validation report](evidence/design-history/before-border-piece-integration/evidence/validation.json) and [extraction proof](evidence/merge-west-tail-extraction.json) accept the actual saved four-tile resources and complete arrangement: **105 occupied tiles**, **74 support positions**, **709,002 placed-tile triangles**, and **166 encoded PATH fragments**. Support spacing remains at least **16 m**. Historical test logs, build provenance, and preservation audits remain linked in the [design history](#design-history). These software results create no human image approval, installation, or game-test pass.

The preserved four-tile-merge [portable regression report](evidence/merge-west-tail-tests.json) records **1,023 reported tests**, **78 explicit skips**, zero failures, and zero errors from `python3 -B tools/run_tests.py`. Its clean source snapshot excludes private settings, native game inputs, and staged builds; the skipped native cases are not counted as executed. The saved-resource, complete-assembly, connector, and menu checks above have their own separately executed evidence.

### Accepted border corrections and three-piece fan extraction

The current build uses the accepted grey-border repairs in P01 and P08 (the same diverge type at opposite rotations), P04 (the symmetric split and return), P07 (the opposed merge), and P06 (the retained fan fork). The [standalone revision chain](checks/atomization.json) preserves the separate piece-only history; its earlier assembly deferrals are superseded by this separately verified current integration, not rewritten as old assembly passes.

P06 now owns the exact nine saved fork cells. P06A and P06B are two copies of the new one-tile recessed-web paired straight. The [required coordinate-labelled drawing and saved-input audit](evidence/fan-atomization-review.json) explain why the ordinary straight was rejected, compare every non-cap surface and the complete supports/materials, and record the small texture/tessellation cleanup and fourteen redundant northern cap removals. All nine core models remain exact. The unchanged native neighbour's actual end-plane faces continuously cover the inherited structural-web transition, so no new closure patch is introduced.

The current [native parts audit](evidence/fan-core-parts-build.json), both [core extraction](../../00_pieces/hsr-component-l2-paired-fan-compact-core/evidence/fan-core-extraction.json) and [straight extraction](../../00_pieces/hsr-component-l2-paired-straight-recessed-web/evidence/straight-extraction.json) proofs, and the complete current physical audit have separate scopes. The other twenty-five original placement dictionaries are unchanged. Track directions, all six complete journeys, support positions, outside ports, and the city grid remain preserved; the inherited northern web transition is not universal native-profile compatibility.

### Current independent acceptance scope

A **PATH** describes train movement. An **S3D model** contains visible triangles. A **DAT archive** packages those game resources. A **fingerprint** is a hash of exact file bytes; it detects any change in the approved resources.

Use the [quality contract](checks/contract.json) and [layout contract](checks/layout.json) with the resource fingerprints below; these source records define the current acceptance requirements.

The current [resource contract](checks/resources.json) binds the 14 selected piece DATs, their identities, recipes, sizes, resource counts, and hashes, plus the models, PATHs, and shadows of the 105 placed tiles, their owners and rotations, all six complete directed journeys, the fixed layout, and the historical decision content. The current pins identify the newly audited fourteen-type assembly; the following older extraction figures retain their original four-tile-merge scope. The [extraction proof](evidence/merge-west-tail-extraction.json) confirms exact resource preservation in **103 world cells**, byte-identical PATHs in **104 retained world cells**, identical decoded routes for the replacement straight's **two routes**, **12 byte-identical complete DATs**, identical point counts and hashes for **all six complete journeys**, and all **74 support positions** preserved. The preceding [five-tile-merge audit](evidence/design-history/evidence-validation-before-merge-west-tail-extraction.json) recorded **708,930 placed-tile triangles**, **166 encoded PATH fragments**, and **1,155 tile-resource fingerprints**; those figures remain facts about that earlier capture.

The current placement contract requires **28 placements, 14 types, 105 occupied tiles, and 74 support centres**, at least **16 m** apart. Outside ports, the **20 × 23 tile** construction rectangle and fixed X/Y grid are unchanged. P26 owns the extracted tile and its existing support, and P07's reference was moved 16 m east while its retained geometry was rebased 16 m west locally. The approved local physical adjustment affects the upper northern parapet and adjacent upper bed strip within a **2.5 m** collar at the new western seam, by at most **3.4524 mm**. The rail region, slab underside, pier, outside ports, and support positions are preserved. The executed audit checks all six HSR journeys in every proper rotation, with no U-turn or unintended level transfer, as well as the new P26/P07 seam and **six native joining sections**. Keeping an inherited interface byte-identical does not establish that every visual detail at that interface has been redesigned.

The production blend's [independent collar proof](../../00_pieces/hsr-component-l2-short-opposed-merge-core/evidence/west-parapet-collar-proof.json) records a measured maximum displacement of **3.452301025 mm** and **6,518 finite section checks** with zero new gaps above **2 micrometres** in that scan. A micrometre is 0.001 mm. The complete saved-build audit additionally checks **87 collar sections** at 29 positions and matches all five zooms to the approved seam model. These finite checks do not establish unrestricted watertightness. Triangle partitioning interpolates texture coordinates at new vertices; texture placement inside the deformed collar is not asserted unchanged.

The verifier also checks full **5 m** train corridors, native visible rails, deck intersections, pillar contacts, separate tile ownership, all five model/shadow zooms, and construction rotation lists. It measures **all six complete journeys**, including both northern loops, against the existing **24 m minimum radius**, **0.0015 per square metre maximum curvature change**, and **0.0005 per metre maximum curvature at the native outside ends**. Curvature means bend tightness, or one divided by the radius. These whole-journey checks supplement each constituent module's independent contract.

Every complete journey must also stay within **3°** of heading change between raw encoded segments, **8°** between quality samples spaced no more than **2 m** apart, and **0.025 per metre** of grade change, checked on both the raw and sampled routes. Grade means vertical rise divided by horizontal distance. Each journey has its own length and winding limits below. The length ratio is route length divided by the straight-line distance between its ends. Cumulative turn adds the size of every bend; signed turn retains the left/right sign, so opposite bends can cancel. The signed-turn tolerance is **0.01°** for every movement.

| Complete movement | Maximum length ratio | Cumulative turn | Required signed turn |
| --- | ---: | --- | ---: |
| West → East and East → West | 1.00001 | At most 0.01° | 0° |
| West → South and South → East | 1.55 | At most 130° | −90° |
| East → South | 3.5 | 269°–271° | +90° |
| South → West | 3.5 | 269°–271° | −270° |

The accepted fan region contains **11 tiles**, now split between the nine-tile P06 core and one-tile placements P06A and P06B. Four former structural cells remain omitted only after every saved model zoom has no surface or positive-area projection inside those cells, their PATH resources are absent, and no support is owned there. The two earlier near-centre fan supports are replaced by one support at **(112 m, 32 m)** in assembly authoring coordinates. The explicit plan retains all **59 support positions** outside the redesigned modules and has **74 positions** overall. The [junction redesign record](checks/junction-rework.json) holds the baseline hashes, exact allowed region, fixed sockets, and actual saved-resource proof.

### Approved paired-fan structure width

The paired part of P06 now retains its native **15 m** width through the approach and the start of the fork. Each shoulder taper begins at 48 m and ends at 72 m along its authored sweep. The [saved-model comparison](../../00_pieces/hsr-component-l2-paired-fan-compact-join/evidence/fan-width-audit.json) measures bed and underside cross-sections, confirms exact identity of all **21,245 visible rail triangles**, and confirms unchanged bytes for all **11 PATH resources**. The approved angled and top pictures have their own image-bound user observations; that approval does not establish game appearance or operation.

The preceding fan-width baseline reran the full independent geometry audit from the approved fan DAT and twelve byte-identical earlier component DATs. Its [normal build provenance](evidence/junction-rework-build.json) distinguishes reuse of verified saved meshes from resource generation and verification, and its [executed native test report](evidence/junction-rework-tests.json) identifies the exact inputs and results. Those executions predate the four-tile merge extraction. The later [extraction proof](evidence/merge-west-tail-extraction.json) identifies the new saved build and current normalizer execution. Earlier audits and render reports remain preserved under `evidence/design-history/*-before-fan-width.json`.

### Inherited interface checks and limits

The four exposed ordinary connections receive full native slab, underside, and parapet checks. The revised P06/P07 branch geometry and both uses of the Short Mainline Diverge Core must also pass the complete-assembly train-corridor and neighbouring-model checks. Earlier interface exceptions belong to the historical build that established them; the current validation records any retained exception explicitly.

The two shortened one-way curves retain their custom-end tiles. Their standalone rail audit allows a narrowly limited **2.65 m cut depth**, tied to the exact approved port-tile model hashes at all five zooms. This accounts for a rail strip crossing the artificial standalone cut. It neither widens the allowed rail strip nor permits stray rails inside the piece. The complete-assembly audit uses actual neighbouring models and uncut routes, with no artificial end cap. Mutation tests reject changed port hashes, excessive depth or width, and interior stray rails.

### Run the software checks

To check the existing staged candidate, open a terminal in the repository folder containing `custom-pieces`, and activate this checkout's Python environment using [Python setup](../../../../docs/BUILD_AND_INSTALL.md#python-setup-for-a-checkout-or-source-zip). The commands below use `python`, which selects that environment's interpreter on macOS, Linux, and Windows. Verify the candidate, then write a private assembly-audit report under `custom-pieces/local/`. If `trumpet-validation.json` already contains a run you need to retain, choose an unused report filename:

```sh
python custom-pieces/scp.py verify --output custom-pieces/dist/trumpet-fan-core-menu-final-01
python custom-pieces/domains/high-speed-rail/tools/verify_hsr_trumpet.py --build custom-pieces/dist/trumpet-fan-core-menu-final-01 --scene custom-pieces/domains/high-speed-rail/01_assemblies/straight-stem-trumpet/assembly.json --output custom-pieces/local/trumpet-validation.json
```

Next, set `SCP_TRUMPET_BUILD`, an **environment variable** that tells the integration checks which candidate directory to inspect. Some saved-resource checks default to `custom-pieces/dist/straight-stem-trumpet` when this variable is absent; the complete-candidate integration check requires it explicitly. The check runner resolves relative candidate paths from the repository root. The following commands set an absolute path, run the assembly checks, and remove the variable afterward. On macOS or Linux, use:

```sh
export SCP_TRUMPET_BUILD="$PWD/custom-pieces/dist/trumpet-fan-core-menu-final-01"
python custom-pieces/scp.py check --scope straight-stem-trumpet
unset SCP_TRUMPET_BUILD
```

On Windows, use PowerShell:

```powershell
$env:SCP_TRUMPET_BUILD = (Resolve-Path 'custom-pieces/dist/trumpet-fan-core-menu-final-01').Path
python custom-pieces/scp.py check --scope straight-stem-trumpet
Remove-Item Env:SCP_TRUMPET_BUILD
```

If the candidate is missing or a fresh one is needed, follow the numbered [assembly-menu procedure](../../../../docs/BUILD_AND_INSTALL.md#prepare-the-assembly-menu). That guide owns the preparation commands and uses fresh output directories, such as `custom-pieces/dist/trumpet-fan-core-menu-final-02`; choose an unused name if its example already exists. Do not rerun `assembly-menu` into an existing candidate directory.

For the fresh run, replace `custom-pieces/dist/trumpet-fan-core-menu-final-01` in both verification commands, the `SCP_TRUMPET_BUILD` value for your shell, and every later candidate reference with the chosen new directory. Then repeat the verification and assembly checks above. Keep retained evidence links bound to their original runs, and record fresh reports separately. These commands create or check local outputs; they do not install the candidate.

The preceding [validation report](evidence/design-history/before-border-piece-integration/evidence/validation.json) and [public binary-payload projection of its audit input manifest](evidence/design-history/before-border-piece-integration/evidence/audited-build-manifest.json) identify that earlier four-tile-merge audit and 26-placement scene. Its exact input manifest's hash is `manifest_sha256` in that preserved validation report. Read the projection's declared scope before comparing its own file hash with that original manifest. The dedicated [extraction proof](evidence/merge-west-tail-extraction.json) binds the merge DAT with SHA-256 `a4b00568156436b3de3493f51dd13d939de7d5f50fbf72a9b432f3586cee726f`, preserved world routes and supports, and the bounded collar difference. The normal piece builder and normal saved-resource verifiers ran; unchanged analytic surface contexts were reused from verified cached models, and the production affine collar normalizer executed from the current source. This capture does not claim a cold recompilation of those unchanged analytic contexts. A missing current descriptor, missing required staged build, or changed resource must fail verification. Optional integration tests may explicitly skip an absent current build; they must not hide malformed present builds or substitute generated expected answers.

The preceding [25-placement validation](evidence/design-history/evidence-validation-before-merge-west-tail-extraction.json) and its [audit-input manifest](evidence/design-history/evidence-audited-build-manifest-before-merge-west-tail-extraction.json) preserve the five-tile merge's original accepted inputs. Its [build provenance](evidence/junction-rework-build.json) records two freshly generated revised mesh types and guarded reuse of unchanged model meshes for the other 11 types. The normal builder regenerated their PATHs, shadows, construction definitions, previews, effects, and rules; all 11 unchanged complete DAT archives were compared byte for byte with that run's accepted baseline. The earlier [branch-angle proof](evidence/design-history/checks-junction-rework-before-merge-west-tail-extraction.json) records its 85 preserved world cells, four empty removed cells, fixed sockets, support plan, and complete-route movement measurements. Those are historical facts about that execution, rather than fresh proof of the western-tile extraction.

The previous [validation](evidence/design-history/validation-before-junction-rework.json) and [audit-input manifest projection](evidence/design-history/audited-build-manifest-before-junction-rework.json) remain frozen byte for byte. They retain the earlier accepted 109-tile, 26-placement, and 14-type baseline and its original measured scope.

The preceding [native test report](evidence/junction-rework-tests.json) records **71 tests passed, zero failures, zero errors, and zero skips**, including a full saved-candidate audit after the scoped custom-cut verifier correction. Its declared source, verifier, and manifest inputs stayed unchanged throughout that run, and all 13 component archives were checked against its recorded resource pins. This report predates the new four-tile extraction and does not replace a fresh test execution.

The [earlier executed capture](evidence/design-history/validation-at-junction-rework-capture.json), its exact [scene input](evidence/design-history/assembly-at-junction-rework-audit.json), and its exact [layout input](evidence/design-history/layout-at-junction-rework-audit.json) preserve the stage before the descriptive `geometry_status` and `purpose` updates. Their original hashes remain historical facts. At that stage, a later integration audit used the refreshed scene. After that run, only the layout's descriptive `scope` was corrected from fourteen types to thirteen; the exact [layout input for that rerun](evidence/design-history/layout-at-junction-rework-postfix-audit.json) is also frozen. That report records the before/after fingerprints and proves every other JSON field was identical. Those metadata updates changed no physical layout, models, PATHs, supports, or outside connections and are separate from the later western-tile extraction.

### Artwork evidence

The six assembly pictures start with `Assembly - Straight-stem HSR trumpet`; the second row identifies a `Clean view`, `Component guide`, or `Construction view`, followed by the camera direction. Their [render report](evidence/render.json) records the exact images, fixed captions, renderer settings, and saved-model inputs for all **28 placements**. The named views and construction plan show the nine-tile P06 core, separate P06A and P06B recessed-web straights, four-tile P07, and separate P26. The [artwork audit](evidence/border-piece-integration-artwork.json) binds those six pictures to the immutable whole-assembly gate and preserves the original observations. The [preceding 26-placement render report](evidence/design-history/before-border-piece-integration/evidence/render.json) and [earlier P01–P25 render report](evidence/design-history/evidence-render-before-merge-west-tail-extraction.json) retain their original scopes. The current [component picture report](evidence/piece-previews.json) maps all 28 placements to the 14 reusable type-picture pairs.

The preceding [executed connector refresh](evidence/merge-west-tail-connectors.json) rerendered and independently checked all 15 then-supported migrated types after the owning implementation changed. All **56 canonical PNGs for the other 14 types** remained byte-identical, and every authoritative manual record remained unchanged during that pass. Refreshed image bindings and generated case summaries remain views of the original observations; they create no human image approval or game-test pass.

<a id="game-testing"></a>

## 4. Game checks

Use the exact reference layout from chapter 2 and the verified candidate from chapter 3. Installation requires an explicit installation request; running software checks does not install the candidate. Record each observation against its exact direction, service, inputs, and game environment.

### Menu and placement

The current assembly menu requires one **SCP | ASSEMBLY | HSR Trumpet** button containing its **14 component types**. Check that Tab visits all 14 types, Shift+Tab reverses that order, and one click places only the selected component. The [assembly-menu guide](../../../../docs/BUILD_AND_INSTALL.md#prepare-the-assembly-menu) owns those preparation steps. Current static acceptance belongs to the [final package report](evidence/border-piece-integration-package.json), which records the actual fourteen-type cycle, unchanged component DATs, one button, and no submenu for the new candidate. The preceding [menu audit](evidence/design-history/before-border-piece-integration/evidence/assembly-menu.json) retains its original thirteen-type scope; older menu results do not certify the new cycle. Static verification does not establish the button’s appearance or keyboard behaviour inside the game.

### Appearance and travel

After installing an authorized test build, use a disposable flat city. Inspect P22/P01, the new P26/P07 seam, and P07/P23 at every zoom, then P03/P24 and P25/P10. Check rails, deck, wall openings, pillars, and shadows. Verify each piece's cursor placement at its specified orientation. Build the complete reference arrangement, supply real Monorail demand, and check every journey with separate Route Query and visible-train observations. Also test forbidden U-turns and level transfers, demolition, and save/reload. Record the tested file hashes, city layout, platform, and screenshots with the observation.

The three generated forbidden-transfer cases cover the approach U-turns. They do not separately establish an in-game crossing-level isolation result; keep that distinction when reporting the observed scope.

### Record the outcome

Assembly game observations remain **unverified** unless the user has explicitly confirmed the exact case in this subject's own record. Documentation and menu changes do not establish a game observation. Use the [shared observation procedure](../../../../docs/TESTING.md) to record precise human results in `checks/manual-tests.json`; software checks cannot create those confirmations.

## 5. Results and known issues

The generated checklist below reads [checks/manual-tests.json](checks/manual-tests.json), the authoritative observation record. A known defect can remain open even when no current case is marked failed: the defect report may describe a different recorded build or an incompletely identified environment. Keep its evidence and limits visible alongside the current case results.

### Known issues

**Open demolition defect, reported 2026-10-23:** selecting one tile for demolition caused connected custom parts to appear as Monorail; disconnected copies remained unchanged in the original report. The user also confirmed a smaller reproduction: place three copies of `hsr-component-lower-paired-straight` end to end, delete the middle copy, and both connected survivors appear as Monorail. The disconnected control's outcome was not separately reported for this second test. The exact original deleted type, orientation, affected cells, and confirmed game environment remain unknown. The [scoped failure report](evidence/demolition-regression-20261023.json) binds the installed menu-trial context and retains both observations and their limits. Static comparison found all 165 installed piece archives and every construction definition unchanged from the pre-menu installation; it does not establish the runtime cause or a fix. Follow the [single-tile demolition regression procedure](../../../../docs/TESTING.md#investigate-single-tile-demolition-and-connected-survivors) in a disposable city. Existing whole-placement demolition and save/reload observations do not cover this failure.

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Human game checks are required only at 0° CCW. Supported construction orientations and software rotation checks retain their separate scope; these human cases do not establish observations at the other orientations.

Current totals: unverified: 26, passed: 2, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/01_assemblies/straight-stem-trumpet/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/01_assemblies/straight-stem-trumpet/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-fe740c153144a3695751">[x] passed</a> | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-fe740c153144a3695751"></a>

**General: passed** — `software_resources-fe740c153144a3695751`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: verify_hsr_trumpet.py: actual saved-resource and full-assembly audit; confirmed at: 2026-10-27T14:12:46.158490+00:00; evidence: [evidence/validation.json, evidence/audited-build-manifest.json]; environment: {}
- result: passed; authority: software; reviewer: verify_hsr_trumpet.py: completed native saved-resource and whole-assembly audit; confirmed at: 2026-10-27T19:05:41.349287+00:00; evidence: [evidence/validation.json, evidence/audited-build-manifest.json, evidence/junction-rework-build.json]; environment: {}
- result: passed; authority: software; reviewer: verify_hsr_trumpet.py: completed native saved-resource and whole-assembly audit; confirmed at: 2026-10-27T19:17:27.127678+00:00; evidence: [evidence/validation.json, evidence/audited-build-manifest.json, evidence/junction-rework-build.json]; environment: {}
- result: passed; authority: software; reviewer: verify_hsr_trumpet.py: completed native saved-resource and whole-assembly audit; confirmed at: 2026-10-27T21:59:37.265650+00:00; evidence: [evidence/validation.json, evidence/audited-build-manifest.json, evidence/junction-rework-build.json]; environment: {}
- result: passed; authority: software; reviewer: Current saved-resource verifier and independent one-plus-four extraction/assembly controls; confirmed at: 2026-10-28T09:50:03.583685+00:00; evidence: [evidence/validation.json, evidence/merge-west-tail-extraction.json, evidence/audited-build-manifest.json]; environment: {}
- result: passed; authority: software; reviewer: Current normal native 14-type saved build, independent complete 28-placement assembly integration, and actual saved-PATH extraction with all25 non-fan placement dictionaries unchanged and the reviewed three-piece fan decomposition; confirmed at: 2026-10-28T18:16:00.644573+00:00; evidence: [evidence/border-piece-integration-initial-validation.json, checks/border-piece-integration.json, evidence/border-piece-integration-artwork.json]; environment: {}

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-fe740c153144a3695751">[x] passed</a> | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-fe740c153144a3695751"></a>

**General: passed** — `software_connectivity-fe740c153144a3695751`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: verify_hsr_trumpet.py: actual saved-resource and full-assembly audit; confirmed at: 2026-10-27T14:12:46.158490+00:00; evidence: [evidence/validation.json, evidence/audited-build-manifest.json]; environment: {}
- result: passed; authority: software; reviewer: verify_hsr_trumpet.py: completed native saved-resource and whole-assembly audit; confirmed at: 2026-10-27T19:05:41.349287+00:00; evidence: [evidence/validation.json, evidence/audited-build-manifest.json, evidence/junction-rework-build.json]; environment: {}
- result: passed; authority: software; reviewer: verify_hsr_trumpet.py: completed native saved-resource and whole-assembly audit; confirmed at: 2026-10-27T19:17:27.127678+00:00; evidence: [evidence/validation.json, evidence/audited-build-manifest.json, evidence/junction-rework-build.json]; environment: {}
- result: passed; authority: software; reviewer: verify_hsr_trumpet.py: completed native saved-resource and whole-assembly audit; confirmed at: 2026-10-27T21:59:37.265650+00:00; evidence: [evidence/validation.json, evidence/audited-build-manifest.json, evidence/junction-rework-build.json]; environment: {}
- result: passed; authority: software; reviewer: Current saved-resource verifier and independent one-plus-four extraction/assembly controls; confirmed at: 2026-10-28T09:50:03.583685+00:00; evidence: [evidence/validation.json, evidence/merge-west-tail-extraction.json, evidence/audited-build-manifest.json]; environment: {}
- result: passed; authority: software; reviewer: Current normal native 14-type saved build, independent complete 28-placement assembly integration, and actual saved-PATH extraction with all25 non-fan placement dictionaries unchanged and the reviewed three-piece fan decomposition; confirmed at: 2026-10-28T18:16:00.644573+00:00; evidence: [evidence/border-piece-integration-initial-validation.json, checks/border-piece-integration.json, evidence/border-piece-integration-artwork.json]; environment: {}

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-4b8e61d1c512b7c578e8">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-4b8e61d1c512b7c578e8"></a>

**0° CCW: unverified** — `in_game_render-4b8e61d1c512b7c578e8`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-4b8e61d1c512b7c578e8">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-4b8e61d1c512b7c578e8"></a>

**0° CCW: unverified** — `in_game_placement-4b8e61d1c512b7c578e8`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-4b8e61d1c512b7c578e8">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-4b8e61d1c512b7c578e8"></a>

**0° CCW: unverified** — `in_game_demolition-4b8e61d1c512b7c578e8`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-4b8e61d1c512b7c578e8">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-4b8e61d1c512b7c578e8"></a>

**0° CCW: unverified** — `in_game_save_reload-4b8e61d1c512b7c578e8`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — hsr — 6 cases; unverified: 6</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Route Query**<br>Service: hsr; role: primary; journey: E.in>S.out; entry: E.in; exit: S.out | — | <a href="#case-in_game_route_query-8b08022118fd9f445d85">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out | — | <a href="#case-in_game_route_query-76bf51a0e3b87a77ead7">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out | — | <a href="#case-in_game_route_query-336582ad6132a64a36f8">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out | — | <a href="#case-in_game_route_query-2572758d9ad9c64a40fd">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out | — | <a href="#case-in_game_route_query-87f3cb5204e2970d80c1">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out | — | <a href="#case-in_game_route_query-aea09525a3e21f949d2b">[ ] unverified</a> |


<details>
<summary>Route Query — Service: hsr; role: primary; journey: E.in>S.out; entry: E.in; exit: S.out</summary>

<a id="case-in_game_route_query-8b08022118fd9f445d85"></a>

**0° CCW: unverified** — `in_game_route_query-8b08022118fd9f445d85`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: E.in>S.out; entry: E.in; exit: S.out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out</summary>

<a id="case-in_game_route_query-76bf51a0e3b87a77ead7"></a>

**0° CCW: unverified** — `in_game_route_query-76bf51a0e3b87a77ead7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out</summary>

<a id="case-in_game_route_query-336582ad6132a64a36f8"></a>

**0° CCW: unverified** — `in_game_route_query-336582ad6132a64a36f8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out</summary>

<a id="case-in_game_route_query-2572758d9ad9c64a40fd"></a>

**0° CCW: unverified** — `in_game_route_query-2572758d9ad9c64a40fd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out</summary>

<a id="case-in_game_route_query-87f3cb5204e2970d80c1"></a>

**0° CCW: unverified** — `in_game_route_query-87f3cb5204e2970d80c1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out</summary>

<a id="case-in_game_route_query-aea09525a3e21f949d2b"></a>

**0° CCW: unverified** — `in_game_route_query-aea09525a3e21f949d2b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — hsr — 6 cases; unverified: 6</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Visible travel**<br>Service: hsr; role: primary; journey: E.in>S.out; entry: E.in; exit: S.out | — | <a href="#case-in_game_visible_travel-8b08022118fd9f445d85">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out | — | <a href="#case-in_game_visible_travel-76bf51a0e3b87a77ead7">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out | — | <a href="#case-in_game_visible_travel-336582ad6132a64a36f8">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out | — | <a href="#case-in_game_visible_travel-2572758d9ad9c64a40fd">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out | — | <a href="#case-in_game_visible_travel-87f3cb5204e2970d80c1">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out | — | <a href="#case-in_game_visible_travel-aea09525a3e21f949d2b">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: E.in>S.out; entry: E.in; exit: S.out</summary>

<a id="case-in_game_visible_travel-8b08022118fd9f445d85"></a>

**0° CCW: unverified** — `in_game_visible_travel-8b08022118fd9f445d85`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: E.in>S.out; entry: E.in; exit: S.out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out</summary>

<a id="case-in_game_visible_travel-76bf51a0e3b87a77ead7"></a>

**0° CCW: unverified** — `in_game_visible_travel-76bf51a0e3b87a77ead7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out</summary>

<a id="case-in_game_visible_travel-336582ad6132a64a36f8"></a>

**0° CCW: unverified** — `in_game_visible_travel-336582ad6132a64a36f8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out</summary>

<a id="case-in_game_visible_travel-2572758d9ad9c64a40fd"></a>

**0° CCW: unverified** — `in_game_visible_travel-2572758d9ad9c64a40fd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out</summary>

<a id="case-in_game_visible_travel-87f3cb5204e2970d80c1"></a>

**0° CCW: unverified** — `in_game_visible_travel-87f3cb5204e2970d80c1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out</summary>

<a id="case-in_game_visible_travel-aea09525a3e21f949d2b"></a>

**0° CCW: unverified** — `in_game_visible_travel-aea09525a3e21f949d2b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Forbidden transfer**<br>from port: W.in; to port: W.out; from service: hsr; to service: hsr; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-92b725456842f93c47ca">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: S.in; to port: S.out; from service: hsr; to service: hsr; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-dfbdc4123044e5fb53fe">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: E.in; to port: E.out; from service: hsr; to service: hsr; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-9f7a461fa713c7413977">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: W.in; to port: W.out; from service: hsr; to service: hsr; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-92b725456842f93c47ca"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-92b725456842f93c47ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: W.in; to port: W.out; from service: hsr; to service: hsr; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: S.in; to port: S.out; from service: hsr; to service: hsr; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-dfbdc4123044e5fb53fe"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dfbdc4123044e5fb53fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: S.in; to port: S.out; from service: hsr; to service: hsr; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: E.in; to port: E.out; from service: hsr; to service: hsr; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-9f7a461fa713c7413977"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9f7a461fa713c7413977`.

Confirm this undeclared transfer is unavailable.

Scope: from port: E.in; to port: E.out; from service: hsr; to service: hsr; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 7 cases; unverified: 7</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Preview review**<br>Image: image:straight-stem-trumpet:clean-southeast | <a href="#case-preview_review-4255f74d1a0022065ce4">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:straight-stem-trumpet:clean-top | <a href="#case-preview_review-8f00df0ccb26670bca5a">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:straight-stem-trumpet:fan-atomization-review | <a href="#case-preview_review-11a85f8a26bcca0d56f4">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:straight-stem-trumpet:named-northwest | <a href="#case-preview_review-09c7f0560ea1efecf6f1">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:straight-stem-trumpet:named-southeast | <a href="#case-preview_review-b0defe1adfa80a596bb8">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:straight-stem-trumpet:named-top | <a href="#case-preview_review-ecf9be65aaa4dd4c3c7b">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:straight-stem-trumpet:tile-ownership | <a href="#case-preview_review-a613bd9fbd07c6e7cb5f">[ ] unverified</a> | — |


<details>
<summary>Preview review — Image: image:straight-stem-trumpet:clean-southeast</summary>

<a id="case-preview_review-4255f74d1a0022065ce4"></a>

**General: unverified** — `preview_review-4255f74d1a0022065ce4`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:straight-stem-trumpet:clean-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:straight-stem-trumpet:clean-top</summary>

<a id="case-preview_review-8f00df0ccb26670bca5a"></a>

**General: unverified** — `preview_review-8f00df0ccb26670bca5a`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:straight-stem-trumpet:clean-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:straight-stem-trumpet:fan-atomization-review</summary>

<a id="case-preview_review-11a85f8a26bcca0d56f4"></a>

**General: unverified** — `preview_review-11a85f8a26bcca0d56f4`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:straight-stem-trumpet:fan-atomization-review.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:straight-stem-trumpet:named-northwest</summary>

<a id="case-preview_review-09c7f0560ea1efecf6f1"></a>

**General: unverified** — `preview_review-09c7f0560ea1efecf6f1`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:straight-stem-trumpet:named-northwest.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:straight-stem-trumpet:named-southeast</summary>

<a id="case-preview_review-b0defe1adfa80a596bb8"></a>

**General: unverified** — `preview_review-b0defe1adfa80a596bb8`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:straight-stem-trumpet:named-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:straight-stem-trumpet:named-top</summary>

<a id="case-preview_review-ecf9be65aaa4dd4c3c7b"></a>

**General: unverified** — `preview_review-ecf9be65aaa4dd4c3c7b`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:straight-stem-trumpet:named-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:straight-stem-trumpet:tile-ownership</summary>

<a id="case-preview_review-a613bd9fbd07c6e7cb5f"></a>

**General: unverified** — `preview_review-a613bd9fbd07c6e7cb5f`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:straight-stem-trumpet:tile-ownership.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

<a id="design-history"></a>

## 6. Design history

### Western merge approach extraction

The approved decomposition moves the ordinary western tile out of the five-tile Short Opposed Merge Core and reuses the existing **HSR L2 Two-Track Straight** there. The new straight is **P26 at (X9, Y13), 270°**. **P07 starts at (X10, Y13), 0°**, and owns four tiles through (X13, Y13). At that extraction stage, all existing P01–P25 labels were retained, giving 26 placements of the same 13 types before the later three-piece fan extraction. Occupied world cells, outside routes, and support positions stay fixed; the only approved local physical change is the bounded parapet-and-upper-bed adjustment described in chapter 3.

The historical P03B western-tail decision below measured **6.437054 mm** in the deleted predecessor before branch-angle unification. The later northern branch redesign changed that cell's contents; the subsequent review identified an ordinary paired-route tile. The original five-tile report, decision history, and observations retain their original identities and inputs. They are not relabelled as proof of the new four-tile core. The new [extraction audit](evidence/merge-west-tail-extraction.json), [current validation](evidence/validation.json), and [render report](evidence/render.json) identify the later executed work. No software comparison or picture refresh creates a game pass.

### Branch-angle unification and placement numbering

The preceding branch-angle redesign replaced the former P03CW straight and P03C Compact Fan Diverge with a second copy of the retained Short Mainline Diverge Core, placed at authoring position (176 m, 0 m), or picture position (X18, Y13), at 180°. The adjoining paired fan and opposed merge were reworked to match that core's branch angle. That stage used 25 placements and 13 types, before the later P26 extraction above. It was an authorized geometry revision, separate from the earlier sub-5 mm tail-extraction policy. The older socket-mismatch measurements below describe the previous geometry and retain their original identities and scope.

The [current redesign record](checks/junction-rework.json) freezes the previous complete east-to-south and south-to-west train routes and checks their movement against an independent **6.0 m** envelope. This limit was chosen before measuring the new routes: the fixed connection sockets move **5.835829856 m**, rounded upward to 6.0 m. The measurement is the greatest distance from either route to the nearest point on the other route, including points between stored coordinates. The actual saved native PATH audit encloses the maximum between **5.005208772 m and 5.005308655 m**, a range narrower than **0.1 mm**; the earlier source preflight independently produced the same interval. The record retains the original decoded coordinates and their fingerprints, so later checks do not need deleted source folders or predecessor DAT files. The 24-cell change boundary, fixed outside connections, 85 unchanged cells, four unchanged complete routes, and existing radius, curvature, clearance, and support limits remain separate mandatory checks.

That branch-angle stage numbered placements consecutively from P01 through P25; the later extraction appends P26 and retains those labels. The following map preserves the meaning of older reports without relabelling their evidence. P03B maps to P07's reusable type, but its former westernmost tile is now separately owned by P26. Labels identify placed copies; permanent piece and game-resource IDs of retained types do not change.

| Earlier placement | Current placement |
| --- | --- |
| P01A | P01 |
| P01S | P02 |
| P01B | P03 |
| P02A | P04 |
| P02B | P05 |
| P03A | P06 |
| P03B | P07 |
| P03CW | P08 |
| P03CE | P09 |
| P03D | P10 |
| P04A | P11 |
| P04N | P12 |
| P04S | P13 |
| P04W | P14 |
| P04E | P15 |
| P05 | P16 |
| P06 | P17 |
| P07 | P18 |
| P08 | P19 |
| P09 | P20 |
| P10 | P21 |
| P01AW | P22 |
| P03BE | P23 |
| P01BS | P24 |
| P03DS | P25 |

The former P03C and P03CW both map to the single current P08 placement; they are not separate components in the current build.

Historical executions retain their original names, paths, input fingerprints, and results. The [test logs](evidence/test-results.json), [build provenance](evidence/build-provenance.json), and [preservation audit](evidence/preservation.json) describe those original executions. Current entry points, scene identifiers, and software checks use `straight-stem-trumpet`.

This section retains the historical design decisions and their original measurements. These records explain how the current geometry was chosen; they do not represent additional selectable assembly versions or current game-test passes. See the [decision ledger](checks/atomization.json) and [implementation record](evidence/atomization-implementation.json) for the original evidence.

### Accepted and retained candidates

**Atomization** means separating a larger piece into smaller useful modules. The historical candidate threshold was **strictly below 5 mm of original lateral deviation**. It selected a tail for investigation; it did not prove that its deck, wall openings, or supports could be replaced. The actual corrections in adjoining retained tiles had separate bounds: **24.5 mm** for paired junctions and **8.2 mm** for one-way curves. A **millimetre** is 0.001 m. The recorded eligibility measurements and correction bounds remain distinct.

Local X/Y positions in the following table refer to the original reviewed modules, not the shortened current previews. The schema-2 [atomization history](checks/atomization.json) retains those measurements, all **51 reviewed source cells**, the 17 decisions and their reasons. Original identifiers and hashes describe historical inputs; current verification neither opens deleted predecessor definitions nor remeasures deleted DATs. Instead, it checks that the recorded history stays unchanged and that every current replacement still matches its approved geometry fingerprint.

| Candidate in original piece | Original deviation | Decision | Reason |
| --- | ---: | --- | --- |
| P01A: (X0, Y0) | 4.018 mm | Extract into standard straight | The original branch tail is strictly below 5 mm from the compatible ordinary straight. A bounded correction in its adjoining retained tile gives an independently placeable native end; the existing straight then owns the extracted tile and its support. Both mirrored tails are changed together to preserve direct-slip symmetry. |
| P03B: (X5, Y0) | 4.018 mm | Extract into standard straight | The original branch tail is strictly below 5 mm from the compatible ordinary straight. A bounded correction in its adjoining retained tile gives an independently placeable native end; the existing straight then owns the extracted tile and its support. Both mirrored tails are changed together to preserve direct-slip symmetry. |
| P01B: (X4, Y0) | 2.058 mm | Extract into standard straight | The original branch tail is strictly below 5 mm from the compatible ordinary straight. A bounded correction in its adjoining retained tile gives an independently placeable native end; the existing straight then owns the extracted tile and its support. Both mirrored tails are changed together to preserve direct-slip symmetry. |
| P03D: (X0, Y0) | 2.058 mm | Extract into standard straight | The original branch tail is strictly below 5 mm from the compatible ordinary straight. A bounded correction in its adjoining retained tile gives an independently placeable native end; the existing straight then owns the extracted tile and its support. Both mirrored tails are changed together to preserve direct-slip symmetry. |
| P01A: Whole-piece substitution | Not applicable | Retain | A rotated P03C is a different branch: its socket misses by 5.835829856 m and its tangent by 2.202886 degrees. Replacing P01A that way would move several existing modules and break the agreed direct-slip symmetry. |
| P01A: (X4, Y0) | 0.000 mm | Retain | Straight PATHs are insufficient: this tile owns a 500 mm branch-platform wing and an open parapet. An ordinary straight restores a wall only 1.169553309 m from the neighbouring branch PATH, inside its 2.6 m half-width clearance. |
| P02A: (X1, Y0) | 119.840 mm | Retain | Both directional branch tails move 119.840 mm, above the 5 mm eligibility threshold. This is also a split/merge platform rather than an ordinary straight profile. |
| P02A: (X0, Y5), (X2, Y5) | 119.840 mm | Retain | The side tails each move 119.840 mm. They fail the 5 mm threshold and participate in the shared split/merge platform. |
| P02A: (X1, Y3) | 0.000 mm | Retain | Its paired PATHs are straight but the shared slab is 16 m wide and has branch wall openings. An ordinary 15 m straight changes the physical connection. |
| P03B: (X0, Y0) | 6.437 mm | Retain | Its branch moves 6.437054 mm. This is above the strict 5 mm threshold, so it is not silently rounded into eligibility. |
| P03B: (X4, Y0) | 286.369 mm | Retain | The branch moves 286.369 mm and the northern branch deck reaches 8 m beyond the centre instead of the native 7.5 m half-width. An ordinary straight removes useful branch geometry. |
| P01B: (X4, Y1) | 148.533 mm | Retain | The next tile bends 148.533079 mm. Its route is not an almost-straight tail under the 5 mm policy. |
| P03D: (X0, Y1) | 148.533 mm | Retain | The next tile bends 148.533079 mm. Its route is not an almost-straight tail under the 5 mm policy. |
| P01B: (X4, Y2) | 1025.727 mm | Retain | This tile contains 1.02572658 m of lateral curve movement, so replacing it with a straight would materially change the layout. |
| P03D: (X0, Y2) | 1025.727 mm | Retain | This tile contains 1.02572658 m of lateral curve movement, so replacing it with a straight would materially change the layout. |
| P01B: (X4, Y3) | 3543.300 mm | Retain | This is a substantial bend of approximately 3.5433 m, not a straight tail. |
| P03D: (X0, Y3) | 3543.300 mm | Retain | This is a substantial bend of approximately 3.5433 m, not a straight tail. |

The saved [candidate-coverage report](evidence/candidate-coverage.json) preserves the rationale for the 34 generic retained cells: eight were structural models without train routes, while the other 26 each had a route fragment more than 5 mm from every tested cardinal or 45° straight, even with the best lateral offset. The smallest such recorded deviation was **72.955 mm**. It also records physical wall-clearance witnesses for the two all-straight candidates; an ordinary replacement at P02A would put a wall approximately **1.5 m** from the adjoining branch, inside its **2.6 m** clearance half-width. These are historical measurement results, not instructions to restore the removed source files or fixtures. A candidate can be reconsidered only through a separately authorized redesign and new evidence.

### Tail extraction decisions

V4 extracts four almost-straight tail tiles into two existing standard types. Their remaining junctions and curves become four new reusable types with their own menu buttons. No new special straight variant is needed. The comparison table preserves each **original reviewed piece’s local coordinates** as historical measurement context; those predecessor definitions are not current dependencies. The shortened V4 preview starts its own local grid: for example, new P01B local (X4, Y0) is the retained tile at assembly (X6, Y7), while original P01B local (X4, Y0) becomes the separate P01BS tile at assembly (X6, Y6).

| Original placement and local tile | Assembly tile | New ordinary placement | Existing standard and rotation | Remaining reusable core |
| --- | --- | --- | --- | --- |
| P01A (X0, Y0) | (X0, Y13) | P01AW | HSR L2 Two-Track Straight, 270° | P01A: Short Mainline Diverge Core, 4 tiles |
| P03B (X5, Y0) | (X14, Y13) | P03BE | HSR L2 Two-Track Straight, 270° | P03B: Short Opposed Merge Core, 5 tiles |
| P01B (X4, Y0) | (X6, Y6) | P01BS | One-Way HSR L2 Eight-Metre Straight, 180° | P01B: Shortened One-Way Departure Curve, 12 tiles |
| P03D (X0, Y0) | (X8, Y6) | P03DS | One-Way HSR L2 Eight-Metre Straight, 0° | P03D: Shortened One-Way Return Curve, 12 tiles |

The original P01A/P03B tails deviate **4.018 mm** from ordinary paired track; P01B/P03D deviate **2.058 mm** from centred one-way track. Those measurements qualify under the requested **strictly less than 5 mm** candidate policy. The joining curve in the next retained tile needs a separately measured correction: approximately **24.33 mm** for each paired junction and **8.14 mm** for each one-way curve. These were small local redesigns; the sub-5 mm eligibility threshold was not a bound on every adjoining route correction. The independent bounds are **24.5 mm** and **8.2 mm**, while the existing curve, clearance, and support limits stay in force.

The one-way straight must be **One-Way HSR L2 Eight-Metre Straight** (`hsr-component-lower-oneway-straight`), whose centred deck is 8 m wide. The similarly named `interchange-oneway-hsr-straight` has a different 7.5 m profile and is not the replacement used here. P01BS runs south at 180°; P03DS runs north at 0°.

Not every straight-looking tile qualifies. P02A's end tails bend **119.840 mm**. P03B's western tail bends **6.437 mm**. P01A's opposite end has straight train routes but a necessary platform wing and wall opening beside the branch; inserting a normal straight would put a wall inside the branch's train clearance. A rotated P03C also misses P01A's branch connection by approximately **5.836 m**. The [decision table in TESTING](TESTING.md#accepted-and-retained-candidates) explains the remaining candidates. The [historical decision record](checks/atomization.json) accounts for all **51 reviewed source tiles** in the five original modules and records why each stayed or was extracted. Current verification checks the retained design against its [approved resource fingerprints](checks/resources.json), without opening deleted predecessor files.

### Preserved measurement context

The earlier tail-extraction redesign was limited to eight world tiles: **(X0–X1, Y13)** and **(X13–X14, Y13)** for paired tails and joining collars; **(X6, Y6–Y7)** and **(X8, Y6–Y7)** for one-way tails and joining collars. The ledger preserves that run's measured movement and bounds as history. Its subsequently accepted **109-tile baseline** allowed no further edits and pinned every saved tile, including those eight. The later branch-angle redesign has a separate [24-cell authorization and preservation record](checks/junction-rework.json): the current candidate owns **105 tiles**, preserves the **85 unaffected world cells** exactly, and retains the four extracted standard-straight placements. The original tail-extraction measurements are not a measurement of the later branch work.

The historical mesh comparison measured the **sum of changed cross-section intervals**, not one track's movement. Two parapet strips have four interval edges, giving a one-way bound of **4 × (8.2 mm route bound + 0.05 mm section precision) = 33 mm** in total, with each edge checked independently. That did not permit a 33 mm route shift: the route bound was **8.2 mm**. The current contract now pins the approved result exactly instead of requiring the deleted comparison inputs.

### Identity and presentation cleanup

On 2026-10-27, the maintained assembly identity, collection, verifier, and test names changed to `straight-stem-trumpet`. The [migration report](evidence/identity-migration.json) records the mapping and unchanged measured payloads. Original identity-bound contracts and the [original observations](evidence/design-history/checks-manual-tests-before-identity-rename.json) are archived byte for byte; their passes were not relabelled as new cases. Current software cases require their own executed verification, and game checks remain unverified.

The earlier identity-only execution gave the six assembly renders neutral titles and removed the atomization-history text. In that specific execution, the saved S3D model bytes, track layout, supports, and every image pixel below the header band stayed unchanged; the archived render-source context retains that limited scope. The later junction redesign changes geometry and requires newly generated images with their own [current render report](evidence/render.json). The identity-only pixel comparison is not a preservation claim for those new images.
