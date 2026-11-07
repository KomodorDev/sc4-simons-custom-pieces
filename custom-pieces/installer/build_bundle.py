"""Build a compact prebuilt player app or the separate source-builder review app."""
from __future__ import annotations

import argparse
from contextlib import ExitStack, nullcontext
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
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
PREBUILT_PAYLOAD = "installer/prebuilt"
FROZEN_RUNTIME = "_internal/scp"
SOURCE_BUILDER = "source-local-builder"
PREBUILT_BUILDER = "verified-prebuilt"
ARCHIVE_METADATA_LIMIT = 16 * 1024 * 1024
SOURCE_EXTENSIONS = {".py", ".json", ".jsonc", ".md", ".png", ".svg", ".txt", ".toml"}
FORBIDDEN_PARTS = {"local", "dist", "__pycache__", ".git", ".venv", "node_modules"}
GAME_EXTENSIONS = {".dat", ".sc4model", ".sc4lot", ".sc4desc", ".dll", ".exe"}
INSTALL_MANIFEST = "installer/install-manifest.json"
PLAYER_SOURCE_FILES = frozenset({
    "installer/main.py", "installer/build_bundle.py",
    "installer/scp_installer/__init__.py", "installer/scp_installer/service.py",
    "installer/scp_installer/gui.py", "installer/scp_installer/ui_support.py",
    "framework/scp/__init__.py", "framework/scp/jsonc.py", "framework/scp/dbpf.py",
    "framework/scp/install.py", "framework/scp/prebuilt.py", "framework/scp/player_manifest.py",
})
EXTRACTION_DESTINATION_CHARACTERS = 100
WINDOWS_PATH_CHARACTERS = 259  # MAX_PATH's terminating NUL occupies character 260.
PLAYER_FORBIDDEN_PARTS = frozenset({
    "tests", "testing", "test", "evidence", "previews", "docs", "schemas", "domains",
    "numpy", "numpy.libs", "shapely", "shapely.libs", "pil", "pillow.libs",
    "scp_hsr", "scp_highway", "pytest", "_pytest",
})


def _prepare_install_manifest(source: Path, payload: Path) -> dict:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "framework"))
    try:
        from scp.player_manifest import build_install_manifest
        return build_install_manifest(source, payload)
    finally:
        sys.path.pop(0)


def _player_runtime_allowed(name: str) -> bool:
    return (name in PLAYER_SOURCE_FILES | {INSTALL_MANIFEST, BUILD_INFO, RUNTIME_MANIFEST}
            or PurePosixPath(name).is_relative_to(PREBUILT_PAYLOAD))


def _check_player_member(name: str) -> None:
    member = _relative(name)
    runtime = PurePosixPath(FROZEN_RUNTIME)
    if member.is_relative_to(runtime):
        if not _player_runtime_allowed(member.relative_to(runtime).as_posix()):
            raise ValueError("Player download contains a development file: " + name)
    elif (member.parts[0] != "licenses"
          and any(part.casefold() in PLAYER_FORBIDDEN_PARTS for part in member.parts)):
        raise ValueError("Player download contains an excluded dependency or development file: " + name)


def _windows_characters(value: str) -> int:
    return len(value.encode("utf-16-le")) // 2


def _path_budget(names: list[str]) -> dict:
    longest = max(names, key=_windows_characters)
    length = _windows_characters(longest)
    extracted = EXTRACTION_DESTINATION_CHARACTERS + 1 + length
    if extracted > WINDOWS_PATH_CHARACTERS:
        raise ValueError(f"Installer extraction-path budget exceeded: {extracted} > "
                         f"{WINDOWS_PATH_CHARACTERS} characters: {longest}")
    return {"destination_characters": EXTRACTION_DESTINATION_CHARACTERS,
            "max_path_characters": WINDOWS_PATH_CHARACTERS,
            "longest_member": longest, "longest_member_characters": length,
            "longest_extracted_characters": extracted}


def _source_json(path: Path):
    """Use this source tree's JSONC reader before any application bootstrap."""
    reader_path = Path(__file__).resolve().parents[1] / "framework/scp/jsonc.py"
    spec = spec_from_file_location("_scp_bundle_jsonc", reader_path)
    reader = module_from_spec(spec)
    spec.loader.exec_module(reader)
    return reader.load(path)


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
            or any(part.endswith((".", " ")) or re.fullmatch(
                r"(?:con|prn|aux|nul|com[1-9]|lpt[1-9])(?:\..*)?", part, re.IGNORECASE)
                   for part in path.parts)
            or any(ord(char) < 32 or char in '<>:"|?*' for char in value)):
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
        return path.name in {"project.jsonc", "pyproject.toml", "README.md", "AGENTS.md", "scp.py"}
    if parts[0] in {"framework", "schemas"}:
        return path.suffix in {".py", ".jsonc"}
    if parts[0] == "installer":
        return path.suffix == ".py" and (len(parts) == 2 and path.name in {"main.py", "build_bundle.py"}
                                        or len(parts) == 3 and parts[1] == "scp_installer")
    if parts[0] == "docs":
        return path.suffix in {".md", ".png", ".svg", ".jsonc", ".txt"}
    if parts[0] == "config":
        return relative in {"config/allocations.jsonc", "config/release.jsonc", "config/installer.jsonc"} or (
            len(parts) == 3 and parts[1] == "profiles" and path.suffix == ".jsonc")
    if parts[0] != "domains" or len(parts) < 3 or parts[1] not in domain_names:
        return False
    if len(parts) == 3:
        return path.suffix in {".json", ".jsonc", ".md"}
    if parts[2] == "implementation":
        return path.suffix in {".py", ".jsonc"}
    if parts[2] == "tools":
        return path.suffix == ".py"
    if parts[2] == "assets":
        return path.suffix in {".png", ".svg"}
    if parts[2] in {"00_pieces", "01_assemblies"}:
        if len(parts) == 4:
            return path.name in {"inventory.jsonc", "INVENTORY.md"}
        return "/".join(parts[:4]) in subjects and path.suffix in {
            ".json", ".jsonc", ".md", ".png", ".svg", ".txt"}
    return False


