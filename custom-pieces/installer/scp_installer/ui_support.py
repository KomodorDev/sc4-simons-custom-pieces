"""Operating-system and presentation helpers with no graphical dependency."""
import csv
import io
import os
from pathlib import Path
import subprocess
import sys


def default_work_root():
    if sys.platform == "win32":
        base = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData/Local"))
    else:
        base = Path.home() / ".local/share"
    return (base / "SimonsCustomPieces/Installer").expanduser().resolve()


def require_game_closed():
    """Read process names only; never terminate a game or alter its saves."""
    if sys.platform != "win32":
        return
    try:
        result = subprocess.run(["tasklist", "/FO", "CSV", "/NH"], capture_output=True,
                                timeout=15, check=True,
                                creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    except (OSError, subprocess.SubprocessError) as error:
        raise ValueError("Windows could not check whether SimCity 4 is closed. Close the game, and try again.") from error
    # Windows utilities can emit a local code page even in a UTF-8 Python
    # process. Only the two ASCII game image names matter here; replacement
    # characters in unrelated localized columns must not block this check.
    output = result.stdout.decode("ascii", errors="replace")
    processes = {row[0].casefold() for row in csv.reader(io.StringIO(output)) if row}
    if processes & {"simcity 4.exe", "simcity4.exe"}:
        raise ValueError("Close SimCity 4 before installing or undoing an installation, then try again.")


def progress_text(event, names):
    phase = event.get("phase")
    if phase == "compile":
        label = names.get(event.get("piece"), event.get("piece", "piece"))
        return f"Building {event.get('index', '?')} of {event.get('pieces', '?')}: {label}"
    return {
        "discover": "Finding your game and Plugins folders…",
        "selection": f"Preparing all {event.get('pieces', '')} implemented pieces…",
        "capture": "Reading the required resources from your installed game and NAM…",
        "audit": "Checking the installed NAM version and existing plugins…",
        "verify": "Verifying the built pieces…",
        "menu": "Preparing the trumpet assembly button…",
        "install": "Saving a backup and installing the verified pieces…",
        "undo": "Restoring the previous installation…",
        "complete": "Installed",
    }.get(phase, "Working…")
