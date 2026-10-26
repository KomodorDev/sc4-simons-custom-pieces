# SimCity 4 Windows setup status

Updated: 14 September 2026, Europe/Berlin.

Current readable overview: [SimCity 4 - Setup Summary](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/SimCity 4 - Setup Summary.md>). The sections below record installation stages; later dated entries supersede earlier resolution and package-count values.

## Installed and verified

- MacBook Pro, Apple M1 Max, 32GB RAM, macOS15.7.4, Rosetta present.
- GOG offline installer `setup_simcity_4_deluxe_edition_1.1.641_hotfix_(25621).exe` installed successfully using supported Inno Setup silent flags. Exit0 and installer log say succeeded.
- Game executable PE32/x86, version1.1.641.0. Applied LAA/4GB bit; only one byte changed at offset342. Original and hash report in setup/backups and setup/game-executable-verification.json.
- App: `/Users/simonhinterreiter/Applications/SimCity 4 Windows.app`. Desktop shortcut created.
- Wrapper: Wineskin3.0.6_2 with WS11WineCX19.0.2-3 (Wine4.12.1). PortingKit6.7.0 remains installed. Its wizard was cancelled after copying the prepared wrapper to final app; final app is launched directly.
- Final active CFBundleExecutable is ORIGINAL `wineskinlauncher`. Program path `/windows/system32/cmd.exe`, flags `/c C:/launch-sc4.bat`, use-start0. Batch file starts the game with separate UserDir, window1280x800, introoff, CPUCount1, DirectX. Forward slash fixes shell flag quoting. A failed diagnostic while another external Wine session existed produced a Mach-port error. After scoped test-process shutdown, CUA app launch started the game and all mod DLLs.
- A minimal `Contents/MacOS/sc4-launcher` fallback script remains but is NOT the active CFBundleExecutable. Its self-test succeeded. `setup/wine-task.py` is a diagnostic CLI, not the user-facing launcher.
- Windows profile: `/Users/simonhinterreiter/Documents/SimCity 4 Windows`, mapped as `C:\SC4UserData\`. Wine My Documents is private; Symlinks In User Folder0. Original Mac Documents/SimCity4 unchanged.
- Winetricks vcrun2022 completed with exit0; Microsoft runtime log exit0; native runtime overrides installed.
- NAM50 via sc4pac, recommended Low/RHD/US/MaxisHighway; optional one-way-arrow replacement excluded. 23 managed package records, 732 regular files plus3 DLL links, 978,017,205 bytes.
- DLLs: NAM1.3.1, ResourceLoadingHooks2.0.1, SC4DBPFLoading2.1, SC4CPUOptions1.0.2, SC4GraphicsOptions1.4.0, SC4Fixrev8. All produced successful startup logs. NAM logs confirm LAA and network patches.
- Original profile reverified:1278files,1515330586bytes,177directories, allpaths/sizes/SHA256 identical to backup. Report setup/original-profile-verification.json.

## Gameplay test status — user confirmed launch

Vanilla and modded processes launched and generated hardware configuration / profile files. Latest app launch at23:36 generated fresh logs for all DLLs; it subsequently exited, and SimCity4.cfg exists with23:37 timestamp. No game Exception Reports found. The user subsequently confirmed: "the game started. i quit. just for your info". This confirms the visible game launched and explains its exit. A city save/reload has not been tested.

CUA cannot see Wine-created game windows: getApp times out despite starting the Windows process. User confirmed the game started and they quit. Leave it closed. Installation and visible launch complete; city save/reload remains untested. Do not claim every third-party mod is guaranteed to work under Wine.

## User guide

`/Users/simonhinterreiter/Documents/SimCity 4 Windows/START HERE - SimCity 4 Windows.md`

NAM manifests, exact updates, and logs are under Windows profile/Setup logs. Native original profile backup: `setup/backups/SimCity 4 Mac - 2026-09-06`.

## Graphical mod manager — installed and verified

- Official sc4pac GUI 1.6.1 cross-platform web app, bundled CLI 0.10.0, installed in `/Users/simonhinterreiter/Applications/sc4pac Mod Manager`. Existing Java 17 reused; Homebrew Mono 6.14.1 installed for legacy installer extraction support.
- Source: `https://github.com/memo33/sc4pac-gui/releases/download/1.6.1/sc4pac-gui-webapp-crossplatform.zip`. Archive in `setup/tools/sc4pac-gui-webapp-crossplatform-1.6.1.zip`; 79,324,410 bytes; SHA-256 `b814d407ec7009002ac1894915e77a30ee7c2535e1640a12fa5ceac996a8008e` matched the official release asset digest. Download manifest: `setup/tools/sc4pac-gui-download.json`.
- Mac launcher: `/Users/simonhinterreiter/Applications/sc4pac Mod Manager.app`; desktop shortcut of the same name. It supplies Java/Mono paths and the profiles directory, then runs the official web-app launcher. Local browser interface uses port 51515 and automatic shutdown when its browser client closes. No startup service created.
- Canonical profile: `/Users/simonhinterreiter/Library/Application Support/io.github.memo33.sc4pac/profiles/1`, registered as **SimCity 4 Windows** in the parent `sc4pac-profiles.json`. Migrated metadata without changing the existing Plugins location or reinstalling mods. GUI recognizes all 23 installed package records. CPU Options, Graphics Options, and SC4Fix remain manually managed.
- Original metadata and updater backed up in Windows profile `Setup logs/Before graphical mod manager`; former active JSON filenames in the Windows user folder now end in `.migrated-backup`. `Update Windows Mods.command` uses the canonical GUI profile and bundled CLI, so both interfaces share state.
- Browser startup initially failed with `net::ERR_INVALID_HTTP_RESPONSE` for `flutter_bootstrap.js`. Local workaround: embed the official bootstrap inline in `webapp/index.html`, use bundled `/webapp/canvaskit/` resources, and omit the bootstrap service-worker registration. Original web files are backed up in `setup/backups/sc4pac GUI original web files`. `main.dart.js` remains unchanged. A future distribution replacement may overwrite this workaround.
- Fresh normal app launch succeeded without a browser refresh. CUA verified the profile dashboard and My Plugins showing 23 packages. Final working browser tab was left open and marked as a deliverable. No package update/install/remove actions were performed during GUI setup. Temporary diagnostic servers were stopped; final server uses the normal launcher with auto-shutdown enabled.
- Beginner guide and NAM update instructions revised for the graphical manager and canonical profile location. Game remains closed as requested by context.

