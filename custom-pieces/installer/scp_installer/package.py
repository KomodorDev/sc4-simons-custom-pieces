"""Verify installed application files and their revision-bound player payload.

The builder and launcher share these checks. This module contains no freezing,
archive-writing, release-publication, or source-authoring operations.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path, PurePosixPath
import re
import sys


PLATFORMS = ("windows-x64",)
APP_NAME = "SCP Installer"
RUNTIME_MANIFEST = "installer/runtime-manifest.json"
BUILD_INFO = "installer/build-info.json"
PREBUILT_PAYLOAD = "installer/prebuilt"
FROZEN_RUNTIME = "_internal/scp"
SOURCE_BUILDER = "source-local-builder"
PREBUILT_BUILDER = "verified-prebuilt"
GAME_EXTENSIONS = {".dat", ".sc4model", ".sc4lot", ".sc4desc", ".dll", ".exe"}
INSTALL_MANIFEST = "installer/install-manifest.json"
PLAYER_SOURCE_FILES = frozenset({
    "installer/main.py", "installer/scp_installer/package.py",
    "installer/scp_installer/__init__.py", "installer/scp_installer/service.py",
    "installer/scp_installer/gui.py", "installer/scp_installer/ui_support.py",
    "framework/scp/__init__.py", "framework/scp/jsonc.py", "framework/scp/dbpf.py",
    "framework/scp/install.py", "framework/scp/prebuilt.py", "framework/scp/player_manifest.py",
})


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


def _verify_prebuilt_payload(path: Path, commit: str, *, allow_synthetic=True) -> str:
    # This script can run directly without an editable library installation.
    sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "framework"))
    try:
        from scp.prebuilt import SYNTHETIC_FIXTURE_MANIFEST_SHA256, verify_payload
        manifest = verify_payload(path, source_commit=commit)
        if not allow_synthetic and manifest["verified_build_manifest_sha256"] == SYNTHETIC_FIXTURE_MANIFEST_SHA256:
            raise ValueError("A synthetic player fixture can never be a public installer payload.")
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


def _player_runtime_allowed(name: str) -> bool:
    return (name in PLAYER_SOURCE_FILES | {INSTALL_MANIFEST, BUILD_INFO, RUNTIME_MANIFEST}
            or PurePosixPath(name).is_relative_to(PREBUILT_PAYLOAD))


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
        if _verify_prebuilt_payload(root / PREBUILT_PAYLOAD, commit,
                                   allow_synthetic=metadata["review_only"]) != payload_digest:
            raise ValueError("Installer prebuilt payload manifest differs from build metadata.")
        result.update(kind=PREBUILT_BUILDER, prebuilt_payload_manifest_sha256=payload_digest)
        if "release_record" in metadata:
            result["release_record"] = metadata["release_record"]
    return result


def _is_dbpf(path: Path) -> bool:
    with path.open("rb") as stream:
        return stream.read(4) == b"DBPF"
