# SimCity 4 — display and zoom fixes

**Working setup documented and saved settings checked: 14 September 2026.**

This is the main reference for the resolution, fullscreen, zoom speed, and two-finger scrolling repairs made on 13–14 September. The user confirmed that the resulting display setup and two-finger zoom work, and accepted the final hidden-helper behavior. This documentation update did not change the game or launch it.

## 1. What works now

| Area | Current result |
|---|---|
| Game picture | Requested resolution is **1920 × 1200**, with the graphics compatibility setting below enabled. |
| Fullscreen | Use the **green Mac window button**. The game itself remains configured as **Windowed**. |
| Desktop and other monitors | Mac fullscreen allows the confirmed three-finger swipe back to the desktop and leaves the other displays usable. |
| Mouse clicks | Accurate on the **MacBook’s built-in display**. Alignment on external displays remains unresolved. |
| Zoom drawing speed | The user confirmed that the on-screen zoom buttons became much more fluent after the Render Services change. |
| Trackpad zoom | **One zoom level per two-finger vertical swipe**. Lift both fingers before the next swipe. |
| Pinch | No pinch control is installed; the user chose ordinary two-finger scrolling. |
| Zoom helper | Starts with SimCity, its window is explicitly hidden, and it is stopped when the game wrapper shuts down. |

The game is the **Windows GOG edition of SimCity 4 Deluxe, version 1.1.641.0**, running through **Wineskin 3.0.6_2 / Wine 4.12.1, engine WS11WineCX19.0.2-3** on an Apple M1 Max MacBook Pro. Wine supplies the Windows functions the game needs. A *wrapper* is the Mac app containing Wine, the game, and their launch settings. The recorded macOS version is **26.6.2 (25G83)**.

## 2. Everyday use

1. Open **SimCity 4 Windows** using the usual desktop shortcut. It starts the zoom helper automatically.
2. Keep the game on the **built-in MacBook screen** for accurate clicks.
3. For Mac fullscreen, click the **green circle at the upper left** of the game window. To leave fullscreen, move the pointer to the top of the screen to reveal the controls, then click the green circle again.
4. In a city, place the pointer over the map. Slide two fingers up or down together, keeping the distance between them the same. Lift both fingers, then repeat to change another zoom level.
5. Save with **Control + S**. Quit through the game’s **three-dot options button at the bottom left**. The wrapper’s shutdown script then stops the zoom helper.

There is no separate helper window to manage during normal play. Its controls can still be opened deliberately from **SimCity Trackpad Zoom.app** in the user’s Applications folder. Clicking **Stop** disables its scrolling filter; closing that helper window quits it. After clicking Stop, click **Start** to enable scrolling again, or close the helper before launching SimCity. Starting the game can reuse an already-running helper without turning it back on. If it is opened manually while no game is running, close it manually afterward—the automatic cleanup is tied to SimCity’s shutdown.

**External-display limitation:** moving the game to a 4K monitor can make its clickable areas differ from the displayed buttons. This was accepted as an outstanding issue, not fixed. Do not describe external-monitor play as verified.

## 3. Resolution, window borders, and fullscreen

### The problem and the final fix

The initial symptoms included cut-off controls, a repeated strip along the bottom, and clicks landing somewhere other than the visible buttons. Some trial settings corrected one symptom while causing others.

The accepted combination is **1920 × 1200 Windowed**, **normal native Mac window controls**, and **ForceDrawOnScroll=true**. The last setting enables fuller picture updates in the Graphics Options mod and corrected the stale or damaged drawing seen during testing.

The distinction between the two fullscreen modes matters:

- **Mac fullscreen:** enter with the green Mac window button. This is the accepted mode.
- **The game’s exclusive fullscreen:** selects the game’s `-f` / `FullScreen` mode. It took over the other monitors and interfered with desktop gestures. It is disabled.

