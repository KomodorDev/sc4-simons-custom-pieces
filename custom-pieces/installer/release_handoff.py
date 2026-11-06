"""Check the protected GitHub release and receive its private Dropbox payload."""
from __future__ import annotations

import argparse
from hashlib import sha1
import json
import os
from pathlib import Path
import re
import subprocess

from release_dropbox import DropboxNotFound, download_archive
from release_payload import archive_name, extract_release_payload, source_identity


REVIEW_JOB = "Private hosted prebuilt review"
REVIEW_STEPS = {"Verify Dropbox handoff and rejected inputs", "Build and test the private Windows installer"}
REVIEWED_PATHS = (
    ".github/workflows/installer-release.yml",
    "custom-pieces/installer",
    "custom-pieces/framework/scp/prebuilt.py",
    "custom-pieces/framework/scp/install.py",
    "custom-pieces/framework/scp/release.py",
    "custom-pieces/framework/scp/catalog.py",
    "custom-pieces/requirements-installer.txt",
)


def _gh(endpoint, *, paginated=False):
    flags = ["--paginate", "--slurp"] if paginated else []
    result = subprocess.run(["gh", "api", *flags, endpoint], capture_output=True, check=True, text=True)
    return json.loads(result.stdout)


def _repository():
    repository = os.environ.get("GITHUB_REPOSITORY", "")
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
        raise ValueError("This operation requires the canonical GitHub repository context.")
    return repository


def _require_private_review(repo, repository, run_id, commit):
    if not re.fullmatch(r"[1-9][0-9]*", run_id):
        raise ValueError("Set SCP_PREBUILT_REVIEW_RUN_ID to the successful private hosted review run ID.")
    endpoint = f"repos/{repository}/actions/runs/{run_id}"
    run = _gh(endpoint)
    if (run.get("event") != "workflow_dispatch" or run.get("head_branch") != "dev"
            or run.get("conclusion") != "success" or run.get("path") != ".github/workflows/installer-release.yml"
            or (run.get("head_repository") or {}).get("full_name") != repository):
        raise ValueError("The selected review run did not succeed on this repository's dev branch.")
    attempt = run.get("run_attempt")
    if type(attempt) is not int or attempt < 1:
        raise ValueError("The review run has no valid attempt number.")
    pages = _gh(f"{endpoint}/attempts/{attempt}/jobs", paginated=True)
    jobs = [job for page in pages for job in page["jobs"] if job.get("name") == REVIEW_JOB]
    if len(jobs) != 1 or jobs[0].get("conclusion") != "success" or not REVIEW_STEPS <= {
        step.get("name") for step in jobs[0].get("steps", []) if step.get("conclusion") == "success"
    }:
        raise ValueError("The selected run did not pass the actual Dropbox handoff and Windows installer review.")
    reviewed = run.get("head_sha", "")
    if not isinstance(reviewed, str) or not re.fullmatch(r"[0-9a-f]{40}", reviewed) or subprocess.run(
            ["git", "diff", "--quiet", reviewed, commit, "--", *REVIEWED_PATHS],
            cwd=repo, capture_output=True).returncode != 0:
        raise ValueError("The release tooling differs from the selected private review. Review the current dev tooling first.")


def approved_release_head(repo, commit, tree):
    """Require a merged release PR and its exact dev tree before reading private data."""
    if (os.environ.get("GITHUB_EVENT_NAME") != "push" or os.environ.get("GITHUB_REF") != "refs/heads/main"
            or os.environ.get("GITHUB_SHA") != commit):
        raise ValueError("Publication requires the exact protected main push.")
    if os.environ.get("SCP_PREBUILT_PUBLICATION") != "enabled":
        raise ValueError("Public prebuilt publication is disabled. Complete the private hosted review first.")
    repository = _repository()
    _require_private_review(repo, repository, os.environ.get("SCP_PREBUILT_REVIEW_RUN_ID", ""), commit)
    pages = _gh(f"repos/{repository}/commits/{commit}/pulls", paginated=True)
    candidates = [pr for page in pages for pr in page
                  if pr.get("merged_at") and pr.get("merge_commit_sha") == commit
                  and pr.get("base", {}).get("ref") == "main"
                  and pr.get("head", {}).get("ref") == "dev"
                  and all((pr.get(side, {}).get("repo") or {}).get("full_name") == repository
                          for side in ("head", "base"))]
    if len(candidates) != 1:
        raise ValueError("This main commit is not the merge of this repository's approved dev release PR.")
    dev_commit, dev_tree = source_identity(repo, candidates[0]["head"]["sha"])
    if tree != dev_tree:
        raise ValueError(f"Main {commit} has tree {tree}, but release dev {dev_commit} has tree {dev_tree}. "
                         f"Reconcile the branches and prepare the exact resulting dev revision before merging.")
    return dev_commit


