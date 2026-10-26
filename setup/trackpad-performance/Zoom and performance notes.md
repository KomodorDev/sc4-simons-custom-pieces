# SimCity 4: trackpad zoom and performance — 13 September 2026

**Final status updated 14 September:** the user confirmed faster zoom drawing and working two-finger scrolling. Both performance settings below are retained. Pinch was abandoned at the user's request. See the [complete display and zoom repair guide](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/SimCity 4 - Display and Zoom Fixes.md>) for the final configuration, helper startup/shutdown, and reversal steps.

## Zoom controls

The Mac's pinch setting is already enabled. This installed Wine 4.12 Mac driver translates scrolling into Windows mouse-wheel input but has no pinch/magnification handler. There is no unused Wine preference that enables pinch for this Windows copy of the game.

In a city:

1. Press **+** to zoom in or **−** to zoom out.
2. Alternatively, press a number from **1 to 6** to select one of the game's six zoom levels directly. These controls are documented on printed page 78 of the installed Windows manual.
3. Slide two fingers together vertically, then lift both fingers before the next swipe. The installed **SimCity Trackpad Zoom** Mac helper limits each vertical gesture to one wheel step. The user confirmed that this now works; it starts hidden with SimCity and stops when the game wrapper shuts down.

## Mac Game Mode

The actual operating system is **macOS 26.6.2 (25G83)**, verified with the system version tool. Earlier project notes describing macOS 15 are stale.

Game Mode can prioritise CPU and GPU access for recognised games, but it is not confirmed active for this Wine game. The user reports that Command–Esc does nothing. The outer app's game metadata does not automatically apply to its Wine child process. No app metadata was changed and no Game Mode activation is claimed.

## Zoom-delay investigation

The user reports a delay when zooming with the on-screen buttons, including a largely empty God-mode map. The game already uses hardware DirectX drawing. Power mode was normal and the system reported no thermal/performance warning. The process used about 132% CPU in one short reading; macOS measures 100% as one core, so this does not mean the whole Mac was saturated. A short activity sample is retained in game-sample.txt.

The sampled process module map placed SC4RenderServices.dll at address 0x01d90000. Frequently sampled addresses matched the custom terrain-decal clipping loop in version 0.7.1, including repeated checks of terrain-cell coordinates. The code location was a strong lead; the sample alone does not prove the complete cause of zoom delay.

## Retained performance change

Only two values were changed in Plugins/SC4RenderServices.ini:

| Setting | Original | Retained |
|---|---|---|
| EnableCustomTerrainDecalRenderer | true | false |
| LogLevel | info | error |

The first setting delegates ground-decal drawing to the game's original method. While disabled, advanced ground-painting clipping, texture-region and depth-offset behavior are unavailable. Other Render Services and Plop and Paint services remain enabled. The second setting avoids a warning written on every draw by that fallback path; error reporting remains enabled.

Resolution, native Mac window controls, fullscreen behavior and ForceDrawOnScroll=true were retained. No city saves were modified by these file changes.

**Result: the user confirmed that zooming with the buttons is much more fluent after the change.** There was no controlled FPS or zoom-latency benchmark, so no percentage improvement is claimed. Trackpad sensitivity was fixed separately by the native Mac helper.

The original settings are backed up in [before-zoom-test](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/trackpad-performance/before-zoom-test>). To reverse the performance change, first save with Control + S and quit normally through the three-dot options button. Change only the two retained values back to their original values, preserving unrelated later edits. The complete guide linked above gives the exact file and editing steps.

## Sources

- [Installed Windows manual](</Users/simonhinterreiter/Applications/SimCity 4 Windows.app/Contents/SharedSupport/prefix/drive_c/GOG Games/SimCity 4 Deluxe Edition/manual.pdf>)
- [Wine 4.12 input handling](https://github.com/wine-mirror/wine/blob/wine-4.12/dlls/winemac.drv/cocoa_app.m)
- [Apple Game Mode](https://support.apple.com/en-us/105118)
- [Apple: child processes do not inherit the launcher's game properties](https://developer.apple.com/forums/thread/787774)
- [Render Services 0.7.1 terrain drawing](https://github.com/caspervg/sc4-render-services/blob/v0.7.1/src/service/decal/ClippedTerrainDecalRenderer.cpp)