The built-in display was measured on 13 September as 3456 × 2234 physical pixels, with a 2056 × 1329 logical desktop and approximately 2056 × 1196 usable window space after the menu bar and Dock. *Logical pixels* are the coordinates macOS gives applications after display scaling. A requested 1200-pixel game height plus a title bar can exceed the normal usable window area. These are recorded measurements, not a promise that every future display arrangement has the same dimensions.

### Exact retained settings

An **INI file** is a plain-text settings file containing named values. In the live [SC4GraphicsOptions.ini](</Users/simonhinterreiter/Documents/SimCity 4 Windows/Plugins/SC4GraphicsOptions.ini>), the existing keys are:

```ini
ForceDrawOnScroll=true
Driver=DirectX
WindowWidth=1920
WindowHeight=1200
ColorDepth=32
WindowMode=Windowed
```

These keys already belong to sections in that file. Do not replace the whole file with this short excerpt.

The live [launch-sc4.bat](</Users/simonhinterreiter/Applications/SimCity 4 Windows.app/Contents/drive_c/launch-sc4.bat>) is:

```bat
@echo off
cd /d "C:\GOG Games\SimCity 4 Deluxe Edition\Apps"
"SimCity 4.exe" -UserDir:C:\SC4UserData\ -w -CustomResolution:enabled -r1920x1200x32 -intro:off -CPUCount:1 -d:DirectX
```

A **batch file** is a list of Windows commands. Here it selects the game’s own folder and starts the game with the Windows user profile, windowed mode, custom resolution, no opening movie, one-CPU option, and DirectX drawing. `C:\SC4UserData` maps to the real [SimCity 4 Windows profile](</Users/simonhinterreiter/Documents/SimCity 4 Windows>).

Wine’s **registry** is its Windows-style settings database. The game-specific key below exists with **no `Decorated` value**:

```text
HKEY_CURRENT_USER\Software\Wine\AppDefaults\SimCity 4.exe\Mac Driver
```

Removing the temporary `Decorated=N` override restored the normal Mac window controls. The saved registry also retains global `UsePreciseScrolling=N` and font DPI 96, with no Retina override. These were checked as existing settings; they are not the new one-swipe zoom fix. Wineskin **Debug Mode=false** is retained.

### Approaches that are not the final setup

| Trial | Outcome |
|---|---|
| `Decorated=N` | Improved alignment in that trial, but gave old Windows-style borders and removed normal Mac fullscreen controls. Removed. |
| 1920 × 1080 | Windowed and fullscreen attempts crashed during startup. The exact cause was not established. |
| 1920 × 1200 exclusive fullscreen | Rendered correctly after the redraw fix, but blacked out other displays and blocked normal desktop gestures. Rejected. |
| DxWrapper or a replacement display-mode helper | Downloads/drafts were retained for investigation only. They were not installed. |

The accepted graphics INI and batch file still match the copies in [accepted-mac-window](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/window-alignment/accepted-mac-window>). Its old `Info.plist` predates the final zoom-helper launch integration, so it must not replace the complete current app configuration.

## 4. Why zooming became faster

The slow zoom buttons were a separate issue from trackpad sensitivity. A short activity sample repeatedly found work in **Render Services 0.7.1’s custom terrain-decal clipping code**. A *terrain decal* is an image drawn on top of the ground, such as ground paint.

Two values were changed in the live [SC4RenderServices.ini](</Users/simonhinterreiter/Documents/SimCity 4 Windows/Plugins/SC4RenderServices.ini>):

| Key | Before | Retained value | Reason |
|---|---|---|---|
| `EnableCustomTerrainDecalRenderer` | `true` | **`false`** | Uses the game’s original ground-decal drawing path instead of the expensive custom clipping path. |
| `LogLevel` | `info` | **`error`** | Prevents that fallback path from writing a warning on every draw. Error reporting remains enabled. |

The user confirmed that zooming with the buttons became **much more fluent**. No controlled FPS or zoom-latency benchmark was performed, so there is no claimed percentage improvement.