def _runtime_paths(root: Path) -> list[Path]:
    project = _source_json(root / "project.jsonc")
    domains = set(project["domains"])
    subjects = set()
    for record in project["domains"].values():
        registry_path = _relative(record["registry"])
        registry = _source_json(root.joinpath(*registry_path.parts))
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


def _verify_prebuilt_payload(path: Path, commit: str) -> str:
    # This script can run directly without an editable library installation.
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "framework"))
    try:
        from scp.prebuilt import verify_payload
        verify_payload(path, source_commit=commit)
    finally:
        sys.path.pop(0)
    return _hash(path / "manifest.json")


def _distribution_metadata(commit: str, target: str, payload_digest: str | None, *,
                           release_record=None, public=False) -> dict:
    if (public and release_record is None) or (release_record is not None and payload_digest is None):
        raise ValueError("Public prebuilt distribution requires a verified release handoff record.")
    if release_record is not None:
        keys = {"schema_version", "kind", "prebuild_commit", "source_tree", "source_commit",
                "prebuild_manifest_sha256", "payload_manifest_sha256", "archive_sha256"}
        if (not isinstance(release_record, dict) or set(release_record) != keys
                or release_record["schema_version"] != 1 or release_record["kind"] != "scp-release-payload"
                or release_record["source_commit"] != commit
                or release_record["payload_manifest_sha256"] != payload_digest
                or any(not isinstance(release_record[key], str) or not re.fullmatch(r"[0-9a-f]{40}", release_record[key])
                       for key in ("prebuild_commit", "source_tree"))
                or any(not isinstance(release_record[key], str) or not re.fullmatch(r"[0-9a-f]{64}", release_record[key])
                       for key in ("prebuild_manifest_sha256", "archive_sha256"))):
            raise ValueError("The installer payload and its release handoff record disagree.")
    kind = SOURCE_BUILDER if payload_digest is None else PREBUILT_BUILDER
    tag_prefix = "installer-" if payload_digest is None or public else "installer-prebuilt-review-"
    metadata = {"schema_version": 1, "kind": kind, "source_commit": commit,
                "release_tag": tag_prefix + commit[:12], "platform": target,
                "experimental": True, "bundled_native_game_resources": False}
    if payload_digest is not None:
        metadata.update(prebuilt_payload_manifest_sha256=payload_digest, review_only=not public)
    if release_record is not None:
        metadata["release_record"] = release_record
    return metadata


def _check_distribution_metadata(record: dict, commit: str, suffix: str = "") -> str | None:
    digest = record.get("prebuilt_payload_manifest_sha256")
    if digest is not None and (not isinstance(digest, str) or re.fullmatch("[0-9a-f]{64}", digest) is None):
        raise ValueError("Installer prebuilt payload manifest digest is invalid.")
    expected = _distribution_metadata(commit, record.get("platform"), digest,
                                      release_record=record.get("release_record"),
                                      public=record.get("review_only") is False)
    expected["kind"] += suffix
    if (record.get("platform") not in PLATFORMS or record.get("experimental") is not True
            or record.get("bundled_native_game_resources") is not False
            or any(record.get(key) != value for key, value in expected.items())
            or (digest is None and any(key in record for key in
                                      ("prebuilt_payload_manifest_sha256", "review_only", "release_record")))):
        raise ValueError("Installer distribution metadata is inconsistent.")
    return digest


def prepare_runtime(source: Path, destination: Path, source_commit: str, target: str, *,
                    prebuilt_payload: Path | None = None, release_record=None, public_prebuilt=False) -> dict:
    source, destination = source.resolve(), destination.absolute()
    _commit(source_commit)
    if target not in PLATFORMS:
        raise ValueError("Unknown installer platform.")
    if destination.exists() and any(destination.iterdir()):
        raise ValueError("Runtime destination must be new or empty.")
    if source == destination or source.is_relative_to(destination):
        raise ValueError("Runtime output cannot contain or replace the source checkout.")
    payload_digest = None
    if prebuilt_payload is not None:
        payload_digest = _verify_prebuilt_payload(prebuilt_payload, source_commit)
        if destination.is_relative_to(prebuilt_payload.resolve()):
            raise ValueError("Installer runtime output cannot be inside its prebuilt payload input.")
    destination.mkdir(parents=True, exist_ok=True)
    sources = ([source / name for name in sorted(PLAYER_SOURCE_FILES)]
               if prebuilt_payload is not None else _runtime_paths(source))
    missing = [path.relative_to(source).as_posix() for path in sources if not path.is_file()]
    if missing:
        raise ValueError("Installer runtime is missing required source files: " + ", ".join(missing))
    for path in sources:
        if path.is_symlink() or any(parent.is_symlink() for parent in path.parents if parent != source.parent):
            raise ValueError("Installer runtime source must not be a symbolic link: " + str(path.relative_to(source)))
        relative = path.relative_to(source)
        raw = path.read_bytes()
        if raw.startswith(b"DBPF") or path.suffix.lower() in GAME_EXTENSIONS:
            raise ValueError(f"Native game resource is forbidden in installer sources: {relative}")
        output = destination / relative
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(raw)
    required = {"project.jsonc", "pyproject.toml", "installer/main.py", "installer/build_bundle.py",
                "installer/scp_installer/service.py", "config/installer.jsonc", "framework/scp/check_bootstrap.py",
                "framework/scp/jsonc.py"}
    if prebuilt_payload is not None:
        required = PLAYER_SOURCE_FILES
    missing = required - {path.relative_to(source).as_posix() for path in sources}
    if missing:
        raise ValueError("Installer runtime is missing required source files: " + ", ".join(sorted(missing)))
    if prebuilt_payload is not None:
        shutil.copytree(prebuilt_payload, destination / PREBUILT_PAYLOAD, symlinks=True)
        _json(destination / INSTALL_MANIFEST, _prepare_install_manifest(source, prebuilt_payload))
    metadata = _distribution_metadata(source_commit, target, payload_digest,
                                      release_record=release_record, public=public_prebuilt)
    _json(destination / BUILD_INFO, {**metadata, "runtime_manifest": RUNTIME_MANIFEST})
    records = [_record(path, destination) for path in _files(destination)]
    manifest = {"schema_version": 1, "kind": metadata["kind"] + "-runtime",
                "source_commit": source_commit, "files": records}
    _json(destination / RUNTIME_MANIFEST, manifest)
    verify_runtime(destination)
    return manifest


