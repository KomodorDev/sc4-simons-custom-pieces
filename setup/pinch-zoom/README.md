> Historical experiment: the pinch helper was removed at the user’s request. The working solution is the native Mac two-finger scrolling helper. See the [complete display and zoom repair guide](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/SimCity 4 - Display and Zoom Fixes.md>). The older pinch instructions below are retained only as a development record and do not describe the installed setup.

# SimCity 4 pinch bridge — staged for review

This folder contains a small Mac library that translates a pinch into one SimCity 4 zoom step. It has not been installed or tested inside the game.

The library uses only the running game's own Mac event queue. It does not use a global input monitor, Accessibility access, or system-wide event posting. Three-finger gestures, fullscreen controls, and two-finger scrolling are outside its input mask.

## Activation and behavior

- The constructor returns immediately unless `SC4_PINCH_ENABLED=1` and a complete process argument has the exact basename `SimCity 4.exe`. Both Windows and Mac path separators are accepted.
- It waits for Wine's existing `WineApplication`; it never creates an application object itself. Readiness polling stops after 60 seconds.
- Pinches are accepted only while the application is active and its key `WineWindow` is titled `SimCity 4` (case-insensitive). Shift, Control, Option, or Command suppresses translation.
- Magnification accumulates to `+0.12` or `-0.12`, then queues keypad Plus or Minus key-down and key-up events to that window. The gesture can produce only one step before it ends.
- Explicit gesture phases and generic beginning/end markers reset the state. For older streams without phases, a 0.6-second gap supplies a fallback boundary. Losing application focus also resets it.
- `SC4_PINCH_STATUS` may name an absolute path for an optional JSON status file. The directory must already exist. The file contains only bridge state, its process ID, event/step counters, threshold, and update time. Writes are limited to four per second during continuous input, plus zoom steps, gesture completion, and lifecycle changes. A status file can remain after the process exits; check its PID before treating it as current.

Use the staged **x86_64** library with Wine's x86_64 Mac process. Do not install or restart the game solely on the strength of the console test: real pinch delivery, the title guard, startup loading, and the game's response remain integration checks.

## Build and isolated verification

Run these commands from the project folder. They create or update files only in this staging folder.

```sh
/usr/bin/clang -fno-modules -fobjc-arc -arch x86_64 -dynamiclib -framework Cocoa -mmacosx-version-min=10.13 -O2 -Wall -Wextra 'setup/pinch-zoom/SC4PinchZoom.m' -o 'setup/pinch-zoom/SC4PinchZoom.dylib'
```

```sh
/usr/bin/clang -fno-modules -fobjc-arc -arch x86_64 -DSC4_PINCH_TEST -framework Cocoa -mmacosx-version-min=10.13 -O2 -Wall -Wextra 'setup/pinch-zoom/SC4PinchZoom.m' -o 'setup/pinch-zoom/sc4-pinch-test'
```

```sh
'setup/pinch-zoom/sc4-pinch-test'
```

Expected result:

```text
PASS: pinch state, process arguments, and keypad events; no NSApp created or events posted.
```

The test checks threshold accumulation, both directions, one step during a continuous or paused phased gesture, phase-less timeout recovery, cancellation, boundary/focus reset, invalid numeric input, exact argument matching, and all generated keypad event fields. Its constructor and monitor code are excluded at compile time; it never posts events.
