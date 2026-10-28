"""Install and reverse a verified build without changing NAM's own files.

The only managed location inside Plugins is ``zzz_Simons_Custom_Pieces``.
Every replacement has an external snapshot; a receipt records the exact files
owned by the installation. Unknown, missing or changed files stop the operation.
"""
from __future__ import annotations

import hashlib
from functools import wraps
from inspect import signature
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import tempfile
import uuid


FOLDER = 'zzz_Simons_Custom_Pieces'
RECEIPT = '.scp-install.json'
OPERATION_LOCK = '.scp-operation.lock'
RUL0 = (0x0A5BCF4B, 0xAA5BCF57, 0x10000000)
NETWORK_INI = (0x00000000, 0x8A5971C5, 0x8A5993B9)


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text())
    except (OSError, ValueError) as exc:
        raise ValueError(f'Cannot read {path.name}: {exc}') from exc
    if not isinstance(value, dict):
        raise ValueError(f'{path.name} must contain a JSON object')
    return value


def _write_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, sort_keys=True, indent=2) + '\n')


def _root(path: Path, *, required: bool = True) -> Path:
    path = Path(path).expanduser().absolute()
    # Inspect before resolve(), which would conceal a supplied symbolic link.
    for component in (path, *path.parents):
        if component.is_symlink():
            raise ValueError(f'Symbolic links are not allowed: {component}')
    if required and not path.is_dir():
        raise ValueError(f'Directory does not exist: {path}')
    if path.exists() and not path.is_dir():
        raise ValueError(f'Expected a directory: {path}')
    return path.resolve()


def _inside(path: Path, root: Path) -> bool:
    return path == root or root in path.parents


def _relative(value: str) -> str:
    if not isinstance(value, str) or '\\' in value:
        raise ValueError('File paths must be relative POSIX paths')
    path = PurePosixPath(value)
    if not value or path.is_absolute() or '..' in path.parts or str(path) != value:
        raise ValueError(f'Unsafe relative file path: {value!r}')
    return value


def _tree(folder: Path) -> dict[str, str]:
    """Hash all regular files, rejecting symbolic links and special objects."""
    if folder.is_symlink() or not folder.is_dir():
        raise ValueError(f'Expected a real directory: {folder}')
    result = {}
    for path in sorted(folder.rglob('*')):
        if path.is_symlink():
            raise ValueError(f'Symbolic links are not allowed: {path}')
        if path.is_file():
            result[path.relative_to(folder).as_posix()] = _sha(path.read_bytes())
        elif not path.is_dir():
            raise ValueError(f'Unsupported filesystem object: {path}')
    return result


def _hashes(value: object) -> dict[str, str]:
    if not isinstance(value, dict) or not value:
        raise ValueError('Expected a nonempty file hash table')
    result = {}
    for path, digest in value.items():
        _relative(path)
        if not isinstance(digest, str) or not re.fullmatch(r'[0-9a-f]{64}', digest):
            raise ValueError(f'Invalid SHA-256 for {path}')
        result[path] = digest
    return result


def _owned(folder: Path) -> dict | None:
    if folder.is_symlink():
        raise ValueError(f'Symbolic links are not allowed: {folder}')
    if not folder.exists():
        return None
    actual = _tree(folder)
    if RECEIPT not in actual:
        raise ValueError(f'Existing {FOLDER} has no ownership receipt; refusing to replace it')
    receipt = _json(folder / RECEIPT)
    if receipt.get('schema_version') != 1 or receipt.get('plugin_folder') != FOLDER:
        raise ValueError('Unrecognized installation receipt')
    expected = _hashes(receipt.get('files'))
    if RECEIPT in expected:
        raise ValueError('The receipt cannot claim ownership of itself')
    actual.pop(RECEIPT)
    if actual != expected:
        raise ValueError('Managed folder has unknown, missing or changed files; refusing to overwrite it')
    if not isinstance(receipt.get('backup_id'), str):
        raise ValueError('Installation receipt has no backup identifier')
    return receipt


def _scan_roots(plugins: Path, extra_roots=None) -> list[Path]:
    roots = [plugins] + [_root(path) for path in (extra_roots or [])]
    if len(roots) != len(set(roots)):
        raise ValueError('Duplicate Plugins scan root')
    if any(a != b and _inside(a, b) for a in roots for b in roots):
        raise ValueError('Nested Plugins scan roots are not allowed')
    return roots


