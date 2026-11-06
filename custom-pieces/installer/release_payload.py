"""Transfer a verified private installer payload between identical Git trees."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import tempfile
import zipfile
import zlib

KIND = "scp-release-payload"
ENVELOPE = "release-payload.json"
MANIFEST = "manifest.json"
METADATA_LIMIT = 16 * 1024 * 1024
CHUNK_SIZE = 1024 * 1024
GIT_ID = re.compile(r"[0-9a-f]{40}")
SHA256 = re.compile(r"[0-9a-f]{64}")


def _git_id(value, label):
    if not isinstance(value, str) or not GIT_ID.fullmatch(value):
        raise ValueError(f"The {label} must be a complete, lowercase, 40-character Git object ID.")
    return value


def source_identity(repo, revision="HEAD"):
    """Resolve a Git revision to its commit and exact tracked source tree."""
    def resolve(expression):
        result = subprocess.run(
            ["git", "--no-replace-objects", "rev-parse", "--verify", "--end-of-options", expression],
            cwd=repo, check=True, capture_output=True, text=True)
        return result.stdout.strip()

    commit = _git_id(resolve(f"{revision}^{{commit}}"), "source commit")
    tree = _git_id(resolve(f"{commit}^{{tree}}"), "source tree")
    return commit, tree


def archive_name(tree):
    return f"SCP-Prebuilt-Payload-{_git_id(tree, 'source tree')}.zip"


def _json_bytes(value):
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8")


def _zip_path(path, tree):
    from scp.install import _root

    path = Path(path).expanduser().absolute()
    expected = archive_name(tree)
    if path.name != expected:
        raise ValueError(f"Expected a ZIP named {expected}.")
    parent = _root(path.parent, required=False)
    path = parent / path.name
    if path.is_symlink():
        raise ValueError("The prebuilt handoff ZIP must be a regular file.")
    return path


def _stream(source, target=None, *, limit=None):
    digest, size = hashlib.sha256(), 0
    for block in iter(lambda: source.read(CHUNK_SIZE), b""):
        digest.update(block)
        size += len(block)
        if limit is not None and size > limit:
            raise ValueError("A payload file exceeds the size in its manifest.")
        if target is not None:
            target.write(block)
    return digest.hexdigest(), size


def _zip_member(name, size):
    info = zipfile.ZipInfo(name)
    info.create_system = 3
    info.external_attr = (stat.S_IFREG | 0o600) << 16
    info.compress_type = zipfile.ZIP_DEFLATED
    info.file_size = size
    return info


def _record(envelope, source_commit, payload_digest, archive_stream):
    archive_stream.seek(0)
    archive_digest, _ = _stream(archive_stream)
    return {**envelope, "source_commit": source_commit, "payload_manifest_sha256": payload_digest,
            "archive_sha256": archive_digest}


def write_release_payload(payload, zip_path, *, source_commit, source_tree):
    """Write a new handoff ZIP containing only the exact verified payload."""
    from scp.install import FOLDER, _root
    from scp.prebuilt import _indexed_payload, load_payload

    _git_id(source_commit, "prebuild commit")
    zip_path = _zip_path(zip_path, source_tree)
    payload = _root(payload)
    if zip_path.is_relative_to(payload):
        raise ValueError("The prebuilt handoff ZIP must be outside the prepared payload.")
    manifest_path = payload / MANIFEST
    if manifest_path.is_symlink() or not manifest_path.is_file() or manifest_path.stat().st_size > METADATA_LIMIT:
        raise ValueError("The prepared payload manifest is missing, linked, or exceeds its size limit.")
    manifest, manifest_digest = load_payload(payload, source_commit)
    raw_manifest = manifest_path.read_bytes()
    if len(raw_manifest) > METADATA_LIMIT or hashlib.sha256(raw_manifest).hexdigest() != manifest_digest:
        raise ValueError("The prepared payload manifest changed or exceeds its size limit.")
    records = {row["path"]: row for row in manifest["files"]}
    allowed_dirs = {FOLDER, f"{FOLDER}/20_Pieces"}
    actual = set()
    for path in payload.rglob("*"):
        name = path.relative_to(payload).as_posix()
        if path.is_symlink() or not (path.is_file() or path.is_dir() and name in allowed_dirs):
            raise ValueError(f"Unexpected filesystem entry in the prepared payload: {name}")
        if path.is_file():
            actual.add(name)
    if actual != set(records) | {MANIFEST}:
        raise ValueError("The prepared payload contains undeclared or missing files.")
    _indexed_payload(payload, manifest)
    envelope = {"schema_version": 1, "kind": KIND, "prebuild_commit": source_commit,
                "source_tree": source_tree, "prebuild_manifest_sha256": manifest_digest}
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    output = open(zip_path, "x+b", opener=lambda name, flags: os.open(name, flags, 0o600))
    try:
        with output:
            with zipfile.ZipFile(output, "w") as archive:
                for name, raw in ((ENVELOPE, _json_bytes(envelope)), (MANIFEST, raw_manifest)):
                    archive.writestr(_zip_member(name, len(raw)), raw)
                for name, row in sorted(records.items()):
                    with (payload / name).open("rb") as source, archive.open(
                            _zip_member(name, row["bytes"]), "w") as target:
                        if _stream(source, target, limit=row["bytes"]) != (row["sha256"], row["bytes"]):
                            raise ValueError(f"The prepared payload file changed: {name}")
            return _record(envelope, source_commit, manifest_digest, output)
    except BaseException:
        zip_path.unlink(missing_ok=True)
        raise


def _members(archive):
    members = {}
    folded = set()
    for info in archive.infolist():
        name = info.filename
        mode = stat.S_IFMT(info.external_attr >> 16)
        if (name.casefold() in folded or name != info.orig_filename or info.is_dir()
                or mode not in (0, stat.S_IFREG) or info.flag_bits & 1
                or info.compress_type not in (zipfile.ZIP_DEFLATED, zipfile.ZIP_STORED)):
            raise ValueError(f"Unexpected or duplicate handoff ZIP member: {name!r}")
        members[name] = info
        folded.add(name.casefold())
    return members


def _read_metadata(archive, members, name, *, limit):
    info = members.get(name)
    if info is None or info.file_size > limit:
        raise ValueError(f"The handoff ZIP is missing {name} or it exceeds its size limit.")
    return archive.read(info)


def _verified_envelope(archive, members, source_commit, source_tree, repo):
    envelope = json.loads(_read_metadata(archive, members, ENVELOPE, limit=4096))
    if (not isinstance(envelope, dict) or set(envelope) != {
            "schema_version", "kind", "prebuild_commit", "source_tree", "prebuild_manifest_sha256"}
            or type(envelope["schema_version"]) is not int or envelope["schema_version"] != 1
            or envelope["kind"] != KIND):
        raise ValueError("The prebuilt handoff envelope is invalid.")
    original_commit = _git_id(envelope["prebuild_commit"], "original prebuild commit")
    if envelope["source_tree"] != source_tree:
        raise ValueError("The handoff ZIP was prepared for a different Git source tree.")
    digest = envelope["prebuild_manifest_sha256"]
    if not isinstance(digest, str) or not SHA256.fullmatch(digest):
        raise ValueError("The prebuilt handoff is missing the original manifest fingerprint.")
    if repo is None and original_commit != source_commit:
        raise ValueError("A Git checkout is required to confirm both commits before rebinding the payload.")
    if repo is not None:
        for commit in dict.fromkeys((original_commit, source_commit)):
            if source_identity(repo, commit) != (commit, source_tree):
                raise ValueError(f"Git commit {commit} does not contain the claimed source tree.")
    return envelope


def extract_release_payload(zip_path, destination, *, source_commit, source_tree, repo=None):
    """Validate a private handoff, then stage it for packaging at the receiving commit."""
    from scp.install import FOLDER, _root
    from scp.prebuilt import _indexed_payload, load_payload

    _git_id(source_commit, "release source commit")
    _git_id(source_tree, "release source tree")
    destination = _root(destination, required=False)
    if destination.exists():
        raise ValueError("Choose a new directory for the extracted prebuilt payload.")
    try:
        zip_path = _zip_path(zip_path, source_tree)
        if not zip_path.is_file():
            raise ValueError(f"The expected handoff ZIP is missing: {archive_name(source_tree)}.")
        with zip_path.open("rb") as source, zipfile.ZipFile(source) as archive:
            members = _members(archive)
            envelope = _verified_envelope(archive, members, source_commit, source_tree, repo)
            raw_manifest = _read_metadata(archive, members, MANIFEST, limit=METADATA_LIMIT)
            manifest_digest = hashlib.sha256(raw_manifest).hexdigest()
            if manifest_digest != envelope["prebuild_manifest_sha256"]:
                raise ValueError("The original prebuilt payload manifest fingerprint differs.")
            destination.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.TemporaryDirectory(prefix=".scp-release-payload-", dir=destination.parent) as temporary:
                stage = Path(temporary) / "payload"
                stage.mkdir(mode=0o700)
                (stage / FOLDER).mkdir()
                (stage / MANIFEST).write_bytes(raw_manifest)
                manifest, _ = load_payload(stage, envelope["prebuild_commit"])
                if set(members) != {ENVELOPE, MANIFEST, *(row["path"] for row in manifest["files"])}:
                    raise ValueError("The handoff ZIP has undeclared or missing payload members.")
                for row in manifest["files"]:
                    name = row["path"]
                    info = members[name]
                    if info.file_size != row["bytes"]:
                        raise ValueError(f"The prebuilt payload file size differs: {name}")
                    path = stage / name
                    path.parent.mkdir(parents=True, exist_ok=True)
                    with archive.open(info) as member, path.open("xb") as target:
                        if _stream(member, target, limit=row["bytes"]) != (row["sha256"], row["bytes"]):
                            raise ValueError(f"The prebuilt payload file fingerprint differs: {name}")
                _indexed_payload(stage, manifest)
                if envelope["prebuild_commit"] != source_commit:
                    manifest["source_commit"] = source_commit
                    raw_manifest = _json_bytes(manifest)
                    (stage / MANIFEST).write_bytes(raw_manifest)
                    manifest_digest = hashlib.sha256(raw_manifest).hexdigest()
                record = _record(envelope, source_commit, manifest_digest, source)
                if destination.exists() or destination.is_symlink():
                    raise ValueError("The extraction destination already exists.")
                stage.rename(destination)
                return record
    except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError, zipfile.BadZipFile, zlib.error) as error:
        raise ValueError(
            f"Cannot use the prebuilt handoff for release commit {source_commit} "
            f"(Git tree {source_tree}). Prepare a fresh payload for this exact source tree. {error}"
        ) from error
