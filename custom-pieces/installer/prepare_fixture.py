"""Create synthetic, review-only player payloads for hosted installer checks.

Every DAT contains marker text rather than playable game resources. This fixture
checks Windows packaging, startup, transactions, and extraction without native
SimCity or NAM inputs; it supplies no release or in-game verification evidence.
"""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
import tempfile

from main import bootstrap


MARKER = b'SCP SYNTHETIC PLAYER FIXTURE: not playable and never a public release.\n'


def prepare_fixture(source: Path, destination: Path, source_commit: str) -> dict:
    """Write a deterministic fixture using the current complete piece selection."""
    source = Path(source).resolve()
    destination = Path(destination).expanduser().absolute()
    if re.fullmatch(r'[0-9a-f]{40}', source_commit) is None:
        raise ValueError('The synthetic fixture requires a complete lowercase Git commit.')
    checkout = Path(subprocess.check_output(
        ['git', 'rev-parse', '--show-toplevel'], cwd=source, text=True).strip()).resolve()
    if any(part.is_symlink() for part in (destination, *destination.parents)):
        raise ValueError('Synthetic fixture output must be new, outside the checkout, and without symbolic links.')
    destination = destination.resolve()
    if (destination.exists() or destination.is_relative_to(checkout)
            or checkout.is_relative_to(destination)):
        raise ValueError('Synthetic fixture output must be new, outside the checkout, and without symbolic links.')
    bootstrap(source)
    from scp.dbpf import pack_dbpf
    from scp.install import FOLDER, NETWORK_INI, RUL0
    from scp.player_manifest import _source
    from scp.prebuilt import CONTROLLER, KIND, MENU, MENU_PREFIXES, MODEL_PREFIX, verify_payload

    project = _source(source, 'project.jsonc')
    pieces = []
    dependencies = {'controller'}
    for domain in project['domains'].values():
        registry = _source(source, domain['registry'])
        for relative in registry.get('pieces', []):
            piece = _source(source, (Path(domain['path']) / relative).as_posix())
            if piece['status'] != 'draft':
                pieces.append(piece['id'])
                dependencies.update(piece['dependencies'])
    if not pieces or len(set(pieces)) != len(pieces):
        raise ValueError('Synthetic fixture requires a nonempty, unique implemented piece selection.')
    profile = _source(source, project['profile'])
    donors = [{key: profile['files'][label][key] for key in ('filename', 'sha256')}
              for label in sorted(dependencies)]
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.scp-player-fixture-', dir=destination.parent) as temporary:
        payload = Path(temporary) / 'payload'
        files = []

        def archive(name, resources):
            relative = f'{FOLDER}/{name}'
            raw = pack_dbpf(resources)
            filename = payload / relative
            filename.parent.mkdir(parents=True, exist_ok=True)
            filename.write_bytes(raw)
            files.append({'path': relative, 'bytes': len(raw), 'sha256': sha256(raw).hexdigest()})

        archive(CONTROLLER, {RUL0: MARKER + b'controller rules', NETWORK_INI: MARKER + b'network settings'})
        archive(MENU, {(*sorted(MENU_PREFIXES)[0], 0xF1700000): MARKER + b'menu'})
        for index, piece_id in enumerate(pieces, 1):
            archive(f'20_Pieces/SCP_{piece_id}.dat',
                    {(*MODEL_PREFIX, 0xF1700000 + index): MARKER + piece_id.encode('ascii')})
        manifest = {
            'schema_version': 1, 'kind': KIND, 'plugin_folder': FOLDER, 'source_commit': source_commit,
            'verified_build_manifest_sha256': sha256(MARKER + b'no verified native build exists').hexdigest(),
            'profile': {'id': profile['id'], 'donors': donors},
            'pieces': [{'id': piece_id} for piece_id in pieces], 'files': files,
            'dependency_audit': {'textures': [], 'shadows': []}, 'exclusive_instance_ids': [],
        }
        (payload / 'manifest.json').write_text(json.dumps(manifest, indent=2, sort_keys=True) + '\n', encoding='utf-8')
        verify_payload(payload, source_commit)
        payload.rename(destination)
    return manifest


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--source-commit', required=True)
    args = parser.parse_args(argv)
    manifest = prepare_fixture(args.source, args.output, args.source_commit)
    print(json.dumps({'status': 'passed', 'synthetic_review_fixture': True,
                      'playable': False, 'source_commit': manifest['source_commit'],
                      'pieces': len(manifest['pieces']), 'files': len(manifest['files'])}, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
