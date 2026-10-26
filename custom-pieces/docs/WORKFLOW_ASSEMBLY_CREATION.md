---
title: "WORKFLOW: Assembly Creation"
summary: "Apply the piece-versus-assembly decision, design and verify a modular layout, reuse or author useful pieces, review the compiled assembly, and document its reconstruction."
audience: "Assembly designers and piece authors"
document_type: "procedure"
---

# WORKFLOW: Assembly Creation

Use this process for Simon's Custom Pieces interchanges. It records the method developed with the modular HSR trumpet: agree on the routes and shape, prove the reusable parts, assemble the actual game models, review them with coordinates, then remove unnecessary size.

Read the selected transport domain's short `AGENTS.md` router and human `README.md`, then its network specification for actual connection rules; the [HSR network specification](../domains/high-speed-rail/NETWORK_SPEC.md) is the existing example. Shared operational contracts are in the framework's `docs/FRAMEWORK_ENGINEERING.md` and `docs/BUILD_AND_INSTALL.md`. Network heights and domain-specific geometry/routing criteria belong in the owning domain; shared [render-group budgets](FRAMEWORK_ENGINEERING.md#model-and-render-preservation) belong in framework engineering. Future highway work must use its own domain facts.

## Terms and evidence

- A **movement** is one permitted journey, such as south to west. The reverse journey is a separate movement. A full three-arm T has six movements.
- A **port** is a measured traffic-route endpoint. The [connector reference](CONNECTOR_METADATA.md) defines how complete shared boundaries, permissions, and placement are compared; physical fit requires its own geometry checks.
- A **module** is a functional piece with its own selectable SCP button.
- A **blueprint** is an exact arrangement of several modules. Building it requires several placements, even when the finished layout is ready-made.
- A **one-click interchange** is one selectable piece that constructs the complete junction. It needs its own construction and address checks.
- A **DAT** is the game's resource archive. **PATH** resources describe traffic routes; **S3D** resources contain the visible model; **FSH** resources contain artwork, including textures and shadows.

**Current delivery policy: new complete complex interchanges are modular blueprints, assembled from individually selectable pieces.** Do not promise one-click PNP placement for them with the current construction system. Each interchange needs its own Markdown rebuilding guide and the image and placement information listed below. Every functional module must remain individually available.

Apply the mandatory [piece-versus-assembly decision](WORKFLOW_PIECE_CREATION.md#0-decide-between-a-piece-and-an-assembly) before allocating types or producing detailed geometry, including requests phrased as a single “piece.” When the design belongs here, announce that delivery is an assembly and that the complete junction will not be provided as one selectable piece. Record the reusable functions and granularity rationale in the existing assembly README, then prove the modules through steps 3–5. A large diagonal X with central and branching regions is an assembly-design task; neither successful one-piece compilation nor internal mesh chunking proves a reusable-parts design. Preserve existing accepted types and treat the current trial's single-piece model as feasibility evidence, rather than claiming that a modular replacement already exists.

The current straight-stem trumpet cannot be one ordinary construction piece: its 109 occupied tiles map to only 95 unique runtime lookup keys, causing 14 tile-address collisions. A **collision** means that two tiles ask the engine for the same lookup entry and one selects the other tile's model and paths. Combining meshes or choosing new resource identifiers does not repair that. The current Plop & Paint tool also cannot stamp a network-piece blueprint. These are measured limits of the current layout and tools, not a claim that every possible one-click junction is impossible.

Preserve the two existing accepted smooth full T pieces and their PNP buttons. A new complete one-click construction is a separate future project, reopened only at the user's request with a newly proved construction or placement mechanism and independent checks. It is not an automatic target of this workflow. A rendered assembly alone does not establish that a button exists.

Keep these evidence states separate:

| State | What has actually been established |
| --- | --- |
| Layout agreed | The user accepts the intended routes and overall shape. |
| Pieces checked | The individual compiled pieces pass their independent file checks. |
| Assembly checked | The complete arrangement passes route, geometry, and construction checks. |
| Installed | The installed files match the verified build. |
| Game-tested | The exact installed version has passed recorded tests inside SimCity 4. |

Use “working in SimCity 4” only for the last state. A plausible chart, an attractive render, and a successful installation provide different evidence.

## 1. Establish the brief and draw a rough layout in chat

Write a short brief before creating detailed geometry:

1. Name the network on each arm: for example, HSR west/east/south.
2. List the intended movements and their train directions. For a full T: `W→E`, `W→S`, `E→W`, `E→S`, `S→W`, and `S→E`; exclude U-turns unless requested.
3. State which crossings must be separated vertically. Identify intended merges and splits, where routes are allowed to meet at the same height.
4. Record the external connection heights, track widths, and native network ends. Name any intermediate custom height explicitly.
5. Record the desired footprint, straight/diagonal orientation, symmetry, terrain assumptions, and modular placement method. Distinguish requirements from preferences and unresolved questions. Plan a dedicated rebuilding guide rather than an unimplemented complete-interchange button.

Then present an editable in-chat chart using the available visualization tools. Show north, the city grid, labelled arms, direction arrows, a consistent colour per movement, and height labels wherever lines cross or change level. Include a legend and an explicit **schematic** label. Until dimensions are checked, state that sizes and radii are provisional.

The chart should make the transport logic obvious before models, textures, pillars, or menu resources are built. Investigate an uncertain crossing or connection with a small feasibility sketch rather than expanding the whole family immediately.

**Output:** a short brief, a movement list, and the current schematic shown directly in chat.

## 2. Iterate until the shape matches the user's intent

Use the user's comments to revise the chart. Resolve the arrangement of loops, branches, crossing order, direction of travel, and symmetry first. For example, “make the east-to-south curve follow the south-to-west loop before separating” changes the route layout and must be visible in the chart.

Keep the movement colours, arm names, and coordinate origin stable between iterations. Explain what changed and why. If a requested shape conflicts with a height transition or matching track end, show the specific conflict and a small alternative.

Once the intended shape is clear, carry out routine implementation decisions without repeatedly asking for confirmation. Return to this layout discussion when feasibility requires a material change to the agreed shape or movements.

**Output:** the agreed current layout, with any remaining assumptions marked.

## 3. Check existing pieces and prove the connection plan

Inspect `project.json`, the domain inventory, current manifests, and verified builds. Similar names or appearances do not prove that two pieces connect.

Create a parts table with one row per required functional module:

| Module label | Purpose | Existing exact piece ID | Port/placement compatibility | Action |
| --- | --- | --- | --- | --- |
| P01 | Mainline crossing | Exact current ID, if available | Checked / unverified, with the reason | Reuse, test, adapt, or build |
| P02 | Curved height change | None, if missing | Required entry/exit heights and headings | Build a separate module |

For each connection, check the exact three-dimensional endpoint, heading along the track, permitted train direction, track spacing, visible profile, and construction-grid alignment. Write these expected connections independently of the generator. Keep visual fit and traffic-path compatibility separate.

Also assign every occupied city tile to exactly one module. Upper and lower tracks sharing a tile generally need a coordinated module containing both routes; independently placing another piece there can overwrite the first. Check sparse footprints, empty construction-origin cells, rotations, and the runtime tile-address rules before relying on an apparent fit.

Check runtime addressing for each independently placed module. Keep the complete arrangement as a blueprint; a safe component allocation does not imply that merging all components into one construction is safe.

**Output:** a parts list, expected ports and movement connections, tile owners, and an explicit list of missing or unproven parts.

## 4. Build and test the smallest missing reusable parts

Implement only the missing modules needed for the agreed design. Start with the smallest useful crossing, split, merge, adapter, or curved ramp that tests an uncertain connection.

Each new functional module needs:

1. Its own current manifest, unique identifiers, descriptive SCP menu name, and icon, so the user can place it independently.
2. Explicit traffic paths, visible geometry, occupied cells, construction rules, matching ports, supports, and shadow resources.
3. Independent checks of the saved DAT contents. Inspect actual encoded PATH samples, S3D geometry, and construction rules, not just values supplied by the generator.
4. Checks for permitted and forbidden movements, correct split/merge flags, all four proper 90-degree rotations, native connection profiles, curve and slope limits, train clearance, open joins, support contacts and spacing, and all five model/shadow zooms.
5. Its own canonical artwork, connection overview, manual records, and inventory row under the shared [documentation-generation workflow](WORKFLOW_DOCUMENTATION_GENERATION.md), including both angled and north-up views for a new or geometrically revised type.

Use the existing piece-authoring guide for the commands and allocation rules. Test a small changed selection first. Reuse already verified results only when every relevant specification and binary input is identical.

**Rotation is required for every independently placeable module:** check 0°, 90°, 180°, and 270° for its emitted construction rules, occupied cells, actual model, PATH entry/exit directions, ports, preview, and shadows. A **proper rotation** turns a piece without reflecting it. Do not mirror a one-way route to create extra states; repeat the four rotations if the menu needs eight states. A diagonal variant is a separately authored 45-degree layout with native diagonal ports, not an extra 45-degree rotation of a straight piece. Record file-check evidence separately from all-four-rotation placement and traffic tests in the game.

Useful wider variants remain separate current pieces. Add a clearly named compact variant when its geometry is different; do not silently change an existing useful piece or retain rejected prototype versions as compatibility artifacts.

**Output:** independently selectable, compiled, and checked missing modules.

## 5. Assemble actual compiled pieces and check the whole interchange

Make a machine-readable placement plan. Record a stable module label such as `P01`, its exact piece ID and descriptive SCP menu name, translation, rotation, occupied cells, and source DAT fingerprint. Give repeated copies separate instance labels: four copies of one straight are `P05`, `P06`, `P07`, and `P08`, even though their menu name and piece ID match. Preserve those labels through all views and revisions. A fingerprint is a hash identifying the exact file bytes.

Assemble the saved component models using rotations and translations only. Do not reshape track ends, hide clipping, delete pillars, or repair walls only inside the preview. A repair belongs in an independently placeable module.

Check the complete arrangement:

- Every required directed journey exists; unwanted U-turns, transfers between levels, reverse travel, and unintended same-height crossings are absent.
- Every seam matches in position, height, direction, and profile. The actual train corridor remains clear across the join.
- Occupied construction cells do not overwrite another module's routes.
- Pillars meet their decks and satisfy spacing across module boundaries. Two pieces that pass separately can still introduce duplicate or obstructing pillars when placed next to each other.
- Crossings have sufficient clearance in the visible model, including walls and deck thickness, rather than only different PATH heights.
- Rotations, tile addresses, previews, render-group budgets, and all zoom resources remain valid in the final arrangement.

If a module is missing or wrong, return to **step 4**, then rebuild and recheck the affected assembly. If the agreed route arrangement itself is infeasible, return to **step 2** with a concrete explanation.

**Output:** a reproducible assembly and a whole-interchange validation report.

## 6. Review coordinate-labelled renders with the user

Generate the accepted layout's actual compiled-model pictures using [WORKFLOW: Documentation Generation](WORKFLOW_DOCUMENTATION_GENERATION.md#assembly-picture-set-and-in-picture-identification). Apply its fixed [coordinate contract](WORKFLOW_DOCUMENTATION_GENERATION.md#coordinate-contract-for-charts-and-renders), six-image clean/named set, exact menu-name callouts, and ownership colours. Use the current machine-readable placement plan and verified builds; check the documented renderer scope before running a command. Add a close-up where a join, crossing, or support needs discussion.

Review the shape, symmetry, route clarity, joins, supports, and space use with the user on that same fixed grid. Geometry feedback returns to **step 4**; layout feedback returns to **step 2**. Do not change approved geometry solely to improve a camera view. Keep software preview approval separate from game-test evidence.

**Output:** the complete current coordinate-labelled review set and the user's feedback, with image roles, placements, and input fingerprints recorded under the shared generation contract.

## 7. Compact the agreed interchange, then recheck it

Consider available space from the first sketch. Perform a deliberate compaction pass after the complete arrangement is understandable and reviewed.

1. Remove straight approach padding that serves no connection or height transition. Check the west, east, and south arms and the loop's own straights.
2. Move compatible splits and merges closer to the main crossing where clearances and tile ownership permit it.
3. Shorten loop sides and its top straight, and reduce curve size where the approved curvature and slope limits still pass. A curve may also change height if an independently tested module supports that combination.
4. Preserve matching end segments, safe train clearances, support spacing, and required climb length. Do not weaken existing limits to make a smaller footprint pass. Record why any remaining straight length is necessary.
5. Build additional compact modules as needed, returning to **step 4**. Run the affected piece checks and the whole-assembly checks again. Present the result on the same coordinate grid for review.

Compare the width and depth of the enclosing construction rectangle, occupied tile count, route lengths, and relevant curve/slope measurements. The rectangle includes empty space; its area is not the number of occupied tiles. Describe the achieved reduction rather than claiming a mathematically minimum design.

**Output:** the current compact layout, verified measurements, and updated coordinate-labelled review images.

## 8. Package, install when requested, and test inside the game

Freeze the accepted current design. Deliver the movement list, exact module selection and names, coordinate plan, placement order and rotations, required heights, previews, and verification results. Keep current docs and packages in sync; remove rejected or superseded prototype artifacts without deleting useful current alternative components.

Build the complete intended installed selection with **one shared controller and one menu**. Preserve existing installed pieces. Independent subset builds must not be stacked as if their controller files could all remain active. Record the exact final file hashes and compare installed files with the build. An installation request authorizes installation; creating a preview alone does not install a new collection.

Package the individually placeable components and the complete rebuilding guide. Do not add an unproved whole-interchange menu entry, mark a component selection as PNP, or present the blueprint as a stamp supported by Plop & Paint. The current whole-trumpet address collisions remain even if its components are packaged together. A future one-click research project must satisfy the policy in **Terms and evidence** before it can change this delivery method.

To establish game operation, use a disposable flat city and the exact installed version. Test placement and every intended movement with real traffic demand, the game's route query, and moving trains. Also test forbidden transfers at same-network crossings and parallel edges at different heights. Check all supported rotations and zooms, shadows, joins, demolition, save/reload, and the claimed terrain behaviour. Record the game/platform, file hashes, city layout, observations, and screenshots. Return defects to the appropriate earlier step.

Keep untested behaviours explicitly unverified. Public distribution has additional requirements documented separately in `docs/RELEASE.md`.

## Required Markdown guide for each modular interchange

Register the assembly and keep its complete rebuilding guide in `domains/<domain>/01_assemblies/<assembly-id>/README.md`, with software evidence, limitations, and generated human checks in `TESTING.md`. Follow the shared [assembly guide layout](WORKFLOW_DOCUMENTATION_GENERATION.md#required-markdown-guide-for-each-modular-interchange) for the required pictures, type quantities, placement table, rebuilding order, complete journeys, coordinates, and evidence. Update the accepted plan, guide, image links, and reports together; a chart or parts list alone is insufficient.

## Worked example

The [current trumpet README](../domains/high-speed-rail/01_assemblies/straight-stem-trumpet-v4/README.md) demonstrates the complete rebuilding guide, six-image set, type thumbnails, placement tables, and permitted journeys. Its [TESTING page](../domains/high-speed-rail/01_assemblies/straight-stem-trumpet-v4/TESTING.md) owns the layout-specific measurements, current resource contract, technical limitations, and scoped checks. Reuse that structure without copying its particular dimensions or rail assumptions into unrelated assemblies.

## Clear piece ownership and reusable types

A placement label (P05, P06, P04E) identifies one copy in the assembly; it does not create a new menu piece type. Reuse one existing straight button at every compatible placement, applying proper rotations. Do not create east/west or numbered variants merely to preserve different triangle ordering, texture repeat counts, or endpoint tessellation. Preserve track geometry, direction, height, native connection profiles, pillar positions, and shadow silhouettes; verify any permitted resource substitution explicitly and narrowly. Keep exact resource checks on unaffected curves, junctions, and ramps. Include a type-to-placement/quantity table so repeated copies are obvious to players. For an exact-position design, do not replace tiny curve tails or shared branch-deck wings merely because they look straight in the overview.

Use the shared [ownership colours](WORKFLOW_DOCUMENTATION_GENERATION.md#ownership-colours) in named model views and the occupied-tile plan. The assignment must distinguish neighbouring placements, including two copies of one type.

## Reusable names and standalone type pictures

Use the shared [reusable-name and standalone-picture contract](WORKFLOW_DOCUMENTATION_GENERATION.md#reusable-names-and-standalone-type-pictures) when preparing a new or revised type, and use the [generic canonical top-view workflow](WORKFLOW_DOCUMENTATION_GENERATION.md#current-renderer-support-and-canonical-top-views). Repeated placements share one type, one menu button, and its canonical images; assembly views retain their fixed layout coordinates and instance labels.

Before replacing an almost-straight tile, inspect every encoded route and the whole saved model. A 2 mm curve is still a curve under an exact-position requirement; straight PATHs can also sit on necessary branch-deck wings. Compare any approved ordinary substitution's directed samples/flags, complete native profile, level, support contacts, material/texture repeats, and all five world-oriented shadows. Keep all other resource checks strict. Do not change curves or snap ports unless the user's chosen layout policy permits it.

## Distinguish unchanged geometry from binary identity

A source reorganization must be checked against freshly compiled saved resources. The same visible track does not imply identical DAT or S3D bytes. Preserve the original input and image hashes as provenance; record fresh build hashes separately. When encodings differ, disclose them and require an independent comparison of exact ordered visible float32 XYZ/UV draws, winding, materials, flags, frames, and bounds, plus actual PATHs, shadows, identifiers, menus, and construction rules. A picture alone cannot establish that equivalence. Keep strict byte checks for resources that are required to remain byte-identical.

A saved comparison must identify its exact input files and distinguish equivalent rendering from identical binary encoding. Do not treat an old hash as a new file identity, overwrite actual preview fingerprints, or use a software comparison to confirm an in-game/manual test. When a subject is explicitly deleted, remove its obsolete reports and fixtures instead of retaining them as current dependencies. Apply actual case-dependency rules when refreshing the retained subjects' manual records; geometry equivalence cannot tick a user checkbox.

## Atomize to the smallest useful reusable module

A useful module has an independently placeable function, valid construction addresses, meaningful ports, and practical uses beyond one pictured location. It need not be one tile. Inspect every apparently straight tile's actual PATH samples and full deck before extracting it. Shared branches, widened wings, small curve tails, slope easing, and support ownership can require a larger coordinated module. Reuse an existing standard type when compatible; do not create cardinal/P-label variants of an ordinary straight. Under an exact-layout requirement do not snap a tiny curve to make an extraction fit. Explain the measured limitation, preserve the geometry, and split only proven useful blocks.

## Persist atomization decisions and coordinate parallel work

An **atomization decision** records why a candidate tile can become an existing standard piece, or why it must remain inside a larger module. Keep one authoritative `checks/atomization.json` beside the assembly's placement and quality contracts; summarize its decisions in the existing README or TESTING page rather than adding another Markdown file. Distinguish historical eligibility measurements from checks on the current resources. When predecessor subjects are explicitly deleted, keep their useful decision measurements as history and pin the retained assembly with its own `checks/resources.json`; verification must not require deleted definitions, layouts, or DAT fixtures. A reusable type's README links the relevant decision, states its generic connection limits, and explains the useful function that remains.

For each reviewed candidate, record its source type and placement, local and assembly X/Y tiles, original measured deviation, physical deck and wall requirements, decision, plain-language reason, and exact replacement type and rotation. An accepted redesign also records the smallest changed region, actual maximum route movement, independent acceptance bound, support/port policy, compiled evidence, and source fingerprints. A rejected candidate records the measured obstacle and what larger redesign or evidence could justify reconsideration. A real platform wing or a restored wall obstructing another train is a different reason from a curve exceeding a threshold; explain which applies. List all reviewed source cells so omitted interior or structural tiles are accounted for explicitly.

Keep the **eligibility threshold** separate from the **actual redesign bound**. For example, an original 2.058 mm tail can qualify under a strict “less than 5 mm” policy while its adjoining joining curve needs an 8.14 mm correction to meet the existing native-end curvature limit. Record both numbers and their measurement methods. Do not claim that the whole redesign moved less than 5 mm, relax curvature/clearance limits, or silently broaden the allowed cells. An exact-position policy still forbids snapping a curve unless the user has authorized bounded redesign.

When several agents atomize one assembly, first freeze the approved version and its actual compiled resources. Work in a new requested version, with source hashes protecting subjects that the user wants to retain. Assign each geometry family a separate new implementation file and new piece folders; keep identifiers, shared hooks, collection registration, and assembly integration under one coordinator. Have an independent reviewer inspect actual saved resources. Start the final render pass only after every geometry agent has finished and the complete assembly passes its checks. Render the integrated result once; preserve retained versions' images and observations. If the user explicitly deletes earlier subjects, remove their files and exclusive dependencies, preserve useful measurement rationale as history, and verify the retained design against its approved current resource contract. Source fingerprint changes make applicable decision evidence stale until rechecked; they never create a game-test pass.

## Connections, journeys, and human-confirmed checks

Each piece needs its own connection overview, with stable identities, actual positions in canonical local orientation, network services, physical channels and boundary cuts, directed movements and mode permissions, nominal level and exact path height, and actual endpoint heading and slope. Use the shared [connector reference](CONNECTOR_METADATA.md) for complete-boundary comparisons and [overview procedure](WORKFLOW_DOCUMENTATION_GENERATION.md#reading-an-overview) for generation, cards, and freshness checks. Link direct candidate matches and required adapters; existing per-port counterpart shortlists are not an exhaustive compatibility catalogue. A common height or profile name alone does not establish a continuation or physical fit.

Prepare missing or changed types through [WORKFLOW: Piece Creation](WORKFLOW_PIECE_CREATION.md#51-generate-and-check-the-pieces-connector-export-and-overview): verify saved resources, extract current measurements, author source-backed channel associations, and generate the resolved export and canonical cards. Assembly and Planner consumers read that result. Do not create another authoring/parser workflow in the application or hand-copy numerical tables into an assembly as an independent source.

At a proposed join, transform the complete tile-edge segments, member positions, headings, outward grades, models, and owned cells under one common placement. Require every service and required cut on the shared boundary to agree, and check other already occupied neighbours separately. A touching corner, a compatible upper service with a missing lower service, or unrelated placements that fit different groups cannot establish one complete join. Other branches can remain unfinished only where no existing neighbour creates a conflict. Pairwise compatibility does not replace whole-assembly ownership, construction, journey, or clearance checks.

Each assembly declares every permitted directed journey for every participating transport, plus forbidden level transfers and unintended crossings. HSR, tram, and future conventional rail checks are separate even when their game resource identifiers overlap. Every real journey needs travel demand, compatible end connections, a route query or observed traffic, and the tested orientation and platform. A pretty render does not establish any journey.

Use [TESTING.md](TESTING.md) for the sole observation record, exact case scope, current and stale states, and the recording procedure. Only an explicitly confirmed matching human observation can create a manual pass. Keep the assembly's coverage distinct by service, directed journey, pose, rotation, and tested environment; preview approval and software checks do not confirm game traffic. Recheck the affected whole traffic graph after a route change, rather than only the edited member, and report the actual covered cases.

## Compact documentation ownership

Follow [WORKFLOW: Documentation Generation](WORKFLOW_DOCUMENTATION_GENERATION.md#readme-layouts-and-generated-sections) for the one-README piece layout, assembly README/TESTING layout, generated-block ownership, inventories, and preservation checks. Keep source-specific design decisions and measurements with the owning subject; shared presentation and regeneration rules stay in that workflow.
