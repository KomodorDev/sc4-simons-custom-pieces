#!/usr/bin/env python3
"""Checked additive merge of CLI-generated Scoty staging records and folders.

Default is read-only validation and a JSON plan. --apply creates a timestamped
backup and commits only new sc4pac folders/records. It never rebuilds catalogues.
Run from any directory; no third-party Python packages are required.
"""
from __future__ import annotations

import argparse
import copy
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys
import tempfile
from urllib.parse import quote, unquote, urlsplit
import uuid

TASK = Path(__file__).resolve().parent
WORKSPACE = TASK.parent.parent
ACTIVE = Path('/Users/simonhinterreiter/Library/Application Support/io.github.memo33.sc4pac/profiles/1')
STAGING = TASK / 'staging-profile'
TARGET = 'local-scoty:walls-sets'
CONFIG_NAME = 'sc4pac-plugins.json'
LOCK_NAME = 'sc4pac-plugins-lock.json'
CATALOGUES = ('lots.cbor', 'props.cbor', 'flora.cbor', 'lot_thumbnails.bin',
              'prop_thumbnails.bin', 'flora_thumbnails.bin')


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def snapshot(root, allow_existing_file_symlinks=False):
    require(root.is_dir(), f'Missing directory: {root}')
    result = {}
    for path in sorted(root.rglob('*')):
        require(not path.is_symlink() or (allow_existing_file_symlinks and path.is_file()),
                f'Refusing new, broken, or directory symbolic link in payload: {path}')
        if path.is_file():
            result[path.relative_to(root).as_posix()] = sha(path)
    return result


def json_bytes(obj):
    return (json.dumps(obj, indent=2, ensure_ascii=False) + '\n').encode('utf-8')


def atomic_write(path, data):
    mode = path.stat().st_mode & 0o777 if path.exists() else 0o644
    fd, name = tempfile.mkstemp(prefix='.' + path.name + '.', dir=path.parent)
    temp = Path(name)
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        temp.chmod(mode)
        os.replace(temp, path)
    finally:
        temp.unlink(missing_ok=True)


def quiescent():
    # Read-only process inspection. Any Wine process is treated conservatively as
    # a possibly live SC4 instance. Detect both GUI and CLI sc4pac processes.
    rows = subprocess.run(['ps', '-axo', 'pid=,comm=,args='], check=True,
                          text=True, capture_output=True).stdout.splitlines()
    blocked = []
    for line in rows:
        parts = line.strip().split(None, 1)
        if not parts or int(parts[0]) == os.getpid():
            continue
        details = parts[1].lower() if len(parts) > 1 else ''
        if (re.search(r'(^|[ /])(?:wine(?:32on64-preloader|64-preloader|server|skinlauncher)?|sc4scrollhelper)(?:[ /]|$)', details)
                or re.search(r'simcity\s*4(?:\.exe|\s|/|$)', details)
                or 'sc4pac-cli' in details
                or 'sc4pac mod manager.app/' in details
                or re.search(r'(^|/)sc4pac(?:\.app/|\s|$)', details)):
            blocked.append(line.strip())
    require(not blocked, 'Close SimCity 4/Wine and sc4pac GUI/CLI before merging:\n' + '\n'.join(blocked))


def keyed(records, kind):
    def key(record):
        if kind == 'package':
            return record['group'] + ':' + record['name']
        return record['assetId']
    result = {}
    for record in records:
        k = key(record)
        require(k not in result, f'Duplicate {kind} record: {k}')
        result[k] = record
    return result


def managed_path(value):
    p = PurePosixPath(value)
    require(not p.is_absolute() and '..' not in p.parts and '.' not in p.parts,
            f'Unsafe manager path: {value}')
    require(len(p.parts) >= 2 and p.name.endswith('.sc4pac'),
            f'New payload is not a manager folder; review manually: {value}')
    return Path(*p.parts)


