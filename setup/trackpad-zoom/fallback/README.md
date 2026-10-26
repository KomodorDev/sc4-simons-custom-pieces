# Working SimCity scrolling helper

**Installed and user-confirmed; documentation updated 14 September 2026.** Despite this folder's historical name `fallback`, `SC4ScrollHelper.m` is the active implementation. The earlier injected Wine helpers are no longer installed. See the [complete repair guide](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/SimCity 4 - Display and Zoom Fixes.md>) for the display/performance settings and maintenance instructions.

Installed artifact: [SimCity Trackpad Zoom.app](</Users/simonhinterreiter/Applications/SimCity Trackpad Zoom.app>) (native Apple Silicon, ad hoc signed). The user enabled Accessibility access, real game attachment was verified, and the user confirmed the scrolling behavior works.

The game starts this app through the separate [StartTrackpadZoom launcher](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/trackpad-zoom/StartTrackpadZoom.m>), which waits for launch completion and explicitly hides its window. Wineskin's shutdown script stops it when the game closes. Those changes preserve the helper executable and its existing permission identity.

## Activation and permission

- Opening normally starts off; the Start button is available after Accessibility access is present.
- Launching with `--start` waits for Accessibility access, then attaches when SimCity runs. Granting permission is the only additional user step in that mode.
- Only clicking **Open Accessibility Settings** invokes the macOS permission prompt and opens the Accessibility pane. The user grants access themselves.
- Stop or closing the helper window removes its event filter. No login item or system preference is created by this application.

## Scope

The helper discovers processes using `proc_listallpids`. It accepts a process only when `proc_pidpath` places its executable inside this installed SimCity wrapper's Wine folder and the kernel argument list contains an exact `SimCity 4.exe` basename. It creates `CGEventTapCreateForPid` for that PID with only the scroll-wheel mask. It does not rely on Wine having a recognized macOS application bundle and does not create a global event tap. No keyboard events are collected or posted.

Vertical precise scrolling emits one 20-point native scroll event per gesture. Wine 4.12 multiplies that value by six, producing exactly one 120-unit Windows wheel notch. Further vertical movement and its momentum are suppressed. Horizontal intent is passed through after the initial four-point direction decision. Ordinary mouse wheel events and scrolling with modifier keys pass through.

The native event metadata identifies precise/touch scrolling rather than the exact hardware model; another precise touch scrolling device may also be capped. Phased trackpad swipes retain one step even when paused. Devices without gesture phases use a 0.6-second gap to identify a new gesture.

## Verification

The standalone `scroll-helper-test` compiles the actual normalization function and checks forward/reverse steps, large later deltas, phased pauses, momentum, horizontal intent, mouse-wheel passthrough, and modifier passthrough. It only creates local CGEvent objects; it never creates NSApplication, an event tap, or input for a game.

The status file is:

`/Users/simonhinterreiter/Documents/SimCity 4 Windows/Setup logs/Mac Trackpad Zoom status.json`

It contains permission/activation state, helper PID, target PID, whether the tap is active, and event/step/suppression counters. Writes occur on state changes or the one-second GUI timer, never from the event callback. No input contents are logged.

Actual attachment under the granted macOS permission was separately verified, and the user confirmed real trackpad swipes work. The pure-event tests alone did not establish that result. The installation and runtime verification record is [mac-helper-installation-status.json](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/trackpad-zoom/mac-helper-installation-status.json>).

A status file can survive shutdown and contain old process IDs. Check that its recorded processes are still running before treating it as evidence of current attachment.

After copying/rebuilding this generated app in an iCloud-backed Documents folder, Finder metadata may prevent signing. Remove this generated app's `com.apple.FinderInfo` attribute before re-signing; signing after installation outside Documents avoids that file-provider interference. Do not rebuild after the user grants permission unless needed, because a changed ad hoc signature may require renewed approval.

Apple's API: https://developer.apple.com/documentation/coregraphics/cgevent/tapcreateforpid(pid:place:options:eventsofinterest:callback:userinfo:)