**Tradeoff:** advanced ground-decal clipping, texture-region selection, and depth-offset behavior are unavailable with the custom renderer disabled. Render Services remains installed; other Render Services and Plop and Paint functions, including building tools, remain enabled. This did not remove the entire ground-painting mod.

Mac Game Mode was not confirmed active. The user reported that Command–Esc did nothing. The performance result above does not depend on a claimed Game Mode activation.

## 5. How two-finger zoom was fixed

### The active Mac helper

The installed app is [SimCity Trackpad Zoom.app](</Users/simonhinterreiter/Applications/SimCity Trackpad Zoom.app>). Its final source is [SC4ScrollHelper.m](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/trackpad-zoom/fallback/SC4ScrollHelper.m>). **Despite the source folder’s historical name `fallback`, this is the working, installed implementation.**

The original Wine scrolling could turn one swipe into several zoom levels. The native Apple Silicon helper now:

1. Finds the actual SimCity process by checking both its executable path inside this wrapper and the exact `SimCity 4.exe` argument.
2. Attaches a **process-specific event filter**: a function that can adjust scrolling sent to that game process. The macOS API used is `CGEventTapCreateForPid`, with only the scroll-wheel event mask.
3. Waits for four accumulated movement points to decide whether the gesture is vertical or horizontal.
4. For a vertical swipe, sends one native scroll event of **+20 or −20 points**. This Wine driver multiplies it by six, producing **+120 or −120 Windows wheel units**: one wheel notch and one game zoom step.
5. Suppresses the rest of that vertical gesture and its **momentum**, meaning scrolling that continues after the fingers lift.

Explicit gesture boundaries allow another step on the next swipe. A device without those boundaries uses a 0.6-second gap as a fallback. Horizontal movement passes through after the initial direction decision; its first movement below the four-point threshold is buffered. Ordinary noncontinuous mouse-wheel events and scrolling with Shift, Control, Option, or Command pass through.

The filter also applies to vertical scrolling over the game’s menus. Another device that produces precise touch-scroll events may be limited too; detection is based on event metadata, not the physical trackpad model. It does not collect or generate keyboard events, install pinch handling, or change global Mac scrolling preferences.

### Permission and application identity

The user enabled **System Settings → Privacy & Security → Accessibility → SimCity Trackpad Zoom**. This permission lets the helper adjust the game’s input. The actual filter is restricted to the verified game process.

The helper has a local, **ad hoc code signature**: an identity attached to its executable. Its current permission was granted to that identity. Rebuilding or re-signing the helper can require renewed permission. The later hidden-window and automatic-quit fixes therefore leave that working app’s binary and signature untouched.

### Automatic start, hidden window, and automatic stop

The final startup chain is:

```text
SimCity desktop shortcut
  → Wineskin launcher
  → StartTrackpadZoom opens the Mac helper with --start
  → waits for launch completion, hides it, verifies hidden state
  → Windows batch file starts SimCity
  → helper attaches to the game’s scroll events
```

The short native launcher is installed as [Resources/StartTrackpadZoom](</Users/simonhinterreiter/Applications/SimCity 4 Windows.app/Contents/Resources/StartTrackpadZoom>); its source is [StartTrackpadZoom.m](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/trackpad-zoom/StartTrackpadZoom.m>).

In the wrapper’s [Info.plist](</Users/simonhinterreiter/Applications/SimCity 4 Windows.app/Contents/Info.plist>), a **property list** containing app settings, the exact current launch fields are:

| Field | Value |
|---|---|
| `Program Name and Path` | `/windows/system32/cmd.exe` |
| `Program Flags` | `/c C:/launch-sc4.bat` |
| `use start.exe` | `0` |
| `CLI Custom Commands` | `'/Users/simonhinterreiter/Applications/SimCity 4 Windows.app/Contents/Resources/StartTrackpadZoom';` |

