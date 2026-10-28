"""Discover a supported installation, build locally, and use the owned installer.

No NAM or game archive is bundled, downloaded, or modified. Folder discovery
is deliberately bounded to the selected game, its Wine prefix, and documented
player-data locations; ambiguous locations require another explicit selection.
"""
from __future__ import annotations

from dataclasses import dataclass
import ctypes
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import uuid

from scp import jsonc
from scp.catalog import load_catalog, select_pieces, safe_relative
from scp.dbpf import pack_dbpf
from scp.install import FOLDER, _owned
from scp.subject_identity import canonical_subject_id


class InstallationCancelled(ValueError):
    """Cancellation before the final owned-folder transaction."""


class PlayerDataSelectionRequired(ValueError):
    """Keep the selected game and ask explicitly for its active player data."""

    def __init__(self, message, candidate_paths):
        super().__init__(message)
        self.candidate_paths = [str(path) for path in candidate_paths]


@dataclass(frozen=True)
class Installation:
    game_folder: Path
    plugins: Path
    extra_plugins: tuple[Path, ...]
    host_platform: str
    game_kind: str = "windows"

    def as_dict(self):
        return {"game_folder": str(self.game_folder), "plugins": str(self.plugins),
                "extra_plugins": [str(path) for path in self.extra_plugins],
                "host_platform": self.host_platform, "game_kind": self.game_kind}


def _child(folder, name):
    """Find one direct child, preserving case-insensitive Windows names on Wine."""
    if folder is None or not folder.is_dir():
        return None
    matches = [path for path in folder.iterdir() if path.name.casefold() == name.casefold()]
    if len(matches) > 1:
        raise ValueError(f"More than one {name} exists in {folder}. Select an unambiguous installation.")
    return matches[0] if matches else None


def _game(folder):
    archive = _child(folder, "SimCity_3.dat")
    if archive is None or not archive.is_file():
        return False
    for base in (folder, _child(folder, "Apps")):
        if base is not None:
            for name in ("SimCity 4.exe", "SimCity4.exe"):
                executable = _child(base, name)
                if executable is not None and executable.is_file():
                    return True
    return False


def _documents(home):
    """Resolve redirected Windows Documents rather than guessing its spelling."""
    if sys.platform == "win32":
        buffer = ctypes.create_unicode_buffer(32768)
        # CSIDL_PERSONAL is the shell's current Documents known folder,
        # including OneDrive or an administrator's folder redirection.
        result = ctypes.windll.shell32.SHGetFolderPathW(None, 0x0005, None, 0, buffer)
        if result != 0 or not buffer.value:
            raise ValueError("Windows could not locate Documents. Select your SimCity 4 player-data folder instead.")
        return Path(buffer.value)
    return home / "Documents"


def _prefix(folder):
    for parent in (folder, *folder.parents):
        if parent.name.casefold() == "drive_c":
            return parent.parent
        drive = _child(parent, "drive_c")
        if drive is not None and drive.is_dir():
            return parent
    return None


