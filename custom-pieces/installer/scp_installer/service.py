"""Discover a supported installation and install built or prebuilt pieces.

Folder discovery is deliberately bounded to the selected game, its Wine prefix,
and documented player-data locations. Ambiguous locations require another
explicit selection.
"""
from __future__ import annotations

from dataclasses import dataclass
import ctypes
import hashlib
import json
from pathlib import Path
import re
import sys
import tempfile
import uuid

from scp import jsonc
from scp.dbpf import pack_dbpf
from scp.install import FOLDER, _owned


def load_catalog(*args, **kwargs):
    """Load authoring data only when running the separate source-builder mode."""
    from scp.catalog import load_catalog as load
    return load(*args, **kwargs)


def select_pieces(*args, **kwargs):
    from scp.catalog import select_pieces as select
    return select(*args, **kwargs)


def safe_relative(*args, **kwargs):
    from scp.catalog import safe_relative as relative
    return relative(*args, **kwargs)


SOURCE_KIND = "source-local-builder"
PREBUILT_KIND = "verified-prebuilt"
PREBUILT_DIR = "installer/prebuilt"


# A new prefix is not an implementation claim. Keep this reviewed B roster
# finite so another registered or misspelled recipe still stops selection.
PARALLEL_ALIGNMENT_B_RECIPES = frozenset({
    "highway_ddrhw_parallel_b_crossing",
    "highway_ddrhw_parallel_b_northwest_terminal",
    "highway_ddrhw_parallel_b_southeast_terminal",
    "highway_ddrhw_parallel_b_lower_exit_slip",
    "highway_ddrhw_parallel_b_lower_entry_slip",
    "highway_ddrhw_parallel_b_upper_exit_slip",
    "highway_ddrhw_parallel_b_upper_entry_slip",
    "highway_ddrhw_parallel_b_lower_exit_departure",
    "highway_ddrhw_parallel_b_lower_entry_departure",
    "highway_ddrhw_parallel_b_upper_exit_departure",
    "highway_ddrhw_parallel_b_upper_entry_departure",
    "highway_ddrhw_parallel_b_lower_exit_grade",
    "highway_ddrhw_parallel_b_lower_entry_grade",
    "highway_ddrhw_parallel_b_upper_exit_grade",
    "highway_ddrhw_parallel_b_upper_entry_grade",
})


class InstallationCancelled(ValueError):
    """Cancellation before the final owned-folder transaction."""


class GameSelectionRequired(ValueError):
    """Retain the selected Plugins folder and ask for its Windows game folder."""


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


def discover_installation(selected, *, platform=None, home=None, documents=None, player_data=None, game_folder=None):
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
    if game_folder is not None:
        supplied_game = Path(game_folder).expanduser().resolve()
        game = _one_game([supplied_game, supplied_game.parent])
    else:
        try:
            game = _one_game(direct_game or [*_registered_games(), *_prefix_games(prefix)])
        except ValueError as error:
            if _data_plugins(selected) is not None and not direct_game:
                raise GameSelectionRequired(str(error)) from error
            raise
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