## Higher resolution and Region Thumbnail Fix — 7 September 2026

- User requested higher resolution, the region-view fix, and DLL-manager research. Existing Graphics Options 1.4.0 INI changed from 1280x800 to **1920x1200**, retaining DirectX, Windowed, and 32-bit color. `drive_c/launch-sc4.bat` updated to the same resolution. Actual macOS logical display dimensions are 2056x1329, confirmed by CoreGraphics and the game's hardware log; the physical Retina panel is 3456x2234. Both requested dimensions remain below the DirectX7 2048-per-dimension limit.
- Added only `memo:region-thumbnail-fix-dll` package 1.0.0-2 (DLL version1.0.0) through canonical sc4pac profile. Update completed exit0. Total24packages; comparison of lock records confirmed all previous23 unchanged. DLL SHA256 matches official metadata: `2b17a275727012c8d9d74a84035be5bdcca480bea4b23322bab3941ed14609a5`. Top-level Plugins DLL link resolves correctly.
- Backups of pre-change INI, launcher batch file, package config and lock: `/Users/simonhinterreiter/Documents/SimCity 4 Windows/Setup logs/Before high resolution - 2026-09-07`.
- Test launch began00:18:05 and took several minutes to reach mod loading. Region DLL log00:20:44 explicitly confirms patch installation; Graphics Options log fresh without resolution/wrapper warning; NAM startup continued through00:21:57. User explicitly confirmed **"the game loaded fine in higher res"**. Do not mistake normal initial startup delay or CUA's inability to see Wine windows for failure. No processes were killed during this test. Visual regeneration of an old broken city preview remains untested; it requires loading and saving that city.
- DLL manager recommendation: retain sc4pac GUI1.6.1/CLI0.10.0. Research comparison and current graphics instructions saved as `/Users/simonhinterreiter/Documents/SimCity 4 Windows/High resolution and DLL managers.md`. No second DLL manager or graphics translator installed. CPUOptions, GraphicsOptions and SC4Fix remain manually managed.

