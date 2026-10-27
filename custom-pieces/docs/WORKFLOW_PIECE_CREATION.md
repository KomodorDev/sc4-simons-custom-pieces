---
title: "WORKFLOW: Piece Creation"
summary: "Choose a reusable piece or modular assembly before allocation, then create justified pieces through measured boundaries, physical-space and render checks, independent verification, documentation, and packaging."
audience: "Piece authors"
document_type: "procedure"
---

# WORKFLOW: Piece Creation

A **piece definition**, `piece.json`, describes one reusable type. The generated build manifest records the resources and fingerprints produced from selected definitions. A **scaffold** is an unfinished registered entry; it does not create working geometry or traffic paths. This procedure orchestrates one new or revised piece. Use [BUILD_AND_INSTALL.md](BUILD_AND_INSTALL.md) for operator commands, [FRAMEWORK_ENGINEERING.md](FRAMEWORK_ENGINEERING.md) for shared technical contracts, and [WORKFLOW: Documentation Generation](WORKFLOW_DOCUMENTATION_GENERATION.md) for every artwork, README, catalogue, and connection-card generation step.

For an **existing piece**, open its README and `piece.json`, follow its `recipe` into the owning domain’s implementation map, and inspect its existing checks and evidence. Apply the [design-granularity decision](#0-decide-between-a-piece-and-an-assembly) before a substantial functional redesign. Preserve the registered piece and resource identifiers; skip scaffolding and allocation in sections 2 and 3. Continue with [section 4](#4-implement-the-recipe-and-the-independent-verifier), then the relevant verification, extraction, connector-generation, and documentation steps. Creating a separately selectable type uses the new-piece path instead. For a prose-only change, follow the [documentation refresh contract](FRAMEWORK_ENGINEERING.md#documentation-generation-and-observations).

If the piece is a missing module in an assembly, first use [WORKFLOW: Assembly Creation](WORKFLOW_ASSEMBLY_CREATION.md) to agree on the layout and prove why a new reusable type is needed. That guide owns assembly positions, atomization, and the handoff to shared documentation generation. A new piece definition does not create a whole-assembly one-click button.

Choose the owning transport domain before editing. Each type owns `domains/<domain>/00_pieces/<piece-id>/`, with its definition, artwork, connection records, and evidence. The domain player guide and engineering reference supply network-specific joining and donor contracts; the HSR [network specification and implementation map](../domains/high-speed-rail/NETWORK_SPEC.md#implementation-entry-points) identifies its actual generators, independent verifiers, and registration tools. Future highway types belong in their own domain, rather than the rail folder.

Extend an existing family only through its documented domain generator and independent verifier. Registration must preserve reserved identities and refuse unintended changes to an existing layout. The registry and allocation ledger describe current pieces; do not reconstruct deleted prototypes from older scripts. Use the [documentation-generation workflow](WORKFLOW_DOCUMENTATION_GENERATION.md) for inventory and other readable views; changed resources still require verification and extraction first.

## 0. Decide between a piece and an assembly

Make this decision **before scaffolding, reserving identifiers, or building detailed geometry**, even if the brief calls the requested design a “piece.” A **piece** is one independently selectable construction with a coherent reusable function. An **assembly** is a layout made from several placed pieces. **Design granularity** means choosing how much function belongs in each selectable piece. The size of a compiled file or its internal render groups does not make that choice.

1. List the requested functions: for example, a central crossing, approach splits and merges, connecting curves, and height transitions. Inspect the current catalogue for exact reusable types, rather than inventing another complete junction by default.
2. Identify functions that would be useful independently or in another layout. Look for repeated placements that could share one type under proven proper rotations. Visual symmetry does not prove that asymmetric paths, supports, or native joining collars are rotational copies.
3. Check whether proposed module boundaries can preserve complete measured connections and assign each claimed tile to one owner. Routes that share a tile, a branching floor, necessary walls, or coordinated supports may need to remain in one larger module. Follow the [smallest useful module rules](WORKFLOW_ASSEMBLY_CREATION.md#atomize-to-the-smallest-useful-reusable-module); do not split by arbitrary source curves, model chunks, or a fixed tile count.
4. Record the decision, reusable functions, proposed boundaries, and measured obstacles in the brief, then in the owning subject's existing README. Detailed cut decisions belong in the assembly's existing [atomization record](WORKFLOW_ASSEMBLY_CREATION.md#persist-atomization-decisions-and-coordinate-parallel-work). Do not create another decision-guide Markdown file.

| Design finding | Delivery decision |
| --- | --- |
| One bounded, independently useful function, including coordinated services that share its tiles | A single piece can be appropriate; prove its construction, geometry, and interfaces. |
| A complete complex junction with a core, branching regions, connecting curves, or independently reusable approaches | Use an assembly of reusable types under the [current assembly delivery policy](WORKFLOW_ASSEMBLY_CREATION.md#terms-and-evidence). Author only its missing modules. |
| An apparently reusable section has no proven safe cut or compatible existing replacement | Investigate that boundary first, retaining the smallest coordinated block required by its actual geometry and routes. Do not assume either a finished split or a monolithic final delivery. |
| A model exceeds a render-group budget | Correct its model packing under the [render-preservation contract](FRAMEWORK_ENGINEERING.md#model-and-render-preservation). This does not create gameplay modules or resolve the piece-versus-assembly decision. |

When an assembly is the better design, **tell the user before implementation**: “I will deliver this junction as an assembly of reusable, individually selectable pieces. I will not provide the complete junction as one selectable piece.” Explain the reusable functions and follow [WORKFLOW: Assembly Creation](WORKFLOW_ASSEMBLY_CREATION.md). Continue within the agreed functional brief; the announcement is not an automatic request for another approval. A complete one-click mechanism is a separate explicitly requested and independently proved project under that workflow's policy, rather than a promise inferred from the word “piece.”

**Example: the large fully connected diagonal HSR X.** Treat the complete junction as an assembly-design task. Investigate a coordinated central core, approach split/merge regions, connecting paired curves, and genuinely reusable diagonal approach sections. These are candidate functions, not an established part count or a claim that current catalogue pieces already fit. Preserve the required directed journeys and intended same-height conflicts while proving every cut, complete boundary, tile owner, support, and overhang. A successful one-piece prototype remains feasibility evidence; it does not establish that the final delivery has appropriate reusable parts.

This gate does not authorize redesigning accepted existing types, changing their identifiers, or rewriting frozen experiments. Preserve the existing accepted full-T pieces and other retained useful types. A documentation-only refresh does not trigger decomposition of an approved piece.

## 1. Open the project and inspect the existing pieces

Open a terminal. On macOS, press **Command + Space**, type **Terminal**, and press **Return**. A **checkout** is your local copy of the repository, and its **root** is the folder containing `custom-pieces/` and the repository README. In the following command, replace `/path/to/sc4-simons-custom-pieces` with that folder's full path, keep the single quotation marks so spaces work, and press **Return**:

```sh
cd '/path/to/sc4-simons-custom-pieces'
```

Then run:

```sh
python3 -m pip install -r custom-pieces/requirements.txt
python3 -m pip install -e custom-pieces
python3 custom-pieces/scp.py list
```

Run the two installation commands on first use of a source checkout. The `-e` option registers the shared and domain Python packages at their source locations. `python3` starts Python; `scp.py` is this project's command-line program. The `list` command shows the registered pieces. A registered piece can be disabled by default or still be a draft. Look at the piece's status before selecting it.

Use these two complete authoring examples when creating a new reusable type. They are experimental: their saved-resource checks and generated documentation do not establish operation inside the game. A **permanent ID** is the value used by selection commands; retain each existing ID when revising that type.

| Example | Permanent ID | What to follow |
| --- | --- | --- |
| [HSR Paired Quarter-Turn Level 2 to Level 4](../domains/high-speed-rail/00_pieces/blind-hsr-rise-quarter-turn/README.md) | `blind-hsr-rise-quarter-turn` | One curved, paired height transition, complete native joining boundaries, separate generation and verification, and the canonical angled/top pictures and connection cards. |
| [HSR above parallel Road](../domains/high-speed-rail/00_pieces/blind-hsr-road-stack/README.md) | `blind-hsr-road-stack` | Several required services sharing a boundary, a central pillar with explicit clearance evidence, service-separated cards, and permitted and forbidden movements. |

Open the example's README first, then its `piece.json`, `connections.json`, `connector-groups.jsonc`, and evidence links. Use the [HSR implementation map](../domains/high-speed-rail/NETWORK_SPEC.md#implementation-entry-points) to find its recipe and independent verifier. Copy the authoring sequence and documentation structure, then supply the new type's own measured routes, geometry, declarations, and evidence. Do not copy an example's game IDs, numerical exceptions, source fingerprints, or observations into another type. New piece guides use the [shared numbered README layout](WORKFLOW_DOCUMENTATION_GENERATION.md#piece-readme), including a generated intrinsic movement matrix.

Additional small examples and shared implementation entry points:

- `custom-pieces/domains/high-speed-rail/00_pieces/hsr-diagonal-ghsr/piece.json`: the two-tile elevated HSR over diagonal GHSR piece.
- `custom-pieces/domains/high-speed-rail/00_pieces/tram-under-hsr/piece.json`: the one-tile ground tram crossing beneath HSR. It is disabled by default.
- `custom-pieces/framework/scp/recipes.py`: code that builds the actual game resources.
- `custom-pieces/framework/scp/verify.py`: independent checks of the generated resources.

## 2. Create a draft and allocate its local identifiers

Choose a unique **slug**, meaning a short lowercase identifier containing letters, numbers, and hyphens. For this example use `example-crossing`. Decide its occupied width and depth before assigning its identifiers. This example uses one tile across and two tiles deep.

The concrete example uses the `high-speed-rail` domain. For a different network, select its registered domain explicitly and use its source specification; the following command does not implement that other network. Run:

```sh
python3 custom-pieces/scp.py scaffold --domain high-speed-rail --id example-crossing --name 'Example Crossing' --width 1 --depth 2
```

The command creates `custom-pieces/domains/high-speed-rail/00_pieces/example-crossing/piece.json`, registers the draft, and records its local identifiers in `custom-pieces/config/allocations.json`. Read the printed file locations and inspect the generated manifest. A draft cannot be included in a working build until its construction recipe and verification are implemented.

`--width` and `--depth` both default to 1 if omitted. Each must be a positive integer no greater than 16; the current scaffold supports at most 16 occupied tiles in total. For example, `--width 4 --depth 4` describes 16 tiles.

The **allocation ledger** records which identifiers belong to each current piece. Do not take another current piece's numbers. Local allocation prevents collisions inside this project; it is not a public reservation with the NAM Team. See [the release requirements](RELEASE.md). The ledger also records occupied coordinates and the construction base. Correct a draft's allocation before enabling it; a working piece's manifest and allocation must agree.

If `example-crossing` already exists, choose another slug and use that slug consistently in the commands below. Do not overwrite an existing piece to make the example command succeed.

## 3. Complete the manifest

Open `custom-pieces/domains/high-speed-rail/00_pieces/example-crossing/piece.json` in the editor. JSON uses double quotation marks around field names and text values. Its Boolean values are the unquoted words `true` and `false`.

Review these fields:

| Field | What to supply and why |
| --- | --- |
| `id` | Keep the allocated slug. It identifies this piece in selection commands. |
| `name` | A unique reusable name describing network, level, movement, and profile. Write nominal levels in full, such as `Level 2` and `Level 4`; this is the safest source form for shared picture titles. Do not use an assembly P-label or cardinal placement role. |
| `description` | State the crossing directions, levels, and any relevant placement limitation. This becomes player-facing information. |
| `recipe` | A Python-style name, such as `example_crossing`, matching the implementation selected by `build_piece`. Use lowercase letters, numbers, and underscores; do not put a path here. |
| `enabled_by_default` | Keep `false` during development so ordinary builds do not silently add the unfinished experiment. |
| `status` | Keep `draft` until the recipe and its verification exist. Use `experimental` for a build that still needs game tests. Use `tested` only when its test evidence supports that claim. |
| `puzzle_id`, `tile_ids`, `preview_id`, `menu.id` | Keep the values assigned in the allocation ledger. They link the game's resources and construction definitions. |
| `footprint` | The width and depth of the bounding rectangle, for example `[1, 2]`. By default every cell is occupied. Scaffolding permits dimensions from 1 through 16 and at most 16 cells in total. Reviewed larger layouts require explicit allocation and the address checks below. |
| `cells` | Optional list of occupied `[column, row]` coordinates. The construction anchor `[0, 0]` may be empty. Use this for an L-shaped footprint. Tile IDs must appear in the same order and follow the native grid offsets. |
| `orientation_count` | Eight entries. Supply audited reflections where appropriate, or four proper rotations repeated twice for a directional piece. Do not assume reflection preserves a one-way train path. |
| `dependencies` | Names from the selected profile's `files` table, including `controller`. Add each donor archive the recipe reads. |
| `menu` | The owning domain's menu button ID, ordering value, and supported icon style; this example uses the Rail menu. See [the native menu contract](FRAMEWORK_ENGINEERING.md#native-menu-resources). |
| `shadow_mappings` | For each affected tile, the native or newly generated shadow source and rotation. A generated source must supply all five zooms in that piece's DAT. Model correctness does not prove in-game shadow selection. |
| `provenance` | Identify the geometry and rule donors and the actual redistribution-permission status. Do not mark permission as recorded unless evidence exists. |
| `game_tests` | Keep each result `unverified` until that exact behavior has been tested in the game. Record failures as `failed`. |

The scaffold reads the selected domain registry's `scaffold.dependencies` and `scaffold.menu_style`. The current rail defaults are `controller`, `hsr` and the `diagonal-hsr` icon style; the reserved highway domain starts with only `controller` and a draft style. These defaults are a starting point, not proof of the donors a new recipe needs. For example, the existing diagonal GHSR crossing also needs `urail` for its donor models and paths.

For example, `interchange-hsr-split-90-compact` has `footprint: [2, 2]` and `cells: [[0, 0], [1, 0], [0, 1]]`. It occupies the top-left, top-right, and bottom-left cells. Its tile IDs are `base`, `base + 0x100`, and `base + 0x10`, in that order. The bottom-right cell is unoccupied. `0x` means hexadecimal, or base 16: `0x100` is 256 in decimal and `0x10` is 16. Without `cells`, rectangular pieces use row order: left to right, then down. For a diagonal S-curve the first occupied cell can be `[2, 0]` or `[2, 1]`. The allocation base is the first actual tile ID minus `column * 0x100` minus `row * 0x10`. The game's construction offsets instead start at the smallest modeled column and row. Therefore `AutoTileBase` is the allocation base plus `minimum_column * 0x100 + minimum_row * 0x10`. `PlaceQueryID` still points to the first actual tile exemplar. Do not create a fake network tile in an empty anchor cell. `scp.catalog.auto_tile_base` calculates this adjusted base. Reserve the correct IDs before enabling a new sparse piece. Never move an already released cell to a different coordinate under its existing tile ID.

### Check the game's tile-address calculation

An **address** identifies a resource such as a model or traffic path. The game builds a one-byte lookup key for each modeled cell; two different cells can receive the same key, so unique resource IDs alone do not make a large or sparse piece safe. The canonical [runtime tile-lookup contract](FRAMEWORK_ENGINEERING.md#runtime-tile-lookup) defines the exact byte arithmetic, additive `AutoTileBase`, modeled origin, resource families, and required tests.

For example, modeled cells `(19,4)` and `(3,5)` both receive key `0x54`. The later cell replaces the earlier lookup entry regardless of the chosen base. A fully modeled area no larger than 16 × 16 has unique keys, while a wider sparse area can also be valid if its actual cells have distinct keys. Check actual modeled coordinates rather than imposing an unsupported width limit or assuming that a new base repairs a collision.

Before registration, use `framework/scp/autotile.py` to validate the modeled origin, lookup uniqueness, selected resource IDs, and all five zoom slots. The independent verifier must decode the emitted construction rules and verify those facts again; a correct manifest cannot repair incorrect controller rules. Include a colliding layout tested with different bases and a valid wider sparse layout as negative and positive controls. A prototype with an explicitly failed placement result remains inspectable, but must not become a selectable build.

A **dependency profile** pins the supported input archives and their SHA-256 fingerprints, meaning hashes identifying exact file bytes. The existing profile is `custom-pieces/config/profiles/nam50-rhd.json`; `rhd` means right-hand traffic. Inspect and re-audit a changed donor before updating its fingerprint, and add an audited entry for a new dependency. This input profile is separate from optional connector defaults.

## 4. Implement the recipe and the independent verifier

The shared `custom-pieces/framework/scp/recipes.py` dispatches through the domain registry's `implementation` package. Implement the new recipe in that owning package's `build_piece(spec, context)` path, following its actual return structure. Register an explicit independent verifier for the recipe; unknown recipes must fail rather than inherit another type's passing result. Use the domain's implementation map for concrete source files and tools.

Keep generation and independent contracts separate. The recipe supplies actual geometry, traffic routes, asset resources, and its own construction additions. Shared parsing and resource helpers belong in the framework; domain geometry remains in the owning implementation package. A height change needs its own explicit contract rather than a weakened same-height verifier.

Each recipe contributes its own additions to one shared controller assembled from the audited clean input. It must not copy a complete earlier generated overlay into the piece. A **rotation ring** lists the construction states cycled by the game. The shared builder inserts each ring exactly once in the single `[Ordering]` section; use the canonical [controller composition contract](FRAMEWORK_ENGINEERING.md#controller-composition-and-verification) for return values, manifest fields, and saved-resource checks.

Verify the actual saved controller, including ring section context, selected definitions, and byte-for-byte recovery of the clean base after removing generated additions. Text presence alone is insufficient. These file checks do not establish in-game rotation controls; retain the corresponding manual cases until tested.

Check every part of the piece explicitly:

1. **Model geometry:** supply the visible transport surfaces, supports, and ground surfaces that are actually needed. A model is a collection of vertices and triangles. Preserve valid texture references and remove invalid animation references when adapting a donor. Pack authored geometry within the [per-render-group budgets](FRAMEWORK_ENGINEERING.md#model-and-render-preservation), and check every frame of all five tile-model zooms and the complete cursor preview in the actual saved resources. Oversized groups can appear in software previews while failing to display in the game. Dividing render groups preserves model geometry; it does not replace the design-granularity decision in section 0 or establish a game-rendering pass.
2. **Traffic paths:** supply every intended travel direction with the correct transport type, edge, channel position, and height. The visible model and the traffic path are separate resources; one does not create the other.
3. **Tile connections:** compare the complete exposed boundary at each actual shared tile edge, including all required services, physical channels, measured intersections, and permitted movements under one placement. Matching coordinates and heights for one endpoint are insufficient if another required continuation fails. Compare outside endpoints with the actual approach network's donor paths, and apply the shared [connector rules](CONNECTOR_METADATA.md).
4. **Construction rules:** declare the required networks, occupied cells, rotations, mirrors, and resource references. Use a native piece with the same network relationship as a starting point where one exists. Networks at different heights can still use the same underlying game network.
5. **Preview:** build the entire footprint in the cursor preview, including correct offsets for its tiles. Do not point the cursor at an unrelated donor model.
6. **Shadows:** reuse an appropriate native shadow with the correct orientation or deliberately supply and validate a new one. Do not relabel a narrower donor shadow as a match for a wider piece.
7. **Menu:** normal builds use a distinct button and a readable icon/title for each reusable type. Construction section identifiers must match the button's construction target. An explicitly requested browsing experiment may add another presentation or a shared type family through the [opt-in menu workflow](BUILD_AND_INSTALL.md#try-the-trumpet-menu-experiment); it must preserve independent selection, geometry, and permanent construction identifiers. An assembly-parts button selects one component at a time and is not a one-click interchange. Menu icon generation does not supply the construction rules.

Require the four proper rotations **0°, 90°, 180°, and 270°** for every new independently placeable piece. Independently inspect the emitted construction rules and occupied cells, actual models and traffic paths, entry/exit directions, matching ports, cursor previews and shadows in each rotation. Proper rotation turns the piece without reflecting it. One-way pieces repeat those four rotations when eight menu states are required; reflection must not silently reverse their travel directions. A 45-degree diagonal variant needs separate geometry and audited diagonal ports. It is not created by rotating an orthogonal piece through an additional 45 degrees. Static rotation checks do not replace four-direction placement and traffic tests inside the game.

Before adapting a donor, check the shared [SC4PATH/S3D coordinate conversion](FRAMEWORK_ENGINEERING.md#coordinate-frames-and-boundary-edges) and its domain-specific source conventions. Do not transform a new source using an assumed axis order. The shared [connector coordinate definitions](CONNECTOR_METADATA.md#3-positions-headings-heights-and-slopes-use-one-comparison-frame) define the comparison frame after source conversion.

### Measure the complete native joining boundary

A **complementary member** is the actual neighbouring route that continues one source member across the shared edge with the required travel direction. A **sampled chord** is the straight segment between consecutive saved PATH points; its direction supplies the encoded tangent at that end. Measure the actual approach before designing its joining collar, meaning the short end section that preserves that measured continuation.

1. Identify the exact donor archive, complete resource identifier, traffic-side/version variant, and source fingerprints. Decode its saved PATH, identify the intended neighbouring cell and proper rotation, and record which real tile edge will be shared. A resource absent from a reduced fixture is a discovery limit; it does not justify substituting a similar resource.
2. Record every required physical channel and directed member on that boundary, including its exact intersection, travel direction, first or last nonzero sampled chord, height, and edge grade. Preserve each member separately. Do not obtain the second channel by mirroring the first, replace asymmetric offsets with their average, or replace a measured chord with a nominal `45°` diagonal label. The [native diagonal HSR worked measurement](../domains/high-speed-rail/NETWORK_SPEC.md#measure-the-native-diagonal-half-exactly) shows why both channels matter.
3. Transform both complete boundaries into one layout frame using one permitted translation and rotation. Check complementary travel, coincident positions, opposite outward tangents, and complementary outward grades for every member together. Repeat the intended comparison under all four proper whole-piece rotations, using the [explicit connector tolerances](CONNECTOR_METADATA.md#5-matching-procedure-and-evidence). A successful first channel must not conceal a different position or tangent on the second.
4. Record the actual donor, placements, errors, and coverage in the owning piece's existing checks or evidence. Independently inspect the saved generated PATH again after building; an in-memory construction formula alone is insufficient. Keep native-boundary PATH agreement, physical deck-seam inspection, neighbouring construction, and game joining as separate evidence states.

### Check complete support solids and physical space

A **path corridor** is a volume reserved around a traffic route using explicitly chosen width and height. A **support solid** is the complete three-dimensional column, cap, foundation, or other supporting body. Choose corridor dimensions for every relevant service and mode before positioning supports, state their vertical reference, and label them as authored design assumptions unless a measured game envelope supports them. For example, a 3.0 m wide × 4.5 m high vehicle corridor and a 1.8 m wide × 2.2 m high pedestrian corridor are explicit authoring choices; passing them does not establish the dimensions or collision behavior of actual moving vehicles and pedestrians.

Inspect all saved support faces and full solid extents against every relevant PATH segment between samples, including lower services, lateral access paths, caps above a route, and foundations beside it. Check that declared closed solids have their expected faces and closure; a missing face must not make an obstruction disappear from the audit. A distance from a path centre to a pillar centre does not account for pillar width, and a point-only test can miss an obstruction between samples. State whether the checker handles axis-aligned boxes, curved sweeps, inclined solids, or another explicit geometric scope; do not generalize a box-only result to arbitrary supports. Report minimum horizontal and vertical margins with the chosen corridor dimensions and inspected resource hashes.

Keep four spatial facts distinct: the **construction rectangle** describes the declared width and depth; the **owned-cell mask** identifies the cells claimed by construction resources; the **physical projection** identifies ground-plane cells touched by actual saved geometry; and **keep-clear restrictions** identify space that neighbouring construction must avoid. Compute projection by intersecting actual triangles with tile areas, rather than checking vertices alone. List projections outside owned cells, support foundations, relevant height ranges, and any placement restrictions in the existing piece README and source-bound evidence. Changing the rectangle or drawing an ownership plan does not reserve an unowned overhang. A conservative projection can identify space to keep clear, but height-dependent collision and native-seam checks still need the actual placed geometry. Owned-cell overlap checks do not establish that physical fit; see the [connector evidence limits](CONNECTOR_METADATA.md#physical-projection-ownership-and-clearance).

### Keep independent checks and numeric exceptions scoped

An independent verifier must inspect saved resources against separately reviewed expectations. It may share neutral parsers, but must not import the route or model generator as its expected truth. If an audit reuses a generator-owned geometry helper, disclose that dependency and independently recompute the affected measurement before describing it as independent evidence. Include meaningful corruptions, such as a moved native endpoint, altered tangent, missing journey, shifted support, or missing support face, that the relevant check must reject.

A numeric exception must name the measured property, original bound, replacement bound, exact geometric subset, input resources, measured maximum, and remaining margin. Keep the default bound everywhere else. For a joining-collar exception, define the collar distance from actual joining ports and test both sides of that distance boundary, a value exceeding the replacement bound, absent opt-in, and unchanged recipes. Keep unrelated checks, such as visible rail-centre alignment, connector position/tangent tolerance, and physical clearance, unchanged. A justified visual stripe allowance is not permission to widen connector tolerances or claim a game collision limit. Store the particular numbers with the owning piece's engineering contract and evidence, rather than turning one exception into a domain-wide default.

Register the new recipe with its owning domain's independent verifier, reached through `custom-pieces/framework/scp/verify.py`; change shared verification only for genuinely shared behavior. Inspect the generated DAT to establish the intended geometry, references, routes, connections, construction layout, and shadow mapping. Apply the [shared geometry/routing checks](FRAMEWORK_ENGINEERING.md#geometry-and-routing-verification), [render preservation and budgets](FRAMEWORK_ENGINEERING.md#model-and-render-preservation), and the domain's numerical contracts. Repeating builder assumptions without inspecting output cannot catch a builder error. Unknown recipes must not inherit another type's passing result.

When that implementation exists, change the manifest's `status` to `experimental`. Replace a scaffold's generic `purpose` and description with the implemented behavior and its evidence limits, so a completed candidate no longer says only “Draft reusable piece.” Keep a new experimental type disabled by default during development, and leave its game-test results `unverified`.

## 5. Build and check only the new piece

Use a separate output folder so the experiment is easy to inspect:

```sh
python3 custom-pieces/scp.py build --include example-crossing --output custom-pieces/dist/example-crossing
python3 custom-pieces/scp.py verify --output custom-pieces/dist/example-crossing
```

`--include` selects the named piece explicitly, even when it is disabled by default. An unknown name must fail instead of silently building the default piece. Add another `--include` argument when selecting an additional piece.

If an experimental recipe, independent contract, or procedural icon changes, choose a fresh private output, such as `custom-pieces/dist/example-crossing-v2`. The builder checks an existing managed output before replacing it; a newly changed contract can therefore reject an older experiment before rebuilding it. Preserve that earlier evidence and use a new output name rather than weakening verification or deleting an unrelated directory.

Read the printed result and the generated manifest and verification report. Check the piece's identifiers, donor fingerprints, dependency locations, resource list, and limitations. A successful static check means the files passed those checks; it is not a game-test result.

Run framework registry and installation safety tests from the project folder:

```sh
python3 custom-pieces/scp.py check --scope framework
```

Then check the owning domain and, when relevant, the changed assembly:

```sh
python3 custom-pieces/scp.py check --scope high-speed-rail
python3 custom-pieces/scp.py check --scope straight-stem-trumpet-v4
```

Replace those identifiers with the actual domain or assembly. Use `python3 custom-pieces/scp.py check --scope all` for every registered check folder. The runner discovers framework, domain and assembly tests separately; ordinary discovery in `custom-pieces/tests` covers only the shared framework. These tests use temporary fixtures and must not install into the real Plugins folder or edit a city. When changing the builder or verifier, add tests that exercise a meaningful failure or invariant rather than checking only that the new branch exists.

### 5.1 Generate and check the piece's connector export and overview

After saved-resource checks pass, use the owning domain's verified extraction path to update measured connection records for an actual resource change. Define any new channel/cut associations and optional defaults under [CONNECTOR_METADATA.md](CONNECTOR_METADATA.md). These source-authoring steps precede visual and readable output generation; a renderer cannot repair stale measurements or supply missing associations.

Complete the applicable gates in [WORKFLOW: Documentation Generation](WORKFLOW_DOCUMENTATION_GENERATION.md) before handing the piece to an assembly. That one procedure owns icon coordination, standalone pictures, catalogue coverage, README sections, connector exports/cards, preservation checks, and their exact commands. New or intentionally migrated connector declarations require its full freshness check; unmigrated types retain their existing measured documentation until intentionally migrated. A later resource change returns to verification and extraction rather than a fingerprint-only update.

This validates the piece's own resources and connector facts. It does not scan every possible neighbour or create manual endpoint/counterpart cases. The current library does not supply automatic compatibility discovery. Any future consumer must restrict its comparisons to types with complete, current connector exports; an older unmigrated type retains its existing build status and has unknown compatibility.

## 6. Check the combined build

Once the new recipe can be built, run:

```sh
python3 custom-pieces/scp.py build --all
python3 custom-pieces/scp.py verify
```

`--all` selects all implemented, non-draft pieces, including experiments disabled by default. Drafts are excluded; explicitly selecting a draft with `--include` fails until its recipe is implemented and its status is changed. A combined build catches identifier collisions and shared-controller problems that a one-piece build can miss.

Use `python3 custom-pieces/scp.py doctor` to inspect the configured dependency and Plugins locations. Both the active user Plugins directory and the game's installation Plugins directory matter because either can contain a competing resource. Keep generated files outside Plugins while reviewing them.

## 7. Test in the game and record the evidence

First quit the game completely. Follow the [framework's installation directions](BUILD_AND_INSTALL.md) and use a disposable test city with flat, clear land. Keep the generated build and its hash with the test evidence so a later change does not inherit the earlier result automatically.

Use this procedure for focused game verification of new behavior, changed assumptions, or reported problems, and retain the evidence required by the release policy when preparing publication. Do not multiply it by an arbitrary shortlist of neighbour pieces. Matching follows the complete connection rules; software validation checks the actual generated files, while a game observation records only the stated behavior and environment.

Check, in order:

1. Find the intended menu button and select the new piece by its title.
2. Place every distinct supported rotation and explicitly supported reflected orientation.
3. Build the intended approaches at every outside connection. Confirm that the models meet and the heights stay correct.
4. Supply real travel demand using the network's required compatible access points or stations, homes, and jobs. Check every permitted service and direction with Route Query or observed movement. An unused route without demand is inconclusive.
5. Check that a crossing does not permit unintended transfers between levels.
6. Inspect the cursor, placed models, shadows, game zooms, and camera rotations.
7. Save the test city, reopen it, and inspect the piece again.
8. Test removal and rebuilding in the disposable city.

Use [TESTING.md](TESTING.md) to record each explicitly confirmed observation with its exact resources, environment, movement, and orientation. Any coarse `game_tests` summary must agree with all required current cases; a single rotation or software success cannot establish a whole-piece pass. Keep known failures visible in the record and user instructions.

## 8. Prepare packaging separately from publication

Finish the [final artwork and documentation sequence](WORKFLOW_DOCUMENTATION_GENERATION.md#final-artifacts-and-packaging) first. For a local experimental archive containing the current README, renders, connector exports, and observation views:

```sh
python3 custom-pieces/scp.py package --output custom-pieces/dist/example-crossing --refresh-docs
```

For the public-release assessment:

```sh
python3 custom-pieces/scp.py release-check --all
```

The release assessment checks the permission, identifier-allocation, platform-test, and publication-material records as well as piece-level evidence. Keep pending gates pending. The `package --release` option is for a build whose required release evidence is complete; it does not create that evidence. See [RELEASE.md](RELEASE.md) before distributing copied NAM assets or complete controller resources.

`source-package` prepares the framework's source package separately. A source archive, a local DAT build, a public-ready binary, and an uploaded release are four different outcomes. No successful local command should be described as having published a mod.

Packaging without `--refresh-docs` deliberately retains the original build-time documentation snapshot. With `--refresh-docs`, the ZIP receives current portable documentation and matching document hashes without rebuilding or changing the compiled resources. Connector freshness binds those compiled facts separately from documentation, so this final handoff does not invalidate an otherwise unchanged export.

## Controlled workflow reproduction

Use this separate procedure when evaluating whether another author can reproduce a functional brief from the documented workflow. **Blindness** means withholding earlier and sibling solutions from that author; it does not mean the filesystem necessarily prevents access.

1. Give each author a fresh conversation history, the same functional brief, an identical cleaned source baseline, and a separate workspace. Record the baseline archive and file hashes, allowed read/write roots, and comparison criteria before work begins.
2. Inspect the copied baseline and exported archive for prior solutions, sibling outputs, and unregistered piece drafts as well as `local/` and `dist/` contents. The registered catalogue alone is insufficient. Exclude those solutions from the experimental copy, preserve the originals, and record every omission and resulting baseline hash.
3. List the permitted native archives, resource identifiers, and fingerprints. Record all missing inputs, documentation gaps, failed commands, rejected geometry, workarounds, and coordinator interventions in the run's existing evidence, including how each issue was resolved or left uncertain.
4. Preserve command logs and tool session IDs as commands start, so interrupted work can resume through its own sessions without inspecting unrelated process command lines. Disclose incidental exposure to another solution's metadata or files and its possible effect on the result.
5. State whether isolation is procedural, technically enforced by permissions, or both. Separate workspaces on a shared filesystem establish a procedure, not proof that no other files were accessible or read.
6. Freeze the authors' final outputs and record their hashes before comparing them with the hidden reference. Compare required behavior and evidence, rather than demanding identical implementation bytes, then obtain independent saved-resource, artifact, and preservation reviews. Disclose the reviewers' dependencies and limits; software review supplies neither human image approval nor game observations.

## Names, previews, and documentation

Use [WORKFLOW: Documentation Generation](WORKFLOW_DOCUMENTATION_GENERATION.md) for reusable names, standalone pictures, readable output, and the exact generation/review sequence. Follow that procedure again after the final combined build if its source inputs changed. Keep the piece's particular behavior and limitations in its own README, and retain exact cases in `checks/manual-tests.json` under [TESTING.md](TESTING.md); a generation command cannot supply a human observation.

The [connector reference](CONNECTOR_METADATA.md) defines boundary/channel semantics. The shared generation procedure produces the related library-owned outputs for documentation and consumer applications. This creation workflow does not duplicate their schemas, card layouts, camera rules, or refresh commands.
