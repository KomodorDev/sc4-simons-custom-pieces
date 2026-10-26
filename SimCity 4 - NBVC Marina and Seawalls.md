# NBVC Marina and seawalls

**Installed and checked — 14 September 2026.** NBVC Marina, Modular Marina AddOn, Marina Round Corners, all required supporting files, and PEG CDK Leveler are installed. Plop and Paint's catalogue has been rebuilt successfully. File and catalogue checks passed; placement inside a city remains untested.

A **seawall** is an artificial edge between land and water. These NBVC pieces provide a concrete waterfront using your city's existing sea or river. A **lot** is a complete placeable item occupying one or more map squares; one map square is also called a **tile**.

## What is installed

| Download | What it provides |
|---|---|
| [NBVC Marina](https://community.simtropolis.com/files/file/28951-marina/) | The main seawalls and 12 pier choices. Start here for a straight concrete waterfront. |
| [Modular Marina AddOn](https://community.simtropolis.com/files/file/29045-modular-marina-addon/) | Diagonal seawalls and piers assembled from separate sections. |
| [Marina Round Corners](https://community.simtropolis.com/files/file/29870-marina-round-corners/) | Rounded waterfront corners and additional piers. |
| [PEG CDK Leveler](https://community.simtropolis.com/files/file/4527-peg-cdk-leveler-v205/) | Temporary lots for making a level strip of land before placing waterfront pieces. |

The two NBVC additions need models from the main Marina download. A **model** supplies an object's visible shape. The main download supplies those models; no separate third-party scenery pack is listed as a requirement.

The updated Marina sets also need **Submenus DLL**, the add-on that groups menu entries. It is installed in your Windows game setup. One official copy of **Marina Submenu.dat** has also been installed separately because the current sc4pac packages omit it.

The Leveler was extracted from your [Pegasus CDK3 Collection](https://community.simtropolis.com/files/file/35353-pegasus-cdk3-collection/) download. Only its Leveler data file was installed. You do not need to run that collection's Windows installer.

## Find the pieces

The original menu files define this path:

1. Click **Transportation → Water Transportation → Waterfront**.
2. Click **NBVC Marina Main → Modular Marina Menu**.
3. Choose **Modular Marina Base Set** for the main walls, **Modular Marina Addon Set** for the diagonal additions, or **Modular Marina Round Corners Set** for rounded turns.

These exact names and their connections were checked in the files; their display inside the running game still needs confirmation. Four individual pier/corner lots have no custom submenu assignment in the original downloads, so use the search panel below if you cannot find a particular piece here.

For the Leveler, look in the **Parks** menu: its files classify both sizes as parks. The search panel is also available.

You can also use your existing search panel. Its catalogue is already refreshed:

1. Open **SimCity 4 Windows** from your desktop and enter a city.
2. Press the letter **O** to open **Advanced Plopping & Painting**.
3. Select **Buildings & Lots**. Use this category to place complete wall lots with their grounds.
4. Click the search field and type **Marina Seawall**. For a straight section, select **Marina Seawall** and check that its description says **Marina seawall. 1x1**. This lot's internal name is **NBVC_MarinaWall1**.
5. Inspect the preview and choose the lot's **Plop** option. **Plop** means place the selected lot yourself.
6. Move the placement preview to the shoreline. Before clicking, check that the concrete edge faces the water and the paved part meets the land.
7. To rotate the preview, hold **fn / 🌐** and tap **←** or **→**. Click once to place the piece when the game permits it.
8. Press **Escape** when you have finished placing that piece. Press **O** again to close the panel.

The panel name, category and Plop controls follow your existing [Plop and Paint guide](</Users/simonhinterreiter/Documents/SimCity 4 Windows/Plop and Paint - How to use it.md>). The straight, diagonal and rounded seawall names and both Leveler names were found in the rebuilt catalogue.

Useful additional names are **Marina Seawall Diagonal**, **Marina Rounded Inner Corner**, and **Marina Rounded Outer Corner**. Some choices share a display name. Read the description and inspect the preview to distinguish left and right corners or decorated versions.

## Prepare a short waterfront first

**Do not assume these walls automatically stretch to fit any cliff height.** NBVC recommends PEG's Leveler to obtain suitable land height beside the water. The [author's reply](https://community.simtropolis.com/files/file/28951-marina/?page=2&tab=comments) does not give a required height in metres.

Use a short, empty shoreline for your first attempt so that you can see whether the wall fits before extending it.

1. Open **Buildings & Lots** as described above and search for **Leveler**.
2. Select **PEG Leveler (1x4)** for the smaller trial area. The other choice is **PEG Leveler (4x4)**; the numbers describe the number of tiles it covers.
3. Move the preview to the empty shoreline. Rotate it so that its **orientation arrow points inland/uphill**, away from the water. Check the area it covers, then click where the game permits placement. This arrow direction is specified in the Leveler's own tooltip.
4. Select the game's **Bulldoze** tool and remove the temporary Leveler lot. The terrain adjustment remains after the lot is removed. If the game will not let you place a new lot on that cleared area, use the **De-Zone** tool to remove the remaining zoning; the Leveler's tooltip identifies this as a possible extra step.
5. Select a straight Marina seawall lot and try placing it along that prepared edge.
6. Inspect the result: the paved top should meet the land, the wall should face the water, and there should be no exposed beach strip between the wall and the intended waterfront edge.
7. If the fit is satisfactory, repeat with neighboring straight wall pieces. Check that their tops meet at the same height before building a long stretch.

The Leveler is a temporary placeable lot. Its author documents the place-then-bulldoze method and the two sizes, but does not supply a universal numerical waterfront height. Its tooltip uses the opposite arrow direction—downhill—for inland leveling. Final waterfront alignment needs a test in your city. [Leveler instructions](https://community.simtropolis.com/files/file/4527-peg-cdk-leveler-v205/)

## Installation checks and future changes

The installed NBVC sets contain **58 lots**, **74 model files**, and **74 description files**. All 206 files match the original downloads. One matching menu file and the Leveler file, containing both sizes, bring the total to **208 new files**. sc4pac now manages **169 packages**; all 162 previous package records and 2,036 existing plugin payloads were retained unchanged.

The catalogue rebuild completed successfully with **879 buildings, 2,349 lots and zero parsing errors**, including all 60 new lots. It generated 875 building thumbnails, compared with 815 before this installation. The four missing thumbnails predate this work. The old HSRP Transit Hub is still present in the catalogue.

Installation records and backups are in [setup/nbvc-marina](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/nbvc-marina>). The separate menu support is at `Plugins/700-transit/NBVC Marina - Menu Support/Marina Submenu.dat`. Keep one copy if updating these packs manually; it is outside sc4pac's tracking.

For later mod changes, close the game, double-click **Rebuild SimCity Content** on your desktop, click **Rebuild**, wait for **Finished**, and click **Close** before starting the game again. This refreshes the search catalogue; it does not reshape your shoreline.
