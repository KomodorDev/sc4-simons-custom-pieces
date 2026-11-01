"""Pinned multi-source capture keeps exact resources and never changes game inputs."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import struct
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "framework"))
sys.path.insert(0, str(ROOT / "installer"))

from scp import jsonc, resource_audit
from scp.dbpf import decompress, entries, pack_dbpf, tgi_string
from scp_installer import service

FIRST = (0x7AB50E44, 0x1ABE787D, 0x04000200)
SECOND = (0x7AB50E44, 0x1ABE787D, 0x04003800)
PROP = (0x6534284A, 0xC977C536, 0x5EB4BEE9)
UNRELATED = (1, 2, 3)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def source_row(path, location, selected):
    return {"archive": path, "filename": path.name, "location": location,
            "archive_sha256": sha(path.read_bytes()), "archive_bytes": path.stat().st_size,
            "resources": [{"tgi": tgi_string(key), "stored_resource_sha256": sha(raw),
                           "decompressed_resource_sha256": sha(decompress(raw)),
                           "stored_bytes": len(raw), "decompressed_bytes": len(decompress(raw))}
                          for key, raw in selected.items()]}


class BundleFixture:
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.plugins = self.root / "Plugins"
        self.plugins.mkdir()
        self.game = self.root / "Game"
        self.game.mkdir()
        self.first = self.plugins / "native.dat"
        self.second = self.game / "SimCity_4.dat"
        self.stored = {FIRST: b"\x10\xfb\x00\x00\x04\xe0test\xfc", PROP: b"native prop", SECOND: b"full texture"}
        self.first.write_bytes(pack_dbpf({FIRST: self.stored[FIRST], PROP: self.stored[PROP], UNRELATED: b"excluded"}))
        self.second.write_bytes(pack_dbpf({SECOND: self.stored[SECOND], UNRELATED: b"game input stays private"}))
        self.sources = [source_row(self.first, "plugins", {FIRST: self.stored[FIRST], PROP: self.stored[PROP]}),
                        source_row(self.second, "game", {SECOND: self.stored[SECOND]})]
        self.expected = pack_dbpf(self.stored)

    def capture(self, name="fresh", sources=None, **kwargs):
        return resource_audit.capture_resource_bundle(self.sources if sources is None else sources,
            self.root / "local/captures" / name, filename="SCP_AdaptiveAvenue_Capture.dat",
            root=self.root, plugins=self.plugins, **kwargs)


class BundleCaptureTests(BundleFixture, unittest.TestCase):
    def test_capture_is_deterministic_preserves_compression_and_excludes_other_resources(self):
        before = [self.first.read_bytes(), self.second.read_bytes()]
        first = self.capture(expected_sha256=sha(self.expected))
        second = self.capture("reordered", list(reversed(self.sources)))
        for report in (first, second):
            raw = (Path(report["capture"]["directory"]) / report["capture"]["file"]).read_bytes()
            self.assertEqual(raw, self.expected)
            self.assertEqual(entries(raw), self.stored)
            self.assertEqual(report["capture"]["resource_count"], 3)
            self.assertTrue(report["capture"]["stored_bytes_preserved"])
            self.assertFalse(report["capture"]["installed"])
        self.assertEqual([self.first.read_bytes(), self.second.read_bytes()], before)

    def test_selected_resource_cannot_hide_a_changed_original_archive(self):
        self.second.write_bytes(pack_dbpf({SECOND: self.stored[SECOND], UNRELATED: b"different game"}))
        # Keep size independent: the full archive fingerprint is mandatory.
        self.sources[1].pop("archive_bytes")
        with self.assertRaisesRegex(ValueError, "archive fingerprint differs"):
            self.capture()
        self.assertFalse((self.root / "local").exists())

    def test_rehashed_source_cannot_hide_changed_selected_bytes(self):
        self.second.write_bytes(pack_dbpf({SECOND: b"wrong selected texture"}))
        self.sources[1]["archive_sha256"] = sha(self.second.read_bytes())
        self.sources[1]["archive_bytes"] = self.second.stat().st_size
        with self.assertRaisesRegex(ValueError, "resource fingerprint differs"):
            self.capture()
        self.assertFalse((self.root / "local").exists())

    def test_missing_and_duplicate_index_entries_fail_without_writes(self):
        for duplicate in (False, True):
            with self.subTest(duplicate=duplicate):
                raw = bytearray(pack_dbpf({SECOND: self.stored[SECOND], UNRELATED: b"another"}))
                index = struct.unpack_from("<I", raw, 40)[0]
                if duplicate:
                    struct.pack_into("<3I", raw, index, *SECOND)
                else:
                    struct.pack_into("<3I", raw, index + 20, 9, 9, 9)
                self.second.write_bytes(raw)
                self.sources[1]["archive_sha256"] = sha(raw)
                self.sources[1]["archive_bytes"] = len(raw)
                with self.assertRaisesRegex(ValueError, "one exact occurrence"):
                    self.capture()
                self.assertFalse((self.root / "local").exists())

    def test_overlapping_bundle_declarations_are_rejected(self):
        duplicate = deepcopy(self.sources)
        duplicate[0]["resources"].append(duplicate[0]["resources"][0])
        with self.assertRaisesRegex(ValueError, "Duplicate TGI"):
            self.capture(sources=duplicate)

    def test_profile_output_hash_is_checked_before_any_directory_is_created(self):
        with self.assertRaisesRegex(ValueError, "capture fingerprint differs"):
            self.capture(expected_sha256="0" * 64)
        self.assertFalse((self.root / "local").exists())

    def test_output_scope_and_filenames_cannot_target_plugins_or_existing_content(self):
        with self.assertRaisesRegex(ValueError, "private local directory"):
            resource_audit.capture_resource_bundle(self.sources, self.plugins / "bad",
                filename="capture.dat", root=self.root, plugins=self.plugins)
        for filename in ("../capture.dat", "nested/capture.dat", "nested\\capture.dat", "capture.json"):
            with self.subTest(filename=filename), self.assertRaisesRegex(ValueError, "plain DAT filename"):
                resource_audit.capture_resource_bundle(self.sources, self.root / "local/fresh",
                    filename=filename, root=self.root)
        self.capture()
        with self.assertRaisesRegex(ValueError, "already exists"):
            self.capture()


class BundleInstallerTests(BundleFixture, unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.library = self.root / "library"
        self.library.mkdir()
        self.work = self.root / "work"
        self.work.mkdir()
        evidence = {"schema_version": 1, "capture_kind": "resource-bundle",
                    "sources": [{key: value for key, value in row.items() if key != "archive"}
                                for row in self.sources],
                    "capture": {"file": "SCP_AdaptiveAvenue_Capture.dat", "sha256": sha(self.expected)}}
        (self.library / "bundle-audit.json").write_text(json.dumps(evidence))
        self.record = {"filename": "SCP_AdaptiveAvenue_Capture.dat", "sha256": sha(self.expected),
                       "capture_kind": "resource-bundle", "audit": "bundle-audit.json"}
        catalog = {"_profile": {"files": {"adaptive_avenue": self.record}}}
        plan = service.Installation(self.game, self.plugins, (), "win32")
        self.plan = plan
        for mock in (patch.object(service, "load_catalog", return_value=catalog),
                     patch.object(service, "select_pieces", return_value=[{"dependencies": ["adaptive_avenue"]}])):
            mock.start()
            self.addCleanup(mock.stop)

    def prepare(self):
        return service.prepare_captures(self.library, self.plan, self.work, ["synthetic-piece"])

    def test_installer_resolves_game_and_nam_separately_and_keeps_capture_private(self):
        before = [self.first.read_bytes(), self.second.read_bytes()]
        roots, records = self.prepare()
        self.assertEqual(records, [{"label": "adaptive_avenue", "filename": self.record["filename"],
                                    "sha256": self.record["sha256"]}])
        captures = list(roots[0].rglob(self.record["filename"]))
        self.assertEqual(len(captures), 1)
        self.assertEqual(captures[0].read_bytes(), self.expected)
        self.assertTrue(captures[0].is_relative_to(self.work / "local/captures"))
        self.assertEqual([self.first.read_bytes(), self.second.read_bytes()], before)

    def test_existing_capture_never_bypasses_changed_original_game(self):
        captured = self.plugins / self.record["filename"]
        captured.write_bytes(self.expected)
        self.second.write_bytes(pack_dbpf({SECOND: self.stored[SECOND], UNRELATED: b"different game edition"}))
        with self.assertRaisesRegex(ValueError, "archive size differs|archive fingerprint differs"):
            self.prepare()
        self.assertEqual(captured.read_bytes(), self.expected)
        self.assertFalse((self.work / "local").exists())

    def test_existing_valid_capture_is_reused_but_changed_capture_is_preserved(self):
        captured = self.plugins / self.record["filename"]
        captured.write_bytes(self.expected)
        self.assertEqual(self.prepare(), ([], []))
        captured.write_bytes(b"user data")
        with self.assertRaisesRegex(ValueError, "duplicated or differs"):
            self.prepare()
        self.assertEqual(captured.read_bytes(), b"user data")

    def test_duplicate_original_sources_are_not_guessed(self):
        duplicate = self.plugins / "nested" / self.first.name
        duplicate.parent.mkdir()
        duplicate.write_bytes(self.first.read_bytes())
        with self.assertRaisesRegex(ValueError, "found 2"):
            self.prepare()
        self.assertFalse((self.work / "local").exists())

    def test_native_non_capture_audit_is_not_interpreted_as_single_resource_capture(self):
        (self.library / "native.json").write_text(json.dumps({"scope": "Native archive measurements"}))
        record = {"filename": "native.dat", "audit": "native.json", "sha256": sha(self.first.read_bytes())}
        with patch.object(service, "load_catalog", return_value={"_profile": {"files": {"native": record}}}), \
                patch.object(service, "select_pieces", return_value=[{"dependencies": ["native"]}]):
            self.assertEqual(self.prepare(), ([], []))
        self.assertFalse((self.work / "local").exists())


class AdaptiveAvenueCaptureEvidenceTests(unittest.TestCase):
    def test_profile_and_portable_evidence_cover_exact_native_families(self):
        profile = jsonc.load(ROOT / "config/profiles/nam50-rhd.jsonc")["files"]["adaptive_avenue"]
        evidence = json.loads((ROOT / profile["audit"]).read_text())
        self.assertEqual(profile["filename"], "SCP_AdaptiveAvenue_Capture.dat")
        self.assertEqual(profile["sha256"], evidence["capture"]["sha256"])
        self.assertEqual(profile["capture_kind"], "resource-bundle")
        keys = {tuple(int(part, 16) for part in resource["tgi"].split("-"))
                for source in evidence["sources"] for resource in source["resources"]}
        expected = {(0x7AB50E44, 0x1ABE787D, base + appearance + zoom)
                    for base in (0x04000200, 0x04003800)
                    for appearance in (0, 16, 32, 48) for zoom in range(5)} | {PROP}
        self.assertEqual(keys, expected)
        self.assertEqual(evidence["capture"]["resource_count"], 41)
        self.assertFalse(evidence["installed"])
        self.assertFalse(evidence["game_tested"])
        self.assertNotIn(str(Path.home()), json.dumps(evidence))


class ModelShadowLightingInstallerTests(unittest.TestCase):
    """Exercise the existing generic capture route for the new base-game input."""

    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.library, self.work = self.root / 'library', self.root / 'work'
        self.plugins, self.game = self.root / 'Plugins', self.root / 'Game'
        for path in (self.library, self.work, self.plugins, self.game):
            path.mkdir()
        self.key = (0x6534284A, 0xA9189CF0, 0x00000001)
        self.stored = b'synthetic pinned native lighting exemplar'
        self.source = self.game / 'SimCity_1.dat'
        self.source.write_bytes(pack_dbpf({self.key: self.stored, UNRELATED: b'unrelated game content'}))
        self.expected = pack_dbpf({self.key: self.stored})
        row = source_row(self.source, 'game', {self.key: self.stored})
        row.pop('archive')
        evidence = {'schema_version': 1, 'capture_kind': 'resource-bundle', 'sources': [row],
                    'capture': {'file': 'SCP_ModelShadow_Lighting_Capture.dat', 'sha256': sha(self.expected)}}
        (self.library / 'lighting-audit.json').write_text(json.dumps(evidence))
        self.record = {'filename': 'SCP_ModelShadow_Lighting_Capture.dat', 'sha256': sha(self.expected),
                       'capture_kind': 'resource-bundle', 'audit': 'lighting-audit.json'}
        self.plan = service.Installation(self.game, self.plugins, (), 'win32')
        for patcher in (patch.object(service, 'load_catalog', return_value={
                '_profile': {'files': {'model_shadow_lighting': self.record}}}),
                patch.object(service, 'select_pieces', return_value=[{'dependencies': ['model_shadow_lighting']}])):
            patcher.start()
            self.addCleanup(patcher.stop)

    def prepare(self):
        return service.prepare_captures(self.library, self.plan, self.work, ['synthetic-carrier-piece'])

    def test_lighting_is_captured_from_the_selected_game_without_copying_other_resources(self):
        original = self.source.read_bytes()
        roots, records = self.prepare()
        self.assertEqual(records, [{'label': 'model_shadow_lighting', 'filename': self.record['filename'],
                                    'sha256': self.record['sha256']}])
        captured = next(roots[0].rglob(self.record['filename']))
        self.assertEqual(captured.read_bytes(), self.expected)
        self.assertEqual(entries(captured.read_bytes()), {self.key: self.stored})
        self.assertTrue(captured.is_relative_to(self.work / 'local/captures'))
        self.assertEqual(self.source.read_bytes(), original)
        self.assertEqual(list(self.plugins.iterdir()), [])

    def test_a_reused_lighting_capture_cannot_hide_a_different_game_archive(self):
        existing = self.plugins / self.record['filename']
        existing.write_bytes(self.expected)
        self.source.write_bytes(pack_dbpf({self.key: self.stored, UNRELATED: b'a different game edition'}))
        with self.assertRaisesRegex(ValueError, 'archive size differs|archive fingerprint differs'):
            self.prepare()
        self.assertEqual(existing.read_bytes(), self.expected)
        self.assertFalse((self.work / 'local').exists())


class ModelShadowLightingEvidenceTests(unittest.TestCase):
    def test_carrier_dependencies_and_public_evidence_bind_the_exact_supported_light(self):
        from scp.catalog import load_catalog, select_pieces
        from scp.model_shadows import LIGHTING_EXEMPLAR, LIGHTING_SHA256, enabled
        catalog = load_catalog(ROOT)
        selected = select_pieces(catalog, service.all_implemented_ids(ROOT))
        carriers = [piece for piece in selected if piece.get('shadow_mode') == 'model-carrier']
        self.assertTrue(carriers)
        self.assertTrue(all(('model_shadow_lighting' in piece['dependencies']) == enabled(piece)
                            for piece in carriers))
        record = catalog['_profile']['files']['model_shadow_lighting']
        evidence = json.loads((ROOT / record['audit']).read_text())
        self.assertEqual(record['capture_kind'], 'resource-bundle')
        self.assertEqual(record['sha256'], evidence['capture']['sha256'])
        self.assertEqual(evidence['capture']['resource_count'], 1)
        self.assertEqual(len(evidence['sources']), 1)
        source = evidence['sources'][0]
        self.assertEqual((source['filename'], source['location']), ('SimCity_1.dat', 'game'))
        self.assertEqual(len(source['resources']), 1)
        self.assertEqual(source['resources'][0]['tgi'], tgi_string(LIGHTING_EXEMPLAR))
        self.assertEqual(source['resources'][0]['decompressed_resource_sha256'], LIGHTING_SHA256)
        self.assertFalse(evidence['capture']['installed'])
        self.assertNotIn(str(Path.home()), json.dumps(evidence))


if __name__ == "__main__":
    unittest.main()