def within(path, root):
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def archives_for(assets, stage_config, extra):
    """Resolve actual staged asset inputs using local URLs, download receipts, or cache."""
    receipt_by_id = {}
    receipt_by_url = {}
    for p in sorted((TASK / 'downloads').rglob('*.json')):
        try:
            obj = json.loads(p.read_text())
        except (ValueError, OSError):
            continue
        for item in obj if isinstance(obj, list) else [obj]:
            if isinstance(item, dict) and item.get('path'):
                if item.get('assetId'):
                    receipt_by_id[item['assetId']] = Path(item['path'])
                if item.get('url'):
                    receipt_by_url[item['url']] = Path(item['path'])
    cache = Path(stage_config['config']['cacheRoot']) / 'coursier'
    paths = []
    mapping = []
    for asset in assets:
        url = asset['url']
        parts = urlsplit(url)
        candidates = []
        if parts.scheme == 'file':
            require(parts.netloc in ('', 'localhost'), f'Unsupported file URL host: {url}')
            candidates.append(Path(unquote(parts.path)))
        candidates.extend(p for p in (receipt_by_id.get(asset['assetId']), receipt_by_url.get(url)) if p)
        if parts.scheme in ('http', 'https'):
            # Coursier percent-escapes URL punctuation in its cache filename.
            tail = parts.path.lstrip('/') + (('?' + parts.query) if parts.query else '')
            candidates.append(cache / parts.scheme / parts.netloc / quote(tail, safe='/.-_~'))
        existing = next((p for p in candidates if p.is_file() and not p.is_symlink()), None)
        require(existing is not None,
                f'Cannot find source archive for {asset["assetId"]} ({url}); preserve it and its download receipt first.')
        paths.append(existing.resolve())
        mapping.append({'assetId': asset['assetId'], 'source': str(existing.resolve()), 'url': url})
    paths.extend(Path(p).expanduser().resolve() for p in extra)
    prep = TASK / 'preparation.json'
    if prep.exists():
        obj = json.loads(prep.read_text())
        for key in ('downloadedArchive', 'preservedArchive'):
            if obj.get(key) and Path(obj[key]).is_file():
                paths.append(Path(obj[key]).resolve())
    unique = sorted(set(paths), key=str)
    require(all(p.is_file() and not p.is_symlink() for p in unique), 'An archive input is missing or is a symlink.')
    return unique, mapping