def implemented_recipes_by_domain():
    """Report exact provider declarations without accepting recipe prefixes."""
    from scp_hsr import crossings, directional_t, directional_diagonal_t
    from scp_hsr import hsr_components, interchange_layouts, rail_features, rail_repairs
    from scp_highway import native, ramp_paths, modular_ramps, modular_stamp, parallel_layout, ghsr_crossing, y_junction_layout, y_junction_reversed_layout
    hsr_recipes = {"hsr_diagonal_ghsr", "tram_under_hsr"}
    for module in (crossings, directional_t, directional_diagonal_t, hsr_components,
                   interchange_layouts, rail_features, rail_repairs):
        hsr_recipes.update(getattr(module, "RECIPES", ()))
        hsr_recipes.update(getattr(module, "INFO", {}))
    # The module catalogue declares a finite recipe for each MODULES entry;
    # its provider remains responsible for the recipe naming convention.
    highway_recipes = {native.RECIPE, ghsr_crossing.RECIPE, ghsr_crossing.ALIGNMENT_B_RECIPE}
    from scp_highway.orthogonal_transition_variants import SUPPORTED_RECIPES as transition_recipes
    from scp_highway.diagonal_transition_variants import RECIPES as diagonal_transition_recipes
    highway_recipes.update(transition_recipes)
    highway_recipes.update(diagonal_transition_recipes)
    highway_recipes.update(item["recipe"] for item in ramp_paths.module_catalog()["types"])
    highway_recipes.add(modular_stamp.RECIPE)
    highway_recipes.update(item["recipe"] for item in modular_ramps.module_catalog()["types"])
    highway_recipes.update(item["recipe"] for item in parallel_layout.module_catalog()["types"])
    highway_recipes.update(item["recipe"] for item in y_junction_layout.module_catalog()["types"])
    highway_recipes.update(item["recipe"] for item in y_junction_reversed_layout.module_catalog()["types"])
    highway_recipes.update(PARALLEL_ALIGNMENT_B_RECIPES)
    return {"high-speed-rail": frozenset(hsr_recipes),
            "highway": frozenset(highway_recipes)}


def all_implemented_ids(root):
    """Include every implemented non-draft type and reject unrecognized recipes."""
    catalog = load_catalog(root)
    recipes = implemented_recipes_by_domain()
    selected = [piece for piece in catalog["pieces"] if piece["status"] != "draft"]
    unknown = [piece["id"] for piece in selected
               if piece["recipe"] not in recipes.get(piece["domain"], ())]
    if unknown:
        raise ValueError("The installer cannot prove an implementation for these registered pieces: " + ", ".join(unknown))
    ids = [piece["id"] for piece in selected]
    if not ids:
        raise ValueError("This installer contains no implemented pieces.")
    select_pieces(catalog, ids)  # Preserve the ordinary failed-placement guard.
    return ids


def _policy(root):
    player_manifest = Path(root) / "installer/install-manifest.json"
    if player_manifest.is_file():
        if player_manifest.is_symlink():
            raise ValueError("The player installation manifest must be a regular file.")
        data = json.loads(player_manifest.read_text(encoding="utf-8"))
        policy = data.get("policy") if isinstance(data, dict) else None
    else:
        policy = jsonc.load(Path(root) / "config/installer.jsonc")
    if not isinstance(policy, dict):
        raise ValueError("This installer has an invalid distribution policy.")
    if (policy.get("schema_version") != 1 or policy.get("selection") != "all-implemented"
            or policy.get("bundles_nam_resources") is not False
            or policy.get("bundles_game_resources") is not False):
        raise ValueError("This installer has an unsupported release policy; download a complete supported installer.")
    menu = policy.get("assembly_menu", {})
    if menu != {"domain": "high-speed-rail", "layout": "trumpet", "include_all_highway_layouts": True}:
        raise ValueError("This installer has an unsupported assembly-menu selection.")
    return policy


