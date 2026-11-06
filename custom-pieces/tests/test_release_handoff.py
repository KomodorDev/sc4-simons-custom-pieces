"""Check hosted release policy and fail-closed orchestration without credentials."""
from pathlib import Path
import tempfile
import os
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "installer"))
import release_handoff as handoff


MAIN = "1" * 40
DEV = "2" * 40
TREE = "3" * 40
REPO = "owner/repository"
EVENT = {"GITHUB_REPOSITORY": REPO, "GITHUB_SHA": MAIN}


class ReleaseHandoffTests(unittest.TestCase):
    def test_review_run_requires_both_actual_job_steps(self):
        run = {"event": "workflow_dispatch", "head_branch": "dev", "conclusion": "success",
               "path": ".github/workflows/installer-release.yml", "head_repository": {"full_name": REPO},
               "run_attempt": 2, "head_sha": DEV}
        job = {"name": handoff.REVIEW_JOB, "conclusion": "success",
               "steps": [{"name": name, "conclusion": "success"} for name in handoff.REVIEW_STEPS]}
        with patch.object(handoff, "_gh", side_effect=[run, [{"jobs": [job]}]]), \
                patch.object(handoff.subprocess, "run") as diff:
            diff.return_value.returncode = 0
            handoff._require_private_review(ROOT, REPO, "123", MAIN)
            self.assertEqual(diff.call_args.args[0][3:5], [DEV, MAIN])
        with patch.object(handoff, "_gh", side_effect=[run, [{"jobs": [job]}]]), \
                patch.object(handoff.subprocess, "run") as diff:
            diff.return_value.returncode = 1
            with self.assertRaisesRegex(ValueError, "release tooling differs"):
                handoff._require_private_review(ROOT, REPO, "123", MAIN)
        job["steps"][0]["conclusion"] = "skipped"
        with patch.object(handoff, "_gh", side_effect=[run, [{"jobs": [job]}]]):
            with self.assertRaisesRegex(ValueError, "actual Dropbox handoff"):
                handoff._require_private_review(ROOT, REPO, "123", MAIN)

    def test_main_merge_can_use_different_commit_with_same_tree(self):
        pr = {"merged_at": "2026-11-06", "merge_commit_sha": MAIN,
              "base": {"ref": "main", "repo": {"full_name": REPO}},
              "head": {"ref": "dev", "sha": DEV, "repo": {"full_name": REPO}}}
        env = {**EVENT, "GITHUB_EVENT_NAME": "push", "GITHUB_REF": "refs/heads/main",
               "SCP_PREBUILT_PUBLICATION": "enabled", "SCP_PREBUILT_REVIEW_RUN_ID": "123"}
        with patch.dict(os.environ, env, clear=True), patch.object(handoff, "_require_private_review"), \
                patch.object(handoff, "_gh", return_value=[[pr]]), \
                patch.object(handoff, "source_identity", return_value=(DEV, TREE)) as identity:
            self.assertEqual(handoff.approved_release_head(ROOT, MAIN, TREE), DEV)
            identity.assert_called_once_with(ROOT, DEV)
            identity.return_value = (DEV, "4" * 40)
            with self.assertRaisesRegex(ValueError, f"release dev {DEV} has tree"):
                handoff.approved_release_head(ROOT, MAIN, TREE)

    def test_disabled_publication_does_not_request_credentials_or_review(self):
        env = {**EVENT, "GITHUB_EVENT_NAME": "push", "GITHUB_REF": "refs/heads/main"}
        with patch.dict(os.environ, env, clear=True), patch.object(handoff, "_gh") as api:
            with self.assertRaisesRegex(ValueError, "publication is disabled"):
                handoff.approved_release_head(ROOT, MAIN, TREE)
            api.assert_not_called()

    def test_missing_dropbox_zip_identifies_revision_and_stops_before_extraction(self):
        env = {**EVENT, "GITHUB_EVENT_NAME": "workflow_dispatch", "GITHUB_REF": "refs/heads/dev"}
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary) / "handoff"
            with patch.dict(os.environ, env, clear=True), \
                    patch.object(handoff, "source_identity", return_value=(MAIN, TREE)), \
                    patch.object(handoff, "download_archive", side_effect=handoff.DropboxNotFound("not found")), \
                    patch.object(handoff, "extract_release_payload") as extract:
                with self.assertRaisesRegex(ValueError, f"Prepare that exact dev revision.*") as error:
                    handoff.receive(ROOT, workspace, mode="review")
                self.assertIn(MAIN, str(error.exception))
                extract.assert_not_called()
                self.assertFalse((workspace / "payload").exists())
                self.assertFalse((workspace / "release-record.json").exists())

    def test_mismatched_zip_stops_before_writing_release_record(self):
        env = {**EVENT, "GITHUB_EVENT_NAME": "workflow_dispatch", "GITHUB_REF": "refs/heads/dev"}
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary) / "handoff"
            with patch.dict(os.environ, env, clear=True), \
                    patch.object(handoff, "source_identity", return_value=(MAIN, TREE)), \
                    patch.object(handoff, "download_archive"), \
                    patch.object(handoff, "extract_release_payload", side_effect=ValueError("Wrong tree")), \
                    patch.object(handoff, "_negative_review") as next_stage:
                with self.assertRaisesRegex(ValueError, "Wrong tree"):
                    handoff.receive(ROOT, workspace, mode="review")
                next_stage.assert_not_called()
                self.assertFalse((workspace / "release-record.json").exists())


if __name__ == "__main__":
    unittest.main()