def _registered_games():
    """Read only explicit Windows App Paths and SimCity 4 installation keys."""
    if sys.platform != "win32":
        return []
    import winreg
    result = []
    names = ((r"SOFTWARE\Maxis\SimCity 4", ("Install Dir", "InstallDir")),
             (r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\SimCity 4.exe", ("Path", "")))
    for hive in (winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE):
        for view in (winreg.KEY_WOW64_32KEY, winreg.KEY_WOW64_64KEY):
            for name, values in names:
                try:
                    with winreg.OpenKey(hive, name, 0, winreg.KEY_READ | view) as key:
                        for value in values:
                            try:
                                path = Path(winreg.QueryValueEx(key, value)[0])
                            except (OSError, TypeError):
                                continue
                            result.extend((path, path.parent, path.parent.parent))
                except OSError:
                    continue
    return result


def _prefix_games(prefix):
    if prefix is None:
        return []
    drive = _child(prefix, "drive_c")
    if drive is None:
        return []
    result = []
    for base in drive.iterdir():
        if base.is_dir() and base.name.casefold().startswith(("program files", "gog games", "games")):
            # Search only this explicitly selected Wine/CrossOver prefix,
            # never all bottles, the home directory, or Wine's dosdevices.
            for archive in base.rglob("*"):
                if archive.name.casefold() == "simcity_3.dat" and archive.is_file():
                    result.append(archive.parent)
    return result


def _one_game(candidates):
    found = sorted({path.resolve() for path in candidates if _game(path)})
    if len(found) != 1:
        detail = "Several game installations were found" if found else "The Windows game files were not found"
        raise ValueError(f"{detail}. Select the game folder containing SimCity_3.dat and Apps/SimCity 4.exe.")
    return found[0]


def _data_plugins(data):
    if data.name.casefold() == "plugins" and data.is_dir():
        return data
    plugins = _child(data, "Plugins")
    return plugins if plugins is not None and plugins.is_dir() else None


def discover_installation(selected, *, platform=None, home=None, documents=None, player_data=None):
    """Find the game's two loading roots without guessing between user profiles."""
    host = platform or sys.platform
    home = Path(home or Path.home()).expanduser().resolve()
    selected = Path(selected).expanduser()
    if not selected.exists():
        raise ValueError("That folder does not exist. Select your installed SimCity 4 game folder.")
    selected = selected.resolve()
    if selected.is_file():
        selected = selected.parent
    if selected.suffix.casefold() == ".app" or (selected / "Contents/MacOS").is_dir():
        raise ValueError("The native macOS edition is not supported by the audited NAM 50 Windows profile. This release targets SimCity 4 Deluxe for Windows.")
    prefix = _prefix(selected)
    near = [selected, selected.parent]
    direct_game = [path for path in near if _game(path)]
    game = _one_game(direct_game or [*_registered_games(), *_prefix_games(prefix)])
    if host == "darwin" and prefix is None:
        # A Windows installation's files can be outside its prefix; selecting
        # an existing Documents/SimCity 4 Windows folder below is still valid.
        game_kind = "windows-under-wine"
    else:
        game_kind = "windows-under-wine" if prefix is not None else "windows"
    game_plugins = _child(game, "Plugins")
    direct_plugins = _data_plugins(selected)
    if player_data is not None:
        supplied_data = Path(player_data).expanduser()
        if not supplied_data.is_dir():
            raise ValueError("The selected player-data folder does not exist. Select your existing SimCity 4 player-data folder, or its Plugins folder.")
        explicit_plugins = _data_plugins(supplied_data.resolve())
        if explicit_plugins is None:
            raise ValueError("That player-data folder has no Plugins folder. Select its existing Plugins folder, or start the game once so it creates the player-data folders.")
        if game_plugins is not None and explicit_plugins.resolve() == game_plugins.resolve():
            raise ValueError("Select the Plugins folder in your SimCity 4 player data, rather than the Plugins folder inside the game installation.")
        candidates = [explicit_plugins]
    elif direct_plugins is not None and direct_plugins.resolve() != (game_plugins.resolve() if game_plugins else None):
        candidates = [direct_plugins]
    else:
        try:
            docs = Path(documents).expanduser().resolve() if documents is not None else _documents(home)
        except ValueError as error:
            raise PlayerDataSelectionRequired(str(error) + " Choose your existing player-data or Plugins folder.", []) from error
        candidates = []
        for base in (docs / "SimCity 4", docs / "SimCity 4 Windows"):
            candidate = _data_plugins(base)
            if candidate:
                candidates.append(candidate)
        if prefix is not None:
            users = _child(_child(prefix, "drive_c"), "users")
            if users is not None and users.is_dir():
                for user in users.iterdir():
                    if not user.is_dir() or user.name.casefold() in ("public", "default", "default user", "all users"):
                        continue
                    for docs_name in ("Documents", "My Documents"):
                        data = _child(user, docs_name)
                        if data is None:
                            continue
                        for name in ("SimCity 4", "SimCity 4 Windows"):
                            candidate = _data_plugins(data / name)
                            if candidate:
                                candidates.append(candidate)
    candidates = sorted({path.resolve() for path in candidates
                         if path.resolve() != (game_plugins.resolve() if game_plugins else None)})
    if len(candidates) != 1:
        reason = "Several player-data folders exist" if candidates else "No player-data Plugins folder was found"
        raise PlayerDataSelectionRequired(f"{reason}. Choose the SimCity 4 player-data folder you use, or its Plugins folder. Start the game once first if it has not created that folder.", candidates)
    plugins = candidates[0]
    extras = () if game_plugins is None or game_plugins.resolve() == plugins else (game_plugins.resolve(),)
    if any(path == plugins or plugins in path.parents or path in plugins.parents for path in extras):
        raise ValueError("The game and player-data Plugins folders overlap. Select separate original game and player-data folders.")
    return Installation(game, plugins, extras, host, game_kind)


def all_implemented_ids(root):
    """Include every implemented non-draft type and reject unrecognized recipes."""
    catalog = load_catalog(root)
    from scp_hsr import crossings, directional_t, directional_diagonal_t
    from scp_hsr import hsr_components, interchange_layouts, rail_features, rail_repairs
    recipes = {"hsr_diagonal_ghsr", "tram_under_hsr"}
    for module in (crossings, directional_t, directional_diagonal_t, hsr_components,
                   interchange_layouts, rail_features, rail_repairs):
        recipes.update(getattr(module, "RECIPES", ()))
        recipes.update(getattr(module, "INFO", {}))
    selected = [piece for piece in catalog["pieces"] if piece["status"] != "draft"]
    unknown = [piece["id"] for piece in selected
               if piece["domain"] != "high-speed-rail" or piece["recipe"] not in recipes]
    if unknown:
        raise ValueError("The installer cannot prove an implementation for these registered pieces: " + ", ".join(unknown))
    ids = [piece["id"] for piece in selected]
    if not ids:
        raise ValueError("This installer contains no implemented pieces.")
    select_pieces(catalog, ids)  # Preserve the ordinary failed-placement guard.
    return ids


def _policy(root):
    policy = jsonc.load(Path(root) / "config/installer.jsonc")
    if (policy.get("schema_version") != 1 or policy.get("selection") != "all-implemented"
            or policy.get("bundles_nam_resources") is not False
            or policy.get("bundles_game_resources") is not False):
        raise ValueError("This installer has an unsupported release policy; download a complete supported installer.")
    menu = policy.get("assembly_menu", {})
    if menu != {"domain": "high-speed-rail", "layout": "trumpet"}:
        raise ValueError("This installer has an unsupported assembly-menu selection.")
    return policy


def installed_selection(root, installation):
    """Protect every previously installed identifier when preparing an update."""
    ids = all_implemented_ids(root)
    previous = _owned(installation.plugins / FOLDER)
    if previous is not None:
        retained = previous.get("piece_ids")
        if not isinstance(retained, list) or any(not isinstance(value, str) for value in retained):
            raise ValueError("The existing installation has no valid piece selection. Keep it unchanged and use its original installer to recover it.")
        # Receipts bind an installed version and retain its original IDs.
        # A declared selection-ID migration does not remove its numeric game
        # resources; compare through the piece-only ledger without rewriting
        # the receipt or treating an unknown/assembly identity as a piece.
        current = set(ids)
        missing = {identifier for identifier in retained
                   if canonical_subject_id(identifier, kind="piece", root=root) not in current}
        if missing:
            raise ValueError("This version would remove installed pieces: " + ", ".join(sorted(missing)) + ". Keep the existing version; remove their placed pieces from cities before deliberately uninstalling it.")
    return ids


def _notify(progress, phase, **values):
    if progress:
        progress({"phase": phase, **values})


def _cancelled(cancel):
    if cancel and cancel():
        raise InstallationCancelled("Installation cancelled before the plugin-folder transaction; installed files are unchanged.")


def prepare_captures(root, installation, work_root, piece_ids, *, progress=None, cancel=None):
    """Create required one-resource inputs from this user's installed originals."""
    from scp.resource_audit import audit_archive, capture_resource
    catalog = load_catalog(root)
    pieces = select_pieces(catalog, piece_ids)
    needed = sorted({label for piece in pieces for label in piece["dependencies"]})
    roots = [installation.plugins, *installation.extra_plugins]
    donors = Path(work_root) / "local/captures" / uuid.uuid4().hex
    prepared = []
    for label in needed:
        record = catalog["_profile"]["files"][label]
        if not record.get("audit"):
            continue
        _cancelled(cancel)
        _notify(progress, "capture", dependency=label)
        evidence = json.loads(safe_relative(root, record["audit"]).read_text())
        key = evidence["tgi"]
        source_name = evidence["scope"]["archive"].replace("\\", "/").rsplit("/", 1)[-1]
        existing = [path for folder in roots for path in folder.rglob("*")
                    if path.is_file() and path.name.casefold() == record["filename"].casefold()
                    and not (installation.plugins / FOLDER) in path.parents]
        if existing:
            if len(existing) != 1 or hashlib.sha256(existing[0].read_bytes()).hexdigest() != record["sha256"]:
                raise ValueError(f"Existing {record['filename']} is duplicated or differs from the supported source. Keep your current Plugins unchanged and resolve that dependency first.")
            if source_name.casefold() != "simcity_3.dat":
                continue
        if source_name.casefold() == "simcity_3.dat":
            source = _child(installation.game_folder, source_name)
            matches = [source] if source is not None and source.is_file() else []
        else:
            matches = [path for folder in roots for path in folder.rglob("*")
                       if path.is_file() and path.name.casefold() == source_name.casefold()
                       and not (installation.plugins / FOLDER) in path.parents]
        if len(matches) != 1:
            raise ValueError(f"Expected one installed {source_name} for {record['filename']}; found {len(matches)}. Install the supported NAM 50 right-hand profile, including its US Road textures, then select this game again.")
        original = matches[0]
        audit = audit_archive(original, key)
        expected = evidence["matches"][0]["stored_resource_sha256"]
        if (audit["status"] != "complete" or audit["matching_index_entries"] != 1
                or audit["matches"][0]["stored_resource_sha256"] != expected):
            raise ValueError(f"{source_name} does not contain the exact supported {label} resource. This game/NAM variant needs a new compatibility audit.")
        if (source_name.casefold() == "simcity_3.dat"
                and audit["matches"][0]["archive_sha256"] != evidence["matches"][0].get("archive_sha256")):
            raise ValueError("SimCity_3.dat differs from the exact supported game archive. This game edition needs a new compatibility audit, even when its pavement resource is identical.")
        if existing:
            continue
        target = donors / label
        report = capture_resource(original, key, target, root=work_root, plugins=installation.plugins)
        captured = target / report["capture"]["file"]
        if hashlib.sha256(captured.read_bytes()).hexdigest() != record["sha256"]:
            raise ValueError(f"The generated {label} fingerprint differs from the supported profile; installation stopped.")
        captured.rename(target / record["filename"])
        report["capture"]["original_capture_filename"] = report["capture"]["file"]
        report["capture"]["file"] = record["filename"]
        (target / "resource-audit.json").write_text(json.dumps(report, indent=2) + "\n")
        prepared.append({"label": label, "filename": record["filename"], "sha256": record["sha256"]})
    return ([donors] if prepared else []), prepared


def _work_root(path, installation):
    path = Path(path).expanduser().absolute()
    if any(parent.is_symlink() for parent in (path, *path.parents)):
        raise ValueError("The installer working folder contains a symbolic link. Choose a regular folder outside Plugins.")
    path = path.resolve()
    for folder in (installation.plugins, *installation.extra_plugins):
        if path == folder or folder in path.parents or path in folder.parents:
            raise ValueError("The installer working folder and backups must stay outside every Plugins folder.")
    path.mkdir(parents=True, exist_ok=True)
    return path


def run_install(root, selected_folder, work_root, progress=None, cancel=None, *,
                platform=None, home=None, documents=None, player_data=None):
    """Build all implemented types locally, prepare the assembly, and install."""
    from scp.build import doctor, build_project
    from scp.menu_experiment import build_assembly_menu
    from scp.install import install_build
    policy = _policy(root)
    _cancelled(cancel)
    _notify(progress, "discover")
    installation = discover_installation(selected_folder, platform=platform, home=home,
                                        documents=documents, player_data=player_data)
    work_root = _work_root(work_root, installation)
    ids = installed_selection(root, installation)
    _notify(progress, "selection", pieces=len(ids), **installation.as_dict())
    capture_roots, captures = prepare_captures(root, installation, work_root, ids, progress=progress, cancel=cancel)
    extras = [*installation.extra_plugins, *capture_roots]
    _cancelled(cancel)
    _notify(progress, "audit", pieces=len(ids))
    doctor(root, installation.plugins, include=ids, extra_roots=extras)
    run = work_root / "runs" / uuid.uuid4().hex
    run.mkdir(parents=True)
    source, output = run / "source", run / "assembly"

    def build_progress(event):
        _cancelled(cancel)
        if progress:
            progress(event)

    _cancelled(cancel)
    build_project(root, installation.plugins, source, include=ids, extra_roots=extras, progress=build_progress)
    _cancelled(cancel)
    _notify(progress, "menu", pieces=len(ids))
    menu = policy["assembly_menu"]
    build_assembly_menu(root, source, output, layout_id=menu["layout"], domain_id=menu["domain"],
                        plugins=installation.plugins, extra_roots=extras)
    _cancelled(cancel)
    # Cancellation ends here: the existing installer owns the complete atomic
    # exchange and recovery transaction; never terminate it halfway through.
    _notify(progress, "install", pieces=len(ids), cancellation_available=False)
    result = install_build(output, installation.plugins, work_root / "backups", extra_roots=extras)
    result.update(pieces=len(ids), piece_ids=ids, installation=installation.as_dict(),
                  build=str(output), backup_root=str(work_root / "backups"),
                  extra_plugins=[str(path) for path in extras], captures=captures,
                  in_game_tested=False, distribution="experimental-local-builder")
    saved = json.dumps(result, indent=2) + "\n"
    try:
        (run / "installation.json").write_text(saved)
        temporary = work_root / f".last-installation-{uuid.uuid4().hex}.json"
        temporary.write_text(saved)
        temporary.replace(work_root / "last-installation.json")
    except OSError as error:
        # The transaction already succeeded. Report a recovery-record warning
        # honestly instead of presenting a successful installation as a failure.
        result["recovery_record_warning"] = str(error)
    _notify(progress, "complete", **result)
    return result


def undo_install(root, selected_folder, work_root, progress=None, *,
                 platform=None, home=None, documents=None, player_data=None):
    """Restore the last transaction only when it still owns this installation."""
    from scp.install import rollback_install
    _policy(root)
    installation = discover_installation(selected_folder, platform=platform, home=home,
                                        documents=documents, player_data=player_data)
    work_root = _work_root(work_root, installation)
    record = work_root / "last-installation.json"
    if record.is_symlink() or not record.is_file():
        raise ValueError("There is no saved installer transaction to undo on this computer.")
    saved = json.loads(record.read_text())
    if saved.get("status") != "installed":
        raise ValueError("The last recorded installation has already been undone.")
    if Path(saved.get("installation", {}).get("plugins", "")).resolve() != installation.plugins:
        raise ValueError("The last installation belongs to another Plugins folder. Select that game's player-data folder to undo it.")
    extras = [Path(path).resolve() for path in saved.get("extra_plugins", [])]
    if not set(installation.extra_plugins) <= set(extras) or any(
            path not in installation.extra_plugins and not path.is_relative_to(work_root / "local/captures")
            for path in extras):
        raise ValueError("The saved recovery input folders do not match this game and installer. Keep the installation unchanged and restore its original recovery record.")
    if Path(saved.get("backup_root", "")).resolve() != work_root / "backups":
        raise ValueError("The saved backup location does not match this installer's recovery folder.")
    _notify(progress, "undo", cancellation_available=False)
    result = rollback_install(installation.plugins, work_root / "backups", saved.get("backup_id"),
                              extra_roots=extras)
    saved["status"] = "rolled_back"
    try:
        record.write_text(json.dumps(saved, indent=2) + "\n")
    except OSError as error:
        result["recovery_record_warning"] = str(error)
    _notify(progress, "complete", **result)
    return result


def self_test(root):
    """Exercise the real receipt/backup transaction with synthetic DBPFs only."""
    from unittest.mock import patch
    from scp.install import RUL0, NETWORK_INI, install_build, rollback_install
    with tempfile.TemporaryDirectory(prefix="scp-installer-self-test-") as temporary:
        base = Path(temporary).resolve()
        plugins = base / "Plugins"
        plugins.mkdir()
        native = pack_dbpf({RUL0: b"synthetic native rules", NETWORK_INI: b"synthetic native ini"})
        (plugins / "NetworkAddonMod_Controller.dat").write_bytes(native)
        unrelated = plugins / "unrelated.txt"
        unrelated.write_text("preserve")
        output = base / "build"
        managed = output / FOLDER
        managed.mkdir(parents=True)
        raw = pack_dbpf({RUL0: b"synthetic custom rules", NETWORK_INI: b"synthetic custom ini"})
        filename = "00_SCP_Controller_NAM50.dat"
        (managed / filename).write_bytes(raw)
        manifest = {"schema_version": 1, "plugin_folder": FOLDER,
                    "pieces": [{"id": "synthetic-self-test"}],
                    "profile": {"donors": [{"filename": "NetworkAddonMod_Controller.dat",
                                               "sha256": hashlib.sha256(native).hexdigest()}]},
                    "files": [{"path": f"{FOLDER}/{filename}", "bytes": len(raw),
                               "sha256": hashlib.sha256(raw).hexdigest()}]}
        (output / "manifest.json").write_text(json.dumps(manifest))
        with patch("scp.build.verify_build", return_value={"status": "synthetic-only"}):
            result = install_build(output, plugins, base / "backups", extra_roots=[])
        if (managed / filename).read_bytes() != (plugins / FOLDER / filename).read_bytes():
            raise ValueError("Synthetic installer self-test did not preserve the payload.")
        rollback_install(plugins, base / "backups", result["backup_id"], extra_roots=[])
        if ((plugins / FOLDER).exists() or unrelated.read_text() != "preserve"
                or (plugins / "NetworkAddonMod_Controller.dat").read_bytes() != native):
            raise ValueError("Synthetic installer rollback did not restore the original state.")
    _policy(root)
    ids = all_implemented_ids(root)
    return {"status": "passed", "implemented_pieces": len(ids),
            "real_receipt_install_and_rollback": True, "synthetic_payload_only": True,
            "geometry_verification_mocked_for_synthetic_fixture": True,
            "live_game_modified": False}