def verify_runtime(root: Path) -> dict:
    """Verify the packaged source and optional payload before using native inputs."""
    root = Path(root).resolve()
    manifest = json.loads((root / RUNTIME_MANIFEST).read_text(encoding="utf-8"))
    metadata = json.loads((root / BUILD_INFO).read_text(encoding="utf-8"))
    commit = _commit(manifest["source_commit"])
    payload_digest = _check_distribution_metadata(metadata, commit)
    if (manifest.get("schema_version") != 1 or manifest.get("kind") != metadata["kind"] + "-runtime"
            or metadata.get("runtime_manifest") != RUNTIME_MANIFEST):
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
        if payload_digest is not None and not _player_runtime_allowed(record["path"]):
            raise ValueError("Player runtime contains a development file: " + record["path"])
        if _record(path, root) != record:
            raise ValueError("Installer source changed: " + record["path"])
        if PurePosixPath(record["path"]).is_relative_to(PREBUILT_PAYLOAD):
            if payload_digest is None:
                raise ValueError("Source-local installer runtime unexpectedly contains a prebuilt payload.")
            continue
        if path.suffix.lower() in GAME_EXTENSIONS or _is_dbpf(path):
            raise ValueError("Installer runtime unexpectedly contains a native game resource.")
    result = {"status": "passed", "source_commit": commit, "files_verified": len(records),
              "bundled_native_game_resources": False}
    if payload_digest is not None:
        if not PLAYER_SOURCE_FILES | {INSTALL_MANIFEST, BUILD_INFO} <= set(names):
            raise ValueError("Player runtime is missing required application files.")
        if _verify_prebuilt_payload(root / PREBUILT_PAYLOAD, commit) != payload_digest:
            raise ValueError("Installer prebuilt payload manifest differs from build metadata.")
        result.update(kind=PREBUILT_BUILDER, prebuilt_payload_manifest_sha256=payload_digest)
        if "release_record" in metadata:
            result["release_record"] = metadata["release_record"]
    return result


def _is_dbpf(path: Path) -> bool:
    with path.open("rb") as stream:
        return stream.read(4) == b"DBPF"


def _bundle_record(path: Path, root: Path) -> dict:
    return {**_record(path, root), "kind": "file", "mode": 0o100755 if path.stat().st_mode & 0o111 else 0o100644}


def create_archive(folder: Path, destination: Path, source_commit: str, target: str) -> dict:
    """Write the Windows app and its exact file manifest into one ZIP."""
    _commit(source_commit)
    folder, destination = Path(folder).resolve(), Path(destination).absolute()
    records = [_bundle_record(path, folder) for path in _files(folder)
               if path.relative_to(folder).as_posix() not in {"bundle-index.json", "SHA256SUMS"}]
    runtime = folder / FROZEN_RUNTIME
    build_info = runtime / BUILD_INFO
    payload_digest = None
    metadata = {}
    if build_info.is_file():
        metadata = json.loads(build_info.read_text(encoding="utf-8"))
        payload_digest = _check_distribution_metadata(metadata, source_commit)
        if metadata["platform"] != target:
            raise ValueError("Installer runtime and ZIP target platforms differ.")
    index = _distribution_metadata(source_commit, target, payload_digest,
                                   release_record=metadata.get("release_record"),
                                   public=metadata.get("review_only") is False)
    index.update(kind=index["kind"] + "-installer", files=records)
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
        report["zip_sha256"] + "  " + destination.name + "\n", encoding="utf-8")
    return report


def _read_archive_metadata(archive: zipfile.ZipFile, info: zipfile.ZipInfo) -> bytes:
    if info.file_size > ARCHIVE_METADATA_LIMIT:
        raise ValueError("Installer ZIP metadata exceeds its size limit: " + info.filename)
    return archive.read(info)


def _stream_archive_member(archive: zipfile.ZipFile, info: zipfile.ZipInfo,
                           destination: Path | None) -> tuple[str, int, bytes]:
    digest = sha256()
    size = 0
    with archive.open(info) as source, (destination.open("wb") if destination else nullcontext()) as target:
        block = source.read(1024 * 1024)
        magic = block[:4]
        while block:
            digest.update(block)
            size += len(block)
            if target is not None:
                target.write(block)
            block = source.read(1024 * 1024)
    return digest.hexdigest(), size, magic


def _payload_destination(root: Path, name: str) -> Path:
    if name != "manifest.json" and re.fullmatch(
            r"zzz_Simons_Custom_Pieces/(?:00_SCP_Controller_NAM50|10_SCP_Menu|20_Pieces/SCP_[a-z0-9-]+)\.dat",
            name) is None:
        raise ValueError("Prebuilt installer ZIP contains an unexpected payload file: " + name)
    destination = root / name
    destination.parent.mkdir(parents=True, exist_ok=True)
    return destination


