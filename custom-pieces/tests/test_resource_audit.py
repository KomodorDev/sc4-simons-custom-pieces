"""Exercise exact resource discovery and private byte-preserving capture."""
from contextlib import redirect_stderr, redirect_stdout
import hashlib
import io
import json
from pathlib import Path
import struct
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "framework"))

from scp.dbpf import entries, pack_dbpf, tgi_string
from scp import resource_audit as audit

KEY = (0x5ad0e817, 0xbadb57f1, 0x12345678)
OTHER = (0x5ad0e817, 0xbadb57f1, 0x12345679)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def duplicate_archive(first=b"first", second=b"second"):
    raw = bytearray(pack_dbpf({KEY: first, OTHER: second}))
    offset = struct.unpack_from("<I", raw, 40)[0]
    struct.pack_into("<3I", raw, offset + 20, *KEY)
    return bytes(raw)


class ResourceAuditTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.plugins = self.root / "Plugins"
        self.plugins.mkdir()

    def write_archive(self, name="source.dat", raw=None):
        path = self.plugins / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw or pack_dbpf({KEY: b"source resource"}))
        return path

    def test_reports_every_archive_and_duplicate_index_occurrence_without_winner(self):
        first = self.write_archive("a.dat", duplicate_archive())
        second = self.write_archive("nested/z.SC4Model", pack_dbpf({KEY: b"third variant"}))
        self.write_archive("unrelated.dat", pack_dbpf({OTHER: b"unrelated"}))
        report = audit.audit_plugins(self.plugins, tgi_string(KEY).upper())
        self.assertEqual(report["status"], "complete")
        self.assertEqual((report["archives_inspected"], report["matching_archives"], report["matching_index_entries"]), (3, 2, 3))
        self.assertEqual([match["index_entry_1based"] for match in report["matches"]], [1, 2, 1])
        self.assertEqual([match["tgi_occurrence_1based"] for match in report["matches"]], [1, 2, 1])
        self.assertEqual([match["stored_resource_sha256"] for match in report["matches"]],
                         [digest(b"first"), digest(b"second"), digest(b"third variant")])
        self.assertEqual([match["archive_sha256"] for match in report["matches"]],
                         [digest(first.read_bytes()), digest(first.read_bytes()), digest(second.read_bytes())])
        self.assertEqual(report["stored_variant_count"], 3)
        self.assertFalse(report["selection"]["winner_selected"])
        self.assertFalse(report["selection"]["load_order_evaluated"])
        self.assertFalse(report["selection"]["priority_inferred"])

    def test_compressed_capture_preserves_stored_bytes_and_records_both_hashes(self):
        compressed = b"\x10\xfb\x00\x00\x04\xe0test\xfc"
        archive = self.write_archive(raw=pack_dbpf({KEY: compressed, OTHER: b"unrelated"}))
        original = archive.read_bytes()
        destination = self.root / "local/captures/exact"
        report = audit.capture_resource(archive, KEY, destination, root=self.root, plugins=self.plugins)
        captured = destination / report["capture"]["file"]
        self.assertEqual(entries(captured.read_bytes()), {KEY: compressed})
        self.assertEqual(archive.read_bytes(), original)
        match = report["matches"][0]
        self.assertEqual(match["stored_resource_sha256"], digest(compressed))
        self.assertEqual(match["decompressed_resource_sha256"], digest(b"test"))
        self.assertEqual(match["compression"], "qfs")
        self.assertTrue(report["capture"]["stored_bytes_preserved"])
        self.assertFalse(report["capture"]["installed"])
        self.assertEqual(json.loads((destination / "resource-audit.json").read_text()), report)
        self.assertEqual(sorted(path.name for path in destination.iterdir()), [captured.name, "resource-audit.json"])

    def test_capture_rejects_duplicate_occurrences_even_when_payloads_agree(self):
        archive = self.write_archive(raw=duplicate_archive(b"same", b"same"))
        destination = self.root / "local/captures/ambiguous"
        with self.assertRaisesRegex(ValueError, "Ambiguous capture: 2 index entries"):
            audit.capture_resource(archive, KEY, destination, root=self.root)
        self.assertFalse(destination.exists())
        self.assertFalse((self.root / "local").exists())

    def test_capture_rejects_existing_private_directory_and_preserves_files(self):
        archive = self.write_archive()
        destination = self.root / "local/captures/already"
        destination.mkdir(parents=True)
        marker = destination / "original.txt"
        marker.write_text("preserve")
        with self.assertRaisesRegex(ValueError, "already exists"):
            audit.capture_resource(archive, KEY, destination, root=self.root)
        self.assertEqual(marker.read_text(), "preserve")
        self.assertEqual(list(destination.iterdir()), [marker])

    def test_capture_rejects_public_or_plugins_output_even_within_local(self):
        archive = self.write_archive()
        with self.assertRaisesRegex(ValueError, "private local directory"):
            audit.capture_resource(archive, KEY, self.root / "public/capture", root=self.root)
        fixture = self.root / "local/Plugins"
        fixture.mkdir(parents=True)
        with self.assertRaisesRegex(ValueError, "supplied Plugins"):
            audit.capture_resource(archive, KEY, fixture / "capture", root=self.root, plugins=fixture)
        with self.assertRaisesRegex(ValueError, "inside a Plugins"):
            audit.capture_resource(archive, KEY, fixture / "capture", root=self.root)
        self.assertFalse((fixture / "capture").exists())

    def test_no_match_reads_only_header_and_index_without_hashing_unrelated_archive(self):
        archive = self.write_archive(raw=pack_dbpf({OTHER: b"a" * (4 * 1024 * 1024)}))
        opened = Path.open
        reads = []
        class Tracked:
            def __init__(self, stream):
                self.stream = stream
            def __enter__(self):
                self.stream.__enter__()
                return self
            def __exit__(self, *args):
                return self.stream.__exit__(*args)
            def seek(self, *args):
                return self.stream.seek(*args)
            def read(self, size=-1):
                reads.append(size)
                return self.stream.read(size)
        def tracked(path, mode="r", *args, **kwargs):
            stream = opened(path, mode, *args, **kwargs)
            return Tracked(stream) if path.resolve() == archive.resolve() and mode == "rb" else stream
        with patch.object(Path, "open", tracked), patch.object(Path, "read_bytes", side_effect=AssertionError("Unbounded archive read")):
            report = audit.audit_archive(archive, KEY)
        self.assertEqual(report["status"], "not_found")
        self.assertEqual(reads, [96, 20])

    def test_matching_archive_uses_bounded_hash_reads_and_exact_resource_seek(self):
        archive = self.write_archive(raw=pack_dbpf({KEY: b"small", OTHER: b"z" * (4 * 1024 * 1024)}))
        opened = Path.open
        reads, seeks = [], []
        class Tracked:
            def __init__(self, stream):
                self.stream = stream
            def __enter__(self):
                self.stream.__enter__()
                return self
            def __exit__(self, *args):
                return self.stream.__exit__(*args)
            def seek(self, offset):
                seeks.append(offset)
                return self.stream.seek(offset)
            def read(self, size=-1):
                if not 0 <= size <= audit.HASH_CHUNK_BYTES:
                    raise AssertionError(f"Unbounded read: {size}")
                reads.append(size)
                return self.stream.read(size)
        def tracked(path, mode="r", *args, **kwargs):
            stream = opened(path, mode, *args, **kwargs)
            return Tracked(stream) if path.resolve() == archive.resolve() and mode == "rb" else stream
        with patch.object(Path, "open", tracked), patch.object(Path, "read_bytes", side_effect=AssertionError("Unbounded archive read")):
            report = audit.audit_archive(archive, KEY)
        self.assertEqual(report["matches"][0]["stored_resource_sha256"], digest(b"small"))
        self.assertIn(96, seeks)
        self.assertIn(5, reads)
        self.assertIn(audit.HASH_CHUNK_BYTES, reads)

    def test_bad_archives_and_invalid_resource_are_explicit_and_capture_is_rejected(self):
        self.write_archive("invalid.dat", b"this is not a DBPF archive")
        broken = self.write_archive("broken.dat", pack_dbpf({KEY: b"\x10\xfb\x00\x00\x04\xfc"}))
        report = audit.audit_plugins(self.plugins, KEY)
        self.assertEqual(report["status"], "incomplete")
        self.assertEqual(len(report["errors"]), 1)
        self.assertIn("Invalid DBPF", report["errors"][0]["error"])
        self.assertEqual(report["matches"][0]["decompression_status"], "invalid")
        self.assertIsNone(report["matches"][0]["decompressed_resource_sha256"])
        with self.assertRaisesRegex(ValueError, "invalid resource"):
            audit.capture_resource(broken, KEY, self.root / "local/capture", root=self.root)

    def test_symlinked_inputs_are_reported_without_following_hidden_content(self):
        archive = self.write_archive()
        (self.plugins / "link.dat").symlink_to(archive)
        report = audit.audit_plugins(self.plugins, KEY)
        self.assertEqual(report["status"], "incomplete")
        self.assertEqual(report["matching_index_entries"], 1)
        self.assertIn("Symlinked resource", report["errors"][0]["error"])

    def test_missing_resource_and_archive_are_actionable(self):
        archive = self.write_archive(raw=pack_dbpf({OTHER: b"unrelated"}))
        with self.assertRaisesRegex(ValueError, "Exact TGI .* was not found"):
            audit.capture_resource(archive, KEY, self.root / "local/capture", root=self.root)
        with self.assertRaisesRegex(ValueError, "Archive does not exist"):
            audit.audit_archive(self.plugins / "missing.dat", KEY)
        for value in ("1-2-3", "5ad0e817-badb57f1", (-1, 2, 3), (True, 2, 3)):
            with self.subTest(value=value), self.assertRaises(ValueError):
                audit.parse_tgi(value)

    def test_cli_queries_only_explicit_source_and_requires_archive_for_capture(self):
        archive = self.write_archive()
        with redirect_stdout(io.StringIO()) as output:
            code = audit.main(["--archive", str(archive), "--tgi", tgi_string(KEY)])
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(output.getvalue())["matching_index_entries"], 1)
        with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
            audit.main(["--plugins", str(self.plugins), "--tgi", tgi_string(KEY), "--capture", str(self.root / "local/capture")])
        self.assertEqual(error.exception.code, 2)
        self.assertFalse((self.root / "local/capture").exists())


if __name__ == "__main__":
    unittest.main()
