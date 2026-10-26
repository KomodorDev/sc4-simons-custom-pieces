# Elevated HSR crossing diagonal ground HSR — experimental NAM 50 piece

**Framework update, 18 October 2026:** further development now lives in [Simon's Custom Pieces](../../custom-pieces/README.md). Its coordinated builder supports multiple pieces and separate SCP menu icons. This standalone prototype is retained for regression comparison; do not install it alongside the framework's shared controller overlay.

Built on 18 October 2026 for the installed Windows SimCity 4 / NAM 50 setup.

This adds one selectable crossing: **straight elevated High Speed Rail (HSR)** passes over **diagonal Ground High Speed Rail (GHSR)** at a 45-degree angle. Each railway has paths in both directions. The upper train paths stay at 15.5 metres; the lower paths stay at 1 metre. This is a crossing, with no connecting ramp or interchange between the two lines.

**Status: built and checked outside the game; not installed.** Binary checks and a software model preview cannot establish that placement, train routing, shadows, and demolition work in the game. First use a disposable test city.

![Preview of the actual packaged model](dist/model-preview.png)

The image renders the real packaged geometry with the installed NAM textures. It is not a SimCity 4 screenshot. Its two construction tiles occupy a 1 × 2 tile rectangle; native diagonal track geometry extends beyond the tile edges in the same way as the original NAM diagonal GHSR models.

## Files

- `dist/HSR-over-diagonal-GHSR-NAM50-experimental.zip`: installation package.
- `dist/zzz_Custom_HSR_Over_Diagonal_GHSR/zzz_Custom_HSR_Over_Diagonal_GHSR_NAM50.dat`: the game add-on. A DAT is an archive of resources that SimCity 4 loads.
- `dist/model-preview.png`: preview of the actual model.
- `dist/verification.json`: independent static-check results.
- `dist/build-manifest.json`: source fingerprints, resource list and limitations.

No existing NAM file, Plugins folder, saved city, or mod-manager record was changed.

## Install for a test

1. In SimCity 4, save any city you want to keep, return to the region, and quit the game. The game reads add-ons when it starts.
2. In Finder, click **Go → Go to Folder…**.
3. Paste this path, then press **Return**:

   ```text
   /Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/hsr-over-diagonal-ghsr/dist
   ```

4. Select the folder **zzz_Custom_HSR_Over_Diagonal_GHSR**. Press **Command + C**.
5. Click **Go → Go to Folder…** again. Paste this path and press **Return**:

   ```text
   /Users/simonhinterreiter/Documents/SimCity 4 Windows/Plugins
   ```

6. Press **Command + V**. The copied folder must sit directly inside Plugins, alongside the `770-network-addon-mod` folder. Do not put it inside NAM's mod-manager-controlled folder. Do not copy the source scripts, the whole `dist` folder, or the ZIP file into Plugins.
7. Start **SimCity 4 Windows.app**. Open a disposable test city with flat, empty land.

This add-on was built for the exact installed NAM 50 controller. **Remove it before updating NAM.** It also overrides the shared construction-menu and shadow-mapping resources. Other manual add-ons overriding those same resources need to be merged with it. In particular, do not install the earlier staged `zzz_Custom_Tram_Under_HSR` prototype at the same time without a combined build. No conflicting custom controller overlay was installed when this piece was built.

## Find and place the piece

1. Open **Transportation → Rail → Ground High Speed Rail (GHSR)**.
2. Move the pointer over flat, empty land. Press **Tab** until the description is:

   **HSR over Diagonal GHSR - Straight Upper Track (Experimental)**

   The custom entry is immediately after the existing **GHSR x HSR** crossing in that button's sequence. Use the description to identify it. **Shift + Tab** cycles backward. If the sequence behaves unexpectedly, select the GHSR button again and restart the search.
3. Rotate the preview with **Home / End**. On your Mac keyboard these are **fn + left arrow / fn + right arrow**. The sequence includes both mirrored diagonal directions. If a quarter-turn does not give the required diagonal, continue cycling the variants with **Tab** and check the preview.
4. Place the piece on clear, flat land. Start with the piece itself, so you can see exactly where its four outside connection ends are. Do not start by forcing a Monorail drag through the crossing.
5. At each of the **two upper ends**, build a straight elevated HSR approach. Use an **HSR starter**, then the ordinary **Monorail** drawing tool to extend that approach to the edge of the custom piece. Stop at the piece; do not draw through it.
6. At each of the **two lower diagonal ends**, build a diagonal GHSR approach. Use a **GHSR starter**, then the ordinary **Monorail** drawing tool to extend the approach to the appropriate edge of the piece. Again, stop at its edge.
7. Use a starter on each separate approach as necessary. This is a fixed puzzle piece; it does not automatically convert the approaches into HSR or GHSR. Keep the first approach sections straight or diagonal as shown by the piece, and put bends farther away.

The base orientation has two construction tiles in a column. The upper railway runs through both tiles. The lower railway enters the west side of the lower tile and leaves the east side of the upper tile. Rotating or mirroring the piece changes those compass directions.

## Check it in the test city

1. Inspect all four connection ends for gaps and sudden changes in height.
2. Rotate the game camera and change the zoom. Check that both decks are visible and that no support pillar blocks the lower line. Check the shadows in the game; they are not displayed by the software preview.
3. Give each line a real passenger trip, with compatible stations and a reason for Sims to travel between their origins and destinations.
4. Run the simulation. Use **Route Query** on each approach and check that passengers cross on both lines and in both directions. An empty route query does not prove the piece is broken if there is no travel demand. Check that trains stay on their own level rather than transferring to the other line.
5. In the disposable city, test removal with the **NAM Eraser** and check that the two crossing cells and their shadows can be removed. A clean test-city demolition does not modify your main city.
6. Check rotated and mirrored placements before relying on one in a city you want to keep. Saving and reopening the test city is another useful check.

These are the remaining in-game checks, not claims that they have passed.

## Remove the add-on

1. While the add-on is still installed, remove its crossing pieces from any city you intend to keep. Save those cities and quit the game.
2. In Finder, open the Windows Plugins folder shown above.
3. Move **zzz_Custom_HSR_Over_Diagonal_GHSR** out of Plugins.
4. Restart the game. The original NAM files were never edited, so the original menu and shadow mappings load again when this overlay is absent.

## Technical construction and verification

- The two-cell placement, eight rotations/mirrors, and same-network connection flags come from NAM's native `AAC1` railway-over-railway underpass. Only the underlying network name changes from Rail to Monorail.
- The diagonal ground models and paths come from native `C219`, retaining their two-tile alignment exactly. The upper deck and paths come from native straight HSR. Model buffers, including texture coordinates, are preserved.
- The two-height Monorail path-format convention comes from native `GHSR x HSR`. No path changes height, and no interchange paths are added.
- Explicit shadow mappings reuse the existing straight HSR shadows in the same orientation as the upper deck. No placeholder Monorail shadow images are copied into this add-on. Actual selection and appearance need checking in the game.
- The construction menu and NetworkINI overlays preserve all original bytes apart from the reversible additions. The build is pinned to the installed NAM 50 controller fingerprint and checks for identifier collisions.
- The staged tile identifiers are `5DD0F200` and `5DD0F210`; the preview is `5DD0F225`; the puzzle identifier is `F7A1`. These are not needed to use it.

To rebuild and check the staged files, open a terminal in this project folder and run these commands in order:

```sh
python3 setup/hsr-over-diagonal-ghsr/build.py
python3 setup/hsr-over-diagonal-ghsr/verify.py
python3 setup/hsr-over-diagonal-ghsr/render_preview.py
python3 setup/hsr-over-diagonal-ghsr/package.py
```

The build and verifier use Python's standard library and the existing project DBPF/model helpers. The preview renderer also uses NumPy and Pillow, which are available in the current local Python environment. No command installs the add-on.

Original models, textures, paths, effects and rules: **NAM Team and its contributors**, including the native crossing rules attributed to ebina. This is a private local experimental derivative, not an official NAM release.
