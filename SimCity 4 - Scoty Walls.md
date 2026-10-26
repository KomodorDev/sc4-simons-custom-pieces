# Scoty Walls Sets

Installed on 16 September 2026. sc4pac tracks the pack as **local-scoty:walls-sets**, version **1.2.0**, in the **Local additions** channel. All 210 wall lots are present in the rebuilt O-menu catalogue. No walls have been placed in your city, and no city terrain or roads were changed.

## Find and place a wall

1. Start **SimCity 4 Windows** and load your city.
2. Press **O** to open Plop and Paint.
3. Select **Buildings & Lots**.
4. Click **Clear filters** so a previous size or building-type filter does not hide the walls.
5. In **Search buildings...**, type **Concrete Wall**.
6. Select **Concrete Wall - straight** in the upper results table.
7. Select its lot in the lower table, then click **Plop**. A lot is the piece of land occupied by the selected object.
8. Move the placement preview over an existing terrain slope. The wall follows the slope; it does not create the lowered ground for you.
9. Orient the orange arrow toward the higher side of the slope, as the author's guide specifies. Check the preview before clicking to place it.

The regular game menu location is **Parks → Embankment**. Searching through O is usually easier because the pack contains many pieces with similar names.

Other useful searches are **Granite Wall**, **Brick Wall**, **Sandstone Wall**, **Rubble Wall**, and **Retaining Wall**.

## Stairs down to the park

Search **Concrete Wall**, then select one of these entries:

- **Concrete Wall - Straight stairs**: a 1 × 1 pedestrian stair lot.
- **Concrete Wall - Stairs & ramp**: a 2 × 1 pedestrian lot.

Their files contain pedestrian transit connections. The word “ramp” in the second name refers to the pedestrian lot; it is not a road ramp for cars. These pieces are suitable candidates for connecting the upper district to a lower park, but their placement and connections still need checking in the game.

## Installation details and limitation

The installation includes all mandatory dependencies listed by the author, plus Girafe Wheat, which supplies two additional plant objects used by the lots. The version 1.2 ZIP omits its under-bridge prop file, so that original file was recovered unchanged from the author's version 1.1 ZIP. Current wall lots and submenu patches were retained.

Five unidentified small prop references remain unresolved on **10 of the 210 lots**. A prop is an object placed on a lot, such as a plant, fence or street fixture. The affected pieces are four concrete diagonal/end variants, four brick diagonal/end/scene variants, one granite end variant and one retaining-wall diagonal variant. Their small footprints suggest decoration or fixtures; their exact identities are unknown. The missing references also occur in version 1.1 and are absent from the complete listed dependency archives.

Ordinary concrete straight walls, intermediate pieces, and both stair sizes have no unresolved lot references. Main wall textures are supplied. These are file and catalogue checks; an in-game visual test has not been performed. The precise affected lot IDs are recorded in `setup/scoty-walls/review/remaining-five-prop-impact.json`.

## Management and verification

Use sc4pac to manage or remove **local-scoty:walls-sets**. Its newly added dependencies are tracked automatically. Keep this project's **setup/sc4pac-local-channel** folder: it contains the preserved source archives and local package metadata needed for reinstalling. Future releases by the author require importing updated files into this local channel.

Installation added 16 managed packages and 350 files. All 2,346 prior non-catalogue plugin files were verified unchanged. The catalogue contains 1,104 buildings and 2,574 lots, including every one of the 210 new wall lots, with zero parsing errors. The scanner continues to skip the game's unrelated `unins000.dat` uninstall data, as it did before this installation.

Profile and catalogue backups are in **setup/scoty-walls/before-20260916-203222-c50c61**. Detailed checks are in **setup/scoty-walls/installation-verification.json**.

## Western business-district access

My recommendation is to keep the existing north–south tunnel as a through route and connect the business district through the western surface road network. The compactness problem includes the tunnel mouths, space to turn, and enough road length to climb back to the upper level. Retaining walls improve the appearance of the slope but do not remove the road's climbing distance.

The walls can instead frame the lower north and south parks, with pedestrian stairs leading down from the business district. Keep the HSR loop and the planned tram extension to the south park.

Sources: [Scoty Walls Sets](https://community.simtropolis.com/files/file/35922-scoty-walls-sets/), the included author PDF, and the installed [Plop and Paint usage documentation](/Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/plop-and-paint-native/source/docs/USAGE.md).