## Essential and optional mods — 7 September 2026, 01:00 onward

- User authorized all eight previously recommended mods, including Submenus and Query Tool UI Extensions. Seven are installed; Space Port Fix is pending the answer about existing Space Ports.
- Full pre-change Windows profile and sc4pac records backed up to `setup/backups/Before essential mods - 2026-09-07 005301`. Original package records remain unchanged.
- Added through sc4pac: `null-45:sc4-autosave` 1.2.0, `memo:transparent-texture-fix-dll` 1.0.0-2, `memo:submenus-dll` 2.1.0, `null-45:query-tool-ui-extensions-dll` 2.7.1, `heinbloed4711:hi-tech-missing-high-wealth-jobs` 1.11-1 with `CAM=no`, and `mz:opera-house-fix` beta1.1. Current total **30 managed packages; 11 unique x86 DLLs**. Root/package copies are intentional same-target symbolic links.
- Activated SC4AutoSave.ini: enabled, 10 minutes, FastSave=false, IgnoreTimePaused=true, LogSaveEvents=true. Full saves regenerate thumbnails; this does not keep rotating backups. Activated SC4QueryUIHooks.ini with shipped defaults: sounds enabled; building-path diagnostic logging disabled.
- Four new DLLs tested in launch at01:01. Transparent Texture Fix, Submenus, and Query UI Hooks explicitly logged installed patches/hooks. Auto Save logged v1.2.0. Query log was initially empty because its output is buffered; successful hooks message appeared after normal exit. User explicitly confirmed the game was closed. No process was killed.
- Simtropolis automatic downloads returned403, and Chrome blocked the attempted download click. User downloaded all four remaining archives. Used sc4pac's supported Select a file from disk fallback to install IHT and Opera; CLI finished exit0. No browser security settings were changed.
- HippoTank Demand Fix installed manually following its included readme: `drive_c/GOG Games/SimCity 4 Deluxe Edition/Plugins/HT_DemandFix.dat` within the game app. Its source archive, original readme, destination, and SHA256 are recorded under `setup/essential-mods-manual/`. This is outside sc4pac tracking.
- Space Port archive and readme are retained in that staging folder. Selected fix-only `Spaceport Fix Mod.dat`; Alt excluded. **Not installed yet**: included author instructions require bulldozing existing Space Ports before adding/removing the mod. User answer pending; no buildings or saves changed to satisfy this rule.
- GUI Dashboard recognizes SimCity 4 Windows and reports Pending updates (0); new managed packages visible. Verification record: Windows profile `Setup logs/Essential mods verification.json`. Readable setup summary and beginner guide updated; new `Essential mods - September 2026.md` guide includes controls and status.
- Remembered Reddit overlay identified with high confidence as **SC4 Plop and Paint** by CasperVg, but exact clip unconfirmed. It remains research-only, not installed. Its Advanced Plopping & Painting panel uses O and supports object browsing/painting/prop removal. Requires SC4RenderServices and cache generation; shipped cache builder is x64 Windows, with source build instructions also available for macOS. Exact Wine compatibility untested.
- Remaining validation: in-city feature checks and timed autosave; data fixes were installed after the DLL startup check. Game remains closed.

## Plop and Paint and remaining Space Port Fix — 7 September 2026

