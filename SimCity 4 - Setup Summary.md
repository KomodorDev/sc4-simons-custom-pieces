# SimCity 4 — setup summary

General setup last checked: **13 September 2026**, Europe/Berlin. Display, zoom, additional stations, slopes, canals, and NBVC Marina checked and documented: **14 September 2026**.

**Display and zoom: start with the [complete repair guide](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/SimCity 4 - Display and Zoom Fixes.md>).** It explains the working resolution and Mac fullscreen settings, faster zoom drawing, one-step two-finger scrolling, the hidden helper, remaining external-monitor limitation, and how to undo each change.

Your Mac runs the **Windows, 32-bit GOG edition of SimCity 4 Deluxe**, including Rush Hour, through Wine. It is configured for **1920 × 1200 windowed play**, with **Network Addon Mod 50**, twenty-two game DLL mods, and the **sc4pac graphical mod manager**.

You confirmed that the game starts successfully at the higher resolution. The Region Thumbnail Fix log also confirms that its patch loaded.

The previously requested essential mods and **SC4 Plop and Paint** remain available. CAM now supplies the fixes that replaced the older Opera House, high-tech jobs, HippoTank and Space Port files. See the [CAM and hospitals — beginner guide](</Users/simonhinterreiter/Documents/SimCity 4 Windows/CAM and hospitals - Guide.md>) for the complete new setup.

**Installed and checked on 7 September 2026:** CAM 3.1.1, System Integration Module 4.0.1, CAM Ordinances 3.3.0, Cobb, Cerulean and AndisArt building collections, Art Deco and Neo Futurism styles, and both medical additions. sc4pac tracked **133 packages at that stage**, including supporting files. All 15 manual downloads were verified. Content-file checks, the graphical manager, and fresh DLL startup logs passed. The computer-control tool cannot inspect the Wine game window; visual confirmation of the fresh region and hospital placement is still pending.

**11 September update:** Extra Cheats is installed through sc4pac (`simmaster07:extra-cheats-dll` 1.1.1-3), bringing the total at that stage to **134 packages**. Both DLL files match the official package hashes and have the required top-level Plugins links. The previous 133 package records and all 431 region files are unchanged. The game was not launched for this installation, so the money command remains untested in-game. [Money-control guide](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/SimCity 4 - Money Control Guide.md>).

**13 September update — Tokyo hub:** Tokyo Central Station v2.0 (right-hand traffic), all three Yunika Building Shinjuku shop variants, Daiwa House Tokyo (Maxis night), and Toranomon Hills Station Tower are installed. Their supporting files include RR Mega Props Vol02, PEG MTP, BSC MISC Vol02, and selected Moonlight/RDQ scenery files. sc4pac tracked **138 packages at that stage**; three buildings and two selected dependency files are installed manually. Existing Cobb Emperador Hotel and Xyloxadoria HSR stations were retained. [Building and connection guide](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/Tokyo Hub - Installed Buildings.md>).

**13 September update — large region:** **BananaLand V2** is installed in the active Windows profile's Regions folder. Its 100 large city tiles form a 10 × 10 grid, about 41 × 41 km using the game's 16-metre building grid. All tiles were checked: God mode, zero residential/commercial/industrial population, and no saved buildings, lots, transport networks, bridges or tunnels. The 102 installed files match the user's downloaded archive exactly; all 431 prior region files are unchanged. Loading the region in-game is still untested. [Region guide](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/BananaLand - Start Here.md>).

**13 September update — zoom performance:** a live activity sample identified substantial work in Render Services' custom ground-decal drawing. The optional custom renderer was disabled, with logging reduced to errors to avoid repeated fallback warnings. You confirmed that the zoom buttons became much more fluent. Building and other Plop and Paint services remain enabled; advanced ground-decal clipping, texture-region and depth-offset behavior is unavailable in this configuration. [Zoom and performance record](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/trackpad-performance/Zoom and performance notes.md>).

