# Tokyo hub — installed buildings

Prepared 13 September 2026 for your **SimCity 4 Windows** profile, with NAM 50, right-hand traffic, CAM and standard Maxis night lighting.

## Find and place the buildings

1. Open **SimCity 4 Windows** from your desktop and enter a city.
2. Press **O** to open **Advanced Plopping & Painting**.
3. Select **Buildings & Lots**.
4. Search for a name from the table below. Use a short word such as **Tokyo**, **Yunika**, **Daiwa**, **Toranomon** or **Emperador** if the complete name gives no results.
5. Select the desired building and lot. A **lot** is the complete parcel, including the building and its immediate grounds. Choose the lot's **Plop** option, move the preview onto clear land beside a suitable street or avenue, and click to place it.

| Building | Installed choices | Size in game squares |
|---|---|---|
| Tokyo Central Station | APTX version 2.0, right-hand traffic paths | 19 × 13 |
| PC Yunika Building Shinjuku | Alpen Tokyo, Alpen Sports and Labi; all three include growable and directly placeable versions | 2 × 4 |
| Mattb325 Daiwa House Tokyo | Maxis night version; commercial office growable, also available through Plop and Paint | 4 × 4 |
| Toranomon Hills Station Tower | Office building with an avenue passing through its lot | 13 × 5 |
| Cobb Emperador Hotel | Existing installed hotel from the Cobb collection | 4 × 4 |
| Xyloxadoria Modern Arched L2 HSR Station | Existing elevated HSR station | Choose the matching elevated lot |
| Xyloxadoria Modern Diagonal L2 HSR Station | Existing diagonal elevated HSR station | Choose the matching diagonal lot |

With your Submenus DLL, the directly placeable Yunika shops are also under **Commercial zoning → Ploppable CS$$**. Here **CS$$** means medium-wealth commercial services, including shops.

**Growable** means the game can construct the building on appropriately zoned land when demand and other conditions allow. **Ploppable** means you can select and place it yourself. Daiwa House does not add its own ordinary Landmarks-menu button.

## Connect Tokyo Central Station

With your Submenu DLL, look for the station under **Transportation → Misc-Transit → Multi-Modal Stations**. Plop and Paint is an alternative way to find it.

1. Place the station on flat land, leaving space at both ends for the tracks.
2. Find the station's main entrance/front facade.
3. The **three track routes nearest the front** use the **Elevated Rail** tool. They are for elevated light rail, not ordinary ground-level railway.
4. The **two rear routes** use **HSR/Monorail**. Connect your elevated HSR approaches using the Monorail drawing tool and the NAM HSR starter as usual.
5. Open the subway view. Find the concrete **1 × 1 square near the centre** of the station and draw a subway line through it.
6. Provide street access to the station. It also includes bus service.

The station costs **§35,000** to place and **§1,722 per month** to maintain. Its documented capacity is **560,000**. The installed custom track paths are at **15 metres** elevation.

Toranomon Hills is an office destination; it does not handle HSR or subway passengers. Its original lot has a small **100-unit transit capacity**, so keep the district's busiest avenue alongside the building instead of relying on the avenue through its lot as the main traffic route. The author's original lot statistics were retained.

## Installation and updates

- **sc4pac manages:** Daiwa House, RR Mega Prop Pack Vol. 2, PEG MTP Super Pack and BSC MEGA Props MISC Vol02, in addition to your existing packages.
- **Installed manually because no matching current package was found in your channels:** Tokyo Central Station, Yunika, Toranomon, and two selected supporting scenery files from the Moonlight and RDQ collections.
- Those two supporting files supply the required planter and tree props. No old Moonlight network replacements were installed.
- Your existing BSC Textures Vol02 supplies the remaining BSC texture needed by Toranomon.
- BSC MEGA Props MISC Vol02 supplies a timed crowd effect used by Yunika that was absent from the author’s dependency list.
- If these manual buildings become available in sc4pac later, remove their manual duplicates as part of that migration.
- After future additions, close the game and use **Rebuild SimCity Content → Rebuild**, then wait for **Finished** before playing.

Source archives, exact file hashes, installation manifests and dependency audits are retained in the project's `setup/tokyo-hub-install` folder. The pre-install sc4pac configuration is backed up under `setup/backups/Before Tokyo hub - 2026-09-13 210941`.

## Original downloads

- [Tokyo Central Station](https://community.simtropolis.com/files/file/27630-tokyo-central-station/)
- [PC Yunika Building Shinjuku](https://community.simtropolis.com/files/file/37457-pc-yunika-building-shinjuku/)
- [Daiwa House, Tokyo](https://community.simtropolis.com/files/file/34025-daiwa-house-tokyo/)
- [Toranomon Hills Station Tower](https://community.simtropolis.com/files/file/37097-toranomon-hills-station-tower/)

File and dependency checks passed. The refreshed catalogue contains **660 buildings and 2,130 lots**, with **zero parsing errors** and previews for all 660 buildings. All new building names are present in the catalogue. The only indexing warning is the existing GOG uninstaller database, which is not game content.

The new station and lots have not yet been placed or tested inside a running city.