def verify_archive(path: Path) -> dict:
    """Verify ZIP closure, hashes, and the scope of any prebuilt SCP payload."""
    with zipfile.ZipFile(path) as archive, ExitStack() as cleanup:
        infos = archive.infolist()
        names = [info.filename for info in infos]
        if len(names) != len({name.casefold() for name in names}):
            raise ValueError("Installer ZIP has duplicate members.")
        paths = [_relative(name) for name in names]
        roots = {name.parts[0] for name in paths}
        if len(roots) != 1 or any(len(name.parts) < 2 for name in paths):
            raise ValueError("Installer ZIP must have one enclosing folder.")
        prefix = next(iter(roots)) + "/"
        by_name = {info.filename[len(prefix):]: info for info in infos}
        if not {"bundle-index.json", "SHA256SUMS"} <= by_name.keys():
            raise ValueError("Installer ZIP is missing its bundle index or checksums.")
        index_raw = _read_archive_metadata(archive, by_name["bundle-index.json"])
        index = json.loads(index_raw)
        commit = _commit(index["source_commit"])
        payload_digest = _check_distribution_metadata(index, commit, "-installer")
        path_budget = None
        if payload_digest is not None:
            path_budget = _path_budget(names)
            for name in by_name:
                _check_player_member(name)
        indexed = {_relative(record["path"]).as_posix(): record for record in index["files"]}
        if (len(indexed) != len(index["files"])
                or set(by_name) != indexed.keys() | {"bundle-index.json", "SHA256SUMS"}):
            raise ValueError("Installer ZIP has undeclared or missing members.")

        payload_root = None
        if payload_digest is not None:
            temporary = cleanup.enter_context(tempfile.TemporaryDirectory(prefix="scp-prebuilt-zip-"))
            payload_root = Path(temporary).resolve()
        verified = {"bundle-index.json": sha256(index_raw).hexdigest()}
        payload_prefix = PurePosixPath(FROZEN_RUNTIME, PREBUILT_PAYLOAD)
        for name, record in indexed.items():
            info = by_name[name]
            mode = info.external_attr >> 16
            if info.file_size != record["bytes"] or mode != record["mode"]:
                raise ValueError("Installer ZIP member changed: " + name)
            if record["kind"] != "file" or stat.S_IFMT(mode) != stat.S_IFREG:
                raise ValueError("Unsupported installer ZIP member kind.")
            member = PurePosixPath(name)
            destination = None
            if member.is_relative_to(payload_prefix):
                if payload_root is None:
                    raise ValueError("Source-local installer ZIP unexpectedly contains a prebuilt payload.")
                relative = member.relative_to(payload_prefix).as_posix()
                if relative == "manifest.json" and info.file_size > ARCHIVE_METADATA_LIMIT:
                    raise ValueError("Installer ZIP metadata exceeds its size limit: " + info.filename)
                destination = _payload_destination(payload_root, relative)
            digest, size, magic = _stream_archive_member(archive, info, destination)
            if size != record["bytes"] or digest != record["sha256"]:
                raise ValueError("Installer ZIP member changed: " + name)
            # Frozen Python and its native libraries are part of the executable.
            if destination is None and (member.suffix.lower() in GAME_EXTENSIONS - {".exe", ".dll"}
                                        or magic == b"DBPF"):
                raise ValueError("Installer ZIP contains a native game resource: " + name)
            verified[name] = digest

        build_info = FROZEN_RUNTIME + "/" + BUILD_INFO
        if build_info in by_name:
            metadata = json.loads(_read_archive_metadata(archive, by_name[build_info]))
            if (_check_distribution_metadata(metadata, commit) != payload_digest
                    or metadata["platform"] != index["platform"]
                    or metadata.get("review_only") != index.get("review_only")
                    or metadata.get("release_record") != index.get("release_record")
                    or metadata.get("runtime_manifest") != RUNTIME_MANIFEST):
                raise ValueError("Installer ZIP and runtime metadata differ.")
        elif payload_root is not None:
            raise ValueError("Prebuilt installer ZIP is missing its build metadata.")
        if payload_root is not None:
            manifest_name = FROZEN_RUNTIME + "/" + RUNTIME_MANIFEST
            if manifest_name not in by_name:
                raise ValueError("Prebuilt installer ZIP is missing its runtime manifest.")
            manifest = json.loads(_read_archive_metadata(archive, by_name[manifest_name]))
            _verify_archive_runtime_manifest(manifest, indexed, commit)
            if _verify_prebuilt_payload(payload_root, commit) != payload_digest:
                raise ValueError("Prebuilt installer ZIP payload manifest differs from archive metadata.")

        expected_sums = {}
        sums_raw = _read_archive_metadata(archive, by_name["SHA256SUMS"])
        for line in sums_raw.decode("utf-8").splitlines():
            digest, name = line.split("  ", 1)
            _relative(name)
            if name in expected_sums or re.fullmatch("[0-9a-f]{64}", digest) is None:
                raise ValueError("Installer checksums contain an invalid or duplicate entry.")
            expected_sums[name] = digest
        if expected_sums != verified:
            raise ValueError("Installer checksum closure does not match the archive.")
    result = {"status": "passed", "source_commit": commit, "platform": index["platform"],
              "members_verified": len(names), "bundled_native_game_resources": False, "zip_sha256": _hash(Path(path))}
    if payload_digest is not None:
        result.update(kind=index["kind"], prebuilt_payload_manifest_sha256=payload_digest,
                      review_only=index["review_only"], path_budget=path_budget)
        if "release_record" in index:
            result["release_record"] = index["release_record"]
    return result


def _verify_archive_runtime_manifest(manifest: dict, indexed: dict, commit: str) -> None:
    if (manifest.get("schema_version") != 1 or manifest.get("source_commit") != commit
            or manifest.get("kind") != PREBUILT_BUILDER + "-runtime"):
        raise ValueError("Prebuilt installer ZIP and runtime manifest differ.")
    records = manifest["files"]
    names = [_relative(record["path"]).as_posix() for record in records]
    runtime = FROZEN_RUNTIME + "/"
    runtime_files = {name.removeprefix(runtime): record for name, record in indexed.items()
                     if name.startswith(runtime)}
    if (len(names) != len(set(names)) or RUNTIME_MANIFEST in names
            or set(runtime_files) != set(names) | {RUNTIME_MANIFEST}):
        raise ValueError("Prebuilt installer ZIP file set differs from the runtime manifest.")
    if not PLAYER_SOURCE_FILES | {INSTALL_MANIFEST, BUILD_INFO} <= set(names):
        raise ValueError("Player archive is missing required application files.")
    if any(not _player_runtime_allowed(name) for name in names):
        raise ValueError("Player archive runtime contains a development file.")
    for record in records:
        archived = runtime_files[record["path"]]
        if archived["bytes"] != record["bytes"] or archived["sha256"] != record["sha256"]:
            raise ValueError("Prebuilt installer ZIP runtime file changed: " + record["path"])


