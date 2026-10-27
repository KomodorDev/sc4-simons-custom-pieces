---
title: "High-speed rail player guide"
summary: "Choose, place and test the current HSR/GHSR pieces, then find the individual-piece instructions or complete assembly blueprint without opening several overlapping guides."
audience: "Rail players and authors"
document_type: "guide"
---

# High-speed rail player guide

**HSR** means elevated High Speed Rail; **GHSR** means Ground High Speed Rail. Both carry the game's Monorail traffic. A **piece** is one separately selectable construction button. An **assembly** is a documented arrangement of several placed pieces; the trumpet is an assembly. A **collection** is a named selection of existing pieces used when building the plugin, not an extra game button.

Each piece has one README containing its preview, measured connection interfaces, and human observations. The **[Straight-stem HSR trumpet](01_assemblies/straight-stem-trumpet/README.md)** has a four-section overview and a separate testing reference. Its assembly menu has one button, with Tab and Shift+Tab cycling through the reusable components. Design history and measurements remain in its TESTING document.

The library's [connector reference](../../docs/CONNECTOR_METADATA.md) explains complete shared boundaries, physical channels, measured positions, and permissions, with the modular crossing and tight curve as its final examples. Their generated overview cards live beside those two pieces. Authors use the shared [generation procedure](../../docs/WORKFLOW_DOCUMENTATION_GENERATION.md); other types retain their existing measured connection views until intentionally migrated. A displayed route candidate remains separate from physical fit and an observed game connection.

The current library does not supply automatic compatibility discovery. Most existing pieces are not yet migrated to the new connector-export format; that absence establishes neither compatibility nor incompatibility. Ordinary piece validation does not generate a manual test for every possible neighbour.

<!-- BEGIN COLLECTIONS -->

## Inventories and collections

- [Individual pieces: 165 menu types](00_pieces/INVENTORY.md).
- [Assembly blueprints: 1 design](01_assemblies/INVENTORY.md).

<details>
<summary>Named build collections</summary>

A collection selects existing piece types; it is not an additional piece or a one-click assembly.

- `hsr-crossings`: 4 piece types.
- `diagonal-s-curves`: 4 piece types.
- `adjacent-switches`: 4 piece types.
- `mixed-level`: 1 piece types.
- `rail-expansion`: 9 piece types.
- `rail-interchanges`: 114 piece types.
- `oneway-levels`: 48 piece types.
- `oneway-branches`: 48 piece types.
- `oneway-grades`: 8 piece types.
- `true-flyovers`: 10 piece types.
- `revised-rail-junctions`: 2 piece types.
- `flagged-junctions`: 32 piece types.
- `junctions-needing-review`: 32 piece types.
- `redesigned-junction-example`: 1 piece types.
- `redesigned-diagonal-junction-example`: 1 piece types.
- `smooth-t-junctions`: 2 piece types.
- `hsr-all-components`: 33 piece types.
- `hsr-modular-connection-parts`: 3 piece types.
- `hsr-split-and-climb`: 2 piece types.
- `hsr-crossing-core-and-approaches`: 3 piece types.
- `hsr-compact-fan-parts`: 2 piece types.
- `hsr-straight-stem-trumpet`: 14 piece types.

</details>

<!-- END COLLECTIONS -->

## Choose the right family