def _prebuilt_bundle(root):
    """Return a revision-bound payload or identify an explicit source build."""
    root = Path(root)
    metadata = root / "installer/build-info.json"
    runtime_manifest = root / "installer/runtime-manifest.json"
    payload = root / PREBUILT_DIR
    runtime_present = runtime_manifest.exists() or runtime_manifest.is_symlink()
    payload_present = payload.exists() or payload.is_symlink()
    if not metadata.exists() and not metadata.is_symlink():
        if getattr(sys, "frozen", False) or runtime_present or payload_present:
            raise ValueError("The installer is missing its package metadata. Extract the complete installer ZIP.")
        return None
    if metadata.is_symlink() or not metadata.is_file():
        raise ValueError("The installer package metadata must be a regular file.")
    data = json.loads(metadata.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        raise ValueError("The installer package metadata is invalid.")
    kind, commit = data.get("kind"), data.get("source_commit")
    if kind not in (SOURCE_KIND, PREBUILT_KIND) or not isinstance(commit, str) or not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise ValueError("The installer package type or source revision is invalid.")
    if runtime_present:
        if runtime_manifest.is_symlink() or not runtime_manifest.is_file():
            raise ValueError("The installer runtime manifest must be a regular file.")
        runtime = json.loads(runtime_manifest.read_text(encoding="utf-8"))
        if (not isinstance(runtime, dict) or runtime.get("kind") != kind + "-runtime"
                or runtime.get("source_commit") != commit):
            raise ValueError("The installer package metadata and runtime manifest disagree.")
    manifest_sha256 = data.get("prebuilt_payload_manifest_sha256")
    if kind == SOURCE_KIND:
        if payload_present or "prebuilt_payload_manifest_sha256" in data:
            raise ValueError("The source-builder package unexpectedly contains prebuilt payload metadata or files.")
        return None
    if not isinstance(manifest_sha256, str) or not re.fullmatch(r"[0-9a-f]{64}", manifest_sha256):
        raise ValueError("The prebuilt installer is missing its payload manifest fingerprint.")
    if payload.is_symlink() or not payload.is_dir() or not (payload / "manifest.json").is_file():
        raise ValueError("The prebuilt piece payload is missing. Extract the complete installer ZIP.")
    return payload, commit, manifest_sha256


def _player_manifest(root, prebuilt):
    from scp.player_manifest import load_install_manifest
    payload, commit, digest = prebuilt
    manifest = load_install_manifest(root, payload, source_commit=commit)
    if manifest["payload_manifest_sha256"] != digest:
        raise ValueError("The installation manifest differs from the installer payload fingerprint.")
    _policy(root)
    return manifest


def available_pieces(root):
    """Read player labels from the compact manifest without loading authoring data."""
    prebuilt = _prebuilt_bundle(root)
    if prebuilt is not None:
        return {row["id"]: row["name"] for row in _player_manifest(root, prebuilt)["pieces"]}
    ids = set(all_implemented_ids(root))
    return {piece["id"]: piece["name"] for piece in load_catalog(root)["pieces"] if piece["id"] in ids}


def _assembly_menu_selections(root, menu):
    """Combine the selected Rail assembly with the registered Highway layouts."""
    registry = jsonc.load(Path(root) / "domains/highway/menu-layout.jsonc")
    layouts = registry.get("layouts")
    if registry.get("schema_version") != 1 or not isinstance(layouts, dict) or not layouts:
        raise ValueError("This installer is missing its Highway assembly-menu layouts.")
    return [
        {"domain_id": menu["domain"], "layout_id": menu["layout"]},
        *({"domain_id": "highway", "layout_id": layout_id} for layout_id in layouts),
    ]


def installed_selection(root, installation, piece_ids=None):
    """Protect every previously installed identifier when preparing an update."""
    ids = all_implemented_ids(root) if piece_ids is None else list(piece_ids)
    previous = _owned(installation.plugins / FOLDER)
    if previous is not None:
        retained = previous.get("piece_ids")
        if not isinstance(retained, list) or any(not isinstance(value, str) for value in retained):
            raise ValueError("The existing installation has no valid piece selection. Keep it unchanged and use its original installer to recover it.")
        missing = set(retained) - set(ids)
        if missing:
            raise ValueError("This version would remove installed pieces: " + ", ".join(sorted(missing)) + ". Keep the existing version; remove their placed pieces from cities before deliberately uninstalling it.")
    return ids


def _notify(progress, phase, **values):
    if progress:
        progress({"phase": phase, **values})


def _cancelled(cancel):
    if cancel and cancel():
        raise InstallationCancelled("Installation cancelled before the plugin-folder transaction; installed files are unchanged.")


def _prepare_bundle_capture(record, evidence, installation, roots, target, work_root):
    """Resolve only declared originals and keep a multi-source capture outside Plugins."""
    from scp.resource_audit import capture_resource_bundle, inspect_resource_bundle
    captured = evidence.get("capture", {})
    if (evidence.get("capture_kind") != "resource-bundle"
            or captured.get("file") != record["filename"] or captured.get("sha256") != record["sha256"]):
        raise ValueError("Resource-bundle evidence differs from the supported capture profile")
    sources = []
    for descriptor in evidence.get("sources", []):
        name = descriptor.get("filename")
        if (not isinstance(name, str) or Path(name).name != name or "\\" in name or ":" in name):
            raise ValueError("Bundle source filename must be one plain filename")
        location = descriptor.get("location")
        if location == "game":
            source = _child(installation.game_folder, name)
            matches = [source] if source is not None and source.is_file() else []
        elif location == "plugins":
            matches = [path for folder in roots for path in folder.rglob("*")
                       if path.is_file() and path.name.casefold() == name.casefold()
                       and not (installation.plugins / FOLDER) in path.parents]
        else:
            raise ValueError("Bundle source location must be game or plugins")
        if len(matches) != 1:
            raise ValueError(f"Expected one original {name} for the resource bundle; found {len(matches)}")
        sources.append({**descriptor, "archive": matches[0]})
    existing = [path for folder in roots for path in folder.rglob("*")
                if path.is_file() and path.name.casefold() == record["filename"].casefold()
                and not (installation.plugins / FOLDER) in path.parents]
    if existing:
        if (len(existing) != 1 or existing[0].is_symlink()
                or hashlib.sha256(existing[0].read_bytes()).hexdigest() != record["sha256"]):
            raise ValueError(f"Existing {record['filename']} is duplicated or differs from the supported source. Keep it unchanged.")
        # An old capture cannot bypass the current original-game/NAM checks.
        resources, _audit = inspect_resource_bundle(sources)
        if hashlib.sha256(pack_dbpf(resources)).hexdigest() != record["sha256"]:
            raise ValueError("Generated bundle capture fingerprint differs from the supported profile")
        return False
    capture_resource_bundle(sources, target, filename=record["filename"],
                            expected_sha256=record["sha256"], root=work_root, plugins=installation.plugins)
    return True


def prepare_captures(root, installation, work_root, piece_ids, *, progress=None, cancel=None,
                     verify_originals=False):
    """Create declared single-resource or bundle inputs from the user's originals."""
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
        evidence = jsonc.load(safe_relative(root, record["audit"]))
        capture_kind = record.get("capture_kind")
        # Native archive audits also describe measurements; only actual
        # single-resource evidence or an explicit bundle declares a capture.
        if capture_kind is None and "tgi" not in evidence:
            continue
        _cancelled(cancel)
        _notify(progress, "capture", dependency=label)
        if capture_kind == "resource-bundle":
            if _prepare_bundle_capture(record, evidence, installation, roots, donors / label, work_root):
                prepared.append({"label": label, "filename": record["filename"], "sha256": record["sha256"]})
            continue
        if capture_kind is not None:
            raise ValueError(f"Unsupported capture kind: {capture_kind}")
        key = evidence["tgi"]
        source_name = evidence["scope"]["archive"].replace("\\", "/").rsplit("/", 1)[-1]
        existing = [path for folder in roots for path in folder.rglob("*")
                    if path.is_file() and path.name.casefold() == record["filename"].casefold()
                    and not (installation.plugins / FOLDER) in path.parents]
        if existing:
            if len(existing) != 1 or hashlib.sha256(existing[0].read_bytes()).hexdigest() != record["sha256"]:
                raise ValueError(f"Existing {record['filename']} is duplicated or differs from the supported source. Keep your current Plugins unchanged and resolve that dependency first.")
            if source_name.casefold() != "simcity_3.dat" and not verify_originals:
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


def _require_submenu_files(installation):
    """Check that the SCP menu dependencies are in the game's loading roots."""
    roots = (installation.plugins, *installation.extra_plugins)
    missing = []
    for name in ("memo.submenus.dll", "SC4ResourceLoadingHooks.dll"):
        if not any(path is not None and path.is_file() for path in (_child(root, name) for root in roots)):
            missing.append(f"{name} directly inside either Plugins folder")
    owned = installation.plugins / FOLDER
    if not any(path.name.casefold() == "submenu-essentials.dat" and owned not in path.parents
               and path.is_file() for root in roots for path in root.rglob("*")):
        missing.append("submenu-essentials.dat anywhere under Plugins outside the SCP installation")
    if missing:
        raise ValueError("Install these missing files to use the SCP menus.\n\n- "
                         + "\n- ".join(missing)
                         + "\n\nUse Resource Loading Hooks 2.0.1 or later, then retry. "
                         + "See https://github.com/memo33/submenus-dll#installation")


def _capture_install_inputs(root, installation, work_root, ids, *, progress=None, cancel=None,
                            verify_originals=False):
    _cancelled(cancel)
    capture_roots, captures = prepare_captures(root, installation, work_root, ids, progress=progress,
                                              cancel=cancel, verify_originals=verify_originals)
    return [*installation.extra_plugins, *capture_roots], captures


def _new_run(work_root):
    run = work_root / "runs" / uuid.uuid4().hex
    run.mkdir(parents=True)
    return run


def prepare_install_build(root, installation, work_root, ids, *, progress=None, cancel=None, jobs=1):
    """Build and verify the selected assembly-menu candidate without installing it."""
    from scp.build import build_project
    from scp.menu_experiment import build_assembly_menus
    from scp.verify import compiled_highway_model_audits

    selections = _assembly_menu_selections(root, _policy(root)["assembly_menu"])
    work_root = _work_root(work_root, installation)
    extras, captures = _capture_install_inputs(root, installation, work_root, ids,
                                              progress=progress, cancel=cancel)
    run = _new_run(work_root)
    source, output = run / "source", run / "assembly"

    def build_progress(event):
        _cancelled(cancel)
        if progress:
            progress(event)

    with compiled_highway_model_audits():
        _cancelled(cancel)
        build_project(root, installation.plugins, source, include=ids, extra_roots=extras, progress=build_progress,
                      jobs=jobs)
        _cancelled(cancel)
        _notify(progress, "menu", pieces=len(ids))
        build_assembly_menus(root, source, output, selections=selections,
                             plugins=installation.plugins, extra_roots=extras)
    _cancelled(cancel)
    return run, output, extras, captures


def run_install(root, selected_folder, work_root, progress=None, cancel=None, *,
                platform=None, home=None, documents=None, player_data=None, game_folder=None):
    """Install the explicit package payload or build a source-mode installation."""
    _policy(root)
    prebuilt = _prebuilt_bundle(root)
    player = _player_manifest(root, prebuilt) if prebuilt is not None else None
    _cancelled(cancel)
    _notify(progress, "discover")
    discovery = {"platform": platform, "home": home, "documents": documents, "player_data": player_data}
    if game_folder is not None:
        discovery["game_folder"] = game_folder
    installation = discover_installation(selected_folder, **discovery)
    _require_submenu_files(installation)
    work_root = _work_root(work_root, installation)
    ids = (installed_selection(root, installation) if player is None else
           installed_selection(root, installation, piece_ids=[row["id"] for row in player["pieces"]]))
    _notify(progress, "selection", pieces=len(ids), **installation.as_dict())
    if prebuilt is None:
        from scp.install import install_build
        run, output, extras, captures = prepare_install_build(
            root, installation, work_root, ids, progress=progress, cancel=cancel)
        install = install_build
        install_options = {}
        distribution = "experimental-local-builder"
    else:
        from scp.install import install_prebuilt
        from scp.player_manifest import prepare_dependencies
        from scp.prebuilt import load_payload
        output, commit, manifest_sha256 = prebuilt
        payload_manifest, digest = load_payload(output, commit)
        if digest != manifest_sha256:
            raise ValueError("Prebuilt payload manifest differs from the installer build record")
        _notify(progress, "audit", pieces=len(ids))

        def check_cancelled():
            _cancelled(cancel)
            return False

        capture_roots, captures = prepare_dependencies(player, installation, work_root,
                                                       progress=progress, cancel=check_cancelled)
        extras = [*installation.extra_plugins, *capture_roots]
        _cancelled(cancel)
        expected_profile = payload_manifest["profile"]
        run = _new_run(work_root)
        install = install_prebuilt
        install_options = {"source_commit": commit, "expected_piece_ids": ids,
                           "expected_manifest_sha256": manifest_sha256, "expected_profile": expected_profile}
        distribution = PREBUILT_KIND
    _cancelled(cancel)
    # Cancellation ends here: the existing installer owns the complete atomic
    # exchange and recovery transaction; never terminate it halfway through.
    _notify(progress, "install", pieces=len(ids), cancellation_available=False, distribution=distribution)
    result = install(output, installation.plugins, work_root / "backups", extra_roots=extras, **install_options)
    result.update(pieces=len(ids), piece_ids=ids, installation=installation.as_dict(),
                  build=str(output), backup_root=str(work_root / "backups"),
                  extra_plugins=[str(path) for path in extras], captures=captures,
                  in_game_tested=False, distribution=distribution)
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
                 platform=None, home=None, documents=None, player_data=None, game_folder=None):
    """Restore the last transaction only when it still owns this installation."""
    from scp.install import rollback_install
    _policy(root)
    discovery = {"platform": platform, "home": home, "documents": documents, "player_data": player_data}
    if game_folder is not None:
        discovery["game_folder"] = game_folder
    installation = discover_installation(selected_folder, **discovery)
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


