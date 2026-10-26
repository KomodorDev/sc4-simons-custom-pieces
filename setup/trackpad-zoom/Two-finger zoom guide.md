# Two-finger zoom in SimCity 4

Status: you confirmed two-finger zoom works. The helper starts hidden with SimCity and stops automatically when its game wrapper shuts down. Automatic stopping was tested successfully.

The [complete display and zoom repair guide](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/SimCity 4 - Display and Zoom Fixes.md>) records the exact installed settings, source files, remaining limitations, and reversal steps.

## Permission, if it ever needs to be restored

Accessibility access is already enabled. These steps are only needed if that access is lost.

1. Open **SimCity Trackpad Zoom.app** from `/Users/simonhinterreiter/Applications`. In its window, click **Open Accessibility Settings**.
2. In System Settings, allow **SimCity Trackpad Zoom** under **Privacy & Security → Accessibility**. Authenticate with your Mac password or Touch ID if asked.
3. Return to the helper and click **Start** if it says it is off. It should say **Waiting for SimCity 4** while the game is closed. When the game opens, it should say **On — one zoom step per vertical swipe in SimCity**.

If the helper is missing from the Accessibility list, click **+**, press **Command + Shift + G**, type `/Users/simonhinterreiter/Applications`, and press Return. Select **SimCity Trackpad Zoom.app**, click **Open**, then enable its switch.

## Use it

1. Open a city and put the pointer over the terrain.
2. Place two fingers on the trackpad, keeping the distance between them the same.
3. Slide both fingers up or down. The game should change by one zoom level.
4. Lift both fingers. Swipe again to change by another level.

The helper keeps your existing scroll direction. It limits repeated movement during a swipe and ignores extra vertical scrolling after you lift your fingers. It does not add pinch controls.

Open and quit SimCity normally. Its shortcut waits for the helper to finish opening, explicitly hides it, and checks that no helper window is onscreen. A failed check is recorded in the window-status file; the game can still start. Its shutdown script closes the helper after you quit the game. You do not need to manage the helper during play. Open SimCity Trackpad Zoom from your Applications folder only if you want to see its controls. **Stop** turns filtering off; closing the helper window quits it early.

The filter attaches only to the verified SimCity game process and only receives its scroll events. Ordinary mouse-wheel and horizontal scrolling pass through. In a scrollable game menu, the vertical limit sends one wheel step per swipe there too.

If you click **Stop**, click **Start** to enable scrolling again, or close the helper before opening SimCity. Opening the game can reuse an already-running helper without re-enabling it. If you open the helper manually while the game is closed, close it manually when finished.

The original Windows batch launcher, Mac window settings, and confirmed drawing-performance improvement remain in place. Earlier helpers inside Wine were removed because they did not activate reliably.

## Remove it

Quit the Mac helper, remove its StartTrackpadZoom command from the game's CLI Custom Commands field (the original value was empty), remove the helper-only block from WineskinShutdownScript, and remove only **SimCity Trackpad Zoom.app** from your Applications folder. Its installation record and the prior launcher settings are saved in this project folder. Leave the separate graphics/performance changes alone.
