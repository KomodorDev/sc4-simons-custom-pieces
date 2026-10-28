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

- A **movement** is one permitted journey, such as south to west. The reverse journey is a separate movement. A full three-arm T carrying one service has six movements.
- A **port** is a measured traffic-route endpoint. The [connector reference](CONNECTOR_METADATA.md) defines how complete shared boundaries, permissions, and placement are compared; physical fit requires its own geometry checks.
- A **module** is a functional component selected within an assembly's shared menu cycle. Its reusable type can also belong to other builds.
- A **blueprint** is an exact arrangement of several modules. Building it requires several placements, even when the finished layout is ready-made.
- A **one-click interchange** is one selectable piece that constructs the complete junction. It needs its own construction and address checks.
- A **DAT** is the game's resource archive. **PATH** resources describe traffic routes; **S3D** resources contain the visible model; **FSH** resources contain artwork, including textures and shadows.

**Assembly menu policy: every assembly has exactly one menu button, with Tab cycling forward through its reusable components and Shift+Tab cycling backward.** Each click places the selected component; the placement table describes the complete arrangement. Package the compiled components through the [assembly-menu step](BUILD_AND_INSTALL.md#prepare-the-assembly-menu), hide their duplicate member buttons in that assembly package, and keep unrelated standalone piece buttons unchanged. Every component remains selectable through the cycle. New complete complex interchanges are modular blueprints with their own README and TESTING documents.

Apply the mandatory [piece-versus-assembly decision](WORKFLOW_PIECE_CREATION.md#0-decide-between-a-piece-and-an-assembly) before allocating types or producing detailed geometry, including requests phrased as a single “piece.” When the design belongs here, announce that delivery is an assembly and that the complete junction will not be provided as one selectable piece. Record the reusable functions and granularity rationale in the assembly's TESTING document, then prove the modules through steps 3–5. A large diagonal X with central and branching regions is an assembly-design task; neither successful one-piece compilation nor internal mesh chunking proves a reusable-parts design. Preserve existing accepted types and treat the current trial's single-piece model as feasibility evidence, rather than claiming that a modular replacement already exists.

The earlier straight-stem trumpet baseline could not be one ordinary construction piece: its 109 occupied tiles mapped to only 95 unique runtime lookup keys, causing 14 tile-address collisions. These figures describe that historical baseline and do not report a measurement of the current redesigned assembly. A **collision** means that two tiles ask the engine for the same lookup entry and one selects the other tile's model and paths. Combining meshes or choosing new resource identifiers does not repair that. The current Plop & Paint tool also cannot stamp a network-piece blueprint. Any future one-click design requires its own construction and placement checks.

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
2. List the intended movements and permitted travel directions separately for each network service. For a full T carrying one service: `W→E`, `W→S`, `E→W`, `E→S`, `S→W`, and `S→E`; exclude U-turns unless requested.
3. State which crossings must be separated vertically. Identify intended merges and splits, where routes are allowed to meet at the same height.
4. Record the external connection heights, interface widths, and native network ends for each service. Name any intermediate custom height explicitly.
5. Record the desired footprint, straight/diagonal orientation, symmetry, terrain assumptions, and modular placement method. Distinguish requirements from preferences and unresolved questions. Plan a dedicated rebuilding guide rather than an unimplemented complete-interchange button.

Then present an editable in-chat chart using the available visualization tools. Show north, the city grid, labelled arms, direction arrows, a consistent colour per movement, and height labels wherever lines cross or change level. Include a legend and an explicit **schematic** label. Until dimensions are checked, state that sizes and radii are provisional.

The chart should make the transport logic obvious before models, textures, pillars, or menu resources are built. Investigate an uncertain crossing or connection with a small feasibility sketch rather than expanding the whole family immediately.

**Output:** a short brief, a movement list, and the current schematic shown directly in chat.

## 2. Iterate until the shape matches the user's intent

Use the user's comments to revise the chart. Resolve the arrangement of loops, branches, crossing order, direction of travel, and symmetry first. For example, “make the east-to-south curve follow the south-to-west loop before separating” changes the route layout and must be visible in the chart.

Keep the movement colours, arm names, and coordinate origin stable between iterations. Explain what changed and why. If a requested shape conflicts with a height transition or matching network end, show the specific conflict and a small alternative.

Once the intended shape is clear, carry out routine implementation decisions without repeatedly asking for confirmation. Return to this layout discussion when feasibility requires a material change to the agreed shape or movements.

**Output:** the agreed current layout, with any remaining assumptions marked.

## 3. Check existing pieces and prove the connection plan

Inspect `project.json`, the domain inventory, current manifests, and verified builds. Similar names or appearances do not prove that two pieces connect.

Create a parts table with one row per required functional module:

| Module label | Purpose | Existing exact piece ID | Port/placement compatibility | Action |
| --- | --- | --- | --- | --- |
| P01 | Mainline crossing | Exact current ID, if available | Checked / unverified, with the reason | Reuse, test, adapt, or build |
| P02 | Curved height change | None, if missing | Required entry/exit heights and headings | Build a separate module |

For each connection, check the exact three-dimensional endpoint, travel heading, permitted direction for each service, required interface spacing, visible profile, and construction-grid alignment. Write these expected connections independently of the generator. Keep visual fit and traffic-path compatibility separate.

Also assign every occupied city tile to exactly one module. Upper and lower routes sharing a tile generally need a coordinated module containing both routes; independently placing another piece there can overwrite the first. Check sparse footprints, empty construction-origin cells, rotations, and the runtime tile-address rules before relying on an apparent fit.

Check runtime addressing for each independently placed module. Keep the complete arrangement as a blueprint; a safe component allocation does not imply that merging all components into one construction is safe.

**Output:** a parts list, expected ports and movement connections, tile owners, and an explicit list of missing or unproven parts.

## 4. Build and test the smallest missing reusable parts

Implement only the missing modules needed for the agreed design. Start with the smallest useful crossing, split, merge, adapter, or curved ramp that tests an uncertain connection.

Each new functional module needs:

1. Its own current manifest, unique identifiers, descriptive SCP menu name, and icon, so the user can place it independently.
2. Explicit traffic paths, visible geometry, occupied cells, construction rules, matching ports, supports, and shadow resources.
3. Independent checks of the saved DAT contents. Inspect actual encoded PATH samples, S3D geometry, and construction rules, not just values supplied by the generator.
4. Checks for permitted and forbidden movements, correct split/merge flags, all four proper 90-degree rotations, native connection profiles, curve and slope limits, traffic clearance, open joins, support contacts and spacing, and all five model/shadow zooms.
5. Its own canonical artwork, connection overview, manual records, and inventory row under the shared [documentation-generation workflow](WORKFLOW_DOCUMENTATION_GENERATION.md), including both angled and north-up views for a new or geometrically revised type.

Use the existing piece-authoring guide for the commands and allocation rules. Test a small changed selection first. Reuse already verified results only when every relevant specification and binary input is identical.

**Rotation is required for every independently placeable module:** check 0°, 90°, 180°, and 270° for its emitted construction rules, occupied cells, actual model, PATH entry/exit directions, ports, preview, and shadows. A **proper rotation** turns a piece without reflecting it. Do not mirror a one-way route to create extra states; repeat the four rotations if the menu needs eight states. A diagonal variant is a separately authored 45-degree layout with native diagonal ports, not an extra 45-degree rotation of a straight piece. Record file-check evidence separately from all-four-rotation placement and traffic tests in the game.

Useful wider variants remain separate current pieces. Add a clearly named compact variant when its geometry is different; do not silently change an existing useful piece or retain rejected prototype versions as compatibility artifacts.

**Output:** independently selectable, compiled, and checked missing modules.

## 5. Assemble actual compiled pieces and check the whole interchange

Make a machine-readable placement plan. Record a stable module label such as `P01`, its exact piece ID and descriptive SCP menu name, translation, rotation, occupied cells, and source DAT fingerprint. Give repeated copies separate instance labels: four copies of one straight are `P05`, `P06`, `P07`, and `P08`, even though their menu name and piece ID match. Preserve those labels through all views and revisions. A fingerprint is a hash identifying the exact file bytes.

Assemble the saved component models using rotations and translations only. Do not reshape network ends, hide clipping, delete pillars, or repair walls only inside the preview. A repair belongs in an independently placeable module.

Check the complete arrangement:

- Every required directed journey exists; unwanted U-turns, transfers between levels, reverse travel, and unintended same-height crossings are absent.
- Every seam matches in position, height, direction, and profile. The actual traffic corridor remains clear across the join.
- Occupied construction cells do not overwrite another module's routes.
- Pillars meet their decks and satisfy spacing across module boundaries. Two pieces that pass separately can still introduce duplicate or obstructing pillars when placed next to each other.
- Crossings have sufficient clearance in the visible model, including walls and deck thickness, rather than only different PATH heights.
- Rotations, tile addresses, previews, render-group budgets, and all zoom resources remain valid in the final arrangement.

If a module is missing or wrong, return to **step 4**, then rebuild and recheck the affected assembly. If the agreed route arrangement itself is infeasible, return to **step 2** with a concrete explanation.

**Output:** a reproducible assembly and a whole-interchange validation report.

## 6. Review coordinate-labelled renders with the user

Generate the accepted layout's actual compiled-model pictures using [WORKFLOW: Documentation Generation](WORKFLOW_DOCUMENTATION_GENERATION.md#assembly-picture-set-and-in-picture-identification). Start each render's first row with `Assembly - ` and the assembly name; start its second row with `Clean view`, `Component guide`, or `Construction view`, followed by the camera direction. Apply the fixed [coordinate contract](WORKFLOW_DOCUMENTATION_GENERATION.md#coordinate-contract-for-charts-and-renders), six-image set, exact menu-name callouts, and ownership colours. Use the current machine-readable placement plan and verified builds; check the documented renderer scope before running a command. Add a close-up where a join, crossing, or support needs discussion.

Review the shape, symmetry, route clarity, joins, supports, and space use with the user on that same fixed grid. Geometry feedback returns to **step 4**; layout feedback returns to **step 2**. Do not change approved geometry solely to improve a camera view. Keep software preview approval separate from game-test evidence.

**Output:** the complete current coordinate-labelled review set and the user's feedback, with image roles, placements, and input fingerprints recorded under the shared generation contract.

## 7. Compact the agreed interchange, then recheck it

Consider available space from the first sketch. Perform a deliberate compaction pass after the complete arrangement is understandable and reviewed.

1. Remove straight approach padding that serves no connection or height transition. Check the west, east, and south arms and the loop's own straights.
2. Move compatible splits and merges closer to the main crossing where clearances and tile ownership permit it.
3. Shorten loop sides and its top straight, and reduce curve size where the approved curvature and slope limits still pass. A curve may also change height if an independently tested module supports that combination.
4. Preserve matching end segments, safe traffic clearances, support spacing, and required climb length. Do not weaken existing limits to make a smaller footprint pass. Record why any remaining straight length is necessary.
5. Build additional compact modules as needed, returning to **step 4**. Run the affected piece checks and the whole-assembly checks again. Present the result on the same coordinate grid for review.

Compare the width and depth of the enclosing construction rectangle, occupied tile count, route lengths, and relevant curve/slope measurements. The rectangle includes empty space; its area is not the number of occupied tiles. Describe the achieved reduction rather than claiming a mathematically minimum design.

**Output:** the current compact layout, verified measurements, and updated coordinate-labelled review images.

## 8. Package, install when requested, and test inside the game

Freeze the accepted current design. Deliver the movement list, exact module selection and names, coordinate plan, placement order and rotations, required heights, previews, and verification results. Keep current docs and packages in sync; remove rejected or superseded prototype artifacts without deleting useful current alternative components.

Build the complete intended installed selection with **one shared controller and one menu**. Preserve existing installed pieces. Independent subset builds must not be stacked as if their controller files could all remain active. Record the exact final file hashes and compare installed files with the build. An installation request authorizes installation; creating a preview alone does not install a new collection.

Package the individually placeable components, the one-button assembly cycle, and the README/TESTING documents. The assembly button selects components through Tab; it does not construct the complete arrangement with one click. Do not mark that component cycle as PNP or describe it as a Plop & Paint stamp. The current whole-trumpet address collisions remain even if its components are packaged together. A future one-click research project must satisfy the policy in **Terms and evidence** before it can change this delivery method.

To establish game operation, use a disposable flat city and the exact installed version. Test placement and every intended movement with real traffic demand and the observations required by the declared test plan. **Route Query** is the game's tool for showing assigned traffic routes; **visible travel** means watching traffic complete the stated directed journey. When the plan declares both checks, record them as separate observations for each service and direction; neither establishes the other. Also test forbidden transfers at same-network crossings and parallel edges at different heights. Use the declared reference layout for human checks; inspect zooms, shadows, joins, demolition, save/reload, and the claimed terrain behaviour. Require additional manual orientations only when the test plan identifies a specific reason; automatic software rotation checks keep their own coverage. Record the game/platform, file hashes, city layout, observations, and screenshots. Return defects to the appropriate earlier step.

Keep untested behaviours explicitly unverified. Public distribution has additional requirements documented separately in `docs/RELEASE.md`.

## Required Markdown guide for each modular interchange

Register the assembly and keep its player overview in `domains/<domain>/01_assemblies/<assembly-id>/README.md`, with detailed preparation, coordinate definitions, software evidence, limitations, history, and generated human checks in `TESTING.md`. Follow the shared [assembly guide layout](WORKFLOW_DOCUMENTATION_GENERATION.md#required-markdown-guide-for-each-modular-interchange) and its [six-chapter TESTING layout](WORKFLOW_DOCUMENTATION_GENERATION.md#required-assembly-testing-layout). The TESTING chapters are **1. Test scope**, **2. Test setup**, **3. Software checks**, **4. Game checks**, **5. Results and known issues**, and **6. Design history**; detailed current results precede design history. Update the accepted plan, guide, image links, and reports together; a chart or parts list alone is insufficient.

## Worked example

The [current trumpet README](../domains/high-speed-rail/01_assemblies/straight-stem-trumpet/README.md) demonstrates the current four-section overview: **1. Views**, **2. Pieces**, **3. Placements**, and **4. Connection matrix**. Its top navigation labels the Testing link as a separate document. It includes the six-image set, component thumbnails, exact placements, and directed connection statuses. Its [TESTING page](../domains/high-speed-rail/01_assemblies/straight-stem-trumpet/TESTING.md) owns the layout-specific measurements, current resource contract, technical limitations, and scoped checks. Reuse that structure without copying its particular dimensions or rail assumptions into unrelated assemblies.

## Start a small HSR assembly from existing pieces

Use this bounded example to learn the registration and first-documentation sequence before attempting a junction. It creates a **two-tile training layout**, using two copies of the existing `hsr-component-lower-paired-straight` type at 15.5 m. Its expected footprint is one tile east–west and two tiles north–south. It introduces no new reusable type, puzzle identifier, or model-resource allocation. Both placements share one component-cycle entry; a multi-type assembly adds its distinct types in first-use order. This example does not establish physical fit, native construction, game traffic, or a complete interchange.

Follow the [creation checklist](WORKFLOW_DOCUMENTATION_GENERATION.md#creation-checklist-and-output-files) alongside these steps. Run commands from the repository root after the [Python installation and editable project installation](WORKFLOW_PIECE_CREATION.md#1-open-the-project-and-inspect-the-existing-pieces). If several checkouts exist, run the editable installation for the checkout you are actually editing. Prepare the supported native inputs through [Build and install](BUILD_AND_INSTALL.md#build-a-selected-collection) before any build or actual-model render. Replace `/path/to/SimCity 4/Plugins` below with the existing Plugins directory containing the required native inputs; it is read for resources and collision checks.

### 1. Copy the unregistered placement template

The [starter JSON](templates/assembly-two-hsr-straights.json) lives outside the domain registry. Merely downloading or editing that template creates no registered assembly. The following commands deliberately create a new assembly folder and copy the plan into it. Stop if `two-tile-hsr-starter` already exists; choose another lowercase hyphenated slug and replace that slug consistently in the plan, registry, menu layout, icon identity, and commands.

```sh
mkdir custom-pieces/domains/high-speed-rail/01_assemblies/two-tile-hsr-starter
cp -n custom-pieces/docs/templates/assembly-two-hsr-straights.json custom-pieces/domains/high-speed-rail/01_assemblies/two-tile-hsr-starter/assembly.json
```

Open the copied `assembly.json`. `P01` is at metre position `[0, 0]`, and `P02` is at `[0, 16]`; both use `rotation_degrees_ccw: 0`. **Counterclockwise** means turning left when viewed from above; accepted proper rotations are 0°, 90°, 180°, and 270°. A placement's `piece_id` names the existing type, whereas `instance_id` and `label` identify that copy. `origin_m` stores the technical east/north translation in metres. The separately stored display positions are `(X0, Y0)` and `(X0, Y1)`, using the shared southwest tile-centre reference. The construction reference is not a promise about the untested game cursor.

The template's external-port positions are authored expectations from that exact type: south at northing −8 m and north at northing 24 m, with opposing track centres at easting ±2 m and height 15.5 m. Its count fields describe the intended placement plan. Leave `geometry_status` explicitly unverified until real checks justify a more specific statement. Do not paste the trumpet's dimensions, source hashes, or observations into this new subject.

### 2. Register the plan in the owning domain

Run the following command to append the new relative path to `custom-pieces/domains/high-speed-rail/domain.json`. It checks that the plan exists and refuses duplicate registration; it preserves the existing piece and assembly entries.

```sh
python3 - <<'PY'
import json
from pathlib import Path
domain = Path('custom-pieces/domains/high-speed-rail')
relative = '01_assemblies/two-tile-hsr-starter/assembly.json'
if not (domain / relative).is_file():
    raise SystemExit('Create the assembly.json plan first.')
path = domain / 'domain.json'
registry = json.loads(path.read_text())
assemblies = registry.setdefault('assemblies', [])
if relative in assemblies:
    raise SystemExit('This assembly is already registered; inspect it instead of adding a duplicate.')
assemblies.append(relative)
path.write_text(json.dumps(registry, indent=2) + '\n')
print('Registered ' + relative)
PY
```

The folder name supplies the assembly ID `two-tile-hsr-starter`. The registry entry is relative to the domain directory; it must have the form `01_assemblies/<assembly-id>/assembly.json`. Do not run the piece scaffold for this assembly: its member type already owns the piece's game-resource identities.

### 3. Add its separate menu layout

`menu-layout.json` connects the registered assembly to its single button. Its layout key is the name passed to `assembly-menu --layout`; it is separate from the permanent assembly ID. The command below uses `two-tile-hsr-starter` for both to keep the example clear. It reserves a new **local presentation ID**, meaning the identifier for this assembly's button resources, rather than reusing the trumpet's or a member piece's button ID.

Run this command once. It chooses an unused candidate in a small local menu-prefix range after checking current piece-menu reservations and every registered domain's existing layout entries, then writes the complete accepted layout object. This is a local development choice, rather than a public reservation. The later `assembly-menu` operation must still check that candidate against the actual installed Plugins resources. If that check reports a collision, replace only the new button's `id` with another locally unused candidate and repeat the final checks; preserve existing identities.

```sh
python3 - <<'PY'
import json
from pathlib import Path
from scp.catalog import load_catalog
root = Path('custom-pieces').resolve()
catalog = load_catalog(root)
path = root / 'domains/high-speed-rail/menu-layout.json'
menu = json.loads(path.read_text())
key = 'two-tile-hsr-starter'
if key in menu['layouts']:
    raise SystemExit('This menu layout already exists; inspect it instead of replacing it.')
used = {int(piece['menu']['id'], 16) for piece in catalog['pieces']}
for domain in catalog['domains'].values():
    layouts_path = root / domain['path'] / 'menu-layout.json'
    if not layouts_path.is_file():
        continue
    for layout in json.loads(layouts_path.read_text()).get('layouts', {}).values():
        for field in ('cycle_button', 'submenu'):
            if field in layout:
                used.add(int(layout[field]['id'], 16))
candidate = next((value for value in range(0x6A47FE00, 0x6A47FF00) if value not in used), None)
if candidate is None:
    raise SystemExit('The example range is full; obtain another reviewed local presentation range.')
menu['layouts'][key] = {
    'assembly_id': key,
    'member_order': 'first-use-in-assembly',
    'cycle_button': {
        'id': f'{candidate:08x}',
        'order': f'7010{candidate & 0xffff:04x}',
        'title': 'SCP | ASSEMBLY | Two-tile HSR starter',
        'description': 'Select the reusable HSR straight. Tab and Shift+Tab select component types; each click places one copy. Rebuild the two placements from the assembly guide.'
    }
}
path.write_text(json.dumps(menu, indent=2) + '\n')
print('Locally reserved assembly presentation: ' + f'{candidate:08x}')
PY
```

Open the changed `menu-layout.json` and inspect the new entry. `member_order` must be exactly `first-use-in-assembly`. The button must contain exactly `id`, `order`, `title`, and `description`; both numeric strings have eight hexadecimal digits. **Hexadecimal** is base-16 notation, using 0–9 and a–f. `order` places the button in the Rail menu's accepted `70000000`–`7fffffff` range. Keep the full readable title and component-placement explanation; the icon cannot replace those instructions.

### 4. Declare the HSR icon identity and generate artwork

The current HSR icon adapter requires an explicit network declaration for every assembly ID. Open `custom-pieces/domains/high-speed-rail/implementation/scp_hsr/icons.py`, find `assembly_icon_network`, and add `'two-tile-hsr-starter': 'HSR'` to its existing `networks` dictionary, retaining all existing entries. For the current registry, that dictionary becomes:

```python
networks = {
    'straight-stem-trumpet': 'HSR',
    'two-tile-hsr-starter': 'HSR',
}
```

This is a deliberate domain-adapter edit: the current API receives an assembly ID and does not read an arbitrary network field from `assembly.json`. It selects the truthful network code for the button; it changes no track geometry or piece identities. The HSR route artwork helper currently supports its authored component recipes, including this straight. Another family or network needs its owning adapter implemented and checked before this artwork/menu path applies.

Generate the canonical assembly icon from the source placements:

```sh
python3 -B custom-pieces/scp.py assembly-icons --domain high-speed-rail
```

This command refreshes all registered HSR assembly icons and their `evidence/icon.json` reports, including the new one; inspect that scope before running it. Inspect the actual 44 × 44 pixels in each of the four button states. Keep the route drawing legible, the small SCP brand in the top-left corner, and the ASM HSR label near the bottom with its required clearance. An icon is a source-derived illustration, rather than compiled-model or game evidence.

### 5. Build the member and populate the first document pair

Choose a fresh output directory; replace `review-01` consistently if it already exists. This assembly uses only one distinct member type, so one `--include` supplies both copies:

```sh
python3 custom-pieces/scp.py build --include hsr-component-lower-paired-straight --output custom-pieces/dist/two-tile-hsr-parts-review-01
python3 custom-pieces/scp.py verify --output custom-pieces/dist/two-tile-hsr-parts-review-01
python3 -m scp_hsr.hsr_connections --root custom-pieces --build custom-pieces/dist/two-tile-hsr-parts-review-01
```

The last command intentionally omits `--piece`. The build-wide HSR extractor measures supported members in that verified build, preserves uncaptured measured records, composes affected registered assembly graphs, and refreshes shared connection/inventory views. Because this straight also belongs to the trumpet, inspect changes to that existing assembly and shared views too. The command preserves human observations and applies dependency staleness; it does not approve them. Exact-piece extraction deliberately defers assemblies, so it cannot perform this first assembly population.

Open the new assembly's generated `README.md` and `TESTING.md`, plus `connections.json`, `checks/manual-tests.json`, and `checks/observation.example.json`. The initial README has the four required chapters and the separate Testing navigation; TESTING has six chapters. The generated matrix describes encoded routes at the saved poses. Matching PATH endpoints do not establish complete physical boundaries, support clearance, native construction, or game operation. Ordinary `python3 -m scp.content refresh --root custom-pieces` refreshes views from existing records; it skips a new assembly without connection/manual records and is not a substitute for this initial extraction.

### 6. Complete the views, authored instructions, and checks

Stage the actual-model review pictures from that verified build:

```sh
python3 custom-pieces/domains/high-speed-rail/tools/render_hsr_assembly.py --scene custom-pieces/domains/high-speed-rail/01_assemblies/two-tile-hsr-starter/assembly.json --build custom-pieces/dist/two-tile-hsr-parts-review-01 --plugins '/path/to/SimCity 4/Plugins' --output-dir custom-pieces/local/two-tile-hsr-review --prefix reviewed-two-tile
```

Follow the shared [six-image review and promotion handoff](WORKFLOW_DOCUMENTATION_GENERATION.md#current-renderer-support-and-canonical-top-views). The renderer stages images and their real report under `local/`; it does not install canonical source images automatically. Inspect the pictures, retain their actual source and output fingerprints, and deliberately integrate the accepted images under the assembly's `previews/` and the render report under `evidence/`. Complete README chapters 1–3 with links, the one-type/two-placement quantities, P01/P02 positions, 0° rotations, 15.5 m connections, and the Tab/component instructions. Complete TESTING with real preparation, the checks actually performed, the remaining physical/game limitations, and design history. Add a link to this assembly from the owning domain's human README. Keep authored text outside generated blocks, and record no game pass without a matching human observation.

After the final images and text are present, run:

```sh
python3 custom-pieces/scp.py observations refresh-images --assembly two-tile-hsr-starter
python3 -m scp.content refresh --root custom-pieces
python3 custom-pieces/scp.py inventory
python3 -B custom-pieces/scp.py docs-check --assembly two-tile-hsr-starter
python3 -B tools/run_tests.py
```

`docs-check` validates the current pair, required files, and local links without creating missing outputs or changing observations. An initial scaffold can satisfy the chapter structure while still containing pending instructions; complete and review those instructions before calling it a documented experimental candidate. The software suite does not prove the new assembly's physical joins or game behaviour; add and execute the independent checks required by the actual claims, and report skips. If the whole catalogue/shared guides need checking, run `python3 -B custom-pieces/scp.py docs-check` without selectors.

### 7. Prepare a fresh final assembly-menu candidate

Finish source documentation, icon artwork, measurements, and applicable checks first. Then build a fresh ordinary source selection, prepare this layout's single button, verify the candidate, and package it without `--refresh-docs`:

```sh
python3 custom-pieces/scp.py build --include hsr-component-lower-paired-straight --output custom-pieces/dist/two-tile-hsr-parts-final-01
python3 custom-pieces/scp.py assembly-menu --domain high-speed-rail --layout two-tile-hsr-starter --source custom-pieces/dist/two-tile-hsr-parts-final-01 --output custom-pieces/dist/two-tile-hsr-menu-final-01 --plugins '/path/to/SimCity 4/Plugins'
python3 custom-pieces/scp.py verify --output custom-pieces/dist/two-tile-hsr-menu-final-01
python3 custom-pieces/scp.py package --output custom-pieces/dist/two-tile-hsr-menu-final-01 --destination custom-pieces/dist/two-tile-hsr-menu-final-01.zip
```

Use unused output names, and preserve previous candidates. Include other wanted SCP types in the same fresh ordinary source selection before preparing a candidate intended to replace an existing installation. The menu builder checks the new presentation ID against installed resources, verifies the canonical icon and member definitions, and freezes the source proof. This one-type training example has one cycle entry and still requires two placements. Its archived pending menu checks are not observations. Follow the [separate install and game-testing procedures](BUILD_AND_INSTALL.md#install-remove-or-roll-back-a-test-build) only when installation and testing are intended; producing this ZIP installs and publishes nothing.

## Clear piece ownership and reusable types

A placement label (P05, P06, P04E) identifies one copy in the assembly; it does not create a new menu piece type. Reuse one existing straight type at every compatible placement, applying proper rotations. Do not create east/west or numbered variants merely to preserve different triangle ordering, texture repeat counts, or endpoint tessellation. Preserve model and route geometry, direction, height, native connection profiles, pillar positions, and shadow silhouettes; verify any permitted resource substitution explicitly and narrowly. Keep exact resource checks on unaffected curves, junctions, and ramps. Include a type-to-placement/quantity table so repeated copies are obvious to players. For an exact-position design, do not replace tiny curve tails or shared branch-deck wings merely because they look straight in the overview.

Use the shared [ownership colours](WORKFLOW_DOCUMENTATION_GENERATION.md#ownership-colours) in named model views and the occupied-tile plan. The assignment must distinguish neighbouring placements, including two copies of one type.

## Reusable names and standalone type pictures

Use the shared [reusable-name and standalone-picture contract](WORKFLOW_DOCUMENTATION_GENERATION.md#reusable-names-and-standalone-type-pictures) when preparing a new or revised type, and use the [generic canonical top-view workflow](WORKFLOW_DOCUMENTATION_GENERATION.md#current-renderer-support-and-canonical-top-views). Repeated placements share one type, one menu button, and its canonical images; assembly views retain their fixed layout coordinates and instance labels.

Before replacing an almost-straight tile, inspect every encoded route and the whole saved model. A 2 mm curve is still a curve under an exact-position requirement; straight PATHs can also sit on necessary branch-deck wings. Compare any approved ordinary substitution's directed samples/flags, complete native profile, level, support contacts, material/texture repeats, and all five world-oriented shadows. Keep all other resource checks strict. Do not change curves or snap ports unless the user's chosen layout policy permits it.

## Distinguish unchanged geometry from binary identity

A reorganization of code that generates game resources must be checked against freshly compiled saved resources. The same visible network geometry does not imply identical DAT or S3D bytes. Preserve the original input and image hashes as provenance; record fresh build hashes separately. When encodings differ, disclose them and require an independent comparison of exact ordered visible float32 XYZ/UV draws, winding, materials, flags, frames, and bounds, plus actual PATHs, shadows, identifiers, menus, and construction rules. A picture alone cannot establish that equivalence. Keep strict byte checks for resources that are required to remain byte-identical.

A saved comparison must identify its exact input files and distinguish equivalent rendering from identical binary encoding. Do not treat an old hash as a new file identity, overwrite actual preview fingerprints, or use a software comparison to confirm an in-game/manual test. When a subject is explicitly deleted, remove its obsolete reports and fixtures instead of retaining them as current dependencies. Apply actual case-dependency rules when refreshing the retained subjects' manual records; geometry equivalence cannot tick a user checkbox.

## Atomize to the smallest useful reusable module

A useful module has an independently placeable function, valid construction addresses, meaningful ports, and practical uses beyond one pictured location. It need not be one tile. Inspect every apparently straight tile's actual PATH samples and full deck before extracting it. Shared branches, widened wings, small curve tails, slope easing, and support ownership can require a larger coordinated module. Reuse an existing standard type when compatible; do not create cardinal/P-label variants of an ordinary straight. Under an exact-layout requirement do not snap a tiny curve to make an extraction fit. Explain the measured limitation, preserve the geometry, and split only proven useful blocks.

### Required line drawing for user-requested atomization

**Atomization** means dividing a larger piece or assembly into smaller, useful, reusable pieces. Whenever a user asks to atomize, split further, or check whether an existing design can be divided, produce and show a coordinate-labelled line drawing with the recommendation. This applies to individual pieces, complete assemblies, analysis-only requests, and reviews concluding that no further useful split is possible. Produce the drawing early enough to explain the proposed work; this requirement does not add another approval step when the user has already authorized that work.

The drawing must let a reader see which track sections are straight, which bend, where a cut is proposed, and why each reviewed cut is feasible, conditional, blocked, or unverified. A textured model preview and a prose recommendation do not supply this line drawing. Use these steps:

1. **Identify the input and coordinate frame.** Name the piece or assembly, identify the reviewed source version or input fingerprints, state the orientation, and show a north arrow, tile boundaries, X/Y labels, and tile scale. A standalone review uses the piece's local grid; an assembly review uses its fixed global grid and placement labels. Show the original reviewed extent before any extraction, and keep its coordinates consistent across alternatives. Label the drawing as a proposal, implemented result, or historical review, as applicable.
2. **Draw the actual routes as lines.** Use saved PATH coordinates when available; explicitly label source-only analysis when saved resources have not been checked. Include every participating route, travel direction, and relevant level or height change. Keep the top view's horizontal and vertical scales equal. Clearly distinguish straight stretches from curved stretches, with an in-picture legend and readable labels or line styles as well as colour. Branch identity alone does not distinguish curvature: a branch can contain a straight stretch, and a straight-looking top view can conceal a necessary slope transition.
3. **Mark the proposed boundaries and outcomes.** Draw candidate cut lines, show the resulting module extents, and put the decision and short reason beside each cut. Where a standard piece can be reused, name its exact type and rotation. Distinguish the recommended arrangement from optional alternatives, and account for retained interior and structural cells. For a large review, use several readable panels on the same coordinate frame rather than covering the tracks with labels.
4. **Show physical obstacles as well as route geometry.** Mark a necessary deck wing, wall, support, shared tile, or slope transition at the affected cut. Add a footprint outline or a small cross-section/detail panel when route lines cannot show the obstacle. Straight traffic paths alone cannot establish that an ordinary straight replaces the complete physical piece. If the visible model has not been checked, mark that cut unverified.
5. **Make small differences explicit.** Print the measured deviation and applicable limit beside an almost-straight candidate. Show any required adjoining correction separately from the candidate's eligibility measurement. Use a labelled close-up when millimetre differences disappear at overview scale; state its scale and any exaggeration. Never straighten the plotted route, hide a physical obstacle, or imply that a tolerance authorizes an otherwise forbidden redesign.

Use the following decision legend, or equally explicit wording, inside the drawing. Do not rely on colour alone, and keep decision status separate from whether a change has been implemented:

| Decision | Meaning for the reader |
| --- | --- |
| **Reusable as is** | The proposed split preserves the current requirements, and the exact replacement and necessary route, physical, and construction checks are established. |
| **Requires bounded redesign** | The split needs a stated local change. Show what changes, its measured or proposed bound, and whether the current user authorization covers it. This is not an unchanged extraction. |
| **Retain** | The candidate cannot be separated under the current requirements. Show the specific measured or structural obstacle. |
| **Unverified** | Required inputs or checks are missing. State what must be measured before deciding; an attractive line fit is insufficient. |

Show the diagram directly in the user review, and persist it with the owning piece or assembly under the shared [atomization review artwork rule](WORKFLOW_DOCUMENTATION_GENERATION.md#atomization-review-artwork). Link the measured decisions and evidence from that subject's existing TESTING document, using chapter 3 for the current analysis and chapter 6 for historical proposals. If the user authorizes an implementation, update or supplement the drawing to identify the final split and its checked inputs. Preserve any retained earlier proposal with its original coordinates and clearly historical scope. A drawing records an explanation; actual saved-resource verification and human game observations retain their separate authority.

## Persist atomization decisions and coordinate parallel work

An **atomization decision** records why a candidate tile can become an existing standard piece, or why it must remain inside a larger module. Keep one authoritative `checks/atomization.json` beside the assembly's placement and quality contracts; keep historical decisions in the assembly's TESTING design-history section rather than adding another Markdown file. Current README titles and render captions describe the current assembly without predecessor-version or atomization-history labels. Distinguish historical eligibility measurements from checks on the current resources. When predecessor subjects are explicitly deleted, keep their useful decision measurements as history and pin the retained assembly with its own `checks/resources.json`; verification must not require deleted definitions, layouts, or DAT fixtures. A reusable type's README links the relevant decision, states its generic connection limits, and explains the useful function that remains.

For each reviewed candidate, record its source type and placement, local and assembly X/Y tiles, original measured deviation, physical deck and wall requirements, decision, plain-language reason, and exact replacement type and rotation. An accepted redesign also records the smallest changed region, actual maximum route movement, independent acceptance bound, support/port policy, compiled evidence, and source fingerprints. A rejected candidate records the measured obstacle and what larger redesign or evidence could justify reconsideration. A real platform wing or a restored wall obstructing passing traffic is a different reason from a curve exceeding a threshold; explain which applies. List all reviewed source cells so omitted interior or structural tiles are accounted for explicitly.

Keep the **eligibility threshold** separate from the **actual redesign bound**. For example, an original 2.058 mm tail can qualify under a strict “less than 5 mm” policy while its adjoining joining curve needs an 8.14 mm correction to meet the existing native-end curvature limit. Record both numbers and their measurement methods. Do not claim that the whole redesign moved less than 5 mm, relax curvature/clearance limits, or silently broaden the allowed cells. An exact-position policy still forbids snapping a curve unless the user has authorized bounded redesign.

When several agents atomize one assembly, first freeze the approved version and its actual compiled resources. Work in a new requested version, with source hashes protecting subjects that the user wants to retain. Assign each geometry family a separate new implementation file and new piece folders; keep identifiers, shared hooks, collection registration, and assembly integration under one coordinator. Have an independent reviewer inspect actual saved resources. Start the final render pass only after every geometry agent has finished and the complete assembly passes its checks. Render the integrated result once; preserve retained versions' images and observations. If the user explicitly deletes earlier subjects, remove their files and exclusive dependencies, preserve useful measurement rationale as history, and verify the retained design against its approved current resource contract. Source fingerprint changes make applicable decision evidence stale until rechecked; they never create a game-test pass.

## Connections, journeys, and human-confirmed checks

Each piece needs its own connection overview, with stable identities, actual positions in canonical local orientation, network services, physical channels and boundary cuts, directed movements and mode permissions, nominal level and exact path height, and actual endpoint heading and slope. Use the shared [connector reference](CONNECTOR_METADATA.md) for complete-boundary comparisons and [overview procedure](WORKFLOW_DOCUMENTATION_GENERATION.md#reading-an-overview) for generation, cards, and freshness checks. Link direct candidate matches and required adapters; existing per-port counterpart shortlists are not an exhaustive compatibility catalogue. A common height or profile name alone does not establish a continuation or physical fit.

Prepare missing or changed types through [WORKFLOW: Piece Creation](WORKFLOW_PIECE_CREATION.md#51-generate-and-check-the-pieces-connector-export-and-overview): verify saved resources, extract current measurements, author source-backed channel associations, and generate the resolved export and canonical cards. Assembly workflows and any separate consumer applications must use that result. Do not create another authoring/parser workflow in the application or hand-copy numerical tables into an assembly as an independent source.

At a proposed join, transform the complete tile-edge segments, member positions, headings, outward grades, models, and owned cells under one common placement. Require every service and required cut on the shared boundary to agree, and check other already occupied neighbours separately. A touching corner, a compatible upper service with a missing lower service, or unrelated placements that fit different groups cannot establish one complete join. Other branches can remain unfinished only where no existing neighbour creates a conflict. Pairwise compatibility does not replace whole-assembly ownership, construction, journey, or clearance checks.

Each assembly declares every permitted directed journey for every participating transport, plus forbidden level transfers and unintended crossings. For example, HSR, tram, and future conventional rail checks are separate even when their game resource identifiers overlap. Every real journey needs travel demand, compatible end connections, the observations required by its declared test plan, and the tested orientation and platform. When the plan includes both Route Query and visible travel, each needs its own observation; neither proves the other. A pretty render does not establish any journey.

Each subject's `checks/manual-tests.json` is its sole observation record, including exact case scope and current or stale states. Use [TESTING.md](TESTING.md) for the common interpretation and recording procedure. Only an explicitly confirmed matching human observation can create a manual pass. Keep the assembly's coverage distinct by service, directed journey, pose, rotation, and tested environment; preview approval and software checks do not confirm game traffic. Recheck the affected whole traffic graph after a route change, rather than only the edited member, and report the actual covered cases.

## Compact documentation ownership

Follow [WORKFLOW: Documentation Generation](WORKFLOW_DOCUMENTATION_GENERATION.md#readme-layouts-and-generated-sections) for the split piece and assembly README/TESTING layouts, generated-block ownership, inventories, and preservation checks. Intentionally retained legacy piece guides remain combined until explicitly refreshed. Keep source-specific design decisions and measurements with the owning subject; shared presentation and regeneration rules stay in that workflow.
