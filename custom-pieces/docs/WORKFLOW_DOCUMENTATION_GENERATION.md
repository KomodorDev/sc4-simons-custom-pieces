---
title: "WORKFLOW: Documentation Generation"
summary: "Generate and review reusable-piece and assembly artwork, readable guides, connector exports, and evidence from current authoritative sources, with explicit commands and tool limits."
audience: "Piece authors, assembly designers, and maintainers"
document_type: "procedure"
---

# WORKFLOW: Documentation Generation

Use this workflow after creating or changing a reusable piece through [WORKFLOW: Piece Creation](WORKFLOW_PIECE_CREATION.md), or checking a multi-piece layout through [WORKFLOW: Assembly Creation](WORKFLOW_ASSEMBLY_CREATION.md). It owns shared picture, grid, caption, connection-card, README, and documentation-refresh requirements for every transport domain. The owning domain's network specification supplies its actual interfaces and classification; the [HSR network specification](../domains/high-speed-rail/NETWORK_SPEC.md) is the existing example. [FRAMEWORK_ENGINEERING.md](FRAMEWORK_ENGINEERING.md) owns renderer and generator implementation contracts, and [CONNECTOR_METADATA.md](CONNECTOR_METADATA.md) owns connector semantics, schemas, and matching rules.

A **piece type** is one reusable component, selected through its own standalone button or an assembly's component cycle. A **placement** is one copy of that type in an assembly. A **compiled model** is the actual saved game model, rather than a sketch reconstructed from its metadata. A **provenance record** identifies the source files, settings, and output bytes behind an image or table. A software preview, a checked build, an installed file, and an observed game result establish different facts; label each output by the evidence it actually supplies.

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

1. Identify the owning piece’s README, TESTING document where split, and `piece.json`, or the assembly README, TESTING document, and machine-readable placement plan. Read the domain's network specification for actual transport facts. A layout plan must retain exact piece IDs, instance IDs, poses, owned cells, and the current compiled source fingerprints.
2. Confirm the intended build has passed its relevant independent saved-resource checks. A **DAT** is the game's resource archive, **S3D** contains model triangles, **FSH** contains texture images, and **PATH** describes traffic routes. A missing built piece remains pending; an older or similar-looking model is not its replacement.
3. Finish concurrent geometry work and the integrated checks before starting the final render pass. Render the accepted current result, rather than several competing intermediate copies.
4. Open a terminal. On macOS, press **Command + Space**, type **Terminal**, and press **Return**. A **checkout** is your local copy of the repository, and its **root** is the folder containing `custom-pieces/` and the repository README. Replace `/path/to/sc4-simons-custom-pieces` below with your checkout's full path, keep the quotation marks so spaces work, and press **Return** to select that root directory.

```sh
cd '/path/to/sc4-simons-custom-pieces'
```

