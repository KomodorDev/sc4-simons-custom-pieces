---
title: "Framework engineering reference"
summary: "Define shared resource addressing, controller composition, coordinate conversion, model and routing verification, preservation, caches, menus, and generator integration."
audience: "Framework developers and maintainers"
document_type: "reference"
---

# Framework engineering reference

<!-- BEGIN DOCUMENT NAVIGATION -->
[1. Source ownership and implementation entry points](#1-source-ownership-and-implementation-entry-points) · [2. Current identifiers and runtime addressing](#2-current-identifiers-and-runtime-addressing) · [3. Controller composition and verification](#3-controller-composition-and-verification) · [4. Coordinate frames and boundary edges](#4-coordinate-frames-and-boundary-edges) · [5. Model and render preservation](#5-model-and-render-preservation) · [6. Geometry and routing verification](#6-geometry-and-routing-verification) · [7. Cache correctness and performance](#7-cache-correctness-and-performance) · [8. Inspect additional donor resources](#8-inspect-additional-donor-resources) · [9. Native menu resources](#9-native-menu-resources) · [10. Mixed-network ownership](#10-mixed-network-ownership) · [11. Documentation generation and observations](#11-documentation-generation-and-observations) · [12. Installation and saved-resource constraints](#12-installation-and-saved-resource-constraints)
<!-- END DOCUMENT NAVIGATION -->

Read [STRUCTURE.md](../STRUCTURE.md) for the directory map, [BUILD_AND_INSTALL.md](BUILD_AND_INSTALL.md) for operator commands, [TESTING.md](TESTING.md) for recording observations, and [RELEASE.md](RELEASE.md) for publication requirements. For rail dimensions, donor evidence, and routing limits, read the [rail network specification](../domains/high-speed-rail/NETWORK_SPEC.md). The [assembly workflow](WORKFLOW_ASSEMBLY_CREATION.md) owns layout and atomization; [documentation generation](WORKFLOW_DOCUMENTATION_GENERATION.md) owns artwork, cards, README views, and their operator sequence.

<a id="source-ownership-and-implementation-entry-points"></a>

## 1. Source ownership and implementation entry points

The [project registry](../project.jsonc) names domain registries. Each domain has a short README and AGENTS router, a `domain.jsonc`, and named selections in `collections.jsonc`. One selectable type owns `00_pieces/<piece-id>/`; one multi-placement blueprint owns `01_assemblies/<assembly-id>/`. A collection selects existing types and creates neither a new type nor a complete-interchange button.

| Entry point | Responsibility |
| --- | --- |
| `framework/scp/catalog.py` | Validate registries, current allocations, and selectable types. |
| `framework/scp/build.py`, `dbpf.py` | Compose staged DAT archives, exact manifests, and packages. |
| `framework/scp/recipes.py`, `verify.py` | Dispatch generation and independent saved-resource checks. Unknown recipes fail. |
| `framework/scp/rul0.py`, `autotile.py` | Compose controller ordering and validate actual runtime tile lookup. |
| [framework/scp/track_paths.py](../framework/scp/track_paths.py) | Own shared PATH/S3D resource constants, path encoding/parsing, construction flags, and neutral modular shape templates. |
| `framework/scp/install.py` | Verify ownership receipts, source profiles, snapshots, and transactional replacement. |
| `framework/scp/content.py`, `inventory.py` | Generate readable subject sections, current observations, and illustrated catalogues. |
| `framework/scp/connector_metadata.py`, `jsonc.py`; `schemas/` | Parse and validate source-owned connector declarations, verify measured/compiled source agreement, and generate or check resolved connector exports. |
| `framework/scp/connector_overview.py` | Render actual compiled models with complete boundary cards, record provenance, and refresh the existing piece README's connector-overview block. |
| `framework/scp/release.py` | Assess permission, identifier, and build-specific game evidence. |
| `domains/<domain>/implementation/`, `tools/`, `tests/` | Keep transport-specific generation, contracts, authoring tools, and checks with their owning network. |

The installed plugin consists of the combined controller, combined menu, and one DAT per selected type. Recipe resources and construction fragments enter the [controller composition pipeline](#3-controller-composition-and-verification) below.

Reuse the current shared and domain helpers. Do not recreate the removed prototype implementation copies around them; the owning network specification identifies its existing geometry helpers and independent verifiers.

<a id="current-identifiers-and-runtime-addressing"></a>

## 2. Current identifiers and runtime addressing

[Allocations](../config/allocations.jsonc) contain current types only. Preserve each retained piece's logical ID, puzzle/menu roots, resource families, and construction coordinates. Explicitly deleted subjects retain no definitions, compatibility snapshots or tombstones. The local puzzle range is F7A0–F8FF and model families use 7F500000–7F5FFFFF; these are local identifiers, not confirmed public reservations. Preflight against actual installed resources before building.

Use the [piece-authoring procedure](WORKFLOW_PIECE_CREATION.md) to reserve and complete a disabled draft before enabling a new type. The runtime rules below apply independently of the piece's transport domain.

<a id="runtime-tile-lookup"></a>

### 2.1 Runtime tile lookup

Declare occupied cells explicitly for a sparse footprint. Each source cell uses `[column,row]` order, and its resource ID is `allocation_base + column * 0x100 + row * 0x10`; each tile owns model zoom IDs `tile` through `tile+4`. The allocation base is the first actual tile ID minus that cell's column and row offsets. `AutoTileBase` instead adds the minimum modeled column and row offsets to the allocation base, because runtime construction offsets begin at the modeled bounding box. `PlaceQueryID` still identifies the first actual tile exemplar. An empty construction anchor is not a reason to add a fake network tile or move released coordinates. `scp.catalog.auto_tile_base` computes the adjusted base.

The inspected executable creates a one-byte lookup key for each modeled cell, excluding check-only and optional cells. Columns and rows below are normalized to the minimum modeled bounding box. Cells are processed left to right, then down:

```python
key = ((row << 4) + column + 1) & 0xff
offset_by_key[key] = column * 0x100 + row * 0x10
placed_id = (auto_tile_base + offset_by_key[key]) & 0xffffffff
```

`<< 4` multiplies by 16; `& 0xff` retains the lowest eight bits, including wraparound and addition carries. A later cell with the same key overwrites the earlier offset. Both positions then select the later model and PATH. The final address uses addition, not bitwise OR. Cells `(19,4)` and `(3,5)` both receive key `0x54`, so changing the allocation base cannot repair that collision.

A fully modeled area at most 16 × 16 has unique keys, including key `0x00` at `(15,15)`. Wider sparse areas can also have unique keys; verify their actual modeled coordinates rather than inventing an absolute 16-column limit. The cited native 18-column examples contain check-only borders whose modeled areas remain within 16 columns. Check-only borders do not enlarge the modeled area.

Widths above 16 columns require `ceil(width/16)` contiguous `0x1000` resource families in the allocation ledger's `resource_blocks`. Put the preview at `last_family + 0xff5`, keeping every tile's fifth model below it. Row 16 aliases column 1 because `16 * 0x10 == 0x100`. The implemented framework guard permits 64 columns and 16 rows; the scaffold's simple rectangular template permits only 16 occupied cells. Neither guard proves runtime-key uniqueness or game placement.

`framework/scp/autotile.py` checks the modeled origin, unique runtime keys, selected resource IDs, and all five zoom slots during registration and saved-rule verification. Registration rejects unsafe layouts before reserving IDs. A catalogue prototype with an explicitly failed placement test remains inspectable but cannot be selected for a build. Independent construction verification must decode the emitted RUL layout and check its actual keys, source order, adjusted base, and additive offsets; a valid manifest cannot repair incorrect rules. Regression cases include one colliding layout under different bases and valid sparse areas wider than 16 tiles.

Preserve construction-palette symbol case: native section `HighwayIntersectionInfo_0x00001010` uses uppercase `A` for a highway check and lowercase `a` for a road check. Lowercasing `CellLayout` or `CheckType` labels merges distinct symbols and corrupts the palette. Verify model, PATH, shadow, and preview allocation uniqueness across the complete selected plugin.

Every independent piece supports four proper rotations: 0°, 90°, 180°, and 270°. One-way pieces repeat those rotations to fill eight construction states without reflected traffic. A separate diagonal variant requires actual diagonal geometry and interfaces. Construction aliases do not establish additional manual orientations.

<a id="controller-composition-and-verification"></a>

## 3. Controller composition and verification

The [official NAM compatibility FAQ](https://www.sc4nam.com/docs/getting-started/frequently-asked-questions/#is-the-nam-compatible-with-other-transportation-mods) warns that modifications of the same network-rule resources conflict. The shared resources replaced by this framework are:

| Resource | TGI |
| --- | --- |
| RUL0 construction rules | `0A5BCF4B-AA5BCF57-10000000` |
| NetworkINI | `00000000-8A5971C5-8A5993B9` |

Keep each piece's additions as separate source data, and compose all selected pieces against one clean, audited base. Emit one combined controller overlay; asset DATs can remain separate when their TGIs are distinct. Two complete RUL0 replacements do not merge when installed: one can hide the other's rules. Renaming files with additional `z` characters cannot combine their additions.

The composition and saved-resource checks must:

1. Read the clean NAM controller, never an earlier generated overlay, and verify its approved SHA-256 fingerprint rather than only its version label.
2. Inventory the game's installation `Plugins`, the active user profile's `Plugins`, and explicitly known additional loading roots. Report incomplete scan coverage.
3. Reject unknown competing RUL0 or NetworkINI replacements. Recognize an owned prior output only by its recorded hash for an explicit replacement; do not absorb an unrelated overlay.
4. Apply the selected additions deterministically, preserving every native byte outside those additions. Recipe modules return their construction sections without a `RotationRing`; the domain's `build_piece` adds that ring exactly once to its returned rule fragment.
5. Separate the rings from the construction definitions. Insert the selected `RotationRing` lines inside the native controller's existing single `[Ordering]` section, and append only the piece definitions at the resource end. Do not append rings among definitions, add another `[Ordering]` section, or use `AddTypes` to extend native NAM rings.
6. Record the ring insertion as `overlay.rul0.ordering_insertion` and the definition appendix as `overlay.rul0.suffix`. Inspect the actual saved section context, then remove both additions and recover every native RUL0 byte. Matching ring text or eight valid state definitions alone does not establish registered rotation.
7. Validate the complete selected set for resource and construction-ID collisions, menu-slot counts, model/PATH references, texture dependencies, shadow-rule priority, and encoded continuity between tiles. Save staging outputs and an exact manifest; building must neither install files nor edit a saved city.

Rotation controls, placement, and traffic remain separate game observations; follow [TESTING.md](TESTING.md). The manifest and native-byte restoration establish file identity and composition, not those observations.

The documented NAM DLL RUL2 engine and Resource Loading Hooks exemplar patches do not establish additive RUL0 or NetworkINI merging; their documented scopes differ. A future runtime merger requires its own implementation review and tests before changing this architecture. See the [NAM DLL guide](https://www.sc4nam.com/docs/feature-guides/nam-dll/#new-rul2-engine) and the [Resource Loading Hooks author's documentation](https://community.simtropolis.com/files/file/36242-resource-loading-hooks-dll-for-simcity-4/).

<a id="coordinate-frames-and-boundary-edges"></a>

## 4. Coordinate frames and boundary edges

A **coordinate frame** defines which direction each numerical axis represents. SC4PATH stores traffic routes, and S3D stores three-dimensional model geometry. A game tile is 16 m square. Piece source cells use zero-based `[column,row]` indices, increasing east and south respectively; their SC4PATH centres are `(16 * column, -16 * row)`. SC4PATH point coordinates are `(east,north,height)` in metres. S3D model vertices are `(east,height,-north)`, so converting a PATH point `(e,n,h)` to model coordinates gives `(e,h,-n)`. Verify the source frame before transforming imported data, and transform geometry, routes, cell offsets, and previews consistently.

SC4PATH boundary numbers are west `0`, north `1`, east `2`, and south `3`. These identify tile sides, rather than a route's exact heading or permitted travel direction. Construction-cell row offsets increase south; do not confuse them with the north-positive PATH axis. The [connector coordinate contract](CONNECTOR_METADATA.md#3-positions-headings-heights-and-slopes-use-one-comparison-frame) defines the common comparison frame, outward headings, section offsets, and grade signs after source conversion. Transport-class meanings and native heights belong to the owning domain specification.

<a id="model-and-render-preservation"></a>

## 5. Model and render preservation

A **vertex** is a stored model point with position and texture coordinates, and a **triangle** is one three-cornered surface face. A **render group** is one stored collection of those vertices and triangles. Authored geometry is packed into groups of at most **512 stored vertices and 512 triangles**, including every frame of all five model zooms and the assembled cursor preview. These are conservative project authoring budgets, not established game-engine limits. Native donor groups retain their separately audited contracts.

Here, “mesh size” means the stored vertex and triangle counts **per render group**. It does not mean metres, owned tiles, the construction rectangle, the DAT's byte size, or the total triangle count across a whole piece. One S3D model can contain several compliant groups. Splitting those groups changes how the model is stored; an assembly instead arranges several independently selectable gameplay pieces with their own functions, construction rules, and measured interfaces. Apply the [piece-versus-assembly decision](WORKFLOW_PIECE_CREATION.md#1-decide-between-a-piece-and-an-assembly) separately.

A **float32** is a 32-bit floating-point number. Vertex reuse compares identical encoded float32 XYZUV bytes: XYZ supplies position, and UV supplies texture coordinates. Preserve every triangle, its corner order, and its texture coordinates. Signed zeros and texture seams remain distinct. Imported compiled geometry uses `preserve_encoded_triangles=True`, retaining even existing encoded degenerate faces. Repacking is not permission to simplify or retessellate a retained piece. Changes to visible geometry, visible triangle order, XYZ/UV, materials, or render state need the applicable explicit geometry-change scope; a serialization-only change needs an exact-equivalence guard and an encoding disclosure.

`framework/scp/render_meshes.py` provides `assert_render_budget`, which checks every frame of meshes named `SCP ...`, and `repack_s3d`, an available utility that can split static compiled authored groups while proving that the ordered encoded triangle/material stream is unchanged. Do not assume every build automatically invokes that repair utility. Repacking retains unchanged native buffers and rejects unsupported animated changes. Domain packers consume this shared preservation contract; the [rail rendering evidence](../domains/high-speed-rail/NETWORK_SPEC.md#7-measured-rail-rendering-evidence) retains the scoped diagnosis and authorized representation-repair history.

The package verifier checks every zoom and the complete placement preview. The preview loader applies the same render budget and checks runtime tile addressing before drawing. Geometry tests inspect all groups; reading only the first mesh silently omits surfaces. Software rasterizers can draw oversized groups that the game fails to display, so a successful model render does not establish game rendering. Regression coverage lives in [test_render_mesh_packing.py](../tests/test_render_mesh_packing.py), [test_render_meshes.py](../tests/test_render_meshes.py), and [test_render_budget_verification.py](../tests/test_render_budget_verification.py).

<a id="geometry-and-routing-verification"></a>

## 6. Geometry and routing verification

Independent checks inspect saved resources and their placed relationships, rather than repeat generator declarations. Apply the owning domain's numeric profiles, clearances, texture rules, and movement contracts; rail-specific dimensions do not become universal framework defaults.

- Compare external travel tangents with independently reviewed cardinal or diagonal vectors. Where an audited interface uses an analytic collar, its first and last encoded chords must meet that interface as specified. Derive external construction categories from the reviewed vectors, and preserve cell palettes when other routes share the edge.
- Check shared three-dimensional endpoints, including height, under the complete [boundary contract](CONNECTOR_METADATA.md). Reject unintended dangling routes, missing or reversed movements, cross-level teleports, zero-length segments, and unintended U-turns. A same-height intersection on a cell boundary can create an unwanted connection in the encoded graph; inspect every seam, and repair the route geometry instead of hiding the graph error with a flag. The encoded-graph result does not establish the game's inter-tile matching tolerance.
- Check routes against the placed union of all relevant cell models. Model overhangs can cross cell boundaries, so demanding support from each cell's local model alone creates false failures. Still verify exact cursor-preview offsets, owned tiles, and the land reserved for supports.
- Inspect the domain's swept traffic envelope between PATH samples, including walls and actual branch openings. A visible surface beneath a route does not prove that a wall no longer blocks it. Check both route-to-surface agreement and clearances between surfaces and supports. Record a chosen minimum as an authoring criterion, not a measured game collision threshold.
- A flyover needs both an actual raised three-dimensional traffic route and matching visible geometry. Raised decoration with flat PATH data, or raised PATH data without the corresponding visible route, fails this consistency check.
- Structure-only cells need an audited purpose and an explicit `structural_cells` declaration. An intentionally empty PATH uses exactly `SC4PATHS / 1.2 / 0 / 0 / 0`; do not weaken the route parser to accept arbitrary missing traffic. Verify the saved models, reserved footprint, and zero construction edge flags. Native examples and any domain exceptions remain in the network specification.
- A local route entering and leaving the same tile edge requires its own explicit contract. Distinguish an intended curve grazing a cell from an unwanted external same-arm U-turn. A valid file-format example alone does not establish game operation for another network.

Independent test expectations remain separate from layout/model generation. Include failure controls that mutate actual resources, and connect relevant modules across disjoint owned cells when checking a complete movement. Report static resource, graph, physical-clearance, and observed game results separately under [TESTING.md](TESTING.md).

<a id="cache-correctness-and-performance"></a>

## 7. Cache correctness and performance

A model-audit cache can reuse a result only for the exact immutable specification and every model, PATH, exemplar, and preview byte read by that audit. Keep the cache bounded in memory, invalidate it on any changed input, and return a fresh report. The existing verifier removes `texture_ids` from its returned report; sharing a mutable cached dictionary corrupts later verification.

Seek selected resources through the DAT index instead of reading unrelated archives, and load a referenced texture atlas once per rendering run. Preserve the bounded renderer's pixel equality with the reference implementation. Its fingerprint follows the rendering code and settings actually used, while cache reuse also checks every saved PNG hash. Historical build names alone do not identify reusable render results.

The catalogue's private `local/cache/preview-index.json` is a rebuildable acceleration and coverage index, excluded from exports. Canonical piece images live in each piece's `previews/`; portable per-piece `evidence/preview.json` and `evidence/preview-top.json` retain each view's actual model, texture, renderer, grid, header, and image fingerprints. Top-only output must preserve existing angled files, and coverage must distinguish requested types and views from the rest of the registry. `render_headers.py` supplies the shared three-row piece header; the tile scale appears there once. The [documentation-generation workflow](WORKFLOW_DOCUMENTATION_GENERATION.md#9-maintain-the-complete-preview-catalogue) owns commands, selection, coverage review, and the point at which image writes are frozen before tests or packaging copy the source.

<a id="inspect-additional-donor-resources"></a>

## 8. Inspect additional donor resources

A **TGI** is the three-part identifier of one game resource: its type, group, and instance, written as eight hexadecimal digits each. A pinned test fixture contains only its recorded input archives; absence from that fixture does not establish absence from the installed game. Use the optional `scp.resource_audit` tool from the parent project directory to find an exact TGI in an existing Plugins directory. Replace the path and resource identifier with the actual source being investigated:

```sh
python3 -m scp.resource_audit --plugins '/absolute/path/to/Plugins' --tgi 296678f7-69668828-00004b00
```

The report lists every matching archive and index occurrence, its archive fingerprint, and its stored and decompressed resource fingerprints. It reads resource indices and selected payloads without loading entire archives into memory. It does not select the game's winning override, infer load order, or claim that two different variants are interchangeable. Compare the actual approach routes, offsets, heights, and materials before choosing a donor.

When an otherwise useful source archive also contains unrelated conflicting overrides, explicitly capture only the independently selected resource into a new private directory:

```sh
python3 -m scp.resource_audit --plugins '/absolute/path/to/Plugins' --archive '/absolute/path/to/selected-source.dat' --tgi 296678f7-69668828-00004b00 --capture custom-pieces/local/resource-captures/ordinary-road-path --root custom-pieces
```

This creates a single-resource DAT and `resource-audit.json` beneath `custom-pieces/local/`, retaining the original stored bytes and both source and output fingerprints. The archive argument selects an exact file; ambiguous duplicate index entries are rejected rather than resolved silently. Existing output directories, invalid compression, and writes inside the supplied Plugins tree are rejected. No original archive changes. Inspect the report, add the deliberate narrow dependency and its audit to the owning profile, and rerun actual-resource verification. Capture does not grant redistribution permission or repair a mismatching approach profile. Keep network-specific donor measurements in the owning `NETWORK_SPEC.md` or piece evidence.

<a id="native-menu-resources"></a>

## 9. Native menu resources

The button exemplar is derived from the installed NAM 50 **Ground High Speed Rail** button:

| Resource | Type | Group | Original instance |
| --- | --- | --- | --- |
| Native menu exemplar | `6534284a` | `2a3858e4` | `6a47c200` |
| Native icon PNG | `856ddbac` | `6a386d26` | `6a47c200` |
| Button title, localized text | `2026960b` | `123007bb` | `6a47c200` |
| Button description, localized text | `2026960b` | `123006aa` | `6a47c200` |

A resource identifier consists of its **type**, **group**, and **instance**. Together, those three numbers are called a **TGI**. An instance number alone does not uniquely identify a resource.

The exemplar's type property stays **40**, the native network-menu type. The builder retains its parent reference, property order, costs, reserved fields, and property encodings. It changes only:

| Property | Identifier | Custom value |
| --- | --- | --- |
| Internal exemplar name | `00000020` | The SCP button title |
| Item Icon | `8a2602b8` | That piece's menu instance number |
| Item Order | `8a2602b9` | The piece's registered Rail-menu order |
| Item Button ID | `8a2602bb` | That piece's menu instance number |
| User Visible Name Key | `8a416a99` | The custom title TGI |
| Item Description Key | `ca416ab5` | The custom description TGI |

Each button's last four hexadecimal digits match its construction sequence root. The accepted straight and diagonal smooth T junctions use `6a47f864` and `6a47f865`. The two scissors switches use `6a47f862` and `6a47f863`. Other current piece IDs are recorded in their manifests and `config/allocations.jsonc`. Artwork and text use those same instance numbers with their respective resource types and groups. Do not assume the current collection occupies a contiguous ID range.

These identifiers were checked against the locally installed Plugins files. They are private project identifiers; public allocation has not been confirmed. The build must repeat collision checks before producing a package.

<a id="icon-encoding-and-maintenance"></a>

### 9.1 Icon encoding and maintenance

The player-facing colour, network, and type legend is in [Recognize SCP menu icons](BUILD_AND_INSTALL.md#2-recognize-scp-menu-icons). Labels remain readable without colour. Domain artwork implementations and their registration commands are listed in the [rail implementation map](../domains/high-speed-rail/NETWORK_SPEC.md#1-implementation-entry-points).

Every icon is a noninterlaced PNG with 8-bit red, green, blue, and alpha channels. Alpha controls transparency. The complete image is **176 pixels wide and 44 pixels high**. It contains four adjacent **44 × 44** frames, in this order:

1. Locked: grey artwork.
2. Normal: full-color artwork.
3. Selected: full-color artwork with a pale outline.
4. Highlighted: full-color artwork with a white outline.

The format was checked against the installed NAM PNG. The state order is also documented by the author of [Creating Custom Lot Icons](https://community.simtropolis.com/omnibus/simcity-4/bat-lot-editor-tutorials/creating-custom-lot-icons-r62/).

Each current piece manifest identifies its own native-size icon strip under `domains/<domain>/00_pieces/<piece-id>/icon.png`. Each registered assembly owns its strip under `domains/<domain>/01_assemblies/<assembly-id>/icon.png`, beside `assembly.json`. Keep both kinds of icon at the owning subject's root and documentation images in its `previews/`. The ordinary build includes the selected pieces' strips, and assembly-menu preparation reads and validates the selected assembly's canonical strip. Inspect those files to review their four menu states; use the [artwork-only regeneration command](WORKFLOW_DOCUMENTATION_GENERATION.md#10-menu-artwork-and-source-registration) to refresh registered assembly icons without constructing a build.

<a id="builder-interface-and-verification"></a>

### 9.2 Builder interface and verification

```python
resources, metadata = build_menu_resources(donor_exemplar, piece_spec)
validate_menu_resources(package_resources, donor_exemplar, piece_spec)
```

The first function returns four resources as a dictionary whose keys are TGIs. It does not write files. The second function can inspect those four resources inside a larger package dictionary.

A domain's icon-identity function supplies the same category, network, and type vocabulary to artwork and menu text. Complete-junction classification uses an explicit allowlist, rather than a recipe prefix, assembly guide, or selected component set. Preserve the two accepted smooth-T PNP entries. New complete one-click mechanisms follow the explicitly requested mechanism and proof policy in [WORKFLOW: Assembly Creation](WORKFLOW_ASSEMBLY_CREATION.md). Label changes affect icon and localized-text bytes; they do not change identifiers, menu order, geometry, or native menu costs.

Validation reads the actual exemplar and text resources, checks every retained native property, and verifies the new title, description, icon, order, and root button references. Icon validation checks PNG checksums, dimensions, channel format, all four distinct states, greyscale locking, color, and transparent corners. It also checks that the actual artwork matches the registered style.

These are static file checks. The separate SCP buttons and their selection behavior still require an in-game check.

<a id="assembly-component-menu"></a>

### 9.3 Assembly component menu

The normal compilation stage gives each reusable type its own button and independent construction family. Every final assembly delivery uses the [assembly-menu step](BUILD_AND_INSTALL.md#8-prepare-the-assembly-menu): one button selects that assembly's components through Tab and Shift+Tab. The owning domain's `menu-layout.jsonc` declares the assembly, first-use component order, and cycle-button presentation ID. The final menu removes member-specific presentations and keeps unrelated piece buttons unchanged. Existing piece and construction identifiers remain authoritative.

In RUL0 Ordering, **RotationRing** supplies Home/End rotation states, and subsequent **AddTypes** rows supply Tab/Shift+Tab component changes within that family. The transformation changes only selected ordering rows, retains every state and construction definition, and records the original controller as verification proof. Each click places one selected component. See the [NAM controls reference](https://www.sc4nam.com/docs/getting-started/frequently-asked-questions/#how-do-i-move-between-the-different-puzzleflexstarter-pieces-and-how-do-i-rotate-them).

The assembly entry has its own presentation exemplar, icon, and text resources; its `Item Button ID` targets the first component's existing construction root. Preparation reads the assembly-owned `icon.png` and verifies its exact expected procedural artwork before packaging it. Frozen candidate verification retains its own saved inputs, so a later source icon refresh does not rewrite earlier candidates. Current assembly menus emit no submenu entry or Submenus DLL properties. Verification support for archived source formats remains separate from the one-button output policy. Actual button visibility and keyboard behaviour require a recorded game observation.

`scp.menu_experiment` implements the public `assembly-menu` command, frozen source proof, and strict candidate verification. `scp.menu_experiment_resources` owns menu resource transformation; `scp.rul0.with_feature_sequence` owns the reversible ordering transformation. Verification reconstructs the original normal build, preserves all piece DATs and NetworkINI, compares the exact allowed transformation, independently inspects properties and ordering, and rejects missing proof or changed file closure. The coordinated installer, omission guard, ownership receipt, backup, and rollback remain in force. Build and static verification do not install the candidate or create a game observation.

Repeated verification in one process may reuse the canonical baseline report only after rechecking the candidate's complete file closure, every declared file hash, the exact source proof and manifest, actual menu/controller facts, and regular external donor files and their recorded fingerprints. The bounded cache identifies the validator and all frozen inputs, and the report explicitly discloses reuse. It does not cache a final candidate pass or survive a new CLI process.

<a id="mixed-network-ownership"></a>

## 10. Mixed-network ownership

For a straightforward crossing, **the upper participating transport network owns the piece**. Ownership determines its primary catalogue group, folder family and main icon network label. The lower network remains explicit in the full name, tooltip and searchable metadata.

Use the actual track or carriageway at the crossing to determine which is upper. Do not use the tallest pylon, decorative object, model bounding box, the underlying game transport number, or the network selected by a filename substring.

| Geometry | Owning family/domain | Main network label | Suggested readable name |
| --- | --- | --- | --- |
| HSR above tram | High-speed rail | HSR | HSR L2 over Tram L0 — Crossing |
| Tram above HSR | Light rail/tram | TRAM | Tram L4 over HSR L2 — Crossing |
| HSR above GHSR | High-speed rail | HSR | HSR L2 over GHSR L0 — Crossing |
| Highway above HSR | Highway | Highway variant | Highway L4 over HSR L2 — Crossing |
| Ground HSR curve | High-speed rail | GHSR | GHSR L0 — Curve |
| HSR changing to GHSR | High-speed rail | HSR family | GHSR L0 ↔ HSR L2 — Transition |
| Complete HSR T | High-speed rail | HSR | HSR — Full T — PNP |

The tram-above-HSR and highway-above-HSR examples illustrate classification; they do not claim that those exact proposed pieces have been implemented.

<a id="keep-these-properties-separate"></a>

### 10.1 Keep these properties separate

1. **Domain:** the owning network family and its source folder. Keep HSR and GHSR together in `high-speed-rail`; distinguish their individual variants.
2. **Networks involved:** all participating networks, including the lower network. A piece can be found when filtering either participating network without duplicating its source or installed resources.
3. **Feature:** crossing, straight, curve, ramp, split, merge, switch, or adapter.
4. **Levels:** nominal game levels plus the actual path heights in metres. For example, HSR L2 has a 15.5 m path. Upper authored HSR remains HSR.
5. **Placement:** an individual PART, an implemented one-click PNP junction, or an assembly blueprint requiring several placements.

The PART/PNP colours retain their current meaning. They indicate placement type, not the owning transport family or the extent of game testing. A mixed crossing is still PART unless it is itself a complete junction.

`MIX` can be a searchable characteristic, but should not replace a known owning domain. In particular, HSR over tram should display `PART HSR`, with `XNG` as its type code; its tooltip names the tram below. Pure ground HSR can display the GHSR variant. Any short icon spelling must be defined in the icon legend; the full tooltip uses the full network names.

<a id="cases-where-height-alone-cannot-choose-an-owner"></a>

### 10.2 Cases where height alone cannot choose an owner

- **Same-height crossings or junctions:** explicitly choose the primary network or mainline and cross-index the other networks. Do not invent an upper network.
- **Complex pieces where networks exchange vertical order:** explicitly record one owning family for the complete design, while listing every participating network. A single tallest point is insufficient.
- **Transitions:** classify by the network family being connected. HSR to GHSR belongs to high-speed rail; a connector between unrelated families needs an explicitly documented owner.
- **Ground or underground pieces:** classify using the actual participating routes and the preceding rules. A decorative structure does not supply a transport network or change the owner.

The explicit owner is mandatory whenever the simple upper-network rule has no unambiguous answer. This is a metadata requirement, not a reason to ask the user repeatedly about routine implementation details.

<a id="nam-comparison-and-provenance"></a>

### 10.3 NAM comparison and provenance

NAM groups puzzle pieces into a feature button and its Tab sequence. Its current organization does not establish a universal rule that the physically upper network owns every crossing.

The local audit checked the installed, fingerprint-pinned NAM 50 archives, the actual menu exemplars and controller sequences, and the encoded paths:

| Crossing in NAM 50 | Actual path heights | Button containing the crossing |
| --- | --- | --- |
| HSR over GHSR | HSR 15.5 m; GHSR 1 m | Ground High Speed Rail |
| Monorail over Ground Light Rail/tram | Monorail 15.5 m; GLR 0 m | GroundLightRail |
| Elevated highway over GHSR | Elevated highway above ground HSR | Ground High Speed Rail |
| Elevated highway over GLR | Elevated highway above ground GLR | GroundLightRail |

**GLR** means Ground Light Rail, the game's ground tram system. The second example is a native Monorail crossing, not proof of a separately named native HSR/tram piece. It still demonstrates that NAM's button owner can be the lower network. Which game submenu contains a button is a separate property.

Provenance of this NAM 50 comparison: readable source matching the audited controller was inspected under the optional workspace donor tree `setup/nam-tram-ddrhw-source/Controller/RUL0/`. That tree is not a runtime dependency or part of the portable mod source. The recorded source locations were:

- `C000_Monorail/C200_GHSR.txt`: lines 4–14 put crossing C20A in the GHSR sequence; the C20A definition starts at line 874.
- `B000_Lightrail/B110_GLR.txt`: lines 5 and 36–38 put crossing B12F in the GLR sequence; its definition starts at line 746.

The installed controller SHA-256 is `d903540cdf772b4ed6a072c504e006e1cac384f8027ce58a288a5a9654f94161`. The checked crossing PATH resources are `296678f7-a966883f-5dcf0a00` (HSR/GHSR) and `296678f7-a966883f-580e0700` (Monorail/GLR).

Official NAM documentation supports treating HSR and GHSR as variants of one Monorail-based family, with their own feature buttons. See the [High Speed Rail guide](https://www.sc4nam.com/docs/feature-guides/high-speed-rail/). The [Light Rail/Tram guide](https://www.sc4nam.com/docs/feature-guides/light-rail-tram/) describes that separate family and its ground, elevated, and dual-network forms. Menu organization can also follow a construction system: the [FLUPs guide](https://www.sc4nam.com/docs/feature-guides/flexible-underpasses/) places its underground-road and assorted overcrossing tools under Highways.

These are facts about NAM. The following simpler ownership rule is a proposed SCP convention, not a claim that NAM already follows it everywhere.

<a id="classification-metadata-status"></a>

### 10.4 Classification metadata status

The upper-network ownership rule is an SCP authoring convention. Existing menu labels are still supplied by `scp_hsr.icons.icon_identity(menu.style)`, and the optional classification schema has not been implemented. In particular, the existing HSR-over-ground-tram style uses TRAM, and mixed HSR/GHSR styles use MIX. Consolidating documentation does not change those resources.

A future validated `classification` object could store `owner_network`, `feature`, `placement`, `ownership_basis` and a `routes` list; each route would identify its family, network, nominal level, and actual path height. Registry validation, generators, artwork, inventories and menu construction must agree before adopting that schema. Verify ownership against real model/PATH definitions, not a renamed string heuristic. Keep one source owner and cross-index other participating networks.

<a id="documentation-generation-and-observations"></a>

## 11. Documentation generation and observations

The [source map](../STRUCTURE.md) identifies each definition, placement, extracted interface, observation record, and generated view. [TESTING.md](TESTING.md) defines observation identity, confirmation, and staleness. The contracts below describe generator behavior against those sources.

Connector source semantics, schemas, and authoring-versus-derived fields are defined in [CONNECTOR_METADATA.md](CONNECTOR_METADATA.md). The [documentation-generation workflow](WORKFLOW_DOCUMENTATION_GENERATION.md) owns extraction prerequisites, refresh/check commands, coverage, output locations, artwork, README views, and evidence. The framework integration contract is that `connector_metadata.py` validates and resolves source declarations, `connector_overview.py` renders verified compiled resources, and consumers use the shared export API rather than copying parsers or extractors.

Keep authored prose outside named HTML comment blocks. `scp.content` replaces only its generated overview, summary, connection, and manual-check blocks. New or deliberately migrated pieces use `<!-- PIECE README LAYOUT: 2 -->` for the three-chapter overview and `<!-- PIECE TESTING LAYOUT: 1 -->` for the six-chapter TESTING document; README matrix results link to exact cases in TESTING. Legacy combined guides remain in their existing layout until explicitly migrated. Preserve the canonical README/TESTING pair while removing only superseded connection, checklist, or recording-helper pages; refreshes must not recreate duplicates. The two illustrated inventories stay in `00_pieces/` and `01_assemblies/`; collection navigation/counts are generated inside the domain README. Domain `inventory.jsonc` remains a machine-readable index.

A prose-only `scp.content` refresh preserves observation, connection, and class JSON byte for byte; changed DAT resources require upstream extraction and scoped case regeneration. Recording a confirmed observation also refreshes its subject and inventories. Generated matrices retain each current case's service, pose, rotation, environment, identity, and failed or stale results. Current generation does not expand legacy endpoint/counterpart shortlists into manual cases. Their explicit retirement operation preserves observed and explicitly not-applicable history without promoting it to complete-edge evidence. [Documentation generation](WORKFLOW_DOCUMENTATION_GENERATION.md#124-refresh-generated-markdown-and-inventories) owns refresh commands, and [TESTING.md](TESTING.md) owns observation recording and legacy-case retirement.

An extractor's explicit exact-piece scope uses `refresh_catalog_content(..., scope_to_changed=True)` with validated changed IDs and freshly extracted records. That path reads and refreshes only those subjects' cached evidence; catalog definitions still supply identity validation and affected-assembly IDs. It does not rewrite assemblies, the global connection-class index, or inventories, and its result explicitly reports deferred work. The default build-wide path retains its existing affected-assembly and global-view behavior. Validate the entire exact selection before any write, consume single-use input iterables once, and test that malformed or inaccessible unselected evidence cannot interfere with a selected refresh. The [documentation workflow](WORKFLOW_DOCUMENTATION_GENERATION.md#1-choose-the-refresh-scope) owns operator selection and follow-up commands.

The explicit `observations refresh-images` operation binds final existing angled, top, and connector-overview images without regenerating any non-image case or measured connection. Preserve exact prior image observations and dependencies so changed PNGs become stale rather than approved.

For an ordinary verified piece build, final-documentation packaging uses `package --refresh-docs`: verify the original build without writing reports, construct current portable ZIP documentation and document hashes, and preserve every original build file. An assembly-menu candidate requires its frozen source proof and rejects that option. Finalize its documentation before a fresh normal source build and a fresh assembly-menu candidate, then package without `--refresh-docs`; preserve superseded candidates unchanged as historical evidence. Follow the [final-artifact sequence](WORKFLOW_DOCUMENTATION_GENERATION.md#13-final-artifacts-and-packaging) for the applicable branch.

Connector exports bind `compiled_manifest_sha256`, excluding only documentation and release/installation/game-summary state; exact payload hashes and every other compiled fact remain bound.

The check runner reads the selected checkout's `pyproject.toml` package-directory mapping through `check_bootstrap.py`. This includes differently named tool directories such as `scp_hsr_tools`; a global editable installation must not silently supply another checkout's package. Validate package origins in isolation tests, and reject mappings escaping the selected source root.

Piece extraction and validation establish intrinsic source facts without scanning potential neighbours. For an existing saved assembly, route composition uses its actual placed endpoints and directed piece journeys; it does not use a neighbour shortlist or establish complete-boundary compatibility for unmigrated types. Automatic compatibility discovery is not supplied by the current library; a separate consumer must accept only source-valid, fresh connector exports and compare complete boundaries. Preserve missing, stale, invalid, and unmigrated coverage states instead of converting them into compatibility failures or filling missing facts from old per-port lists.

Validate meaningful documentation behavior: authored sections survive repeated refreshes, deleted pages stay absent, exact case identities and results survive, statuses are separated by orientation, and links resolve to actual files and headings. Export maintained source and current documentation with their relative paths intact. Exclude local inputs, caches, backups, and previous build outputs from source archives.

Include connector JSONC declarations, strict-JSON generated data and optional profiles, source schemas, current overview artwork, provenance, shared generation code, and their library-owned guides in portable exports. A library declaration must not depend on an external application guide to explain or validate its source format. Keep generated overview blocks outside other generators' markers and preserve them during a prose-only refresh.

<a id="installation-and-saved-resource-constraints"></a>

## 12. Installation and saved-resource constraints

The installer accepts sc4pac top-level DLL file links only when they target a regular Windows DLL with an MZ header inside explicitly scanned Plugins roots and outside the managed SCP folder. Directory links, DBPF/archive aliases, broken links, and external targets remain forbidden. Preserve existing valid DLL links and their targets. [Installation tests](../tests/test_install.py) cover this distinction.

<a id="structural-shadow-quantization"></a>

### 12.1 Structural shadow quantization

FSH resources store texture and shadow images. Shadow checks compare saved FSH artwork with actual S3D geometry at all five zooms. The rasterizer and generated FSH bytes remain unchanged. Pixel quantization means a tiny real structural sliver can fall between samples on an 8, 16, 32, or 64 px grid while covering one faint pixel on the 128 px grid. This is a narrowly checked exception, not permission to omit shadows.

Acceptance requires every condition to be established from saved resources:

1. The cell is explicitly declared structural, and its actual PATH is exactly `SC4PATHS / 1.2 / 0 / 0 / 0`.
2. All five S3D zoom resources are byte-identical.
3. Each FSH is byte-identical to the silhouette derived from its corresponding model.
4. The highest-resolution shadow is nonempty, and empty zooms form only a leading coarse prefix.

Traffic cells, missing or stale FSH resources, differing zoom geometry, all-empty shadows, and holes after a visible zoom still fail. Do not invent shadow pixels, enlarge geometry, or skip any of the five model/PATH/shadow checks to bypass the guard. Reports identify each accepted subpixel structural zoom; game shadow projection remains a separate, unverified observation.

<a id="saved-resource-verification"></a>

### 12.2 Saved-resource verification

Staged verification checks package closure, exact resource ownership, texture/shadow references, controller restoration, native menu properties, and independent domain contracts. Portable saved-DAT verification works without an input audit or installed donor archives. Run tests appropriate to changed behavior; report omitted or skipped broader suites separately from completed checks. Source/model evidence does not establish game placement, traffic, or shadow selection. Installation and publication are separate authorized actions; use the operator and release guides for their exact procedures.
