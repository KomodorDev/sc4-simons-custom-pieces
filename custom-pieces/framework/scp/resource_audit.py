"""Inspect exact resources in explicitly supplied DBPF archives without loading them.

The query reports every index occurrence, rather than choosing a game load-order
winner. Explicit capture writes one selected resource or a pinned multi-source
bundle under the library's private local directory, preserving stored bytes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

from .dbpf import EXTENSIONS, decompress, pack_dbpf, read_index, tgi_string

HASH_CHUNK_BYTES = 1024 * 1024
MAX_RESOURCE_BYTES = 128 * 1024 * 1024
TGI_PATTERN = re.compile(r"(?:0x)?([0-9a-f]{8})-(?:0x)?([0-9a-f]{8})-(?:0x)?([0-9a-f]{8})", re.I)


def parse_tgi(value):
    """Accept one exact, unsigned 32-bit type/group/instance triple."""
    if isinstance(value, str):
        match = TGI_PATTERN.fullmatch(value)
        if not match:
            raise ValueError("Use an exact hexadecimal TGI, for example 5ad0e817-badb57f1-12345678")
        return tuple(int(part, 16) for part in match.groups())
    if (not isinstance(value, (tuple, list)) or len(value) != 3
            or any(isinstance(part, bool) or not isinstance(part, int) or not 0 <= part <= 0xffffffff
                   for part in value)):
        raise ValueError("A TGI must contain exactly three unsigned 32-bit integers")
    return tuple(value)


def _sha(raw):
    return hashlib.sha256(raw).hexdigest()


def _file_identity(path):
    stat = path.stat()
    return stat.st_dev, stat.st_ino, stat.st_size, stat.st_mtime_ns, stat.st_ctime_ns


def _archive_sha(path):
    """An archive hash visits all bytes, using a fixed memory bound."""
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while chunk := stream.read(HASH_CHUNK_BYTES):
            digest.update(chunk)
    return digest.hexdigest()


def _source_path(archive):
    supplied = Path(archive).expanduser().absolute()
    if supplied.is_symlink():
        raise ValueError(f"Select the original archive explicitly, rather than a symlink: {supplied}")
    path = supplied.resolve()
    if not path.is_file():
        raise ValueError(f"Archive does not exist or is not a regular file: {path}")
    return path


def _inspect_archive(archive, key, *, retain_stored=False):
    path = _source_path(archive)
    before = _file_identity(path)
    selected = [(index, entry) for index, entry in enumerate(read_index(path), 1)
                if tuple(entry[:3]) == key]
    matches, stored_payloads = [], []
    if selected:
        oversized = next((index for index, entry in selected if entry[4] > MAX_RESOURCE_BYTES), None)
        if oversized is not None:
            raise ValueError(f"Resource index entry {oversized} exceeds the {MAX_RESOURCE_BYTES}-byte inspection limit: {path}")
        archive_hash = _archive_sha(path)
        with path.open("rb") as stream:
            for occurrence, (index, (_, _, _, offset, length)) in enumerate(selected, 1):
                stream.seek(offset)
                stored = stream.read(length)
                if len(stored) != length:
                    raise ValueError(f"Resource index entry {index} was truncated during inspection: {path}")
                match = {
                    "archive": str(path), "archive_sha256": archive_hash,
                    "archive_bytes": before[2], "tgi": tgi_string(key),
                    "index_entry_1based": index, "tgi_occurrence_1based": occurrence,
                    "stored_offset_bytes": offset, "stored_bytes": length,
                    "stored_resource_sha256": _sha(stored),
                    "compression": "qfs" if stored.find(b"\x10\xfb", 0, 16) >= 0 else "none",
                }
                try:
                    decoded = decompress(stored)
                except ValueError as error:
                    match.update(decompression_status="invalid", decompressed_bytes=None,
                                 decompressed_resource_sha256=None, error=str(error))
                else:
                    match.update(decompression_status="passed", decompressed_bytes=len(decoded),
                                 decompressed_resource_sha256=_sha(decoded))
                matches.append(match)
                if retain_stored:
                    stored_payloads.append(stored)
    if _file_identity(path) != before:
        raise ValueError(f"Archive changed during inspection; retry against stable source bytes: {path}")
    return matches, stored_payloads


def _report(key, matches, errors, *, scope, archive_count):
    invalid = sum(match["decompression_status"] != "passed" for match in matches)
    status = ("incomplete" if errors else "invalid_matches" if invalid else
              "complete" if matches else "not_found")
    return {
        "schema_version": 1, "purpose": "Exact resource discovery; no game load-order selection or installation",
        "status": status, "tgi": tgi_string(key), "scope": scope,
        "archives_inspected": archive_count, "matching_archives": len({match["archive"] for match in matches}),
        "matching_index_entries": len(matches), "matches": matches, "errors": errors,
        "stored_variant_count": len({match["stored_resource_sha256"] for match in matches}),
        "decompressed_variant_count": len({match["decompressed_resource_sha256"] for match in matches
                                           if match["decompressed_resource_sha256"] is not None}),
        "selection": {"winner_selected": False, "load_order_evaluated": False,
                      "priority_inferred": False, "sort_order": "Archive path, then original index entry"},
        "read_scope": {"index": "dbpf.read_index", "resource": "Seek to exact matching index entries only",
                       "archive_hash": "Entire matching archive streamed in bounded chunks",
                       "hash_chunk_bytes": HASH_CHUNK_BYTES, "maximum_stored_resource_bytes": MAX_RESOURCE_BYTES},
        "next_step": ("Resolve the reported archive errors before treating this search as complete" if errors else
                      "Use a valid source resource; malformed compressed bytes cannot be captured" if invalid else
                      "Check the exact TGI and supplied source path; no other directory was searched" if not matches else
                      "Review every occurrence; capture requires one explicitly selected archive with one occurrence"),
        "source_files_modified": False,
    }


def audit_archive(archive, tgi):
    """Audit only the supplied archive and retain duplicate index occurrences."""
    key = parse_tgi(tgi)
    path = _source_path(archive)
    matches, _ = _inspect_archive(path, key)
    return _report(key, matches, [], scope={"archive": str(path)}, archive_count=1)


def audit_plugins(plugins, tgi):
    """Search only the explicitly supplied tree; never infer a preferred match."""
    key = parse_tgi(tgi)
    supplied = Path(plugins).expanduser().absolute()
    if supplied.is_symlink() or not supplied.is_dir():
        raise ValueError(f"Select an existing original Plugins directory: {supplied}")
    root = supplied.resolve()
    matches, errors, archives = [], [], 0
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            if path.is_dir() or path.suffix.lower() in EXTENSIONS:
                errors.append({"archive": str(path), "error": "Symlinked resource content was not searched; audit its original path explicitly"})
            continue
        if not path.is_file() or path.suffix.lower() not in EXTENSIONS:
            continue
        archives += 1
        try:
            found, _ = _inspect_archive(path, key)
        except (OSError, ValueError) as error:
            errors.append({"archive": str(path), "error": str(error)})
        else:
            matches.extend(found)
    return _report(key, matches, errors, scope={"plugins": str(root)}, archive_count=archives)


def _capture_target(destination, *, root=None, plugins=None):
    library = Path(root or Path(__file__).resolve().parents[2]).expanduser().resolve()
    if not library.is_dir():
        raise ValueError(f"Selected library root does not exist: {library}")
    private = (library / "local").resolve()
    if not private.is_relative_to(library):
        raise ValueError("The selected library's private local directory must not resolve outside its root")
    target = Path(destination).expanduser().resolve()
    if target == private or not target.is_relative_to(private):
        raise ValueError(f"Capture output must be a new directory below the selected library's private local directory: {private}")
    if plugins is not None and target.is_relative_to(Path(plugins).expanduser().resolve()):
        raise ValueError("Capture output must not be inside the supplied Plugins directory")
    if any(parent.name.casefold() == "plugins" for parent in (target, *target.parents)):
        raise ValueError("Capture output must not be inside a Plugins directory")
    if target.exists():
        raise ValueError(f"Capture directory already exists; choose a fresh private directory: {target}")
    return target


def _write_capture(target, dat_name, raw, report):
    target.parent.mkdir(parents=True, exist_ok=True)
    target.mkdir()  # Exclusive creation prevents an existing capture from being replaced.
    created = []
    try:
        for name, payload in ((dat_name, raw), ("resource-audit.json", (json.dumps(report, indent=2) + "\n").encode("utf-8"))):
            with (target / name).open("xb") as stream:
                created.append(target / name)
                stream.write(payload)
    except Exception:
        for output in created:
            output.unlink(missing_ok=True)
        target.rmdir()
        raise


def capture_resource(archive, tgi, destination, *, root=None, plugins=None):
    """Copy one unambiguous stored resource to a fresh private capture directory."""
    key = parse_tgi(tgi)
    target = _capture_target(destination, root=root, plugins=plugins)
    path = _source_path(archive)
    matches, stored = _inspect_archive(path, key, retain_stored=True)
    if not matches:
        raise ValueError(f"Exact TGI {tgi_string(key)} was not found in the selected archive: {path}")
    if len(matches) != 1:
        raise ValueError(f"Ambiguous capture: {len(matches)} index entries match {tgi_string(key)} in {path}; select an archive with one exact occurrence")
    if matches[0]["decompression_status"] != "passed":
        raise ValueError(f"Cannot capture an invalid resource: {matches[0]['error']}")
    raw = pack_dbpf({key: stored[0]})
    dat_name = tgi_string(key) + ".dat"
    report = _report(key, matches, [], scope={"archive": str(path)}, archive_count=1)
    report["capture"] = {
        "directory": str(target), "file": dat_name, "sha256": _sha(raw), "bytes": len(raw),
        "resource_count": 1, "stored_bytes_preserved": True, "resource_tgi_unchanged": True,
        "installed": False, "source_archive": str(path), "source_archive_sha256": matches[0]["archive_sha256"],
        "source_index_entry_1based": matches[0]["index_entry_1based"],
        "audit_file": "resource-audit.json",
    }
    _write_capture(target, dat_name, raw, report)
    return report


def inspect_resource_bundle(sources):
    """Read exact resources from explicitly pinned archives, with one hash pass per source.

    Each source supplies ``archive``, ``archive_sha256``, and ``resources``.
    Resource rows require a ``tgi`` and may pin both resource hashes. Sources
    can include portable ``location`` metadata for the game/Plugins locator.
    Returned stored bytes are inputs for private capture, never installed data.
    """
    if not isinstance(sources, list) or not sources:
        raise ValueError("A resource bundle needs a nonempty source list")
    resources, measured, seen_paths = {}, [], set()
    for source in sources:
        path = _source_path(source["archive"])
        if path in seen_paths:
            raise ValueError("A bundle source archive must appear only once")
        seen_paths.add(path)
        expected_hash = source.get("archive_sha256")
        if not isinstance(expected_hash, str) or not re.fullmatch(r"[0-9a-f]{64}", expected_hash):
            raise ValueError("Every bundle source needs a pinned archive SHA-256")
        rows = source.get("resources")
        if not isinstance(rows, list) or not rows:
            raise ValueError("Every bundle source needs exact resource rows")
        keys = [parse_tgi(row["tgi"]) for row in rows]
        if len(set(keys)) != len(keys) or set(keys) & set(resources):
            raise ValueError("Duplicate TGI in resource bundle declaration")
        before = _file_identity(path)
        if source.get("archive_bytes", before[2]) != before[2]:
            raise ValueError(f"Bundle source archive size differs: {path.name}")
        if _archive_sha(path) != expected_hash:
            raise ValueError(f"Bundle source archive fingerprint differs: {path.name}")
        selected = {}
        for entry in read_index(path):
            key = tuple(entry[:3])
            if key in keys:
                selected.setdefault(key, []).append(entry)
        details = []
        with path.open("rb") as stream:
            for row, key in zip(rows, keys):
                entries = selected.get(key, [])
                if len(entries) != 1:
                    raise ValueError(f"Bundle needs one exact occurrence of {tgi_string(key)} in {path.name}; found {len(entries)}")
                _, _, _, offset, length = entries[0]
                if length > MAX_RESOURCE_BYTES:
                    raise ValueError("Bundle resource exceeds the inspection limit")
                stream.seek(offset)
                stored = stream.read(length)
                if len(stored) != length:
                    raise ValueError("Bundle source resource was truncated during inspection")
                decoded = decompress(stored)
                detail = {"tgi": tgi_string(key), "stored_bytes": len(stored),
                          "decompressed_bytes": len(decoded), "stored_resource_sha256": _sha(stored),
                          "decompressed_resource_sha256": _sha(decoded)}
                for field in ("stored_resource_sha256", "decompressed_resource_sha256", "stored_bytes", "decompressed_bytes"):
                    if field in row and row[field] != detail[field]:
                        raise ValueError(f"Bundle resource fingerprint differs: {detail['tgi']} ({field})")
                resources[key] = stored
                details.append(detail)
        if _file_identity(path) != before:
            raise ValueError(f"Archive changed during bundle inspection: {path.name}")
        measured.append({"archive": str(path), "filename": path.name,
                         "location": source.get("location", "explicit"), "archive_sha256": expected_hash,
                         "archive_bytes": before[2], "resources": details})
    return resources, {"schema_version": 1, "capture_kind": "resource-bundle",
                       "purpose": "Exact pinned resource bundle; no load-order inference or installation",
                       "status": "complete", "sources": measured, "source_files_modified": False}


def capture_resource_bundle(sources, destination, *, filename, expected_sha256=None, root=None, plugins=None):
    """Capture a deterministic multi-archive resource set without touching game inputs."""
    if (not isinstance(filename, str) or Path(filename).name != filename or "\\" in filename
            or ":" in filename or not filename.lower().endswith(".dat")):
        raise ValueError("Bundle capture filename must be one plain DAT filename")
    target = _capture_target(destination, root=root, plugins=plugins)
    resources, report = inspect_resource_bundle(sources)
    raw = pack_dbpf(resources)
    if expected_sha256 is not None and _sha(raw) != expected_sha256:
        raise ValueError("Generated bundle capture fingerprint differs from the supported profile")
    report["capture"] = {"directory": str(target), "file": filename, "sha256": _sha(raw),
                         "bytes": len(raw), "resource_count": len(resources),
                         "stored_bytes_preserved": True, "resource_tgi_unchanged": True,
                         "installed": False, "audit_file": "resource-audit.json"}
    _write_capture(target, filename, raw, report)
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tgi", required=True, help="Exact hexadecimal TYPE-GROUP-INSTANCE")
    parser.add_argument("--plugins", help="Search only this existing Plugins directory")
    parser.add_argument("--archive", help="Inspect this exact archive instead of searching a directory")
    parser.add_argument("--capture", help="Capture from --archive to a new directory below the selected root's local/")
    parser.add_argument("--root", help="Library root used to bound private capture output; default: this module's library")
    args = parser.parse_args(argv)
    if not args.plugins and not args.archive:
        parser.error("Supply --plugins for discovery or --archive for exact inspection")
    if args.capture and not args.archive:
        parser.error("--capture requires one explicit --archive; directory discovery never chooses a match")
    try:
        if args.capture:
            report = capture_resource(args.archive, args.tgi, args.capture, root=args.root, plugins=args.plugins)
        elif args.archive:
            report = audit_archive(args.archive, args.tgi)
        else:
            report = audit_plugins(args.plugins, args.tgi)
    except (OSError, ValueError) as error:
        print(json.dumps({"status": "error", "error": str(error)}), file=sys.stderr)
        return 2
    print(json.dumps(report, indent=2))
    return 0 if report["status"] == "complete" else 1 if report["status"] == "not_found" else 2


if __name__ == "__main__":
    raise SystemExit(main())