def _notices(destination: Path, *, prebuilt: bool = False, public_prebuilt: bool = False) -> None:
    text = ["SCP Installer: bundled third-party software", "", "Python: https://docs.python.org/3/license.html",
            "PyInstaller bootloader: https://pyinstaller.org/en/stable/license.html",
            "Tcl/Tk: https://www.tcl-lang.org/software/tcltk/license.html", "",
            "PyInstaller's licensing exception covers generated bundles; the bundled components retain their own licenses.",
            ("This bundle contains compiled SCP data that may include NAM or SimCity-derived resources."
             if public_prebuilt else
             "Review-only: this bundle contains compiled SCP data that may include NAM or SimCity-derived resources."
             if prebuilt else
             "NAM and SimCity game resources are not included. The installer reads the user's installed dependencies locally."),
            ""]
    licenses = destination / "licenses"
    licenses.mkdir()
    packages = ["pyinstaller", "pyinstaller-hooks-contrib", "altgraph", "packaging"]
    if not prebuilt:
        text.extend(["Pillow: https://github.com/python-pillow/Pillow",
                     "NumPy: https://numpy.org/doc/stable/license.html",
                     "Shapely: https://github.com/shapely/shapely/blob/main/LICENSE.txt",
                     "Bundled GEOS: see the accompanying license files under licenses/shapely."])
        packages += ["Pillow", "numpy", "shapely"]
    for name in packages:
        package = importlib.metadata.distribution(name)
        text.append(f"{package.metadata['Name']} {package.version}")
        for number, file in enumerate(package.files or ()):
            if any(part.casefold().startswith(("license", "copying", "notice")) for part in file.parts):
                source = Path(package.locate_file(file))
                if source.is_file():
                    target = licenses / name / f"{number}-{file.name}"
                    target.parent.mkdir(exist_ok=True)
                    shutil.copyfile(source, target)
    import builtins
    builtins.license._Printer__setup()
    (licenses / "Python.txt").write_text("\n".join(builtins.license._Printer__lines) + "\n", encoding="utf-8")
    (destination / "THIRD-PARTY-NOTICES.txt").write_text("\n".join(text) + "\n", encoding="utf-8")


def _freeze_command(runtime: Path, output: Path, *, prebuilt: bool) -> list[str]:
    command = [sys.executable, "-B", "-m", "PyInstaller", "--noconfirm", "--clean", "--windowed", "--onedir",
               "--python-option", "X utf8", "--name", APP_NAME,
               "--distpath", str(output / "work/frozen"), "--workpath", str(output / "work/pyinstaller"),
               "--specpath", str(output / "work"), "--add-data", str(runtime) + ":scp",
               "--paths", str(runtime / "framework"), "--paths", str(runtime / "installer"),
               "--hidden-import", "tkinter", "--hidden-import", "tkinter.ttk",
               "--hidden-import", "tkinter.filedialog", "--hidden-import", "tkinter.messagebox"]
    if prebuilt:
        # main.py loads this verifier by filename, so module analysis would
        # otherwise miss its standard-library dependencies in the frozen app.
        command += ["--hidden-import", "build_bundle"]
        # Source files are needed by the integrity-checked bootstrap. Freeze
        # only the player modules; never collect installed geometry packages.
        for name in sorted(PLAYER_SOURCE_FILES):
            if name.startswith("framework/scp/") and name.endswith(".py"):
                module = PurePosixPath(name).stem
                command += ["--hidden-import", "scp" if module == "__init__" else "scp." + module]
            elif name.startswith("installer/scp_installer/") and name.endswith(".py"):
                module = PurePosixPath(name).stem
                command += ["--hidden-import", "scp_installer" if module == "__init__" else "scp_installer." + module]
        excluded = {"PIL", "numpy", "shapely", "scp_hsr", "scp_highway", "pytest", "unittest"}
        source_scp = Path(__file__).resolve().parents[1] / "framework/scp"
        included = {PurePosixPath(name).stem for name in PLAYER_SOURCE_FILES if name.startswith("framework/scp/")}
        excluded.update("scp." + path.stem for path in source_scp.glob("*.py") if path.stem not in included)
        for module in sorted(excluded):
            command += ["--exclude-module", module]
    else:
        command += ["--paths", str(runtime / "domains/high-speed-rail/implementation"),
                    "--paths", str(runtime / "domains/highway/implementation")]
        for module in ("scp", "scp_hsr", "scp_highway", "scp_installer"):
            command += ["--collect-submodules", module]
        for module in ("PIL", "numpy", "shapely"):
            command += ["--collect-all", module]
    return [*command, str(runtime / "installer/main.py")]


