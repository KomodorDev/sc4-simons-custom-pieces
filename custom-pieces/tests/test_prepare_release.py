"""Test the Mac release command without a real render or Dropbox transfer."""
from contextlib import ExitStack, redirect_stderr, redirect_stdout
import hashlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import Mock, call, patch
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "installer"))
import prepare_release as command


COMMIT = "a" * 40
TREE = "b" * 40
ARCHIVE = f"SCP-Prebuilt-Payload-{TREE}.zip"
CONTENTS = b"verified test archive"
DIGEST = hashlib.sha256(CONTENTS).hexdigest()


class PrepareReleaseTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        base = Path(temporary.name).resolve()
        self.repo = base / "repo"
        self.game = base / "game"
        self.player_data = base / "player data"
        self.dropbox = base / "Dropbox" / "Apps" / "SCP"
        self.staging = base / "staging"
        for directory in (self.repo, self.game, self.player_data, self.dropbox, self.staging):
            directory.mkdir(parents=True)
        self.credentials = object()
        self.options = {
            "game_folder": self.game, "player_data": self.player_data,
            "dropbox_folder": self.dropbox, "staging_folder": self.staging,
            "credentials_path": base / "credentials.json", "sync_timeout": 61,
        }
        self.proof = {"filename": ARCHIVE, "sha256": DIGEST, "bytes": len(CONTENTS),
                      "dropbox_content_hash": "c" * 64, "dropbox_path": f"/{ARCHIVE}"}

    def mocks(self, stack):
        probes = Mock()
        probes.fetch = stack.enter_context(patch.object(command, "_fetch_dev"))
        probes.source = stack.enter_context(patch.object(command, "_clean_dev_source", return_value=(COMMIT, TREE)))
        probes.validate = stack.enter_context(patch.object(command, "validate_dropbox_directory", return_value=self.dropbox))
        probes.credentials = stack.enter_context(patch.object(command, "load_local_credentials", return_value=self.credentials))
        probes.client = stack.enter_context(patch.object(command, "DropboxClient"))
        probes.build = stack.enter_context(patch.object(command.subprocess, "run"))
        stack.enter_context(patch.object(command, "bootstrap"))
        probes.write = stack.enter_context(patch.object(command, "write_release_payload", side_effect=self.write))
        probes.extract = stack.enter_context(patch.object(command, "extract_release_payload",
                                                         return_value={"prebuild_commit": COMMIT, "archive_sha256": DIGEST}))
        probes.folder = stack.enter_context(patch.object(command, "_prove_dropbox_folder"))
        probes.sync = stack.enter_context(patch.object(command, "sync_archive", return_value=self.proof))
        stack.enter_context(redirect_stderr(io.StringIO()))
        return probes

    def write(self, payload, archive, *, source_commit, source_tree):
        self.assertEqual((source_commit, source_tree), (COMMIT, TREE))
        self.assertEqual(payload, archive.parent / "payload")
        self.assertEqual(archive.name, ARCHIVE)
        archive.write_bytes(CONTENTS)
        return {"archive_sha256": DIGEST}

    def test_fresh_release_builds_private_archive_then_waits_for_exact_remote_proof(self):
        with ExitStack() as stack:
            probes = self.mocks(stack)

            def build(*args, **kwargs):
                probes.client.return_value.refresh_access_token.assert_called_once()
                probes.client.return_value.get_metadata.assert_called_once_with(f"/{ARCHIVE}")

            probes.build.side_effect = build
            report = command.prepare_release(self.repo, **self.options)
        path = Path(report["archive"])
        self.assertEqual(report, {"status": "payload-ready", "source_commit": COMMIT, "source_tree": TREE,
                                  "archive": str(path), **self.proof})
        self.assertEqual(path.read_bytes(), CONTENTS)
        self.assertTrue(path.is_relative_to(self.staging))
        self.assertEqual(probes.fetch.call_args_list, [call(self.repo)] * 3)
        self.assertEqual(probes.source.call_count, 4)
        probes.client.assert_called_once_with(self.credentials)
        probes.client.return_value.get_metadata.assert_called_once_with(f"/{ARCHIVE}")
        probes.build.assert_called_once()
        self.assertEqual(probes.build.call_args.args[0], [
            sys.executable, "-B", str(self.repo / "custom-pieces/installer/prepare_payload.py"),
            "--game-folder", str(self.game), "--player-data", str(self.player_data),
            "--work-dir", str(path.parent / "work"), "--output", str(path.parent / "payload"),
        ])
        probes.sync.assert_called_once_with(path, self.dropbox, timeout=61, credentials=self.credentials,
                                            sha256_digest=DIGEST, size=len(CONTENTS))
        probes.folder.assert_called_once_with(self.staging, self.dropbox, self.credentials, 61)
        probes.extract.assert_not_called()

    def test_fetched_dev_tree_must_still_match_before_any_transfer(self):
        with ExitStack() as stack:
            probes = self.mocks(stack)
            probes.source.side_effect = [(COMMIT, TREE), (COMMIT, TREE),
                                         ValueError("fetched origin/dev tree changed")]
            with self.assertRaisesRegex(ValueError, "origin/dev"):
                command.prepare_release(self.repo, **self.options)
        probes.write.assert_called_once()
        probes.sync.assert_not_called()
        self.assertEqual(len(list(self.staging.glob(f"*/{ARCHIVE}"))), 1)

    def test_dev_change_during_sync_prevents_readiness(self):
        with ExitStack() as stack:
            probes = self.mocks(stack)
            probes.source.side_effect = [(COMMIT, TREE)] * 3 + [("d" * 40, "e" * 40)]
            with self.assertRaisesRegex(ValueError, "while Dropbox was syncing"):
                command.prepare_release(self.repo, **self.options)
        probes.sync.assert_called_once()

    def test_unproven_dropbox_folder_stops_before_copying_the_release(self):
        with ExitStack() as stack:
            probes = self.mocks(stack)
            probes.folder.side_effect = ValueError("Dropbox did not confirm the marker")
            with self.assertRaisesRegex(ValueError, "did not confirm the marker"):
                command.prepare_release(self.repo, **self.options)
        probes.sync.assert_not_called()

    def test_dropbox_folder_probe_uses_no_game_files_and_removes_marker_on_failure(self):
        def failed_sync(probe, folder, *, timeout, credentials):
            self.assertEqual((folder, timeout, credentials), (self.dropbox, 61, self.credentials))
            with zipfile.ZipFile(probe) as archive:
                self.assertEqual(archive.namelist(), ["probe.txt"])
                self.assertIn(archive.read("probe.txt").decode("ascii"), probe.name)
            (folder / probe.name).write_bytes(probe.read_bytes())
            raise ValueError("Dropbox did not confirm the marker")

        with patch.object(command, "sync_archive", side_effect=failed_sync):
            with self.assertRaisesRegex(ValueError, "did not confirm the marker"):
                command._prove_dropbox_folder(self.staging, self.dropbox, self.credentials, 61)
        self.assertEqual(list(self.dropbox.iterdir()), [])
        self.assertEqual(list(self.staging.iterdir()), [])

    def test_remote_authentication_failure_stops_before_rendering(self):
        with ExitStack() as stack:
            probes = self.mocks(stack)
            probes.client.return_value.refresh_access_token.side_effect = ValueError("bad credentials")
            with self.assertRaisesRegex(ValueError, "bad credentials"):
                command.prepare_release(self.repo, **self.options)
        probes.build.assert_not_called()
        probes.write.assert_not_called()
        probes.sync.assert_not_called()

    def test_resume_verifies_exact_staged_archive_without_rebuilding(self):
        archive = self.staging / ARCHIVE
        archive.write_bytes(CONTENTS)
        with ExitStack() as stack:
            probes = self.mocks(stack)
            result = command.prepare_release(self.repo, **{**self.options, "game_folder": None, "player_data": None},
                                             resume_archive=archive)
        self.assertEqual(result["status"], "payload-ready")
        probes.build.assert_not_called()
        probes.write.assert_not_called()
        self.assertEqual(probes.extract.call_args.args[0], archive)
        self.assertEqual(probes.extract.call_args.kwargs, {
            "source_commit": COMMIT, "source_tree": TREE, "repo": self.repo,
        })
        probes.sync.assert_called_once()

    def test_resume_rejects_zip_from_different_commit_before_uploading(self):
        archive = self.staging / ARCHIVE
        archive.write_bytes(CONTENTS)
        with ExitStack() as stack:
            probes = self.mocks(stack)
            probes.extract.return_value = {"prebuild_commit": "f" * 40, "archive_sha256": DIGEST}
            with self.assertRaisesRegex(ValueError, "exact source commit"):
                command.prepare_release(self.repo, **self.options, resume_archive=archive)
        probes.sync.assert_not_called()
        probes.build.assert_not_called()

    def test_cli_writes_no_ready_report_when_dropbox_times_out(self):
        arguments = ["--game-folder", str(self.game), "--player-data", str(self.player_data),
                     "--dropbox-folder", str(self.dropbox), "--staging-folder", str(self.staging)]
        with ExitStack() as stack:
            probes = self.mocks(stack)
            probes.sync.side_effect = TimeoutError("Dropbox remote proof unavailable")
            output = stack.enter_context(redirect_stdout(io.StringIO()))
            with self.assertRaisesRegex(TimeoutError, "proof unavailable"):
                command.main(arguments)
        self.assertEqual(output.getvalue(), "")
        self.assertEqual(len(list(self.staging.glob(f"*/{ARCHIVE}"))), 1)

    def test_staging_rejects_dropbox_paths_even_via_parent_navigation(self):
        with self.assertRaisesRegex(ValueError, "outside the Dropbox"):
            command._staging_root(self.repo, self.staging / ".." / "Dropbox" / "private", self.dropbox.parent.parent)

    def test_git_guard_accepts_same_tree_under_distinct_commits(self):
        with patch.object(command.subprocess, "check_output", return_value=""), \
                patch.object(command, "source_identity", side_effect=[(COMMIT, TREE), ("f" * 40, TREE)]), \
                patch.object(command.subprocess, "run", return_value=Mock(returncode=0)):
            self.assertEqual(command._clean_dev_source(self.repo), (COMMIT, TREE))

    def test_git_guard_rejects_local_only_commit_even_if_its_tree_matches(self):
        with patch.object(command.subprocess, "check_output", return_value=""), \
                patch.object(command, "source_identity", side_effect=[(COMMIT, TREE), ("f" * 40, TREE)]), \
                patch.object(command.subprocess, "run", return_value=Mock(returncode=1)):
            with self.assertRaisesRegex(ValueError, "local-only prebuild commit"):
                command._clean_dev_source(self.repo)

    def test_git_guard_rejects_dirty_checkout_and_wrong_tree(self):
        with patch.object(command.subprocess, "check_output", return_value=" M file\n"):
            with self.assertRaisesRegex(ValueError, "clean, committed"):
                command._clean_dev_source(self.repo)
        with patch.object(command.subprocess, "check_output", return_value=""), \
                patch.object(command, "source_identity", side_effect=[(COMMIT, TREE), (COMMIT, "f" * 40)]):
            with self.assertRaisesRegex(ValueError, "origin/dev tree"):
                command._clean_dev_source(self.repo)


if __name__ == "__main__":
    unittest.main()