def _prebuilt_self_test(root, prebuilt, player):
    """Check finished archives and real repeat-install/Undo transactions offline."""
    import scp.install as transactions
    from scp.prebuilt import load_payload
    output, commit, digest = prebuilt
    manifest, actual_digest = load_payload(output, commit)
    if actual_digest != digest:
        raise ValueError("Prebuilt self-test payload fingerprint differs from its build record.")
    ids = [row["id"] for row in player["pieces"]]
    with tempfile.TemporaryDirectory(prefix="scp-installer-self-test-") as temporary:
        base = Path(temporary).resolve()
        plugins = base / "Plugins"
        plugins.mkdir()
        resources = {transactions.RUL0: b"synthetic native rules",
                     transactions.NETWORK_INI: b"synthetic native ini"}
        for dependencies in manifest["dependency_audit"].values():
            for key in dependencies:
                resources.setdefault(tuple(int(part, 16) for part in key.split("-")), b"synthetic dependency")
        native = pack_dbpf(resources)
        controller = plugins / "NetworkAddonMod_Controller.dat"
        controller.write_bytes(native)
        unrelated = plugins / "unrelated.txt"
        unrelated.write_text("preserve", encoding="utf-8")
        # Hosted checks have no proprietary NAM files. Bypass only exact donor
        # fingerprints; keep payload hashes, resource scans, receipts, and Undo.
        original_profile = transactions._profile
        transactions._profile = lambda *args, **kwargs: controller
        try:
            options = {"source_commit": commit, "expected_manifest_sha256": digest,
                       "expected_piece_ids": ids, "expected_profile": manifest["profile"]}
            first = transactions.install_prebuilt(output, plugins, base / "backups", **options)
            second = transactions.install_prebuilt(output, plugins, base / "backups", **options)
            for record in manifest["files"]:
                with (plugins / record["path"]).open("rb") as stream:
                    if hashlib.file_digest(stream, "sha256").hexdigest() != record["sha256"]:
                        raise ValueError("Installer self-test changed a finished archive.")
            transactions.rollback_install(plugins, base / "backups", second["backup_id"])
            transactions.rollback_install(plugins, base / "backups", first["backup_id"])
        finally:
            transactions._profile = original_profile
        if ((plugins / FOLDER).exists() or unrelated.read_text(encoding="utf-8") != "preserve"
                or controller.read_bytes() != native):
            raise ValueError("Installer self-test Undo did not restore the original state.")
    return {"status": "passed", "implemented_pieces": len(ids),
            "assembly_menu_layouts": player["assembly_menu_layouts"],
            "real_receipt_install_and_rollback": True, "repeat_install_and_rollback": True,
            "synthetic_payload_only": False, "planar_geometry_runtime_checked": False,
            "prebuilt_transaction_verified": True, "prebuilt_files_verified": len(manifest["files"]),
            "native_profile_mocked_for_prebuilt_fixture": True,
            "geometry_verification_mocked_for_synthetic_fixture": False, "live_game_modified": False}


