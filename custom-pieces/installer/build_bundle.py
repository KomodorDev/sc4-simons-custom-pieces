"""Build and inspect a self-contained source/local-builder installer.

No game inputs or generated DAT archives enter this distribution. The runtime
retains the library's source hierarchy because its independent checks read the
authoritative source, geometry, and frozen audit files directly.
"""
from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.metadata
import json
import os
from pathlib import Path, PurePosixPath
import platform
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import zipfile


PLATFORMS = ("windows-x64",)
APP_NAME = "SCP Installer"
RUNTIME_MANIFEST = "installer/runtime-manifest.json"
BUILD_INFO = "installer/build-info.json"
SOURCE_EXTENSIONS = {".py", ".json", ".jsonc", ".md", ".png", ".svg", ".txt", ".toml"}
FORBIDDEN_PARTS = {"local", "dist", "__pycache__", ".git", ".venv", "node_modules"}
GAME_EXTENSIONS = {".dat", ".sc4model", ".sc4lot", ".sc4desc", ".dll", ".exe"}


def _json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _hash(path: Path) -> str:
    with path.open("rb") as stream:
        digest = sha256()
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _relative(value: str) -> PurePosixPath:
    path = PurePosixPath(value)
    if (not value or "\\" in value or path.is_absolute() or path.as_posix() != value
            or any(part in {"", ".", ".."} for part in path.parts)
            or ":" in value or "\x00" in value):
        raise ValueError(f"Unsafe distribution path: {value!r}")
    return path


def _commit(value: str) -> str:
    if re.fullmatch(r"[0-9a-f]{40}", value) is None:
        raise ValueError("The source commit must be a complete, lowercase, 40-character Git SHA.")
    return value


def host_platform() -> str:
    system, machine = platform.system(), platform.machine().lower()
    if system == "Windows" and machine in {"amd64", "x86_64"}:
        return "windows-x64"
    raise ValueError(f"No installer build is defined for {system}/{machine}.")


def _source_paths(root: Path) -> list[Path]:
    """Take only public source candidates, including this PR's new files."""
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z", "--", "."],
        cwd=root, check=True, capture_output=True,
    )
    paths = []
    for raw in sorted(set(result.stdout.decode("utf-8").split("\0")) - {""}):
        relative = _relative(raw)
        path = root.joinpath(*relative.parts)
        if path.is_symlink() or any(parent.is_symlink() for parent in path.parents if parent != root.parent):
            raise ValueError(f"Source distribution refuses a symbolic link: {raw}")
        if path.is_file():
            paths.append(path)
    return paths


def runtime_allowed(relative: str, domain_names: set[str], subjects: set[str]) -> bool:
    """The runtime is an allowlist, not a copy of a developer's checkout."""
    path = _relative(relative)
    parts = path.parts
    if any(part.casefold() in FORBIDDEN_PARTS for part in parts):
        return False
    if path.suffix.lower() not in SOURCE_EXTENSIONS:
        return False
    if len(parts) == 1:
        return path.name in {"project.json", "pyproject.toml", "README.md", "AGENTS.md", "scp.py"}
    if parts[0] in {"framework", "schemas"}:
        return path.suffix in {".py", ".json"}
    if parts[0] == "installer":
        return path.suffix == ".py" and (len(parts) == 2 or len(parts) == 3 and parts[1] == "scp_installer")
    if parts[0] == "docs":
        return path.suffix in {".md", ".png", ".svg", ".json", ".txt"}
    if parts[0] == "config":
        return relative in {"config/allocations.json", "config/release.json", "config/installer.json"} or (
            len(parts) == 3 and parts[1] == "profiles" and path.suffix == ".json")
    if parts[0] != "domains" or len(parts) < 3 or parts[1] not in domain_names:
        return False
    if len(parts) == 3:
        return path.suffix in {".json", ".md"}
    if parts[2] in {"implementation", "tools"}:
        return path.suffix == ".py"
    if parts[2] == "assets":
        return path.suffix in {".png", ".svg"}
    if parts[2] in {"00_pieces", "01_assemblies"}:
        if len(parts) == 4:
            return path.name in {"inventory.json", "INVENTORY.md"}
        return "/".join(parts[:4]) in subjects and path.suffix in {
            ".json", ".jsonc", ".md", ".png", ".svg", ".txt"}
    return False


