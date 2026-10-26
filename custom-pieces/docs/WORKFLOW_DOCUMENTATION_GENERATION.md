---
title: "WORKFLOW: Documentation Generation"
summary: "Generate and review reusable-piece and assembly artwork, readable guides, connector exports, and evidence from current authoritative sources, with explicit commands and tool limits."
audience: "Piece authors, assembly designers, and maintainers"
document_type: "procedure"
---

# WORKFLOW: Documentation Generation

Use this workflow after creating or changing a reusable piece through [WORKFLOW: Piece Creation](WORKFLOW_PIECE_CREATION.md), or checking a multi-piece layout through [WORKFLOW: Assembly Creation](WORKFLOW_ASSEMBLY_CREATION.md). It owns shared picture, grid, caption, connection-card, README, and documentation-refresh requirements for every transport domain. The owning domain's network specification supplies its actual interfaces and classification; the [HSR network specification](../domains/high-speed-rail/NETWORK_SPEC.md) is the existing example. [FRAMEWORK_ENGINEERING.md](FRAMEWORK_ENGINEERING.md) owns renderer and generator implementation contracts, and [CONNECTOR_METADATA.md](CONNECTOR_METADATA.md) owns connector semantics, schemas, and matching rules.

A **piece type** is one individually selectable menu button. A **placement** is one copy of that type in an assembly. A **compiled model** is the actual saved game model, rather than a sketch reconstructed from its metadata. A **provenance record** identifies the source files, settings, and output bytes behind an image or table. A software preview, a checked build, an installed file, and an observed game result establish different facts; label each output by the evidence it actually supplies.

## Choose the refresh scope

Start by identifying what changed. This determines which existing inputs can be reused and prevents an old measurement or picture from being relabelled as new evidence.