def _negative_review(archive, workspace, commit, tree):
    """Exercise the real downloader and reject a real ZIP under a wrong tree."""
    wrong_tree = sha1(("scp negative review " + tree).encode("ascii")).hexdigest()
    wrong = workspace / "negative" / archive_name(wrong_tree)
    wrong.parent.mkdir()
    try:
        download_archive(wrong.name, wrong)
    except DropboxNotFound:
        if wrong.exists():
            raise ValueError("The rejected download left a partial ZIP.")
    else:
        raise ValueError("The Dropbox path reserved for the missing-file check unexpectedly exists.")
    # Move the local copy temporarily so this tests its internal envelope, not
    # just the name of a file that happens to contain the wrong Git tree.
    archive.rename(wrong)
    rejected = wrong.parent / "payload"
    try:
        try:
            extract_release_payload(wrong, rejected, source_commit=commit, source_tree=wrong_tree)
        except ValueError:
            if rejected.exists():
                raise ValueError("The mismatched ZIP left a usable payload.")
        else:
            raise ValueError("The wrong source tree was accepted.")
    finally:
        wrong.rename(archive)


def receive(repo, workspace, *, mode):
    commit, tree = source_identity(repo)
    if os.environ.get("GITHUB_SHA") != commit:
        raise ValueError("The runner checkout differs from the requested GitHub Actions revision.")
    if mode == "publish":
        dev_commit = approved_release_head(repo, commit, tree)
    elif os.environ.get("GITHUB_EVENT_NAME") == "workflow_dispatch" and os.environ.get("GITHUB_REF") == "refs/heads/dev":
        dev_commit = commit
    else:
        raise ValueError("Private hosted review must be manually dispatched on dev.")
    workspace.mkdir(parents=True, exist_ok=False)
    archive = workspace / archive_name(tree)
    try:
        download = download_archive(archive.name, archive)
    except DropboxNotFound:
        raise ValueError(f"Dropbox has no complete {archive.name} for dev {dev_commit} and receiving commit {commit}. "
                         "Prepare that exact dev revision on the Mac.") from None
    payload = workspace / "payload"
    record = extract_release_payload(archive, payload, source_commit=commit, source_tree=tree, repo=repo)
    if record["archive_sha256"] != download["sha256"]:
        raise ValueError("The verified handoff ZIP changed after the Dropbox download.")
    if mode == "review":
        _negative_review(archive, workspace, commit, tree)
    (workspace / "release-record.json").write_text(
        json.dumps(record, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    return record


def require_release_evidence(root, manifest):
    """Check public evidence for an experimental prebuilt installer."""
    from scp import jsonc
    from scp.catalog import load_catalog
    from scp.release import assess_build

    pieces = [piece for piece in load_catalog(root)["pieces"] if piece["status"] != "draft"]
    if {piece["id"] for piece in pieces} != {piece["id"] for piece in manifest["pieces"]}:
        raise ValueError("Public release payload does not contain the current complete catalogue.")
    folder = manifest["plugin_folder"]
    complete = [{**piece, "asset_file": f"{folder}/20_Pieces/SCP_{piece['id']}.dat"} for piece in pieces]
    gates = jsonc.load(Path(root) / "config/release.jsonc")
    installer = gates.get("prebuilt_installer", {}) if isinstance(gates, dict) else None
    if not isinstance(installer, dict):
        raise ValueError("Release record prebuilt_installer settings must be an object.")
    require_build_game_evidence = installer.get("require_build_game_evidence", True)
    if type(require_build_game_evidence) is not bool:
        raise ValueError("Release record prebuilt_installer.require_build_game_evidence must be true or false.")
    result = assess_build(root, {**manifest, "pieces": complete},
                          require_build_game_evidence=require_build_game_evidence)
    if not result["public_release_ready"]:
        reasons = result["blocked"]
        remaining = len(reasons) - min(len(reasons), 12)
        raise ValueError("Public prebuilt release requirements are unmet. "
                         + " | ".join(reasons[:12])
                         + (f" | {remaining} additional release checks are blocked." if remaining else ""))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path, required=True)
    parser.add_argument("--mode", choices=("review", "publish"), required=True)
    args = parser.parse_args(argv)
    root = Path(__file__).resolve().parents[1]
    from main import bootstrap
    bootstrap(root)
    record = receive(root.parent, args.workspace, mode=args.mode)
    if args.mode == "publish":
        require_release_evidence(root, json.loads((args.workspace / "payload/manifest.json").read_bytes()))
    print(json.dumps({"status": "passed", "mode": args.mode, **record}, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        # API clients report a safe failure without printing request headers,
        # bearer tokens, or a remote error response.
        raise SystemExit(str(error)) from None
