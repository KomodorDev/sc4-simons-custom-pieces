# Fresh region prepared for CAM

**Status: staged only.** No active region, existing city, game setting, or cache was changed during this subtask. The game was not opened.

The folder **CAM - Fresh Start** contains exactly two newly created files:

- `region.ini`: names the region and selects flat land with `Terrain type = 0`.
- `config.bmp`: an 8 × 8 pixel, uncompressed, 24-bit Windows bitmap. Every pixel has RGB colour `(0, 0, 255)`. Each 4 × 4 blue block describes one large city tile, so the region is **8 × 8 km with four large city tiles**.

There are **zero `.sc4` city files**. No developed or previously simulated city was copied. This is a fresh plains region; the layout bitmap does not encode hills, rivers, coastlines, roads, or buildings.

## Why this is valid

The EA manual documents creating regions with land or ocean terrain and distinguishes untouched city tiles from developed cities. See printed pages 10–13 of the [official SimCity 4 Deluxe manual supplied through Steam](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/24780/manuals/SIMC4DpcMAN%28ukeng%29_DDAM.pdf).

The file method is documented by the original author of Simtropolis's [Creating Area Strip Maps and Multiple SC4 Regions tutorial](https://community.simtropolis.com/omnibus/simcity-4/mapping-terraforming/creating-area-strip-maps-and-multiple-sc4-regions-r85/), Part III. It explicitly describes creating a region folder, `region.ini`, and `config.bmp` outside the game; opening that region produces a plain region with the specified city layout. This is a community author's primary tutorial, not an EA support article.

The bitmap's scale and colour rules are also explained in Wuphon's Reach's original [Creating a Region Layout Bitmap guide](https://wuphonsreach.github.io/blog/2003/01/24/sc4-creating-region-layout-bitmap.html).

The INI section name and settings match the installed Fairview and Berlin examples. The bitmap header, pixel data, file sizes, and absence of city saves were checked locally. **Actual loading in this Wine installation remains untested.** Checksums are recorded in `verification.json`.

## Installation and first use

1. Finish installing CAM and the chosen mods. Keep SimCity 4 closed while installing the new region.
2. Copy the entire **CAM - Fresh Start** folder into `/Users/simonhinterreiter/Documents/SimCity 4 Windows/Regions/`. Do not merge it with another region or replace an existing folder of the same name.
3. Start **SimCity 4 Windows** and wait for the region screen.
4. Open **Region View Options** at the top of the screen, then click **Load Region** and choose **CAM - Fresh Start**.
5. The expected result is four empty large city tiles on flat land. Double-click a tile to enter it. Shape the terrain before establishing the city if desired.
6. To begin building, click **Mayor Mode**, which opens **Establish City**. Enter a city name and mayor name, choose the difficulty, and confirm.

Do not use **Import City** for this fresh start; that would bring in a saved city's state. A mixed land-and-water region would require terrain editing or a separate height-map import. Neither was staged here.

## Rebuild Plop and Paint after changing the mods

The existing helper is `/Users/simonhinterreiter/Applications/Rebuild SimCity Content.app`. With the game closed, open it, click **Rebuild**, and wait for **Finished** before starting the game.

For the parent agent's command-line workflow, the helper runs the following executable with its working directory set to `/Users/simonhinterreiter/Applications/SC4 Plop and Paint Tools`:

```text
/Users/simonhinterreiter/Applications/SC4 Plop and Paint Tools/SC4PlopAndPaintCacheBuilder
```

Its argument list is:

```text
--scan
--game
/Users/simonhinterreiter/Applications/SimCity 4 Windows.app/Contents/SharedSupport/prefix/drive_c/GOG Games/SimCity 4 Deluxe Edition
--plugins
/Users/simonhinterreiter/Documents/SimCity 4 Windows/Plugins
--locale
English
--render-thumbnails
--thumbnail-size
44
```

The working directory is required so the builder can find `PropertyMapper.xml`. The helper checks that the Wine game is closed and exclusively creates `.cache-rebuild.lock` in the tools folder. A direct command-line invocation must also avoid overlapping with a helper rebuild. Raw output normally goes to `/Users/simonhinterreiter/Documents/SimCity 4 Windows/Setup logs/Plop and Paint cache rebuild.log`.

No cache rebuild was performed for this research/staging subtask.
