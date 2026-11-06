"""Validate the release handoff using small DBPFs and real Git commits."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "installer"))
import release_payload
from scp.dbpf import pack_dbpf
from scp.install import FOLDER, NETWORK_INI, RUL0
from scp.menu import MENU_EXEMPLAR
from scp.prebuilt import verify_payload
from scp.track_paths import S3D


MODEL = f"{FOLDER}/20_Pieces/SCP_example.dat"


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


class ReleasePayloadTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="scp-release-handoff-test-")
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name).resolve()
        self.repo = self.base / "source"
        self.repo.mkdir()
        self.git("init", "-q", "--object-format=sha1")
        source = self.repo / "example.txt"
        source.write_text("Original source\n", encoding="utf-8")
        self.git("add", "example.txt")
        self.git("commit", "-qm", "Prepared source")
        self.original, self.tree = release_payload.source_identity(self.repo)
        self.git("commit", "--allow-empty", "-qm", "Promote identical tree")
        self.receiving, identical_tree = release_payload.source_identity(self.repo)
        self.assertEqual(self.tree, identical_tree)
        self.assertNotEqual(self.original, self.receiving)
        source.write_text("Changed tracked source\n", encoding="utf-8")
        self.git("add", "example.txt")
        self.git("commit", "-qm", "Change source tree")
        self.changed, self.changed_tree = release_payload.source_identity(self.repo)
        self.assertNotEqual(self.tree, self.changed_tree)
        self.payload = self.base / "prepared"
        self.archive = self.base / release_payload.archive_name(self.tree)
        self.destination = self.base / "output"
        self.make_payload()

    def git(self, *arguments):
        subprocess.run(["git", "-c", "user.name=SCP fixture", "-c", "user.email=fixture@example.invalid",
                        "-c", "commit.gpgsign=false", *arguments],
                       cwd=self.repo, check=True, capture_output=True)

    def make_payload(self):
        resources = {
            f"{FOLDER}/00_SCP_Controller_NAM50.dat": {RUL0: b"fixture RUL0", NETWORK_INI: b"fixture INI"},
            f"{FOLDER}/10_SCP_Menu.dat": {(*MENU_EXEMPLAR, 0x6A478001): b"fixture menu"},
            MODEL: {(*S3D, 0x7F580000): b"fixture model"},
        }
        files = []
        for name, archive in resources.items():
            path = self.payload / name
            path.parent.mkdir(parents=True, exist_ok=True)
            raw = pack_dbpf(archive)
            path.write_bytes(raw)
            files.append({"path": name, "bytes": len(raw), "sha256": digest(raw)})
        self.manifest = {
            "schema_version": 1, "kind": "scp-prebuilt-payload", "plugin_folder": FOLDER,
            "source_commit": self.original, "verified_build_manifest_sha256": "1" * 64,
            "profile": {"id": "nam50-rhd", "donors": [
                {"filename": "NetworkAddonMod_Controller.dat", "sha256": "2" * 64}]},
            "pieces": [{"id": "example"}], "files": files,
            "dependency_audit": {"textures": [], "shadows": []}, "exclusive_instance_ids": [],
        }
        self.original_manifest = json.dumps(self.manifest).encode()
        (self.payload / "manifest.json").write_bytes(self.original_manifest)

    def write(self):
        return release_payload.write_release_payload(
            self.payload, self.archive, source_commit=self.original, source_tree=self.tree)

    def extract(self, *, commit=None, tree=None, archive=None, destination=None):
        return release_payload.extract_release_payload(
            archive or self.archive, destination or self.destination,
            source_commit=commit or self.receiving, source_tree=tree or self.tree, repo=self.repo)

    def rewrite(self, update):
        with zipfile.ZipFile(self.archive) as archive:
            entries = [(info, archive.read(info)) for info in archive.infolist()]
        with zipfile.ZipFile(self.archive, "w") as archive:
            for name, raw in update(entries):
                archive.writestr(name, raw)

    def test_identical_tree_rebinds_manifest_and_keeps_all_install_files_exact(self):
        written = self.write()
        with zipfile.ZipFile(self.archive) as archive:
            self.assertEqual(set(archive.namelist()), {"release-payload.json", "manifest.json",
                                                       *(row["path"] for row in self.manifest["files"])})
        received = self.extract()
        expected = {**self.manifest, "source_commit": self.receiving}
        self.assertEqual(verify_payload(self.destination, self.receiving), expected)
        self.assertEqual(received, {**written, "source_commit": self.receiving,
                                    "payload_manifest_sha256": digest((self.destination / "manifest.json").read_bytes())})
        self.assertEqual(received["archive_sha256"], digest(self.archive.read_bytes()))
        self.assertEqual(received["prebuild_manifest_sha256"], digest(self.original_manifest))
        self.assertNotEqual(received["prebuild_manifest_sha256"], received["payload_manifest_sha256"])
        self.assertEqual((self.payload / "manifest.json").read_bytes(), self.original_manifest)
        for row in self.manifest["files"]:
            self.assertEqual((self.destination / row["path"]).read_bytes(), (self.payload / row["path"]).read_bytes())

    def test_same_commit_preserves_even_the_original_manifest_serialization(self):
        record = self.write()
        self.assertEqual(self.extract(commit=self.original), record)
        self.assertEqual((self.destination / "manifest.json").read_bytes(), self.original_manifest)

    def test_missing_handoff_identifies_receiving_revision_and_exact_archive(self):
        with self.assertRaisesRegex(ValueError, self.receiving + ".*" + self.tree + ".*missing.*" + self.archive.name):
            self.extract()
        self.assertFalse(self.destination.exists())

    def test_archive_name_cannot_override_the_original_tree(self):
        self.write()
        renamed = self.archive.with_name(release_payload.archive_name(self.changed_tree))
        shutil.copyfile(self.archive, renamed)
        with self.assertRaisesRegex(ValueError, self.changed + ".*different Git source tree"):
            self.extract(commit=self.changed, tree=self.changed_tree, archive=renamed)
        self.assertFalse(self.destination.exists())

    def test_receiving_commit_must_also_contain_the_claimed_tree(self):
        self.write()
        with self.assertRaisesRegex(ValueError, "Git commit " + self.changed + " does not contain the claimed source tree"):
            self.extract(commit=self.changed)
        self.assertFalse(self.destination.exists())

    def test_rebinding_requires_the_git_checkout(self):
        self.write()
        with self.assertRaisesRegex(ValueError, "A Git checkout is required"):
            release_payload.extract_release_payload(
                self.archive, self.destination, source_commit=self.receiving, source_tree=self.tree)
        self.assertFalse(self.destination.exists())

    def test_original_commit_must_contain_the_claimed_tree_even_if_internal_hashes_match(self):
        self.write()
        forged = json.dumps({**self.manifest, "source_commit": self.changed}).encode()

        def update(entries):
            for info, raw in entries:
                if info.filename == "release-payload.json":
                    envelope = json.loads(raw)
                    envelope.update(prebuild_commit=self.changed, prebuild_manifest_sha256=digest(forged))
                    raw = json.dumps(envelope).encode()
                elif info.filename == "manifest.json":
                    raw = forged
                yield info, raw

        self.rewrite(update)
        with self.assertRaisesRegex(ValueError, "Git commit " + self.changed + " does not contain the claimed source tree"):
            self.extract()
        self.assertFalse(self.destination.exists())

    def test_missing_extra_linked_duplicate_or_changed_members_are_rejected(self):
        link = zipfile.ZipInfo("link")
        link.create_system = 3
        link.external_attr = (stat.S_IFLNK | 0o600) << 16
        cases = [
            ("undeclared or missing", lambda entries: [(info, raw) for info, raw in entries if info.filename != MODEL]),
            ("undeclared or missing", lambda entries: [*entries, ("../outside.dat", b"unexpected")]),
            ("Unexpected or duplicate", lambda entries: [*entries, (link, b"manifest.json")]),
            ("Unexpected or duplicate", lambda entries: [*entries, ("MANIFEST.JSON", b"duplicate")]),
            ("fingerprint differs", lambda entries: [(info, raw[:-1] + b"z" if info.filename == MODEL else raw)
                                                     for info, raw in entries]),
            ("manifest fingerprint differs", lambda entries: [
                (info, raw + b" " if info.filename == "manifest.json" else raw) for info, raw in entries]),
        ]
        for expected, update in cases:
            with self.subTest(expected=expected):
                self.write()
                self.rewrite(update)
                with self.assertRaisesRegex(ValueError, expected):
                    self.extract()
                self.assertFalse(self.destination.exists())
                self.assertFalse((self.base / "outside.dat").exists())
                self.archive.unlink()

    def test_invalid_zip_and_incorrect_archive_name_fail_before_extraction(self):
        self.archive.write_bytes(b"incomplete archive")
        with self.assertRaisesRegex(ValueError, self.receiving + ".*File is not a zip file"):
            self.extract()
        with self.assertRaisesRegex(ValueError, "Expected a ZIP named"):
            self.extract(archive=self.archive.with_name("arbitrary.zip"))
        self.assertFalse(self.destination.exists())

    def test_archive_writer_removes_partial_output_and_refuses_to_overwrite(self):
        path = self.payload / MODEL
        original = path.read_bytes()
        path.write_bytes(original.replace(b"fixture model", b"changed model"))
        with self.assertRaisesRegex(ValueError, "prepared payload file changed"):
            self.write()
        self.assertFalse(self.archive.exists())
        path.write_bytes(original)
        first = self.write()
        with self.assertRaises(FileExistsError):
            self.write()
        self.assertEqual(first["archive_sha256"], digest(self.archive.read_bytes()))

    def test_dat_members_are_transferred_without_whole_file_reads(self):
        read_file = Path.read_bytes
        read_member = zipfile.ZipFile.read

        def bounded_file(path):
            self.assertNotEqual(path.suffix, ".dat")
            return read_file(path)

        def bounded_member(archive, info):
            self.assertIn(info.filename, {"manifest.json", "release-payload.json"})
            return read_member(archive, info)

        with patch.object(Path, "read_bytes", bounded_file), patch.object(zipfile.ZipFile, "read", bounded_member):
            self.write()
            self.extract()


if __name__ == "__main__":
    unittest.main()