def _runtime_paths(root: Path) -> list[Path]:
    project = json.loads((root / "project.json").read_text(encoding="utf-8"))
    domains = set(project["domains"])
    subjects = set()
    for record in project["domains"].values():
        registry_path = _relative(record["registry"])
        registry = json.loads(root.joinpath(*registry_path.parts).read_text(encoding="utf-8"))
        directory = _relative(record["path"])
        for name in (*registry.get("pieces", []), *registry.get("assemblies", [])):
            subjects.add((directory / _relative(name)).parent.as_posix())
    return [path for path in _source_paths(root)
            if runtime_allowed(path.relative_to(root).as_posix(), domains, subjects)]


def _record(path: Path, root: Path) -> dict:
    return {"path": path.relative_to(root).as_posix(), "bytes": path.stat().st_size, "sha256": _hash(path)}


def _files(root: Path) -> list[Path]:
    found = []
    for path in root.rglob("*"):
        if path.is_symlink():
            raise ValueError(f"Unexpected symbolic link: {path.relative_to(root)}")
        elif path.is_file():
            found.append(path)
    return sorted(found, key=lambda path: path.relative_to(root).as_posix())


def prepare_runtime(source: Path, destination: Path, source_commit: str, target: str) -> dict:
    source, destination = source.resolve(), destination.absolute()
    _commit(source_commit)
    if target not in PLATFORMS:
        raise ValueError("Unknown installer platform.")
    if destination.exists() and any(destination.iterdir()):
        raise ValueError("Runtime destination must be new or empty.")
    if source == destination or source.is_relative_to(destination):
        raise ValueError("Runtime output cannot contain or replace the source checkout.")
    destination.mkdir(parents=True, exist_ok=True)
    sources = _runtime_paths(source)
    for path in sources:
        relative = path.relative_to(source)
        raw = path.read_bytes()
        if raw.startswith(b"DBPF") or path.suffix.lower() in GAME_EXTENSIONS:
            raise ValueError(f"Native game resource is forbidden in installer sources: {relative}")
        output = destination / relative
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(raw)
    required = {"project.json", "pyproject.toml", "installer/main.py", "installer/build_bundle.py",
                "installer/scp_installer/service.py", "config/installer.json", "framework/scp/check_bootstrap.py"}
    missing = required - {path.relative_to(source).as_posix() for path in sources}
    if missing:
        raise ValueError("Installer runtime is missing required source files: " + ", ".join(sorted(missing)))
    metadata = {"schema_version": 1, "kind": "source-local-builder", "source_commit": source_commit,
                "release_tag": "installer-" + source_commit[:12], "platform": target,
                "experimental": True, "bundled_native_game_resources": False,
                "runtime_manifest": RUNTIME_MANIFEST}
    _json(destination / BUILD_INFO, metadata)
    records = [_record(path, destination) for path in _files(destination)]
    manifest = {"schema_version": 1, "kind": "source-local-builder-runtime", "source_commit": source_commit,
                "files": records}
    _json(destination / RUNTIME_MANIFEST, manifest)
    verify_runtime(destination)
    return manifest


def verify_runtime(root: Path) -> dict:
    """Verify the exact source tree before the GUI can read native inputs."""
    root = Path(root).resolve()
    manifest = json.loads((root / RUNTIME_MANIFEST).read_text(encoding="utf-8"))
    metadata = json.loads((root / BUILD_INFO).read_text(encoding="utf-8"))
    commit = _commit(manifest["source_commit"])
    if (manifest.get("schema_version") != 1 or manifest.get("kind") != "source-local-builder-runtime"
            or metadata.get("source_commit") != commit or metadata.get("platform") not in PLATFORMS
            or metadata.get("release_tag") != "installer-" + commit[:12]
            or metadata.get("kind") != "source-local-builder" or metadata.get("experimental") is not True
            or metadata.get("bundled_native_game_resources") is not False):
        raise ValueError("Installer source manifest or build metadata is inconsistent.")
    records = manifest["files"]
    names = [_relative(record["path"]).as_posix() for record in records]
    if len(names) != len({name.casefold() for name in names}) or RUNTIME_MANIFEST in names:
        raise ValueError("Installer runtime manifest has duplicate or self-referential files.")
    actual = {path.relative_to(root).as_posix(): path for path in _files(root)}
    if set(actual) != set(names) | {RUNTIME_MANIFEST}:
        raise ValueError("Installer runtime file set differs from its source manifest.")
    for record in records:
        path = actual[record["path"]]
        if _record(path, root) != record:
            raise ValueError("Installer source changed: " + record["path"])
        if path.read_bytes()[:4] == b"DBPF" or path.suffix.lower() in GAME_EXTENSIONS:
            raise ValueError("Installer runtime unexpectedly contains a native game resource.")
    return {"status": "passed", "source_commit": commit, "files_verified": len(records),
            "bundled_native_game_resources": False}


