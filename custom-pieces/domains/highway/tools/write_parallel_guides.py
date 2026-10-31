#!/usr/bin/env python3
"""Write the new parallel-kit player guides, preserving every generated block.

Only the fifteen parallel piece guides and their new assembly guides are in
scope. Existing retained assemblies, measurements, images, and observations
are never rewritten by this authoring helper.
"""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'framework'))
from scp import jsonc

SUBJECT = 'ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond'
ASSEMBLY = ROOT / 'domains/highway/01_assemblies' / SUBJECT
PARTS = 'custom-pieces/dist/ddrhw-parallel-diamond-parts-01'
MENU = 'SCP | ASSEMBLY | DD RHW-4 — Parallel Diagonal Avenue Diamond'
NAV_TEST = ('[1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · '
            '[3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · '
            '[5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)')
BLOCK = re.compile(r'<!-- BEGIN ([A-Z ]+) -->.*?<!-- END \1 -->', re.S)


def preserve_write(path, text):
    current = path.read_text() if path.exists() else ''
    blocks = {match[1]: match[0] for match in BLOCK.finditer(current)}
    text = BLOCK.sub(lambda match: blocks.get(match[1], match[0]), text)
    final = text.rstrip() + '\n'
    if final != current:
        path.write_text(final)


def metadata(title, summary, audience='contributors', kind='reference'):
    return ('---\n' + '\n'.join(f'{key}: {json.dumps(value, ensure_ascii=False)}' for key, value in
            (('title', title), ('summary', summary), ('audience', audience), ('document_type', kind))) + '\n---\n\n')


def block(name):
    return f'<!-- BEGIN {name} -->\n\n<!-- END {name} -->'


def display_cells(piece, pose):
    x, y = pose['display_origin_tiles_en']
    return ', '.join(f'(X{x + c}, Y{y - r})' for c, r in piece['cells'])


def details(piece):
    key = piece['geometry_key'].removeprefix('parallel-')
    lower = key.startswith('lower')
    height = '7.5' if lower else '15'
    deck = 'lower L1' if lower else 'upper L2'
    direction = 'off-ramp' if '-exit-' in key else 'on-ramp'
    if key == 'crossing':
        return ('This is the central crossing of both straight highway decks over the diagonal ground Avenue. L0 means the ground pavement at 0 m, L1 is the lower deck at 7.5 m, and L2 is the upper deck at 15 m. The three occupied tiles preserve the native Avenue car and pedestrian routes and the four highway through lanes. The outside-deck upper-ramp turns also cross these city tiles, so their required traffic fragments stay with this owner.',
                'Its sparse 2 × 2 footprint has three occupied corners and an empty local [1,1] corner. That empty corner supplies a temporary placement handle, which the supported NAM DLL removes. It is not a fourth permanent road tile. The highway model stays straight; curved high departures belong to the separate ramp modules.',
                '0 m Avenue; 7.5 m L1; 15 m L2')
    if key.endswith('terminal'):
        side = 'northwest' if key.startswith('northwest') else 'southeast'
        served = 'lower L1' if side == 'northwest' else 'upper L2'
        return (f'This ground terminal joins the {served} on-ramp and off-ramp to the {side} Avenue arm. Each ramp approaches the Avenue at 90° and uses a finite right turn into or out of the adjacent carriageway. A carriageway is the part of a road carrying traffic in one direction. The turn has a 6 m centreline radius, labelled R6; there is no ramp movement across the opposing carriageway.',
                'Its three occupied tiles retain the native two-way Avenue and pedestrian channels. The visible turn models extend above some neighbouring owners, while their traffic fragments remain with the city tile they cross. All three native Avenue cells use adaptive ground textures and retained overlay models. The unused local [1,1] corner is the removable placement handle.',
                '0 m ground Avenue and right-turn pavement')
    if key.endswith('slip'):
        return (f'This straight highway section contains the {deck} {direction} slip-lane service and its native barrier opening. A slip lane is the auxiliary lane leading between a through lane and a ramp. Both highway decks remain completely straight, with their native through routes retained. All curved roadway outside the native highway edge belongs to the separately placed lateral-departure module.',
                'The two occupied cells lie diagonally inside a sparse 2 × 2 rectangle. Its construction reference is an empty corner, so align both occupied preview cells instead of assuming that the reference position is a third tile. Complete boundary cards include both highway levels and every access fragment; matching only the named ramp is insufficient.',
                f'Both highway levels: 7.5/15 m; named access at {height} m')
    if key.endswith('departure'):
        return (f'This separately placed {deck} {direction} contains the curved sideways departure beside the straight highway. Its pavement, 1 m underside, native Jersey barrier profiles, and connecting barrier strips belong to this ramp. The complete lateral transition stays at {height} m and changes position over 17 m measured along the highway axis. It becomes fully parallel before the adjoining grade starts to descend.',
                'One city tile owns this component, but its curved model extends over adjacent slip-lane tiles. That model overhang does not add another traffic owner. Because traffic is stored by complete city tile, this owner also retains the beginning of the neighbouring straight grade route. Its saved traffic edge and its physical flat joining section therefore occur at different places.',
                f'Physical departure at {height} m and 0% grade')
    maximum = '17.911624' if lower else '28.202932'
    length = '44.872251' if lower else '56.185959'
    return (f'This {deck} {direction} contains the straight parallel grade between the flat high departure at {height} m and the ground terminal at 0 m. A grade is height change divided by horizontal distance: 20% means 2 m of height change over 10 m horizontally. Its physical straight run is {length} m, with a maximum source grade of approximately {maximum}%. The profile includes a 2 m change of grade at each end and a final 1 m flat ground collar.',
            'This is a fixed-height transition, not a straight slope that can be repeated to obtain any chosen height. Its visible grade model overhangs neighbouring departure and terminal tiles. Its whole-cell traffic ownership also includes one native highway half, so the model and traffic boundaries differ. The native through PATHs and outside-deck ramp route remain with those owned cells. The visible native highway half and its centre pier instead belong to the adjacent straight slip-lane model through overhang, leaving this component’s physical model as a pure graded ramp.',
            f'Physical grade: {height} ↔ 0 m; saved tile-edge cuts have their measured intermediate heights')


