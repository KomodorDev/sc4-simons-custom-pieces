"""Installer distributions have exact, public-only source and archive closure."""
from __future__ import annotations

from copy import deepcopy
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import stat
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch
import warnings
import zipfile


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "installer"))
import build_bundle as bundle
from scp.dbpf import pack_dbpf
from scp.install import FOLDER, NETWORK_INI, RUL0
from scp.menu import DESCRIPTION, ICON, MENU_EXEMPLAR, TITLE
from scp.track_paths import PATH, S3D


COMMIT = "1234567890abcdef1234567890abcdef12345678"


class InstallerBundleTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="scp-installer-bundle-")
        self.addCleanup(temporary.cleanup)
        self.directory = Path(temporary.name).resolve()

    def _write(self, root, relative, raw=b"source fixture\n"):
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        return path

    def _downloads_home(self):
        # macOS's resolved default temp directory is much longer than a normal
        # Windows user home; use a short synthetic home for mocked Windows I/O.
        temporary = tempfile.TemporaryDirectory(prefix="scp-", dir="/tmp" if os.name != "nt" else None)
        self.addCleanup(temporary.cleanup)
        return Path(temporary.name)

    def _source(self):
        root = self.directory / "source"
        project = {"profile": "config/profiles/fixture.jsonc",
                   "domains": {"fixture": {"registry": "domains/fixture/domain.jsonc", "path": "domains/fixture"}}}
        registry = {"pieces": ["00_pieces/example/piece.json"], "assemblies": []}
        for relative in set(bundle.PLAYER_SOURCE_FILES) | {"pyproject.toml", "installer/main.py", "installer/build_bundle.py",
                         "installer/scp_installer/service.py", "config/installer.jsonc",
                         "framework/scp/check_bootstrap.py", "framework/scp/__init__.py", "framework/scp/jsonc.py",
                         "domains/fixture/README.md"}:
            self._write(root, relative)
        self._write(root, "project.jsonc", self._commented(project, "Installer fixture project"))
        self._write(root, "domains/fixture/domain.jsonc", self._commented(registry, "Installer fixture domain"))
        self._write(root, "domains/fixture/00_pieces/example/piece.json", json.dumps(
            {"id": "example", "name": "Example piece", "status": "implemented", "game_tests": {}}).encode())
        self._write(root, "config/profiles/fixture.jsonc", json.dumps({"id": "nam50-rhd", "files": {
            "controller": {"filename": "NetworkAddonMod_Controller.dat", "sha256": "b" * 64}}}).encode())
        self._write(root, "domains/highway/menu-layout.jsonc", b'{"layouts":{"fixture":{}}}')
        self._write(root, "config/installer.jsonc", (ROOT / "config/installer.jsonc").read_bytes())
        return root

    def _commented(self, value, title):
        return ("// title: " + json.dumps(title) + '\n// summary: "Portable synthetic installer input."\n'
                + json.dumps(value, indent=2) + "\n").encode()

    def _prepare(self, prebuilt_payload=None, runtime=None, *, real_modules=False, **handoff):
        source = self._source()
        if real_modules:
            for relative in bundle.PLAYER_SOURCE_FILES:
                shutil.copyfile(ROOT / relative, source / relative)
        runtime = runtime or self.directory / "runtime"
        with patch.object(bundle, "_source_paths", return_value=list(source.rglob("*"))) as paths:
            paths.return_value = [path for path in paths.return_value if path.is_file()]
            bundle.prepare_runtime(source, runtime, COMMIT, "windows-x64", prebuilt_payload=prebuilt_payload,
                                   **handoff)
        return runtime

    def _prebuilt_payload(self):
        root = self.directory / "payload"
        menu_id = 0x6A478001
        tile_id = 0x7F580000
        archives = {
            "00_SCP_Controller_NAM50.dat": {RUL0: b"fixture RUL0", NETWORK_INI: b"fixture INI"},
            "10_SCP_Menu.dat": {(*prefix, menu_id): b"fixture menu"
                               for prefix in (MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION)},
            "20_Pieces/SCP_example.dat": {(*S3D, tile_id): b"fixture model",
                                           (*PATH, tile_id): b"fixture path"},
        }
        paths = [self._write(root, f"{FOLDER}/{name}", pack_dbpf(resources))
                 for name, resources in archives.items()]
        manifest = {"schema_version": 1, "kind": "scp-prebuilt-payload", "plugin_folder": FOLDER,
                    "source_commit": COMMIT, "verified_build_manifest_sha256": "a" * 64,
                    "profile": {"id": "nam50-rhd", "donors": [
                        {"filename": "NetworkAddonMod_Controller.dat", "sha256": "b" * 64}]},
                    "pieces": [{"id": "example"}], "files": [bundle._record(path, root) for path in paths],
                    "dependency_audit": {"textures": [], "shadows": []}, "exclusive_instance_ids": []}
        self._write(root, "manifest.json", json.dumps(manifest).encode())
        return root

    def _archive(self, target="windows-x64"):
        folder = self.directory / "SCP-Installer-fixture"
        executable = self._write(folder, "SCP Installer.exe", b"MZ synthetic executable fixture")
        executable.chmod(0o755)
        self._write(folder, "_internal/custom-pieces/project.jsonc", b'{"fixture":true}\n')
        archive = self.directory / "installer.zip"
        bundle.create_archive(folder, archive, COMMIT, target)
        return folder, archive

    def _rewrite_zip(self, archive, transform):
        with zipfile.ZipFile(archive) as source:
            members = [(info, source.read(info.filename)) for info in source.infolist()]
        members = transform(members)
        archive.unlink()
        with zipfile.ZipFile(archive, "w") as destination:
            for info, raw in members:
                destination.writestr(info, raw)

    def _publication(self):
        folder, original = self._archive()
        name = "SCP-Installer-windows-x64-" + COMMIT[:12] + ".zip"
        archive = original.with_name(name)
        original.rename(archive)
        original.with_name("installer.zip.sha256").unlink()
        archive.with_name(name + ".sha256").write_text(bundle._hash(archive) + "  " + name + "\n")
        report = {"status": "passed", "source_commit": COMMIT, "platform": "windows-x64", "utf8_mode": 1}
        for name in ("self-test-windows-x64.json", "gui-smoke-test-windows-x64.json"):
            (self.directory / name).write_text(json.dumps(report))
        index = json.loads((folder / "bundle-index.json").read_text())
        (self.directory / "bundle-index-windows-x64.json").write_text(json.dumps(index))
        (self.directory / "archive-check-windows-x64.json").write_text(json.dumps(bundle.verify_archive(archive)))
        return {"GITHUB_SHA": COMMIT, "GITHUB_REPOSITORY": "owner/repository",
                "GITHUB_EVENT_NAME": "push", "GITHUB_REF": "refs/heads/main"}

    def test_allowlist_excludes_private_builds_tests_and_unregistered_subjects(self):
        allowed = lambda name: bundle.runtime_allowed(name, {"fixture"}, {"domains/fixture/00_pieces/example"})
        for name in ("project.jsonc", "installer/scp_installer/service.py", "framework/scp/build.py",
                     "schemas/connector-groups.schema.jsonc", "docs/templates/assembly-starter.jsonc",
                     "config/profiles/fixture.jsonc", "config/allocations.jsonc", "config/release.jsonc",
                     "config/installer.jsonc", "domains/fixture/domain.jsonc",
                     "domains/fixture/implementation/scp_fixture/geometry-inputs.jsonc",
                     "domains/fixture/00_pieces/inventory.jsonc", "domains/fixture/01_assemblies/inventory.jsonc",
                     "domains/fixture/00_pieces/example/geometry.json",
                     "domains/fixture/00_pieces/example/evidence/design-history/record.json"):
            with self.subTest(name=name):
                self.assertTrue(allowed(name))
        for name in ("local/settings.json", "local/settings.jsonc", "dist/build/manifest.json", "tests/test_build.py",
                     "project.json", "schemas/connector-groups.schema.json", "config/profiles/fixture.json",
                     "config/local.example.jsonc", "domains/fixture/00_pieces/unknown/piece.json",
                     "domains/fixture/00_pieces/example/native.dat", "framework/scp/__pycache__/cache.pyc",
                     "domains/fixture/implementation/scp_fixture/native.dat",
                     "installer/private/settings.json", "domains/fixture/local/secret.json"):
            with self.subTest(name=name):
                self.assertFalse(allowed(name))

    def test_commented_sources_survive_runtime_and_archive_while_reports_stay_strict_json(self):
        source = self._source()
        included = ("project.jsonc", "domains/fixture/domain.jsonc", "config/installer.jsonc",
                    "config/allocations.jsonc", "config/release.jsonc", "config/profiles/fixture.jsonc",
                    "schemas/connector-groups.schema.jsonc", "docs/templates/assembly-starter.jsonc",
                    "domains/fixture/implementation/scp_fixture/geometry-inputs.jsonc",
                    "domains/fixture/inventory.jsonc", "domains/fixture/00_pieces/inventory.jsonc",
                    "domains/fixture/01_assemblies/inventory.jsonc")
        for relative in included[2:]:
            self._write(source, relative, self._commented({"fixture": relative}, "Installer shared source"))
        self._write(source, "local/settings.jsonc", self._commented({"plugins": "private"}, "Private settings"))
        self._write(source, "config/local.example.jsonc", self._commented({}, "Private settings example"))
        expected = {relative: (source / relative).read_bytes() for relative in included}
        runtime = self.directory / "distribution/custom-pieces"
        with patch.object(bundle, "_source_paths", return_value=[path for path in source.rglob("*") if path.is_file()]):
            bundle.prepare_runtime(source, runtime, COMMIT, "windows-x64")
        for relative, raw in expected.items():
            with self.subTest(source=relative):
                self.assertEqual((runtime / relative).read_bytes(), raw)
        self.assertFalse((runtime / "local/settings.jsonc").exists())
        self.assertFalse((runtime / "config/local.example.jsonc").exists())
        for relative in (bundle.RUNTIME_MANIFEST, bundle.BUILD_INFO):
            self.assertIsInstance(json.loads((runtime / relative).read_text()), dict)
        archive = self.directory / "commented-runtime.zip"
        bundle.create_archive(runtime.parent, archive, COMMIT, "windows-x64")
        with zipfile.ZipFile(archive) as saved:
            for relative, raw in expected.items():
                self.assertEqual(saved.read("distribution/custom-pieces/" + relative), raw)
            self.assertIsInstance(json.loads(saved.read("distribution/bundle-index.json")), dict)
        self.assertEqual(bundle.verify_archive(archive)["status"], "passed")

    def test_runtime_retains_source_hierarchy_and_verifies_every_file(self):
        runtime = self._prepare()
        result = bundle.verify_runtime(runtime)
        self.assertEqual(result["status"], "passed")
        self.assertEqual(result["source_commit"], COMMIT)
        self.assertFalse(result["bundled_native_game_resources"])
        self.assertTrue((runtime / "domains/fixture/00_pieces/example/piece.json").is_file())

    def test_native_dbpf_payload_disguised_as_json_is_rejected(self):
        source = self._source()
        self._write(source, "domains/fixture/00_pieces/example/geometry.json", b"DBPF hidden donor bytes")
        with patch.object(bundle, "_source_paths", return_value=[path for path in source.rglob("*") if path.is_file()]):
            with self.assertRaisesRegex(ValueError, "Native game resource"):
                bundle.prepare_runtime(source, self.directory / "runtime", COMMIT, "windows-x64")

    def test_missing_service_cannot_produce_a_runtime(self):
        source = self._source()
        (source / "installer/scp_installer/service.py").unlink()
        with patch.object(bundle, "_source_paths", return_value=[path for path in source.rglob("*") if path.is_file()]):
            with self.assertRaisesRegex(ValueError, "missing required source"):
                bundle.prepare_runtime(source, self.directory / "runtime", COMMIT, "windows-x64")

    def test_changed_or_injected_runtime_source_fails_closed(self):
        runtime = self._prepare()
        path = runtime / "framework/scp/build.py"
        path.write_text("injected\n")
        with self.assertRaisesRegex(ValueError, "file set"):
            bundle.verify_runtime(runtime)
        path.unlink()
        (runtime / "framework/scp/__init__.py").write_text("changed\n")
        with self.assertRaisesRegex(ValueError, "source changed"):
            bundle.verify_runtime(runtime)

    def test_duplicate_runtime_manifest_entry_is_rejected(self):
        runtime = self._prepare()
        path = runtime / bundle.RUNTIME_MANIFEST
        manifest = json.loads(path.read_text())
        manifest["files"].append(deepcopy(manifest["files"][0]))
        path.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, "duplicate"):
            bundle.verify_runtime(runtime)

    def test_runtime_manifest_cannot_reference_outside_tree(self):
        runtime = self._prepare()
        path = runtime / bundle.RUNTIME_MANIFEST
        manifest = json.loads(path.read_text())
        manifest["files"][0]["path"] = "../outside.py"
        path.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, "Unsafe distribution path"):
            bundle.verify_runtime(runtime)

    def test_build_metadata_commit_and_platform_are_bound(self):
        runtime = self._prepare()
        path = runtime / bundle.BUILD_INFO
        original = json.loads(path.read_text())
        for key, value in (("source_commit", "a" * 40), ("platform", "unsupported"),
                           ("bundled_native_game_resources", True), ("experimental", False)):
            with self.subTest(key=key):
                path.write_text(json.dumps({**original, key: value}))
                with self.assertRaisesRegex(ValueError, "inconsistent"):
                    bundle.verify_runtime(runtime)

    def test_prebuilt_runtime_and_zip_include_exact_review_payload_and_digest(self):
        payload = self._prebuilt_payload()
        folder = self.directory / "frozen"
        runtime = self._prepare(payload, folder / bundle.FROZEN_RUNTIME)
        digest = bundle._hash(payload / "manifest.json")
        info = json.loads((runtime / bundle.BUILD_INFO).read_text())
        self.assertEqual(info["kind"], "verified-prebuilt")
        self.assertTrue(info["review_only"])
        self.assertEqual(info["prebuilt_payload_manifest_sha256"], digest)
        self.assertEqual(bundle.verify_runtime(runtime)["prebuilt_payload_manifest_sha256"], digest)
        archive = self.directory / "prebuilt.zip"
        result = bundle.create_archive(folder, archive, COMMIT, "windows-x64")
        self.assertEqual(result["kind"], "verified-prebuilt-installer")
        self.assertTrue(result["review_only"])
        self.assertEqual(result["prebuilt_payload_manifest_sha256"], digest)
        with zipfile.ZipFile(archive) as saved:
            prefix = f"{folder.name}/{bundle.FROZEN_RUNTIME}/{bundle.PREBUILT_PAYLOAD}/"
            included = {name.removeprefix(prefix): saved.read(name) for name in saved.namelist()
                        if name.startswith(prefix)}
            overhead = [info for info in saved.infolist() if not info.filename.startswith(prefix)]
            self.assertEqual(result["player_overhead"], {
                "uncompressed_bytes": sum(info.file_size for info in overhead),
                "compressed_member_bytes": sum(info.compress_size for info in overhead),
                "max_uncompressed_bytes": bundle.PLAYER_OVERHEAD_LIMIT})
        expected = {path.relative_to(payload).as_posix(): path.read_bytes() for path in bundle._files(payload)}
        self.assertEqual(included, expected)

    def test_prebuilt_archive_reads_only_metadata_as_complete_members(self):
        folder = self.directory / "frozen"
        self._prepare(self._prebuilt_payload(), folder / bundle.FROZEN_RUNTIME)
        archive = self.directory / "prebuilt.zip"
        bundle.create_archive(folder, archive, COMMIT, "windows-x64")
        read = zipfile.ZipFile.read

        def read_metadata_only(saved, member):
            name = member.filename if isinstance(member, zipfile.ZipInfo) else member
            self.assertIn(PurePosixPath(name).name,
                          {"bundle-index.json", "build-info.json", "runtime-manifest.json", "SHA256SUMS"})
            return read(saved, member)

        with patch.object(zipfile.ZipFile, "read", new=read_metadata_only):
            self.assertEqual(bundle.verify_archive(archive)["status"], "passed")

    def test_public_prebuilt_zip_binds_the_original_and_receiving_commits(self):
        payload = self._prebuilt_payload()
        digest = bundle._hash(payload / "manifest.json")
        record = {"schema_version": 1, "kind": "scp-release-payload",
                  "prebuild_commit": "a" * 40, "source_tree": "b" * 40, "source_commit": COMMIT,
                  "prebuild_manifest_sha256": "c" * 64, "payload_manifest_sha256": digest,
                  "archive_sha256": "d" * 64}
        folder = self.directory / "frozen"
        runtime = self._prepare(payload, folder / bundle.FROZEN_RUNTIME,
                                release_record=record, public_prebuilt=True)
        self.assertEqual(bundle.verify_runtime(runtime)["release_record"], record)
        archive = self.directory / "prebuilt.zip"
        result = bundle.create_archive(folder, archive, COMMIT, "windows-x64")
        self.assertFalse(result["review_only"])
        self.assertEqual(result["release_record"], record)
        info = json.loads((runtime / bundle.BUILD_INFO).read_bytes())
        self.assertEqual(info["release_tag"], f"installer-{COMMIT[:12]}")
        self.assertEqual(info["source_commit"], COMMIT)
        self.assertNotEqual(info["source_commit"], record["prebuild_commit"])
        with self.assertRaisesRegex(ValueError, "handoff record disagree"):
            bundle._distribution_metadata(COMMIT, "windows-x64", digest,
                                          release_record={**record, "payload_manifest_sha256": "e" * 64},
                                          public=True)

    def test_prebuilt_payload_rejects_a_different_source_revision_or_unexpected_donor_archive(self):
        payload = self._prebuilt_payload()
        manifest = payload / "manifest.json"
        original = manifest.read_bytes()
        manifest.write_text(json.dumps({**json.loads(original), "source_commit": "c" * 40}))
        with self.assertRaisesRegex(ValueError, "source revision"):
            self._prepare(payload)
        manifest.write_bytes(original)
        donor = self._write(payload, f"{FOLDER}/NetworkAddonMod_Controller.dat",
                            pack_dbpf({RUL0: b"native rules"}))
        with self.assertRaisesRegex(ValueError, "undeclared"):
            self._prepare(payload)
        declared = json.loads(original)
        declared["files"].append(bundle._record(donor, payload))
        manifest.write_text(json.dumps(declared))
        with self.assertRaisesRegex(ValueError, "differ from the declared"):
            self._prepare(payload)

    def test_prebuilt_payload_rejects_raw_donor_bytes_under_an_allowed_name(self):
        payload = self._prebuilt_payload()
        manifest_path = payload / "manifest.json"
        manifest = json.loads(manifest_path.read_bytes())
        # Keep the expected controller filename, DBPF resource types, and hashes,
        # but identify its exact bytes as the original installed NAM input.
        donor = payload / FOLDER / "00_SCP_Controller_NAM50.dat"
        manifest["profile"]["donors"][0]["sha256"] = bundle._hash(donor)
        manifest_path.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, "unmodified source archive"):
            self._prepare(payload)

    def test_synthetic_player_fixture_cannot_be_packaged_as_a_public_release(self):
        from scp.prebuilt import SYNTHETIC_FIXTURE_MANIFEST_SHA256
        payload = self._prebuilt_payload()
        filename = payload / "manifest.json"
        manifest = json.loads(filename.read_text())
        manifest["verified_build_manifest_sha256"] = SYNTHETIC_FIXTURE_MANIFEST_SHA256
        filename.write_text(json.dumps(manifest))
        self.assertIsInstance(bundle._verify_prebuilt_payload(payload, COMMIT), str)
        with self.assertRaisesRegex(ValueError, "synthetic player fixture can never"):
            self._prepare(payload, public_prebuilt=True)

    def test_prebuilt_runtime_detects_changed_and_missing_payload_bytes(self):
        runtime = self._prepare(self._prebuilt_payload())
        path = runtime / bundle.PREBUILT_PAYLOAD / FOLDER / "20_Pieces/SCP_example.dat"
        path.write_bytes(b"changed")
        with self.assertRaisesRegex(ValueError, "source changed"):
            bundle.verify_runtime(runtime)
        path.unlink()
        with self.assertRaisesRegex(ValueError, "file set"):
            bundle.verify_runtime(runtime)

    def test_prebuilt_runtime_metadata_and_archive_bind_exact_manifest(self):
        folder = self.directory / "frozen"
        runtime = self._prepare(self._prebuilt_payload(), folder / bundle.FROZEN_RUNTIME)
        info_path = runtime / bundle.BUILD_INFO
        info = json.loads(info_path.read_text())
        info["prebuilt_payload_manifest_sha256"] = "d" * 64
        info_path.write_text(json.dumps(info))
        manifest_path = runtime / bundle.RUNTIME_MANIFEST
        manifest = json.loads(manifest_path.read_text())
        manifest["files"] = [bundle._record(info_path, runtime) if row["path"] == bundle.BUILD_INFO
                             else row for row in manifest["files"]]
        manifest_path.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, "manifest differs from build metadata"):
            bundle.verify_runtime(runtime)
        with self.assertRaisesRegex(ValueError, "manifest differs from archive metadata"):
            bundle.create_archive(folder, self.directory / "prebuilt.zip", COMMIT, "windows-x64")

    def test_raw_game_archive_is_rejected_outside_prebuilt_subtree(self):
        folder = self.directory / "frozen"
        self._prepare(self._prebuilt_payload(), folder / bundle.FROZEN_RUNTIME)
        self._write(folder, "SimCity_3.dat", pack_dbpf({RUL0: b"native rules"}))
        with self.assertRaisesRegex(ValueError, "native game resource"):
            bundle.create_archive(folder, self.directory / "prebuilt.zip", COMMIT, "windows-x64")

    def test_publishing_rejects_prebuilt_review_archive_even_with_public_filename(self):
        folder = self.directory / "frozen"
        self._prepare(self._prebuilt_payload(), folder / bundle.FROZEN_RUNTIME)
        archive = self.directory / ("SCP-Installer-windows-x64-" + COMMIT[:12] + ".zip")
        bundle.create_archive(folder, archive, COMMIT, "windows-x64")
        environment = {"GITHUB_SHA": COMMIT, "GITHUB_REPOSITORY": "owner/repository",
                       "GITHUB_EVENT_NAME": "push", "GITHUB_REF": "refs/heads/main"}
        with patch.dict(os.environ, environment, clear=True), patch.object(bundle, "_gh") as github:
            with self.assertRaisesRegex(ValueError, "cannot publish a prebuilt review bundle"):
                bundle.publish(self.directory, COMMIT, "owner/repository")
            github.assert_not_called()

    def test_archive_hashes_closure_and_executable_mode_are_verified(self):
        folder, archive = self._archive()
        result = bundle.verify_archive(archive)
        self.assertEqual(result["status"], "passed")
        self.assertEqual(result["source_commit"], COMMIT)
        self.assertEqual(result["members_verified"], 4)
        self.assertNotIn("player_overhead", result)
        self.assertEqual(result["zip_bytes"], archive.stat().st_size)
        with zipfile.ZipFile(archive) as saved:
            self.assertEqual(result["uncompressed_bytes"], sum(info.file_size for info in saved.infolist()))
            info = saved.getinfo(folder.name + "/SCP Installer.exe")
            self.assertTrue(info.external_attr >> 16 & stat.S_IXUSR)
        self.assertEqual(archive.with_name("installer.zip.sha256").read_text(), result["zip_sha256"] + "  installer.zip\n")

    def test_versioned_asset_keeps_a_short_enclosing_folder_for_windows_extraction(self):
        folder = self.directory / bundle.APP_NAME
        self._write(folder, "SCP Installer.exe", b"MZ synthetic executable fixture")
        archive = self.directory / ("SCP-Installer-windows-x64-" + COMMIT[:12] + ".zip")
        bundle.create_archive(folder, archive, COMMIT, "windows-x64")
        with zipfile.ZipFile(archive) as saved:
            self.assertTrue(all(name.startswith("SCP Installer/") for name in saved.namelist()))
            self.assertNotIn(archive.stem + "/SCP Installer.exe", saved.namelist())
        self.assertEqual(bundle.verify_archive(archive)["source_commit"], COMMIT)

    def test_archive_changed_member_is_rejected(self):
        _, archive = self._archive()
        self._rewrite_zip(archive, lambda records: [(info, b"changed" if info.filename.endswith("project.jsonc") else raw)
                                                  for info, raw in records])
        with self.assertRaisesRegex(ValueError, "member changed"):
            bundle.verify_archive(archive)

    def test_archive_undeclared_member_is_rejected(self):
        folder, archive = self._archive()
        with zipfile.ZipFile(archive, "a") as saved:
            saved.writestr(folder.name + "/extra.txt", "extra")
        with self.assertRaisesRegex(ValueError, "undeclared"):
            bundle.verify_archive(archive)

    def test_archive_duplicate_member_is_rejected(self):
        folder, archive = self._archive()
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            with zipfile.ZipFile(archive, "a") as saved:
                saved.writestr(folder.name + "/SCP Installer.exe", "duplicate")
        with self.assertRaisesRegex(ValueError, "duplicate members"):
            bundle.verify_archive(archive)

    def test_archive_case_collisions_cannot_overwrite_a_windows_file(self):
        folder, archive = self._archive()
        with zipfile.ZipFile(archive, "a") as saved:
            saved.writestr(folder.name + "/SCP INSTALLER.EXE", "collision")
        with self.assertRaisesRegex(ValueError, "duplicate members"):
            bundle.verify_archive(archive)

    def test_archive_path_traversal_is_rejected(self):
        _, archive = self._archive()
        with zipfile.ZipFile(archive, "a") as saved:
            saved.writestr("../outside.txt", "escape")
        with self.assertRaisesRegex(ValueError, "Unsafe distribution path"):
            bundle.verify_archive(archive)

    def test_archive_with_native_game_dat_is_rejected_even_with_valid_hashes(self):
        folder = self.directory / "native-fixture"
        self._write(folder, "donor.dat", b"DBPF donor fixture")
        with self.assertRaisesRegex(ValueError, "native game resource"):
            bundle.create_archive(folder, self.directory / "native.zip", COMMIT, "windows-x64")

    def test_links_are_forbidden_in_the_windows_distribution(self):
        if os.name == "nt":
            self.skipTest("Creating symbolic links requires privileges unavailable on Windows test hosts.")
        folder = self.directory / "escape-fixture"
        self._write(folder, "inside.txt")
        (folder / "outside").symlink_to(self.directory / "external")
        with self.assertRaisesRegex(ValueError, "Unexpected symbolic link"):
            bundle.create_archive(folder, self.directory / "escape.zip", COMMIT, "windows-x64")

    def test_publishing_is_impossible_from_pull_requests_manual_runs_or_other_branches(self):
        common = {"GITHUB_SHA": COMMIT, "GITHUB_REPOSITORY": "owner/repository"}
        for event, ref in (("pull_request", "refs/pull/1/merge"), ("workflow_dispatch", "refs/heads/main"),
                           ("push", "refs/heads/dev"), ("push", "refs/tags/installer-test")):
            with self.subTest(event=event, ref=ref), patch.dict(os.environ, {
                    **common, "GITHUB_EVENT_NAME": event, "GITHUB_REF": ref}, clear=True):
                with patch.object(bundle, "_gh") as github:
                    with self.assertRaisesRegex(ValueError, "exact main push"):
                        bundle.publish(self.directory, COMMIT, "owner/repository")
                    github.assert_not_called()

    def test_publishing_rejects_mismatched_external_provenance_before_calling_github(self):
        environment = self._publication()
        index = self.directory / "bundle-index-windows-x64.json"
        value = json.loads(index.read_text())
        value["source_commit"] = "a" * 40
        index.write_text(json.dumps(value))
        with patch.dict(os.environ, environment, clear=True), patch.object(bundle, "_gh") as github:
            with self.assertRaisesRegex(ValueError, "external member manifest differs"):
                bundle.publish(self.directory, COMMIT, "owner/repository")
            github.assert_not_called()

    def test_publishing_rejects_gui_smoke_report_from_another_build(self):
        environment = self._publication()
        (self.directory / "gui-smoke-test-windows-x64.json").write_text(json.dumps({
            "status": "passed", "source_commit": "a" * 40, "platform": "windows-x64"}))
        with patch.dict(os.environ, environment, clear=True), patch.object(bundle, "_gh") as github:
            with self.assertRaisesRegex(ValueError, "GUI smoke-test"):
                bundle.publish(self.directory, COMMIT, "owner/repository")
            github.assert_not_called()

    def test_publishing_requires_utf8_mode_in_both_frozen_executable_reports(self):
        environment = self._publication()
        for name in ("self-test-windows-x64.json", "gui-smoke-test-windows-x64.json"):
            path = self.directory / name
            original = json.loads(path.read_text())
            path.write_text(json.dumps({**original, "utf8_mode": 0}))
            with self.subTest(report=name), patch.dict(os.environ, environment, clear=True), \
                    patch.object(bundle, "_gh") as github:
                with self.assertRaisesRegex(ValueError, "frozen"):
                    bundle.publish(self.directory, COMMIT, "owner/repository")
                github.assert_not_called()
            path.write_text(json.dumps(original))

    def test_published_tag_is_never_retargeted(self):
        environment = self._publication()
        wrong = [{"ref": "refs/tags/installer-" + COMMIT[:12], "object": {"type": "commit", "sha": "a" * 40}}]
        with patch.dict(os.environ, environment, clear=True), patch.object(bundle, "_gh", return_value=wrong) as github:
            with self.assertRaisesRegex(ValueError, "different source commit"):
                bundle.publish(self.directory, COMMIT, "owner/repository")
            self.assertEqual(github.call_count, 1)

    def test_published_release_assets_are_never_overwritten(self):
        environment = self._publication()
        ref = [{"ref": "refs/tags/installer-" + COMMIT[:12], "object": {"type": "commit", "sha": COMMIT}}]
        releases = [[{"tag_name": "installer-" + COMMIT[:12], "draft": False, "prerelease": True,
                      "assets": [{"name": "unexpected.zip", "digest": "sha256:" + "a" * 64}]}]]
        with patch.dict(os.environ, environment, clear=True), patch.object(bundle, "_gh", side_effect=[ref, releases]), \
                patch.object(bundle.subprocess, "run") as upload:
            with self.assertRaisesRegex(ValueError, "will not be overwritten"):
                bundle.publish(self.directory, COMMIT, "owner/repository")
            upload.assert_not_called()

    def test_freezing_requires_native_platform(self):
        with patch.object(bundle, "host_platform", return_value="unsupported"):
            with self.assertRaisesRegex(ValueError, "run natively"):
                bundle.build_bundle(self.directory, self.directory / "output", COMMIT, "windows-x64")

    def test_player_runtime_has_only_application_sources_generated_data_and_finished_payload(self):
        source = self._source()
        for name in ("docs/guide.md", "domains/fixture/00_pieces/example/previews/preview.png",
                     "domains/fixture/00_pieces/example/evidence/design-history/report.json",
                     "framework/scp/build.py", "tests/test_piece.py"):
            self._write(source, name)
        runtime = self.directory / "runtime"
        payload = self._prebuilt_payload()
        bundle.prepare_runtime(source, runtime, COMMIT, "windows-x64", prebuilt_payload=payload)
        expected = bundle.PLAYER_SOURCE_FILES | {bundle.BUILD_INFO, bundle.RUNTIME_MANIFEST, bundle.INSTALL_MANIFEST}
        actual = {path.relative_to(runtime).as_posix() for path in bundle._files(runtime)
                  if not path.is_relative_to(runtime / bundle.PREBUILT_PAYLOAD)}
        self.assertEqual(actual, expected)
        self.assertFalse((runtime / "installer/build_bundle.py").exists())
        self.assertTrue((runtime / "installer/scp_installer/package.py").is_file())
        generated = json.loads((runtime / bundle.INSTALL_MANIFEST).read_text())
        self.assertEqual(generated["pieces"], [{"id": "example", "name": "Example piece"}])
        for forbidden in ("design-history", "preview.png", "source fixture"):
            self.assertNotIn(forbidden, json.dumps(generated))

    def test_player_archive_rejects_development_or_unused_dependency_files_even_with_valid_hashes(self):
        folder = self.directory / "frozen"
        self._prepare(self._prebuilt_payload(), folder / bundle.FROZEN_RUNTIME)
        for name in ("_internal/numpy/__init__.py", "_internal/shapely/lib.dll", "_internal/PIL/Image.py",
                     "_internal/package/tests/test_resource.py", "_internal/scp/docs/guide.md",
                     "_internal/scp/installer/build_bundle.py",
                     "_internal/tcl8/8.5/tcltest-2.5.3.tm", "_internal/tcl8/8.5/TCLTEST-helper.tm"):
            with self.subTest(name=name):
                injected = self._write(folder, name)
                with self.assertRaisesRegex(ValueError, "development file|excluded dependency"):
                    bundle.create_archive(folder, self.directory / "excluded.zip", COMMIT, "windows-x64")
                injected.unlink()
                (self.directory / "excluded.zip").unlink()

    def test_player_trim_removes_only_tcltest_modules_and_preserves_licenses(self):
        folder = self.directory / "frozen"
        removed = [self._write(folder, name) for name in (
            "_internal/tcl8/8.5/tcltest-2.5.3.tm", "_internal/TCLTEST-support/nested/fixture.tcl")]
        retained = [self._write(folder, name, b"retain exact bytes") for name in (
            "_internal/tcl8/8.6/http-2.9.tm", "_internal/_tk_data/ttk/ttk.tcl",
            "licenses/tcltest-NOTICE.txt", "licenses/TclTest/licenses.txt")]
        bundle._trim_player_runtime(folder)
        self.assertTrue(all(not path.exists() for path in removed))
        self.assertFalse((folder / "_internal/TCLTEST-support").exists())
        for path in retained:
            self.assertEqual(path.read_bytes(), b"retain exact bytes")
            bundle._check_player_member(path.relative_to(folder).as_posix())

    def test_player_freezer_has_no_collect_all_or_geometry_modules(self):
        command = bundle._freeze_command(self.directory / "runtime", self.directory / "output", prebuilt=True)
        self.assertNotIn("--collect-all", command)
        self.assertNotIn("--collect-submodules", command)
        excluded = {command[index + 1] for index, token in enumerate(command) if token == "--exclude-module"}
        self.assertTrue({"PIL", "numpy", "shapely", "scp_hsr", "scp_highway", "scp.build", "scp.catalog"} <= excluded)
        included = {command[index + 1] for index, token in enumerate(command) if token == "--hidden-import"}
        self.assertIn("scp.player_manifest", included)
        self.assertIn("scp_installer.package", included)
        self.assertNotIn("build_bundle", included)

    def test_player_overhead_budget_rejects_unknown_bloat_before_payload_extraction(self):
        folder = self.directory / "frozen"
        self._prepare(self._prebuilt_payload(), folder / bundle.FROZEN_RUNTIME)
        unused_name = "_internal/scipy/linalg/_unused.pyd"
        unused = folder / unused_name
        unused.parent.mkdir(parents=True)
        with unused.open("wb") as stream:
            stream.truncate(bundle.PLAYER_OVERHEAD_LIMIT + 1)
        archive = self.directory / "oversized.zip"
        with patch.object(bundle.tempfile, "TemporaryDirectory", side_effect=AssertionError("Payload extracted")):
            with self.assertRaisesRegex(ValueError, "application overhead budget exceeded"):
                bundle.create_archive(folder, archive, COMMIT, "windows-x64")

        # Even a forged small index value cannot replace the central-directory
        # size, which is checked before opening any large archive member.
        def understate_index(records):
            changed = []
            for info, raw in records:
                if info.filename.endswith("/bundle-index.json"):
                    index = json.loads(raw)
                    next(row for row in index["files"] if row["path"] == unused_name)["bytes"] = 1
                    raw = json.dumps(index).encode()
                changed.append((info, raw))
            return changed

        self._rewrite_zip(archive, understate_index)
        with patch.object(bundle, "_stream_archive_member", side_effect=AssertionError("Large member opened")):
            with self.assertRaisesRegex(ValueError, "application overhead budget exceeded"):
                bundle.verify_archive(archive)

    def test_player_overhead_budget_excludes_only_recognized_payload_paths(self):
        application = zipfile.ZipInfo("_internal/python311.dll")
        application.file_size = bundle.PLAYER_OVERHEAD_LIMIT
        application.compress_size = 12
        payload_name = f"{bundle.FROZEN_RUNTIME}/{bundle.PREBUILT_PAYLOAD}/{FOLDER}/20_Pieces/SCP_example.dat"
        payload = zipfile.ZipInfo(payload_name)
        payload.file_size = bundle.PLAYER_OVERHEAD_LIMIT * 100
        payload.compress_size = 34
        report = bundle._player_overhead({application.filename: application, payload.filename: payload})
        self.assertEqual(report["uncompressed_bytes"], bundle.PLAYER_OVERHEAD_LIMIT)
        self.assertEqual(report["compressed_member_bytes"], 12)
        disguised = f"{bundle.FROZEN_RUNTIME}/{bundle.PREBUILT_PAYLOAD}/unused.bin"
        with self.assertRaisesRegex(ValueError, "unexpected payload file"):
            bundle._player_overhead({disguised: payload})

    def test_source_builder_archive_is_not_subject_to_player_overhead_budget(self):
        folder = self.directory / "source-builder"
        unused = folder / "development-source.bin"
        unused.parent.mkdir()
        with unused.open("wb") as stream:
            stream.truncate(bundle.PLAYER_OVERHEAD_LIMIT + 1)
        result = bundle.create_archive(folder, self.directory / "source-builder.zip", COMMIT, "windows-x64")
        self.assertEqual(result["status"], "passed")
        self.assertGreater(result["uncompressed_bytes"], bundle.PLAYER_OVERHEAD_LIMIT)
        self.assertNotIn("player_overhead", result)

    def test_prepared_player_installs_repeats_and_undoes_without_site_packages_or_source_checkout(self):
        runtime = self._prepare(self._prebuilt_payload(), real_modules=True)
        report = self.directory / "player-self-test.json"
        result = subprocess.run([sys.executable, "-I", "-S", "-B", str(runtime / "installer/main.py"),
                                 "--self-test", "--report", str(report)], cwd=self.directory,
                                text=True, capture_output=True, timeout=60)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        check = json.loads(report.read_text())
        self.assertTrue(check["prebuilt_transaction_verified"])
        self.assertTrue(check["repeat_install_and_rollback"])
        self.assertFalse(check["planar_geometry_runtime_checked"])
        self.assertEqual(check["runtime_verification"]["prebuilt_payload_manifest_sha256"],
                         bundle._hash(runtime / bundle.PREBUILT_PAYLOAD / "manifest.json"))

    def test_path_budget_counts_windows_utf16_units_and_rejects_overflow(self):
        # A non-BMP character occupies two Windows UTF-16 units.
        self.assertEqual(bundle._windows_characters("a\U0001f600"), 3)
        remaining = bundle.WINDOWS_PATH_CHARACTERS - bundle.EXTRACTION_DESTINATION_CHARACTERS - 1
        self.assertEqual(bundle._path_budget(["x" * remaining])["longest_extracted_characters"], 259)
        with self.assertRaisesRegex(ValueError, "extraction-path budget exceeded"):
            bundle._path_budget(["x" * (remaining + 1)])
        current_names = ["SCP Installer/" + bundle.FROZEN_RUNTIME + "/" + bundle.PREBUILT_PAYLOAD
                         + f"/{FOLDER}/20_Pieces/SCP_" + path.parent.name + ".dat"
                         for path in (ROOT / "domains").glob("*/00_pieces/*/piece.*")]
        self.assertLessEqual(bundle._path_budget(current_names)["longest_extracted_characters"], 259)

    def test_player_archive_enforces_path_budget_before_extraction(self):
        folder = self.directory / "frozen"
        self._prepare(self._prebuilt_payload(), folder / bundle.FROZEN_RUNTIME)
        self._write(folder, "_internal/" + "a" * 180 + ".dll")
        with self.assertRaisesRegex(ValueError, "extraction-path budget exceeded"):
            bundle.create_archive(folder, self.directory / "too-long.zip", COMMIT, "windows-x64")

    def test_archive_rejects_windows_reserved_names_and_trailing_dots(self):
        for name in ("app/CON.txt", "app/LPT1", "app/folder./file.txt", "app/data:stream", "app/name?/file"):
            with self.subTest(name=name), self.assertRaisesRegex(ValueError, "Unsafe distribution path"):
                bundle._relative(name)

    def test_downloads_extraction_checks_exact_files_and_relaunches_both_executable_actions(self):
        folder = self.directory / bundle.APP_NAME
        self._prepare(self._prebuilt_payload(), folder / bundle.FROZEN_RUNTIME)
        self._write(folder, bundle.APP_NAME + ".exe", b"MZ fixture")
        archive = self.directory / "player.zip"
        verification = bundle.create_archive(folder, archive, COMMIT, "windows-x64")
        actions = []

        def windows_command(command, **options):
            if command[0] == "powershell.exe":
                destination = Path(options["env"]["SCP_CHECK_DESTINATION"])
                self.assertEqual(bundle._windows_characters(str(destination)), 100)
                self.assertIn("Expand-Archive", command[-1])
                self.assertEqual(destination.parents[1].name, "Downloads")
                with zipfile.ZipFile(options["env"]["SCP_CHECK_ARCHIVE"]) as saved:
                    saved.extractall(destination)
            else:
                self.assertIn("Downloads", Path(command[0]).parts)
                self.assertTrue(Path(command[0]).is_file())
                actions.append(command[1])
                check = {"status": "passed", "utf8_mode": 1, "source_commit": COMMIT,
                         "prebuilt_transaction_verified": True, "repeat_install_and_rollback": True,
                         "runtime_verification": {"prebuilt_payload_manifest_sha256":
                                                  verification["prebuilt_payload_manifest_sha256"]}}
                Path(command[3]).write_text(json.dumps(check))

        with patch.object(bundle, "host_platform", return_value="windows-x64"), \
                patch.object(Path, "home", return_value=self._downloads_home()), \
                patch.object(bundle.subprocess, "run", side_effect=windows_command):
            report = bundle.check_windows_extraction(archive, self.directory)
        bundle._check_extraction_report(report, verification)
        self.assertEqual(actions, ["--self-test", "--gui-smoke-test"])
        for key, value in (("zip_sha256", "a" * 64), ("source_commit", "b" * 40),
                           ("destination_characters", 99), ("longest_extracted_characters", 260)):
            with self.subTest(key=key), self.assertRaisesRegex(ValueError, "exact player ZIP"):
                bundle._check_extraction_report({**report, key: value}, verification)
        report["executable_checks"]["self-test"]["repeat_install_and_rollback"] = False
        with self.assertRaisesRegex(ValueError, "repeat installation"):
            bundle._check_extraction_report(report, verification)

    def test_downloads_extraction_rejects_corrupted_files_before_launching(self):
        folder = self.directory / bundle.APP_NAME
        self._prepare(self._prebuilt_payload(), folder / bundle.FROZEN_RUNTIME)
        self._write(folder, bundle.APP_NAME + ".exe", b"MZ fixture")
        archive = self.directory / "player.zip"
        bundle.create_archive(folder, archive, COMMIT, "windows-x64")

        damaged = [bundle.APP_NAME + ".exe"]

        def corrupt_extraction(command, **options):
            self.assertEqual(command[0], "powershell.exe")
            destination = Path(options["env"]["SCP_CHECK_DESTINATION"])
            with zipfile.ZipFile(archive) as saved:
                saved.extractall(destination)
            (destination / bundle.APP_NAME / damaged[0]).write_bytes(b"corrupted")

        with patch.object(bundle, "host_platform", return_value="windows-x64"), \
                patch.object(Path, "home", return_value=self._downloads_home()), \
                patch.object(bundle.subprocess, "run", side_effect=corrupt_extraction):
            with self.assertRaisesRegex(ValueError, "extraction changed an installer file"):
                bundle.check_windows_extraction(archive, self.directory)
            damaged[0] = "SHA256SUMS"
            with self.assertRaisesRegex(ValueError, "extraction changed the installer checksums"):
                bundle.check_windows_extraction(archive, self.directory)

    def test_freezer_collects_dynamic_highway_provider_from_runtime_source(self):
        class CommandCaptured(Exception):
            pass

        commands = []

        def run(command, **kwargs):
            if command[:2] == ["git", "rev-parse"]:
                return SimpleNamespace(stdout=COMMIT + "\n")
            if command[:2] == ["git", "diff"]:
                return SimpleNamespace(returncode=0)
            if command[:2] == ["git", "ls-files"]:
                return SimpleNamespace(stdout=b"")
            if command[:2] == ["git", "show"]:
                return SimpleNamespace(stdout="1700000000\n")
            if command[:4] == [sys.executable, "-B", "-m", "PyInstaller"]:
                commands.append((command, kwargs))
                raise CommandCaptured
            self.fail("Unexpected command before freezing: " + repr(command))

        tcl = SimpleNamespace(Tcl=lambda: SimpleNamespace(eval=lambda script: "8.6"))
        output = self.directory / "output"
        with patch.object(bundle, "host_platform", return_value="windows-x64"), \
                patch.object(bundle, "prepare_runtime"), \
                patch.object(bundle.subprocess, "run", side_effect=run), \
                patch.dict(sys.modules, {"tkinter": tcl}):
            with self.assertRaises(CommandCaptured):
                bundle.build_bundle(self.directory, output, COMMIT, "windows-x64")
        self.assertEqual(len(commands), 1)
        command, kwargs = commands[0]
        collected = {command[index + 1] for index, token in enumerate(command)
                     if token == "--collect-submodules"}
        self.assertEqual(collected, {"scp", "scp_hsr", "scp_highway", "scp_installer"})
        runtime = output / "work/runtime/custom-pieces"
        search_paths = {command[index + 1] for index, token in enumerate(command)
                        if token == "--paths"}
        self.assertIn(str(runtime / "domains/highway/implementation"), search_paths)
        self.assertEqual(kwargs["cwd"], runtime)


if __name__ == "__main__":
    unittest.main()