- User explicitly requested SC4 Plop and Paint, then confirmed there are no Space Ports. Installed standard `Spaceport Fix Mod.dat` in Windows profile `Plugins/150-manual-fixes/Cougar2004`. Alternative variant omitted. Original eight-mod request is complete; no buildings were demolished. Updated manual installation and essential-mod verification records.
- Backup before this stage: `setup/backups/Before Plop and Paint - 2026-09-07 011811`. Contains Windows profile, package records, game Apps, installation Plugins, prefix registry files, and launcher batch file. Pointer: `setup/plop-and-paint-backup.json`.
- Added `caspervg:sc4-plop-and-paint-dll` 0.10.2 and its dependency `caspervg:sc4-render-services-dll` 0.7.1 via sc4pac. Official GitHub release ZIPs and installer hashes matched metadata. Current **32 package records**, all previous30 unchanged. These packages track NSIS installers, not the separately completed runtime payloads. Updates/removals need a matching extra runtime step.
- Extracted official installer payloads using sevenzip, installed unmodified SC4PlopAndPaint.dll/DAT/INI and SC4RenderServices.dll/INI into Windows Plugins root, plus imgui.dll into game Apps. Shipped settings retained. Current **13 game DLL mods**; supporting Apps DLLs are not counted as game plugins. Game executable, graphics settings, autosave settings, Wine engine, and launch command retained.
- Compiled native ARM64 cache builder from official Plop/Paint v0.10.2 source to avoid needing x64 Windows in the existing win32 Wine prefix. Apple Clang16 needs a narrow DBPFKit floating-parser fallback using fast_float::from_chars; game DLLs and cache schemas unchanged. Both upstream suites passed:61cases/361assertions. Notes, source provenance, patch and logs: `setup/plop-and-paint-native/BUILD-NOTES.md`. Installed runnable binary and exact author PropertyMapper.xml at `/Users/simonhinterreiter/Applications/SC4 Plop and Paint Tools`.
- Initial cache scan succeeded:486buildings/1932lots/2105props/408propFamilies/22flora;0parseerrors. Generated previews:486buildings/1988props/22flora. Some special/composite/effect props do not yield thumbnails; full log records limitations. Six caches written into Windows Plugins; native format compatibility subsequently confirmed by successful Windows DLL loading.
- Import audit identified missing `fmaf` in Wine4.12's CRT math API-set stub. Added official Microsoft x86 `api-ms-win-crt-math-l1-1-0.dll` version10.0.16299.15 to game Apps, SHA256 `bece7bab83a5d0ec5c35f0841cbbf413e01ac878550fbdb34816ed55185dcfed`. Source: Microsoft's UCRT component from official Python.org win32 ucrt.msi; no Python installed. All314 exports forward to functions present in existing native ucrtbase; existing mod imports audited. Registry override restricted to `HKCU\Software\Wine\AppDefaults\SimCity 4.exe\DllOverrides`, value `*api-ms-win-crt-math-l1-1-0`=`native,builtin`. Prefix system32 unchanged. Audit records: `setup/plop-and-paint-runtime-audit`.
- Game launch01:28:56 succeeded. Plop/Paint acquired all four services, loaded all three CBOR caches and thumbnails, registered panels. RenderServices log01:29:17 reports scene hooks installed and first frame rendered with4panels. lsof confirmed game loaded native math forwarder from Apps. Game later exited at about01:30:37, writing favorites; no process was killed. Visual user confirmation is pending; asked user to open city, pause, pressO. CUA cannot inspect Wine's window.
- Native graphical **Rebuild SimCity Content.app** and desktop shortcut installed. Its button runs the native helper with matching paths and44pxpreviews; checks game process before rebuilding; POSIX mkdir lock prevents concurrent helper instances. Full GUI rebuild completed01:34:37 exit0 (~35seconds), with game already closed. Source/build notes: `setup/plop-and-paint-helper`. Desktop app and builder need no Homebrew runtime dependencies.
- Authoritative installation record: `setup/plop-and-paint-installation.json`. Logs copied into Windows profile Setup logs. Readable summary, essential-mod guide, beginner guide, and dedicated `Plop and Paint - How to use it.md` updated.
- Final helper refinement keeps technical output in its log and shows readable progress/counts plus real warning summaries in the window. Offline verification against the successful162KBlog passed; rebuilt app/signature verified and installed. Reopening its final window was blocked because the Mac was locked. Prior GUI rebuild succeeded. Do not claim final visual/in-city confirmation; user has not answered that check. City files match the pre-installation backup.