The final semicolon is intentional. The native launcher advances the Mac main event loop while checking startup; macOS updates application visibility properties on those event-loop turns. After the helper finishes launching, it explicitly hides the same verified process and requires **hidden=true plus zero helper windows in an OnScreenOnly query for 0.8 seconds**. Its total wait is bounded at ten seconds; it exits afterward. It does not continuously fight someone deliberately reopening the helper’s controls.

Simply using `open -g -j` was insufficient: the helper explicitly showed its own window at startup. The first visibility check also wrongly treated missing window metadata as proof of invisibility. The final check uses the actual application hidden state and an explicit onscreen-window list. A fresh helper start and a later independent check passed while the existing city stayed open and scrolling remained attached. The user then accepted the result.

When Wineskin shuts down, [WineskinShutdownScript](</Users/simonhinterreiter/Applications/SimCity 4 Windows.app/Contents/Resources/Scripts/WineskinShutdownScript>) finds processes named `SC4ScrollHelper`, verifies the **full exact installed helper executable path**, then sends only that helper a termination signal. This stops its event filter without affecting the game or unrelated apps. Automatic stopping was tested. It creates no login item or permanent background watcher.

### Experiments that were removed

The pinch helper and later `SC4TrackpadZoom.dylib` helpers injected into Wine did not activate reliably. They were removed from the game’s Resources folder and launch command. Constructor, timer, direct-game-launch, and preloader experiments remain as historical source and diagnostic files; they are not the installed solution. Wine’s additional launch/re-exec stages were investigated, but the exact cause of every failed initialization was not conclusively established.

The final wrapper is back to the original Windows batch launch above. It contains **no `DYLD_INSERT_LIBRARIES` injection for a zoom helper**. Do not reinstall old `.dylib` experiments or replace the final launcher with the discarded direct-game settings.

## 6. Troubleshooting and maintenance

### If clicking or fullscreen breaks

1. Move the game back to the MacBook’s built-in display.
2. Use the green Mac fullscreen button. Do not switch the game’s INI to `FullScreen` or replace `-w` with `-f`.
3. If settings need repair, save with Control + S and quit the game first.
4. In Finder, choose **Go → Go to Folder**, enter `/Users/simonhinterreiter/Documents/SimCity 4 Windows/Plugins`, then press Return.
5. Right-click `SC4GraphicsOptions.ini`, choose **Open With → TextEdit**, and compare its existing keys with section 3. Change only those values and press **Command + S**. Keep it as plain text; if TextEdit offers **Format → Make Plain Text**, choose that before saving.
6. Reopen SimCity and check the built-in screen. A persistent external-display offset remains the documented limitation.

### If vertical scrolling becomes too sensitive again

Open the following status file in the project/file viewer: [Mac Trackpad Zoom status.json](</Users/simonhinterreiter/Documents/SimCity 4 Windows/Setup logs/Mac Trackpad Zoom status.json>).

While the game and helper are actually running, expect `accessibility_trusted` and `tap_active` to be true, `target_pid` to identify SimCity, and the step counters to increase once per vertical gesture. A **PID** is a temporary process identification number; it changes on restart. Always check that the recorded processes still exist. A saved status file alone does not prove that a helper is currently running, particularly after termination by the shutdown script.

To check a recorded PID, open **Terminal** from **Applications → Utilities**. Type `/bin/ps -ww -p 12345 -o pid=,comm=`, replacing `12345` with the actual `helper_pid` number, then press Return. A running helper should produce a line containing that number and the installed `SC4ScrollHelper` executable path. No output means that PID is no longer running; a different executable means the number has been reused. Repeat with `target_pid`; its executable should be inside this SimCity wrapper’s Wine folder. This checks process existence, while `tap_active` reports whether the helper attached its filter.

If permission was lost, deliberately open **SimCity Trackpad Zoom.app**, click **Open Accessibility Settings**, and enable that app in the Accessibility list. If it is not listed, click **+**, press **Command + Shift + G**, enter `/Users/simonhinterreiter/Applications`, press Return, select **SimCity Trackpad Zoom.app**, and click **Open**. Authenticate if macOS asks. For a manually opened helper, click **Start** afterward.