def write_piece(piece, pose):
    directory = ROOT / 'domains/highway/00_pieces' / piece['id']
    name, pid = piece['name'], piece['id']
    description, special, heights = details(piece)
    placement = pose['instance_id']
    x, y = pose['display_origin_tiles_en']
    w, h = piece['footprint']
    assembly_link = f'../../01_assemblies/{SUBJECT}'
    readme = f'''# {name}

Purpose: Place this functional component of the compact parallel diagonal highway diamond and match all of its measured services.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

The canonical angled and north-up pictures show the saved model in its authored 0° orientation. The connector overview identifies complete traffic boundaries. Software images show the authored resources; appearance and travel in the game need their own observations in [TESTING.md](TESTING.md).

{block('PIECE VIEWS')}

## 2. Piece and placement

{description}

{special}

A construction tile is a 16 × 16 m city square occupied by one component. This type owns **{len(piece['cells'])} tiles inside a {w} × {h}-tile rectangle**. Its reference position in the complete assembly is **{placement}: X{x}, Y{y}, at 0°**. Its actual occupied cells on that shared grid are **{display_cells(piece, pose)}**. The [assembly construction picture]({assembly_link}/README.md#1-views) distinguishes thick ownership borders from each real model outline, including overhang.

1. Use the matching parallel-kit build with Windows SimCity 4 and NAM 50 in right-hand traffic, including supported Wine or CrossOver use. See [the build and install guide](../../../../docs/BUILD_AND_INSTALL.md); compiling a build does not install it.
2. Open a disposable, flat test area, and follow the [complete assembly placement sequence]({assembly_link}/README.md#3-placements). The three adaptive pieces are placed P02, P01, and P03 first so each temporary helper corner starts clear.
3. Click **Transportation → Highways**, and select **{MENU}**. Press **Tab** to cycle forward or **Shift+Tab** to cycle backward until **{name}** appears. Each click places only that selected component.
4. Keep the authored 0° orientation for the reference plan. **Home** and **End** rotate the selected preview; use the actual occupied squares to match the table. Four proper rotations repeat across eight selection states, without reflecting traffic handedness.
5. Position the construction reference at **X{x}, Y{y}**, check the occupied cells listed above, and click once. Add the matching components at their own reference positions; never place a second owner on an occupied city square merely because two models overlap visually.

**Physical connection levels:** {heights}. Match exact positions, height profiles, directions, and every boundary service on the generated cards. Matching a visible edge or one road lane alone does not establish a compatible neighbour. These fixed pieces do not adjust to arbitrary terrain heights, and the kit does not establish that native RHW can be dragged through its occupied cells.

{block('PIECE OVERVIEW')}

## 3. Connection matrix

Read from an entrance row to an exit column. A saved PATH is the traffic data stored in the game resource. Route Query is the route shown by the game, and Visible travel is an observed car or pedestrian completing it. The matrix describes this component's intrinsic fragments; the complete journey can pass through another component's city tile even when its physical model is visibly continuous. Physical joining sections and saved traffic cuts are checked separately.

{block('PIECE CONNECTION MATRIX')}

{block('CONNECTOR OVERVIEW')}
'''
    testing = metadata('Testing: ' + name, 'Check this parallel component against its saved resources and retain separate human game observations.') + f'''# Testing: {name}

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · {NAV_TEST}

## 1. Test scope

This record covers **{pid}**, used once as **{placement}** in the [parallel diamond]({assembly_link}/README.md). It has {len(piece['cells'])} occupied tiles in a {w} × {h} rectangle, the exact authored 0° reference at X{x}, Y{y}, and the functional levels described in the [piece guide](README.md#2-piece-and-placement). Saved native through routes, added access fragments, actual model support, material flags, physical joins, rotations, and adaptive resources where present have distinct software checks. Human appearance and travel observations remain separate.

{block('CONNECTIONS')}

## 2. Test setup

Use Windows SimCity 4 with the pinned NAM 50 right-hand-traffic inputs, including through Wine or CrossOver. The shared [build guide](../../../../docs/BUILD_AND_INSTALL.md) owns private input settings and explicit installation. Use the complete fifteen-component assembly for travel tests: this individual component can expose required route fragments at more than one city-tile edge. A matching-looking isolated end is insufficient to create the whole journey.

Prepare the [assembly's flat reference test area]({assembly_link}/TESTING.md#2-test-setup), keep the camera north-up for placement, and use the exact occupied cells **{display_cells(piece, pose)}**. The full core occupies 31 cells inside X1–X8 and Y1–Y8; the preserved drawing reference still shows X0–X9 and Y0–Y9. One tile is 16 m. Additional outside road approaches are separate from that core count.

## 3. Software checks

Run from the repository directory containing `custom-pieces/`. These commands inspect an existing build and its current source-bound connector records; they do not install anything, supply missing inputs, or approve a manual case. An absent or failing report is not a software pass.

```sh
python3 -B custom-pieces/scp.py verify --output {PARTS}
python3 -B custom-pieces/scp.py connectors check --domain highway --piece {pid} --build dist/ddrhw-parallel-diamond-parts-01
python3 -B custom-pieces/scp.py docs-check --piece {pid}
```

The [complete saved-assembly check]({assembly_link}/TESTING.md#3-software-checks) checks this component in all fifteen placements, including physical model overhang and the traffic fragments owned by its neighbours. The ordinary build's manifest and verification report identify the actual measured resources. Retain every software failure with its source fingerprint; rerunning a renderer cannot repair it.

## 4. Game checks

1. Select this exact component through the assembly button, match {placement} at **X{x}, Y{y}**, and confirm that the occupied preview squares match **{display_cells(piece, pose)}** before clicking.
2. Place the full assembly using the order in its guide. Inspect this component's saved model from both opposing oblique views, and compare its real join with the neighbouring models; look for gaps, blocked barrier openings, misplaced supports, or a sudden pavement-colour patch.
3. Repeat fresh placement in the four distinct proper rotations. Rotate the camera separately after placement, because camera movement and a newly rotated piece test different things.
4. For an adaptive Avenue cell, connect ordinary Avenue outside the core, add nearby development, and check its pavement variant. Then check pedestrian Route Query and visible walking separately; a sidewalk image does not create a pedestrian PATH. For a component without Avenue cells, inspect the neighbouring adaptive owners instead of expecting this piece to change pavement itself.
5. Run every required car and pedestrian journey listed by the exact matrix. Record Route Query and visible travel separately. Also confirm that every declared forbidden transfer stays unavailable; a visually clear road surface is not traffic evidence.
6. Inspect shadows, demolish the component, replace it, save the city, quit completely, and reload. Check that no temporary placement handle remains and that the component and its traffic neighbours remain correct.

Record only explicit observations through [the shared observation workflow](../../../../docs/TESTING.md), selecting **{pid}** and its exact current cases. No observation of the older adaptive probe, R40 diamond, or another rotation automatically approves this new component.

## 5. Results and known issues

The implementation is experimental. The generated records below are authoritative for the current evidence scope; **all new human game observations remain unverified** until the user confirms their exact cases. In particular, outside native DD RHW connections, over-Avenue placement, Avenue redraw, temporary-handle collision behaviour, pedestrian pavement variants, moving traffic, camera rotations, demolition, and save/reload require game checks.

The whole-cell traffic partition is intentionally different from the physical model split. {special} This is a limitation to understand when choosing replacement modules, not permission to discard a required boundary service.

{block('MANUAL SUMMARY')}

{block('MANUAL CHECKS')}

## 6. Design history

This new type implements one functional part of the human-approved close parallel layout. It preserves the [frozen source proposal](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/TESTING.md#32-close-parallel-ramps-and-perpendicular-avenue-approaches) and leaves the retained R40 and compact assemblies available with their own resource identities and evidence. This piece's exact source is [piece.jsonc](piece.jsonc); the shared placement plan is [assembly.jsonc]({assembly_link}/assembly.jsonc).
'''
    preserve_write(directory / 'README.md', readme)
    preserve_write(directory / 'TESTING.md', testing)


