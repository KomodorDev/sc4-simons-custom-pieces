# NAM 50 installation and future updates

NAM 50 was installed successfully on 6 September 2026 using the official sc4pac CLI 0.10.0 and native Java 17. This method does not need a Windows Java installation or a graphical NAM installer. The game itself still needs the Windows compatibility environment prepared separately.

## What was installed

The separate Windows game profile is `/Users/simonhinterreiter/Documents/SimCity 4 Windows`. Its `Plugins` child contains the mods. The original native Mac folder `Documents/SimCity 4` was not changed by this installation.

The sc4pac installation contains 23 package records, 732 regular files, and 3 symbolic links, with 978,017,205 bytes of regular file contents. A symbolic link is a small filesystem reference to another file. sc4pac uses three such references to make its DLLs available directly inside Plugins while keeping the actual files inside their package folders. These are not separately maintained duplicate DLL versions.

The three installed game extension DLLs are:

| File in Plugins | Actual mod version | sc4pac package version |
|---|---|---|
| NAM.dll | 1.3.1 | 1.3.1 |
| SC4ResourceLoadingHooks.dll | 2.0.1 | 2.0.1-1 |
| SC4DBPFLoading.dll | 2.1 | 2.1-2 |

All three DLL contents were checked against the source-published metadata SHA-256 hashes. The full NAM archive was also checked against its official SHA-256 hash. A SHA-256 hash is a content fingerprint that detects changed or incomplete downloads.

NAM data packages display version `50,49` in sc4pac because the metadata offers either version. The selected `current` variant downloaded and installed the NAM 50 archive; no NAM 49 assets were selected.

The selected components match the full sc4pac NAM bundle except for the optional one-way-arrow replacement, which was omitted to preserve the game's original arrows. This includes Real Highway, Real Railway, Hybrid Railway, High Speed Rail, Real Expressway, Street Addon Mod, Network Widening Mod, Ground Light Rail, canals, bridges, updated Maxis transit lots, data views, and all core components. Separate Additional Transit Stations and Tunnel and Slope Mod packages were not added.

Selected options: Windows digital edition, right-hand traffic, US road markings, original Maxis night lighting, original Maxis highway style, Low (Recommended) traffic capacity, Standard Persistent vehicle animations, CAL canals, and Medium airport capacity. No NAM.ini was installed; the NAM DLL uses its built-in defaults, including its optional dirt-road-access patch disabled.

Startup Performance Optimization was installed because three installed files exceed the usual 260-character Windows path limit even with `C:\SC4UserData\Plugins\` as the root. The longest path is 280 characters. This DLL explicitly adds long-path support.

CPU Options, Graphics Options and SC4Fix are outside this sc4pac installation and are being installed separately. The file manifest lists only files owned by this sc4pac profile; it does not count separately installed mods or game-created logs.

## How to update these mods later

1. Quit SimCity 4 completely. Updating while the game is open can replace files the running game is reading.
2. In Finder, open Documents, then SimCity 4 Windows.
3. Double-click `Update Windows Mods.command`. This opens Terminal and runs sc4pac from the correct profile folder.
4. Read the proposed changes and answer the questions shown in Terminal. If a new release introduces a choice, sc4pac will ask you to select it. The current choices are already saved.
5. Wait for `Done.` or the message that everything is current. An exit status of 0 means the update command completed successfully.
6. Press Return to close the command window, then start the Windows game.

The exact equivalent Terminal commands are:

```sh
cd '/Users/simonhinterreiter/Documents/SimCity 4 Windows'
'/Library/Java/JavaVirtualMachines/jdk-17.jdk/Contents/Home/bin/java' -jar '/Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/tools/sc4pac-0.10.0/sc4pac-cli.jar' update
```

The CLI stores its profile in its working directory, so the first line is necessary. Do not run it from the native Mac game folder. The `--yes` option can accept installation confirmations automatically, but it does not choose newly introduced variants.

The profile configuration is `sc4pac-plugins.json`. Installed package versions and locations are in `sc4pac-plugins-lock.json`. Cache and temporary extraction files are under `/Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup` in `sc4pac-cache` and `sc4pac-temp`.

## Validation still required in the Windows game

Successful extraction and checksum verification prove the mod files were installed, not that the Wine environment can execute every DLL. Startup Performance Optimization's author requires game version 1.1.641, Windows 10 or later, and Microsoft Visual C++ 2022 x86. The author does not publish special Wine instructions or a Wine compatibility guarantee. Resource Loading Hooks lists Windows 10 or later. NAM DLL 1.3.1 lists Windows 10 or later, or Linux. Both mention the Visual C++ 2022 x86 runtime specifically for possible Windows 7 compatibility; their current instructions do not list it as a separate Windows 10 requirement.

After a game launch, look for `NAM.log`, `SC4ResourceLoadingHooks.log` and `SC4DBPFLoading.log` in Plugins. Inspect their contents to confirm loading. For advanced verification, the game argument `-StartupDBPFLoadTrace:ListLoadedFiles` asks SC4DBPFLoading to list loaded files in its log.

## Files recording this installation

- `Setup logs/sc4pac-NAM50-install.log`: NAM and Resource Loading Hooks installation output.
- `Setup logs/sc4pac-long-path-support-install.log`: Startup Performance Optimization installation output.
- `Setup logs/NAM50-installed-files.json`: exact paths, package ownership, sizes, hashes, symbolic links, and long-path report.
- `Setup logs/NAM50-installed-files.csv`: the same file inventory in a spreadsheet-friendly form.

## Official sources

- [sc4pac CLI 0.10.0 release](https://github.com/memo33/sc4pac-tools/releases/tag/0.10.0)
- [sc4pac CLI documentation](https://github.com/memo33/sc4pac-tools/blob/0.10.0/cli.md)
- [sc4pac profile schema source](https://github.com/memo33/sc4pac-tools/blob/0.10.0/src/main/scala/sc4pac/Data.scala)
- [NAM package definitions](https://github.com/memo33/sc4pac/blob/main/src/yaml/nam/network-addon-mod.yaml)
- [NAM 50 official release](https://github.com/NAMTeam/Network-Addon-Mod/releases/tag/50)
- [Resource Loading Hooks 2.0.1](https://github.com/0xC0000054/sc4-resource-loading-hooks/releases/tag/v2.0.1)
- [Startup Performance Optimization instructions](https://github.com/0xC0000054/sc4-dbpf-loading/blob/v2.1.0/README.md)