If the hidden-window behavior fails, inspect [Trackpad Window status.json](</Users/simonhinterreiter/Documents/SimCity 4 Windows/Setup logs/Trackpad Window status.json>). A successful check has `verified_hidden=true`, `hidden=true`, `launch_finished=true`, and `onscreen_helper_windows=0`. The game can continue starting after a failed helper check; a running game alone is not proof that this check succeeded.

### Temporarily disable or restore the scroll helper

First save and quit SimCity. These commands change **only** its custom helper launch field. To run one, open **Terminal** from **Applications → Utilities**, paste the complete command, and press Return.

Disable automatic helper startup:

```sh
/usr/bin/plutil -replace 'CLI Custom Commands' -string '' '/Users/simonhinterreiter/Applications/SimCity 4 Windows.app/Contents/Info.plist'
```

Restore the final helper startup:

```sh
/usr/bin/plutil -replace 'CLI Custom Commands' -string "'/Users/simonhinterreiter/Applications/SimCity 4 Windows.app/Contents/Resources/StartTrackpadZoom';" '/Users/simonhinterreiter/Applications/SimCity 4 Windows.app/Contents/Info.plist'
```

The existing shutdown block may remain during a temporary disable; it has nothing to stop if the helper is not running. The separate drawing-performance fix remains active.

### Revert the drawing-performance change

Save and quit the game. Use Finder’s **Go → Go to Folder** to open the Plugins folder given above, then open `SC4RenderServices.ini` with **TextEdit**. Change only `EnableCustomTerrainDecalRenderer=false` back to `true` and `LogLevel=error` back to `info`, save with Command + S, and reopen the game. This restores the earlier drawing configuration and can reintroduce the slow zoom behavior. Keep all other lines unchanged.

## 7. Files, backups, and evidence

| Purpose | Location in this project |
|---|---|
| Display investigation and accepted settings | [setup/window-alignment](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/window-alignment>) |
| Accepted graphics INI and launch batch | [accepted-mac-window](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/window-alignment/accepted-mac-window>) |
| Original Render Services settings | [before-zoom-test](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/trackpad-performance/before-zoom-test>) |
| Performance sample and test notes | [Zoom and performance notes.md](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/trackpad-performance/Zoom and performance notes.md>) |
| Working Mac helper source and local gesture checks | [setup/trackpad-zoom/fallback](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/trackpad-zoom/fallback>) |
| Hidden-start launcher source | [StartTrackpadZoom.m](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/trackpad-zoom/StartTrackpadZoom.m>) |
| Installed-helper record | [mac-helper-installation-status.json](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/trackpad-zoom/mac-helper-installation-status.json>) |
| App settings before Mac helper integration | [before-mac-helper](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/trackpad-zoom/before-mac-helper>) |
| Shutdown script before automatic helper stopping | [before-auto-stop](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/trackpad-zoom/before-auto-stop>) |
| App settings before the final hidden-start launcher | [before-verified-hidden-start](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/trackpad-zoom/before-verified-hidden-start>) |

**Backup rule:** older complete `Info.plist` or registry files can undo later working repairs. Restore individual intended settings, not a whole old configuration blindly. `verified-fullscreen` contains a rejected fullscreen trial; `setup/pinch-zoom` and the injected-library sources are historical experiments. The active helper is the Mac app identified in section 5.

**Verification scope:** the display INI, batch file, app settings, registry values, installed helper, and native hidden-start launcher were read back on 14 September. Display acceptance and improved zoom performance are user-confirmed results from the repair session. Gesture logic had independent local tests and then a successful real trackpad test. Hidden startup and automatic helper stopping were tested separately. No external-monitor alignment fix, continuous zoom, or Game Mode activation is claimed.