## 7 September 2026 — CAM request, download blocker, hospital installed

The user requested both hospitals, CAM Controller/SIM/Ordinances, Cobb, Cerulean, AndisArt and their dependencies, then confirmed no existing cities in the Windows profile. A full backup was made at `setup/backups/Before CAM and hospitals - 2026-09-07 105452`.

The full CAM transaction never committed. Simtropolis returned HTTP 403, and Chrome showed ERR_BLOCKED_BY_CLIENT. Fifteen required downloads need user action. The planned CAM profile is preserved in `setup/cam-install/planned-cam-profile.json`. The active profile was restored to CAM=no before installing Large Modern Hospital and its five BSC dependencies. That separate transaction succeeded: the profile now has 38 packages, and all 32 prior package records are unchanged. The graphical manager showed the hospital installed and zero pending updates.

HippoTank, Spaceport, Opera House and the non-CAM IHT fixes remain active for the current setup. Their CAM replacements must be handled only when the full CAM transaction succeeds. No CAM runtime DLL has been installed. The fresh region and CAM guide remain staged only.

Hospital payloads came from the official SC4Evermore 117 compilation and were locally repackaged with original filenames and binaries intact. The model and both lots, service statistics, and model references were verified. Plop and Paint rebuilt successfully with 488 buildings, 1,934 lots, 3,447 props, 781 prop families and 125 flora items. Parsing errors: zero. Its one indexing warning was the harmless GOG uninstaller database unins000.dat, which is not a game DBPF file. Actual in-game hospital placement remains untested.

Provenance and audits are in `setup/cam-install/content-downloads` and `runtime-audit`. Resume plan: `setup/cam-install/installation.json`. User action: `setup/cam-install/Downloads needed.md`. No new matching archive downloads had arrived when preparation finished.


## Completed CAM and hospitals installation — 7 September 2026, 15:35

**Installed and checked on 7 September 2026:** CAM 3.1.1, System Integration Module 4.0.1, CAM Ordinances 3.3.0, Cobb, Cerulean and AndisArt building collections, Art Deco and Neo Futurism styles, and both medical additions. sc4pac now tracks **133 packages**, including supporting files. All 15 manual downloads were verified. Content-file checks, the graphical manager, and fresh DLL startup logs passed. The computer-control tool cannot inspect the Wine game window; visual confirmation of the fresh region and hospital placement is still pending.

- CAM=yes, current controller 3.1.1, SIM 4.0.1, ordinances 3.3.0-2; standard lighting and standard commercial cap fix.
- Both hospitals, Cobb/Cerulean/AndisArt collections and all required models, props, textures and style definitions installed.
- 133 packages; 20 distinct DLL files; no duplicate active DLL payload paths. GUI shows 133 packages and pending updates 0.
- Spaceport and HippoTank files archived; Opera House and non-CAM IHT files removed by sc4pac.
- BuildingStyles.ini, SC4MoreBuildingStyles.ini and SC4LegalizeGamblingUpgrade.ini activated with shipped defaults.
- Fresh region installed with four large, empty tiles.
- Native cache build exit 0: 651 buildings, 2121 lots, 6978 props, 948 prop families, 125 flora; zero parse errors. One harmless uninstaller-database indexing warning. Previews: 651 buildings, 6858 props, 125 flora.
- All seven new DLLs produced fresh startup logs; running Plop and Paint loaded the rebuilt catalogue; Render Services rendered its first frame.
- Evidence: setup/cam-install/final-content-verification.json, runtime-verification.json, post-install-actions.json, download-arrival-audit.json.
- Backup: setup/backups/Before CAM completion - 2026-09-07 151618.
- Visual city loading, hospital placement and a save/reopen cycle remain unverified.


