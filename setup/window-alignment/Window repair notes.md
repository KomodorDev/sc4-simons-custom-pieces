# SimCity 4 display repair — 13 September 2026

For the consolidated settings, zoom repairs, and reversal steps, see [SimCity 4 — Display and Zoom Fixes](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/SimCity 4 - Display and Zoom Fixes.md>), checked on 14 September. These notes retain the detailed display investigation.

The user accepted the final setup for the **MacBook built-in screen**. Normal Mac window controls, Mac fullscreen, swiping back to the desktop, and use of the other monitors work. Game clicks are accurate on the built-in screen. **Click alignment on external monitors remains unresolved**; the user explicitly accepted that limitation for now.

## Everyday use

1. Open **SimCity 4 Windows** using the usual desktop shortcut.
2. Keep the game on the MacBook screen for accurate clicks.
3. Click the **green circle at the upper left of the game window** to enter Mac fullscreen.
4. Use the usual three-finger horizontal swipe to return to the desktop. The user confirmed this works.
5. To leave fullscreen, move the pointer to the top of the screen so the window controls appear, then click the green circle again.

The window can be moved to another display, but its clickable areas may no longer match the picture there. This has not been fixed.

## Retained settings

| Setting | Final value |
|---|---|
| Requested game resolution | 1920 × 1200 |
| Game window mode | Windowed |
| Mac fullscreen | Enter using the green Mac window button |
| Graphics renderer and color depth | DirectX, 32-bit |
| ForceDrawOnScroll | true |
| Per-game Wine Decorated override | Removed, restoring normal native Mac controls |
| Wineskin diagnostic logging | Off, restored after testing |

ForceDrawOnScroll enables the graphics mod's compatibility settings for updating the picture. No graphics translator, display-mode helper, or new Wine engine was installed.

The game's **own exclusive fullscreen mode is disabled**. Although its picture and clicks worked after the graphics-update fix, it blacked out the other monitors and prevented normal Mac gestures. Do not restore that mode as the everyday default.

## Diagnosis and tests

- The initial capture showed clipped upper controls and a repeated strip along the bottom at 1920 × 1200.
- The game-specific Wine setting Decorated=N fixed alignment according to the user, but produced classic Windows borders and removed normal Mac fullscreen controls.
- Tests at 1920 × 1080 crashed during startup. Both fullscreen and windowed attempts produced the same game exception at address 0x0098e9a6; the exact cause was not established.
- Exclusive fullscreen at 1920 × 1200 started, but first produced repeated clouds, stale splash imagery, and damaged controls. Enabling ForceDrawOnScroll=true corrected the visible rendering, verified in game-window and built-in-display captures and confirmed by the user.
- The user rejected exclusive fullscreen because it captured all displays and interfered with gestures.
- The final test restored Windowed mode and native Mac decorations while retaining ForceDrawOnScroll=true. The user confirmed the Mac fullscreen and desktop behavior works, with accurate game clicks only on the built-in screen.

The built-in screen currently offers 2056 × 1329 logical desktop pixels, but its normal usable window area is only 2056 × 1196 after the menu bar and Dock. A requested 1200-pixel game height plus a title bar exceeds that space, so macOS may reduce the window. Earlier notes incorrectly treated the full desktop height as available window space. The two external displays each offer 2560 × 1440 logical pixels.

## Records and backups

- accepted-mac-window/: copies of the accepted graphics settings, launch file, and app settings.
- before-decoration-fix/: original settings before this investigation.
- before-game-fullscreen/: the working classic-window settings before fullscreen tests.
- verified-fullscreen/: a historical test that rendered correctly but was rejected for display capture. **Not the final setup.**
- repair-status.json: test history, exact retained settings, and the user's acceptance.
- native-full-redraw-region.png: native-window test image before the user's final confirmation.
- full-redraw-test-window.png and full-redraw-test-display.png: historical exclusive-fullscreen rendering checks.
- unused-drafts/: abandoned helper source and guide. Do not install.
- dxwrapper-staging/: unused download retained for reference. Nothing was installed.

The .reg files in this folder are historical diagnostic tools. Importing disable-native-window-trimming.reg would restore classic borders and remove normal Mac fullscreen controls; it is not part of the accepted setup. Do not replace the live registry with an old complete backup.

## Sources

- [CodeWeavers: Disable window decorations in the Mac Driver](https://support.codeweavers.com/disable-window-decorations-in-the-mac-driver)
- [Wine 4.12 Mac driver settings](https://github.com/wine-mirror/wine/blob/wine-4.12/dlls/winemac.drv/macdrv_main.c)
- [SC4 Graphics Options and compatibility options](https://github.com/0xC0000054/sc4-graphics-options)