**13 September update — two-finger zoom:** a separate **SimCity Trackpad Zoom** Mac helper is installed. It is designed to send one vertical wheel step per two-finger swipe and discard continued vertical scrolling. Pinch controls and the unsuccessful helpers inside Wine were removed. You enabled macOS Accessibility access and confirmed that two-finger zoom works. The helper starts hidden with SimCity and stops automatically when the game wrapper shuts down; automatic stopping was tested. [Two-finger zoom guide](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/trackpad-zoom/Two-finger zoom guide.md>).

**14 September update — helper window:** the game launcher now waits for the zoom helper to finish launching, explicitly hides it, and verifies its hidden state. A fresh helper start and a later visibility check both passed while the existing city stayed open and zoom remained attached. The earlier launch-hidden flag alone was insufficient.

**14 September update — restored NAM stations:** Installed the separate `nam:additional-transit-stations` package, current NAM 50 variant. Its 59 files include **HSRP Transit Hub by 3ddz** (8 × 6 tiles, HSR/elevated rail/passenger rail/bus) and the other additional station categories absent from the Windows setup. Total at that stage: **139 managed packages**; all previous 138 package records unchanged. The station-stage Plop and Paint rebuild produced **740 buildings, 2,210 lots, zero parsing errors**, and 736 building thumbnails; the hub name is present. In-game placement remains untested. [Find the restored stations](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/SimCity 4 - Restored NAM Stations.md>).

**14 September update — slopes and canals:** Installed **NAM Tunnel and Slope Mod 0.3.1 — Easy / Steep** and **BSC SG Remastered Canals 2.0.0-1** through sc4pac, with their supporting packages. The total at that stage was **162 managed packages**: 23 additions, with all 139 prior package records unchanged. Easy smooths road and railway climbs when drawing networks; hills may need longer approaches. The CAL canal scenery supplies walls, locks, and wharves to match the existing NAM canal transport support. Use the existing NAM canal passenger terminal; new CAN-AM passenger/freight terminals have not been verified in this scenery selection. The two installed Easy files match the official ZIP, and NAM's core Street tunnel support remains installed. The subsequent catalogue rebuild passed with **819 buildings, 2,289 lots, zero parsing errors**, and 815 building thumbnails; the four missing thumbnails were already absent before this installation. In-game slope behavior and canal placement remain untested. [Slopes and canals — beginner guide](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/SimCity 4 - Slopes and Canals.md>).

**14 September update — NBVC Marina and seawalls:** Installed NBVC Marina, Modular Marina AddOn, Marina Round Corners, their supporting resources, and PEG CDK Leveler. The 58 NBVC lots and both Leveler sizes are indexed. One original Marina submenu file is maintained separately because sc4pac omits it. Current total: **169 managed packages**; all 162 prior package records and 2,036 existing plugin payloads are unchanged. The catalogue rebuild passed with **879 buildings, 2,349 lots, zero parsing errors**, and 875 building thumbnails. In-city placement remains untested. [Marina and seawalls — beginner guide](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/SimCity 4 - NBVC Marina and Seawalls.md>).

## 1. How the game runs on your Mac

| Component | Installed setup | What it does |
|---|---|---|
| Computer | MacBook Pro, Apple M1 Max, 32 GB memory | Runs the game and compatibility software. |
| Operating system | macOS 26.6.2 (25G83), verified 13 September | Your Mac's operating system. |
| Game | GOG SimCity 4 Deluxe, Windows 32-bit, version **1.1.641.0** | The actual game executable, including Rush Hour. |
| Porting Kit | **6.7.0** | Supplied the GOG-specific Wine setup used to prepare the game app. |
| Wineskin | **3.0.6_2** | Packages the game, its Windows-like folders, and its launch settings into a Mac application. |
| Wine engine | **WS11WineCX19.0.2-3**, reporting Wine **4.12.1** | Supplies the Windows functions the game expects. This engine uses Wine's 32-bit-on-64-bit support. |
| Rosetta 2 | Installed | Supports Intel-code translation for the compatibility software on the Apple Silicon Mac. |
| Visual C++ support | Microsoft Visual C++ 2022, x86 | Supporting Windows libraries required by some DLL mods. |

When you double-click **SimCity 4 Windows** on the desktop:

1. The shortcut opens the installed **SimCity 4 Windows.app**.
2. Its Wineskin launcher opens the Mac scroll helper and starts the included Wine environment.
3. Wine runs `C:\launch-sc4.bat`. A **batch file** is a short list of Windows commands.
4. That file starts the GOG game with the Windows profile, selected graphics settings, and single-CPU setting.
5. The game loads mods from the game installation's **Plugins** folder and the Windows profile's **Plugins** folder.

You do not need to open Steam, GOG Galaxy, or Porting Kit before playing. GOG Galaxy was used to obtain the game; the installed desktop app launches the offline game directly.

The game executable also has the **4 GB memory option** enabled. This lets a compatible 32-bit process address more memory. It does not convert the game into a 64-bit program. The original executable was backed up before this change.

## 2. Everyday use

### Play

1. Go to your Mac desktop.
2. Double-click **SimCity 4 Windows**.
3. Allow startup to finish. The verified launch took several minutes to reach all mod startup stages, so an initial delay alone does not mean the game has failed.

### Manage mods

1. Quit SimCity 4 before installing, removing, or updating mods.
2. Double-click **sc4pac Mod Manager** on the desktop.
3. Its graphical interface opens in your browser. On **Dashboard**, check that the profile is **SimCity 4 Windows**.
4. Click **My Plugins** to see installed packages, or **Find Packages** to search for additional mods.
5. To apply queued changes or check for updates, click **Dashboard → Update All**. Read the proposed changes and any options before confirming.
6. Wait for the operation to finish before starting the game again.

The browser interface runs locally at `http://localhost:51515/webapp/`. **Localhost** means your own computer. Use the desktop shortcut to start it each time; a browser bookmark alone cannot start its supporting program. If the page becomes blank or disconnected, close its tab and reopen the desktop shortcut.

The older **Update Windows Mods.command** helper remains in the Windows profile folder. It opens a text-based updater and uses the same package records as the graphical manager. Do not run both methods at the same time.

## 3. Graphics and the region-view fix

| Setting | Current value |
|---|---|
| Resolution | **1920 × 1200** |
| Window mode | **Windowed** |
| Graphics renderer | **DirectX**, using hardware rendering |
| Color depth | **32-bit** |
| Graphics update compatibility | **ForceDrawOnScroll=true** |
| Opening movie | Disabled |
| CPU count argument | **1** |

The **Graphics Options** mod controls the resolution and window settings. The launch command requests the same values. A **renderer** is the part of the game that draws its graphics.

The physical Retina display is 3456 × 2234 pixels. On 13 September, macOS provided a desktop area of 2056 × 1329 logical pixels; after the menu bar and Dock, a normal window had only 1196 pixels of available height. The requested 1920 × 1200 game window is slightly too tall before its title bar is added, so macOS can reduce its height. Earlier notes incorrectly described the full desktop height as available window space.

**13 September display repair:** the game is currently set to Windowed with normal Mac window controls and full graphics updates enabled. The game's own exclusive fullscreen was tested: 1920 × 1200 displayed correctly after enabling full updates, but it blacked out the other monitors and prevented normal Mac gestures. That fullscreen mode has been turned off. You confirmed that Mac green-button fullscreen, swiping back to the desktop, and use of the other monitors work. Clicks are accurate on the MacBook screen; click alignment on external monitors remains unresolved, which you accepted for now. Use the built-in screen for play. See the [display repair record](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/window-alignment/Window repair notes.md>).

**Region Thumbnail Fix** corrects incomplete terrain previews that can appear when large cities are saved at high resolutions. A **thumbnail** is the small picture of a city displayed on the region map.

For a preview that was already damaged:

1. Open the affected city.
2. Press **Control + S** while the game is focused to save it again.
3. Return to the region map and check the regenerated preview.

Installing the DLL does not rewrite old city saves by itself. The patch's successful loading is verified; a visual test of regenerating an already damaged preview remains outstanding.

## 4. Installed mods

### Network Addon Mod 50

