# Optional NAM components — checked 14 September 2026

The Windows setup now includes NAM Additional Transit Stations. No other major NAM transport network is missing compared with the current full sc4pac NAM bundle. RealHighway, RealExpressway, Network Widening Mod, Street Addon Mod, Ground Light Rail, Hybrid Railway, High Speed Rail, bridges, improved transport data views, and the core features are installed.

**Updated after the 14 September installation:** the user selected the slope and canal additions below. Both are now installed through sc4pac. The profile contains **162 managed packages**, with 23 additions and all 139 prior package records unchanged. [Beginner guide](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/SimCity 4 - Slopes and Canals.md>).

| Option | Status | Purpose |
|---|---|---|
| NAM Tunnel and Slope Mod (`nam-team:tunnel-and-slope-mod`) | **Installed: 0.3.1, Easy / Steep.** Both selected files match the official archive; in-game behavior remains untested. | Smooths road and railway climbs when drawing networks. Easy is forgiving, but hills may need longer approaches. The original Mac setup had an older rail-only Moderate file; this is the current separate package. |
| BSC SG Remastered Canals (`bsc:sg-remastered-canals`) | **Installed: 2.0.0-1**, matching the existing NAM CAL support. In-game placement remains untested. | Adds scenery including canal walls, locks, and wharves for artificial canals on land. Working passenger canals use the existing NAM CAN-AM transport pieces and terminal. New CAN-AM passenger/freight terminals have not been verified in this selected scenery package. |
| One-Way Road Arrow plugin | **Not installed**, by choice. | Changes, reduces, or hides one-way-road arrows. The Windows setup keeps the game's original arrows. |

The canal menu is **Transportation → Water Transportation → Canals → BSC SG Remastered Canals**, alongside **BSC Zero7 Sunken Canals**. Its official menu-support file is maintained separately at `Plugins/660-parks/BSC Canals - Menu Support/BSC_Canals_Submenu.dat`: it was included in the collection archive but omitted from the managed package. No canal lots were installed manually. The [Windows guide](</Users/simonhinterreiter/Documents/SimCity 4 Windows/Slopes and canals - Guide.md>) also explains the CAL search fallback.

NAM 50's core Street tunnel assets and runtime patch remain installed, together with Resource Loading Hooks. They work alongside the new slope settings; the old supplemental slope-file removal instruction does not require deleting the NAM 50 core tunnel file.

Alternative road textures, Maxis Highway Override, traffic capacity settings, night-lighting styles, and legacy menu choices are preferences, not missing required components.

Sources: [official sc4pac NAM package definitions](https://raw.githubusercontent.com/memo33/sc4pac/master/src/yaml/nam/network-addon-mod.yaml), [Tunnel and Slope Mod guide](https://www.sc4nam.com/docs/feature-guides/tunnel-and-slope-mod/), [NAM canal guide](https://www.sc4nam.com/docs/feature-guides/canals/). Compared against the active Windows package records/files and original native Mac NAM installation/backup.