## Extra Cheats installed — 11 September 2026

- User requested an easy way to set city funds, then explicitly asked for installation.
- Added `simmaster07:extra-cheats-dll` 1.1.1-3 through canonical sc4pac profile 1. Transaction completed exit 0; total 134 packages. All 133 previous package records are byte-for-byte equivalent as parsed records.
- Both official Simtropolis downloads initially returned HTTP 403 through sc4pac. Normal Chrome downloads succeeded after the user completed the website check. Original ZIP retained; secondary DLL wrapped in a local ZIP without changing its bytes for sc4pac's supported disk-file fallback. Both DLL SHA-256 values match official package metadata.
- Top-level `Plugins/SimCity 4 Extra Cheats Plugin.dll` and `Plugins/ExtraExtraCheats.dll` links resolve to the managed package files. Original DLL provides `moolah`; secondary DLL provides additional commands.
- All 431 region files retain their pre-installation paths, sizes and SHA-256 values. No city balance changed. Game was closed and was not launched; command behavior in this Wine setup remains untested. No content-index rebuild required because this package contains code files, not buildings or props.
- Backup, provenance and checks: `setup/extra-cheats/before.json`, `browser-download-verification.json`, `installation-verification.json`. Beginner money guide copied to the Windows profile; setup summary and start guide updated.


## Tokyo hub — 13 September 2026

Installed Tokyo Central Station v2 RHD, Yunika (all three growable/plop variants), Daiwa House MN, Toranomon Hills Station Tower. Added sc4pac packages: mattb325:daiwa-house-tokyo, rretail:mega-prop-pack-vol2, peg:mtp-super-pack (US), bsc:mega-props-misc-vol02. Total managed packages: 138; previous 134 package records unchanged. Tokyo, Yunika and Toranomon are manual; exact file manifests under setup/tokyo-hub-install/records. Selected Moonlight SAM1 prop file and RDQ tree file supply Toranomon dependencies without network overrides. Yunika has an undeclared timed crowd prop supplied by BSC MISC Vol02. No city placement/runtime test performed. User guide: Tokyo Hub - Installed Buildings.md.

## Additional NAM stations — 14 September 2026

Installed `nam:additional-transit-stations` version 50,49, current NAM 50 variant, after the user saved and quit the game. sc4pac transaction completed successfully. All 59 files match verified staging; all 138 previous package records are unchanged. Total managed packages at that stage: 139. Restored HSRP Transit Hub by 3ddz and the missing additional station collection. Hub is 8×6 tiles, submenu ID 0x322c7959: Transportation → Misc-Transit → Multi-modal Stations.

Rebuilt Plop and Paint catalogue successfully: 740 buildings, 2210 lots, zero parsing errors; 736 building thumbnails. Hub title found in lots.cbor. Four catalogue buildings lack thumbnails. In-game placement not tested. Records: `setup/additional-transit-stations/installation-verification.json`, `catalogue-rebuild.log`, and `staging-verification.json`. Beginner guide: `SimCity 4 - Restored NAM Stations.md`.

## Slopes and canals — 14 September 2026

Installed `nam-team:tunnel-and-slope-mod` **0.3.1**, variant **easy** (Easy / Steep), and `bsc:sg-remastered-canals` **2.0.0-1**, with their supporting packages, through the active sc4pac profile. Current total: **162 managed packages**. The transaction added 23 package records; all 139 prior records are unchanged, and none were removed. These two packages and their canal lots are managed by sc4pac; no canal lots were installed manually.

Both Easy full-set files match the downloaded official ZIP exactly: `NetworkAddonMod_Tunnel&SlopeMod_02_Easy_Steep.dat` (3,686 bytes) and `SubwayPipeDepthFix.dat` (749 bytes). No other slope variant is installed. NAM 50's `NAM_Tunnels_Street.dat` is retained; it contains tunnel assets and a runtime property patch compatible with slope mods. Resource Loading Hooks remains installed. This verifies the files, not in-game slope behavior.