**Network Addon Mod**, usually shortened to **NAM**, expands the transport tools and fixes transport behavior. The installation includes core components, Street Addon Mod, Network Widening Mod, Real Highway, Real Railway, Hybrid Railway, High Speed Rail, Real Expressway, Ground Light Rail, canals, bridges, transit-lot updates, and data views.

| NAM option | Selected value |
|---|---|
| Traffic side | Right-hand traffic |
| Road markings | US |
| Highway appearance | Original Maxis style |
| Traffic capacity | Low, the recommended setting |
| Vehicle animation | Standard Persistent |
| Night lighting | Original/standard Maxis |
| Canal style | CAL |
| Separate tunnel and slope setting | Easy / Steep, NAM Tunnel and Slope Mod 0.3.1 |
| Separate canal scenery | BSC SG Remastered Canals 2.0.0-1 |
| Airport capacity | Medium |
| Optional one-way-arrow replacement | Omitted |

Some NAM package records display **50,49** because their definitions support either release. The selected **current** variant installed the NAM 50 archive.

### DLL mods

A **DLL mod** is a Windows code file that extends or fixes the game. These twenty-two are installed:

| DLL mod | Actual mod version | Purpose | Managed by sc4pac? |
|---|---|---|---|
| NAM DLL | **1.3.1** | NAM transport and engine patches | Yes |
| Resource Loading Hooks | **2.0.1** | Extends resource-loading behavior for mods | Yes |
| Startup Performance Optimization / SC4DBPFLoading | **2.1** | Improves startup loading and supports long file paths | Yes |
| Region Thumbnail Fix | **1.0.0** | Fixes high-resolution city previews in the region map | Yes |
| Auto Save | **1.2.0** | Saves every 10 minutes of eligible gameplay; full saves update region thumbnails | Yes |
| Transparent Texture Fix | **1.0.0** | Fixes transparent custom-lot textures after underground/water view | Yes |
| Submenus | **2.1.0** | Adds nested menus for compatible content | Yes |
| Query Tool UI Extensions | **2.7.1** | Adds object copying and extended query information | Yes |
| SC4 Plop and Paint | **0.10.2** | In-game content browser and placement/painting tools | Installer package tracked; runtime completed separately |
| SC4RenderServices | **0.7.1** | Rendering and panel services for Plop and Paint | Installer package tracked; runtime completed separately |
| CPU Options | **1.0.2** | Controls CPU-related options; priority is AboveNormal | No, installed manually |
| Graphics Options | **1.4.0** | Controls rendering, resolution, window mode, and intro behavior | No, installed manually |
| SC4Fix | **Revision 8** | Community game fixes | No, installed manually |
| Custom Budget Departments | **1.1.0** | Supports the expanded budget | Yes |
| Lua Extensions | **1.5.0** | Supports extended game scripts | Yes |
| Advanced Water Management | **1.0.0** | Supports water-system changes | Yes |
| Legalize Gambling Upgrade | **1.0.0** | Extends the gambling ordinance | Yes |
| Custom Ordinance Host | **1.0.1** | Supports custom ordinances | Yes |
| Lua Sandbox | **1.0.0** | Supports isolated game scripts | Yes |
| More Building Styles | **3.6.1** | Adds architecture choices and expanded controls | Yes |
| Original Extra Cheats | **1.0** | Enables `moolah` to set the city balance | Yes; bundled in Extra Cheats package |
| Simmaster Extra Cheats | **1.1.1** | Adds further cheat commands | Yes; bundled in Extra Cheats package |

sc4pac currently tracks **169 packages**. A package can be one mod, part of NAM, an installer, or a supporting configuration package, so the package count is different from the 22 game DLLs. Package versions can include an extra revision suffix; for example, Region Thumbnail Fix is displayed as **1.0.0-2**, while the DLL itself is version **1.0.0**.

**CAM=yes** is active. System Integration Module supplies the replacement simulation and reward fixes. sc4pac removed the separate Opera House fix and the non-CAM high-tech jobs file; the latter package remains as an empty CAM-compatible dependency. The manual HippoTank and Space Port fixes were archived outside Plugins in `setup/cam-install/superseded-fixes` to prevent their old values from overriding CAM. No existing city saves were migrated.