A **port** is a track entrance or exit at the edge of a piece. Its height, heading, width and permitted direction must match the neighbouring piece. **Paired** means two tracks carrying opposite directions; a **one-way** port has one centred track for one direction. A narrow one-way end cannot join one lane of ordinary paired HSR directly: use a compatible split, merge or spacing adapter. The [rail connection contracts](NETWORK_SPEC.md#connection-levels-and-piece-families) give the exact heights and widths.

| You want… | Choose… |
| --- | --- |
| A line carrying trains in one direction | One-Way GHSR, HSR L2, Rail L3 or Rail L4 track and curves |
| A branch leaving or rejoining a paired line | A matching GHSR or HSR L2 Split/Merge; select the required angle and Compact/Wide variant |
| A branch within the upper narrow network | Rail L4 Split/Merge; its mainline is also single-track |
| A change of one-way track height | A directed One-Way … to … Ramp with matching entry and exit levels |
| Separate upper and lower routes on the same tile | A combined crossing containing both routes |
| A same-height full T | [Straight smooth T](00_pieces/directional-hsr-t-smooth-at-grade/README.md) or [diagonal smooth T](00_pieces/directional-hsr-t-smooth-diagonal-at-grade/README.md) |
| A railway that shifts sideways while staying diagonal | HSR/GHSR Diagonal S-Curve Left/Right |
| A transfer between two neighbouring paired mainlines | Adjacent Crossover Left/Right or Adjacent Scissors Revised |
| A paired change between HSR and GHSR | HSR to GHSR Transition |
| Reusable upper paired track, graded corners, spacing adapters or compact connections | The `hsr-all-components` collection in the inventory |
| The complete modular trumpet | The [assembly README](01_assemblies/straight-stem-trumpet/README.md) and `hsr-straight-stem-trumpet` collection |

A 45°, 90° or 135° branch angle describes the change in heading. Wide modular branches have at least twice the sampled minimum radius of their Compact counterparts, so they require more land. A larger **radius** means a gentler curve. Use the exact footprint in the piece README; a diagonal half-tile and a complete diagonal pair are not interchangeable in every layout.

The [menu legend](../../docs/BUILD_AND_INSTALL.md#recognize-scp-menu-icons) explains the icon colours and abbreviations. Teal **PART** identifies components, while purple **PNP** identifies the two separately placeable complete smooth T junctions. A complex assembly blueprint does not add a whole-assembly PNP button. Current Plop & Paint does not stamp these network blueprints; use the documented constituent pieces.

## Build a selected collection

Open a terminal in `custom-pieces`, the directory containing `scp.py`, and run:

```sh
python3 scp.py list
python3 scp.py doctor
python3 scp.py build --set smooth-t-junctions --output dist/smooth-t-junctions
python3 scp.py verify --output dist/smooth-t-junctions
```

This example builds the two accepted smooth T pieces. Repeat `--set` to combine collections, or use `--include EXACT-PIECE-ID` for one exact inventory identifier. These options replace the default selection; `--all` selects every current piece. Building and verifying create and check staged files. Follow the separate [build/install guide](../../docs/BUILD_AND_INSTALL.md) to install them.

A managed SCP installation has one combined controller and menu for its complete selection. Installing a component-only selection replaces the previous managed selection; it does not add to it automatically. Include every SCP piece you want to retain when choosing a collection to install.

## Place and rotate pieces

1. Save and fully quit SimCity 4 before changing Plugins. Follow the installation guide, then open a disposable test city with flat, clear terrain.
2. Open **Transportation → Rail**. Hover over an **SCP** icon to read its exact title, then click that button once.
3. Move the construction preview over clear land. Press **Home** or **End** to rotate before placing. On the keyboard used for this installation, **Fn + ←** and **Fn + →** produce those keys.
4. **Tab** and **Shift+Tab** select the next or previous type within a declared construction family. The ordinary piece-compilation stage keeps types separate. Every assembly delivery uses [one assembly button](../../docs/BUILD_AND_INSTALL.md#prepare-the-assembly-menu), with Tab/Shift+Tab selecting its member types; the final menu step hides duplicate member buttons and preserves unrelated standalone types. **Home** and **End** cycle rotation states. Directional pieces repeat four proper rotations: 0°, 90°, 180°, and 270°. Rotation turns the whole piece and its travel directions together; it does not turn a split into a merge or produce a 45° shape. Choose a separate diagonal or opposite-handed piece when needed.
5. Keep the whole declared **construction rectangle** clear, including unused cells. It is the area reserved around the construction reference position. A gap in a software preview is not a promise that a road or building will fit there; native-width concrete can extend beyond occupied network cells.
6. Check the port heights, profiles, headings and arrows, then click once. Place matching narrow fillers end to end: ordinary Monorail dragging does not extend narrow SCP track. Stop native two-track construction drags at the outside boundary of a compatible piece.
7. Where two routes share a tile, use a combined crossing that contains both levels. Placing an independent upper filler on a lower railway can replace the lower route.
8. Connect stations through compatible native paired lines. Authored narrow ports or upper heights do not establish direct compatibility with native stations, bridges or neighbour connections.
9. Supply travel demand, inspect the game's route query and moving trains, and test every permitted direction. Repeat relevant rotations, demolition and save/reload checks. Use the piece README's test section and the shared [observation guide](../../docs/TESTING.md) to record the exact result.

## One-way branches and height changes

A **split** allows trains to leave a mainline; a **merge** accepts that branch onto a mainline. GHSR and HSR L2 split/merge mainlines retain both travel directions. L4 branch mainlines are also one-way. A return journey needs its own permitted path.

For a simple branch, select **SCP | HSR L2 Split 90 Degree Compact**. Its base orientation has a north/south paired mainline and a branch leaving northbound traffic toward the east. Keep its 2 × 2 construction rectangle clear, place it, then join native paired HSR to the two mainline ends. Select **SCP | One-Way HSR L2 Straight**, rotate its arrow eastward and place it against the branch. To receive that branch at another mainline, use **SCP | HSR L2 Merge 90 Degree Compact** rotated 180°: its west entry accepts the eastbound branch and joins southbound mainline traffic. Check the actual ports before clicking, then test both mainlines and the permitted branch journey.

Use matching ground pieces for a GHSR branch. Use the exact **… to …** ramp name for a height change; rotation changes its heading, not the direction of ascent along its one-way journey. The [network height table](NETWORK_SPEC.md#connection-levels-and-piece-families) lists the four available levels and ramp lengths. A spacing adapter changes the track arrangement at one height and cannot replace a height ramp.

### Worked example: an HSR branch above GHSR

This five-piece example leaves a paired HSR line, climbs to L4, crosses a lower GHSR line, descends and joins another paired HSR line. The lower line is part of the combined crossing. Its encoded-route tests cover the 32 combinations of four rotations and GHSR/HSR choices at the start, finish and lower crossing; those software results do not establish game operation.

The coordinates below describe the software test fixture's construction rows, not the X/Y display grid of an interchange picture and not literal mouse-click positions. They are tile-centre positions. Call the first split's upper-left construction cell `(0, 0)`; count columns eastward and rows southward. Sparse pieces can have an empty construction reference cell, so align their visible ends and occupied cells before clicking.

| Step | Exact name after `SCP \|` | Construction reference | Orientation and occupied cells |
| --- | --- | --- | --- |
| 1 | HSR L2 Split 90 Degree Compact | `(0, 0)` | Paired north/south mainline; branch east |
| 2 | One-Way HSR L2 to Rail L4 Ramp | `(9, 0)` | Arrow east; low west, high east; columns 2–9 on row 0 |
| 3 | One-Way L4 over GHSR Crossing | `(10, 0)` | Upper arrow east; columns 10–12 on row 0; lower GHSR north/south through column 11 |
| 4 | One-Way Rail L4 to HSR L2 Ramp | `(20, 0)` | Arrow east; high west, low east; columns 13–20 on row 0 |
| 5 | HSR L2 Merge 90 Degree Compact | `(22, 1)` | Rotate 180°; west entry accepts the branch; cells `(21, 0)`, `(22, 0)`, `(22, 1)` |

Place the pieces in table order. Join the ramp's low west end to the split's eastern branch; connect the lower GHSR only to the crossing's middle cell. Join the descending ramp to the merge's west entry. Extend compatible paired HSR away from the split and merge. The branch journey runs from split to merge; it does not permit a reverse journey.

For a ground-level start, use **GHSR Split 90 Degree Compact** and add **One-Way GHSR to HSR L2 Ramp** before the climb. For a ground-level finish, add **One-Way HSR L2 to GHSR Ramp** after the descent and choose the ground merge. Those added ramps lengthen the corridor; do not reuse the five-piece positions unchanged.

## Two-track S-curves, switches and transitions

**HSR to GHSR Transition** joins paired elevated and ground lines across an eight-tile straight gap. Its base orientation has HSR at the north end and GHSR at the south; rotate 180° to exchange those ends. Connect matching native paired track at each outside edge. It does not join a centred one-way port.

A **diagonal S-curve** shifts a railway sideways while its entry and exit remain parallel. Select **HSR/GHSR Diagonal S-Curve Left/Right**, choose the matching level and shift, then rotate to the incoming diagonal. Keep the 3 × 3 rectangle clear and place the complete four-cell piece. Its construction reference cell is empty; do not fill unused cells with ordinary Monorail. Extend compatible native diagonal track at both ends and verify that the outgoing line stays parallel to the incoming one.

**Adjacent mainlines** here means two paired lines in neighbouring tile columns, with no empty column between them. Leave a three-tile-long break in both lines, select the matching HSR/GHSR **Adjacent Crossover Left/Right** or **Adjacent Scissors Revised**, align its two north/south mainlines with those columns, and place the whole 2 × 3 block. Rotate for east/west lines and connect all four outside ends. Both original mainlines continue through the block.

A **crossover** transfers trains in one handed arrangement; a **scissors** combines both arrangements. In the base orientation, name the left line A and the right line B. Right allows A northbound → B northbound and B southbound → A southbound; Left allows the other two transfers. Scissors allows all four. A transfer retains its travel direction and is not a U-turn. Test the selected transfers and through traffic on both lines. There is no diagonal scissors or same-size switch between adjacent lines at different heights; those need different authored pieces.

Ground GHSR can pass under elevated HSR using a combined crossing. Passing below GHSR itself requires underground or tunnel pieces, which this kit does not implement.

## Reference sheets and current limitations

These family sheets supplement the canonical preview in each piece README. They do not replace its exact port connections or current test status.

| Reference sheet | What it shows |
| --- | --- |
| [HSR/GHSR crossing matrix](assets/figures/crossings/matrix.png) | The four grid/diagonal alignment combinations |
| [One-way branches](assets/figures/one-way/branches.png) | Split, merge and branch shapes |
| [Flyover levels and crossings](assets/figures/flyovers/levels-and-crossings.png) | Upper/lower route arrangements |
| [Diagonal S-curves](assets/figures/s-curves/diagonal.png) | Sideways diagonal shifts |
| [Menu icon examples](assets/figures/menu/icon-contact-sheet.png) | Category colours and lower-band abbreviations |

The saved [design review](junction-design-review.json) covers 130 current pieces: 32 modular branches/crossovers need support-spacing review, and 98 have no objection recorded under that bounded review. No current piece has a NEEDS REDESIGN verdict. The two smooth T pieces have their own independent audits. Review flags remain visible in the inventory, affected piece READMEs/previews and newly built menu titles/tooltips; a software pass does not clear a flag.

Software checks examine encoded directions, matching 3D endpoints, connected seams, model clearance, supports, shadows and construction rules. They do not confirm placement, moving trains, long-car overhang, terrain, demolition or save/reload. In particular, same-network routes sharing a tile edge at different heights need game testing to ensure trains stay on their intended level. The [network specification](NETWORK_SPEC.md) defines the numerical checks and supported NAM profile; the [observation guide](../../docs/TESTING.md) explains the separate human checkmarks.

For new layouts or atomizing reusable modules, follow the [assembly-design workflow](../../skills/network-assembly-design/SKILL.md). That workflow owns grid, image-labelling and review rules; this player guide does not duplicate them.
