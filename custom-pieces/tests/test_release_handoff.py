"""Check hosted release policy and fail-closed orchestration without credentials."""
import json
from pathlib import Path
import tempfile
import os
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "installer"))
import release_handoff as handoff
from scp.content import new_manual_record, record_user_result


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
            self.assertIn("custom-pieces/framework/scp/player_manifest.py", diff.call_args.args[0])
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


class PrebuiltReleaseEvidenceTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="scp-prebuilt-release-test-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.gates = {
            key: {"enabled": True, "status": "passed", "evidence": "fixture evidence"}
            for key in ("public_name_checked", "ids_allocated", "nam_derivatives_permission",
                        "supported_platform_tests", "simtropolis_description_and_game_images")
        }
        self.gates["prebuilt_installer"] = {"require_build_game_evidence": False}
        self.piece = {"id": "example", "domain": "fixture", "status": "tested",
                      "game_tests": {"placement": "passed"},
                      "provenance": {"redistribution": "permission-recorded"}}
        folder = "zzz_Simons_Custom_Pieces"
        asset = f"{folder}/20_Pieces/SCP_example.dat"
        self.manifest = {
            "plugin_folder": folder,
            "pieces": [{"id": "example"}],
            "files": [{"path": asset, "sha256": "a" * 64},
                      {"path": f"{folder}/00_SCP_Controller_NAM50.dat", "sha256": "b" * 64},
                      {"path": f"{folder}/10_SCP_Menu.dat", "sha256": "c" * 64}],
            "profile": {"donors": [{"filename": "NetworkAddonMod_Controller.dat", "sha256": "d" * 64}]},
        }
        domain = "domains/fixture"
        self.manual_path = f"{domain}/00_pieces/example/checks/manual-tests.json"
        self._write_json("project.jsonc", {})
        self.pending_manual_record = new_manual_record(
            "example", "piece", {}, {"model:example:fixture": "a" * 64},
            manual_check_orientations=[{"rotation_ccw_degrees": 0}])
        case, = (case for case in self.pending_manual_record["cases"] if case["kind"] == "in_game_placement")
        self.pending_manual_record["cases"] = [case]
        passing_record = record_user_result(
            self.pending_manual_record, case["id"], "passed", explicit_user_confirmation=True,
            reviewer="Fixture Tester", confirmed_at="2026-11-06T00:00:00Z",
            evidence=["Synthetic placement observation"],
            environment={"platform": "fixture", "game_version": "fixture", "nam_profile": "fixture"})
        self._write_json(self.manual_path, passing_record)
        catalogue = {"pieces": [self.piece], "domains": {"fixture": {"path": domain}}}
        loader = patch("scp.catalog.load_catalog", return_value=catalogue)
        loader.start()
        self.addCleanup(loader.stop)

    def _write_json(self, relative, value):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value) + "\n", encoding="utf-8")

    def _check_release(self):
        self._write_json("config/release.jsonc", self.gates)
        handoff.require_release_evidence(self.root, self.manifest)

    def _assert_blocked(self, *reasons):
        with self.assertRaisesRegex(ValueError, "Public prebuilt release requirements are unmet") as error:
            self._check_release()
        for reason in reasons:
            self.assertIn(reason, str(error.exception))

    def test_permission_switch_skips_shared_and_piece_permission_until_reenabled(self):
        gate = self.gates["nam_derivatives_permission"]
        gate.update(status="pending", evidence=None)
        self.piece["provenance"]["redistribution"] = "permission-pending"

        self._assert_blocked("nam_derivatives_permission", "example: redistribution evidence")
        gate["enabled"] = False
        self._check_release()
        gate["enabled"] = True
        self._assert_blocked("nam_derivatives_permission", "example: redistribution evidence")

    def test_platform_switch_skips_all_piece_game_checks_until_reenabled(self):
        gate = self.gates["supported_platform_tests"]
        gate.update(status="pending", evidence=None)
        self.piece.update(status="experimental", game_tests={"placement": "unverified"})
        self._write_json(self.manual_path, self.pending_manual_record)
        self.gates["prebuilt_installer"]["require_build_game_evidence"] = True
        blockers = ("supported_platform_tests", "example: in-game test matrix",
                    "example: in_game_placement: 1 current manual cases need confirmation",
                    "example: game_evidence is not recorded")

        self._assert_blocked(*blockers)
        gate["enabled"] = False
        self._check_release()
        gate["enabled"] = True
        self._assert_blocked(*blockers)

    def test_piece_permission_and_platform_switches_are_independent(self):
        self.piece.update(status="experimental", provenance={"redistribution": "permission-pending"})
        permission = self.gates["nam_derivatives_permission"]
        platform = self.gates["supported_platform_tests"]

        permission["enabled"] = False
        self._assert_blocked("example: in-game test matrix")
        permission["enabled"] = True
        platform["enabled"] = False
        self._assert_blocked("example: redistribution evidence")
        permission["enabled"] = False
        self._check_release()

    def test_build_specific_game_evidence_switch_applies_when_platform_checks_enabled(self):
        self._check_release()
        for settings in ({}, {"require_build_game_evidence": True}):
            with self.subTest(settings=settings):
                self.gates["prebuilt_installer"] = settings
                self._assert_blocked("example: game_evidence is not recorded")
        self.gates["prebuilt_installer"] = {"require_build_game_evidence": False}
        self._write_json(self.manual_path, self.pending_manual_record)
        self._assert_blocked("example: in_game_placement: 1 current manual cases need confirmation")

    def test_enabled_build_specific_evidence_must_match_the_prebuilt_package(self):
        self.gates["prebuilt_installer"]["require_build_game_evidence"] = True
        self.piece["game_evidence"] = "evidence/example.json"
        screenshot = self.root / "evidence/placement.png"
        screenshot.parent.mkdir()
        screenshot.write_bytes(b"synthetic screenshot")
        self._write_json(self.piece["game_evidence"], {
            "piece_id": "example",
            "asset_sha256": self.manifest["files"][0]["sha256"],
            "package_fingerprints": {item["path"]: item["sha256"] for item in self.manifest["files"]},
            "donor_fingerprints": {item["filename"]: item["sha256"]
                                   for item in self.manifest["profile"]["donors"]},
            "case_results": self.piece["game_tests"],
            "tester": "Fixture Tester",
            "date": "2026-11-06",
            "screenshots": ["evidence/placement.png"],
        })
        self._check_release()
        self.manifest["files"][1]["sha256"] = "e" * 64
        self._assert_blocked("game evidence package fingerprints differ from this build")

    def test_prebuilt_release_rejects_nonboolean_build_specific_game_evidence_setting(self):
        self.gates["prebuilt_installer"]["require_build_game_evidence"] = 0
        with self.assertRaisesRegex(ValueError, "require_build_game_evidence must be true or false"):
            self._check_release()

    def test_disabling_piece_evidence_checks_keeps_catalogue_and_manifest_validation(self):
        self.gates["nam_derivatives_permission"]["enabled"] = False
        self.gates["supported_platform_tests"]["enabled"] = False

        self.manifest["pieces"] = []
        with self.assertRaisesRegex(ValueError, "does not contain the current complete catalogue"):
            self._check_release()
        self.manifest["pieces"] = [{"id": "example"}]
        self.manifest["files"][0]["sha256"] = "not a fingerprint"
        self._assert_blocked("build evidence metadata: invalid SHA-256 fingerprint")

    def test_installer_applies_only_configured_evidence_checks_with_an_open_design_review(self):
        for gate in self.gates.values():
            if "enabled" in gate:
                gate.update(enabled=False, status="pending", evidence=None)
        self.piece.update(status="experimental", game_tests={"placement": "unverified"},
                          provenance={"redistribution": "permission-pending"})
        self.piece["design_review"] = {
            "status": "needs-redesign",
            "summary": "The approach has an unnecessary detour.",
            "reasons": ["The approach has not been accepted."],
        }
        self._check_release()
        self.gates["ids_allocated"]["enabled"] = True
        self._assert_blocked("ids_allocated")


if __name__ == "__main__":
    unittest.main()