Type `python3 --version` and press **Return**; Python must be version 3.11 or newer. Use the existing project dependencies. For a new checkout, follow [editable installation in BUILD_AND_INSTALL](BUILD_AND_INSTALL.md#build-a-selected-collection), including Pillow and NumPy. The commands below state when they need the repository root or the `custom-pieces` directory; paths are relative to that stated directory.

## Creation checklist and output files

Use this checklist when creating a subject, rather than treating a copied example folder as complete. **Authored** means that an author supplies and reviews the source; **generated** means that a named tool derives the output from those sources. **Required** below means required before presenting a new implemented type or assembly as a documented experimental candidate. A scaffold can exist earlier with pending text and missing evidence. A file's existence does not establish that its contents are current, that the reader has reviewed its pictures, or that it works in the game.

Work through the stages in order. Commands in this table start from the repository root after [preparing Python and the project](#prepare-the-inputs-and-open-the-project). Replace `EXACT-PIECE-ID`, `EXACT-ASSEMBLY-ID`, and `BUILD_NAME` with the real selected identifiers and build directory. In connector commands, `--build dist/BUILD_NAME` is relative to `custom-pieces/`, even when the command starts at the repository root. The other shown build paths include `custom-pieces/` explicitly.

| Stage and output | Required or conditional | Author or exact producer |
| --- | --- | --- |
| 0. Atomization review line drawing and its input/measurement evidence | Required whenever a user requests an atomization or further-splitting review, including a decision to retain the existing design. | Draw the actual routes, tile grid, candidate cuts, decisions, and physical obstacles through the [required review procedure](WORKFLOW_ASSEMBLY_CREATION.md#required-line-drawing-for-user-requested-atomization); show it directly to the user, and retain it through [atomization review artwork](#atomization-review-artwork). No generic CLI currently produces this analysis drawing. |
| 1. Piece `piece.json`, domain registration, and `config/allocations.json` reservation | Required for a **new type**; preserve these identities for an existing type. | `python3 custom-pieces/scp.py scaffold --domain high-speed-rail --id EXACT-PIECE-ID --name 'Descriptive reusable name' --width 1 --depth 1` creates a disabled draft, reserves its identifiers, and creates the initial README/TESTING pair. Choose the actual footprint first; follow [piece creation](WORKFLOW_PIECE_CREATION.md#2-create-a-draft-and-allocate-its-local-identifiers). |
| 1. Assembly `assembly.json`, domain registration, and `menu-layout.json` entry | Required for a **new assembly**. Reusing existing types needs no new piece/resource allocation. | Authored in that order; follow the [bounded HSR starter](WORKFLOW_ASSEMBLY_CREATION.md#start-a-small-hsr-assembly-from-existing-pieces). No assembly-scaffold CLI creates these source registrations. The template under `docs/templates/` is unregistered. |
| 2. Recipe, independent verifier, source geometry, and acceptance contracts | Required for a new or changed **piece implementation**. A separate `geometry.json`, `checks/quality.json`, or assembly-specific test module is conditional on its implementation, rather than a mandatory filename to copy. | Authored code and contracts through the owning [network implementation map](../domains/high-speed-rail/NETWORK_SPEC.md#implementation-entry-points) and [piece implementation step](WORKFLOW_PIECE_CREATION.md#4-implement-the-recipe-and-the-independent-verifier). No generic command invents the geometry, expected values, or independent verifier. An assembly reuses these implemented types and adds its own placement, seam, ownership, and clearance checks. |
| 3. `dist/BUILD_NAME/` with manifest, compiled DATs, and saved-resource verification | Required for actual-resource evidence. This is a disposable build, rather than canonical source. | `python3 custom-pieces/scp.py build --include EXACT-PIECE-ID --output custom-pieces/dist/BUILD_NAME`, then `python3 custom-pieces/scp.py verify --output custom-pieces/dist/BUILD_NAME`. Repeat `--include` for all required member types, or select an existing named collection. A draft must first have a real recipe and verifier and become experimental. |
| 4. Subject `connections.json`, `checks/manual-tests.json`, `checks/observation.example.json`, and generated documentation blocks | Required. Connections come from saved resources; the observation record initially contains unverified cases. | For a changed HSR piece: `python3 -m scp_hsr.hsr_connections --root custom-pieces --build custom-pieces/dist/BUILD_NAME --piece EXACT-PIECE-ID`. For initial/changed assembly graphs, use the [build-wide extraction route](#before-refreshing) without `--piece`; it also refreshes affected assemblies and shared views. Extraction creates missing current README/TESTING scaffolds. A prose-only refresh cannot initialize an assembly that has no connection/manual record. |
| 5. Subject `icon.png` | Required. It is the canonical four-state menu strip, not a model preview. | Use the owning [artwork entry point](#menu-artwork-and-source-registration). HSR piece artwork: `python3 -m scp_hsr.icons --root custom-pieces` refreshes all registered HSR piece icons. HSR assembly artwork: `python3 -B custom-pieces/scp.py assembly-icons --domain high-speed-rail` refreshes all registered HSR assembly icons after each assembly's explicit network identity is supported. These commands have domain-wide scope. |
| 5. Piece `previews/preview.png`, `preview-thumb.png`, and `preview-top.png`; `evidence/preview.json` and `preview-top.json` | Required angled and top views for a new or geometrically revised type. Retain existing unchanged legacy artwork unless intentionally refreshed. | `python3 -m scp.preview --catalog --root custom-pieces --output custom-pieces/dist/BUILD_NAME --plugins '/path/to/SimCity 4/Plugins' --include EXACT-PIECE-ID --views angled top`. Inspect both actual images and their separate evidence; see [canonical views](#current-renderer-support-and-canonical-top-views). |
| 5. Assembly's six layout images in `previews/`, with render provenance in `evidence/` | Required for a documented new assembly. | The owning renderer stages actual compiled-model images and an evidence report; use the [HSR assembly command and explicit review/promotion handoff](#current-renderer-support-and-canonical-top-views). No generic command currently promotes the staged six-image set into canonical assembly source. |
| 6. Piece `connector-groups.jsonc` | Required for a newly authored supported connector type. Existing unmigrated catalogue types retain their legacy status. Optional domain profiles supply shared defaults. | Authored from actual measured port identities and source geometry under the [connector reference](CONNECTOR_METADATA.md#6-stable-identity-reuse-and-file-ownership). No extractor can infer the physical channel associations, permissions, or a justified exception for the author. A new unsupported network needs its adapter before claiming this generation support. |
| 6. Piece `connector-data.json`, `previews/connection-overview.png`, `evidence/connection-overview.json`, and README `CONNECTOR OVERVIEW` block | Required for that newly supported connector declaration. Assemblies consume member exports; they do not acquire a second hand-authored connector parser. | `python3 custom-pieces/scp.py connectors refresh --piece EXACT-PIECE-ID --build dist/BUILD_NAME`, then the same command with `check` in place of `refresh`. These read the existing verified build; follow the [full refresh/check procedure](#refresh-and-check-the-two-migrated-pieces). |
| 7. Authored README and TESTING chapters, image links, setup, limits, and software results | Required. A generated pending paragraph is an unfinished authoring task. | Fill the [piece README](#piece-readme) or [assembly README](#required-markdown-guide-for-each-modular-interchange) and the [six-chapter TESTING document](#required-piece-and-assembly-testing-layout) outside generated markers. Record only actually executed commands and actual reports; no command supplies a human review or game pass. |
| 8. Final image-case fingerprints, generated views, and inventories | Required after accepting the final artwork and authored text. | `python3 custom-pieces/scp.py observations refresh-images --piece EXACT-PIECE-ID` or `--assembly EXACT-ASSEMBLY-ID`, then `python3 -m scp.content refresh --root custom-pieces` and `python3 custom-pieces/scp.py inventory`. These refresh views and bindings, preserve observations, and create no approvals. |
| 9. Documentation and software checks, followed by the appropriate final package | Required before handing over a candidate. | Run the [read-only documentation check](#check-documentation-without-changing-it), relevant saved-resource/domain checks, and `python3 -B tools/run_tests.py`; report actual skips. Follow [final artifacts and packaging](#final-artifacts-and-packaging). An assembly requires a fresh ordinary source build and its `assembly-menu` step after documentation is final. |

Files that are **conditional** need an explicit reason, rather than an empty imitation of an example. Extra reports, mesh comparisons, `checks/resources.json`, `checks/atomization.json`, and domain-specific test files belong with the subject when its actual claims require them. Preserve frozen historical evidence in place. Keep one authoritative `checks/manual-tests.json`; do not add a second checklist, connection guide, or recording-helper Markdown file. Use [TESTING](TESTING.md) when an actual matching human observation is available.

Before calling the result ready for experimental review, confirm that its source and allocation agree, the actual build passes its required checks, every claimed new view and connector output is current, the authored instructions are complete, and each limitation is stated. Keep untested game behaviour unverified. A successful structure/link check establishes neither native-resource correctness nor human review, and a successful software build establishes neither installation nor game operation.

### Check documentation without changing it

Run this command from the repository root to check all registered pieces and assemblies, plus maintained shared guides:

```sh
python3 -B custom-pieces/scp.py docs-check
```

For a smaller selection, use exact IDs. Each selector can be repeated; supplying either selector limits the subject selection and omits the shared-guide sweep:

```sh
python3 -B custom-pieces/scp.py docs-check --piece hsr-component-lower-paired-straight
python3 -B custom-pieces/scp.py docs-check --assembly straight-stem-trumpet
```

This read-only command validates current document layouts, generated-block placement, local links and anchors, and required implemented-subject files. It reports intentionally retained legacy guides separately instead of silently migrating them. Draft piece pairs can pass without implementation artwork or evidence; authored pending text still needs completion. Linked optional views and reports are checked when present. The command needs no native game inputs and writes no generated documents, resource measurements, images, or observations. Use the owning build, extraction, connector-freshness, and human-observation procedures for those different checks.

## Artwork ownership and folders

Every reusable piece and assembly follows the same folder rule. Its **canonical artwork** is the maintained image used by documentation or packaging. Keep its four-state menu strip as `icon.png` beside the owning `piece.json` or `assembly.json`, its documentation images in `previews/`, and its provenance records in `evidence/`. The menu icon represents the selectable button; a preview shows the piece or complete assembly for a reader. These different roles explain why the icon stays beside the definition while the larger documentation images share a subfolder.

```text
00_pieces/<piece-id>/
├── piece.json
├── README.md                         Views, placement, and intrinsic connection matrix
├── TESTING.md                        New or intentionally migrated split guides
├── icon.png
├── previews/
│   ├── preview.png
│   ├── preview-thumb.png
│   ├── preview-top.png                 Where this view is present
│   └── connection-overview.png         Where connector cards are supported
└── evidence/
    ├── preview.json
    ├── preview-top.json                Where this view is present
    └── connection-overview.json        Where connector cards are supported

01_assemblies/<assembly-id>/
├── assembly.json
├── icon.png
├── previews/                          Complete-layout images
└── evidence/                          Software and render reports
```

Repeated assembly placements reuse their piece type's canonical images and icon. The assembly owns a separate `icon.png` for its single component-cycle button. Keep disposable render staging in `local/` and build/package copies in `dist/`; they are not additional canonical sources. [STRUCTURE.md](../STRUCTURE.md#source-and-data-ownership) maps the remaining definitions, connector exports, and observation files.

A folder reorganization moves existing image bytes and updates maintained links and output paths. It does not redraw geometry, rerun measurements, or supply a new rendering result. Preserve original source, input, renderer, and image fingerprints. If current provenance needs a changed image filename, record the relocation explicitly without presenting its original render as newly executed. Preserve frozen reports and backup snapshots. A renderer source change can still make its strict freshness check require a deliberate later render, even when every relocated PNG byte is unchanged.

### Atomization review artwork

Every [user-requested atomization review](WORKFLOW_ASSEMBLY_CREATION.md#required-line-drawing-for-user-requested-atomization) delivers a readable line drawing as well as its written recommendation. This is an additional analysis view; retain the subject's required canonical model pictures. Show the drawing directly in the review, and keep the durable PNG in the owning piece's or assembly's `previews/`, for example `previews/atomization-review.png`. Retain its editable SVG where produced, or its generating source, and store provenance and measured decisions in `evidence/`, for example `evidence/atomization-review.json`. Use distinct descriptive names for multiple reviews; do not overwrite frozen evidence or introduce a separate atomization-guide Markdown file.

Record the exact subject, reviewed source or saved-DAT fingerprints, geometry source, coordinate frame, orientation, scale, route source, actual image hash, and drawing/generation method. Identify every candidate cut, decision, measured obstacle, replacement type and rotation where applicable, relevant user policy, and any bounded correction. Link the authoritative decision record where one exists rather than creating a second conflicting ledger. Mark source-only measurements, unchecked physical models, enlarged details, and unresolved decisions explicitly. Inspect the exported picture for readable route lines, tile labels, cut markers, legend, and nearby reasons; a successful link check cannot establish that clarity.

Apply the shared subject and purpose caption: `Piece - <display name>` or `Assembly - <display name>` on the first row, then `Component guide | Atomization review | <view direction>` on the second row. Include the reviewed input/status and coordinate reference in the picture. Use local piece coordinates for a standalone review and the fixed assembly grid for an assembly review. Link the image and measurements from the owning TESTING document's existing chapter 3 for current analysis or chapter 6 for history; the README can link that explanation within its existing chapters. An analysis-only review needs no new registered assembly or resource allocation.

After implementation changes the footprint or local numbering, keep any retained proposal clearly historical with its original coordinates and input fingerprints, and provide a current result drawing when needed to explain the implemented partition. The review drawing creates no human preview approval or game observation, and it does not replace independent saved-resource checks.

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

A **piece type** is one reusable component in a standalone menu or assembly cycle. A **placement** is a copy used in one assembly. Name reusable types by network, height, movement, and physical profile. Do not put an interchange P-label or a west/east/north/south role in the menu name. Relative left/right handedness is acceptable when it identifies a real functional difference. A generic name does not make a custom curved socket compatible with ordinary track: state its exact connection limits.

Write nominal levels in full in source names, for example `HSR Level 2 above Road Level 0`; this is the safest form for shared picture titles. The shared title helper normalizes `L2`-style shorthand for display, while evidence retains the exact registered name. Keep each nominal level and its measured height together once, and inspect the actual title in every final image. A normalized display title does not rename the registered piece or establish an unmeasured height.

Provide a standalone angled picture and a north-up top picture for every **new or geometrically revised unique type**, not per placement. Both views must show the same complete saved model and use the same canonical orientation and local grid. Preserve the existing current previews of unchanged types; do not regenerate them solely to satisfy this new-view policy. Use the authored **0° orientation**, untranslated compiled geometry except for normalizing its local display grid, and a local southwest tile centre **(X0, Y0)**. Show the source-backed display title, X/Y ticks, the 16 m city grid, scale, and view direction; retain the exact registered menu name in the README and render evidence. Do not show P-labels, trumpet/global coordinates, assembly roles, or assembly-specific rotations in this picture. Every visible caption must be self-contained: only the reusable type display title, local grid, canonical orientation, type/height facts, and software-preview status. Do not mention a trumpet or other interchange, assembly positions or rotations, placement labels, or “see the guide” in titles, subtitles, or footers. These contextual references belong only in the Markdown or JSON placement mapping. Record every visible caption verbatim in render evidence. Keep the software construction reference and the local display-grid reference distinct; a sparse piece can have an empty construction reference cell. Never invent geometry or move a track merely to normalize displayed coordinates.

Store the full angled image as **`00_pieces/<piece-id>/previews/preview.png`**, its thumbnail as **`00_pieces/<piece-id>/previews/preview-thumb.png`**, and the full north-up top image as **`00_pieces/<piece-id>/previews/preview-top.png`**. Keep `piece.json` and `icon.png` at the piece-folder root, with each view's provenance in `evidence/`. A second top-view thumbnail is optional. Show both full views in that type's README. Repeated copies share these images and the same component type in the assembly cycle. The guide needs both a type/image/quantity table and a placement/position/rotation table. State that the standalone image is at 0°; use the rotation column to rebuild the assembly. Record each view's role (angled or top-down), exact input model/DAT hashes, canonical orientation, local display grid, camera, and image hashes in render evidence; retain the angled thumbnail hash as well. Both views must identify the same geometry rather than separate reconstructed models.

Use one shared three-row header for standalone angled pictures, north-up pictures, and connection overviews. The first row always starts with **`Piece - `**, followed by the source-backed display name. The second row starts with the view's purpose, followed by its camera direction and authored orientation. `framework/scp/render_headers.py` owns the title, wording, colours, and font rules; `piece_previews.py` and `connector_overview.py` both use it. The standalone assembly-parts helper delegates to the same renderer. Changing the camera or adding cards must not invent a different piece name or subtitle style. Keep the prefix in the renderer rather than renaming the registered piece.

Apply this caption convention when creating or refreshing artwork. Existing piece images are deliberately retained until their next requested refresh; this documentation change alone does not require regenerating the catalogue.

| Row | Content | Example |
| --- | --- | --- |
| 1, bold dark text | `Piece - ` followed by one source-backed display name, with each nominal level and measured path height in parentheses; retain the exact registered menu name separately in evidence. | `Piece - HSR Paired Quarter-Turn Level 2 (15.5 m) to Level 4 (30.5 m)` |
| 2, blue text | View purpose first: `Clean view` for the standalone model, or `Connection overview` for the model with connection cards; then the actual camera direction and authored orientation. | `Clean view \| Southeast view \| Authored orientation: 0°` |
| 3, grey text | Independent local grid, derived piece reference where applicable, tile size, and meaning of the grid labels. | `Independent local X/Y grid / Piece reference: X0, Y6 / 1 tile = 16 m / Labels mark tile centres` |

Derive the reference position from `local_piece_grid`; do not hardcode a coordinate for a particular footprint. A 45° azimuth in this renderer is the Southeast view, while the north-up top view uses 0° azimuth and 90° elevation. The same display title appears in all three images, and source-backed height details occur once per level. Keep `1 tile = 16 m` in the third row only; suppress the redundant grid footer. Keep the software-preview and unverified-game statements readable elsewhere in the image.

Assembly pictures keep their existing fixed global grid, placement P-labels, exact menu-name callouts, and assembly rotations. Do not restart their X/Y numbering because a standalone type image uses local zero. Do not leave old per-placement type pictures or obsolete types as retired artifacts.

For every new or refreshed render within the requested scope, identify the subject in the first row with `Piece - ` or `Assembly - ` followed by its display name. Begin the second row with its view purpose: `Clean view`, `Component guide`, `Construction view`, or `Connection overview`. Use `Component guide` for named assembly pictures and `Construction view` for the occupied-tile plan. Keep unchanged artwork outside the requested scope. The subject type, purpose, camera, and coordinate reference must agree with the saved render evidence.

## Assembly picture set and in-picture identification

Show the whole actual compiled interchange from above and from at least two opposite oblique angles. An **oblique view** looks down from an angle, so height differences and pillars remain visible. Add a close-up where a join, crossing, or support needs discussion. Label software previews accurately.

Every future user-facing layout or rendered review image, whether top, oblique, whole-interchange, or a standalone type, must carry a readable city-grid reference. Assembly views use the [fixed global coordinate contract](#coordinate-contract-for-charts-and-renders); standalone types use their own [canonical local grid](#reusable-names-and-standalone-type-pictures). A perspective image without a matching coordinate grid is incomplete for a design review.

The first row of every assembly render always reads **`Assembly - `**, followed by the assembly's name. Keep the semantic assembly name unchanged in its source data; the renderer adds the prefix exactly once. Put the view's purpose first on the second row, followed by the actual camera direction. Deliver these three view purposes:

- **Clean view:** one north-up top view and one oblique view without part names, instance IDs, leader lines, or part-name side keys. Keep the coordinate grid, X/Y labels, compass, scale, and view-direction caption. These show the overall shape without the rebuilding annotations.
- **Component guide:** the top and both opposite oblique model views with component names, placement labels, and the side legend. Identify every placed module inside each image using the rules below.
- **Construction view:** the occupied-tile plan with placement positions, ownership colours, and boundaries. Keep the exact component names and placement labels in its side legend.

For example, the trumpet's first row is `Assembly - Straight-stem HSR trumpet`; its second row is `Component guide | Southeast view | looking northwest` in the named southeast picture, or `Construction view | Top view | north up` in the tile plan. The purpose belongs on the second row rather than being appended to the assembly name.

Generate clean and named counterparts from the same compiled models and exact placements. Match their camera directions and suppress annotation layers. Clean views may use the freed side-key space to show the model at a larger scale; record each actual camera and framing in the evidence. Do not move tracks, hide geometry, or change the layout for either version. Present the two clean overviews first in the human guide, followed by the named views and construction plan. Record the annotation mode and image fingerprints separately in render evidence. The minimum set for an assembled interchange is six images: two clean model views, three named model views, and one named construction plan.

In every **named rebuilding/review image**, each placed module must be identifiable inside that image:

1. Show its stable instance label and exact descriptive SCP menu name, for example `P11 — HSR Modular One-Tile Two-Level Crossing`. The common `SCP | [PART HSR]` menu prefix may be explained once in the image key. Do not replace a menu name with a role such as “bridge” or “eastern merge”.
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
| `framework/scp/connector_overview.py`, through `scp.py connectors` | An actual compiled-model connection overview, complete boundary cards, provenance, a resolved export, and the marked piece README section for supported declarations. | A connection overview supplements canonical angled/top previews; it does not create those separate catalogue views. Current connector coverage is the [trumpet’s thirteen reusable types](../domains/high-speed-rail/01_assemblies/straight-stem-trumpet/README.md#2-pieces), the paired rising quarter-turn, and the parallel HSR/Road stack: fifteen types within the larger catalogue. The card renderer requires one measured height per service group. |

The generic catalogue command now produces the complete model's north-up view without requiring an assembly scene or a piece-specific helper. Run from the parent project directory after the editable installation described in [BUILD_AND_INSTALL](BUILD_AND_INSTALL.md#build-a-selected-collection). Replace `EXACT-PIECE-ID`, `BUILD_NAME`, and the texture-directory placeholder with actual values:

```sh
python3 -m scp.preview --catalog --root custom-pieces --output custom-pieces/dist/BUILD_NAME --plugins '/absolute/path/to/Plugins' --include EXACT-PIECE-ID --views angled top
```

Repeat `--include` to select several exact registered types. The supplied verified build must contain every selected type. Under each selected piece folder, the command writes `previews/preview.png`, `previews/preview-thumb.png`, `previews/preview-top.png`, `evidence/preview.json`, and `evidence/preview-top.json`. Each evidence record identifies its own role, actual model and DAT, textures, camera, local grid, captions, generator settings, and output hashes. Both views use the same compiled model. The coverage report states the requested selection and views explicitly; types outside that selection are not a failed or completed migration.

Use `--views top` to add or refresh only the top view; it must leave an existing angled image, thumbnail, and angled evidence untouched. An unchanged repeat reuses each view only when its inputs, evidence, and output image hashes still agree. Missing or altered evidence, top images, or angled thumbnails invalidate the relevant view. A top-only run must not satisfy coverage for a missing angled view. Preserve valid unchanged types' images unless their artwork is deliberately revised.

The existing HSR assembly helper can be used for a type that meets its actual scene restriction. From the parent directory containing `custom-pieces`, the following example writes review outputs into private staging and adds a top view of one type used by the trumpet assembly. Replace the Plugins placeholder with the actual existing texture directory:

```sh
python3 custom-pieces/domains/high-speed-rail/tools/render_hsr_assembly_parts.py --scene custom-pieces/domains/high-speed-rail/01_assemblies/straight-stem-trumpet/assembly.json --build custom-pieces/dist/straight-stem-trumpet --plugins '/path/to/SimCity 4/Plugins' --output-dir custom-pieces/local/documentation-generation/parts --prefix reviewed-part --top-piece-id hsr-component-modular-crossing-core
```

This helper also renders an angled image for every unique type in that scene. It produces `<piece-id>-southeast-local-xy.png`, its `-thumb.png`, selected `<piece-id>-top-local-xy.png` files, and `reviewed-parts-preview-evidence.json`. The report maps staged files to exact types, images, cameras, local grids, source DAT/model hashes, and assembly placements. The `canonical_filename: preview-top.png` field describes the intended basename and role; it does not copy the file into the piece's `previews/` directory. The current helper supplies no automatic command to promote this staged set and its combined report into canonical piece-local top-view evidence. Review that handoff explicitly, preserve the provenance of any deliberately integrated artifact, and do not call the generic catalogue complete on the strength of this staged run.

For the current HSR assembly's six-image set, use its audited scene and matching verified build. This existing example also stages its output without overwriting maintained pictures:

```sh
python3 custom-pieces/domains/high-speed-rail/tools/render_hsr_assembly.py --scene custom-pieces/domains/high-speed-rail/01_assemblies/straight-stem-trumpet/assembly.json --build custom-pieces/dist/straight-stem-trumpet --plugins '/path/to/SimCity 4/Plugins' --output-dir custom-pieces/local/documentation-generation/assembly --prefix reviewed-assembly
```

The helper writes named `reviewed-assembly-{top,southeast,northwest}-xy.png`, clean `reviewed-assembly-{top,southeast}-clean-xy.png`, `reviewed-assembly-placement-plan-xy.png`, and `reviewed-assembly-preview-evidence.json`. Inspect the images and their actual report before updating an assembly's maintained `previews/`, links, and evidence. Use the owning assembly's exact plan, current input build, checked dimensions, and documented command when rendering another accepted layout. A catalogue preview does not replace coordinate-based assembly review.

## Maintain the complete preview catalogue

The generic catalogue renderer reads each selected DAT's actual S3D preview and its referenced FSH texture atlases. Do not substitute a menu icon, a schematic, or an invented illustration for compiled-model evidence. The piece inventory links one canonical image per type, while the assembly inventory links complete-layout pictures. Each reusable type owns its canonical documentation images under its domain's `00_pieces/<piece-id>/previews/`; the [standalone-picture contract](#reusable-names-and-standalone-type-pictures) defines their roles and the separate top-view requirement.

1. Build and verify every new or changed piece first. Use [BUILD_AND_INSTALL](BUILD_AND_INSTALL.md) for the build commands. Keep missing current resources pending.
2. From the parent directory containing `custom-pieces`, render a freshly built all-piece candidate with this exact existing catalogue command. Replace the Plugins placeholder with the actual directory containing the required textures:

   ```sh
   python3 -m scp.preview --catalog --root custom-pieces --output custom-pieces/dist/current --plugins '/path/to/SimCity 4/Plugins' --progress
   ```

   For several current subset candidates, repeat `--output`; the last build supplies a repeated piece ID. Built definitions must match the current registry. Dependencies and editable installation are in [BUILD_AND_INSTALL](BUILD_AND_INSTALL.md#build-a-selected-collection). The default scope is the angled view and thumbnail; add `--views angled top` for both required views of a new or revised type, and repeat `--include EXACT-PIECE-ID` to keep the operation selected.
3. Inspect changed routes, tracks, walls, piers, joins, and shadows. Record human preview approval separately; generating an image does not confirm approval or game operation. Check readability at the actual delivered resolution, not just the provenance fields.
4. Require `coverage.complete` for the requested piece selection and views, with no missing or stale records in that selection. Inspect `selected_piece_ids`, `selected_count`, and `requested_views`; outside-selection pieces do not count as missing in this primary report. The separately labelled `catalogue_coverage` reports all registered types; require its completeness only for a deliberately full-registry audit. The default acceleration/coverage index is private `local/cache/preview-index.json`; it is rebuildable and excluded from exports. Each piece's portable `evidence/preview.json` records the actual model, texture, renderer, and PNG hashes. Reuse requires matching inputs and exact current image hashes; historical build names alone are insufficient. The [framework implementation contract](FRAMEWORK_ENGINEERING.md) owns bounded caches, selected DAT reads, shared texture loading, and pixel equality with the reference renderer.
5. After actual-resource extraction when required, refresh generated connector outputs, then bind review cases to the final images through [the final-artifact procedure](#final-artifacts-and-packaging). A prose-only refresh does not update image-review dependencies or extract resources. Check local Markdown links, then finish and freeze preview writes before tests or packaging copy the source.
6. Package the final documentation and images through the [final-artifact procedure](#final-artifacts-and-packaging), selecting its ordinary-build or assembly-menu branch, then create the current source package. The copied source tree describes the current registry, while the candidate manifest identifies the exact selected subset. Old flat catalogue panels and old build ZIPs are not required inputs.

## Menu artwork and source registration

Every piece keeps its own `icon.png` and registered exact menu name beside `piece.json`. Every registered assembly keeps its own `icon.png` beside `assembly.json`; this strip supplies the assembly's single component-cycle button. Derive identity, network labels, and type vocabulary from the same owning domain source used for menu text and registration, rather than inventing a caption or class from an assembly P-label. Inspect all four native-size menu states. The [framework icon contract](FRAMEWORK_ENGINEERING.md#icon-encoding-and-maintenance) owns the PNG dimensions, frame order, encoding, resource binding, and verification; the [player legend](BUILD_AND_INSTALL.md#recognize-scp-menu-icons) explains the visible vocabulary.

Assembly icons give the layout drawing the available button area without reducing its size to make header or footer bands. Overlay a tiny **SCP** brand at the top left and a small **ASM** followed by the owning domain’s network code at the bottom centre, such as **ASM HSR** for a modular high-speed-rail assembly. Use 3 × 5 pixel footer glyphs on pixel rows 33–37, leaving clearance from the bottom border. Keep the full assembly name and component-placement instructions in the tooltip and guide. Inspect all four menu states at their native 44 × 44 pixel size to ensure that the layout and overlaid labels remain recognizable.

To regenerate only the current HSR assemblies' canonical icons, run this command from the repository root after preparing the dependencies above:

```sh
python3 -B custom-pieces/scp.py assembly-icons --domain high-speed-rail
```

This artwork-only command writes `domains/high-speed-rail/01_assemblies/<assembly-id>/icon.png` under `custom-pieces/` for every registered assembly in that domain. It requires no compiled build or native game inputs, and it changes neither `assembly.json` nor `menu-layout.json`. Assembly-menu preparation reads the canonical strip and checks it against the expected four-state artwork before packaging it. A previous frozen candidate retains its original verification inputs; refresh source artwork before deliberately building a new candidate.

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
| `previews/connection-overview.png` | Fresh compiled-model scene, boundary markers, and complete cards. This image supplements the existing canonical previews. |
| `evidence/connection-overview.json` | Generated provenance: the source evidence and fingerprints tying that overview to its inputs and output image. |
| `README.md` | Piece overview, placement, and intrinsic movement matrix. Its `CONNECTOR OVERVIEW` block is generated; maintained explanations stay outside the markers. |
| `TESTING.md` | Split piece’s test scope, setup, software checks, game checks, results, and design history; legacy combined guides retain those sections in README until deliberately migrated. |

Use the [connector reference](CONNECTOR_METADATA.md#6-stable-identity-reuse-and-file-ownership) for source authority, optional defaults, and schema ownership. This procedure currently covers all [thirteen reusable trumpet types](../domains/high-speed-rail/01_assemblies/straight-stem-trumpet/README.md#2-pieces), plus the paired rising quarter-turn and parallel HSR/Road stack: fifteen types, rather than the whole catalogue. The original crossing and tight-curve [worked examples](CONNECTOR_METADATA.md#8-examples-the-two-existing-hsr-pieces) and [additional authoring examples](CONNECTOR_METADATA.md#86-additional-measured-authoring-examples) retain their narrower illustrative scope.

The source pipeline resolves the declaration and measured records once and uses that complete representation for both export and overview generation. It can pass the resolved records directly to the renderer, so the renderer need not reread a just-written export. Standalone library rendering resolves the same authoring inputs through the shared API. No separate overview-only measurement or manually copied card geometry is introduced.

Keep the export beside `piece.json`, the overview image in `previews/`, and its provenance in `evidence/`, then refresh the existing README block; do not create another per-piece connection or checklist Markdown page. [STRUCTURE.md](../STRUCTURE.md) owns the full file map, and [TESTING.md](TESTING.md) owns manual observations. Consumer applications must read the generated export and keep their reports separately.

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

<a id="refresh-and-check-the-two-migrated-pieces"></a>

### Refresh and check selected migrated pieces

Open a terminal. On macOS, press **Command + Space**, type **Terminal**, and press **Return**. Replace `/path/to/sc4-simons-custom-pieces` below with your checkout's full path, keep the quotation marks, and press **Return** to select its library directory:

```sh
cd '/path/to/sc4-simons-custom-pieces/custom-pieces'
```

The checkout root is the folder containing `custom-pieces/` and the repository README; the final `/custom-pieces` selects the library inside it.

Type `python3 --version` and press **Return**. Python must be version 3.11 or newer. Use the existing project dependencies; the [build instructions](BUILD_AND_INSTALL.md#build-a-selected-collection) explain editable installation, Pillow, and NumPy when preparing a new source checkout.

Select a verified build containing both authoring examples and matching their current measured records. Replace `BUILD_NAME` below with that build directory's actual name. Run this command to verify the selected resources, resolve their authored declarations, write their generated exports, and regenerate their overviews and marked README blocks:

```sh
python3 scp.py connectors refresh --piece blind-hsr-rise-quarter-turn --piece blind-hsr-road-stack --build dist/BUILD_NAME
```

`--piece` selects one exact registered type and can be repeated. `--domain` defaults to `high-speed-rail`. `--build` selects an existing build directory relative to `custom-pieces`, unless an absolute path is supplied; its default is `dist/current`. Refresh does not build that directory. The modular crossing and tight curve can be selected in the same way with their exact IDs and a verified build containing them. Select another build only when its resources match the current measured source records.

Rendering and artwork freshness checks also need the models' existing material textures. Use the configured project texture inputs, or append `--plugins '/absolute/path/to/Plugins'` to select an existing texture directory for refresh or check. Replace that placeholder with the directory's actual path and retain the single quotation marks if the path contains spaces. Texture inputs are read only; no connector command installs or alters Plugins files.

Now run the read-only freshness check with the same selection and build:

```sh
python3 scp.py connectors check --piece blind-hsr-rise-quarter-turn --piece blind-hsr-road-stack --build dist/BUILD_NAME
```

The check validates the source declarations and compiled-resource agreement, compares the saved export with the freshly resolved result, and checks the canonical overview's recorded input and output fingerprints, current material textures, fonts, and renderer settings. Missing or stale outputs are failures, rather than a request to silently rewrite them. Read the command's JSON result and resolve any reported input or provenance mismatch before using the outputs.

To refresh only machine-readable exports, add `--no-render` to `connectors refresh`. Add `--no-render` to `connectors check` only when deliberately checking that machine-readable scope without artwork. A successful check in that scope does not establish overview freshness. Ordinary authoring completion includes the image, its evidence, and the generated README block.

### Reading an overview

The overview shows one clean scene rendered directly from the selected compiled model and its textures at the piece's authored 0° orientation. It does not paste a previously captioned preview into a new frame or reconstruct track geometry from metadata. The existing `previews/preview.png`, `previews/preview-top.png` where present, and their evidence retain their separate roles.

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

New or intentionally refreshed reusable pieces and assemblies use README plus TESTING. Legacy combined piece guides remain intact until explicitly migrated; a general generated-view refresh does not opt them into a different layout. Keep a player guide and network specification per domain, with separate generated piece and assembly inventories. Preserve authored prose outside generated markers and update the generator when changing its output structure. Do not add separate per-subject connections, checklist, or recording-help Markdown files. Preserve all actual connection/observation data and current images when consolidating prose; check files, heading links, and regeneration.

### Piece README

Keep a piece’s useful function, exact identifier and menu name, network services, footprint, supported rotations, intended interface families, and required adapters in README. Put detailed limitations, test evidence, and history in TESTING for a split guide. Show canonical angled and top views for new or geometrically revised types under the [standalone contract](#reusable-names-and-standalone-type-pictures), preserve unchanged types’ current previews, and include the generated connection overview for intentionally migrated types. Reference the exact measured connection and manual records instead of hand-copying their coordinates or checkbox state into maintained prose. Generated intrinsic connection tables do not publish legacy neighbour shortlists or a mandatory port/counterpart manual matrix. Automatic complete-boundary compatibility discovery is not supplied by the current library; any future consumer must exclude incomplete or stale inputs explicitly.

New piece guides and intentionally refreshed subjects use a three-chapter README with a separate TESTING document. A **movement matrix** is a table whose rows are directed entrances and whose columns are directed exits within this one piece. It is generated from measured routes and scoped observations; it does not list possible neighbouring pieces. Use the [paired climb README](../domains/high-speed-rail/00_pieces/hsr-component-modular-paired-climb/README.md) and [TESTING document](../domains/high-speed-rail/00_pieces/hsr-component-modular-paired-climb/TESTING.md), or the [two-level crossing README](../domains/high-speed-rail/00_pieces/hsr-component-modular-crossing-core/README.md) and [TESTING document](../domains/high-speed-rail/00_pieces/hsr-component-modular-crossing-core/TESTING.md), as current split-layout examples. The [paired rising quarter-turn](../domains/high-speed-rail/00_pieces/blind-hsr-rise-quarter-turn/README.md) and [HSR above parallel Road](../domains/high-speed-rail/00_pieces/blind-hsr-road-stack/README.md) retain their older version-1 combined layouts until explicitly refreshed; they remain useful geometry and connector examples.

| README chapter and navigation label | Content and source |
| --- | --- |
| `1. Views` | Canonical angled and north-up images, local grid, and software-preview limits. Keep generated `PIECE VIEWS` images here. |
| `2. Piece and placement` | Exact menu name and permanent ID, function, services, occupied cells and construction rectangle, rotations, approach requirements, and numbered placement instructions. Keep generated `PIECE OVERVIEW` facts here. |
| `3. Connection matrix` | Generated `PIECE CONNECTION MATRIX` with intrinsic entrance-to-exit movements, followed by the generated `CONNECTOR OVERVIEW` image and selectable card details for migrated types. |
| `Testing ↗ (separate document)` | Use exactly `[Testing ↗ (separate document)](TESTING.md)`, matching the assembly label while opening this piece’s own testing document, outside the three numbered README chapters. Detailed evidence and checks belong in that document. |

Use the three second-level headings once each, and use third-level headings for material inside them. Add `<!-- PIECE README LAYOUT: 2 -->` beneath the title and outside generated blocks. The navigation links are `#1-views`, `#2-piece-and-placement`, and `#3-connection-matrix`, followed by exactly `[Testing ↗ (separate document)](TESTING.md)`; the relative target opens this piece’s own TESTING document. The companion document uses `<!-- PIECE TESTING LAYOUT: 1 -->` and the [six-chapter layout below](#required-piece-and-assembly-testing-layout). A missing new piece guide receives this split scaffold; fill the subject-specific prose rather than treating generated placeholders as instructions or evidence.

A deliberate migration moves authored testing prose and generated `CONNECTIONS`, `MANUAL SUMMARY`, and `MANUAL CHECKS` blocks into TESTING without changing their authoritative records. Keep `CONNECTIONS` in chapter 1 and both manual blocks in chapter 5. Update maintained links to exact cases as `TESTING.md#case-…` and retain useful historical anchors where required; frozen evidence remains unchanged. Preserve game IDs, geometry, measured connection bytes, exact case identities, original observations, failed or stale results, and each observation’s dependency fingerprints. The split is a documentation change and supplies no test result.

Existing unmarked guides and `<!-- PIECE README LAYOUT: 1 -->` combined guides retain their layout and in-README checks until explicitly migrated. Ordinary generation and observation recording must preserve their authored content and current links. Do not add a separate connection page, checklist page, test-plan helper, or recording-help page alongside the canonical README/TESTING pair.

Read the matrix from an entrance row to an exit column. Keep **Saved PATH**, meaning checks of the saved traffic routes, **Route Query**, meaning the route displayed by the game, and **Visible travel**, meaning an observed vehicle or pedestrian completing that journey, separate. Show **Game appearance** once above the matrix. In a split guide, each result links to its exact test-case anchor in TESTING; a retained combined guide keeps its existing README anchors. Display ✅ only when every required current case in the declared scope passes, ❌ when a required current case fails, and ? for missing, stale, or otherwise unestablished coverage. A software pass cannot approve either human travel check. A recorded combined journey observation remains historical when separate Route Query and Visible travel cases are introduced; do not copy its approval into either new case.

Mark a pair **Forbidden** only when authoritative `forbidden_transfers` declares it. Keep its software result and focused in-game negative check separate. An unlisted entrance/exit pair remains unknown rather than acquiring an invented permission or prohibition. Service, role, direction, and declared orientation belong to the case scope; a matching display label alone cannot approve a movement. Preserve observations and their original fingerprints when refreshing this view.

The connection overview’s image and selectable Markdown details come from the same complete resolved records used for `connector-data.json`. Keep those generated details in the existing `CONNECTOR OVERVIEW` block in README so full IDs, numerical fields, permissions, and source references remain readable and copyable without extracting text from a PNG. Maintain shape-specific explanations and unresolved limitations outside generated markers, with detailed test evidence in TESTING. Do not copy the shared metadata format or generation procedure into each subject guide.

### Required Markdown guide for each modular interchange

Create `domains/<domain>/01_assemblies/<assembly-id>/`, using the [straight-stem trumpet guide](../domains/high-speed-rail/01_assemblies/straight-stem-trumpet/README.md) as the example. Register `assembly.json` in that domain's `domain.json` and link the blueprint from its human overview. Keep exactly two Markdown files: `README.md` for the player overview (pictures, pieces, placements, and the connection matrix), and `TESTING.md` for detailed preparation, coordinate definitions, software evidence, technical limitations, design history, and generated human checks. The current trumpet overview uses exactly **1. Views**, **2. Pieces**, **3. Placements**, and **4. Connection matrix** as both section titles and navigation labels; its Testing navigation explicitly opens a separate document. Use the [six-chapter TESTING layout](#required-assembly-testing-layout) for every new assembly. Shared observation-recording instructions live once in [framework TESTING](TESTING.md); link them and include the subject-specific command instead of repeating the procedure. Keep `icon.png` beside `assembly.json`, layout pictures in `previews/`, authoritative manual observations in `checks/`, and durable software/render reports in `evidence/`. The generated assembly inventory links one clean preview to this guide. Across these two files include:

1. **What is built:** the intended networks, levels, dimensions, required movements, and terrain assumptions; an explicit modular-blueprint label and instructions for its one assembly button: Tab cycles forward, Shift+Tab cycles backward, and each click places one component. Every assembly follows this menu pattern; [prepare its final assembly menu](BUILD_AND_INSTALL.md#prepare-the-assembly-menu) after compiling the reusable parts.
2. **Six current pictures:** a clean top and clean oblique model view, a named top view, two named opposite oblique views, and a named occupied-tile plan. All follow the same southwest `(X0, Y0)` tile-centre grid, with no global origin annotation. Named pictures contain exact menu names, stable instance IDs, and leader lines; clean pictures retain coordinates while omitting those part annotations.
3. **Coordinate instructions in TESTING.md:** X increases east/right and Y north/up on the north-up plan; give the 16 m tile size and full nonnegative X/Y ranges. Use the shared southwest-zero convention without an in-picture origin annotation. Keep display and technical authoring coordinates explicitly separate.
4. **Parts and placements:** exact menu names and permanent piece IDs; quantity per type; one instance ID per placement (`P01`, `P02`, etc.); each instance's displayed construction reference position, rotation and connection heights. Explain empty reference cells and unverified cursor anchors; picture callouts use **Position X7, Y13**, not **Origin**.
5. **Preparation in TESTING.md:** numbered selection and placement steps, supported rotation controls, exact matching connections and approach requirements. Explain why overlapping tile ownership is forbidden. Cover all permitted journeys and forbidden transfers, not just the visible track shape.
6. **Evidence and limits in TESTING.md:** the machine-readable placement-plan link, exact build/source fingerprints, compiled-piece and complete-assembly checks, render evidence, and rotation checks. State which game behaviours remain unverified; software renders and installation hashes are not game tests.

Update the guide, machine-readable plan, picture names/IDs, placement tables, and evidence together after every accepted layout revision. An assembly chart or parts list alone is insufficient rebuilding documentation.

When changing a picture's coordinate-label format, use a new descriptive image filename and refresh every current guide link and evidence record. A reused image path can show cached older artwork in an already open guide. Validate the newly linked image itself, then remove the superseded source preview file; do not retain an obsolete alternative picture.

<a id="required-assembly-testing-layout"></a>
<a id="required-piece-testing-layout"></a>

### Required piece and assembly TESTING layout

Every new or intentionally refreshed piece’s TESTING document and every new assembly’s TESTING document use the following six level-two Markdown headings, in this exact order. A **level-two heading** starts with `##`; use the complete numbered name for its top navigation link too. Add descriptive level-three (`###`) or level-four (`####`) subsections as needed inside a chapter. Keep all six chapters, even when one contains only a short statement explaining that no information is available yet. The [paired climb TESTING document](../domains/high-speed-rail/00_pieces/hsr-component-modular-paired-climb/TESTING.md) demonstrates an individual piece; the [trumpet TESTING document](../domains/high-speed-rail/01_assemblies/straight-stem-trumpet/TESTING.md) demonstrates an assembly. Their dimensions, interfaces, exceptions, and historical results belong to those subjects.

| Chapter title | Content |
| --- | --- |
| **1. Test scope** | Participating services, entrance/exit roles, permitted directions, forbidden movements, meanings of the checks, and the exact required manual orientations. Keep generated technical connections and journeys in the `CONNECTIONS` block here. |
| **2. Test setup** | Required build and dependencies, recorded game environment, disposable test city, coordinate reference, menu and component selection, outside connections, and travel demand. For a piece, link the README’s placement instructions; for an assembly, link its pieces and placement tables rather than duplicating them. |
| **3. Software checks** | Actual commands, acceptance contracts, verified inputs and reports, coverage, technical exceptions, limitations, and artwork provenance. Distinguish executable checks from historical reports and explicitly skipped checks. |
| **4. Game checks** | Actions to check selection, placement, appearance, Route Query, visible travel, forbidden movements, shadows, demolition, and save/reload where applicable; assemblies also check their component cycle. Identify the direction, service, layout, and environment for each observation, and link the shared recording procedure. |
| **5. Results and known issues** | Known defects and their exact evidence/scope, followed by current states, case details, original observations, and applicable stale or historical results in `MANUAL CHECKS`. A split piece also keeps `MANUAL SUMMARY` here. A defect in another recorded build does not automatically become a failure of a current case. |
| **6. Design history** | Earlier decisions, measurements, migration notes, and change rationale, clearly separated from current acceptance criteria and current results. Retain original identities, input hashes, and observation scope in historical evidence. |

The content generator owns the initial scaffold. A split piece’s README uses `<!-- PIECE README LAYOUT: 2 -->`, and its TESTING document uses `<!-- PIECE TESTING LAYOUT: 1 -->` beneath the title. An assembly’s TESTING document retains `<!-- ASSEMBLY TESTING LAYOUT: 1 -->`. Split-piece scaffolds place `CONNECTIONS` in chapter 1 and `MANUAL SUMMARY` plus `MANUAL CHECKS` in chapter 5; assembly scaffolds retain their existing `CONNECTIONS` and `MANUAL CHECKS` positions. Fill the subject-specific setup, commands, limits, and issues outside generated markers. Do not copy an unrelated subject’s values or claim checks were performed merely because the scaffold exists. Existing legacy documents are preserved until deliberately migrated by moving their authored sections and retaining their evidence links.

In a marked six-chapter document, generated blocks use level-three headings, with their internal subsections one level deeper. Their titles remain `Connections and journeys`, `Manual status` where present, and `Test checklist`, preserving the corresponding heading anchors inside that document. A split-piece README matrix links exact `#case-…` anchors in TESTING. Renaming or relocating an existing heading requires updating its maintained links or retaining a unique explicit HTML anchor for its previous location. Ordinary refreshes and observation recording must preserve the six numbered chapters, their navigation, authored content, and authoritative observation bytes except for the explicitly recorded observation. Piece READMEs retain their three-chapter split layout or their deliberately retained legacy layout.

This layout applies to pieces and assemblies with one service or several services. Identify each service, entrance/exit role, and direction separately even when services share a game traffic class or physical approach. Use **visible travel** as the general check name; an HSR subject can say **visible train travel**. State which orientations the human test plan actually requires; do not add four manual whole-assembly runs solely because software supports four construction rotations.

### Refresh generated Markdown and inventories

A **generated block** is a section bounded by named HTML comments, such as `<!-- BEGIN PIECE OVERVIEW -->` and `<!-- END PIECE OVERVIEW -->`. Edit its source data or its owning generator, rather than editing text that the next run will replace. Keep authored prose and valid existing metadata headers outside these blocks; preserve frontmatter on repeated refreshes. Follow [STRUCTURE.md](../STRUCTURE.md#markdown-metadata) for the four-field document metadata convention and its existing subject exceptions. Write each prose paragraph on one physical source line, with blank lines between paragraphs.

`scp.content` owns `PIECE VIEWS`, `PIECE OVERVIEW`, `PIECE CONNECTION MATRIX`, `CONNECTIONS`, `MANUAL SUMMARY`, `ASSEMBLY CONNECTION MATRIX`, and `MANUAL CHECKS` views; connector refresh owns `CONNECTOR OVERVIEW`; inventory generation owns domain `COLLECTIONS` navigation and the illustrated inventories. Keep the connector block outside other generated markers. The piece movement matrix is enabled by its explicit marker; do not add it to every unchanged historical guide during a general refresh. Assembly checks and split-piece checks belong in TESTING; legacy combined piece guides keep their existing README checks until deliberately migrated. Split-piece README matrices link exact cases in TESTING, while their manual summary and detailed checklist live in TESTING chapter 5. The opted-in assembly matrix gives compact ✅, ❌, or ? statuses in README and links exact cases in TESTING; technical connections and case details stay in TESTING. The assembly inventory's **Connection matrix summary** uses the same status evaluator and counts displayed entries separately for Saved PATH, Route Query, visible travel, and forbidden movements in game; it does not combine them into an independent-test total. Preview review and game appearance read their named cases from `checks/manual-tests.json`, as explained in [TESTING](TESTING.md#understand-the-displayed-results); generated Markdown is a view of those records. Game appearance appears once above each directed entrance/exit matrix. Source definitions, placements, measured connections, source-port identities, class records, and human observations remain authoritative JSON, not Markdown checkboxes.

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

Use this sequence after the implementation, schemas, registry, and required compiled resources have stopped changing. A later source addition or real resource change requires the affected validation and connector refresh again. An ordinary verified piece build can receive newer documentation in its ZIP without rebuilding resources. An assembly-menu candidate freezes its source proof, so finalize its documentation before a fresh normal source build and a fresh final assembly-menu candidate.

1. Verify the actual compiled resources and extract changed route measurements through the owning domain. Select the intended build and subjects. For unchanged resources, preserve the existing measured records.
2. Generate the required standalone angled and top images through the generic command above, then run `connectors refresh` and `connectors check` for migrated types. Inspect the actual PNGs for clipping, complete geometry, consistent headers, and readable connection groups.
3. Bind manual review cases to the final actual images. From the parent directory containing `custom-pieces`, replace the placeholder with the selected type's identifier:

```sh
python3 custom-pieces/scp.py observations refresh-images --piece EXACT-PIECE-ID
python3 custom-pieces/scp.py inventory
```

Repeat `--piece`, select an assembly with `--assembly EXACT-ASSEMBLY-ID`, or deliberately use `--all`. This operation updates only image-review cases for the selected subjects, including separate angled, top, and connector-overview images where present. It records exact PNG fingerprints, preserves all non-image cases and original observations, and never marks an image approved. A changed image makes its earlier approval stale; it does not inherit an approval from a different view. Missing final images remain missing rather than receiving an invented pass. Run inventory afterward because those summaries are a separate view refresh.

4. Finish scoped software checks and run `python3 -B custom-pieces/scp.py docs-check` from the repository root for the read-only catalogue and shared-guide layout, required-file, and local-link checks. Repeated `--piece EXACT-ID` or `--assembly EXACT-ID` selectors check a subject selection; run the unselected command before handing over changes to shared guides. Report retained legacy coverage and real software skips accurately. A passing draft scaffold still needs its authored instructions and actual implementation evidence. Freeze image and documentation writes, then select the applicable packaging branch below.

For an **ordinary verified piece build**, replace `BUILD_NAME` with its existing build directory, and run:

```sh
python3 custom-pieces/scp.py package --output custom-pieces/dist/BUILD_NAME --destination custom-pieces/dist/BUILD_NAME-current-docs.zip --refresh-docs
```

This command verifies the ordinary build, copies its exact compiled payloads, and places current portable documentation plus matching document hashes in the ZIP. It changes no files in the input build. The ZIP's manifest records the delivered documentation, while the source build's original documentation snapshot remains intact.

For an **assembly-menu candidate**, follow [Prepare the assembly menu](BUILD_AND_INSTALL.md#prepare-the-assembly-menu) after finalizing the source documentation. Its commands compile a fresh normal source build, create a fresh final assembly-menu candidate in an unused output directory, verify it, and package it without `--refresh-docs`. That option is rejected because the candidate's source documents are frozen verification proof. Preserve an earlier candidate unchanged and label it as historical when its documentation is superseded; changing its label does not deliver the new documentation.

5. After completing the applicable binary-packaging branch, export the current portable sources:

```sh
python3 custom-pieces/scp.py source-package --destination custom-pieces/dist/current-source.zip
```

The source command excludes compiled DATs, private settings, caches, and workstation textures. Binary packaging and source packaging create local archives; neither installs or publishes anything.

Connector exports and new overview evidence bind a canonical fingerprint of the compiled manifest's resource facts, independently of the documentation list and publication/installation state. Exact DAT hashes, selected definitions, dependencies, construction overlays, and all other build facts remain checked. Consequently, packaging final documentation does not create the old cycle in which updating document hashes invalidated the very connector export being packaged. Legacy overview evidence without this stable field retains its stricter raw-manifest check until deliberately refreshed.

Without `--refresh-docs`, `package` deliberately retains the build-time documentation snapshot. This is required for assembly-menu candidates. For ordinary piece builds, use it to reproduce an earlier artifact, and label a superseded snapshot as historical; use `--refresh-docs` for current documentation. Preserve skipped or unavailable game checks as unverified, and inspect the archive's final manifest and README rather than assuming a successful ZIP operation supplied manual evidence.

## Freshness and evidence


Generate only after integrated source checks pass and concurrent geometry edits have finished. A repeat run with identical inputs must preserve the resolved meaning, stable markers, and reproducible output. Provenance records identify the actual declarations, profiles where used, measured connections, saved model and texture inputs, generator, and output image. A matching filename or an old build name is not proof of matching input bytes.

Overview generation establishes a software view of the validated inputs. Compiled PATH agreement is a separate source check; a single-piece overview does not test a two-piece placement's owned-cell fit. Physical seams, full model interference, construction clearance, terrain behavior, and game operation remain separate evidence states. Unknown or unperformed checks remain unverified.

Manual observations remain solely in `checks/manual-tests.json`. Connector refresh does not rewrite that record, raw `connections.json`, geometry, or assembly placements. After an actual source change, the upstream extraction workflow preserves observations and their original dependencies, marks affected results stale, and never turns software success into a human pass. Follow [TESTING.md](TESTING.md) when recording an explicit observation.

Before packaging, check local links, selected-piece coverage, generated-data freshness, overview provenance, and the source export's included declarations, schemas, images, and evidence. Keep workstation inputs, private caches, and previous build output excluded. Building, installing, packaging, and publishing remain separate actions.

A portable source package excludes compiled DAT archives and workstation texture inputs. The shared `scp.connector_metadata.load_library(...)` API can validate the authored declaration structure and measured-source references without those game assets. Refresh and the full `connectors check` require an existing local compiled build to re-extract and verify its actual routes; fresh rendering and artwork freshness checks additionally require the referenced textures. Included generated records and artwork retain their provenance, but do not supply missing game assets or make an absent compiled-source check pass.

Before final delivery, compare the current source/placement selection against the generated artifacts, check every local file and heading link, inspect each changed image for legibility and clipping, and confirm that image roles, captions, cameras, grids, and hashes agree with their evidence. A repeat refresh must preserve authored prose, valid frontmatter, source records, stable identities, observations, and generated meaning.
