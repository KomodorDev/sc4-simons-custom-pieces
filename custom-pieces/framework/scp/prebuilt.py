"""Prepare a portable installer payload and check its local dependencies."""
from __future__ import annotations

import json
from pathlib import Path
import re
import shutil
import tempfile

from .dbpf import read_index, require, tgi_string
from .install import FOLDER, NETWORK_INI, RUL0, _checked_install_files, _root, _sha


KIND = 'scp-prebuilt-payload'
CONTROLLER = '00_SCP_Controller_NAM50.dat'
MENU = '10_SCP_Menu.dat'
SHA256 = re.compile(r'[0-9a-f]{64}')
COMMIT = re.compile(r'[0-9a-f]{40}')
PIECE_ID = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*')
TGI = re.compile(r'[0-9a-f]{8}(?:-[0-9a-f]{8}){2}')
IID = re.compile(r'[0-9a-f]{8}')


def _matches(pattern, value):
    return isinstance(value, str) and pattern.fullmatch(value) is not None


def _file_paths(piece_ids):
    return {f'{FOLDER}/{CONTROLLER}', f'{FOLDER}/{MENU}',
            *(f'{FOLDER}/20_Pieces/SCP_{piece_id}.dat' for piece_id in piece_ids)}


def load_payload(path, source_commit=None):
    """Read the exact manifest bytes and validate the portable payload format."""
    path = _root(path)
    filename = path / 'manifest.json'
    require(not filename.is_symlink() and filename.is_file(), 'Prebuilt payload manifest is missing or linked')
    require({item.name for item in path.iterdir()} == {'manifest.json', FOLDER},
            'Prebuilt payload contains files outside its managed plugin folder')
    raw = filename.read_bytes()
    manifest = json.loads(raw)
    require(isinstance(manifest, dict) and set(manifest) == {
        'schema_version', 'kind', 'plugin_folder', 'source_commit', 'verified_build_manifest_sha256',
        'profile', 'pieces', 'files', 'dependency_audit', 'exclusive_instance_ids',
    }, 'Invalid prebuilt payload manifest fields')
    require(manifest['schema_version'] == 1 and manifest['kind'] == KIND and manifest['plugin_folder'] == FOLDER
            and _matches(COMMIT, manifest['source_commit'])
            and (source_commit is None or manifest['source_commit'] == source_commit)
            and _matches(SHA256, manifest['verified_build_manifest_sha256']),
            'Prebuilt payload does not match the requested source revision or format')
    pieces = manifest['pieces']
    require(isinstance(pieces, list) and pieces
            and all(isinstance(piece, dict) and set(piece) == {'id'} and _matches(PIECE_ID, piece['id'])
                    for piece in pieces), 'Invalid prebuilt piece selection')
    piece_ids = {piece['id'] for piece in pieces}
    require(len(piece_ids) == len(pieces), 'Duplicate prebuilt piece identifier')
    files = manifest['files']
    require(isinstance(files, list) and all(
        isinstance(row, dict) and set(row) == {'path', 'sha256', 'bytes'} and isinstance(row['path'], str)
        and _matches(SHA256, row['sha256']) and type(row['bytes']) is int and row['bytes'] > 0 for row in files),
        'Invalid prebuilt file records')
    paths = {row['path'] for row in files}
    require(len(paths) == len(files) and paths == _file_paths(piece_ids),
            'Prebuilt archives differ from the declared pieces, controller, and menu')
    profile = manifest['profile']
    require(isinstance(profile, dict) and set(profile) == {'id', 'donors'}
            and _matches(PIECE_ID, profile['id']) and isinstance(profile['donors'], list)
            and all(isinstance(row, dict) and set(row) == {'filename', 'sha256'}
                    and isinstance(row['filename'], str) and bool(row['filename'])
                    and not any(c in row['filename'] for c in ('/', '\\', ':', '\0'))
                    and row['filename'].lower().endswith('.dat') and _matches(SHA256, row['sha256'])
                    for row in profile['donors']), 'Invalid prebuilt NAM donor profile')
    names = {row['filename'].casefold() for row in profile['donors']}
    require(len(names) == len(profile['donors']) and 'networkaddonmod_controller.dat' in names,
            'Prebuilt NAM donor profile has duplicate files or no controller')
    dependencies = manifest['dependency_audit']
    require(isinstance(dependencies, dict) and set(dependencies) == {'textures', 'shadows'}
            and all(isinstance(values, list) and all(_matches(TGI, value) for value in values)
                    and len(set(values)) == len(values) for values in dependencies.values()),
            'Invalid prebuilt texture or shadow dependencies')
    instances = manifest['exclusive_instance_ids']
    require(isinstance(instances, list) and all(_matches(IID, value) for value in instances)
            and len(set(instances)) == len(instances), 'Invalid prebuilt presentation identifiers')
    return manifest, _sha(raw)


def verify_payload(path, source_commit=None):
    """Verify the prepared payload without calling the model or menu builders."""
    path = Path(path)
    manifest, _ = load_payload(path, source_commit)
    _checked_install_files(path, manifest)
    _indexed_payload(path, manifest)
    return manifest