CAL canal scenery supplies walls, locks, and wharves matching the existing NAM CAL canal support. Passenger-route instructions use the existing NAM canal terminal; extra CAN-AM passenger/freight terminals have not been verified in this selected scenery package. Intended menu: **Transportation → Water Transportation → Canals → BSC SG Remastered Canals**, with **BSC Zero7 Sunken Canals** alongside it. Canal placement remains untested.

The official `BSC_Canals_Submenu.dat`, included in the downloaded collection but omitted from the sc4pac package payload, is maintained separately at `Plugins/660-parks/BSC Canals - Menu Support/BSC_Canals_Submenu.dat`. This is menu support only. Downloads, backup, installation output, and verification records are under `setup/slopes-and-canals`.

The subsequent catalogue rebuild completed with exit 0: **819 buildings, 2,289 lots, zero parsing errors**, and 815 building thumbnails. The four missing building thumbnails predate this installation. Verified 137 CAL matches and the original HSRP hub name. Final record: `setup/slopes-and-canals/installation-verification.json`.

Beginner guides: [project guide](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/SimCity 4 - Slopes and Canals.md>) and [Windows-profile guide](</Users/simonhinterreiter/Documents/SimCity 4 Windows/Slopes and canals - Guide.md>).

## NBVC Marina installed — 14 September 2026

Installed through canonical sc4pac profile 1: `nbvc:marina` 2.0-1, `nbvc:modular-marina-addon` 2.0-1, `nbvc:marina-round-corners` 2.0-1, and `peg:cdk-leveler` 2.05, plus three NBVC resource packages (2.0-2, 2.0-2, 2.0-1 respectively). Total 169 packages; all 162 prior package records and 2,036 prior plugin payload files unchanged. Existing Submenus and Resource Loading Hooks retained. Game was closed; no city modified or game launch performed.

The user downloaded three original NBVC ZIPs and the original PEG CDK3 Windows installer after automatic downloads returned 403 and browser links returned ERR_BLOCKED_BY_CLIENT. sc4pac's select-from-disk route accepted these and extracted the data. Only `PEG-CDK_Leveler.dat` was installed from CDK3; the collection's installer was not run. All 206 NBVC files match original archives: 58 SC4Lot, 74 SC4Model, 74 SC4Desc. Exactly one original `Marina Submenu.dat` (94,744 bytes; SHA256 c70bb90982656ca036b1e6c32209e3d9493800ecc23b640bdd9bc0c764fd8257) is installed manually at `Plugins/700-transit/NBVC Marina - Menu Support/Marina Submenu.dat`, since sc4pac excludes DAT files from those packages. All three ZIP copies are identical. Total new payload: 208 files.

Menu definitions: Transportation → Water Transportation → Waterfront → NBVC Marina Main → Modular Marina Menu → Modular Marina Base Set / Modular Marina Addon Set / Modular Marina Round Corners Set. Four original individual lots omit a custom submenu assignment and retain water-transport classification; they remain searchable. Leveler sizes classify as Parks. Its own tooltip says point the arrow inland/uphill at the coast, then bulldoze; De-Zone may be needed afterward. Inland leveling uses the opposite arrow direction. No verified universal numeric waterfront height is claimed.

Catalogue rebuild completed exit 0 from the builder's tools directory, with 879 buildings, 2,349 lots, zero parse errors, 875 building thumbnails, 10,131 props, 1,085 prop families and 125 flora. Exact straight/diagonal/rounded seawall and both Leveler titles were found; HSRP Transit Hub retained. Four absent building thumbnails and the GOG uninstaller indexing warning predate this work. The initial scan from the project directory failed to find PropertyMapper.xml before scanning; rerunning in the installed tools directory succeeded. In-game placement remains untested.

Records and source downloads: `setup/nbvc-marina`. Backup: `setup/nbvc-marina/before-20260914-153926` (profile, six catalogue files, prior payload manifest). Final audit: `installation-verification.json`. Guide: `SimCity 4 - NBVC Marina and Seawalls.md`, also copied into the Windows user profile. No downloads or installation steps remain pending.
