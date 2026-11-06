"""Build a verified dev payload on the Mac and wait for its Dropbox upload."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import secrets
import subprocess
import sys
import tempfile
import zipfile

from main import bootstrap
from release_dropbox import (
    DEFAULT_CREDENTIALS, DropboxClient, load_local_credentials, sync_archive, validate_dropbox_directory,
)
from release_payload import archive_name, extract_release_payload, source_identity, write_release_payload


DEV_REFSPEC = "refs/heads/dev:refs/remotes/origin/dev"
DEFAULT_SYNC_TIMEOUT = 1800


def _regular_path(path):
    path = Path(path).expanduser().absolute()
    if any(part.is_symlink() for part in (path, *path.parents)):
        raise ValueError(f"Use a path without symbolic links: {path}")
    return path.resolve()


def _overlaps(path, other):
    return path.is_relative_to(other) or other.is_relative_to(path)


def _clean_dev_source(repo):
    dirty = subprocess.check_output(
        ["git", "status", "--porcelain=v1", "--untracked-files=all"], cwd=repo, text=True)
    if dirty:
        raise ValueError("Use a clean, committed checkout to prepare a release payload.")
    current = source_identity(repo)
    dev = source_identity(repo, "origin/dev")
    if current[1] != dev[1]:
        raise ValueError("This checkout's Git tree differs from the fetched origin/dev tree.")
    if current[0] != dev[0] and subprocess.run(
            ["git", "merge-base", "--is-ancestor", current[0], dev[0]],
            cwd=repo, capture_output=True).returncode != 0:
        raise ValueError("GitHub cannot verify this local-only prebuild commit. Prepare from the fetched dev history.")
    return current


def _fetch_dev(repo):
    subprocess.run(["git", "fetch", "--no-tags", "origin", DEV_REFSPEC], cwd=repo, check=True)


def _staging_root(repo, staging_folder, dropbox_root):
    cloud_storage = (Path.home() / "Library/CloudStorage").resolve()
    if staging_folder is None:
        staging_folder = repo / "custom-pieces/local/release-staging"
        if _overlaps(staging_folder, dropbox_root) or staging_folder.is_relative_to(cloud_storage):
            staging_folder = Path.home() / "Library/Application Support/SimonsCustomPieces/ReleaseStaging"
    staging = _regular_path(staging_folder)
    if (_overlaps(staging, dropbox_root) or staging.is_relative_to(cloud_storage)
            or repo.is_relative_to(staging)):
        raise ValueError("Choose a dedicated private staging folder outside the Dropbox desktop folder.")
    if staging.is_relative_to(repo):
        relative = staging.relative_to(repo)
        if subprocess.run(["git", "check-ignore", "-q", "--", str(relative)], cwd=repo).returncode != 0:
            raise ValueError("A staging folder in the repository must be ignored by Git.")
    return staging


def _prove_dropbox_folder(staging, dropbox, credentials, timeout):
    """Confirm Desktop sync reaches this OAuth app before copying any game files."""
    with tempfile.TemporaryDirectory(prefix=".dropbox-probe-", dir=staging) as temporary:
        marker = secrets.token_hex(16)
        probe = Path(temporary) / f"SCP-App-Folder-Probe-{marker}.zip"
        with zipfile.ZipFile(probe, "x") as archive:
            archive.writestr("probe.txt", marker)
        target = dropbox / probe.name
        try:
            sync_archive(probe, dropbox, timeout=timeout, credentials=credentials)
        finally:
            if (not target.is_symlink() and target.is_file()
                    and target.stat().st_size == probe.stat().st_size and target.read_bytes() == probe.read_bytes()):
                target.unlink(missing_ok=True)


def prepare_release(repo, *, game_folder, player_data, dropbox_folder, staging_folder,
                    credentials_path, sync_timeout, resume_archive=None, jobs=None):
    """Prepare, verify, and sync the release payload for the current dev tree."""
    if jobs is not None:
        if type(jobs) is not int or jobs < 1:
            raise ValueError("--jobs must be a positive integer")
        if resume_archive is not None:
            raise ValueError("--jobs applies only to new builds")
    repo = Path(repo).resolve()
    dropbox = validate_dropbox_directory(_regular_path(dropbox_folder))
    if dropbox.parent.name.casefold() != "apps":
        raise ValueError("Select the application's existing folder directly inside Dropbox's Apps folder.")
    dropbox_root = dropbox.parent.parent
    staging = _staging_root(repo, staging_folder, dropbox_root)
    credentials_path = _regular_path(credentials_path)
    if credentials_path.is_relative_to(dropbox_root):
        raise ValueError("Keep the credentials file outside the Dropbox desktop folder.")
    if resume_archive is None:
        game_folder = Path(game_folder).expanduser().resolve()
        player_data = Path(player_data).expanduser().resolve()
        if not game_folder.exists() or not player_data.is_dir():
            raise ValueError("Select the existing Windows game and player-data folders on this Mac.")
        for protected in (game_folder.parent if game_folder.is_file() else game_folder, player_data):
            if _overlaps(staging, protected):
                raise ValueError("Keep release staging outside the game and player-data folders.")
    _fetch_dev(repo)
    source_commit, source_tree = _clean_dev_source(repo)
    filename = archive_name(source_tree)
    credentials = load_local_credentials(credentials_path)
    client = DropboxClient(credentials)
    client.refresh_access_token()
    client.get_metadata(f"/{filename}")

    staging.mkdir(mode=0o700, parents=True, exist_ok=True)
    if resume_archive is not None:
        archive = _regular_path(resume_archive)
        if archive.name != filename or not archive.is_relative_to(staging) or not archive.is_file():
            raise ValueError("Resume from the current tree's ZIP in the private staging folder.")
        with tempfile.TemporaryDirectory(prefix=".verify-", dir=staging) as temporary:
            release = extract_release_payload(archive, Path(temporary) / "payload",
                                              source_commit=source_commit, source_tree=source_tree, repo=repo)
        if release["prebuild_commit"] != source_commit:
            raise ValueError("Resume from a ZIP prepared by this exact source commit.")
    else:
        run = Path(tempfile.mkdtemp(prefix=f"{source_tree[:12]}-", dir=staging))
        payload, archive = run / "payload", run / filename
        print(f"Preparing the complete verified payload in {run}", file=sys.stderr, flush=True)
        command = [sys.executable, "-B", str(repo / "custom-pieces/installer/prepare_payload.py"),
                   "--game-folder", str(game_folder), "--player-data", str(player_data),
                   "--work-dir", str(run / "work"), "--output", str(payload)]
        if jobs is not None:
            command.extend(["--jobs", str(jobs)])
        subprocess.run(command, cwd=repo, check=True, stdout=sys.stderr)
        if _clean_dev_source(repo) != (source_commit, source_tree):
            raise ValueError("The checkout changed during preparation. Build again from the current dev tree.")
        release = write_release_payload(payload, archive, source_commit=source_commit, source_tree=source_tree)

    print(f"Verified private ZIP at {archive}", file=sys.stderr, flush=True)
    _fetch_dev(repo)
    if _clean_dev_source(repo) != (source_commit, source_tree):
        raise ValueError("The checkout changed during preparation. Build again from the current dev tree.")
    print("Checking that the selected Dropbox folder belongs to this app.", file=sys.stderr, flush=True)
    _prove_dropbox_folder(staging, dropbox, credentials, sync_timeout)
    print("Waiting for Dropbox to verify the uploaded bytes.", file=sys.stderr, flush=True)
    size = archive.stat().st_size
    proof = sync_archive(archive, dropbox, timeout=sync_timeout, credentials=credentials,
                         sha256_digest=release["archive_sha256"], size=size)
    if proof["sha256"] != release["archive_sha256"] or proof["bytes"] != size:
        raise ValueError("Dropbox proof differs from the verified release ZIP.")
    _fetch_dev(repo)
    if _clean_dev_source(repo) != (source_commit, source_tree):
        raise ValueError("The dev source changed while Dropbox was syncing. Prepare the new dev revision before merging.")
    return {"status": "payload-ready", "source_commit": source_commit, "source_tree": source_tree,
            "archive": str(archive), **proof}


def _positive_seconds(value):
    seconds = float(value)
    if not math.isfinite(seconds) or seconds <= 0:
        raise argparse.ArgumentTypeError("Enter a finite timeout greater than zero.")
    return seconds


def main(argv=None):
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog="A ready payload can proceed to the separate protected review or release workflow.")
    parser.add_argument("--game-folder", type=Path, help="Windows SimCity 4 game folder on this Mac.")
    parser.add_argument("--player-data", type=Path, help="Player-data folder or Plugins folder containing NAM.")
    parser.add_argument("--dropbox-folder", type=Path, required=True,
                        help="Existing Dropbox desktop app folder, inside the Dropbox Apps folder.")
    parser.add_argument("--credentials", type=Path, default=DEFAULT_CREDENTIALS,
                        help="Private Dropbox OAuth credentials file.")
    parser.add_argument("--staging-folder", type=Path,
                        help="Private staging folder. Defaults to ignored local staging outside cloud storage.")
    parser.add_argument("--sync-timeout", type=_positive_seconds, default=DEFAULT_SYNC_TIMEOUT,
                        help="Maximum seconds to wait for Dropbox to sync (default: %(default)s).")
    parser.add_argument("--resume-archive", type=Path,
                        help="Retry syncing the exact verified ZIP from a previous interrupted run.")
    parser.add_argument("--jobs", type=int,
                        help="Maximum compilation workers for a new build (default: half the available logical CPUs, at least one).")
    args = parser.parse_args(argv)
    if args.jobs is not None and args.jobs < 1:
        parser.error("--jobs must be a positive integer")
    if args.resume_archive is None and (args.game_folder is None or args.player_data is None):
        parser.error("--game-folder and --player-data are required for a new build")
    if args.resume_archive is not None and any(
            option is not None for option in (args.game_folder, args.player_data, args.jobs)):
        parser.error("--resume-archive retries only the upload, so omit --game-folder, --player-data, and --jobs")
    library = Path(__file__).resolve().parents[1]
    bootstrap(library)
    report = prepare_release(
        library.parent, game_folder=args.game_folder, player_data=args.player_data,
        dropbox_folder=args.dropbox_folder, staging_folder=args.staging_folder,
        credentials_path=args.credentials, sync_timeout=args.sync_timeout, resume_archive=args.resume_archive,
        jobs=args.jobs)
    print(f"Payload ready to merge for dev {report['source_commit']}. Public release requirements still apply.",
          file=sys.stderr)
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        raise SystemExit(str(error)) from error
