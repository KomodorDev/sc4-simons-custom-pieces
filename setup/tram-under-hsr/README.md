# Ground tram beneath HSR — experimental NAM 50 puzzle piece

**Framework update, 18 October 2026:** this piece is now an optional recipe in [Simon's Custom Pieces](../../custom-pieces/README.md), with its own menu icon and an explicit HSR shadow mapping. The old standalone prototype below is retained for regression comparison. Do not stack its controller overlay with the framework.

Built on 18 October 2026 for this project's installed **NAM 50, right-hand traffic** configuration.

This add-on supplies a **new, one-tile crossing**: a visible tram at ground level passes at a right angle beneath NAM's elevated High Speed Rail (HSR). It uses the actual HSR span and the existing ground-tram surface. The upper train paths remain at **15.5 metres**, exactly matching the installed HSR approaches; the ground tram paths remain at **0 metres**.

**Status:** the DAT file has been built and passed static checks. A static check inspects the file's contents without running SimCity 4. Placement, rendering, traffic and demolition have **not** been tested inside the game. The add-on is staged in this project and is **not installed**. Existing Plugins and city saves were not changed.

**Research update, 18 October 2026:** a specific unfinished visual detail has been identified. The five copied resources in group `2BC2759A` are **shadow images**, not map textures. They still describe the narrower Monorail crossing and do not match the wider HSR deck. The game's selection of shadows for the new tile also remains unverified. These need correction; the standalone model preview does not display the game's network shadows. This finding does not establish a traffic failure.

## Files

- [Game add-on](dist/zzz_Custom_Tram_Under_HSR/zzz_Custom_Tram_Under_HSR_NAM50.dat): the file SimCity 4 can load. A DAT is an archive containing game resources.
- [Model preview](dist/model-preview.png): a render of the actual model, not a game screenshot.
- [Verification results](dist/verification.json): completed file checks and the remaining game checks.
- [Build manifest](dist/build-manifest.json): resource list, dependency locations and original-file fingerprints.
- [Model audit](model-audit.json): geometry and material comparisons with the NAM models.

## Install for a test

1. **Quit SimCity 4 completely.** The game reads Plugins when it starts, so copying the file while it is running will not activate the new piece.
2. In Finder, choose **Go → Go to Folder…** or press **Shift + Command + G**.
3. Paste this path and press **Return**:

   `/Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/tram-under-hsr/dist`

4. Select the folder **zzz_Custom_Tram_Under_HSR** and press **Command + C** to copy it.
5. Press **Shift + Command + G** again. Paste this path and press **Return**:

   `/Users/simonhinterreiter/Documents/SimCity 4 Windows/Plugins`

6. Press **Command + V** to paste the folder. Keep its name: its position after the main NAM folder lets the custom placement rules load last.
7. Start SimCity 4 and open an empty test city with a flat construction area.

**Compatibility:** this includes a placement-rule overlay made from the exact NAM 50 controller currently installed. An overlay is a file that supplies a replacement resource when the game loads. Remove this add-on before updating or reinstalling NAM; it must be rebuilt against the replacement controller. The build script refuses to build against a different controller.

## Find the new crossing

1. Open **Transportation → Miscellaneous Transportation**. If the tools are grouped into submenus, open **Ground Lightrail**.
2. Select **Ground Light Rail (Tram)**. This is the older puzzle-piece button; **Draggable Ground Light Rail (Tram)** is a different button.
3. Move the cursor over clear, flat land and press **Tab** to cycle through the pieces.
4. Stop when the cursor description reads:

   **HSR over Ground Tram - Right-Angle Crossing (Experimental)**

   It is inserted immediately after **Ground Light Rail x Monorail Puzzle Piece** in that button's cycle. From the Monorail crossing, one further **Tab** press selects the custom HSR crossing.
5. Rotate the piece with **Home/End**. On your Mac keyboard these are **fn + left arrow / fn + right arrow**.

## Build the crossing

Use a flat, straight crossing at 90 degrees for the first test. The sequence below is a construction plan based on the copied native puzzle-piece rules; it still needs an in-game check.

1. Place the custom crossing on clear ground. Note its two directions: the wide HSR span is above ground; the tram's two tracks run across it on the ground.
2. Build an HSR approach toward each end of the upper span. Use **Transportation → Rail → High Speed Rail**, place an HSR starter on each side of the crossing, and extend each approach with the **Monorail** drawing tool. HSR uses Monorail as its underlying game network.
3. End each drag at the edge of the crossing tile. Preserve the custom piece itself. The add-on does not include rules for dragging through it or for automatically converting track beyond it into HSR; the separate HSR starters supply that conversion on both sides.
4. Select **Draggable Ground Light Rail (Tram)** and place a straight tram starter on each of the two remaining sides of the crossing.
5. Select the normal **Elevated Rail** drawing tool and draw from each tram starter toward the corresponding ground track on the crossing. End at the tile edge. The starters turn those drawn approaches into ground tram.
6. Inspect the result closely. The HSR span should join both HSR approaches, and the ground tram should join both tram approaches. There should be no ordinary Monorail beam and no pillar across the ground tracks.

For an existing HSR line, the initial test should remove its crossing tile and leave a one-tile opening for the custom piece. Keep the surrounding route straight and flat. Whether the piece can be placed directly on an intact HSR/tram tile remains untested.

## Check actual operation

1. Rotate and place four copies in the test area to check all four distinct orientations. The eight menu rotation entries repeat the four directions, matching the original NAM piece.
2. Check both the placed model and the cursor preview at every game zoom level.
3. To check passengers, connect the tram to working tram stations serving homes and jobs. Connect the upper HSR line to functioning HSR stations. Let the simulation run so journeys can develop.
4. Use **Route Query** on the crossing and approaches to inspect routes on both networks. No displayed routes on a line without travel demand does not establish a broken crossing.
5. Check both travel directions. The files contain a path in each direction for both networks, but the game still needs to demonstrate that it uses them.
6. Check rebuilding an adjacent approach and bulldozing the crossing in the test city. These have not yet been verified in the game.

## Remove the add-on

1. While the add-on is still installed, bulldoze any custom crossing pieces you have placed in a city you intend to keep. Reconnect those routes with ordinary pieces as needed.
2. Quit SimCity 4.
3. Remove **zzz_Custom_Tram_Under_HSR** from the Windows profile's Plugins folder listed above.
4. Start the game again. The original NAM placement rules load automatically because the original controller file was never edited.

## What was built

The custom piece has its own resource IDs. It preserves the original GLR × Monorail piece and the ordinary HSR models.

| Component | Implementation |
| --- | --- |
| Crossing model | Ground mesh from NAM's GLR × Monorail tile, plus the actual straight HSR deck rotated 90 degrees |
| Clearance | Lowest point of the upper model is 14.01 m above ground; no pillar is included |
| Traffic | Original crossing paths: tram and driving-mode rail at 0 m; HSR/Monorail at 15.5 m |
| Menu | New entry in the existing Ground Light Rail (Tram) button |
| Previews | Separate preview model and copied preview effect with unique references |
| Zooms | Five model variants using the existing NAM ground textures |
| Placement rules | Original installed RUL0 resource with one ordering entry and eight new puzzle definitions added; every original byte is recoverable unchanged |
| Automatic dragging rules | None; this version is a static puzzle piece |

The package contains **16 resources**. The file is about **4.7 MB**, mostly because SimCity 4's RUL0 placement rules are loaded as one resource. A separate puzzle piece requires an overlay of that whole resource. The other NAM rule resources are not included or replaced.

The original HSR model contains five animation records that reference buffers absent from that model. The composed model retains its valid deck record and removes the dangling records. Its triangle references, materials, textures and texture coordinates have been checked.

## Rebuild and verify

Run these commands in Terminal, one at a time:

```sh
cd '/Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City'
python3 setup/tram-under-hsr/build.py
python3 setup/tram-under-hsr/verify.py
```

The build uses your installed NAM assets. It writes only inside this project's `setup/tram-under-hsr/dist` folder. It checks for custom resource-ID collisions in installed Plugins and requires the exact audited controller. If this prototype is already installed, remove its copied Plugins folder before rebuilding; otherwise the collision check will correctly detect it.

The model preview can be regenerated with:

```sh
python3 setup/tram-under-hsr/render_preview.py
```

The checks cover the archive structure, rule preservation, model and preview references, all five zoom models, texture dependencies, and matching HSR path endpoints in all four rotations. They do not substitute for the game checks above.

## Credits and references

Historical checks found that the idea was discussed during HSR development: on [16 March 2006, smoncrie identified the same GLR × Monorail models and preview used as this prototype's starting point](https://community.simtropolis.com/forums/topic/8934-high-speed-rail-project/?page=9&tab=comments). Old [NAM cleanup lists](https://community.simtropolis.com/omnibus/simcity-4/reference/nam-network-addon-mod-cleanitol-list-r380/) also name HSR-over-GLR support and shadow-fix files. The names establish historical patches, but do not establish their contents, functionality, or reason for removal.

The [official HSR guide](https://www.sc4nam.com/docs/feature-guides/high-speed-rail/#known-issues) documents crossings reverting to Monorail or behaving incorrectly when built too close to HSR curves. Keep the first test on a straight section. The guide also distinguishes missing draggable support from crossings that can be supplied as static puzzle pieces. Neither the historical material nor the source audit established a blanket prohibition on separate ground-tram tracks crossing beneath elevated HSR.

The original HSR and tram models, textures, paths, previews and construction rules are NAM Team assets from the user's installed NAM 50 distribution. This is a local derivative prototype, not an official NAM release. Resource IDs were checked against the current installation; they have not been reserved with the NAM Team for public distribution.

- [Official NAM source repository](https://github.com/NAMTeam/Network-Addon-Mod)
- [HSR guide](https://www.sc4nam.com/docs/feature-guides/high-speed-rail/)
- [Tram guide](https://www.sc4nam.com/docs/feature-guides/light-rail-tram/)
- Source rule template: `Controller/RUL0/B000_Lightrail/B110_GLR.txt`, piece `B12F`.
- Model parser reference: the local DBPFKit `S3DReader.cpp`.