def verify_prior(before, after):
    changed = [name for name, digest in before.items() if after.get(name) != digest]
    require(not changed, 'Pre-existing plugin files changed/missing: ' + ', '.join(changed[:20]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true', help='Commit after validation; otherwise read-only dry run.')
    parser.add_argument('--archive', action='append', default=[], help='Additional original archive to back up (repeatable).')
    args = parser.parse_args()
    quiescent()
    paths = {('active', n): ACTIVE / n for n in (CONFIG_NAME, LOCK_NAME)}
    paths.update({('stage', n): STAGING / n for n in (CONFIG_NAME, LOCK_NAME)})
    raw = {k: p.read_bytes() for k, p in paths.items()}
    docs = {k: json.loads(v) for k, v in raw.items()}
    active_config, active_lock = docs['active', CONFIG_NAME], docs['active', LOCK_NAME]
    stage_config, stage_lock = docs['stage', CONFIG_NAME], docs['stage', LOCK_NAME]
    plugins = Path(active_config['config']['pluginsRoot']).resolve()
    staged = Path(stage_config['config']['pluginsRoot']).resolve()
    require(plugins != staged, 'Staged plugins must be separate from active plugins.')
    require(within(staged, TASK), 'Unexpected staging payload directory.')
    require(active_lock['scheme'] == stage_lock['scheme'], 'Lock schemes differ.')
    require(active_config['config'].get('variant', {}) == stage_config['config'].get('variant', {}),
            'Active/staged variant configurations differ; reconcile first.')
    require(active_config['config'].get('channels') == stage_config['config'].get('channels'),
            'Active/staged channels differ; reconcile first.')
    old_packages = keyed(active_lock['installed'], 'package')
    staged_packages = keyed(stage_lock['installed'], 'package')
    old_assets = keyed(active_lock['assets'], 'asset')
    staged_assets = keyed(stage_lock['assets'], 'asset')
    require(TARGET in staged_packages, f'{TARGET} is not in the completed staging lock.')
    require(TARGET not in old_packages and TARGET not in active_config['explicit'], 'Target already installed/requested; refusing repeat merge.')
    shared = sorted(set(old_packages) & set(staged_packages))
    for name in shared:
        a, b = old_packages[name], staged_packages[name]
        require(a['version'] == b['version'], f'Shared package version mismatch: {name}')
        require(a.get('variant', {}) == b.get('variant', {}), f'Shared package variant mismatch: {name}')
        require(a.get('files', []) == b.get('files', []), f'Shared package managed paths differ: {name}')
    for name in sorted(set(old_assets) & set(staged_assets)):
        require(old_assets[name]['version'] == staged_assets[name]['version'], f'Shared asset version mismatch: {name}')
        require(old_assets[name]['url'] == staged_assets[name]['url'], f'Shared asset URL mismatch: {name}')
    new_packages = [p for p in stage_lock['installed'] if p['group'] + ':' + p['name'] not in old_packages]
    new_assets = [a for a in stage_lock['assets'] if a['assetId'] not in old_assets]
    folders = []
    for package in new_packages:
        for value in package.get('files', []):
            rel = managed_path(value)
            require(rel not in folders, f'New packages share a managed folder: {rel}')
            require(not (plugins / rel).exists(), f'Destination already exists: {plugins / rel}')
            require(within(staged / rel, staged) and (staged / rel).is_dir(), f'Missing/unsafe staged folder: {rel}')
            require(within(plugins / rel, plugins), f'Unsafe destination: {rel}')
            folders.append(rel)
    require(folders, 'No new manager folders to install.')
    for a in folders:
        require(not any(a != b and a in b.parents for b in folders), 'Managed folders overlap.')
    for name in CATALOGUES:
        require((plugins / name).is_file(), f'Expected catalogue backup file missing: {name}')
    payload = {rel.as_posix(): snapshot(staged / rel) for rel in folders}
    before = snapshot(plugins, allow_existing_file_symlinks=True)
    archives, archive_assets = archives_for(new_assets, stage_config, args.archive)
    archive_hashes = {str(p): sha(p) for p in archives}
    merged_config = copy.deepcopy(active_config)
    merged_config['explicit'].append(TARGET)
    merged_lock = copy.deepcopy(active_lock)
    merged_lock['installed'].extend(copy.deepcopy(new_packages))
    merged_lock['assets'].extend(copy.deepcopy(new_assets))
    plan = {
        'mode': 'apply' if args.apply else 'dry-run',
        'target': TARGET,
        'packageCountBefore': len(old_packages),
        'packageCountAfter': len(merged_lock['installed']),
        'sharedPackagesVerified': shared,
        'newPackages': [p['group'] + ':' + p['name'] for p in new_packages],
        'newAssets': [a['assetId'] for a in new_assets],
        'managedFolders': [str(p) for p in folders],
        'newPayloadFileCount': sum(len(x) for x in payload.values()),
        'priorPluginFileCount': len(before),
        'archiveInputs': archive_assets,
        'archiveSha256': archive_hashes,
        'catalogueStatus': 'untouched; rebuild separately after successful merge',
    }
    if not args.apply:
        print(json.dumps(plan, indent=2))
        return
    stamp = datetime.now().astimezone().strftime('%Y%m%d-%H%M%S')
    backup = TASK / ('before-' + stamp + '-' + uuid.uuid4().hex[:6])
    backup.mkdir()
    (backup / 'archives').mkdir()
    for name in (CONFIG_NAME, LOCK_NAME):
        (backup / name).write_bytes(raw['active', name])
    for name in CATALOGUES:
        shutil.copy2(plugins / name, backup / name)
        require(sha(backup / name) == before[name], f'Catalogue changed during backup: {name}')
    (backup / 'plugin-sha256.json').write_bytes(json_bytes(before))
    (backup / 'merge-plan.json').write_bytes(json_bytes(plan))
    copied_archives = {}
    for path in archives:
        digest = archive_hashes[str(path)]
        if digest not in copied_archives:
            target = backup / 'archives' / (digest[:12] + '-' + path.name)
            shutil.copy2(path, target)
            require(sha(target) == digest, f'Archive changed during backup: {path}')
            copied_archives[digest] = str(target.relative_to(backup))
    (backup / 'archive-backup-index.json').write_bytes(json_bytes({str(p): copied_archives[archive_hashes[str(p)]] for p in archives}))
    scratch = plugins / ('.scoty-merge-' + uuid.uuid4().hex)
    created_parents = []
    installed_folders = []
    written_profiles = []
    scratch.mkdir()
    try:
        # Prepare and hash all copies before the commit. Existing paths are not touched.
        for number, rel in enumerate(folders):
            temporary = scratch / str(number)
            shutil.copytree(staged / rel, temporary)
            require(snapshot(temporary) == payload[rel.as_posix()], f'Staged payload changed while copying: {rel}')
        quiescent()
        for key, path in paths.items():
            require(path.read_bytes() == raw[key], f'Profile changed since validation: {path}')
        current = snapshot(plugins, allow_existing_file_symlinks=True)
        current = {k: v for k, v in current.items() if not k.startswith(scratch.name + '/')}
        require(current == before, 'Active plugin files changed since validation.')
        for number, rel in enumerate(folders):
            destination = plugins / rel
            require(not destination.exists(), f'Destination appeared during validation: {destination}')
            needed = []
            parent = destination.parent
            while not parent.exists():
                needed.append(parent)
                parent = parent.parent
            for parent in reversed(needed):
                parent.mkdir()
                created_parents.append(parent)
            os.rename(scratch / str(number), destination)
            installed_folders.append(destination)
        scratch.rmdir()
        atomic_write(ACTIVE / LOCK_NAME, json_bytes(merged_lock))
        written_profiles.append(LOCK_NAME)
        atomic_write(ACTIVE / CONFIG_NAME, json_bytes(merged_config))
        written_profiles.append(CONFIG_NAME)
        actual_lock = json.loads((ACTIVE / LOCK_NAME).read_bytes())
        actual_config = json.loads((ACTIVE / CONFIG_NAME).read_bytes())
        require(actual_lock == merged_lock and actual_config == merged_config, 'Committed profiles failed verification.')
        require(actual_lock['installed'][:len(active_lock['installed'])] == active_lock['installed'], 'Prior installed records changed.')
        require(actual_lock['assets'][:len(active_lock['assets'])] == active_lock['assets'], 'Prior asset records changed.')
        after = snapshot(plugins, allow_existing_file_symlinks=True)
        verify_prior(before, after)
        expected_new = {f'{rel}/{name}': digest for rel, files in payload.items() for name, digest in files.items()}
        require({k: v for k, v in after.items() if k not in before} == expected_new, 'Added payload verification failed.')
        plan.update({
            'status': 'installed', 'installedAt': datetime.now(timezone.utc).isoformat(),
            'backup': str(backup), 'priorFilesVerifiedUnchanged': len(before),
            'priorNonCatalogueFilesVerifiedUnchanged': len(set(before) - set(CATALOGUES)),
            'priorPackageRecordsVerifiedUnchanged': len(active_lock['installed']),
            'priorAssetRecordsVerifiedUnchanged': len(active_lock['assets']),
        })
        atomic_write(TASK / 'installation-verification.json', json_bytes(plan))
        print(json.dumps(plan, indent=2))
    except BaseException as exc:
        errors = []
        for name in reversed(written_profiles):
            try:
                atomic_write(ACTIVE / name, raw['active', name])
            except BaseException as err:
                errors.append(f'Profile rollback {name}: {err}')
        for folder in reversed(installed_folders):
            try:
                shutil.rmtree(folder)
            except BaseException as err:
                errors.append(f'Folder rollback {folder}: {err}')
        if scratch.exists():
            try:
                shutil.rmtree(scratch)
            except BaseException as err:
                errors.append(f'Scratch rollback: {err}')
        for parent in reversed(created_parents):
            try:
                parent.rmdir()
            except OSError as err:
                errors.append(f'Parent rollback {parent}: {err}')
        try:
            verify_prior(before, snapshot(plugins, allow_existing_file_symlinks=True))
        except BaseException as err:
            errors.append(str(err))
        status = {'status': 'rolled-back' if not errors else 'rollback-needs-review',
                  'error': str(exc), 'rollbackErrors': errors, 'backup': str(backup)}
        (backup / 'rollback-result.json').write_bytes(json_bytes(status))
        print(json.dumps(status, indent=2), file=sys.stderr)
        raise


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(f'ERROR: {error}', file=sys.stderr)
        sys.exit(1)
