# NAM 50 choices and older Wine runtime assessment

Prepared 6 September 2026. This document records inspection and suggested choices; no installation has been performed.

## Resource Loading Hooks downloaded

SC4ResourceLoadingHooks-v2.0.1.zip comes directly from the author's [v2.0.1 release](https://github.com/0xC0000054/sc4-resource-loading-hooks/releases/tag/v2.0.1). It contains the DLL, README and licenses. The 59,263-byte archive passed its ZIP checks and matches the published SHA-256 value. Version 2.0.1 fixes a crash. The author requires SC4 641 and Windows 10+, with Windows 7+ possibly working when the x86 Visual C++ 2022 runtime is present. Copy the DLL into the top level of one Plugins folder. Verify SC4ResourceLoadingHooks.log beside it. Extra exemplar logging is for diagnosis and can slow the game, so leave it off normally.

## Wine CX19.0.2: known facts and limits

The [official CrossOver changelog](https://www.codeweavers.com/crossover/changelog) dates CrossOver 19.0.2 to June 2020 and identifies the CrossOver 19 base as Wine 4.12-1. This predates the current DLL mods. No primary-source confirmation was found for NAM 50 with this exact Porting Kit engine. A successful unmodified game launch alone will not demonstrate current DLL support.

Downloaded vc_redist.x86-vs2022.exe is version 14.44.35211.0, using the same [Microsoft URL](https://aka.ms/vs/17/release/vc_redist.x86.exe) linked by the mod author and the [Winetricks vcrun2022 recipe](https://github.com/Winetricks/winetricks/blob/master/src/winetricks). Its hash matches that recipe. This is a closer match to the authors' documented dependency than the separately staged 14.51 runtime; that is a setup recommendation, not a verified claim of compatibility.

The Winetricks recipe selects native Microsoft v14 runtime libraries before Wine built-ins. It also replaces msvcp140.dll and msvcp140_2.dll because Wine's built-in version numbers may otherwise make the Microsoft installer skip them (Wine bug 57518). Prefer the wrapper's supported vcrun2022 workflow when available. Install into the same Wine prefix as SC4. Avoid adding vcrun2015/2017/2019 as unrelated extra layers; the recipe lists them as conflicting v14 alternatives. Do not downgrade below the build-time runtime requirement just because an older runtime installs successfully. If a newer Windows API is unimplemented in CX19, an engine update may be necessary; exact logs must determine that.

## Actual NAM 50 installer defaults

These values were read directly from the downloaded JAR. Its compiled classes have Java class version 52, confirming a Java 8-compatible installer. The package labels are more reliable than older general documentation that still calls the traffic simulator's default Medium.

| Setting | Actual package default | Suggested initial choice |
| --- | --- | --- |
| Controller | RHD | RHD, provided the installed game drives on the right |
| Maxis Highway | Default Style | Keep Default Style |
| Traffic Simulator | Low (Recommended) | Keep Low; avoid High/Ultra without a reason |
| Automata Controller | Standard Persistent | Keep default; Radical variants add visual traffic |
| Texture Style | US | Keep game's original style; do not switch to EU just because the user lives in Europe |
| Drive-side textures | US_RightSide | Match the controller and game |
| Night models | Maxis Nite | Keep default unless a DarkNite setup is explicitly chosen |
| Extended Station Queries | Standard | Keep Standard |
| Airport Capacity | Maxis Airport Medium Capacity | This is the NAM default; choose Maxis Airport Default Capacity only if preserving original airport capacities is intended |
| Cul-De-Sacs | Selected | Optional appearance change; deselect for a closer original street appearance |
| Intersection Islands / Zebras | Unselected | Leave unselected |

Keep the core files and full network features together for a full NAM installation. The package provides RealRailway as its rail option. Select only one side of mutually exclusive controller, texture, automata and simulator choices. Leave the default-unselected legacy menus, arrow replacements and wide-corner intersection options unchecked. The installer exposes no separate cheat pack. NAM's own traffic capacities are gameplay changes, so 'Low (Recommended)' should not be described as unchanged vanilla simulation.

NAM.ini is optional. Its additional permission for zones to develop along RHW is disabled by default; leave that default intact. One NAM.dll copy is sufficient.
