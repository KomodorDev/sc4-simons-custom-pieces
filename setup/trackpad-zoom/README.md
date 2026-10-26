# SimCity trackpad zoom — which files are current?

**Working setup documented 14 September 2026.** Start with the [complete display and zoom repair guide](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/SimCity 4 - Display and Zoom Fixes.md>). For everyday scrolling instructions, use the [two-finger zoom guide](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/trackpad-zoom/Two-finger zoom guide.md>).

## Active implementation

| File | Purpose |
|---|---|
| [fallback/SC4ScrollHelper.m](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/trackpad-zoom/fallback/SC4ScrollHelper.m>) | Source of the installed native Mac helper. Despite the historical folder name, this is the working scroll filter. |
| [fallback/README.md](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/trackpad-zoom/fallback/README.md>) | Filter behavior, permission, and local test notes. |
| [StartTrackpadZoom.m](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/trackpad-zoom/StartTrackpadZoom.m>) | Source of the short launcher that opens the helper, hides its window, verifies visibility, and exits. |
| [mac-helper-installation-status.json](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/trackpad-zoom/mac-helper-installation-status.json>) | Installation record and completed verification results. Process IDs and running-state fields are historical snapshots. |
| [verified-hidden-helper.json](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/trackpad-zoom/verified-hidden-helper.json>) | Independent visibility-check result from the completed hidden-start repair. |

The installed helper is `/Users/simonhinterreiter/Applications/SimCity Trackpad Zoom.app`. Its executable and signature were preserved when automatic hiding and stopping were added, because changing them can require renewed Accessibility permission.

The game app's `Contents/Resources/Scripts/WineskinShutdownScript` contains the automatic-stop block. The complete guide records its exact installed path, process checks, and backup location.

## Historical material

`SC4TrackpadZoom*.m`, their `.dylib` files, `install-scroll-helper.py`, `installation-status.json`, and the related constructor/preloader/run-start harnesses describe unsuccessful helpers injected into Wine. They are retained for reference and are not the installed solution. [Build notes.md](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/trackpad-zoom/Build notes.md>) describes that older experiment.

`hide-helper` and its source belong to the investigation before the final `StartTrackpadZoom` launcher. They are not the current game startup command.

Folders beginning `before-` are dated repair-stage backups. Their complete `Info.plist` files may omit later fixes. Restore only the intended field using the complete guide; do not replace the whole working configuration with an older snapshot.
