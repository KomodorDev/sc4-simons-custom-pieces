# SimCity 4 display modes

This helper is prepared for review. It has not been installed in Applications.

1. If SimCity 4 is open, **save your city and quit the game**. Wait until its window has closed. The helper refuses to change settings while this game's launcher or game process is still running.
2. Double-click **SimCity 4 Display Mode**.
3. Click one of these buttons:
   - **Built-in Full Screen:** fills the main Mac display, normally your laptop screen. You cannot drag the game between monitors in this mode. If you changed which display is the main display in macOS, the game follows that choice.
   - **Movable Window:** opens a window that you can drag by its title bar to your external monitor. This retains the older Windows-style border required for correct pointer alignment. The Mac green fullscreen button is unavailable in this mode.
   - **Cancel:** leaves your settings unchanged.
4. When **Display mode saved** appears, click **OK**.
5. Double-click your usual **SimCity 4 Windows** game icon.

Both choices use **1920 × 1200** with the working graphics corrections. Moving the window to a 4K monitor does not change the game's resolution to 4K. On the laptop, the movable window may extend into the Dock area; **Option–Command–D** hides or shows the Dock if you need more room.

The helper changes only the graphics file's `WindowMode` value and the launcher's `-w` / `-f` flag. It preserves all other bytes, including comments and line endings. It does not touch your cities, region files, mods or registry. It does not open or close the game.

## Review and verification

The app is a small native macOS application with no Python or Terminal dependency. Its source is `Display Mode Helper.m` in this folder. Fullscreen rendering was visually verified after enabling full redraw; pointer confirmation for fullscreen remains pending. Movable-window pointer alignment was confirmed by the user.

Its executable accepts `--dry-run fullscreen` and `--dry-run windowed`. These validate the installed settings and running-game detection without writing anything. A real change stages both new files first, verifies the originals have not changed, and atomically replaces each file. If the launcher replacement fails, it restores the original graphics file. If that restoration also fails, it preserves the original in a clearly reported recovery file.

The helper intentionally refuses settings it does not recognise. If the game's location, resolution or graphics setup changes later, it must be reviewed before reuse.