def check_windows_extraction(archive: Path, output: Path) -> dict:
    """Use Windows Expand-Archive in Downloads, and launch the extracted app."""
    if host_platform() != "windows-x64":
        raise ValueError("The Downloads extraction check requires native Windows.")
    verification = verify_archive(archive)
    if "path_budget" not in verification:
        raise ValueError("The Downloads extraction check requires a compact player archive.")
    downloads = Path.home() / "Downloads"
    downloads.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="SCP-Installer-check-", dir=downloads) as temporary:
        base = Path(temporary)
        remaining = EXTRACTION_DESTINATION_CHARACTERS - _windows_characters(str(base)) - 1
        if remaining < 1:
            raise ValueError("The Windows Downloads test parent exceeds its extraction budget.")
        destination = base / ("Extracted" + "-" * remaining)[:remaining]
        subprocess.run(["powershell.exe", "-NoProfile", "-NonInteractive", "-Command",
                        "$ErrorActionPreference = 'Stop'; Expand-Archive -LiteralPath "
                        "$env:SCP_CHECK_ARCHIVE -DestinationPath $env:SCP_CHECK_DESTINATION"],
                       check=True, timeout=300,
                       env={**os.environ, "SCP_CHECK_ARCHIVE": str(archive.resolve()),
                            "SCP_CHECK_DESTINATION": str(destination)})
        with zipfile.ZipFile(archive) as saved:
            names = saved.namelist()
            extracted = {path.relative_to(destination).as_posix(): path for path in _files(destination)}
            if set(extracted) != set(names):
                raise ValueError("Downloads extraction produced a different file set.")
            index_name = next(name for name in names if name.endswith("/bundle-index.json"))
            index_raw = _read_archive_metadata(saved, saved.getinfo(index_name))
            if extracted[index_name].read_bytes() != index_raw:
                raise ValueError("Downloads extraction changed the bundle index.")
            prefix = PurePosixPath(index_name).parent.as_posix() + "/"
            for record in json.loads(index_raw)["files"]:
                actual = _record(extracted[prefix + record["path"]], destination / prefix)
                if actual != {key: record[key] for key in ("path", "bytes", "sha256")}:
                    raise ValueError("Downloads extraction changed an installer file: " + record["path"])
        executable = destination / prefix / (APP_NAME + ".exe")
        checks = {}
        for action in ("--self-test", "--gui-smoke-test"):
            report = output / ("extracted-" + action[2:] + ".json")
            subprocess.run([str(executable), action, "--report", str(report)], check=True,
                           cwd=destination, timeout=300, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
            result = json.loads(report.read_text(encoding="utf-8"))
            if (result.get("status") != "passed" or result.get("utf8_mode") != 1
                    or result.get("source_commit") != verification["source_commit"]
                    or result.get("runtime_verification", {}).get("prebuilt_payload_manifest_sha256")
                    != verification["prebuilt_payload_manifest_sha256"]):
                raise ValueError("The extracted Windows executable check failed: " + action)
            checks[action[2:]] = result
            report.unlink()
        longest = max(_windows_characters(str(path)) for path in extracted.values())
        if longest > WINDOWS_PATH_CHARACTERS:
            raise ValueError("Downloads extraction exceeded the Windows path budget.")
    return {"status": "passed", "platform": "windows-x64", "source_commit": verification["source_commit"],
            "zip_sha256": verification["zip_sha256"],
            "prebuilt_payload_manifest_sha256": verification["prebuilt_payload_manifest_sha256"],
            "destination_characters": EXTRACTION_DESTINATION_CHARACTERS,
            "longest_extracted_characters": longest, "members_verified": len(names),
            "method": "Windows PowerShell Expand-Archive under Downloads", "executable_checks": checks}


def _check_extraction_report(report: dict, verification: dict) -> None:
    expected = {"status": "passed", "platform": "windows-x64",
                "source_commit": verification["source_commit"], "zip_sha256": verification["zip_sha256"],
                "prebuilt_payload_manifest_sha256": verification["prebuilt_payload_manifest_sha256"],
                "members_verified": verification["members_verified"],
                "destination_characters": EXTRACTION_DESTINATION_CHARACTERS,
                "longest_extracted_characters": verification["path_budget"]["longest_extracted_characters"],
                "method": "Windows PowerShell Expand-Archive under Downloads"}
    if any(report.get(key) != value for key, value in expected.items()):
        raise ValueError("Release requires Downloads extraction evidence for this exact player ZIP.")
    checks = report.get("executable_checks", {})
    if set(checks) != {"self-test", "gui-smoke-test"}:
        raise ValueError("Release requires both extracted Windows executable checks.")
    for check in checks.values():
        if (check.get("status") != "passed" or check.get("utf8_mode") != 1
                or check.get("source_commit") != verification["source_commit"]
                or check.get("runtime_verification", {}).get("prebuilt_payload_manifest_sha256")
                != verification["prebuilt_payload_manifest_sha256"]
                or check.get("runtime_verification", {}).get("release_record") != verification.get("release_record")):
            raise ValueError("Extracted executable checks differ from the verified release ZIP.")
    if (checks["self-test"].get("prebuilt_transaction_verified") is not True
            or checks["self-test"].get("repeat_install_and_rollback") is not True):
        raise ValueError("Extracted executable did not verify initial installation, repeat installation, and Undo.")


def _check_source_revision(source: Path, source_commit: str) -> None:
    revision = subprocess.run(["git", "rev-parse", "HEAD"], cwd=source, text=True, capture_output=True, check=True)
    if revision.stdout.strip() != _commit(source_commit):
        raise ValueError("Installer source commit differs from the checked-out revision.")
    tracked = subprocess.run(["git", "diff", "--quiet", "HEAD", "--", "."], cwd=source, check=False)
    untracked = subprocess.run(["git", "ls-files", "--others", "--exclude-standard", "-z", "--", "."],
                               cwd=source, capture_output=True, check=True)
    if tracked.returncode != 0 or untracked.stdout:
        raise ValueError("A release build or prebuilt review requires clean, committed source files.")


def _check_release_tree(source, record):
    """Recheck the handoff's Git claims independently on the packaging checkout."""
    from release_payload import source_identity

    for commit in dict.fromkeys((record["prebuild_commit"], record["source_commit"])):
        if source_identity(source, commit) != (commit, record["source_tree"]):
            raise ValueError(f"Release handoff commit {commit} does not contain tree {record['source_tree']}.")


def build_bundle(source: Path, output: Path, source_commit: str, target: str, *,
                 prebuilt_payload: Path | None = None, release_record=None, public_prebuilt=False) -> dict:
    if target != host_platform():
        raise ValueError("PyInstaller must run natively on the selected operating system and architecture.")
    _check_source_revision(source, source_commit)
    output = output.absolute()
    if output.exists() and any(output.iterdir()):
        raise ValueError("Bundle output directory must be new or empty.")
    output.mkdir(parents=True, exist_ok=True)
    runtime = output / "work/runtime/custom-pieces"
    prepare_runtime(source, runtime, source_commit, target, prebuilt_payload=prebuilt_payload,
                    release_record=release_record, public_prebuilt=public_prebuilt)
    if prebuilt_payload is not None:
        _check_source_revision(source, source_commit)
    if release_record is not None:
        _check_release_tree(source, release_record)
    # Check Tcl/Tk before freezing; importing it does not open a window.
    import tkinter
    tkinter.Tcl().eval("info patchlevel")
    command = _freeze_command(runtime, output, prebuilt=prebuilt_payload is not None)
    timestamp = subprocess.run(["git", "show", "--no-patch", "--format=%ct", source_commit],
                               cwd=source, text=True, capture_output=True, check=True).stdout.strip()
    if re.fullmatch(r"[0-9]+", timestamp) is None:
        raise ValueError("Cannot determine the source commit's build timestamp.")
    build_environment = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "PYTHONUTF8": "1",
                         "PYTHONHASHSEED": "0", "SOURCE_DATE_EPOCH": timestamp}
    subprocess.run(command, check=True, cwd=runtime, env=build_environment)
    # Neither discovery nor freezing may modify the exact source payload.
    verification = verify_runtime(runtime)
    payload_digest = verification.get("prebuilt_payload_manifest_sha256")
    name = "SCP-Installer-" + ("Prebuilt-Review-" if payload_digest and not public_prebuilt else "") + target + "-" + source_commit[:12]
    # Keep extracted paths short on Windows. The downloadable asset remains
    # versioned; the folder inside it needs no repeated platform or commit.
    folder = output / APP_NAME
    folder.mkdir()
    frozen = output / "work/frozen"
    shutil.copytree(frozen / APP_NAME, folder, dirs_exist_ok=True)
    executable = folder / (APP_NAME + ".exe")
    report_path = output / ("self-test-" + target + ".json")
    subprocess.run([str(executable), "--self-test", "--report", str(report_path)], check=True,
                   timeout=300 if payload_digest else 180, cwd=output,
                   env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    report = json.loads(report_path.read_text(encoding="utf-8"))
    if (report.get("status") != "passed" or report.get("source_commit") != source_commit
            or report.get("utf8_mode") != 1):
        raise ValueError("Frozen installer self-test did not report a pass with UTF-8 mode enabled.")
    if report.get("runtime_verification", {}).get("prebuilt_payload_manifest_sha256") != payload_digest:
        raise ValueError("Frozen installer self-test verified a different prebuilt payload.")
    if release_record is not None:
        payload = json.loads((runtime / PREBUILT_PAYLOAD / "manifest.json").read_bytes())
        if (report.get("prebuilt_transaction_verified") is not True
                or report.get("prebuilt_files_verified") != len(payload["files"])
                or report["runtime_verification"].get("release_record") != release_record):
            raise ValueError("Frozen installer self-test did not verify the complete prebuilt install and handoff.")
    report["platform"] = target
    _json(report_path, report)
    gui_report_path = output / ("gui-smoke-test-" + target + ".json")
    subprocess.run([str(executable), "--gui-smoke-test", "--report", str(gui_report_path)], check=True,
                   timeout=180 if payload_digest else 30, cwd=output,
                   env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    gui_report = json.loads(gui_report_path.read_text(encoding="utf-8"))
    if (gui_report.get("status") != "passed" or gui_report.get("source_commit") != source_commit
            or gui_report.get("utf8_mode") != 1):
        raise ValueError("Frozen installer GUI smoke test did not report a pass with UTF-8 mode enabled.")
    if gui_report.get("runtime_verification", {}).get("prebuilt_payload_manifest_sha256") != payload_digest:
        raise ValueError("Frozen installer GUI smoke test verified a different prebuilt payload.")
    if release_record is not None and gui_report["runtime_verification"].get("release_record") != release_record:
        raise ValueError("Frozen installer GUI smoke test verified a different release handoff.")
    gui_report["platform"] = target
    _json(gui_report_path, gui_report)
    heading = ("SCP Installer — verified-prebuilt release" if public_prebuilt
               else "SCP Installer — review-only verified-prebuilt bundle" if payload_digest
               else "SCP Installer — experimental source/local-builder release")
    content_notice = (
        "This bundle contains the verified compiled SCP catalogue.\n" if public_prebuilt else
        "This bundle contains verified compiled SCP resources and is for private review.\n"
        if payload_digest else "No SimCity or NAM binary resources are included or downloaded by this release.\n")
    (folder / "README.txt").write_text(
        heading + "\n\n"
        "Open SCP Installer.exe. Keep its _internal folder beside it.\n"
        + ("Choose your SimCity 4 player-data Plugins folder, then select Install.\n"
           "Choose the game folder as well if the installer asks for it.\n" if payload_digest else
           "Choose your SimCity 4 game or user-data folder, then select Install.\n")
        + "The supported NAM installation must already be present; the installer checks it before changing Plugins.\n"
        "Python is bundled. No separate Python installation, terminal command, or source checkout is required.\n"
        "Windows may show an unsigned-app warning.\n"
        + content_notice
        + "Generated pieces remain experimental; software verification does not establish in-game testing.\n"
        "Instructions and limitations: https://github.com/KomodorDev/sc4-simons-custom-pieces/blob/"
        + source_commit + "/custom-pieces/docs/INSTALLER.md\n", encoding="utf-8")
    _notices(folder, prebuilt=payload_digest is not None, public_prebuilt=public_prebuilt)
    archive = output / (name + ".zip")
    verification = create_archive(folder, archive, source_commit, target)
    _json(output / ("bundle-index-" + target + ".json"), json.loads((folder / "bundle-index.json").read_text()))
    _json(output / ("archive-check-" + target + ".json"), verification)
    if payload_digest is not None:
        _json(output / ("extraction-check-" + target + ".json"), check_windows_extraction(archive, output))
    if release_record is not None:
        _json(output / "release-record.json", release_record)
    return verification


def _gh(*arguments: str, input_json: dict | None = None) -> dict:
    result = subprocess.run(["gh", "api", *arguments], input=None if input_json is None else json.dumps(input_json),
                            text=True, capture_output=True, check=True)
    return json.loads(result.stdout) if result.stdout.strip() else {}


def publish(artifacts: Path, source_commit: str, repository: str, *, prebuilt_release=False) -> dict:
    """Publish only the verified native outputs of this exact main push."""
    _commit(source_commit)
    if (os.environ.get("GITHUB_EVENT_NAME") != "push" or os.environ.get("GITHUB_REF") != "refs/heads/main"
            or os.environ.get("GITHUB_SHA") != source_commit or os.environ.get("GITHUB_REPOSITORY") != repository):
        raise ValueError("Publishing requires the exact main push in this repository's GitHub Actions workflow.")
    if re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository) is None:
        raise ValueError("Invalid GitHub repository name.")
    if prebuilt_release and os.environ.get("SCP_PREBUILT_PUBLICATION") != "enabled":
        raise ValueError("Public prebuilt publication is disabled in the protected release environment.")
    assets = []
    release_record = None
    for target in PLATFORMS:
        name = "SCP-Installer-" + target + "-" + source_commit[:12] + ".zip"
        matches = list(Path(artifacts).rglob(name))
        if len(matches) != 1:
            raise ValueError("Expected exactly one platform archive: " + name)
        archive = matches[0]
        verification = verify_archive(archive)
        if verification.get("review_only") is True:
            raise ValueError("The public release workflow cannot publish a prebuilt review bundle.")
        if (verification.get("kind") == PREBUILT_BUILDER + "-installer") != prebuilt_release:
            raise ValueError("Release archive does not use the selected installer distribution.")
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
            if prebuilt_release:
                suffix = "/" + FROZEN_RUNTIME + "/" + PREBUILT_PAYLOAD + "/manifest.json"
                payload = json.loads(saved.read(next(name for name in saved.namelist() if name.endswith(suffix))))
        if json.loads(index_path.read_text(encoding="utf-8")) != embedded:
            raise ValueError("Release's external member manifest differs from the verified ZIP.")
        if json.loads(verification_path.read_text(encoding="utf-8")) != verification:
            raise ValueError("Release's external archive-check report differs from the verified ZIP.")
        assets += [archive, sidecar, report_path, gui_path, index_path, verification_path]
        if prebuilt_release:
            extraction_path = archive.parent / ("extraction-check-" + target + ".json")
            extraction = json.loads(extraction_path.read_text(encoding="utf-8"))
            _check_extraction_report(extraction, verification)
            assets.append(extraction_path)
            record_path = archive.with_name("release-record.json")
            release_record = json.loads(record_path.read_text(encoding="utf-8"))
            if (not release_record or release_record != verification.get("release_record")
                    or report.get("prebuilt_transaction_verified") is not True
                    or report.get("prebuilt_files_verified") != len(payload["files"])
                    or any(test.get("runtime_verification", {}).get("release_record") != release_record
                           for test in (report, gui_report))):
                raise ValueError("Release record differs from the verified prebuilt ZIP or executable checks.")
            from main import bootstrap
            from release_handoff import approved_release_head, require_release_evidence

            source = Path(__file__).resolve().parents[1]
            _check_release_tree(source, release_record)
            approved_release_head(source.parent, source_commit, release_record["source_tree"])
            bootstrap(source)
            require_release_evidence(source, payload)
            assets.append(record_path)
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
        package_description = (
            "A supported existing NAM installation is required. The installer verifies your local NAM and installs "
            "the prebuilt SCP catalogue.\n\n" if prebuilt_release else
            "A supported existing NAM installation is required. The installer builds from your local NAM resources.\n\n")
        handoff_description = (
            "Prebuild commit: `" + release_record["prebuild_commit"] + "`. Tracked source tree: `"
            + release_record["source_tree"] + "`. See the release record for both commit IDs and payload checksums.\n"
            if prebuilt_release else "")
        release = _gh("--method", "POST", endpoint + "/releases", "--input", "-", input_json={
            "tag_name": tag, "target_commitish": source_commit, "name": "SCP Installer — experimental " + source_commit[:12],
            "draft": True, "prerelease": True, "generate_release_notes": False,
            "body": "Experimental self-contained Windows installer for all implemented pieces.\n\n"
                    "Download the ZIP matching your platform, extract it, and open SCP Installer. Python is included. "
                    + package_description
                    + "The Windows executable is unsigned, so operating-system approval may be required. "
                    "Pieces remain experimental; automated checks are not in-game observations.\n\n"
                    "[Installation instructions](https://github.com/" + repository + "/blob/" + source_commit
                    + "/custom-pieces/docs/INSTALLER.md)\n\nSource commit: `" + source_commit + "`.\n"
                    + handoff_description
                    + "Each ZIP has a SHA-256 sidecar, an exact member manifest, and a frozen-executable self-test report.\n"})
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
        command.add_argument("--prebuilt-payload", type=Path,
                             help="Embed this verified SCP payload.")
        command.add_argument("--release-record", type=Path, help="Verified Dropbox handoff record.")
        command.add_argument("--public-prebuilt", action="store_true", help=argparse.SUPPRESS)
    verify = commands.add_parser("verify")
    verify.add_argument("archive", type=Path)
    publication = commands.add_parser("publish")
    publication.add_argument("--artifacts", type=Path, required=True)
    publication.add_argument("--source-commit", required=True)
    publication.add_argument("--repository", required=True)
    publication.add_argument("--prebuilt-release", action="store_true")
    options = parser.parse_args(arguments)
    release_record = None
    if options.command in {"prepare", "build"}:
        if options.release_record is not None:
            release_record = json.loads(options.release_record.read_text(encoding="utf-8"))
        if options.public_prebuilt and (os.environ.get("SCP_PREBUILT_PUBLICATION") != "enabled"
                                       or os.environ.get("GITHUB_EVENT_NAME") != "push"
                                       or os.environ.get("GITHUB_REF") != "refs/heads/main"
                                       or os.environ.get("GITHUB_SHA") != options.source_commit):
            raise ValueError("Public prebuilt packaging requires the enabled, exact GitHub Actions main push.")
    if options.command == "prepare":
        if options.prebuilt_payload is not None:
            _check_source_revision(options.source, options.source_commit)
        manifest = prepare_runtime(options.source, options.output / "custom-pieces", options.source_commit,
                                   options.platform, prebuilt_payload=options.prebuilt_payload,
                                   release_record=release_record, public_prebuilt=options.public_prebuilt)
        result = {"status": "passed", "runtime_files": len(manifest["files"]), "source_commit": manifest["source_commit"]}
        if options.prebuilt_payload is not None:
            _check_source_revision(options.source, options.source_commit)
            result["kind"] = manifest["kind"]
    elif options.command == "build":
        result = build_bundle(options.source, options.output, options.source_commit, options.platform,
                              prebuilt_payload=options.prebuilt_payload,
                              release_record=release_record, public_prebuilt=options.public_prebuilt)
    elif options.command == "verify":
        result = verify_archive(options.archive)
    else:
        result = publish(options.artifacts, options.source_commit, options.repository,
                         prebuilt_release=options.prebuilt_release)
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
