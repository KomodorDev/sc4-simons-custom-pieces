"""Installer distributions have exact, public-only source and archive closure."""
from __future__ import annotations

from copy import deepcopy
import json
import os
from pathlib import Path
import stat
import sys
import tempfile
import unittest
from unittest.mock import patch
import warnings
import zipfile


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "installer"))
import build_bundle as bundle


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

    def _source(self):
        root = self.directory / "source"
        project = {"domains": {"fixture": {"registry": "domains/fixture/domain.jsonc", "path": "domains/fixture"}}}
        registry = {"pieces": ["00_pieces/example/piece.json"], "assemblies": []}
        for relative in ("pyproject.toml", "installer/main.py", "installer/build_bundle.py",
                         "installer/scp_installer/service.py", "config/installer.jsonc",
                         "framework/scp/check_bootstrap.py", "framework/scp/__init__.py", "framework/scp/jsonc.py",
                         "domains/fixture/00_pieces/example/piece.json", "domains/fixture/README.md"):
            self._write(root, relative)
        self._write(root, "project.jsonc", self._commented(project, "Installer fixture project"))
        self._write(root, "domains/fixture/domain.jsonc", self._commented(registry, "Installer fixture domain"))
        return root

    def _commented(self, value, title):
        return ("// title: " + json.dumps(title) + '\n// summary: "Portable synthetic installer input."\n'
                + json.dumps(value, indent=2) + "\n").encode()

    def _prepare(self):
        source = self._source()
        runtime = self.directory / "runtime"
        with patch.object(bundle, "_source_paths", return_value=list(source.rglob("*"))) as paths:
            paths.return_value = [path for path in paths.return_value if path.is_file()]
            bundle.prepare_runtime(source, runtime, COMMIT, "windows-x64")
        return runtime

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
                     "domains/fixture/00_pieces/inventory.jsonc", "domains/fixture/01_assemblies/inventory.jsonc",
                     "domains/fixture/00_pieces/example/geometry.json",
                     "domains/fixture/00_pieces/example/evidence/design-history/record.json"):
            with self.subTest(name=name):
                self.assertTrue(allowed(name))
        for name in ("local/settings.json", "local/settings.jsonc", "dist/build/manifest.json", "tests/test_build.py",
                     "project.json", "schemas/connector-groups.schema.json", "config/profiles/fixture.json",
                     "config/local.example.jsonc", "domains/fixture/00_pieces/unknown/piece.json",
                     "domains/fixture/00_pieces/example/native.dat", "framework/scp/__pycache__/cache.pyc",
                     "installer/private/settings.json", "domains/fixture/local/secret.json"):
            with self.subTest(name=name):
                self.assertFalse(allowed(name))

    def test_commented_sources_survive_runtime_and_archive_while_reports_stay_strict_json(self):
        source = self._source()
        included = ("project.jsonc", "domains/fixture/domain.jsonc", "config/installer.jsonc",
                    "config/allocations.jsonc", "config/release.jsonc", "config/profiles/fixture.jsonc",
                    "schemas/connector-groups.schema.jsonc", "docs/templates/assembly-starter.jsonc",
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

    def test_archive_hashes_closure_and_executable_mode_are_verified(self):
        folder, archive = self._archive()
        result = bundle.verify_archive(archive)
        self.assertEqual(result["status"], "passed")
        self.assertEqual(result["source_commit"], COMMIT)
        self.assertEqual(result["members_verified"], 4)
        with zipfile.ZipFile(archive) as saved:
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


if __name__ == "__main__":
    unittest.main()
