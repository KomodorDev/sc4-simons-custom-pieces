---
title: "High-speed rail network specification"
summary: "Define audited HSR/GHSR donors, exact native boundary measurements, heights, service classification, rail-specific limits, and shared implementations; individual piece manuals own their literal contracts and exceptions."
audience: "Rail piece authors and maintainers"
document_type: "reference"
---

# High-speed rail network specification

This specification owns HSR/GHSR source facts and reviewed rail-family rules. Follow the shared [connector reference](../../docs/CONNECTOR_METADATA.md) for complete boundary/channel/cut comparison and explicit movement permissions. A rail profile here describes an actual native or authored geometric family; its name, parent, expected width, height label, or game class alone never decides a join. Physical model seams and actual game operation remain separate evidence.

Use the [piece-creation workflow](../../docs/WORKFLOW_PIECE_CREATION.md) when changing one type and the [assembly-creation workflow](../../docs/WORKFLOW_ASSEMBLY_CREATION.md) for layouts. The shared [documentation-generation workflow](../../docs/WORKFLOW_DOCUMENTATION_GENERATION.md) owns canonical previews, cards, exports, and README generation. [Framework engineering](../../docs/FRAMEWORK_ENGINEERING.md) owns format/coordinate conversion, runtime addressing, controller composition, generic geometry/render/shadow guards, and cache correctness.

The [domain registry](domain.json), [piece inventory](00_pieces/INVENTORY.md), and [assembly inventory](01_assemblies/INVENTORY.md) identify the current owners. [STRUCTURE.md](../../STRUCTURE.md) explains source authority and generated views. Read each type's authored engineering notes for its own footprint, ports, supports, bounds, and scoped exceptions.

## Implementation entry points

Generation and independent literal contracts remain separate. The shared recipe dispatcher calls this domain's registered `implementation` package; `scp_hsr.recipes.build_piece(spec, context)` must dispatch a new recipe and its verifier explicitly. Unknown recipe names fail. Controller/ring assembly and runtime addressing follow the neutral [framework contract](../../docs/FRAMEWORK_ENGINEERING.md#controller-composition-and-verification), rather than a rail-specific copy.