| Change | Required sequence |
| --- | --- |
| Maintained prose or the layout of a generated Markdown section | Edit maintained prose or its owning generator, then use [README refresh](#readme-layouts-and-generated-sections). Reuse existing valid measurements, images, and observations. |
| Connector declaration or connection-card presentation, with unchanged game resources | Validate the declaration, reuse its matching verified compiled build and current measurements, then run [connector refresh and check](#refresh-and-check-the-two-migrated-pieces). Rebuild neither geometry nor upstream measurements solely to relabel unchanged cards. |
| Picture caption, grid, camera, or annotation changes | Use the appropriate existing renderer with the same approved compiled geometry, record the changed presentation and output hashes, inspect the actual new images, and update their links. A source-code or settings change can make earlier artwork provenance stale. |
| Actual routes, geometry, or construction changes | Finish piece/assembly implementation, build and independently verify the saved resources, run the owning domain's actual-resource extraction, then regenerate affected exports, pictures, README views, and inventories. Preserve observations and let changed dependencies become stale. |
| A new or geometrically revised type needs a north-up preview | Follow the [standalone-picture requirement](#reusable-names-and-standalone-type-pictures), and use the [generic canonical view command](#current-renderer-support-and-canonical-top-views) with `--views angled top`, or `--views top` to preserve an existing angled view. |

A documentation reorganization alone does not authorize changing models, PATH traffic routes, construction cells, identifiers, saved placements, or human observations. Preserve original backups, imported documentation, and frozen evidence; update maintained source and current generated views.

## Prepare the inputs and open the project

1. Identify the owning piece README and `piece.json`, or the assembly README, `TESTING.md`, and machine-readable placement plan. Read the domain's network specification for actual transport facts. A layout plan must retain exact piece IDs, instance IDs, poses, owned cells, and the current compiled source fingerprints.
2. Confirm the intended build has passed its relevant independent saved-resource checks. A **DAT** is the game's resource archive, **S3D** contains model triangles, **FSH** contains texture images, and **PATH** describes traffic routes. A missing built piece remains pending; an older or similar-looking model is not its replacement.
3. Finish concurrent geometry work and the integrated checks before starting the final render pass. Render the accepted current result, rather than several competing intermediate copies.
4. Open a terminal. On macOS, press **Command + Space**, type **Terminal**, and press **Return**. A **checkout** is your local copy of the repository, and its **root** is the folder containing `custom-pieces/` and the repository README. Replace `/path/to/sc4-simons-custom-pieces` below with your checkout's full path, keep the quotation marks so spaces work, and press **Return** to select that root directory.

```sh
cd '/path/to/sc4-simons-custom-pieces'
```

Type `python3 --version` and press **Return**; Python must be version 3.11 or newer. Use the existing project dependencies. For a new checkout, follow [editable installation in BUILD_AND_INSTALL](BUILD_AND_INSTALL.md#build-a-selected-collection), including Pillow and NumPy. The commands below state when they need the repository root or the `custom-pieces` directory; paths are relative to that stated directory.

## Coordinate contract for charts and renders

**Use X/Y tile-centre coordinates in every picture and rebuilding table.** The following fixed-reference rules apply to assembly charts, assembly renders, and placement tables. Standalone reusable type pictures use local zero and canonical orientation under the [standalone-picture rules](#reusable-names-and-standalone-type-pictures). X increases eastward (right on a north-up plan); Y increases northward (up). The fixed zero `(X0, Y0)` is the centre of the southwest tile of the layout's construction rectangle. Reuse that same physical reference in every assembly camera view. All displayed tile indices must be nonnegative.

1. Set that southwest reference early in the design. For the current 20 × 23 tile trumpet, the ranges are **X0–X19** and **Y0–Y22**; its central crossing is **(X7, Y13)**. Keep the physical reference fixed during compaction and camera changes. If the layout extends west or south and the reference must move, record the conversion and refresh every view and human placement table together.
2. Prefix each displayed axis tick with its axis letter, such as **X10** or **Y10**. Write positions as **(X3, Y2)**; do not use E/N prefixes or plus signs. One tile is **16 × 16 metres**, so this example is 48 m east and 32 m north of zero. Number the first tile 0, the next 1, and so on.
3. Draw actual tile boundaries. Tile centres are 16 m apart; each tile's boundaries lie 8 m either side of its centre. Describe the southwest outside edges as the west/south sides of tile 0 rather than introducing negative edge labels. Grid lines through centres are not tile edges.
4. Give every assembly view the same world grid, nonnegative X/Y labels, north arrow, tile scale, and view-direction caption. **Do not draw a global origin marker, origin arrow, origin caption, or origin legend.** Zero is already identified by the axis labels. In an oblique view, project the world grid with the same camera as the tracks; do not replace it with an unrelated screen-space lattice or restart numbering at a screen corner. Keep every labelled tick within the nonnegative display range, including clean overviews and placement-plan side keys.
5. Keep grid lines light enough to read the tracks. Make coordinate labels readable at the delivered resolution, using margins and close-ups when needed. Heavier reference lines every five tiles may improve readability; retain one-tile spacing and enough labels to identify a specific tile.
6. Reuse module labels `P01`, `P02`, etc., exact descriptive menu names, connection labels, movement colours, and direction arrows consistently in the named rebuilding/review views. Apply the [in-picture naming and leader-line rules](#assembly-picture-set-and-in-picture-identification) there. Omit module annotations in clean companions while preserving the coordinates and physical layout. State actual path heights in metres; a ground tile identifies horizontal location, not the track level.
7. Keep authoritative metre coordinates in the placement plan unchanged. Store display coordinates separately with the exact reference conversion; a presentation change must not move geometry or alter game IDs. Human guides, in-picture labels, and rebuilding tables use X/Y display indices. Technical authoring coordinates and native game-axis conventions stay in their own appendix or domain contract, explicitly identified as such. Construction rows increase southward; they are not displayed Y indices. A native model's vertical Y axis is also a separate convention.
8. Separate world positions, module construction reference positions, and mouse-click positions. A module's software reference tile can be empty in a sparse piece. Keep these per-piece positions in the plan and table; label them **Position X7, Y13**, rather than **Origin**, inside pictures. Placement-plan diamonds mark these per-piece reference positions, not the global zero. Do not promise a cursor anchor until checked in the game.

A useful review comment is: “Move the P03 merge from `(X13, Y13)` to `(X11, Y13)`, keeping its 15.5 m height; adjust and recheck the neighbouring connections.” Moving a rigid module also moves its ports. “Shorten the part on the right” becomes ambiguous when the camera changes.

## Reusable names and standalone type pictures

A **piece type** is one menu button. A **placement** is a copy used in one assembly. Name reusable types by network, height, movement, and physical profile. Do not put an interchange P-label or a west/east/north/south role in the menu name. Relative left/right handedness is acceptable when it identifies a real functional difference. A generic name does not make a custom curved socket compatible with ordinary track: state its exact connection limits.

Write nominal levels in full in source names, for example `HSR Level 2 above Road Level 0`; this is the safest form for shared picture titles. The shared title helper normalizes `L2`-style shorthand for display, while evidence retains the exact registered name. Keep each nominal level and its measured height together once, and inspect the actual title in every final image. A normalized display title does not rename the registered piece or establish an unmeasured height.

Provide a standalone angled picture and a north-up top picture for every **new or geometrically revised unique type**, not per placement. Both views must show the same complete saved model and use the same canonical orientation and local grid. Preserve the existing current previews of unchanged types; do not regenerate them solely to satisfy this new-view policy. Use the authored **0° orientation**, untranslated compiled geometry except for normalizing its local display grid, and a local southwest tile centre **(X0, Y0)**. Show the source-backed display title, X/Y ticks, the 16 m city grid, scale, and view direction; retain the exact registered menu name in the README and render evidence. Do not show P-labels, trumpet/global coordinates, assembly roles, or assembly-specific rotations in this picture. Every visible caption must be self-contained: only the reusable type display title, local grid, canonical orientation, type/height facts, and software-preview status. Do not mention a trumpet or other interchange, assembly positions or rotations, placement labels, or “see the guide” in titles, subtitles, or footers. These contextual references belong only in the Markdown or JSON placement mapping. Record every visible caption verbatim in render evidence. Keep the software construction reference and the local display-grid reference distinct; a sparse piece can have an empty construction reference cell. Never invent geometry or move a track merely to normalize displayed coordinates.

Store the full angled image as **`00_pieces/<piece-id>/preview.png`**, its thumbnail as **`00_pieces/<piece-id>/preview-thumb.png`**, and the full north-up top image as **`00_pieces/<piece-id>/preview-top.png`**, beside `piece.json` and `icon.png`. A second top-view thumbnail is optional. Show both full views in that type's README. Repeated copies share these images and one menu button. The guide needs both a type/image/quantity table and a placement/position/rotation table. State that the standalone image is at 0°; use the rotation column to rebuild the assembly. Record each view's role (angled or top-down), exact input model/DAT hashes, canonical orientation, local display grid, camera, and image hashes in render evidence; retain the angled thumbnail hash as well. Both views must identify the same geometry rather than separate reconstructed models.

Use one shared three-row header for standalone angled pictures, north-up pictures, and connection overviews. `framework/scp/render_headers.py` owns the title, wording, colours, and font rules; `piece_previews.py` and `connector_overview.py` both use it. The standalone assembly-parts helper delegates to the same renderer. Changing the camera or adding cards must not invent a different piece name or subtitle style.

| Row | Content | Example |
| --- | --- | --- |
| 1, bold dark text | One source-backed display title, with each nominal level and measured path height in parentheses; retain the exact registered menu name separately in evidence. | `HSR Paired Quarter-Turn Level 2 (15.5 m) to Level 4 (30.5 m)` |
| 2, blue text | Reusable-piece role, actual camera direction, optional connection-overview role, and authored orientation. | `Reusable piece / Southeast view / Authored orientation: 0°` |
| 3, grey text | Independent local grid, derived piece reference where applicable, tile size, and meaning of the grid labels. | `Independent local X/Y grid / Piece reference: X0, Y6 / 1 tile = 16 m / Labels mark tile centres` |

Derive the reference position from `local_piece_grid`; do not hardcode a coordinate for a particular footprint. A 45° azimuth in this renderer is the Southeast view, while the north-up top view uses 0° azimuth and 90° elevation. The same display title appears in all three images, and source-backed height details occur once per level. Keep `1 tile = 16 m` in the third row only; suppress the redundant grid footer. Keep the software-preview and unverified-game statements readable elsewhere in the image.

Assembly pictures keep their existing fixed global grid, placement P-labels, exact menu-name callouts, and assembly rotations. Do not restart their X/Y numbering because a standalone type image uses local zero. Do not leave old per-placement type pictures or obsolete types as retired artifacts.

## Assembly picture set and in-picture identification

Show the whole actual compiled interchange from above and from at least two opposite oblique angles. An **oblique view** looks down from an angle, so height differences and pillars remain visible. Add a close-up where a join, crossing, or support needs discussion. Label software previews accurately.

Every future user-facing layout or rendered review image, whether top, oblique, whole-interchange, or a standalone type, must carry a readable city-grid reference. Assembly views use the [fixed global coordinate contract](#coordinate-contract-for-charts-and-renders); standalone types use their own [canonical local grid](#reusable-names-and-standalone-type-pictures). A perspective image without a matching coordinate grid is incomplete for a design review.

Deliver two complementary kinds of view:

- **Clean overviews:** one north-up top view and one oblique view without part names, instance IDs, leader lines, or part-name side keys. Keep the coordinate grid, X/Y labels, compass, scale, and view-direction caption. These show the overall shape without the rebuilding annotations.
- **Named rebuilding/review views:** the top and both opposite oblique views, plus an occupied-tile construction plan. These identify every placed module inside each image using the rules below. Preserve them alongside the clean overviews so a reader can still reconstruct the assembly.

Generate clean and named counterparts from the same compiled models and exact placements. Match their camera directions and suppress annotation layers. Clean views may use the freed side-key space to show the model at a larger scale; record each actual camera and framing in the evidence. Do not move tracks, hide geometry, or change the layout for either version. Present the two clean overviews first in the human guide, followed by the named views and construction plan. Record the annotation mode and image fingerprints separately in render evidence. The minimum set for an assembled interchange is six images: two clean model views, three named model views, and one named construction plan.

In every **named rebuilding/review image**, each placed module must be identifiable inside that image:

1. Show its stable instance label and exact descriptive SCP menu name, for example `P04A — HSR Modular One-Tile Two-Level Crossing`. The common `SCP | [PART HSR]` menu prefix may be explained once in the image key. Do not replace a menu name with a role such as “bridge” or “eastern merge”.
2. Connect each callout to that instance's actual occupied tile or visible geometry using a leader line. A **leader line** is a thin line from the label to the object it identifies; finish it with a clear dot or arrow. A construction origin can lie in an empty cell, so do not use an unchecked origin as the sole geometry target.
3. Put long names in an in-picture side key if they would obscure tracks. Match each full-name key entry to the same visible instance ID and leader line. A key in a separate Markdown paragraph is insufficient: an exported picture must remain understandable by itself.
4. Label repeated instances separately and point to each one. A bracketed group is acceptable only when each instance's position and unique ID are still unambiguous. Keep callouts readable at the delivered resolution; use larger margins, a larger image, or a labelled close-up instead of hiding geometry or covering joins.
5. Derive IDs and menu names from the current machine-readable placement plan and registered manifests. Record their anchors and full names in render evidence so the rendered key can be checked against that plan. Names, arrows, and colours must not imply an unbuilt one-click piece or tested game behaviour.

Check delivered images for readability as well as checking their metadata. If additional placements make full-name callouts exceed the available side-panel space, increase the canvas dimensions and record the delivered resolution. Keep the existing minimum readable font and complete names; verify that cards, labels, leader lines, and the grid still fit. Reuse the canonical picture when the same type appears in several placements.

Discuss the rendered shape, symmetry, route clarity, joins, supports, and space use with the user through [assembly review step 6](WORKFLOW_ASSEMBLY_CREATION.md#6-review-coordinate-labelled-renders-with-the-user). A comment about a particular coordinate must refer to the same place in every image. Do not change approved geometry solely to improve a camera view.

### Ownership colours

Colour ownership by placed module. Every pair sharing a tile side or corner must have clearly different fill and outline colours; non-neighbours may reuse colours. Use the same assignment in named model views and the tile plan, with readable text contrast. Draw thick outer/inter-piece boundaries (6 px with a 10 px white halo in the current renderer) and thin internal city tile lines (1 px). A seam between two placements of the same type still needs a thick boundary and distinct neighbouring colours. Record palette, adjacency, contrast, and boundary strokes in render evidence and inspect the actual PNG.

<a id="current-renderer-support-and-the-top-view-gap"></a>

## Current renderer support and canonical top views

The requirements above describe the delivered artwork. Existing tools have different scopes:

| Existing tool | Current executable support | Limit |
| --- | --- | --- |
| `framework/scp/preview.py --catalog` | Canonical angled and north-up actual-model views, portable view-specific evidence, independent caches, and explicit selected-piece/view coverage. | Defaults to the angled view for compatibility; request `--views angled top` for both, or `--views top` to preserve an existing angled image and thumbnail. |
| `domains/high-speed-rail/tools/render_hsr_assembly.py` | Actual compiled assembly models, the fixed 16 m X/Y grid, clean top/oblique companions, named top/opposite oblique views, and an occupied-tile placement plan for the current HSR scene workflow. | This is the existing domain helper, not a registered generic assembly renderer for every future network. A raw model alone lacks the placement metadata needed for named views and ownership plans. |
| `domains/high-speed-rail/tools/render_hsr_assembly_parts.py` | Uses the shared standalone renderer and header for each unique type in an audited assembly scene; repeated `--top-piece-id EXACT-ID` adds north-up views. | Retains its scene restriction and stages filenames plus a combined evidence report under `--output-dir`; use the generic catalogue command for canonical piece-local files. |
| `framework/scp/connector_overview.py`, through `scp.py connectors` | An actual compiled-model connection overview, complete boundary cards, provenance, a resolved export, and the marked piece README section for supported declarations. | A connection overview supplements canonical angled/top previews; it does not create those separate catalogue views. Current connector coverage is the two intentionally migrated types, and the card renderer requires one measured height per service group. |

The generic catalogue command now produces the complete model's north-up view without requiring an assembly scene or a piece-specific helper. Run from the parent project directory after the editable installation described in [BUILD_AND_INSTALL](BUILD_AND_INSTALL.md#build-a-selected-collection). Replace `EXACT-PIECE-ID`, `BUILD_NAME`, and the texture-directory placeholder with actual values:

```sh
python3 -m scp.preview --catalog --root custom-pieces --output custom-pieces/dist/BUILD_NAME --plugins '/absolute/path/to/Plugins' --include EXACT-PIECE-ID --views angled top
```

Repeat `--include` to select several exact registered types. The supplied verified build must contain every selected type. The command writes `preview.png`, `preview-thumb.png`, `evidence/preview.json`, `preview-top.png`, and `evidence/preview-top.json` beside each selected definition. Each evidence record identifies its own role, actual model and DAT, textures, camera, local grid, captions, generator settings, and output hashes. Both views use the same compiled model. The coverage report states the requested selection and views explicitly; types outside that selection are not a failed or completed migration.

Use `--views top` to add or refresh only the top view; it must leave an existing angled image, thumbnail, and angled evidence untouched. An unchanged repeat reuses each view only when its inputs, evidence, and output image hashes still agree. Missing or altered evidence, top images, or angled thumbnails invalidate the relevant view. A top-only run must not satisfy coverage for a missing angled view. Preserve valid unchanged types' images unless their artwork is deliberately revised.

The existing HSR assembly helper can be used for a type that meets its actual scene restriction. From the parent directory containing `custom-pieces`, the following example writes review outputs into private staging and adds a top view of one type already used by the V4 assembly. Replace the Plugins placeholder with the actual existing texture directory:

```sh
python3 custom-pieces/domains/high-speed-rail/tools/render_hsr_assembly_parts.py --scene custom-pieces/domains/high-speed-rail/01_assemblies/straight-stem-trumpet-v4/assembly.json --build custom-pieces/dist/straight-stem-trumpet-v4 --plugins '/path/to/SimCity 4/Plugins' --output-dir custom-pieces/local/documentation-generation/parts --prefix reviewed-part --top-piece-id hsr-component-modular-crossing-core
```

This helper also renders an angled image for every unique type in that scene. It produces `<piece-id>-southeast-local-xy.png`, its `-thumb.png`, selected `<piece-id>-top-local-xy.png` files, and `reviewed-parts-preview-evidence.json`. The report maps staged files to exact types, images, cameras, local grids, source DAT/model hashes, and assembly placements. The `canonical_filename: preview-top.png` field describes the intended role; it does not copy the file into the piece directory. The current helper supplies no automatic command to promote this staged set and its combined report into canonical piece-local top-view evidence. Review that handoff explicitly, preserve the provenance of any deliberately integrated artifact, and do not call the generic catalogue complete on the strength of this staged run.

For the current HSR assembly's six-image set, use its audited scene and matching verified build. This existing example also stages its output without overwriting maintained pictures:

```sh
python3 custom-pieces/domains/high-speed-rail/tools/render_hsr_assembly.py --scene custom-pieces/domains/high-speed-rail/01_assemblies/straight-stem-trumpet-v4/assembly.json --build custom-pieces/dist/straight-stem-trumpet-v4 --plugins '/path/to/SimCity 4/Plugins' --output-dir custom-pieces/local/documentation-generation/assembly --prefix reviewed-assembly
```

The helper writes named `reviewed-assembly-{top,southeast,northwest}-xy.png`, clean `reviewed-assembly-{top,southeast}-clean-xy.png`, `reviewed-assembly-placement-plan-xy.png`, and `reviewed-assembly-preview-evidence.json`. Inspect the images and their actual report before updating an assembly's maintained `previews/`, links, and evidence. Use the owning assembly's exact plan, current input build, checked dimensions, and documented command when rendering another accepted layout. A catalogue preview does not replace coordinate-based assembly review.

## Maintain the complete preview catalogue

The generic catalogue renderer reads each selected DAT's actual S3D preview and its referenced FSH texture atlases. Do not substitute a menu icon, a schematic, or an invented illustration for compiled-model evidence. The piece inventory links one canonical image per type, while the assembly inventory links complete-layout pictures. Each reusable type owns its canonical files under its domain's `00_pieces/<piece-id>/`; the [standalone-picture contract](#reusable-names-and-standalone-type-pictures) defines their roles and the separate top-view requirement.

1. Build and verify every new or changed piece first. Use [BUILD_AND_INSTALL](BUILD_AND_INSTALL.md) for the build commands. Keep missing current resources pending.
2. From the parent directory containing `custom-pieces`, render a freshly built all-piece candidate with this exact existing catalogue command. Replace the Plugins placeholder with the actual directory containing the required textures:

   ```sh
   python3 -m scp.preview --catalog --root custom-pieces --output custom-pieces/dist/current --plugins '/path/to/SimCity 4/Plugins' --progress
   ```

   For several current subset candidates, repeat `--output`; the last build supplies a repeated piece ID. Built definitions must match the current registry. Dependencies and editable installation are in [BUILD_AND_INSTALL](BUILD_AND_INSTALL.md#build-a-selected-collection). The default scope is the angled view and thumbnail; add `--views angled top` for both required views of a new or revised type, and repeat `--include EXACT-PIECE-ID` to keep the operation selected.
3. Inspect changed routes, tracks, walls, piers, joins, and shadows. Record human preview approval separately; generating an image does not confirm approval or game operation. Check readability at the actual delivered resolution, not just the provenance fields.
4. Require `coverage.complete` for the requested piece selection and views, with no missing or stale records in that selection. Inspect `selected_piece_ids`, `selected_count`, and `requested_views`; outside-selection pieces do not count as missing in this primary report. The separately labelled `catalogue_coverage` reports all registered types; require its completeness only for a deliberately full-registry audit. The default acceleration/coverage index is private `local/cache/preview-index.json`; it is rebuildable and excluded from exports. Each piece's portable `evidence/preview.json` records the actual model, texture, renderer, and PNG hashes. Reuse requires matching inputs and exact current image hashes; historical build names alone are insufficient. The [framework implementation contract](FRAMEWORK_ENGINEERING.md) owns bounded caches, selected DAT reads, shared texture loading, and pixel equality with the reference renderer.
5. After actual-resource extraction when required, refresh generated connector outputs, then bind review cases to the final images through [the final-artifact procedure](#final-artifacts-and-packaging). A prose-only refresh does not update image-review dependencies or extract resources. Check local Markdown links, then finish and freeze preview writes before tests or packaging copy the source.
6. Package the final current documentation and images using `package --refresh-docs`, followed by a current source package. The copied source tree describes the current registry, while the candidate manifest identifies the exact selected subset. Old flat catalogue panels and old build ZIPs are not required inputs.

## Menu artwork and source registration

Every piece keeps its own `icon.png` and registered exact menu name beside `piece.json`. Derive identity, network labels, and type vocabulary from the same owning domain source used for menu text and registration, rather than inventing a caption or class from an assembly P-label. Inspect all four native-size menu states. The [framework icon contract](FRAMEWORK_ENGINEERING.md#icon-encoding-and-maintenance) owns the PNG dimensions, frame order, encoding, resource binding, and verification; the [player legend](BUILD_AND_INSTALL.md#recognize-scp-menu-icons) explains the visible vocabulary.

Use the owning domain's registration/artwork entry point, listed in its network specification; the [HSR registration table](../domains/high-speed-rail/NETWORK_SPEC.md#registration-and-artwork-tools) is the existing implementation. Several HSR commands allocate or register definitions and named selections as well as generating icons. They are not interchangeable with an artwork-only refresh. For a name or style change, coordinate manifest/menu text, icon identity, registration, inventory labels, saved-resource verification, and current documentation while preserving existing game IDs and geometry. Static icon validation does not establish menu selection behavior in the game.

## Connector exports and connection overviews

The [connector metadata reference](CONNECTOR_METADATA.md) defines channels, boundary intersections, coordinates, permissions, and matching rules. The following procedure preserves the complete source-owned connector generation contract. Create or change a piece through [WORKFLOW: Piece Creation](WORKFLOW_PIECE_CREATION.md) first; connector refresh reads an existing verified build.

### Inputs and outputs


An **overview** is a generated explanation of a reusable piece's exposed connections. A **boundary card** is the detailed panel for one actual source cell and edge. A **source fingerprint** is a SHA-256 value identifying exact input bytes. These fingerprints allow a later check to detect that an output is missing or stale, meaning it describes earlier inputs.

| Piece-local file | Role |
| --- | --- |
| `piece.json` | Existing authoritative type, resource identities, and occupied source cells. |
| `connections.json` | Existing measured directional ports, resource fingerprints, and internal journeys. Connector commands read and verify this file. |
| `connector-groups.jsonc` | Authored stable component, group, channel, cut, and member associations, permissions, boundary bundles, and optional defaults. References measured ports rather than copying their coordinates. |
| `connector-data.json` | Generated resolved connector export, including measured geometry, permissions, journeys, and full source PATH polylines. Consumer applications can read this file; exports and overview generation use the same complete resolved representation. Do not hand-edit it. |
| `connection-overview.png` | Fresh compiled-model scene, boundary markers, and complete cards. This image supplements the existing canonical previews. |
| `evidence/connection-overview.json` | Generated provenance: the source evidence and fingerprints tying that overview to its inputs and output image. |
| `README.md` | Existing single piece guide. Its `CONNECTOR OVERVIEW` block is generated; maintained explanations stay outside the markers. |

Use the [connector reference](CONNECTOR_METADATA.md#6-stable-identity-reuse-and-file-ownership) for source authority, optional defaults, and schema ownership. This procedure currently covers the two migrated HSR types in its [Examples](CONNECTOR_METADATA.md#8-examples-the-two-existing-hsr-pieces); it does not imply whole-catalogue coverage.

The source pipeline resolves the declaration and measured records once and uses that complete representation for both export and overview generation. It can pass the resolved records directly to the renderer, so the renderer need not reread a just-written export. Standalone library rendering resolves the same authoring inputs through the shared API. No separate overview-only measurement or manually copied card geometry is introduced.

Keep the outputs beside the piece and refresh its existing README block; do not create another per-piece connection or checklist Markdown page. [STRUCTURE.md](../STRUCTURE.md) owns the full file map, and [TESTING.md](TESTING.md) owns manual observations. Consumer applications must read the generated export and keep their reports separately.

### Before refreshing

1. Use an existing verified compiled build whose resources match the current piece. If the recipe or resources changed, finish the implementation, build the actual game resources, and pass the relevant saved-resource checks first. Regenerating cards for an unchanged piece reuses the existing build and needs no new build or upstream extraction. A JSON definition or visible model alone does not establish working routes.
2. After a real route, geometry, or construction change, run the owning domain's actual-resource extraction workflow to update `connections.json` and its scoped evidence. For HSR, run the following command from the parent project directory after editable installation. Replace `BUILD_NAME` with the verified build's actual directory name and `EXACT-PIECE-ID` with the exact registered ID of the changed non-draft HSR type:

   ```sh
   python3 -m scp_hsr.hsr_connections --root custom-pieces --build custom-pieces/dist/BUILD_NAME --piece EXACT-PIECE-ID
   ```

   Repeat `--piece SECOND-PIECE-ID` for another changed type in that same verified build. This convenience selector extracts and refreshes only the selected types, even when the build contains unchanged approaches. It reads catalogue definitions for validation, but does not load unrelated cached connection evidence, refresh assemblies, or rewrite global connection classes or inventories. Selection requires exact, unique, nonempty, non-draft HSR IDs present in the supplied capture; invalid selections, mismatching source definitions, and invalid selected resources fail before refresh writes. Inspect `extracted_piece_ids` to confirm the actual selection.

   Read `deferred_assembly_ids`, `connection_classes_refresh_required`, and `inventory_refresh_required` in the result; they identify work deliberately deferred by selected extraction. When affected assemblies or global views need refreshing, use the build-wide extraction command below with a verified capture containing the resources intended for remeasurement. Omitting `--piece` retains the existing behavior: process supported non-draft HSR types present in the build, preserve uncaptured measured records, refresh affected saved-assembly evidence using required cached records, and regenerate the global views. It skips drafts and does not discover counterpart candidates:

   ```sh
   python3 -m scp_hsr.hsr_connections --root custom-pieces --build custom-pieces/dist/BUILD_NAME
   ```

   A verified build containing only the changed types remains an alternative to selecting them from a combined build. Build that subset with repeated `scp.py build --include EXACT-PIECE-ID` arguments, verify its output, and point the build-wide extractor at that subset directory. Its assembly and global-view refresh behavior still applies. These are actual-resource extraction operations; a prose-only refresh needs neither operation.
3. Review or generate `connector-groups.jsonc` as part of authoring the piece. Declare physical-channel and cut associations from the source, retain stable IDs, and associate every required measured member with its channel and permission. Beside each reused `profile_id`, add a short inline comment explaining its network, nominal level and measured path height, boundary alignment, family, channel count and direction arrangement, running convention, and revision tokens; do not leave a beginner to decode the identifier alone. Explain why one physical channel retains its ID at both ends, while local members and cuts have their own IDs. Do not infer a shared car/tram channel from overlapping routes alone. Renew source bindings only after confirming the declarations still describe the new sources.
4. Keep source-port identities, game resource identities, approved geometry, and manual observations intact. Connector refresh does not replace extraction, repair a stale source declaration, or mark a game test passed.

If only maintained prose changes, use the [README refresh procedure](#readme-layouts-and-generated-sections); it preserves measured connections and observations. If connector declarations change, regenerate their export and overview. If saved resources change, start with verification and extraction again. This order prevents an old measurement or picture from being relabelled as current evidence.

### Refresh and check the two migrated pieces

Open a terminal. On macOS, press **Command + Space**, type **Terminal**, and press **Return**. Replace `/path/to/sc4-simons-custom-pieces` below with your checkout's full path, keep the quotation marks, and press **Return** to select its library directory:

```sh
cd '/path/to/sc4-simons-custom-pieces/custom-pieces'
```

The checkout root is the folder containing `custom-pieces/` and the repository README; the final `/custom-pieces` selects the library inside it.

Type `python3 --version` and press **Return**. Python must be version 3.11 or newer. Use the existing project dependencies; the [build instructions](BUILD_AND_INSTALL.md#build-a-selected-collection) explain editable installation, Pillow, and NumPy when preparing a new source checkout.

Run this command to verify the two pieces against the existing saved V4 build, resolve their authored declarations, write their generated exports, and regenerate their overviews and marked README blocks:

```sh
python3 scp.py connectors refresh --piece hsr-component-modular-crossing-core --piece hsr-component-tight-paired-curve90-l4-to-mid --build dist/straight-stem-trumpet-v4
```

`--piece` selects one exact registered type and can be repeated. `--domain` defaults to `high-speed-rail`. `--build` selects an existing build directory relative to `custom-pieces`, unless an absolute path is supplied; its default is `dist/current`. The example explicitly selects `dist/straight-stem-trumpet-v4`, the existing compiled input used by this two-piece trial. Refresh does not build that directory. Select another verified build only when its resources match the current measured source records.

Rendering and artwork freshness checks also need the models' existing material textures. Use the configured project texture inputs, or append `--plugins '/absolute/path/to/Plugins'` to select an existing texture directory for refresh or check. Replace that placeholder with the directory's actual path and retain the single quotation marks if the path contains spaces. Texture inputs are read only; no connector command installs or alters Plugins files.

Now run the read-only freshness check with the same selection and build:

```sh
python3 scp.py connectors check --piece hsr-component-modular-crossing-core --piece hsr-component-tight-paired-curve90-l4-to-mid --build dist/straight-stem-trumpet-v4
```

The check validates the source declarations and compiled-resource agreement, compares the saved export with the freshly resolved result, and checks the canonical overview's recorded input and output fingerprints, current material textures, fonts, and renderer settings. Missing or stale outputs are failures, rather than a request to silently rewrite them. Read the command's JSON result and resolve any reported input or provenance mismatch before using the outputs.

To refresh only machine-readable exports, add `--no-render` to `connectors refresh`. Add `--no-render` to `connectors check` only when deliberately checking that machine-readable scope without artwork. A successful check in that scope does not establish overview freshness. Ordinary authoring completion includes the image, its evidence, and the generated README block.

### Reading an overview

The overview shows one clean scene rendered directly from the selected compiled model and its textures at the piece's authored 0° orientation. It does not paste a previously captioned preview into a new frame or reconstruct track geometry from metadata. The existing `preview.png`, `preview-top.png` where present, and their evidence retain their separate roles.

Each actual source cell and exposed edge has one card, identified by its boundary bundle. Several service groups declared on that same boundary appear as sections of that card; they are not independent attachment choices. Short scene markers such as A and B point to the cards. Stable boundary, group, and member IDs remain visible in the detailed output.

Give each service group its own bordered inset panel, numbered `1 / 3`, `2 / 3`, and `3 / 3` when three groups share an edge. Its tinted header names the network and **Level (path height)**, with the stable group ID underneath. Keep a clear gap between panels, and state above them that all groups are required together at this edge. For parallel HSR above Road, the HSR, Road-vehicle, and pedestrian panels remain visually separate even though they belong to one mandatory boundary connection. Use the same section structure in the selectable Markdown details.

Markers are deterministic display labels: sort bundles by source column, source row, edge rank **south → north → west → east**, and then stable boundary ID; assign letters in that order. Sort service groups inside a card by stable group ID. Reordering arrays in the source must not change the displayed mapping. For the crossing, A is the south upper end, B the north upper end, C the west lower end, and D the east lower end; for the curve, A is the south high end, and B the east custom-height end. Letters are not source identities or traffic instructions.

Cards sit below the model scene. The current curve has two cards across, and the crossing has a 2 × 2 grid. Each card or service section uses the same block order:

| Block | Required content |
| --- | --- |
| Identity | Boundary/group and component IDs, network service, and game transport class and routing role. |
| Boundary and alignment | Source cell and edge, measured section origin where applicable, centring and signed offset, one **Level (path height)** row, outward heading, and slope at the joining edge. |
| Channels and traffic | Physical-channel count in the complete section, physical edge-cut count, directed-member count, running arrangement, permissions, and measured spacing where meaningful. |
| Directed members | Full stable member ID, channel and cut association, incoming or outgoing flow, exact east/north/height position, applicable offset, outward heading, outward grade, and source-port reference. |
| Source references | Full profile reference when used, and the source references required to trace the resolved data. A missing optional profile is explicitly identified. |

The combined height row says **Level 4 (30.5 m)**, **Level 2 (15.5 m)**, or **Custom (23 m)** for these examples. The custom 23 m end has no assigned nominal level. The label never substitutes for the measured height, and a common displayed value is used only when that card's members actually agree.

Each card retains its own matching facts, including values also present on other cards. The shared legend explains conventions only: coordinate units and source/display-grid conversion, outward heading with **0° north and clockwise angles**, outward slope, offset signs, and incoming/outgoing flow. Keep one piece title and one evidence footer. Use regular text for field labels and values, and bold for titles and section headings. Callouts may move for readability; models, source intersections, and supports must not move.

The current card renderer requires one measured height per service group; declare different heights as separate groups within the appropriate boundary bundle. It retains each member's own heading and grade when those differ. The model and DAT must match the selected build manifest and saved route/model resource fingerprints. An earlier preview fingerprint is an optional comparison, rather than a substitute for those current inputs or a requirement to keep using an old build.

The current source cells use `[column,row]`, with columns east and rows south; measured positions use `[east,north,height]` in metres. The picture's local grid increases north from its southwest tile. Explain that display conversion rather than changing the authoring coordinates. The metadata reference's [position definitions](CONNECTOR_METADATA.md#31-which-position-or-centre-is-meant) distinguish the fixed piece anchor, bounding-box centre, tile centre, tile-edge midpoint, section origin, and individual intersections.

## README layouts and generated sections

A reusable piece has one README; an assembly has README plus TESTING. Keep a player guide and network specification per domain, with separate generated piece and assembly inventories. Preserve authored prose outside generated markers and update the generator when changing its output structure. Do not add separate per-subject connections, checklist, or recording-help Markdown files. Preserve all actual connection/observation data and current images when consolidating prose; check files, heading links, and regeneration.

### Piece README

Keep a piece's useful function, exact identifier and menu name, network services, footprint, supported rotations, intended interface families and required adapters, limitations, and current evidence in its existing README. Show canonical angled and top views for new or geometrically revised types under the [standalone contract](#reusable-names-and-standalone-type-pictures), preserve unchanged types' current previews, and include the generated connection overview for intentionally migrated types. Reference the exact measured connection and manual records instead of hand-copying their coordinates or checkbox state into maintained prose. Generated intrinsic connection tables do not publish legacy neighbour shortlists or a mandatory port/counterpart manual matrix. Automatic complete-boundary compatibility discovery is not supplied by the current library; any future consumer must exclude incomplete or stale inputs explicitly.

The connection overview's image and selectable Markdown details come from the same complete resolved records used for `connector-data.json`. Keep those generated details in the existing `CONNECTOR OVERVIEW` block so full IDs, numerical fields, permissions, and source references remain readable and copyable without extracting text from a PNG. Maintain shape-specific explanations and unresolved limitations outside generated markers. Do not copy the shared metadata format or generation procedure into each subject README.

### Required Markdown guide for each modular interchange

Create `domains/<domain>/01_assemblies/<assembly-id>/`, using the [straight-stem trumpet guide](../domains/high-speed-rail/01_assemblies/straight-stem-trumpet-v4/README.md) as the example. Register `assembly.json` in that domain's `domain.json` and link the blueprint from its human overview. Keep exactly two Markdown files: `README.md` for the complete human rebuilding guide (overview, pictures, pieces, placements, connections, and journeys), and `TESTING.md` for software evidence, technical limitations and generated human checks. Shared observation-recording instructions live once in [framework TESTING](TESTING.md); link them and include the subject-specific command instead of repeating the procedure. Put artwork in `previews/`, authoritative manual observations in `checks/`, and durable software/render reports in `evidence/`. The generated assembly inventory links one clean preview to this guide. Across these two files include:

1. **What is built:** the intended networks, levels, dimensions, required movements, and terrain assumptions; an explicit modular-blueprint label and the fact that no complete one-click button is supplied.
2. **Six current pictures:** a clean top and clean oblique model view, a named top view, two named opposite oblique views, and a named occupied-tile plan. All follow the same southwest `(X0, Y0)` tile-centre grid, with no global origin annotation. Named pictures contain exact menu names, stable instance IDs, and leader lines; clean pictures retain coordinates while omitting those part annotations.
3. **Coordinate instructions:** X increases east/right and Y north/up on the north-up plan; give the 16 m tile size and full nonnegative X/Y ranges. Use the shared southwest-zero convention without an in-picture origin annotation. Keep display and technical authoring coordinates explicitly separate.
4. **Parts and placements:** exact menu names and permanent piece IDs; quantity per type; one instance ID per placement (`P01`, `P02`, etc.); each instance's displayed construction reference position, rotation and connection heights. Explain empty reference cells and unverified cursor anchors; picture callouts use **Position X7, Y13**, not **Origin**.
5. **Rebuilding order:** numbered selection and placement steps, supported rotation controls, exact matching connections and approach requirements. Explain why overlapping tile ownership is forbidden. Cover all permitted journeys and forbidden transfers, not just the visible track shape.
6. **Evidence and limits:** the machine-readable placement-plan link, exact build/source fingerprints, compiled-piece and complete-assembly checks, render evidence, and rotation checks. State which game behaviours remain unverified; software renders and installation hashes are not game tests.

Update the guide, machine-readable plan, picture names/IDs, placement tables, and evidence together after every accepted layout revision. An assembly chart or parts list alone is insufficient rebuilding documentation.

When changing a picture's coordinate-label format, use a new descriptive image filename and refresh every current guide link and evidence record. A reused image path can show cached older artwork in an already open guide. Validate the newly linked image itself, then remove the superseded source preview file; do not retain an obsolete alternative picture.

### Refresh generated Markdown and inventories

A **generated block** is a section bounded by named HTML comments, such as `<!-- BEGIN PIECE OVERVIEW -->` and `<!-- END PIECE OVERVIEW -->`. Edit its source data or its owning generator, rather than editing text that the next run will replace. Keep authored prose and valid existing metadata headers outside these blocks; preserve frontmatter on repeated refreshes. Follow [STRUCTURE.md](../STRUCTURE.md#markdown-metadata) for the four-field document metadata convention and its existing subject exceptions. Write each prose paragraph on one physical source line, with blank lines between paragraphs.

`scp.content` owns `PIECE OVERVIEW`, `CONNECTIONS`, `MANUAL SUMMARY`, and `MANUAL CHECKS` views; connector refresh owns `CONNECTOR OVERVIEW`; inventory generation owns domain `COLLECTIONS` navigation and the illustrated inventories. Keep the connector block outside other generated markers. Assembly manual checks belong in its `TESTING.md`, while a piece's checks stay in its single README. Source definitions, placements, measured connections, source-port identities, class records, and human observations remain authoritative JSON, not Markdown checkboxes.

For a prose-only or generator-presentation refresh, return to the repository root containing `custom-pieces/` and the root README. Replace the placeholder path in the first command with your checkout's full path, keep the quotation marks, and run both commands:

```sh
cd '/path/to/sc4-simons-custom-pieces'
python3 -m scp.content refresh --root custom-pieces
```

This reads existing portable measurements, refreshes generated subject sections and inventories, preserves connection/class/observation JSON byte for byte, and does not verify or extract changed DATs. Existing source-bound connector output has its separate refresh/check command; a prose-only refresh preserves its marked block. Do not use this command to make outdated route measurements appear current. The [framework generator contract](FRAMEWORK_ENGINEERING.md#documentation-generation-and-observations) defines preservation, exact case scope, idempotence, and meaningful generator checks.

Changing the presentation does not retire old cases from their authoritative records. For the intentional one-time removal of generated endpoint/counterpart cases from active coverage, use `python3 custom-pieces/scp.py observations retire-connections --all`, or select exact subjects as described in [TESTING](TESTING.md#data-ownership-and-stale-evidence). The operation retains meaningful historical results, changes no measurements or resources, and creates no replacement pair-testing matrix. New intrinsic extraction does not recreate those retired cases.

To refresh only catalogue/navigation views from existing records, run from the same parent directory:

```sh
python3 custom-pieces/scp.py inventory
```

Inventory refresh does not create missing previews, extract resources, verify a DAT, or record a manual pass. Inspect the generated piece and assembly inventories, domain collection counts, and their relative links. Keep failed and stale observations, exact counterpart/pose/rotation/environment scope, and removed-case history intact. Record new human observations only through [TESTING.md](TESTING.md), using an explicitly confirmed matching observation and the subject's exact command.

## Final artifacts and packaging

Use this sequence after the implementation, schemas, registry, and required compiled builds have stopped changing. A later source addition or real resource change requires the affected validation and connector refresh again. Do not rebuild merely to capture a newer README.

1. Verify the actual compiled resources and extract changed route measurements through the owning domain. Select the intended build and subjects. For unchanged resources, preserve the existing measured records.
2. Generate the required standalone angled and top images through the generic command above, then run `connectors refresh` and `connectors check` for migrated types. Inspect the actual PNGs for clipping, complete geometry, consistent headers, and readable connection groups.
3. Bind manual review cases to the final actual images. From the parent directory containing `custom-pieces`, replace the placeholder with the selected type's identifier:

```sh
python3 custom-pieces/scp.py observations refresh-images --piece EXACT-PIECE-ID
python3 custom-pieces/scp.py inventory
```

Repeat `--piece`, select an assembly with `--assembly EXACT-ASSEMBLY-ID`, or deliberately use `--all`. This operation updates only image-review cases for the selected subjects, including separate angled, top, and connector-overview images where present. It records exact PNG fingerprints, preserves all non-image cases and original observations, and never marks an image approved. A changed image makes its earlier approval stale; it does not inherit an approval from a different view. Missing final images remain missing rather than receiving an invented pass. Run inventory afterward because those summaries are a separate view refresh.

4. Finish scoped software checks and local-link checks, then freeze image and documentation writes. Package the verified build with current documentation:

```sh
python3 custom-pieces/scp.py package --output custom-pieces/dist/BUILD_NAME --destination custom-pieces/dist/BUILD_NAME-current-docs.zip --refresh-docs
python3 custom-pieces/scp.py source-package --destination custom-pieces/dist/current-source.zip
```

Replace `BUILD_NAME` with the existing verified build directory. The first command verifies that build, copies its exact compiled payloads, and places current portable documentation plus matching document hashes in the ZIP. It changes no files in the input build. The ZIP's manifest records the delivered documentation, while the source build's original documentation snapshot remains intact. The second command exports current portable sources without compiled DATs, private settings, caches, or workstation textures. Both commands create local archives; neither installs or publishes anything.

Connector exports and new overview evidence bind a canonical fingerprint of the compiled manifest's resource facts, independently of the documentation list and publication/installation state. Exact DAT hashes, selected definitions, dependencies, construction overlays, and all other build facts remain checked. Consequently, packaging final documentation does not create the old cycle in which updating document hashes invalidated the very connector export being packaged. Legacy overview evidence without this stable field retains its stricter raw-manifest check until deliberately refreshed.

Without `--refresh-docs`, `package` deliberately retains the build-time documentation snapshot. Use that behavior to reproduce an earlier artifact, and label it accurately; use the explicit final-documentation option for a current delivery. Preserve skipped or unavailable game checks as unverified, and inspect the archive's final manifest and README rather than assuming a successful ZIP operation supplied manual evidence.

## Freshness and evidence


Generate only after integrated source checks pass and concurrent geometry edits have finished. A repeat run with identical inputs must preserve the resolved meaning, stable markers, and reproducible output. Provenance records identify the actual declarations, profiles where used, measured connections, saved model and texture inputs, generator, and output image. A matching filename or an old build name is not proof of matching input bytes.

Overview generation establishes a software view of the validated inputs. Compiled PATH agreement is a separate source check; a single-piece overview does not test a two-piece placement's owned-cell fit. Physical seams, full model interference, construction clearance, terrain behavior, and game operation remain separate evidence states. Unknown or unperformed checks remain unverified.

Manual observations remain solely in `checks/manual-tests.json`. Connector refresh does not rewrite that record, raw `connections.json`, geometry, or assembly placements. After an actual source change, the upstream extraction workflow preserves observations and their original dependencies, marks affected results stale, and never turns software success into a human pass. Follow [TESTING.md](TESTING.md) when recording an explicit observation.

Before packaging, check local links, selected-piece coverage, generated-data freshness, overview provenance, and the source export's included declarations, schemas, images, and evidence. Keep workstation inputs, private caches, and previous build output excluded. Building, installing, packaging, and publishing remain separate actions.

A portable source package excludes compiled DAT archives and workstation texture inputs. The shared `scp.connector_metadata.load_library(...)` API can validate the authored declaration structure and measured-source references without those game assets. Refresh and the full `connectors check` require an existing local compiled build to re-extract and verify its actual routes; fresh rendering and artwork freshness checks additionally require the referenced textures. Included generated records and artwork retain their provenance, but do not supply missing game assets or make an absent compiled-source check pass.

Before final delivery, compare the current source/placement selection against the generated artifacts, check every local file and heading link, inspect each changed image for legibility and clipping, and confirm that image roles, captions, cameras, grids, and hashes agree with their evidence. A repeat refresh must preserve authored prose, valid frontmatter, source records, stable identities, observations, and generated meaning.
