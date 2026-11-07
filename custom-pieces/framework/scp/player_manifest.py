"""Compact installation data and exact dependency checks for finished payloads.

Only build_install_manifest reads authoring sources. Player operations use the
generated manifest, the standard library, and the bounded DBPF index reader.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath
import uuid

from .dbpf import pack_dbpf, read_index, require
from .install import FOLDER
from .prebuilt import COMMIT, PIECE_ID, SHA256, TGI, load_payload


INSTALL_MANIFEST = 'installer/install-manifest.json'
KIND = 'scp-player-install-manifest'
MAX_STORED_RESOURCE = 128 * 1024 * 1024


def _matches(pattern, value):
    return isinstance(value, str) and pattern.fullmatch(value) is not None


def _filename(value):
    return (isinstance(value, str) and bool(value) and value not in {'.', '..'}
            and not any(char in value for char in '/\\:\0')
            and not value.endswith((' ', '.')))


def _hash(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def _source(root, relative):
    from . import jsonc
    require(isinstance(relative, str) and not any(char in relative for char in '\\:\0'),
            'Invalid installation source path')
    path = PurePosixPath(relative)
    require(path.as_posix() == relative and not path.is_absolute()
            and '..' not in path.parts, 'Unsafe installation source path')
    filename = Path(root).joinpath(*path.parts)
    require(not any(part.is_symlink() for part in (filename, *filename.parents)),
            'Installation source must not use symbolic links')
    return jsonc.load(filename)


def build_install_manifest(root, payload):
    """Compile only names, policy, and exact dependency plans from the sources."""
    root, payload = Path(root), Path(payload)
    manifest, digest = load_payload(payload)
    project = _source(root, 'project.jsonc')
    pieces = {}
    for domain in project['domains'].values():
        registry = _source(root, domain['registry'])
        for relative in registry.get('pieces', []):
            piece = _source(root, (PurePosixPath(domain['path']) / relative).as_posix())
            if piece['status'] != 'draft':
                require(piece['id'] not in pieces, 'Duplicate installer piece identifier')
                require(piece.get('game_tests', {}).get('placement') != 'failed',
                        'Installer cannot include a piece with failed placement tests')
                pieces[piece['id']] = piece
    require(set(pieces) == {row['id'] for row in manifest['pieces']},
            'Prebuilt payload does not contain the complete implemented installer selection')
    profile = _source(root, project['profile'])
    require(profile['id'] == manifest['profile']['id'], 'Installer source and payload profiles differ')
    by_filename = {row['filename']: row for row in profile['files'].values()}
    captures = []
    for donor in manifest['profile']['donors']:
        record = by_filename.get(donor['filename'])
        require(record is not None and record['sha256'] == donor['sha256'],
                'Installer source and payload donor fingerprints differ')
        if not record.get('audit'):
            continue
        evidence = _source(root, record['audit'])
        if record.get('capture_kind') == 'resource-bundle':
            require(evidence.get('capture_kind') == 'resource-bundle'
                    and evidence.get('capture', {}).get('file') == donor['filename']
                    and evidence['capture'].get('sha256') == donor['sha256'],
                    'Dependency capture evidence differs from the payload profile')
            sources = [{key: row[key] for key in ('filename', 'location', 'archive_sha256')}
                       | {'resources': [{'tgi': resource['tgi'], 'sha256': resource['stored_resource_sha256']}
                                        for resource in row['resources']]}
                       for row in evidence['sources']]
        elif record.get('capture_kind') is None and 'tgi' in evidence:
            require(evidence.get('status') == 'complete' and evidence.get('matching_index_entries') == 1
                    and len(evidence.get('matches', [])) == 1
                    and evidence.get('capture', {}).get('sha256') == donor['sha256'],
                    'Single-resource dependency evidence is incomplete')
            match = evidence['matches'][0]
            name = evidence['scope']['archive'].replace('\\', '/').rsplit('/', 1)[-1]
            sources = [{'filename': name, 'location': 'game' if name.casefold() == 'simcity_3.dat' else 'plugins',
                        'archive_sha256': match['archive_sha256'],
                        'resources': [{'tgi': evidence['tgi'], 'sha256': match['stored_resource_sha256']}]}]
        else:
            require(record.get('capture_kind') is None, 'Unsupported dependency capture kind')
            continue
        captures.append({'filename': donor['filename'], 'sha256': donor['sha256'], 'sources': sources})
    policy = _source(root, 'config/installer.jsonc')
    layouts = _source(root, 'domains/highway/menu-layout.jsonc')['layouts']
    result = {'schema_version': 1, 'kind': KIND, 'source_commit': manifest['source_commit'],
              'payload_manifest_sha256': digest, 'policy': policy,
              'pieces': [{'id': row['id'], 'name': pieces[row['id']]['name']} for row in manifest['pieces']],
              'assembly_menu_layouts': 1 + len(layouts), 'captures': captures}
    _validate(result, manifest, digest)
    return result


def _validate(data, payload_manifest, digest):
    require(isinstance(data, dict) and set(data) == {
        'schema_version', 'kind', 'source_commit', 'payload_manifest_sha256', 'policy', 'pieces',
        'assembly_menu_layouts', 'captures'}, 'Invalid player installation manifest fields')
    require(data['schema_version'] == 1 and data['kind'] == KIND
            and _matches(COMMIT, data['source_commit'])
            and data['source_commit'] == payload_manifest['source_commit']
            and data['payload_manifest_sha256'] == digest,
            'Player installation manifest differs from its verified payload')
    require(isinstance(data['policy'], dict) and type(data['assembly_menu_layouts']) is int
            and data['assembly_menu_layouts'] > 0, 'Invalid player installation policy or menu count')
    pieces = data['pieces']
    require(isinstance(pieces, list) and pieces and all(
        isinstance(row, dict) and set(row) == {'id', 'name'} and _matches(PIECE_ID, row['id'])
        and isinstance(row['name'], str) and row['name'].strip() for row in pieces)
        and len({row['id'] for row in pieces}) == len(pieces)
        and {row['id'] for row in pieces} == {row['id'] for row in payload_manifest['pieces']},
        'Player installation manifest has an invalid piece selection')
    donors = {row['filename']: row['sha256'] for row in payload_manifest['profile']['donors']}
    require(isinstance(data['captures'], list), 'Invalid player dependency capture plans')
    seen = set()
    for capture in data['captures']:
        require(isinstance(capture, dict) and set(capture) == {'filename', 'sha256', 'sources'}
                and _filename(capture['filename']) and capture['filename'] not in seen
                and donors.get(capture['filename']) == capture['sha256']
                and isinstance(capture['sources'], list) and capture['sources'],
                'Invalid player dependency capture')
        seen.add(capture['filename'])
        resources = set()
        sources = set()
        for source in capture['sources']:
            require(isinstance(source, dict) and set(source) == {
                'filename', 'location', 'archive_sha256', 'resources'} and _filename(source['filename'])
                and source['location'] in {'game', 'plugins'} and _matches(SHA256, source['archive_sha256'])
                and isinstance(source['resources'], list) and source['resources'],
                'Invalid player dependency source')
            identity = (source['location'], source['filename'].casefold())
            require(identity not in sources, 'Duplicate player dependency source')
            sources.add(identity)
            for resource in source['resources']:
                require(isinstance(resource, dict) and set(resource) == {'tgi', 'sha256'}
                        and _matches(TGI, resource['tgi']) and _matches(SHA256, resource['sha256'])
                        and resource['tgi'] not in resources, 'Invalid or duplicate captured resource')
                resources.add(resource['tgi'])


def load_install_manifest(root, payload, source_commit=None):
    """Read the compact machine interface and bind it to the original payload."""
    filename = Path(root) / INSTALL_MANIFEST
    require(not filename.is_symlink() and filename.is_file(), 'Player installation manifest is missing or linked')
    data = json.loads(filename.read_text(encoding='utf-8'))
    manifest, digest = load_payload(payload, source_commit)
    _validate(data, manifest, digest)
    return data


def prepare_dependencies(manifest, installation, work_root, *, progress=None, cancel=None):
    """Verify originals and recreate only exact, tiny dependency-check archives."""
    roots = [installation.plugins, *installation.extra_plugins]
    managed = installation.plugins / FOLDER
    target = Path(work_root) / 'local/captures' / uuid.uuid4().hex
    prepared = []
    archive_hashes = {}
    for capture in manifest['captures']:
        if cancel and cancel():
            raise ValueError('Installation cancelled before the plugin-folder transaction; installed files are unchanged.')
        if progress:
            progress({'phase': 'capture', 'dependency': capture['filename']})
        resources = {}
        for source in capture['sources']:
            if source['location'] == 'game':
                candidates = [path for path in installation.game_folder.iterdir()
                              if path.name.casefold() == source['filename'].casefold()]
            else:
                candidates = [path for root in roots for path in root.rglob('*')
                              if path.name.casefold() == source['filename'].casefold()
                              and not path.is_relative_to(managed)]
            require(len(candidates) == 1 and candidates[0].is_file(),
                    f"Expected one original {source['filename']} for the supported game/NAM profile")
            path = candidates[0]
            require(not any(part.is_symlink() for part in (path, *path.parents)),
                    f'Original dependency must not use symbolic links: {path.name}')
            if path not in archive_hashes:
                archive_hashes[path] = _hash(path)
            require(archive_hashes[path] == source['archive_sha256'],
                    f'Installed game/NAM fingerprint mismatch: {path.name}; this variant needs a new compatibility audit')
            index = read_index(path)
            with path.open('rb') as stream:
                for resource in source['resources']:
                    key = tuple(int(part, 16) for part in resource['tgi'].split('-'))
                    matches = [row for row in index if row[:3] == key]
                    require(len(matches) == 1, f'Expected exactly one supported resource {resource["tgi"]} in {path.name}')
                    _, _, _, offset, size = matches[0]
                    require(size <= MAX_STORED_RESOURCE, 'Stored dependency resource is too large')
                    stream.seek(offset)
                    raw = stream.read(size)
                    require(len(raw) == size and hashlib.sha256(raw).hexdigest() == resource['sha256'],
                            f'Original dependency resource changed in {path.name}: {resource["tgi"]}')
                    require(key not in resources, 'Duplicate dependency capture resource')
                    resources[key] = raw
        raw = pack_dbpf(resources)
        require(hashlib.sha256(raw).hexdigest() == capture['sha256'],
                f'Generated dependency fingerprint differs from the supported profile: {capture["filename"]}')
        existing = [path for root in roots for path in root.rglob('*')
                    if path.name.casefold() == capture['filename'].casefold() and not path.is_relative_to(managed)]
        if existing:
            require(len(existing) == 1 and existing[0].is_file() and not existing[0].is_symlink()
                    and _hash(existing[0]) == capture['sha256'],
                    f'Existing dependency capture is duplicated or changed: {capture["filename"]}')
            continue
        target.mkdir(parents=True, exist_ok=True)
        (target / capture['filename']).write_bytes(raw)
        prepared.append({'filename': capture['filename'], 'sha256': capture['sha256']})
    return ([target] if prepared else []), prepared
