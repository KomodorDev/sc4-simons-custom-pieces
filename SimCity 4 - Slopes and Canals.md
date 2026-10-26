# Smoother hills and canals — quick guide

**Installed and checked: 14 September 2026.** Both additions are installed in SimCity 4 Windows. The files and selected slope setting passed checks; placement and behavior inside a city remain untested.

Installed packages: **NAM Tunnel and Slope Mod 0.3.1 — Easy / Steep**, and **BSC SG Remastered Canals 2.0.0-1**. The canals match your existing NAM **CAL** canal support.

## Smoother roads and railway slopes

A **slope** is how steeply a road or track climbs a hill. **Easy / Steep** smooths uneven ground and changes the permitted steepness. It is a forgiving option for hilly cities. There is no new building-menu button: the setting is used when you draw transport networks. [NAM slope guide](https://www.sc4nam.com/docs/feature-guides/tunnel-and-slope-mod/)

1. Open **SimCity 4 Windows** and load your city.
2. Find an empty hillside and select your usual **Road** or **Rail** tool.
3. Click and hold near the bottom of the hill. Move your pointer uphill, then release to build.
4. If the game refuses the climb, start farther from the hill and try again. A longer approach gives the same height change more space, making it less steep.

Loading your city alone does not redraw all existing roads. Expect the effect when building or changing a network. The setting does not change horizontal curve sizes or guarantee that a tight HSR junction will fit.

## Find the new canal pieces

These are artificial canals made from pieces placed on land. For a first build, choose clear, flat land and the standard remastered set.

1. Click **Transportation → Water Transportation → Canals → BSC SG Remastered Canals**.
2. Select a straight canal-edge piece, move its preview onto the land, and click to place it. Repeat to extend the edge.
3. To rotate a piece before placing it, hold **fn / 🌐** and tap **←** or **→**.

The neighboring **BSC Zero7 Sunken Canals** submenu contains the sunken alternative; start with **BSC SG Remastered Canals** for this example. These submenu names were checked in the downloaded package; the in-game menu still needs confirmation.

**Search fallback:** press the letter **O** to open **Plop and Paint**, choose **Buildings & Lots**, click the search field, and type **CAL**. Select a matching canal lot to place. A **lot** is a placeable item occupying one or more map squares.

## Make a canal carry passengers

The decorative edges provide its appearance. **CAN-AM**, NAM’s canal transport system, provides the working route. [NAM canal guide](https://www.sc4nam.com/docs/feature-guides/canals/)

1. Place two parallel canal walls, leaving at least **one map square between them**: **wall | transport | wall**, at least **three squares wide** overall.
2. Open **Transportation → Miscellaneous Transportation** and find the **CAN-AM** pieces. Place connected transport pieces along the space between the walls.
3. Place **two matching NAM canal passenger ferry terminals** along that route. Align each with a wall, with its placement arrow facing the canal. Connect the land side to your streets and supply electricity.
4. Include a **90° bend, T-junction, or + junction** in the connected canal route; NAM documents these as necessary for visible canal boats.
5. Let the simulation run. Passenger use depends on whether the route helps people reach their destinations. [NAM canal construction and stations](https://www.sc4nam.com/docs/feature-guides/canals/#building-canals)

Use the existing NAM canal terminal for this example. The selected scenery package does not imply that extra passenger terminals or new ferries for natural rivers and the sea have been installed.

## Installation record

Both main additions and their declared supporting packages are managed by sc4pac. The profile contains **162 managed packages**; all previous 139 installed-package records remain unchanged. Only the **Easy / Steep** slope variant is active, and its two files exactly match the official ZIP. NAM 50’s Street tunnel support remains installed.

The official **BSC_Canals_Submenu.dat** was added separately because the canal package omits it while its lots request that menu. Keep it in `Plugins/660-parks/BSC Canals - Menu Support`. The 12 managed canal scenery files match the original archive. This is the CAL remastered set and its Zero7 extension; the other BSC canal scenery families are not included.

For future mod updates, close the game before opening **sc4pac Mod Manager**. The separate menu support file is recorded in the [installation verification](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/slopes-and-canals/installation-verification.json>), with a fingerprint so it can be checked against future releases.

Plop and Paint was refreshed successfully: **819 buildings, 2,289 lots, zero parsing errors**. CAL canal names and the restored HSRP hub are present in the catalogue. There are 815 building previews; four missing previews were already present before this installation.