Auto Save is enabled with a **10-minute interval**, **full saves**, and **paused time ignored**. It saves the current city rather than keeping a series of older copies. The active settings file is `Plugins/SC4AutoSave.ini`; the pre-installation backup remains separate.

Some managed DLLs appear at the top of Plugins as **symbolic links**: small references to their actual files in package folders. These are intentional. Do not delete them as apparent duplicates or move the DLLs into arbitrary subfolders.

## 5. Mod manager and its supporting software

| Component | Version or setting |
|---|---|
| sc4pac graphical interface | **1.6.1** |
| sc4pac command-line engine | **0.10.0** |
| Java | **17** |
| Mono | **6.14.1** |
| Selected profile | **SimCity 4 Windows**, internal profile ID **1** |

Java runs sc4pac's supporting program. Mono helps extract some older Windows mod installers. The graphical manager uses both through its desktop launcher.

**sc4pac is the recommended DLL manager for this installation.** It handles supported DLL packages and their dependencies, meaning other packages they require. Some DLL settings still require editing a text configuration file ending in `.ini`.

The three manually installed DLL mods listed above are outside sc4pac's tracking. No second DLL manager, dgVoodoo, or DxWrapper was installed. dgVoodoo and DxWrapper are graphics translators, not mod managers.

For Plop and Paint and Render Services, sc4pac tracks their downloaded installer packages. Their active DLL/data/settings files and supporting files were installed separately. Updating or removing those package entries does not automatically update or remove the runtime files. The native Mac indexing tool also needs to stay compatible with the installed Plop and Paint version.

Plop and Paint's content index and previews were generated by a native Mac helper built from the matching source release. Its output loaded successfully in the Windows DLL. A Microsoft math forwarding DLL was added to the game's Apps folder with a **SimCity 4.exe-specific Wine override**, supplying the `fmaf` function missing from this older Wine engine's forwarding file. The Wine engine, game executable, renderer, and resolution were retained.

## 6. Where the files are

| Item | Location |
|---|---|
| Game app | `/Users/simonhinterreiter/Applications/SimCity 4 Windows.app` |
| Mod manager app | `/Users/simonhinterreiter/Applications/sc4pac Mod Manager.app` |
| Plop and Paint content-rebuild app | `/Users/simonhinterreiter/Applications/Rebuild SimCity Content.app` |
| Mod manager supporting files | `/Users/simonhinterreiter/Applications/sc4pac Mod Manager` |
| Windows game profile | `/Users/simonhinterreiter/Documents/SimCity 4 Windows` |
| Windows mods | `/Users/simonhinterreiter/Documents/SimCity 4 Windows/Plugins` |
| Windows city saves | `/Users/simonhinterreiter/Documents/SimCity 4 Windows/Regions` |
| Graphics settings | `/Users/simonhinterreiter/Documents/SimCity 4 Windows/Plugins/SC4GraphicsOptions.ini` |
| Autosave settings | `/Users/simonhinterreiter/Documents/SimCity 4 Windows/Plugins/SC4AutoSave.ini` |
| Installation and verification records | `/Users/simonhinterreiter/Documents/SimCity 4 Windows/Setup logs` |
| Active sc4pac package records | `/Users/simonhinterreiter/Library/Application Support/io.github.memo33.sc4pac/profiles/1` |
| Project documents, downloads, cache, and backups | `/Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City` |
| Original native Mac game's profile | `/Users/simonhinterreiter/Documents/SimCity 4` |

To open one of these folders in Finder: click **Go → Go to Folder…**, paste its path, then press **Return**.