| Rail family or responsibility | Generator/source | Independent checks |
| --- | --- | --- |
| HSR/GHSR crossing recipes | `implementation/scp_hsr/crossings.py` | Shared saved-crossing checks in `../../framework/scp/verify.py` |
| Modular tracks, branches, ramps, and over/under crossings | `implementation/scp_hsr/interchange_layouts.py`, `interchange_models.py` | `implementation/scp_hsr/interchange_verify.py` |
| Diagonal shifts, handed crossovers, and the native two-way height adapter | `implementation/scp_hsr/rail_features.py`, `rail_geometry.py` | `implementation/scp_hsr/rail_feature_verify.py` |
| Current scissors recipes ending in `_revised` | `implementation/scp_hsr/rail_repairs.py` | `implementation/scp_hsr/rail_repair_verify.py` |
| Accepted straight smooth T | `implementation/scp_hsr/directional_t.py` | `implementation/scp_hsr/directional_t_verify.py` |
| Accepted diagonal smooth T | `implementation/scp_hsr/directional_diagonal_t.py` | `implementation/scp_hsr/directional_diagonal_t_verify.py` |
| Reusable paired upper/lower HSR components | `implementation/scp_hsr/hsr_components_layout.py`, `hsr_components.py` | `implementation/scp_hsr/hsr_components_verify.py` |
| [Paired rising quarter-turn authoring example](00_pieces/blind-hsr-rise-quarter-turn/README.md) | `implementation/scp_hsr/hsr_blind_rise.py`, selected by `hsr_reusable_components.py` and built by `hsr_components.py` | `implementation/scp_hsr/hsr_blind_rise_verify.py`, dispatched by `hsr_components_verify.py`; `tools/check_blind_rise.py` checks the saved combined example. |
| [Parallel HSR/Road authoring example with two side pillars and paved sidewalks](00_pieces/blind-hsr-road-stack/README.md) | `implementation/scp_hsr/road_stack.py`, dispatched by `rail_features.py` | `implementation/scp_hsr/road_stack_verify.py`, dispatched by `rail_feature_verify.py` through the shared `scp.py verify` command. |
| Shared height-aware surface unions and inclined support contacts | `implementation/scp_hsr/hsr_mesh.py` | `implementation/scp_hsr/hsr_mesh_verify.py` |
| Shared rail clipping, native templates, model packing, and pillar primitives | [implementation/scp_hsr/single_track_models.py](implementation/scp_hsr/single_track_models.py) | The owning recipe's independent literal verifier and the [shared model-preservation contract](../../docs/FRAMEWORK_ENGINEERING.md#model-and-render-preservation). |
| Menu artwork and text vocabulary | `implementation/scp_hsr/icons.py`: `icon_identity(style)`; `menu.py` consumes the same identity | The [shared menu-resource contract](../../docs/FRAMEWORK_ENGINEERING.md#builder-interface-and-verification) |

A height change needs its own explicit contract; do not weaken a same-height verifier to admit it. Registration and allocation ledgers describe current types only. Do not reconstruct deleted prototypes from older scripts.

For mixed HSR/Road work, audit the actual ordinary Road approaches as well as the elevated donor. The trial found ordinary Road PATH `296678f7-69668828-00004b00` and texture instance `00004b0e` outside the reduced pinned HSR fixture; a crossing's sidewalk offsets can differ from the ordinary Road override. Those are source-discovery examples, not a general compatibility promise. Use the shared [resource-discovery and narrow-capture procedure](../../docs/FRAMEWORK_ENGINEERING.md#inspect-additional-donor-resources) to identify exact archives and variants, record their fingerprints, and compare actual routes and materials before adapting them. Do not substitute an available but different texture or add a whole conflicting override archive merely to obtain one resource.

The [paired quarter-turn](00_pieces/blind-hsr-rise-quarter-turn/README.md) and [parallel HSR/Road stack](00_pieces/blind-hsr-road-stack/README.md) are the maintained end-to-end examples for new piece work. Their permanent IDs are `blind-hsr-rise-quarter-turn` and `blind-hsr-road-stack`; the historical `blind-` prefix remains part of those identifiers. The quarter-turn demonstrates measured paired native boundaries at different levels. The stack demonstrates one boundary requiring HSR, Road-vehicle, and pedestrian groups together, with independently checked side-pillar clearance and opaque pavement panels. Keep each example's literal heights, source resources, geometric exceptions, and evidence in that example's own definition, implementation, and README. Follow the shared creation and documentation workflows for the general procedure rather than treating either example's measurements as a new domain-wide default.

### Registration and artwork tools

Run the following commands from the parent project directory containing `custom-pieces`, after the editable installation in [BUILD_AND_INSTALL](../../docs/BUILD_AND_INSTALL.md#build-a-selected-collection). They require the configured development dependencies, including Pillow, and do not change Plugins or city files. Several commands also register definitions and allocations; they are not artwork-only refreshes. Run Python module commands from this parent directory: running them inside `custom-pieces` can make its `scp.py` file shadow the `scp` package.

| Scope | Command | Contract |
| --- | --- | --- |
| Current HSR artwork | `python3 -m scp_hsr.icons --root custom-pieces` | Regenerates every registered HSR piece's icon and the contact sheet; add `--output custom-pieces/local/icon-review` to stage an isolated artwork review. |
| Current HSR assembly artwork | `python3 -B custom-pieces/scp.py assembly-icons --domain high-speed-rail` | Regenerates each registered assembly's canonical `icon.png` beside `assembly.json`; changes no definitions, allocations, build, installation, or observations. |
| Modular track/branch/ramp/crossing catalogue | `python3 custom-pieces/domains/high-speed-rail/tools/update_interchange_catalog.py` | Allocates new IDs, distinct icons, and named sets; refuses to change a reserved layout. |
| Revised scissors switches | `python3 custom-pieces/domains/high-speed-rail/tools/update_rail_repairs_catalog.py` | Registers the current revised switch modules and icons. |
| Accepted straight smooth T | `python3 custom-pieces/domains/high-speed-rail/tools/register_directional_t.py` | Preserves the allocated straight-piece identity on reruns. |
| Accepted diagonal smooth T | `python3 custom-pieces/domains/high-speed-rail/tools/register_diagonal_t.py` | Registers the separate diagonal piece without overwriting the straight piece. |
| Reusable HSR components | `python3 custom-pieces/domains/high-speed-rail/tools/register_hsr_components.py` | Resolves the existing unique recipe owner before allocating a new type, preserves its permanent ID even when it differs from the recipe's spelling, and rejects ambiguous ownership. |

To refresh only the human inventory views from existing records, use `python3 custom-pieces/scp.py inventory` from the same parent directory. Inventory refresh does not extract changed resources, verify a DAT, or record manual passes. The domain's `AGENTS.md` routes changes to the appropriate owning source before these tools run.

## Connection levels and piece families

The shared connector model defines boundaries and movement compatibility. In the current reviewed rail sources, a paired arrangement has two tracks carrying opposite directions. The existing narrow branch family is authored one-way; a physical single channel is not inherently one-way, and another source must declare its own permissions. Measured member positions, headings, heights, grades, and modes remain the comparison facts.

| Connection label | Train-path height | Outside deck width / permitted neighbour |
| --- | ---: | --- |
| GHSR / Ground | 1 m | Matching ground paired or narrow profile, as declared |
| HSR / L2 | 15.5 m | Native paired profile is 15 m wide; centred narrow track requires its own matching profile |
| Authored Rail L3 | 23 m | Matching authored narrow profile; the tight paired-corner joint is separately Custom (23 m), with nominal level unassigned |
| Rail L4 | 30.5 m | Upper paired profile is 15 m; separate component curved-ramp ends are 8 m single-track profiles |

The level numbers use NAM's nominal 15, 22.5, and 30 m names; PATH heights describe train positions rather than deck tops or undersides. A single-track end does not join one lane of ordinary paired HSR directly. Native stations, bridges, and neighbour connections require independently established matching contracts; authored levels do not create that compatibility.

The eight directed narrow height ramps cover both directions of GHSR ↔ HSR L2 (eight tiles), HSR L2 ↔ Rail L3 (six tiles), Rail L3 ↔ Rail L4 (six tiles), and HSR L2 ↔ Rail L4 (eight tiles). Select the exact entry-to-exit name. A paired-to-single adapter changes width and spacing at one height, so it cannot replace a grade ramp. A **grade** is vertical rise divided by horizontal route distance: 15.625% means 15.625 m rise per 100 m horizontal travel, not a realistic high-speed railway recommendation.

Ground and HSR branch mainlines retain both directions; their outgoing or incoming narrow branch is one-way. L4 branch mainlines are also single-track. Orthogonal 45°/90°/135° branches and their Compact/Wide variants are separately authored types; four quarter-turn rotations do not create additional 45° orientations or reflections.

| Reviewed family | Individual engineering notes |
| --- | --- |
| Diagonal S-curves | [HSR Left](00_pieces/rail-hsr-diagonal-s-left/README.md#engineering-contract), [HSR Right](00_pieces/rail-hsr-diagonal-s-right/README.md#engineering-contract), [GHSR Left](00_pieces/rail-ghsr-diagonal-s-left/README.md#engineering-contract), and [GHSR Right](00_pieces/rail-ghsr-diagonal-s-right/README.md#engineering-contract). |
| Adjacent crossovers | [HSR Left](00_pieces/rail-hsr-adjacent-crossover-left/README.md#engineering-contract), [HSR Right](00_pieces/rail-hsr-adjacent-crossover-right/README.md#engineering-contract), [GHSR Left](00_pieces/rail-ghsr-adjacent-crossover-left/README.md#engineering-contract), and [GHSR Right](00_pieces/rail-ghsr-adjacent-crossover-right/README.md#engineering-contract). |
| Revised adjacent scissors | [HSR](00_pieces/rail-hsr-adjacent-scissors-revised/README.md#engineering-contract) and [GHSR](00_pieces/rail-ghsr-adjacent-scissors-revised/README.md#engineering-contract). |
| Native two-way height transition | [HSR to GHSR](00_pieces/rail-hsr-ghsr-transition/README.md#engineering-contract). |

Adjacent paired mainline centres are 16 m apart with no empty column between them. The switch block preserves both mainlines and their travel directions. There is no implemented diagonal scissors or equivalent compact switch between different heights. Combined crossings own both upper and lower routes wherever they share a tile. Independent overlapping fillers may replace an existing lower route. Surface GHSR below HSR is a visible ground railway; below GHSR requires underground/tunnel work that this kit does not implement.

## Saved rail design review

`junction-design-review.json` retains the measured review of 130 current pieces. Thirty-two modular branches/crossovers need a support-spacing review; no measured wall-defect records remain in this catalogue. The two accepted smooth T junctions have separate independent audits and are outside this earlier review's scope. The 2.6 m support-centre cutoff is a visual-authoring convention, not an engineering rule. No recorded objection is not game compatibility.

`../../framework/scp/design_review.py` validates the separate `design_review` flags. `tools/apply_junction_review.py` applies the saved evidence idempotently, refreshes per-piece review flags and inventories. Flags appear in individual previews and future menu titles/tooltips. Preserve them when regenerating catalogues; never clear them merely because static checks pass. Release assessment also looks up current flags by permanent ID, so an older manifest cannot hide a newer objection. Review evidence and generated views must refer only to currently registered pieces. The JSON remains authoritative; there is no separate review Markdown catalogue.

## Reviewed smooth-T floor compilation

The accepted [straight smooth T](00_pieces/directional-hsr-t-smooth-at-grade/README.md#engineering-contract) and [diagonal smooth T](00_pieces/directional-hsr-t-smooth-diagonal-at-grade/README.md#engineering-contract) own their literal dimensions, routes, support plans, and bounded endpoint exceptions. Their source and registration tools are in the implementation map; the following shared compiler scope applies only to those reviewed recipes.

The first smooth-T audit also exposed a near-parallel polygon-clipping defect: the older clipper accepted an EPS band but intersected at a different plane, allowing out-of-segment intersections and reversed floor triangles. The new recipe's robust floor union uses the same exact plane for classification and intersection, checks every interpolation fraction, and preserves rail UV priority. Keep this behavior confined to the reviewed smooth T recipes; do not change other current models incidentally. The independent mesh checker measures actual coplanar overlaps, full-width bed coverage, and visible-rail-to-PATH coverage. Its meshing tolerance is explicit. The historical catalogue review did not certify all old floors against this new overlap audit; do not imply that it did. Native bed vertices also vary by about two micrometres around their average height. When replacing the old flat faces, use the donor's existing 0.0001 m coplanarity definition: a 0.000001 m filter leaves some original faces behind and duplicates them beside the reconstructed surface. This classification does not relax the independent overlap audit.

## Shared rail surface and profile algorithms

`implementation/scp_hsr/hsr_mesh.py` owns shared height-aware floor unions and slope-seated supports. Overlapping upper and lower deck projections remain separate surfaces; join only genuinely coplanar floors. Rail textures take priority over ballast. Within one non-self-crossing swept sheet, resolve its warped rail/ballast triangulations locally before the height-aware global operation. Do not use a height-blind local union on a sheet that crosses itself at different heights. Preserve all real surface planes, full-width corridors, and nine underside contacts for every support head. The independent audits live in `implementation/scp_hsr/hsr_mesh_verify.py` and take component-specific contracts rather than importing any generation code.

At a coincident mainline branch collar, preserve the native paired slab and parapet exactly while opening the branch wall. The native paired parapet begins 3.996547698974609 m from its track centre; a generic 4 m branch shoulder can cut 3.4523 mm into it. Apply any authored collar adjustment only to the declared shared interface, retain the 5.2 m train corridor and separate 8 m single-track end, and keep the strict 0.00005 m profile tolerance. Do not narrow branches or relax profile checks globally.

Profile checks intersect actual triangles with the declared port plane and mathematically clip section intervals to that port tile's exact lateral span [-8, +8] m. A plane can also hit a distant legitimate branch; that geometry does not belong to the port's own tile. Use interval clipping, not vertex-only filtering. Keep the complete mesh, 5 × 5 m train-clearance, footprint, and construction checks global.

Each connection module loads its own `00_pieces/<piece-id>/geometry.json` through `hsr_partition_components.py`. `partition_layout` supplies local paths, `partition_info` supplies local metadata, and `model_inputs` supplies the analytic surface context, selected cells, and supports. `build_models` emits only that module's owned cells. Preserve the complete sweep samples needed for exact miters and floor unions; the context is not an additional placed piece. Literal independent contracts belong to `hsr_partition_components_verify.py`. Complete-layout joins and route contracts belong with the owning assembly; see the [trumpet testing reference](01_assemblies/straight-stem-trumpet/TESTING.md).

Models reuse the reviewed height-aware floor union and one global support plan per component. `_compile_models` in `hsr_mesh.py` accepts an optional `sweep_function`; the default remains the original native sweep, preserving all existing recipe geometry. New components pass their wrapper, which delegates unchanged for all non-tapered sheets. Follow the shared framework model-preservation and render-budget contract for every zoom and preview.

## Reusable component implementation

Select reusable components with `--set hsr-all-components`. The generated [collection list](README.md#inventories-and-collections) records current counts; registration does not install a piece or establish game compatibility.

Follow the design workflow to atomize useful track modules. A combined overpass can own both levels when separate pieces would claim the same tile. Individual pillars, render groups, and model fragments are not useful track connections by themselves.

`implementation/scp_hsr/hsr_components_layout.py` owns complete directed routes, physical decks, and literal sparse construction cells. Its public entry points include `RECIPES`, `INFO`, `component_routes`, `physical_decks`, and `component_layout`. `implementation/scp_hsr/hsr_components.py` builds models, rules, and resources; `build_hsr_component(spec, context)` returns `(assets, rules)`. Independent literal contracts belong to `implementation/scp_hsr/hsr_components_verify.py`. Registration preflights layouts, JSON definitions, and icons before writing current records. The [piece inventory](00_pieces/INVENTORY.md) links current buttons, exact pictures, and connection/test sections.

| Component contract | Owner |
| --- | --- |
| Compact paired-to-single adapter | [hsr-component-upper-paired-to-single-adapter-compact](00_pieces/hsr-component-upper-paired-to-single-adapter-compact/README.md#engineering-contract) |
| Compact parallel split | [hsr-component-lower-zero-turn-split-compact](00_pieces/hsr-component-lower-zero-turn-split-compact/README.md#engineering-contract) |
| Compact parallel merge | [hsr-component-lower-zero-turn-merge-compact](00_pieces/hsr-component-lower-zero-turn-merge-compact/README.md#engineering-contract) |
| Flat symmetric split and return | [hsr-component-lower-zero-turn-split-merge](00_pieces/hsr-component-lower-zero-turn-split-merge/README.md#engineering-contract) |
| Symmetric graded Y | [hsr-component-symmetric-graded-y](00_pieces/hsr-component-symmetric-graded-y/README.md#engineering-contract) |
| Standard lower one-way quarter-turn | [hsr-component-lower-oneway-curve90-right](00_pieces/hsr-component-lower-oneway-curve90-right/README.md#engineering-contract) |
| Tight paired corner, L4 to custom | [hsr-component-tight-paired-curve90-l4-to-mid](00_pieces/hsr-component-tight-paired-curve90-l4-to-mid/TESTING.md#3-software-checks) |
| Tight paired corner, custom to L2 | [hsr-component-tight-paired-curve90-mid-to-l2](00_pieces/hsr-component-tight-paired-curve90-mid-to-l2/TESTING.md#3-software-checks) |
| Upper paired straight | [hsr-component-upper-paired-straight](00_pieces/hsr-component-upper-paired-straight/TESTING.md#3-software-checks) |
| Paired L2/L4 ramp | [hsr-component-paired-ramp-l2-to-l4](00_pieces/hsr-component-paired-ramp-l2-to-l4/README.md#engineering-contract) |
| One-tile paired crossing | [hsr-component-modular-crossing-core](00_pieces/hsr-component-modular-crossing-core/TESTING.md#3-software-checks) |
| Full paired-to-single adapter | [hsr-component-upper-paired-to-single-adapter](00_pieces/hsr-component-upper-paired-to-single-adapter/README.md#engineering-contract) |

The two standard upper paired turns and four single curved height ramps retain separate [right paired](00_pieces/hsr-component-upper-paired-curve90-right/README.md#engineering-contract), [left paired](00_pieces/hsr-component-upper-paired-curve90-left/README.md#engineering-contract), [right L2→L4](00_pieces/hsr-component-oneway-curve90-right-l2-to-l4/README.md#engineering-contract), [right L4→L2](00_pieces/hsr-component-oneway-curve90-right-l4-to-l2/README.md#engineering-contract), [left L2→L4](00_pieces/hsr-component-oneway-curve90-left-l2-to-l4/README.md#engineering-contract), and [left L4→L2](00_pieces/hsr-component-oneway-curve90-left-l4-to-l2/README.md#engineering-contract) contracts. Full-length and compact variants remain different types, and the wider curves retain their own bounds. Do not move their ports to make another variant fit.

Independent component-family tests cover literal ports, direction, full-width decks, floor overlaps, visible rail-to-PATH agreement, five-metre train corridors, support spacing, nine underside contacts per pillar, runtime tile addresses, and binary mutation controls. Encoded assembly tests use disjoint occupied cells for the paired ramp/crossing/straight, both paired half-circles, and the full adapter with two curved ramps; each is checked under four proper rotations. Individual adapter collar sample positions belong to its own contract.

These are software checks. Actual placement, traffic, level isolation, moving train clearance, terrain, zooms, demolition, shadows, and save/reload remain unverified. Supports are coordinated within one component; a complete junction still needs a review across component boundaries and an exact dimensioned assembly with the existing splits and merges.

### Extending SCP static parts with native draggable HSR

The reported extension failure concerns **our custom SCP parts**: dragging Monorail into or out of them does not establish the intended HSR extension unless a native HSR starter is nearby. This report does not describe ordinary NAM HSR as broken. A **static part** has construction-defined cells and models; a **starter** also supplies the network state that makes a dragged base network adopt an override such as HSR. Native-compatible models and encoded travel paths do not, by themselves, make a custom part a starter.

In the inspected installed NAM DLL 1.3.1 implementation, an adjacent cell marked immovable or belonging to a network lot is represented as tile ID `0` during RUL2 adjacency matching. Therefore, adding a rule keyed to a custom model's tile ID alone is not an established solution for a static neighbour. See the [versioned native evaluation code](https://github.com/NAMTeam/nam-dll/blob/1.3.1/src/Rul2Engine.cpp#L298-L305). Do not change all Monorail beside ID `0` into HSR: that ID also represents unrelated immovable neighbours.

The current workaround is to place a native HSR starter beyond a **compatible centred paired L2 end**, then use the Monorail tool to extend that native HSR connection. Check the declared channel positions, outward heading, edge grade, and 15.5 m path height first. This workaround does not establish native continuation from an L4 end, a single-track end, or an edge carrying several services together.

A candidate authoring approach is the hybrid used by native construction rule [`C215`](https://github.com/NAMTeam/Network-Addon-Mod/blob/7f9cf55ad5a0c3cf4dcd2e61de9b29ced1e69b68/Controller/RUL0/C000_Monorail/C200_GHSR.txt#L1086-L1110): retain the static model cells and add optional external check cells carrying a **false intersection**, a deliberate combination of base-network flags that seeds an override. Investigate that mechanism without copying its height-transition geometry. This is a candidate under investigation, not an implemented or verified SCP feature. Declare every adjacent check or helper plot, its actual network flags, its allowed orientations, and its placement constraints; distinguish these plots from the part's owned model cells, and check their interaction with neighbouring construction. Preserve the part's IDs, geometry, and PATH resources.

**Optional does not mean passive.** The inspected original executable applies missing network flags from optional cells as construction requests. Its earlier collision preflight checks protected occupants before the later commit guard preserves them. An external helper requesting a missing Road marker beside another protected custom part is therefore expected to block placement; this particular occupied-neighbour result still needs game confirmation. Do not enable helpers at every reusable end or assume that an existing custom neighbour is skipped safely.

The narrower proposal is a **starter-enabled terminal variant**, a construction variant used only at an exposed end of an assembly. Put a helper on the outward side, require an empty or reviewed compatible dynamic-native helper plot, and retain the plain inward side for adjoining custom modules. Keep ordinary interior construction unchanged. The trumpet has three exposed paired L2 arms, west, south, and east; they are candidate terminal locations, rather than permission to change all their constituent pieces. Local one-ended straight fragments retain the existing modeled tile address, meshes, and PATH resources, but remain uninstalled, and do not establish safe game operation or an unchanged construction reach. Seamless initiation from arbitrary existing static parts without helper plots requires separately designed runtime integration; no RUL2-only solution has been verified.

Acceptance requires separate game observations for drag initiation and extension, survival after deleting one connected tile, and traffic operation. A successful drag test does not resolve the reported demolition failure, and a matching encoded path does not prove either behavior. Record each result against its exact packaged bytes and layout through [TESTING.md](../../docs/TESTING.md).

## Measured rail rendering evidence

The 2026-10-19 game screenshot showed pillars and shadows with missing deck surfaces. Large authored groups contained up to 44,628 stored vertices; the visible modular examples were much smaller. Native-library inspection found no group above 4,096 vertices among 403,543 groups. This supports a group-size diagnosis but does not establish an exact engine limit or prove the repair in the game.

The representation repair in 0.5.0.dev2 is an authorized exception to earlier instructions freezing model bytes. Piece IDs, encoded traffic paths, visible geometry, materials, and shadows remain unchanged. The shared framework model-preservation contract owns the all-groups verification rule. This records the scope of that historical repair, rather than a standing permission to change other resources.

Generic budgets, full encoded-triangle/float32 preservation, structural-shadow quantization guards, and their tests are in [framework engineering](../../docs/FRAMEWORK_ENGINEERING.md#model-and-render-preservation) and its [shadow contract](../../docs/FRAMEWORK_ENGINEERING.md#structural-shadow-quantization).

## Native rail donors and service classification

The shared [coordinate-frame contract](../../docs/FRAMEWORK_ENGINEERING.md#coordinate-frames-and-boundary-edges) defines tile positions, SC4PATH/S3D axis conversion, and edge numbers. Transport class `7` is the Monorail traffic class used by these registered HSR/GHSR sources; a class number outside that source context does not establish HSR compatibility.

The audited NAM 50 right-hand-running donors are:

| Donor | PATH height | Source instance ID | Visible profile |
| --- | --- | --- | --- |
| Straight HSR | 15.5 m | `5dd31500` | Bed approximately 16.18933 m; bottom 14.01067 m; top 16.98933 m |
| Straight GHSR | 1 m | `5dc31500` | HSR profile translated down exactly 15 m |
| Diagonal HSR half | 15.5 m | `5dd01a00` | Native asymmetric external offsets 2.8/2.9 m |
| Diagonal GHSR half | 1 m | `5dc01a00` | Same diagonal offsets at ground height |
| HSR/GHSR transition | 15.5 to 1 m | `5dcf1700` through `5dcf1770` | Eight complete model/PATH resources |

HSR and GHSR straight lanes use lateral offsets `+2` and `-2` m. A centred single-track branch uses a different port and requires a matching split/merge. Native diagonal offsets must match exactly at external ports. Internal seams must agree in all three coordinates.

### Measure the native diagonal half exactly

The audited NAM 50 right-hand donor PATH is `296678f7-a966883f-5dd01a00`, from `High Speed Rail.dat` pinned by the [dependency profile](../../config/profiles/nam50-rhd.json). Its decompressed PATH SHA-256 is `fa76b58784c3c536246c365291dbf5790f18adc0d5f8ec2bc7779ea763218636`. The following measurements describe that exact saved half at 0° rotation in the shared `[east,north,height]` metre frame. A **chord** is the vector from one saved route point to the next; these two-point records each have one chord.

| Native directed member | Entry point `[E,N,H]` (m) | Exit point `[E,N,H]` (m) | Travel chord `[ΔE,ΔN]` (m) |
| --- | --- | --- | --- |
| First route, north → west | `[-2.9,8,15.5]` | `[-8,2.8,15.5]` | `[-5.1,-5.2]` |
| Second route, west → north | `[-8,-2.9,15.5]` | `[2.9,8,15.5]` | `[10.9,10.9]` |

The north edge therefore has intersections at east `−2.9 m` and `+2.9 m`, while the west edge has intersections at north `+2.8 m` and `−2.9 m`. Its first chord is asymmetric; its second has equal components. After reversing the incoming travel direction to obtain the outward direction, the north-edge headings are approximately `44.4437°` and `45°`; the west-edge headings are approximately `224.4437°` and `225°`. Preserve the actual normalized vectors in comparisons. Labelling both members `45°`, mirroring one offset, or averaging the two offsets changes the source geometry.

Choose the actual complementary neighbouring half and one permitted placement before comparing a new piece. Rotate and translate the complete native resource, check both channels and their complementary travel directions together, and repeat the intended join under all four proper whole-layout rotations. Follow the [shared measurement procedure](../../docs/WORKFLOW_PIECE_CREATION.md#measure-the-complete-native-joining-boundary) for fingerprints, saved-output checks, and tolerances. This resource proves its measured positions, tangents, and 15.5 m height; it does not establish all diagonal variants, physical deck seams, arbitrary neighbouring construction, another NAM version, or game operation. Do not extend these exact tangent measurements to GHSR or another resource without decoding that source too.

### Nominal levels and service classification

The [NAM glossary](https://www.sc4nam.com/docs/reference/glossary/) calls the 15 m nominal level **L2**, 22.5 m **L3**, and 30 m **L4**. Existing HSR is already L2, with a 15.5 m PATH. Local native High Monorail PATH resources `5d1e5030` and the crossing `5d405a00` reach 30.5 m. Do not call a 30.5 m rail path L3. A newly authored intermediate rail profile must be identified as authored, rather than claimed as a native NAM HSR feature.

The registered [HSR source adapter](implementation/scp_hsr/hsr_connections.py) classifies engine `7` as the HSR family, with the reviewed 1 m ground variant classified as GHSR and primary routing role. Engine `6` is primary tram service. Engine `3` is a tram-related auxiliary only for the `tram_under_hsr` recipe, rather than an ordinary heavy-rail route. Other unresolved classes require explicit domain review. Keep service family, engine class, routing role, physical channel, and permitted modes separate.

## Rail-specific geometry and routing criteria

Apply the shared [geometry and routing invariants](../../docs/FRAMEWORK_ENGINEERING.md#geometry-and-routing-verification), [runtime tile lookup](../../docs/FRAMEWORK_ENGINEERING.md#runtime-tile-lookup), and [model preservation](../../docs/FRAMEWORK_ENGINEERING.md#model-and-render-preservation). Native rail donor facts and authored rail criteria below remain separately scoped; they are not universal vehicle collision thresholds.

- Preserve the native single-track rail texture band. A narrower slab painted with the whole two-track texture is not a correct single-track model.
- Sweep the authored **3 m width and 5 m height** envelope along interchange PATH segments. The current `_revised` scissors switches explicitly require **5 m width and 5 m height** instead. These are project dimensions, not a measured in-game train collision box. The unscaled Maxis Monorail engine/passenger S3D bodies are approximately 4.72 m wide; game scaling, replacement automata, and swept car-body corners are not established by this 3 m route audit.
- For mixed rail/Road or other mixed-service work, explicitly dimension every relevant corridor, including pedestrian and lateral-access routes. Check complete saved support solids against every segment using the [shared support procedure](../../docs/WORKFLOW_PIECE_CREATION.md#check-complete-support-solids-and-physical-space); a rail-only corridor, path-centre distance, or support-centre distance cannot establish lower-route clearance. Keep authored corridor dimensions separate from measured game envelopes.
- Check above-bed walls between PATH samples, not only at samples. Remove parapets from genuine branch openings. A visible deck beneath a train does not prove that a concrete wall no longer blocks it.
- The existing audited native HSR/GHSR ramp reaches a maximum sampled grade of approximately `0.236535` rise/run. A `0.25` authored bound must apply to every segment of a new route. This is a geometric prototype criterion, not a claim of realistic high-speed railway gradient.
- Structure-only cells need an explicitly audited purpose. The native `55387000` Monorail helper has an empty `SC4PATHS / 1.2 / 0 / 0 / 0` resource, proving that this empty format exists. Do not weaken the strict route parser to allow arbitrary missing routes. Permit an empty route only for declared structural cells and verify their models, reserved footprint, and zero construction edge flags.

A local path can enter and leave the same tile edge when a reviewed curve only grazes that tile. Native SC4PATH contains same-edge paths (for example `5f071800`), but this file format alone does not prove Monorail operation in game. Require an explicit independent contract and reject unintended same-arm U-turns in the complete external movement graph.

The independent modular interchange checker is `implementation/scp_hsr/interchange_verify.py`; its tests are `tests/test_interchange_verify.py`. Keep its expectations independent of `interchange_layouts.py` and `interchange_models.py`. The `test_interchange_assemblies.py` cases additionally connect split, level ramps, combined crossings, and merges across disjoint occupied city cells.

Generic coordinate conversion and cache requirements are not rail-specific; use the framework [coordinate](../../docs/FRAMEWORK_ENGINEERING.md#coordinate-frames-and-boundary-edges) and [cache/performance](../../docs/FRAMEWORK_ENGINEERING.md#cache-correctness-and-performance) contracts. A real source change requires donor re-audit and upstream extraction under the owning piece workflow.

## Test the actual game pathfinder

The static graph joins identical XYZ endpoints and proves which journeys the encoded files describe. It does **not** reverse engineer how SimCity 4 chooses inter-tile paths when the same Monorail edge has parallel routes at different heights. Native High Monorail crossing `5d405a00` has four transport-7 routes, all class 0, at 15.5/30.5 m. Its perpendicular directions demonstrate a native same-network crossing; they do not prove multilevel parallel-edge matching. A local scan of 52 Monorail/HSR/Hybrid Railway related DAT archives, containing 2491 PATH resources, found no constant-height parallel Monorail example with more than 7 m level separation and identical entry/exit edge pairs. This is a scoped search result, not proof that no such native resource exists elsewhere.

The original [SC4PATH format investigation](https://community.simtropolis.com/forums/topic/121-discovery-file-formats-the-positioning-formats-rul-and-sc4path/?page=5) describes class IDs per entry/exit pair, rather than persistent lane identifiers. Do not invent class numbers and claim they enforce vertical separation.

For the exact packaged bytes, build a disposable flat test city. Make a case with two co-oriented paths sharing a cell edge at different heights and separate origins/destinations. Give the lower route traffic demand without an upper connection, then reverse that arrangement. Inspect both route-query results and moving trains; neither route may transfer vertically at the seam. Repeat with opposite directions, all four rotations, save/reload, and an explicit intended height ramp as a positive control. Record artifact hashes, city layout, station endpoints, observations, and screenshots. Until these cases pass, describe no-transfer results as encoded-graph checks only.

## Current modular families

The modular expansion has 48 track/curve pieces, 48 split/merge branches, eight height ramps, and ten combined over/under crossing modules. The tram crossing, two smooth T junctions, and reusable-component collection are optional. Consult the generated [piece inventory](00_pieces/INVENTORY.md) and [collection list](README.md#inventories-and-collections) for exact current names, dimensions, and selection counts.

## Describe radius variants precisely

After native tangent collars, the ground/HSR modular 45/90/135-degree Wide branches have independently sampled minimum radii at least twice the Compact versions: approximately 31.388→86.285 m, 14.796→65.877 m, and 29.935→65.114 m. The centred L4 branches measure approximately 31.303→82.195 m, 16.975→68.197 m, and 31.412→66.630 m respectively. These measurements describe the modular branch variants; do not generalize them to other geometries.

## Compatibility, documentation, and evidence limits

New L3/L4 or other authored rail heights do not establish compatibility with native stations, bridges, neighbour connections, or arbitrary NAM pieces. Connect them through matching SCP ports and explicit height transitions. Passing below elevated HSR at ground level is a visible ground route. Passing below GHSR requires underground/tunnel work; do not describe a visible surface piece as an underground tunnel.

The existing profile targets an audited NAM 50 right-hand installation. Do not claim support for left-hand traffic, native macOS SimCity 4, another NAM release, or an altered controller without evidence. Preserve one coordinated controller overlay, rather than creating mutually overwriting per-piece overlays.

Follow the shared [documentation-generation workflow](../../docs/WORKFLOW_DOCUMENTATION_GENERATION.md#maintain-the-complete-preview-catalogue) for model previews, connector cards, README blocks, and their provenance. [TESTING.md](../../docs/TESTING.md) owns observation recording and stale results; [RELEASE.md](../../docs/RELEASE.md) owns identifier reservations, redistribution permission, and public platform/game evidence. Keep untested behaviors unverified, and preserve the actual case scope.