def _bundle_record(path: Path, root: Path) -> dict:
    return {**_record(path, root), "kind": "file", "mode": 0o100755 if path.stat().st_mode & 0o111 else 0o100644}


def create_archive(folder: Path, destination: Path, source_commit: str, target: str) -> dict:
    """Write the Windows app and its exact file manifest into one ZIP."""
    _commit(source_commit)
    folder, destination = Path(folder).resolve(), Path(destination).absolute()
    records = [_bundle_record(path, folder) for path in _files(folder)
               if path.relative_to(folder).as_posix() not in {"bundle-index.json", "SHA256SUMS"}]
    index = {"schema_version": 1, "kind": "source-local-builder-installer", "source_commit": source_commit,
             "platform": target, "release_tag": "installer-" + source_commit[:12], "experimental": True,
             "bundled_native_game_resources": False, "files": records}
    _json(folder / "bundle-index.json", index)
    hash_paths = [path for path in _files(folder) if path.relative_to(folder).as_posix() != "SHA256SUMS"]
    sums = []
    for path in hash_paths:
        digest = _hash(path)
        sums.append(f"{digest}  {path.relative_to(folder).as_posix()}")
    (folder / "SHA256SUMS").write_text("\n".join(sums) + "\n", encoding="utf-8")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destination, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for path in _files(folder):
            record = _bundle_record(path, folder)
            name = folder.name + "/" + record["path"]
            info = zipfile.ZipInfo(name, date_time=(2020, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = record["mode"] << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, path.read_bytes())
    report = verify_archive(destination)
    (destination.parent / (destination.name + ".sha256")).write_text(
        _hash(destination) + "  " + destination.name + "\n", encoding="utf-8")
    return report


def verify_archive(path: Path) -> dict:
    """Prove ZIP closure, hashes, regular files, and absence of game DATs."""
    with zipfile.ZipFile(path) as archive:
        infos = archive.infolist()
        names = [info.filename for info in infos]
        if len(names) != len({name.casefold() for name in names}):
            raise ValueError("Installer ZIP has duplicate members.")
        paths = [_relative(name) for name in names]
        roots = {name.parts[0] for name in paths}
        if len(roots) != 1 or any(len(name.parts) < 2 for name in paths):
            raise ValueError("Installer ZIP must have one enclosing folder.")
        prefix = next(iter(roots)) + "/"
        contents = {name[len(prefix):]: archive.read(name) for name in names}
        index = json.loads(contents["bundle-index.json"])
        commit = _commit(index["source_commit"])
        if (index.get("kind") != "source-local-builder-installer" or index.get("schema_version") != 1
                or index.get("platform") not in PLATFORMS or index.get("experimental") is not True
                or index.get("bundled_native_game_resources") is not False
                or index.get("release_tag") != "installer-" + commit[:12]):
            raise ValueError("Installer ZIP metadata is inconsistent.")
        records = index["files"]
        selected = [_relative(record["path"]).as_posix() for record in records]
        if len(selected) != len(set(selected)) or set(contents) != set(selected) | {"bundle-index.json", "SHA256SUMS"}:
            raise ValueError("Installer ZIP has undeclared or missing members.")
        by_name = {info.filename[len(prefix):]: info for info in infos}
        for record in records:
            name, raw = record["path"], contents[record["path"]]
            mode = by_name[name].external_attr >> 16
            if len(raw) != record["bytes"] or sha256(raw).hexdigest() != record["sha256"] or mode != record["mode"]:
                raise ValueError("Installer ZIP member changed: " + name)
            if record["kind"] != "file" or stat.S_IFMT(mode) != stat.S_IFREG:
                raise ValueError("Unsupported installer ZIP member kind.")
            # Frozen Python and its native libraries are expected; SimCity resources are not.
            if PurePosixPath(name).suffix.lower() in GAME_EXTENSIONS - {".exe", ".dll"} or raw.startswith(b"DBPF"):
                raise ValueError("Installer ZIP contains a native game resource: " + name)
        expected_sums = {}
        for line in contents["SHA256SUMS"].decode("utf-8").splitlines():
            digest, name = line.split("  ", 1)
            _relative(name)
            if name in expected_sums or re.fullmatch("[0-9a-f]{64}", digest) is None:
                raise ValueError("Installer checksums contain an invalid or duplicate entry.")
            expected_sums[name] = digest
        if set(expected_sums) != set(contents) - {"SHA256SUMS"} or any(
                sha256(contents[name]).hexdigest() != digest for name, digest in expected_sums.items()):
            raise ValueError("Installer checksum closure does not match the archive.")
    return {"status": "passed", "source_commit": commit, "platform": index["platform"],
            "members_verified": len(names), "bundled_native_game_resources": False, "zip_sha256": _hash(Path(path))}


def _notices(destination: Path) -> None:
    text = ["SCP Installer: bundled third-party software", "", "Python: https://docs.python.org/3/license.html",
            "Pillow: https://github.com/python-pillow/Pillow", "NumPy: https://numpy.org/doc/stable/license.html",
            "PyInstaller bootloader: https://pyinstaller.org/en/stable/license.html",
            "Tcl/Tk: https://www.tcl-lang.org/software/tcltk/license.html", "",
            "PyInstaller's licensing exception covers generated bundles; the bundled components retain their own licenses.",
            "NAM and SimCity game resources are not included. The installer reads the user's installed dependencies locally.", ""]
    licenses = destination / "licenses"
    licenses.mkdir()
    for name in ("Pillow", "numpy", "pyinstaller", "pyinstaller-hooks-contrib", "altgraph", "packaging"):
        package = importlib.metadata.distribution(name)
        text.append(f"{package.metadata['Name']} {package.version}")
        for file in package.files or ():
            if any(part.casefold().startswith(("license", "copying", "notice")) for part in file.parts):
                source = Path(package.locate_file(file))
                if source.is_file():
                    target = licenses / name / str(file).replace("/", "_").replace("\\", "_")
                    target.parent.mkdir(exist_ok=True)
                    shutil.copyfile(source, target)
    import builtins
    builtins.license._Printer__setup()
    (licenses / "Python.txt").write_text("\n".join(builtins.license._Printer__lines) + "\n", encoding="utf-8")
    (destination / "THIRD-PARTY-NOTICES.txt").write_text("\n".join(text) + "\n", encoding="utf-8")


def build_bundle(source: Path, output: Path, source_commit: str, target: str) -> dict:
    if target != host_platform():
        raise ValueError("PyInstaller must run natively on the selected operating system and architecture.")
    revision = subprocess.run(["git", "rev-parse", "HEAD"], cwd=source, text=True, capture_output=True, check=True)
    if revision.stdout.strip() != _commit(source_commit):
        raise ValueError("Installer source commit differs from the checked-out revision.")
    tracked = subprocess.run(["git", "diff", "--quiet", "HEAD", "--", "."], cwd=source, check=False)
    untracked = subprocess.run(["git", "ls-files", "--others", "--exclude-standard", "-z", "--", "."],
                               cwd=source, capture_output=True, check=True)
    if tracked.returncode != 0 or untracked.stdout:
        raise ValueError("A native release build requires committed source files; use prepare to inspect unfinished work.")
    output = output.absolute()
    if output.exists() and any(output.iterdir()):
        raise ValueError("Bundle output directory must be new or empty.")
    output.mkdir(parents=True, exist_ok=True)
    runtime = output / "work/runtime/custom-pieces"
    prepare_runtime(source, runtime, source_commit, target)
    # Check Tcl/Tk before freezing; importing it does not open a window.
    import tkinter
    tkinter.Tcl().eval("info patchlevel")
    command = [sys.executable, "-B", "-m", "PyInstaller", "--noconfirm", "--clean", "--windowed", "--onedir",
               # PyInstaller's isolated interpreter ignores PYTHONUTF8. This
               # bootloader option applies before Python initializes, so the
               # existing library's implicit text reads are UTF-8 on Windows.
               "--python-option", "X utf8",
               "--name", APP_NAME, "--distpath", str(output / "work/frozen"), "--workpath", str(output / "work/pyinstaller"),
               "--specpath", str(output / "work"), "--add-data", str(runtime) + ":custom-pieces",
               "--paths", str(runtime / "framework"),
               "--paths", str(runtime / "installer"),
               "--paths", str(runtime / "domains/high-speed-rail/implementation"),
               "--collect-submodules", "scp", "--collect-submodules", "scp_hsr",
               "--collect-submodules", "scp_installer", "--collect-all", "PIL",
               "--collect-all", "numpy", "--hidden-import", "tkinter", "--hidden-import", "tkinter.ttk",
               "--hidden-import", "tkinter.filedialog", "--hidden-import", "tkinter.messagebox"]
    command.append(str(runtime / "installer/main.py"))
    timestamp = subprocess.run(["git", "show", "--no-patch", "--format=%ct", source_commit],
                               cwd=source, text=True, capture_output=True, check=True).stdout.strip()
    if re.fullmatch(r"[0-9]+", timestamp) is None:
        raise ValueError("Cannot determine the source commit's build timestamp.")
    build_environment = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "PYTHONUTF8": "1",
                         "PYTHONHASHSEED": "0", "SOURCE_DATE_EPOCH": timestamp}
    subprocess.run(command, check=True, cwd=runtime, env=build_environment)
    # Neither discovery nor freezing may modify the exact source payload.
    verify_runtime(runtime)
    name = "SCP-Installer-" + target + "-" + source_commit[:12]
    folder = output / name
    folder.mkdir()
    frozen = output / "work/frozen"
    shutil.copytree(frozen / APP_NAME, folder, dirs_exist_ok=True)
    executable = folder / (APP_NAME + ".exe")
    report_path = output / ("self-test-" + target + ".json")
    subprocess.run([str(executable), "--self-test", "--report", str(report_path)], check=True,
                   timeout=180, cwd=output, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    report = json.loads(report_path.read_text(encoding="utf-8"))
    if (report.get("status") != "passed" or report.get("source_commit") != source_commit
            or report.get("utf8_mode") != 1):
        raise ValueError("Frozen installer self-test did not report a pass with UTF-8 mode enabled.")
    report["platform"] = target
    _json(report_path, report)
    gui_report_path = output / ("gui-smoke-test-" + target + ".json")
    subprocess.run([str(executable), "--gui-smoke-test", "--report", str(gui_report_path)], check=True,
                   timeout=30, cwd=output, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    gui_report = json.loads(gui_report_path.read_text(encoding="utf-8"))
    if (gui_report.get("status") != "passed" or gui_report.get("source_commit") != source_commit
            or gui_report.get("utf8_mode") != 1):
        raise ValueError("Frozen installer GUI smoke test did not report a pass with UTF-8 mode enabled.")
    gui_report["platform"] = target
    _json(gui_report_path, gui_report)
    (folder / "README.txt").write_text(
        "SCP Installer — experimental source/local-builder release\n\n"
        "Open SCP Installer.exe. Keep its _internal folder beside it.\n"
        + "Choose your SimCity 4 game or user-data folder, then select Install.\n"
        "The supported NAM installation must already be present; the installer checks it before changing Plugins.\n"
        "Python is bundled. No separate Python installation, terminal command, or source checkout is required.\n"
        "Windows may show an unsigned-app warning.\n"
        "No SimCity or NAM binary resources are included or downloaded by this release.\n"
        "Generated pieces remain experimental; software verification does not establish in-game testing.\n"
        "Instructions and limitations: https://github.com/KomodorDev/sc4-simons-custom-pieces/blob/"
        + source_commit + "/custom-pieces/docs/INSTALLER.md\n", encoding="utf-8")
    _notices(folder)
    archive = output / (name + ".zip")
    verification = create_archive(folder, archive, source_commit, target)
    _json(output / ("bundle-index-" + target + ".json"), json.loads((folder / "bundle-index.json").read_text()))
    _json(output / ("archive-check-" + target + ".json"), verification)
    return verification


def _gh(*arguments: str, input_json: dict | None = None) -> dict:
    result = subprocess.run(["gh", "api", *arguments], input=None if input_json is None else json.dumps(input_json),
                            text=True, capture_output=True, check=True)
    return json.loads(result.stdout) if result.stdout.strip() else {}


def publish(artifacts: Path, source_commit: str, repository: str) -> dict:
    """Publish only the verified native outputs of this exact main push."""
    _commit(source_commit)
    if (os.environ.get("GITHUB_EVENT_NAME") != "push" or os.environ.get("GITHUB_REF") != "refs/heads/main"
            or os.environ.get("GITHUB_SHA") != source_commit or os.environ.get("GITHUB_REPOSITORY") != repository):
        raise ValueError("Publishing requires the exact main push in this repository's GitHub Actions workflow.")
    if re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository) is None:
        raise ValueError("Invalid GitHub repository name.")
    assets = []
    for target in PLATFORMS:
        name = "SCP-Installer-" + target + "-" + source_commit[:12] + ".zip"
        matches = list(Path(artifacts).rglob(name))
        if len(matches) != 1:
            raise ValueError("Expected exactly one platform archive: " + name)
        archive = matches[0]
        verification = verify_archive(archive)
        if verification["source_commit"] != source_commit or verification["platform"] != target:
            raise ValueError("Release archive is bound to a different commit or platform.")
        sidecar = archive.with_name(name + ".sha256")
        if sidecar.read_text(encoding="utf-8") != _hash(archive) + "  " + name + "\n":
            raise ValueError("Release archive checksum does not match its sidecar.")
        report_path = archive.parent / ("self-test-" + target + ".json")
        report = json.loads(report_path.read_text(encoding="utf-8"))
        if (report.get("status") != "passed" or report.get("source_commit") != source_commit
                or report.get("platform") != target or report.get("utf8_mode") != 1):
            raise ValueError("Release requires the frozen executable self-test result.")
        gui_path = archive.parent / ("gui-smoke-test-" + target + ".json")
        gui_report = json.loads(gui_path.read_text(encoding="utf-8"))
        if (gui_report.get("status") != "passed" or gui_report.get("source_commit") != source_commit
                or gui_report.get("platform") != target or gui_report.get("utf8_mode") != 1):
            raise ValueError("Release requires the frozen Windows GUI smoke-test result.")
        index_path = archive.parent / ("bundle-index-" + target + ".json")
        verification_path = archive.parent / ("archive-check-" + target + ".json")
        with zipfile.ZipFile(archive) as saved:
            embedded = json.loads(saved.read(next(name for name in saved.namelist() if name.endswith("/bundle-index.json"))))
        if json.loads(index_path.read_text(encoding="utf-8")) != embedded:
            raise ValueError("Release's external member manifest differs from the verified ZIP.")
        if json.loads(verification_path.read_text(encoding="utf-8")) != verification:
            raise ValueError("Release's external archive-check report differs from the verified ZIP.")
        assets += [archive, sidecar, report_path, gui_path, index_path, verification_path]
    tag = "installer-" + source_commit[:12]
    endpoint = "repos/" + repository
    # Create the exact ref explicitly; a rerun may reuse it but must never move it.
    refs = _gh(endpoint + "/git/matching-refs/tags/" + tag)
    exact = [record for record in refs if record["ref"] == "refs/tags/" + tag]
    if exact:
        if len(exact) != 1 or exact[0]["object"]["type"] != "commit" or exact[0]["object"]["sha"] != source_commit:
            raise ValueError("Existing installer tag points at a different source commit.")
    else:
        _gh("--method", "POST", endpoint + "/git/refs", "--input", "-",
            input_json={"ref": "refs/tags/" + tag, "sha": source_commit})
    releases = _gh("--paginate", "--slurp", endpoint + "/releases")
    existing = [release for page in releases for release in page if release["tag_name"] == tag]
    if len(existing) > 1:
        raise ValueError("Multiple releases unexpectedly share this installer tag.")
    if existing and not existing[0]["draft"]:
        if existing[0].get("prerelease") is not True:
            raise ValueError("Existing installer release is not the expected experimental prerelease.")
        by_name = {asset["name"]: asset for asset in existing[0]["assets"]}
        if set(by_name) != {path.name for path in assets}:
            raise ValueError("Published installer release has a different asset set; assets will not be overwritten.")
        for path in assets:
            remote = by_name[path.name]
            if remote.get("digest") != "sha256:" + _hash(path):
                raise ValueError("Published installer asset differs; it will not be overwritten: " + path.name)
        return {"status": "already-published-identical", "tag": tag, "source_commit": source_commit}
    if not existing:
        release = _gh("--method", "POST", endpoint + "/releases", "--input", "-", input_json={
            "tag_name": tag, "target_commitish": source_commit, "name": "SCP Installer — experimental " + source_commit[:12],
            "draft": True, "prerelease": True, "generate_release_notes": False,
            "body": "Experimental self-contained Windows installer for all implemented pieces.\n\n"
                    "Download the ZIP matching your platform, extract it, and open SCP Installer. Python is included. "
                    "A supported existing NAM installation is required. The installer builds from your local NAM resources; "
                    "the download contains no SimCity or NAM binary resources.\n\n"
                    "The Windows executable is unsigned, so operating-system approval may be required. "
                    "Pieces remain experimental; automated checks are not in-game observations.\n\n"
                    "[Installation instructions](https://github.com/" + repository + "/blob/" + source_commit
                    + "/custom-pieces/docs/INSTALLER.md)\n\nSource commit: `" + source_commit + "`. "
                    "Each ZIP has a SHA-256 sidecar, an exact member manifest, and a frozen-executable self-test report.\n"})
    else:
        release = existing[0]
    # Draft-only retries may replace incomplete assets. Published assets are immutable here.
    subprocess.run(["gh", "release", "upload", tag, *map(str, assets), "--clobber", "--repo", repository], check=True)
    saved = _gh(endpoint + "/releases/" + str(release["id"]))
    by_name = {asset["name"]: asset for asset in saved["assets"]}
    if set(by_name) != {path.name for path in assets} or any(
            by_name[path.name].get("digest") != "sha256:" + _hash(path) for path in assets):
        raise ValueError("Uploaded draft assets differ from the verified platform outputs.")
    _gh("--method", "PATCH", endpoint + "/releases/" + str(release["id"]), "--input", "-",
        input_json={"draft": False, "prerelease": True, "make_latest": "false"})
    return {"status": "published-experimental-prerelease", "tag": tag, "source_commit": source_commit}


def main(arguments: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("prepare", "build"):
        command = commands.add_parser(name)
        command.add_argument("--source", type=Path, default=Path(__file__).resolve().parents[1])
        command.add_argument("--output", type=Path, required=True)
        command.add_argument("--source-commit", required=True)
        command.add_argument("--platform", choices=PLATFORMS, required=True)
    verify = commands.add_parser("verify")
    verify.add_argument("archive", type=Path)
    publication = commands.add_parser("publish")
    publication.add_argument("--artifacts", type=Path, required=True)
    publication.add_argument("--source-commit", required=True)
    publication.add_argument("--repository", required=True)
    options = parser.parse_args(arguments)
    if options.command == "prepare":
        result = prepare_runtime(options.source, options.output / "custom-pieces", options.source_commit, options.platform)
        result = {"status": "passed", "runtime_files": len(result["files"]), "source_commit": result["source_commit"]}
    elif options.command == "build":
        result = build_bundle(options.source, options.output, options.source_commit, options.platform)
    elif options.command == "verify":
        result = verify_archive(options.archive)
    else:
        result = publish(options.artifacts, options.source_commit, options.repository)
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