Inside Wine, the Windows profile is mapped to **`C:\SC4UserData\`**. This points to the separate **SimCity 4 Windows** folder above. Your original native Mac profile uses the separate **SimCity 4** folder. Do not copy the entire original Plugins folder over the Windows one; this can introduce duplicate or older mods.

## 7. Backups and verification

| Backup | Location |
|---|---|
| Original native Mac profile | [SimCity 4 Mac - 2026-09-06](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/backups/SimCity 4 Mac - 2026-09-06>) |
| Package records before graphical-manager migration | [Before graphical mod manager](</Users/simonhinterreiter/Documents/SimCity 4 Windows/Setup logs/Before graphical mod manager>) |
| Graphics settings, launch command, and package records before higher resolution | [Before high resolution - 2026-09-07](</Users/simonhinterreiter/Documents/SimCity 4 Windows/Setup logs/Before high resolution - 2026-09-07>) |
| Original executable and other setup backups | [Project setup backups](/Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/backups) |
| Windows profile, saves, mods, and package records before essential mods | [Before essential mods - 2026-09-07 005301](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/backups/Before essential mods - 2026-09-07 005301>) |

Historical checks from the earlier installation stages (their package totals describe those stages):

- The Windows GOG installation completed and the executable is version 1.1.641.0, 32-bit.
- The 4 GB memory flag is enabled and was confirmed by the NAM log.
- The earlier seven DLL mods produced startup logs; Region Thumbnail Fix explicitly reported that its patch was installed.
- The four additional DLL mods loaded in the 01:01 startup check. Submenus, Transparent Texture Fix, and Query Tool UI Extensions explicitly reported successful patch installation. Auto Save produced its version log. The user then confirmed the game was closed.
- You confirmed the original game launch and then the higher-resolution launch.
- The original Mac profile's 1,278 files matched the backup by path, size, and content fingerprint when checked during setup.
- Adding Region Thumbnail Fix preserved the previous 23 sc4pac package records unchanged.
- The essential-mod additions preserved all 24 earlier package records unchanged. The six additional managed packages bring the total to 30; HippoTank is separate.
- The later Plop and Paint and Render Services installer packages bring the total to 32. Their startup logs confirm service registration, successful loading of the generated content and thumbnails, and the first rendered overlay frame. In-city visual confirmation is pending.

**Runtime check on 7 September:** all 133 package records at that stage were installed; sc4pac displays no pending updates. All 20 game DLLs produced fresh startup logs. Plop and Paint loaded 651 buildings, 2,121 lots, 6,978 props and 125 flora items; its rendering service drew the first frame. The cache rebuild had zero parsing errors and skipped only the GOG uninstaller database during indexing.

Still untested: a complete city save/reopen cycle, visual repair of an old broken region preview, and every individual feature of every third-party mod. Wine compatibility must still be checked when adding new code mods.

The local graphical manager has a small startup workaround in its web files: its startup script is embedded in `index.html`, bundled rendering resources are used, and offline-cache registration is omitted. Original files are backed up under **setup/backups/sc4pac GUI original web files**. Replacing the manager's distribution during a future upgrade may overwrite this workaround.

Use **BananaLand V2** for the large regional project, or **CAM - Fresh Start** for the original four-tile flat starter. Save with **Control + S**, wait for confirmation, and only then exit without saving again. The installed Save Warning variant disables combined Save and Exit / Save and Quit.

## 8. More detailed guides and sources

- [CAM and hospitals — beginner guide](</Users/simonhinterreiter/Documents/SimCity 4 Windows/CAM and hospitals - Guide.md>)

- [Beginner guide](</Users/simonhinterreiter/Documents/SimCity 4 Windows/START HERE - SimCity 4 Windows.md>)
- [NAM installation and update details](</Users/simonhinterreiter/Documents/SimCity 4 Windows/NAM 50 installation and updates.md>)
- [High-resolution settings and DLL-manager research](</Users/simonhinterreiter/Documents/SimCity 4 Windows/High resolution and DLL managers.md>)
- [Essential mods, autosave, and the remembered overlay](</Users/simonhinterreiter/Documents/SimCity 4 Windows/Essential mods - September 2026.md>)
- [Plop and Paint controls and rebuilding its content list](</Users/simonhinterreiter/Documents/SimCity 4 Windows/Plop and Paint - How to use it.md>)
- [Technical setup record](/Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/SETUP-STATUS.md)
- [sc4pac author documentation](https://github.com/memo33/sc4pac-tools)
- [Graphics Options author documentation](https://github.com/0xC0000054/sc4-graphics-options)
- [Region Thumbnail Fix author documentation](https://github.com/memo33/sc4-thumbnail-fix-dll)