def _profile(profile: dict, plugins: Path, managed: Path, *, extra_roots=None) -> Path:
    if not isinstance(profile, dict) or not isinstance(profile.get('donors'), list):
        raise ValueError('Build has no pinned NAM source profile')
    controller = None
    seen = set()
    for donor in profile['donors']:
        name, expected = donor.get('filename'), donor.get('sha256')
        if not isinstance(name, str) or Path(name).name != name or name in seen:
            raise ValueError('Invalid or duplicate donor filename')
        if not isinstance(expected, str) or not re.fullmatch(r'[0-9a-f]{64}', expected):
            raise ValueError(f'Invalid donor fingerprint: {name}')
        seen.add(name)
        matches = [p for root in _scan_roots(plugins, extra_roots)
                   for p in root.rglob(name) if not _inside(p, managed)]
        if len(matches) != 1 or matches[0].is_symlink() or not matches[0].is_file():
            raise ValueError(f'Expected one regular installed NAM donor named {name}')
        path = matches[0]
        if _sha(path.read_bytes()) != expected:
            raise ValueError(f'Installed NAM fingerprint mismatch: {name}; rebuild for this NAM installation')
        if name == 'NetworkAddonMod_Controller.dat':
            controller = path.resolve()
    if controller is None:
        raise ValueError('Source profile does not pin NetworkAddonMod_Controller.dat')
    return controller


def _scanned_dll_link(path: Path, roots: list[Path], managed: Path) -> bool:
    """Recognize a DLL shortcut without permitting hidden DBPF resources.

    sc4pac exposes nested DLLs at Plugins' top level through file links. DLLs
    are not indexed DBPF archives. Require a real Windows executable target
    within an explicitly scanned root, outside the managed SCP installation.
    Directory links, archive aliases, broken links and external targets remain
    forbidden. This does not copy, move or modify the link or its target.
    """
    if path.suffix.lower() != '.dll':
        return False
    try:
        target = path.resolve(strict=True)
        if (target.suffix.lower() != '.dll' or not target.is_file()
                or _inside(target, managed)
                or not any(_inside(target, root) for root in roots)):
            return False
        with target.open('rb') as stream:
            return stream.read(2) == b'MZ'
    except (OSError, RuntimeError):
        return False


def _foreign_overlays(plugins: Path, managed: Path, controller: Path, *, extra_roots=None) -> None:
    from .dbpf import index_plugins
    # Refuse linked plugin subtrees and DATs: an index scan must not miss a
    # foreign controller. Only validated non-DBPF DLL file shortcuts may pass.
    locations = {}
    roots = _scan_roots(plugins, extra_roots)
    for root in roots:
        for path in root.rglob('*'):
            if path.is_symlink() and not _scanned_dll_link(path, roots, managed):
                raise ValueError(f'Symbolic links are not allowed in Plugins: {path}')
        for key, paths in index_plugins(root, exclude=managed).items():
            locations.setdefault(key, []).extend(paths)
    for resource in (RUL0, NETWORK_INI):
        foreign = [path for path in locations.get(resource, [])
                   if Path(path).resolve() != controller]
        if foreign:
            raise ValueError(f'Foreign shared controller/NetworkINI overlay is installed: {foreign[0]}')
        if not locations.get(resource):
            raise ValueError('The pinned NAM controller is missing a required shared resource')


def _locations(output: Path | None, plugins: Path, backup_root: Path, *, extra_roots=None):
    plugins = _root(plugins)
    roots = _scan_roots(plugins, extra_roots)
    backup_root = _root(backup_root, required=False)
    if any(_inside(backup_root, root) or _inside(root, backup_root) for root in roots):
        raise ValueError('Backup root must be outside Plugins and must not contain Plugins')
    if output is not None:
        output = _root(output)
        if any(_inside(output, root) or _inside(root, output) for root in roots):
            raise ValueError('Build output must be outside Plugins and must not contain Plugins')
        if _inside(backup_root, output / FOLDER):
            raise ValueError('Backup root cannot be inside the generated plugin folder')
    if backup_root.exists():
        _tree(backup_root)
    return output, plugins, backup_root


def _replace(managed: Path, staged: Path | None) -> None:
    """Exchange one directory and restore the old one if the exchange fails."""
    holding = managed.parent / f'.scp-previous-{uuid.uuid4().hex}'
    moved = False
    try:
        if managed.exists():
            managed.rename(holding)
            moved = True
        if staged is not None:
            staged.rename(managed)
    except BaseException:
        if moved and not managed.exists():
            holding.rename(managed)
        raise
    if moved:
        shutil.rmtree(holding)


def _exclusive_operation(function):
    """Prevent two installers from racing between validation and rename."""
    parameters = signature(function)

    @wraps(function)
    def wrapped(*args, **kwargs):
        bound = parameters.bind(*args, **kwargs)
        plugins = _root(bound.arguments['plugins'])
        lock = plugins / OPERATION_LOCK
        token = uuid.uuid4().hex
        try:
            with lock.open('x') as stream:
                stream.write(token)
        except FileExistsError as exc:
            raise ValueError(f'Another SCP operation owns {lock}. If no operation is running, inspect and remove this stale lock.') from exc
        try:
            return function(*args, **kwargs)
        finally:
            # Never delete a replacement supplied by somebody else.
            try:
                if not lock.is_symlink() and lock.is_file() and lock.read_text() == token:
                    lock.unlink()
            except OSError:
                pass
    return wrapped


