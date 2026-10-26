# SimCity 4 trackpad scroll control

`SC4TrackpadZoom.m` is the current scroll-only implementation. It contains no pinch handling, keyboard simulation, global event monitor, or system event posting. The earlier `SC4PinchZoom` files are superseded experiments.

## Behavior

- A vertical two-finger gesture produces one Windows wheel step after 4 accumulated trackpad points. Continuing that gesture does not produce further steps, including after a pause. Vertical momentum is discarded.
- After the first 4 points, the larger accumulated axis selects the gesture direction. Horizontal gestures then pass through normally, including their momentum. Small horizontal jitter does not change a gesture already classified as vertical.
- Ordinary mouse-wheel events pass through. Events with Shift, Control, Option, or Command held also pass through.
- Changes apply only while the active key Wine window is titled `SimCity 4`. Other windows and Mac gestures are untouched.
- For streams without explicit gesture phases, 0.6 seconds without movement supplies a new-gesture boundary. Explicitly phased gestures use their actual beginning/end/cancellation markers.

The library intercepts Wine 4.12's `WineApplicationController.handleScrollWheel:` method. For the single allowed vertical step, it gives the original handler an Objective-C proxy with a copied graphics event: vertical point delta is +20 or -20, horizontal delta is zero, and continuous-scroll mode is enabled. Wine multiplies the point delta by six, producing exactly +120 or -120 Windows wheel units. The original event's position, window, time, and modifiers remain available. The proxy is never submitted to AppKit or the system event queue.

## Startup and diagnostics

The library is x86_64, matching the Wine Mac process. Enable it only in the intended game launch using `SC4_TRACKPAD_ENABLED=1` and an absolute `SC4_TRACKPAD_STATUS` path. The status directory must already exist.

Before using Objective-C, the constructor checks for an argument whose exact basename is `SimCity 4.exe`. It checks both C runtime arguments and this process's kernel argument list; it does not inspect or record other processes or environment contents. A C bootstrap record is written to `<status path>.bootstrap.<PID>.json`, containing only its process ID, argument count, and guard/result booleans. Nonmatching processes stop there.

A timer added directly to the main Core Foundation run loop waits for Wine's application object. It does not use a dispatch queue or create `NSApplication`. Readiness attempts stop after approximately 60 seconds. The main status file reports `scroll_hook_installed` plus the hook's own counters. A stale file can survive process exit; compare its PID to the running game before using it as current evidence.

## Build and standalone checks

From the project folder:

```sh
/usr/bin/clang -fno-modules -fobjc-arc -arch x86_64 -dynamiclib -framework Cocoa -mmacosx-version-min=10.13 -O2 -Wall -Wextra 'setup/pinch-zoom/SC4TrackpadZoom.m' -o 'setup/pinch-zoom/SC4TrackpadZoom.dylib'
```

```sh
/usr/bin/clang -fno-modules -fobjc-arc -arch x86_64 -DSC4_TRACKPAD_TEST -framework Cocoa -mmacosx-version-min=10.13 -O2 -Wall -Wextra 'setup/pinch-zoom/SC4TrackpadZoom.m' -o 'setup/pinch-zoom/sc4-trackpad-test'
```

```sh
'setup/pinch-zoom/sc4-trackpad-test'
```

Expected output:

```text
PASS: scroll state, process arguments, and exact 120-unit scroll proxy; no NSApp created or events posted.
```

The standalone checks verify gesture accumulation and gating, direction, phase-less timeout recovery, exact argument matching, proxy output of exactly one Windows wheel step, preservation of position/window/time/modifiers, and absence of an application object or posted input. The separate integration harness exercises the actual method hook and window guards. Real trackpad delivery and game behavior require confirmation in the running game.