def self_test(root):
    """Exercise the chosen runtime with disposable synthetic NAM inputs."""
    prebuilt = _prebuilt_bundle(root)
    if prebuilt is not None:
        return _prebuilt_self_test(root, prebuilt, _player_manifest(root, prebuilt))

    # The separate source-builder distribution still needs its geometry runtime.
    import shapely
    from shapely import Polygon, constrained_delaunay_triangles, union_all
    polygon = Polygon([(0., 0.), (4., 0.), (4., 4.), (0., 4.)],
                      holes=[[(1., 1.), (2., 1.), (2., 2.), (1., 2.)]])
    triangles = constrained_delaunay_triangles(polygon)
    if (not triangles.geoms or abs(sum(face.area for face in triangles.geoms)-15.) > 1e-12
            or union_all(triangles.geoms).symmetric_difference(polygon).area > 1e-12):
        raise ValueError("Bundled planar geometry runtime failed its boundary-and-hole triangulation check.")
    from unittest.mock import patch
    from scp.install import RUL0, NETWORK_INI, install_build, rollback_install
    policy = _policy(root)
    selections = _assembly_menu_selections(root, policy["assembly_menu"])
    ids = all_implemented_ids(root)
    with tempfile.TemporaryDirectory(prefix="scp-installer-self-test-") as temporary:
        base = Path(temporary).resolve()
        plugins = base / "Plugins"
        plugins.mkdir()
        native = pack_dbpf({RUL0: b"synthetic native rules", NETWORK_INI: b"synthetic native ini"})
        controller = plugins / "NetworkAddonMod_Controller.dat"
        controller.write_bytes(native)
        unrelated = plugins / "unrelated.txt"
        unrelated.write_text("preserve", encoding="utf-8")
        output = base / "build"
        path = f"{FOLDER}/00_SCP_Controller_NAM50.dat"
        asset = output / path
        asset.parent.mkdir(parents=True)
        raw = pack_dbpf({RUL0: b"synthetic custom rules", NETWORK_INI: b"synthetic custom ini"})
        asset.write_bytes(raw)
        manifest = {"schema_version": 1, "plugin_folder": FOLDER,
                    "pieces": [{"id": "synthetic-self-test"}],
                    "profile": {"id": "synthetic-nam50-rhd",
                                "donors": [{"filename": controller.name,
                                            "sha256": hashlib.sha256(native).hexdigest()}]},
                    "files": [{"path": path, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}]}
        (output / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        with patch("scp.build.verify_build", return_value={"status": "synthetic-only"}):
            result = install_build(output, plugins, base / "backups", extra_roots=[])
        for record in manifest["files"]:
            with (plugins / record["path"]).open("rb") as stream:
                if hashlib.file_digest(stream, "sha256").hexdigest() != record["sha256"]:
                    raise ValueError("Installer self-test changed a finished archive.")
        rollback_install(plugins, base / "backups", result["backup_id"], extra_roots=[])
        if ((plugins / FOLDER).exists() or unrelated.read_text(encoding="utf-8") != "preserve"
                or controller.read_bytes() != native):
            raise ValueError("Installer self-test rollback did not restore the original state.")
    return {"status": "passed", "implemented_pieces": len(ids),
            "assembly_menu_layouts": len(selections),
            "real_receipt_install_and_rollback": True, "synthetic_payload_only": True,
            "planar_geometry_runtime_checked": True,
            "shapely_version": shapely.__version__, "geos_version": shapely.geos_version_string,
            "prebuilt_transaction_verified": False, "prebuilt_files_verified": 0,
            "native_profile_mocked_for_prebuilt_fixture": False,
            "geometry_verification_mocked_for_synthetic_fixture": True,
            "live_game_modified": False}