@_exclusive_operation
def install_build(output: Path, plugins: Path, backup_root: Path, *, extra_roots=None) -> dict:
    """Verify, snapshot, and install the manifest's one managed plugin folder."""
    output, plugins, backup_root = _locations(output, plugins, backup_root, extra_roots=extra_roots)
    from .build import verify_build  # Delay the import to avoid a CLI/build cycle.
    verify_build(output)
    manifest = _json(output / 'manifest.json')
    if manifest.get('schema_version') != 1 or manifest.get('plugin_folder') != FOLDER:
        raise ValueError('Unsupported build manifest or plugin folder')
    files = {}
    for item in manifest.get('files', []):
        path = _relative(item['path'])
        prefix = FOLDER + '/'
        if not path.startswith(prefix):
            raise ValueError('Every installable file must be inside the managed plugin folder')
        relative = path[len(prefix):]
        if relative == RECEIPT or relative in files:
            raise ValueError('Reserved or duplicate installable file path')
        files[relative] = item['sha256']
        source = output / path
        if source.is_symlink() or not source.is_file():
            raise ValueError(f'Build file is missing or linked: {path}')
        if source.stat().st_size != item['bytes']:
            raise ValueError(f'Build file size mismatch: {path}')
    files = _hashes(files)
    if _tree(output / FOLDER) != files:
        raise ValueError('Build folder has undeclared, missing or changed files')
    managed = plugins / FOLDER
    previous = _owned(managed)
    piece_ids = sorted({piece['id'] for piece in manifest.get('pieces', [])})
    if previous is not None:
        omitted_ids = set(previous.get('piece_ids', [])) - set(piece_ids)
        previous_files = {name for name in previous['files']
                          if name.startswith('20_Pieces/SCP_') and name.endswith('.dat')}
        current_files = {name for name in files
                         if name.startswith('20_Pieces/SCP_') and name.endswith('.dat')}
        omitted_files = previous_files - current_files
        if omitted_ids or omitted_files:
            omitted = ', '.join(sorted(omitted_ids | omitted_files))
            raise ValueError(f'New build omits installed pieces: {omitted}. '
                             'Keep them selected, or remove their crossings from saved cities '
                             'before uninstalling and reinstalling.')
    controller = _profile(manifest.get('profile'), plugins, managed, extra_roots=extra_roots)
    _foreign_overlays(plugins, managed, controller, extra_roots=extra_roots)

    backup_id = uuid.uuid4().hex
    receipt = {'schema_version': 1, 'plugin_folder': FOLDER, 'backup_id': backup_id,
               'build_manifest_sha256': _sha((output / 'manifest.json').read_bytes()),
               'profile': manifest['profile'], 'files': files, 'piece_ids': piece_ids}
    backup_root.mkdir(parents=True, exist_ok=True)
    backup = backup_root / backup_id
    backup.mkdir()
    staged = None
    try:
        previous_hashes = {}
        if previous is not None:
            shutil.copytree(managed, backup / 'previous' / FOLDER)
            previous_hashes = _tree(backup / 'previous' / FOLDER)
            if previous_hashes != _tree(managed):
                raise ValueError('Existing managed folder changed while it was being backed up')
        staged = Path(tempfile.mkdtemp(prefix='.scp-stage-', dir=plugins))
        for relative in files:
            destination = staged / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(output / FOLDER / relative, destination)
        _write_json(staged / RECEIPT, receipt)
        _owned(staged)
        _write_json(backup / 'backup.json', {
            'schema_version': 1, 'plugin_folder': FOLDER, 'backup_id': backup_id,
            'operation': 'install',
            'previous_state': 'present' if previous is not None else 'absent',
            'previous_files': previous_hashes,
            'installed_receipt_sha256': _sha((staged / RECEIPT).read_bytes())})
        # Recheck immediately before the directory exchange. No existing owned
        # file is overwritten until a complete, hash-checked snapshot exists.
        if _owned(managed) != previous:
            raise ValueError('Managed installation changed while preparing the update')
        _replace(managed, staged)
        staged = None
    except BaseException:
        if staged is not None and staged.exists():
            shutil.rmtree(staged)
        # Keep a complete snapshot if the directory exchange already succeeded.
        if not managed.exists() or not (managed / RECEIPT).exists() or _json(managed / RECEIPT).get('backup_id') != backup_id:
            shutil.rmtree(backup)
        raise
    return {'status': 'installed', 'backup_id': backup_id,
            'plugin_folder': str(managed), 'files': len(files)}


