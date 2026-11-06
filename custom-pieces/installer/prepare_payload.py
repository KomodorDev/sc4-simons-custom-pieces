"""Build the complete, private, prebuilt installer input from audited game files."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys

from main import bootstrap


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--game-folder', type=Path, required=True)
    parser.add_argument('--player-data', type=Path, required=True)
    parser.add_argument('--work-dir', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args(argv)
    root = Path(__file__).resolve().parents[1]
    commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
    dirty = subprocess.check_output(
        ['git', 'status', '--porcelain=v1', '--untracked-files=all', '--', '.'], cwd=root, text=True)
    if dirty:
        raise ValueError('Commit changes to the library before preparing a revision-bound payload.')
    bootstrap(root)
    from scp.prebuilt import prepare_payload
    from scp_installer.service import all_implemented_ids, discover_installation, prepare_install_build, _work_root

    installation = discover_installation(args.game_folder, player_data=args.player_data)
    paths = []
    for path in (args.work_dir, args.output):
        path = path.expanduser().absolute()
        if any(part.is_symlink() for part in (path, *path.parents)):
            raise ValueError('Build and payload paths must use regular directories.')
        path = path.resolve()
        for protected in (installation.game_folder, installation.plugins, *installation.extra_plugins):
            if path.is_relative_to(protected) or protected.is_relative_to(path):
                raise ValueError('Build and payload paths must stay separate from the game and Plugins.')
        paths.append(path)
    work, output = paths
    if output.exists() or work.is_relative_to(output):
        raise ValueError('Choose a new output path that does not contain the working directory.')
    work = _work_root(work, installation)
    ids = all_implemented_ids(root)

    def progress(event):
        print(json.dumps(event), file=sys.stderr, flush=True)

    _, build, _, _ = prepare_install_build(root, installation, work, ids, progress=progress)
    current = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
    dirty = subprocess.check_output(
        ['git', 'status', '--porcelain=v1', '--untracked-files=all', '--', '.'], cwd=root, text=True)
    if dirty or current != commit:
        raise ValueError('The library source changed during preparation. Build again from a clean revision.')
    manifest = prepare_payload(build, output, commit)
    print(json.dumps({'source_commit': commit, 'pieces': len(manifest['pieces']), 'files': len(manifest['files']),
                      'payload': str(output), 'verified_build': str(build)}, indent=2))
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        raise SystemExit(str(error)) from error
