# CAM and hospitals — beginner guide

**Installed and checked on 7 September 2026:** CAM 3.1.1, System Integration Module 4.0.1, CAM Ordinances 3.3.0, Cobb, Cerulean and AndisArt building collections, Art Deco and Neo Futurism styles, and both medical additions. sc4pac now tracks **133 packages**, including supporting files. All 15 manual downloads were verified. Content-file checks, the graphical manager, and fresh DLL startup logs passed. The computer-control tool cannot inspect the Wine game window; visual confirmation of the fresh region and hospital placement is still pending.

Your existing game is the **Windows GOG edition running through Wine**, the software that lets this Windows game run on your Mac. This addition retains **1920 × 1200 windowed play, DirectX graphics, the current Wine environment, and NAM 50**. The hospital models use **Maxis Night**, matching the current lighting.

## Start in the fresh region

**CAM** means **Colossus Addon Mod**. It changes how residential, commercial, and industrial development progresses. Its author requires a new region when moving from the original simulation to CAM 3.0 or later. [CAM installation guidance](https://www.sc4evermore.com/index.php/downloads/download/51-colossus-addon-mod).

**CAM - Fresh Start** is prepared as flat land with **four large city tiles**: four separate building areas, each 4 × 4 km, arranged as an 8 × 8 km region. No saved cities were copied into it.

To begin:

1. Open **SimCity 4 Windows** from your Desktop. Wait for the region screen; this installation can take several minutes to start.
2. At the top of the screen, click **Region View Options**, then **Load Region**.
3. Select **CAM - Fresh Start** and load it.
4. Double-click one of its four empty squares. You will enter the terrain-editing view for that city.
5. Leave the land flat for an easy start, or shape it before building. Click **Mayor Mode** to open **Establish City**.
6. Enter a city name and mayor name, select a difficulty, and confirm. For example: city **New Harbour**, mayor **Simon**, difficulty **Easy**.

Use these empty tiles for the CAM start. **Import City** would bring in an older saved city instead. The region and city controls are documented in the [official game manual, pages 10–14 and 25](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/24780/manuals/SIMC4DpcMAN%28ukeng%29_DDAM.pdf).

## What the building packs do

A **growth stage** is a category the simulation uses when choosing which buildings may develop as a region grows. CAM expands this progression. Large towers still need suitable zoning, enough demand, services, transport, and sufficient regional development.

A **growable** is a building that the game constructs on zoned land. The installed **Cobb, Cerulean, and AndisArt collections** supply additional growables, using their CAM versions. You normally build roads, zone homes or businesses, provide services, and let the simulation develop them. Installing a skyscraper pack does not make every tower appear immediately.

Start with an affordable town. Add higher-density residential and commercial zones as demand and infrastructure support them. The two medical additions below are different: you place those yourself from a menu.

## Select Art Deco and Neo Futurism

The installed **Allow More Building Styles 3.6.1** mod expands the architecture-selection panel. **Art Deco** and **Neo Futurism** are additional style choices supplied with this setup; their files connect the styles to compatible buildings.

1. In your city, select **Mayor Mode**.
2. Click **Building Style Control** in the lower control panel. Hover over the control buttons to see their names if necessary.
3. Check **Art Deco** and **Neo Futurism**. For a varied beginner city, also keep **Chicago 1890**, **New York 1940**, **Houston 1990**, and **Euro-Contemporary** checked.
4. Select **Build all styles at once** so the checked styles can grow together.
5. Close the panel and continue playing. These choices control future growth; existing buildings do not instantly change appearance.

The two added names should appear automatically after their style files and the expanded interface are installed. Their settings files are already active. No text-file editing is necessary. If they do not appear, the installation needs checking. [Author's version 3.6.1 documentation](https://github.com/0xC0000054/sc4-more-building-styles/tree/v3.6.1), [Art Deco](https://community.simtropolis.com/files/file/36970-building-style-art-deco/), [Neo Futurism](https://community.simtropolis.com/files/file/36965-building-style-neo-futurism/).

## Place the medical buildings

Patient capacity is the number of patients a facility can serve, **not** the maximum total population of your city.

| Building | Where to look | Size | Published patient capacity |
|---|---|---|---:|
| **Large Modern Hospital** | **Mayor Mode → Civic Tools → Health** | 7 × 6 tiles, or 10 × 10 with parking | **32,000** for either version |
| **Disease Research Center** by Mattb325 | **Mayor Mode → Rewards** | 8 × 6 tiles | **62,500** |

For a hospital, open the **Health** menu, scroll to the two adjacent hospital icons, and hover to identify the compact or parking version. Select one, move it onto suitably flat land beside a road, and click to place it. Both have the same capacity and published coverage radius of approximately **153 tiles**. [Hospital author page](https://community.simtropolis.com/files/file/33034-large-modern-hospital/).

For the research centre, open **Rewards** and look for Mattb325's **Disease Research Center**. It is an additional reward, available without the original reward's unlock requirements; it does not replace the Maxis building. Its published placement cost is **§29,050** and upkeep **§187 per month**. This package selects the medical reward, not its bonus industrial growable. [Research centre author page](https://community.simtropolis.com/files/file/28014-disease-research-center/).

After placing a medical building, use the **Query** tool to click it and check patient numbers and funding as the city grows. The installed hospital files and model references were checked. Menu placement instructions come from the authors; actual placement inside a city remains untested.

## Save first, then leave

The required **Save Warning — Disable Exit & Quit** variant disables the combined **Save and Exit** and **Save and Quit** choices. Use two separate steps:

1. Press **Control + S** inside the game — the **Control** key, not Command. Keep the game in front and wait for the saved confirmation, then click **OK**.
2. Open the game's options and choose to return to the region or quit. Select **Exit Without Saving** or **Quit Without Saving**: your save already finished in step 1.

Avoid making more changes between those steps. The existing 10-minute autosave helps during play, but save explicitly before leaving. [Save Warning author's instructions](https://community.simtropolis.com/files/file/32812-save-warning/).

## Add or update mods later

A **dependency** is a supporting file another mod needs, such as a building model, decorative object, or ground texture. **sc4pac Mod Manager** tracks these relationships for your **SimCity 4 Windows** profile. Keep its supporting packages; deleting them manually can cause missing objects or brown boxes.

After sc4pac finishes adding, removing, or updating building content:

1. Keep SimCity 4 closed.
2. Open **Rebuild SimCity Content** from Applications.
3. Click **Rebuild** and wait for **Finished**. This refreshes Plop and Paint's searchable content list and preview pictures.
4. Start the game. Inside a city, press **O** to open **Plop and Paint**.

The rebuild window reports missing previews if some objects cannot be pictured. Its detailed log is in **Documents → SimCity 4 Windows → Setup logs**. Rebuilding the list does not change your saved cities.
