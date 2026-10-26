# BananaLand V2 — start here

Installed 13 September 2026 for the **SimCity 4 Windows** game.

## Open the region

1. Double-click **SimCity 4 Windows** on your desktop.
2. Wait for the region screen to load.
3. Select **Region View Options → Load Region**.
4. Select **BananaLand V2** and load it.
5. Double-click an empty city square to inspect its land. This opens God mode, the terrain view before establishing a city.
6. Once you have chosen your location, click **Mayor Mode**, enter your city and mayor names, choose the difficulty, and confirm.
7. Save with **Control + S** and wait for the save to finish. Then use **Exit Without Saving** to return to the region, or **Quit Without Saving** to close the game. Your save has already finished at that point; the installed Save Warning mod disables the combined save-and-exit actions.

## What was installed and checked

**City sizes rechecked in the installed files on 14 September 2026:** all 100 city saves are **Large**, the largest standard SimCity 4 city size. There are **zero Medium and zero Small** city saves. Their saved positions form exactly a 10 × 10 grid. [Read-only size verification](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/region-install/audit/installed-city-size-check-2026-09-14.json>).

- **100 large city tiles**, arranged 10 × 10. Each has 256 × 256 building squares, each 16 metres across: 4.096 × 4.096 km per tile and 40.96 × 40.96 km for the saved region. The creator rounds this to 40 × 40 km. Water and mountains count toward that area.
- All 100 tiles contain undeveloped terrain: God mode, zero population, and no saved lots, buildings or transport networks. This is appropriate for beginning new cities with your installed CAM simulation.
- The downloaded archive passed its integrity check. All 102 installed files exactly match it.
- All **431 existing region files** remained unchanged.
- The author's original config.bmp has two extra blue rows beyond the occupied 40 × 40 area. It was retained unchanged with the other source files.
- The game was not launched for this installation; the first visible load and save remain untested.

Installed location: [Bananaland V2](</Users/simonhinterreiter/Documents/SimCity 4 Windows/Regions/Bananaland V2>).

Original download: [Bananaland-V2.zip](/Users/simonhinterreiter/Downloads/Bananaland-V2.zip).

Source: [BananaLand V2 by TheEstGuy](https://community.simtropolis.com/files/file/34670-bananaland-v2-improved-and-expanded/).

## Finding buildable ground

Read-only terrain measurements identified several promising plains, including the tiles stored as **City - New City (98).sc4** and **City - New City (79).sc4**. They have roughly 94% and 90% dry land, respectively. These filenames do not appear as unique city names in-game; the tiles are still named New City internally.

Gentle slopes are not necessarily perfectly level ground. Those two tiles contain broad areas where each individual 16-metre square varies by at most one metre across its corners. A downtown site still needs a close look at the selected area; the measurements do not guarantee a level plateau across the whole city.

## Diagonal bridges — status

NAM 50 and its bridge, road, highway and rail content are installed. The separate **Diagonal Bridge Enabler** is not installed. Its automatic Simtropolis download was blocked. A helper script was drafted outside Plugins, but no construction mode or desktop controls were activated.

The user asked whether a simpler alternative exists before proceeding with that temporary-water method. Do not treat diagonal bridge setup as complete.

The original tool temporarily lowers water and changes road/rail slope rules during construction; removing it and restarting restores the normal settings. The old DLL Toggler only changes that choice at game startup, not while playing.

Sources: [NAM Team's Diagonal Bridge Enabler](https://community.simtropolis.com/files/file/26795-diagonal-bridge-enabler-removes-water/), [startup toggler](https://community.simtropolis.com/files/file/26970-diagonal-bridge-enabler-dll-toggler-read-instructions/).

Verification: [installation record](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/region-install/installation-verification.json>), [terrain and city audit](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/region-install/audit/bananaland-audit.json>).
