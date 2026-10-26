# Rebuild SimCity Content helper

This native Mac app runs the installed Plop and Paint content builder. It refreshes the list of installed objects and their preview pictures; it does not start or close SimCity 4.

1. After installing or removing mods, quit SimCity 4.
2. Open **Rebuild SimCity Content**.
3. Click **Rebuild** and keep the game closed.
4. Wait until the app says **Finished**. You can then close the helper and start the game.
5. Inside a city, press **O** to open Plop and Paint.

The builder runs from `/Users/simonhinterreiter/Applications/SC4 Plop and Paint Tools`, so its `PropertyMapper.xml` file can be found. It scans the Windows game's installation and Plugins folders, uses English labels, and renders 44-pixel thumbnails.

The complete output from the latest rebuild is saved at:

`/Users/simonhinterreiter/Documents/SimCity 4 Windows/Setup logs/Plop and Paint cache rebuild.log`

The window shows short progress messages and counts. Technical details stay in the complete log. Missing previews, unreadable content, and additional warnings are summarized in the window so they are not silently discarded.

## Limits

- This helper is specific to Simon's current Mac paths and Wine game installation.
- It checks for the existing Wine game's process name before starting. Keep the game closed yourself throughout the rebuild.
- A lock folder prevents two copies of this helper from rebuilding at once. A builder started directly outside the helper does not participate in that lock.
- Force-quitting the helper or shutting down during a rebuild can leave its lock folder behind. Only after confirming that no builder is running, remove `/Users/simonhinterreiter/Applications/SC4 Plop and Paint Tools/.cache-rebuild.lock` before trying again.
- Normal Close and Quit are disabled during a rebuild, so they cannot interrupt the builder accidentally.
- The helper reports the builder's exit code. A successful rebuild does not by itself prove that the in-game overlay can render correctly in Wine.
- It keeps the full output of the latest started rebuild in its log. It does not maintain a history of older logs. Refused attempts (for example, while the game is open) leave the previous log intact.

## Build and verification

The source uses Apple's AppKit and Foundation frameworks. It has no additional library dependencies. Run `sh build.sh` from this folder to compile the Apple Silicon app, apply a local ad hoc signature, and check the resulting bundle without opening it.

The installed Command Line Tools contain two definitions of `SwiftBridging`. `swift-overlay.json` hides the older duplicate from this compiler invocation only. The original toolchain files remain unchanged. The overlay and the compiler's temporary module cache are only build inputs; they are not needed when running the finished app.

This subtask produces an app bundle in this folder only. Installing it into Applications and checking the visible window are handled separately. No rebuild or game launch was performed while creating it.