def write_assembly(scene, pieces):
    title = scene['title']
    rows, placements = [], []
    for pose in scene['placements']:
        p = pieces[pose['piece_id']]
        path = '../../00_pieces/' + p['id']
        rows.append(f'| [![{p["name"]}: angled view]({path}/previews/preview-thumb.png)]({path}/previews/preview.png)<br>[Top view]({path}/previews/preview-top.png) | **[{p["name"]}]({path}/README.md)**<br>`{p["id"]}` | {pose["instance_id"]} | 1 | {len(p["cells"])} |')
        x, y = pose['display_origin_tiles_en']
        placements.append(f'| {pose["instance_id"]} | {p["name"]} | X{x}, Y{y} | 0° | {display_cells(p, pose)} | {details(p)[2]} |')
    readme = metadata(title, 'Place fifteen functional modules forming a close parallel double-decker diamond in 31 occupied tiles.', 'players', 'guide') + f'''# {title}

[1. Views](#1-views) · [2. Pieces](#2-pieces) · [3. Placements](#3-placements) · [4. Connection matrix](#4-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

This modular blueprint crosses a diagonal ground Avenue with a completely straight NAM double-decker RHW-4 highway. The lower deck is 7.5 m above ground and carries traffic southwest; the upper deck is 15 m high and carries traffic northeast. Each deck retains its two through lanes. Four 6 m-wide ramps move sideways at deck height, run close and parallel to the highway, descend or climb, and meet the Avenue through separate 90° right-turn terminals.

The kit uses **15 reusable types, 15 placements, and 31 occupied tiles inside an 8 × 8-tile rectangle**, or **128 × 128 m**. Each parallel ramp centre is 12 m from the highway axis, leaving a **1 m road-edge gap** between its 3 m half-width and the native highway's 8 m half-width. The drawing retains X0–X9 and Y0–Y9 from the earlier blueprint; this smaller layout occupies X1–X8 and Y1–Y8, without resetting the reference grid. Outside approach roads are additional to the 31 core tiles.

One Highways-menu assembly button cycles through the components: **Tab** moves forward, **Shift+Tab** moves backward, and **each click places one component**. This is a fixed-height experimental kit; source compilation, installation, and observed game behaviour are separate stages recorded in [TESTING.md](TESTING.md).

| Ramp | Traffic arrives from | Traffic leaves towards |
| --- | --- | --- |
| Lower off-ramp | Northeast highway approach, lower deck | Northwest Avenue arm |
| Lower on-ramp | Northwest Avenue arm | Southwest highway arm, lower deck |
| Upper off-ramp | Southwest highway approach, upper deck | Southeast Avenue arm |
| Upper on-ramp | Southeast Avenue arm | Northeast highway arm, upper deck |

Ramp traffic uses only the adjacent Avenue carriageway, meaning the lanes carrying traffic in one direction. There is no turn across the opposing carriageway. The Avenue remains two-way, with its native pedestrian routes retained.

## 1. Views

These six canonical pictures follow the HSR trumpet's exact order: clean top, clean southeast, named top, named southeast, named northwest, and construction overview. P01–P15 identify the same placements in every named picture; full menu names, colours, badges, and leaders retain that mapping. X increases east/right, Y increases north/up, and one tile is 16 × 16 m.

![Clean north-up view of the close parallel diamond](previews/overview-top.png)

![Clean southeast view showing both highway decks and the close parallel ramps](previews/preview.png)

![Named north-up view identifying all fifteen placements](previews/named-top.png)

![Named southeast view with the same fifteen placements](previews/named-southeast.png)

![Named northwest view of the fifteen components from the opposite side](previews/named-northwest.png)

![Construction overview showing translucent ownership over the actual top-view models, with distinct model outlines](previews/tile-ownership.png)

The construction view places translucent ownership colours over the actual compiled top view. Thick boundaries show the city squares occupied by each component. Separate coloured outlines follow its real model projection, including parts drawn over another component's tile. This **model overhang** does not create a second owner or a second traffic resource in that square. It also does not establish vertical clearance by itself.

The [implemented atomization drawing](previews/parallel-atomization.png) shows the saved traffic lines, structural obstacles, ownership borders, and selected functional cuts separately. The curved high departures belong to P08–P11, the straight graded ramp models to P12–P15, and the ground right turns to P02/P03. The native highway remains straight. Whole-tile traffic ownership requires native highway PATH fragments inside the grade components and small outside-deck upper-turn fragments inside P01; those necessary services cannot be replaced by an unchanged generic highway tile.

## 2. Pieces

Each visible thumbnail opens that type's full angled picture; **Top view** opens its north-up view. Standalone pictures show the authored 0° orientation. Every row is used once in this layout, and the table order is the assembly button's forward cycle.

| Standalone angled picture | Exact menu name and permanent piece ID | Placement | Quantity | Occupied tiles |
| --- | --- | --- | ---: | ---: |
{chr(10).join(rows)}

A **slip lane** is the auxiliary lane between a highway through lane and a ramp. A **lateral departure** is the flat curved section moving that ramp sideways. A **grade** is height change divided by horizontal distance: 20% means a 2 m change over 10 m horizontally. The grade modules are fixed transitions from 7.5 m or 15 m to ground, with approximately 17.91% lower and 28.20% upper peak slopes; they cannot be repeated indefinitely to choose arbitrary heights. Each R6 terminal turn has a 6 m horizontal centreline radius. These compressed experimental dimensions are not real-road design standards.

## 3. Placements

Prepare a flat disposable test area before following this reference plan. Choose an empty city square southwest of the junction as the picture’s **X0, Y0** square. Count city-tile steps right for X and up for Y; for example, P01’s X4, Y5 reference is four steps right and five steps up from that chosen square. These are blueprint coordinates, not coordinates displayed by the game. The 8 × 8 core uses the positions below; leave additional room outside its Avenue and highway ends for approach tests. All placements use the authored **0°** orientation. **Home** and **End** rotate the selected component, while **Tab** and **Shift+Tab** choose a different component. Match the actual occupied preview squares, especially where the construction reference lies in an empty corner. The software reference does not establish an observed mouse-click anchor for the new pieces.

1. Click **Transportation → Highways**, and select **{MENU}**. Press **Tab** once from P01 to P02, and place **P02** at **X3, Y6**. Press **Shift+Tab** to return to P01, and place **P01** at **X4, Y5**. Press **Tab** twice to select P03, and place **P03** at **X5, Y4**. This sequence leaves each adaptive component's unused helper corner clear during its first placement; occupied-neighbour handling is a separate game test.
2. Cycle forward to P04–P07, and place the four straight slip-lane sections at their table positions. Their 2 × 2 bounding squares contain only two diagonal occupied cells; the reference corner itself is empty.
3. Place P08–P11, the four separate curved high departures. A departure can share a reference coordinate with a slip section while owning a different square. The preview's actual occupied cells decide ownership.
4. Place P12–P15, the four parallel grade sections. Their physical models extend into adjoining components' tiles, but their occupied cells do not overlap. Inspect the layered construction picture before placing any replacement.
5. Select **Transportation → Roads → Avenue**, and extend the exposed northwest and southeast Avenue ends outward. Start at an outside end, and drag away from the core. For the first test, leave the centre as placed; drawing a new Avenue through the whole core and placement over a prebuilt Avenue are separate tests. Check native DD RHW-4 approaches against every required deck boundary before adding the highway ends; matching only one level is insufficient.

| Placement | Exact component name | Construction reference | Rotation | Actual occupied cells | Physical levels |
| --- | --- | --- | --- | --- | --- |
{chr(10).join(placements)}

The three adaptive 2 × 2 components use their unused local **[1,1]** corner as a temporary Road placement handle. NAM's supported DLL removes that helper; it is not permanent construction ownership. The native Avenue texture can respond to surrounding development, while the retained models supply the highway and ramp geometry. Visible sidewalks, pedestrian routes, Avenue redraw, and moving cars are distinct checks; none is approved merely because another one works. See [the exact game test sequence](TESTING.md#4-game-checks).

{block('ASSEMBLY CONNECTION MATRIX')}
'''
    # Preserve the generated chapter heading if already produced; otherwise
    # ensure the scaffold still has its required fourth chapter.
    readme = readme.replace(block('ASSEMBLY CONNECTION MATRIX'), '<!-- BEGIN ASSEMBLY CONNECTION MATRIX -->\n\n## 4. Connection matrix\n\nThe generated matrix records exact saved journeys and separate game observations.\n\n<!-- END ASSEMBLY CONNECTION MATRIX -->')
    testing = metadata('Testing: ' + title, 'Verify the exact compact parallel diamond while retaining unverified human game observations.') + f'''# Testing: {title}

<!-- ASSEMBLY TESTING LAYOUT: 1 -->

[Assembly overview ↗ (README)](README.md) · {NAV_TEST}

## 1. Test scope

The registered assembly **{SUBJECT}** places fifteen distinct functional types once each. The construction union contains **31 disjoint city tiles inside 8 × 8**, with the exact poses in [assembly.jsonc](assembly.jsonc). Required software coverage includes complete native L1/L2 through traffic, two-way Avenue and pedestrian routes, all four permitted right-turn access journeys, forbidden cross-Avenue transfers, full 6 m ramp pavement, 1 m undersides, native Jersey barrier profiles, physical joining sections, eight piers, texture mapping, adaptive Avenue resources, and all four proper rotations.

{block('CONNECTIONS')}

## 2. Test setup

Use **Windows SimCity 4 with NAM 50 and right-hand traffic**, including supported Wine or CrossOver execution. Native macOS SimCity 4 is outside this DLL-dependent setup. Keep the exact audited DD RHW, MIS, controller, preview donor, and adaptive Avenue capture inputs specified in the [build guide](../../../../docs/BUILD_AND_INSTALL.md). Private paths and captured game files remain local; no native texture images are supplied by these public sources.

A **DAT** is a game-resource archive. An **S3D** resource contains an indexed visible model, and a **PATH** resource contains directed traffic data. Car transport is class 1, and pedestrian transport is class 2. A native Avenue texture supplies visible ground appearance; a rotated retained model supplies elevated highway and ramp geometry. Neither appearance nor a preview establishes a working traffic connection.

For a game test, install only the matching verified selection using the shared build/install procedure, with SimCity 4 fully closed during file replacement. The final component-cycle menu is prepared separately from the ordinary fifteen-piece build. Compiling, verifying, rendering, and packaging do not install files. Preserve the existing R40/compact installations or saved cities independently rather than treating the new identifiers as automatic replacements.

1. Open a disposable city, pause the simulation, and flatten enough land for the 8 × 8 core plus outside approaches. A 14 × 14 flat test area gives three extra tiles on each side; those approach reserves are not part of the 31-cell core count.
2. Use a north-up camera for the first layout. The reference picture labels tile centres **X0–X9** eastward and **Y0–Y9** northward. The occupied core lies at **X1–X8/Y1–Y8**. A 16 m tile's sides lie 8 m from its centre; keep this display grid distinct from the source's columns-east/rows-south coordinates.
3. Follow the [complete placement table](README.md#3-placements), using P02, P01, and P03 first, then P04–P15. The temporary local [1,1] handles are clear in that order. Check the exact occupied squares before every click; two different model silhouettes may overlap without sharing a construction owner.
4. Extend normal diagonal Avenue outward from the northwest and southeast mouths. Match every L1/L2 native DD RHW-4 boundary before testing external highway approaches. The exact native starter/drag sequence and external in-game compatibility still require observation; do not infer them from a software image or one matching lane.
5. Save this fresh reference layout before changing pavement development, testing redraw, or demolishing components. Use separate copies for each destructive test so failures remain reproducible.

## 3. Software checks

Run these commands from the repository directory containing `custom-pieces/`. The first command inspects the existing ordinary build; the second independently checks the saved complete layout, and the third checks current documentation. A missing build or report is not a pass. Successful software checks never record a human game observation.

```sh
python3 -B custom-pieces/scp.py verify --output {PARTS}
python3 -B custom-pieces/domains/highway/tools/verify_parallel_assembly.py --build {PARTS} --output custom-pieces/domains/highway/01_assemblies/{SUBJECT}/evidence/saved-assembly.json
python3 -B custom-pieces/scp.py docs-check --assembly {SUBJECT}
python3 -B tools/run_tests.py
```

The retained ordinary `parts-01` build passed verification for all fifteen pieces. Its [complete saved-assembly report](evidence/saved-assembly.json) confirms the 31-cell union, 124 saved traffic fragments, all four proper rotations, 2,278 continuous car segments, 15,272 ramp-width segments, eight functional physical cuts, and all eight piers. The [visual reassignment proof](evidence/native-visual-transfer.json) retains 106,350 native highway/paint/pier triangles with exact materials, texture coordinates, and winding; the largest additional local-coordinate rounding is approximately 0.548 micrometres, below the strict 2 micrometre limit. A micrometre is one millionth of a metre. The [actual native highway/ramp texture-seam check](evidence/native-wheeltrack-seam-uv.json) separately checks twenty saved joins. These reports identify their exact source manifests and do not supply a human game pass.

Texture coordinates, labelled U and V, select a position within an existing native texture image. The owning verifier reconstructs the exact approved route positions independently of the writer, checks every emitted native/access fragment, and tests the complete layout through four proper rotations. Actual indexed triangles establish continuous car support and intrusion checks, seven longitudinal width lines across each ramp, sampled undersides and barrier profiles, and the eight separately owned physical cuts. Bounded native float32 edge certificates address encoding residuals without broadening the road or moving a PATH. At an external native entrance collar, part of the native road width can lie beyond the owned core and must be supplied by the adjoining highway; the report identifies those bounded omissions while retaining full-width checks for every authored ramp section. Material and texture checks inspect saved flags and UV coordinates, not a renderer's colour choices. Structural load capacity and filtered game appearance remain outside these software checks.

A chord is the straight segment between two consecutive traffic-route points. These PATHs store coordinates to nine decimal places, while the shared connection graph samples them to six decimal places. Its shortest exposed chord is approximately 0.008194499 m, or 8.19 mm, so rounding that small segment can noticeably change its calculated direction. The reviewed `tangent` therefore retains the independently approved source-chord direction; `sampled_tangent` and the signed grade retain the actual shared-engine measurements separately. The [accepted connector measurements](checks/accepted-connector-contracts.jsonc) check all 180 incident full-precision saved chords against their individual nine-decimal coordinate-rounding bounds. The largest reviewed direction-vector error is approximately 7.74 × 10⁻⁸, while the preserved six-decimal sample can differ by approximately 5.43 × 10⁻⁵. No traffic point or shared joining tolerance changes.

Regenerate the supplementary implemented drawing only from a matching saved build, after its checks pass:

```sh
python3 -B custom-pieces/domains/highway/tools/draw_parallel_atomization.py --build {PARTS}
```

The drawing's [PNG](previews/parallel-atomization.png) and [resource provenance](evidence/parallel-atomization.json) retain actual traffic lines, ownership, model projections, structural obstacles, and selected physical cuts. The optional editable `previews/parallel-atomization.svg` is available in a Git checkout; portable source archives include the PNG and drawing generator under the existing export policy. They supplement the canonical six views rather than replacing them. The exact 15-type decomposition is crossing 3 tiles, terminals 3 tiles each, slip sections 2 tiles each, lateral departures 1 tile each, lower grades 2 tiles each, and upper grades 3 tiles each: **3 + 6 + 8 + 4 + 4 + 6 = 31**.

The final assembly-cycle candidate uses layout **parallel-diagonal-diamond** and a separate `custom-pieces/dist/ddrhw-parallel-diamond-menu-final` output, created from a fresh `custom-pieces/dist/ddrhw-parallel-diamond-parts-final` source build after the documentation is frozen. The retained `parts-01` build supplies the measured render and connector provenance above. Follow [Prepare the assembly menu](../../../../docs/BUILD_AND_INSTALL.md#8-prepare-the-assembly-menu) after final documentation is frozen. Its source build and current documents must match; do not combine an older menu candidate with newly edited resources or claim that creating the package installed it.

## 4. Game checks

All game observations below are unverified for this new assembly until the user confirms their exact cases. The older adaptive-sidewalk experiment established its own recorded observations; it does not approve this kit's new placement bounds, new terminal geometry, or new external connections.

1. **Menu and placement:** find **{MENU}** in **Transportation → Highways**. Cycle all fifteen exact names forward with Tab and backward with Shift+Tab. Place each component once using the table, beginning P02 → P01 → P03, and confirm that no temporary Road helper remains.
2. **Occupied neighbours and redraw:** in a separate saved copy, try P02 after P01 has already occupied its helper corner, try the other adaptive owners beside existing pieces, try placement over an already built normal Avenue, and try dragging Avenue through the completed ground corridor. Record each outcome separately; do not count the conservative first sequence as proof of these other behaviours.
3. **Orientation:** repeat fresh placement in all four distinct proper rotations. Confirm that the highway remains perpendicular to the Avenue in each one. Rotate the camera separately after placement, and inspect both sides of the highway, each ramp opening, the small right turns, the eight piers, and all shadows.
4. **Adaptive sidewalks:** first inspect the newly placed Avenue on undeveloped ground. Connect Avenue outside both ends, develop nearby zones until the native pavement variant changes, and compare all three adaptive owners. Check that the highway and ramp overlays remain at the correct angle while the visible ground pavement updates. Record each visible appearance separately from traffic.
5. **Through journeys:** provide matching outside approaches and actual origins/destinations. Check Route Query and visible travel separately for southwest → northeast on L2, northeast → southwest on L1, northwest → southeast on the Avenue, southeast → northwest on the Avenue, and the two pedestrian Avenue directions.
6. **Right-turn ramp journeys:** test northeast highway → northwest Avenue through the lower exit; northwest Avenue → southwest highway through the lower entry; southwest highway → southeast Avenue through the upper exit; and southeast Avenue → northeast highway through the upper entry. Record the query and observed moving car for every route.
7. **Forbidden transfers:** confirm that northeast highway → southeast Avenue, southeast Avenue → southwest highway, southwest highway → northwest Avenue, and northwest Avenue → northeast highway are unavailable. Check that no upper/lower-deck transfer or car/pedestrian transport change appears merely because two models overlap.
8. **Persistence and demolition:** save, quit completely, reload, and repeat representative traffic and pavement checks. In a separate copy, demolish each component, inspect the neighbouring roads for leftover models or removed Avenue cells, replace it, and save/reload again.

Use [the shared observation workflow](../../../../docs/TESTING.md) to record the exact assembly **{SUBJECT}**, its current cases, and the matching source/environment. A visible sidewalk is not a pedestrian-travel pass, Route Query is not visible car travel, and a rotation of the camera is not fresh placement in another orientation.

## 5. Results and known issues

Current generated records below retain exact evidence and observation states. No new human game pass is asserted. Resource compilation, saved route verification, actual model support, source-bound connector cards, and software renders have distinct scopes; none establishes native game placement, sidewalk appearance, external draggable connections, or moving traffic.

The geometry is deliberately compressed. Each high departure moves sideways over 17 m along the highway at full deck height; descent starts only when its complete 6 m width lies outside the native deck. The straight grades are 44.872251 m lower and 56.185959 m upper, with approximately 17.911624% and 28.202932% peak source slopes, respectively. The experimental limit is 30%. The R6 terminals are custom geometry, not a claim that an existing NAM ramp has those dimensions. Fixed grade modules do not acquire arbitrary height offsets or adapt to sloping terrain.

The three-cell crossing is the smallest coherent mixed-network owner in this layout, but it also stores upper ground-turn fragments crossing those same city tiles. The straight grade owners similarly retain PATHs in native highway half-cells traversed by outside-deck access traffic. The visible native halves, their white paint, and their centre piers belong to the adjacent slip-lane models by overhang, so the grade models remain pure ramps and the crossing/slip models form the complete straight highway stem. Consequently, none of the four ordinary highway halves from the wider study is an unchanged full-cell substitute here. Every saved traffic fragment retains one city-tile owner, while each complete curved departure or straight grade model belongs to its functional component and can overhang that boundary.

All nine Avenue cells use native adaptive textures plus retained models. Each sparse 2 × 2 adaptive owner has a removable helper at local [1,1]. The pinned DLL's helper removal does not itself prove that the game will accept every occupied-neighbour cursor situation. Avenue texture variants, redraw, overlay rotation, pedestrians, car transfer between resolved Avenue and fixed highway networks, demolition, and persistence need the focused game tests above.

{block('MANUAL CHECKS')}

## 6. Design history

The human-approved [source proposal](../ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/TESTING.md#32-close-parallel-ramps-and-perpendicular-avenue-approaches) moved the ramps close and parallel to the highway, required perpendicular Avenue approaches, and selected the inward upper sockets. This new assembly implements that approved geometry while retaining the earlier [R40/compact modular blueprint](../ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/README.md) and its frozen evidence unchanged.

The new split follows real functions: central crossing, straight slip sections, flat curved departures, straight grades, and ground right-turn terminals. Minimum construction ownership remains constrained by every complete traffic cell, not only the visible road centreline. The implementation and the [saved-model atomization drawing](previews/parallel-atomization.png) preserve that distinction for future replacement ramps and fixed-height profiles.
'''
    preserve_write(ASSEMBLY / 'README.md', readme)
    preserve_write(ASSEMBLY / 'TESTING.md', testing)


def main():
    scene = jsonc.load(ASSEMBLY / 'assembly.jsonc')
    pieces = {}
    for pose in scene['placements']:
        path = ROOT / 'domains/highway/00_pieces' / pose['piece_id'] / 'piece.jsonc'
        piece = jsonc.load(path)
        pieces[piece['id']] = piece
        write_piece(piece, pose)
    write_assembly(scene, pieces)
    print(json.dumps({'piece_guides': len(pieces) * 2, 'assembly_guides': 2,
                      'generated_blocks_preserved': True, 'manual_observations_changed': False}))


if __name__ == '__main__':
    main()