@_exclusive_operation
def uninstall(plugins: Path, backup_root: Path, *, extra_roots=None) -> dict:
    """Snapshot and remove only an unchanged, receipt-owned installation.

    Removal does not load any old overlay, so it remains available after NAM
    changes. Restoring this snapshot through rollback still checks its profile.
    """
    _, plugins, backup_root = _locations(None, plugins, backup_root, extra_roots=extra_roots)
    managed = plugins / FOLDER
    current = _owned(managed)
    if current is None:
        raise ValueError('No managed installation exists to uninstall')
    backup_id = uuid.uuid4().hex
    backup_root.mkdir(parents=True, exist_ok=True)
    backup = backup_root / backup_id
    backup.mkdir()
    try:
        snapshot = backup / 'previous' / FOLDER
        shutil.copytree(managed, snapshot)
        previous_hashes = _tree(snapshot)
        if previous_hashes != _tree(managed):
            raise ValueError('Managed folder changed while it was being backed up')
        _write_json(backup / 'backup.json', {
            'schema_version': 1, 'plugin_folder': FOLDER, 'backup_id': backup_id,
            'operation': 'uninstall', 'previous_state': 'present',
            'previous_files': previous_hashes,
            'removed_receipt_sha256': _sha((snapshot / RECEIPT).read_bytes())})
        if _owned(managed) != current:
            raise ValueError('Managed installation changed while preparing removal')
        _replace(managed, None)
    except BaseException:
        # Retain a complete recovery snapshot if removal already succeeded.
        if managed.exists():
            shutil.rmtree(backup)
        raise
    return {'status': 'uninstalled', 'backup_id': backup_id,
            'plugin_folder': str(managed), 'files': len(current['files'])}


@_exclusive_operation
def rollback_install(plugins: Path, backup_root: Path, backup_id: str, *, extra_roots=None) -> dict:
    """Restore exactly the managed state saved before a particular install."""
    _, plugins, backup_root = _locations(None, plugins, backup_root, extra_roots=extra_roots)
    if not isinstance(backup_id, str) or not re.fullmatch(r'[a-zA-Z0-9_-]+', backup_id):
        raise ValueError('Invalid backup identifier')
    backup = backup_root / backup_id
    _tree(backup)
    metadata = _json(backup / 'backup.json')
    if (metadata.get('schema_version') != 1 or metadata.get('plugin_folder') != FOLDER
            or metadata.get('backup_id') != backup_id
            or metadata.get('previous_state') not in {'present', 'absent'}):
        raise ValueError('Invalid backup metadata')
    managed = plugins / FOLDER
    current = _owned(managed)
    operation = metadata.get('operation', 'install')
    if operation == 'uninstall':
        if current is not None:
            raise ValueError('Uninstall rollback requires the managed folder to remain absent')
        if metadata['previous_state'] != 'present':
            raise ValueError('An uninstall backup must contain the removed installation')
    elif operation == 'install':
        if current is None or current['backup_id'] != backup_id:
            raise ValueError('This backup does not belong to the current managed installation')
        if _sha((managed / RECEIPT).read_bytes()) != metadata.get('installed_receipt_sha256'):
            raise ValueError('Current installation receipt differs from the saved install receipt')
    else:
        raise ValueError('Unknown backup operation')
    staged = None
    try:
        if metadata['previous_state'] == 'present':
            snapshot = backup / 'previous' / FOLDER
            if _tree(snapshot) != _hashes(metadata.get('previous_files')):
                raise ValueError('Backup snapshot has missing, unknown or changed files')
            previous = _owned(snapshot)
            if operation == 'uninstall' and _sha((snapshot / RECEIPT).read_bytes()) != metadata.get('removed_receipt_sha256'):
                raise ValueError('Uninstall backup receipt does not match the removed installation')
            controller = _profile(previous.get('profile'), plugins, managed, extra_roots=extra_roots)
            _foreign_overlays(plugins, managed, controller, extra_roots=extra_roots)
            staged = Path(tempfile.mkdtemp(prefix='.scp-stage-', dir=plugins))
            shutil.copytree(snapshot, staged, dirs_exist_ok=True)
            if _tree(staged) != metadata['previous_files']:
                raise ValueError('Restored staging files do not match the backup')
        elif metadata.get('previous_files') != {} or (backup / 'previous').exists():
            raise ValueError('An absent-state backup contains unexpected previous files')
        if _owned(managed) != current:
            raise ValueError('Managed installation changed while preparing rollback')
        _replace(managed, staged)
        staged = None
    finally:
        if staged is not None and staged.exists():
            shutil.rmtree(staged)
    return {'status': 'rolled_back', 'backup_id': backup_id,
            'plugin_folder': str(managed), 'previous_state': metadata['previous_state']}