def _archive_keys(path):
    index = read_index(path)
    keys = {(kind, group, instance) for kind, group, instance, _, _ in index}
    require(keys and len(keys) == len(index), f'Empty or duplicate resource index: {path.name}')
    return keys


def _indexed_payload(path, manifest):
    from .adaptive_network import RUL1
    from .menu import DESCRIPTION, ICON, MENU_EXEMPLAR, TITLE
    from .track_paths import S3D

    donor_hashes = {row['sha256'] for row in manifest['profile']['donors']}
    resources = set()
    for row in manifest['files']:
        filename = path / row['path']
        keys = _archive_keys(filename)
        require(row['sha256'] not in donor_hashes, f'Prebuilt payload contains an unmodified source archive: {filename.name}')
        if filename.name == CONTROLLER:
            require(keys == {RUL0, NETWORK_INI} or keys == {RUL0, NETWORK_INI, RUL1},
                    'Invalid prebuilt shared-controller resource index')
        elif filename.name == MENU:
            require(all(key[:2] in (DESCRIPTION, ICON, MENU_EXEMPLAR, TITLE) for key in keys),
                    'Invalid prebuilt menu resource index')
        else:
            require(any(key[:2] == S3D for key in keys), f'Prebuilt piece contains no model: {filename.name}')
        require(not keys & resources, f'Duplicate prebuilt resource in {filename.name}')
        resources.update(keys)
    return resources - {RUL0, NETWORK_INI, RUL1}


def check_local_resources(path, manifest, installed):
    """Check installed resource indexes without decoding or rebuilding geometry."""
    keys = _indexed_payload(path, manifest)
    if collision := keys & installed.keys():
        key = min(collision)
        raise ValueError(f'Prebuilt resource {tgi_string(key)} conflicts with {installed[key][0].name}')
    reserved = {int(value, 16) for value in manifest['exclusive_instance_ids']}
    for key in installed:
        if key[2] in reserved:
            raise ValueError(f'Prebuilt menu identifier {key[2]:08x} conflicts with {installed[key][0].name}')
    for kind, keys in manifest['dependency_audit'].items():
        for key in keys:
            if tuple(int(value, 16) for value in key.split('-')) not in installed:
                raise ValueError(f'Missing {kind} required by the prebuilt release: {key}')


def prepare_payload(build, destination, source_commit):
    """Export only the final install files from a fully verified assembly build."""
    from .multi_assembly_menu import KIND as ASSEMBLY_KIND, _alias_targets, _groups
    from .verify import verify_build

    require(_matches(COMMIT, source_commit), 'Prebuilt source revision must be a full Git commit')
    build = _root(build)
    destination = Path(destination).expanduser().absolute()
    require(not any(part.is_symlink() for part in (destination, *destination.parents)),
            'Prebuilt output must not use symbolic links')
    destination = destination.resolve()
    require(not destination.exists() and not destination.is_relative_to(build)
            and not build.is_relative_to(destination), 'Prebuilt output must be new and outside the verified build')
    source_manifest = build / 'manifest.json'
    raw = source_manifest.read_bytes()
    source = json.loads(raw)
    menu = source.get('menu_experiment', {})
    require(menu.get('kind') == ASSEMBLY_KIND, 'Prebuilt payload requires the verified installer assembly menus')
    report = verify_build(build, write_report=False)
    require(report.get('static_checks_passed') is True
            and report.get('source_build_verification', {}).get('local_donor_comparison') is True
            and source_manifest.read_bytes() == raw,
            'Prebuilt payload requires saved-resource verification against the audited local inputs')
    groups_record = menu['source_inputs']['groups']
    groups_raw = (build / groups_record['path']).read_bytes()
    require(_sha(groups_raw) == groups_record['sha256'], 'Assembly selection proof changed after verification')
    groups = _groups(source, json.loads(groups_raw))
    manifest = {
        'schema_version': 1, 'kind': KIND, 'plugin_folder': FOLDER,
        'source_commit': source_commit, 'verified_build_manifest_sha256': _sha(raw),
        'profile': source['profile'], 'pieces': [{'id': piece['id']} for piece in source['pieces']],
        'files': source['files'], 'dependency_audit': source['dependency_audit'],
    }
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.scp-prebuilt-', dir=destination.parent) as temporary:
        stage = Path(temporary) / 'payload'
        shutil.copytree(build / FOLDER, stage / FOLDER)
        _checked_install_files(stage, manifest)
        menu_ids = {key[2] for key in _archive_keys(stage / FOLDER / MENU)}
        menu_ids -= {int(piece['menu']['id'], 16) for piece in source['pieces']}
        menu_ids |= {target for layout, _, pieces in groups
                     for target in _alias_targets(layout, pieces).values()}
        manifest['exclusive_instance_ids'] = [f'{value:08x}' for value in sorted(menu_ids)]
        (stage / 'manifest.json').write_text(json.dumps(manifest, indent=2, sort_keys=True) + '\n', encoding='utf-8')
        verify_payload(stage, source_commit)
        stage.rename(destination)
    return manifest
