"""Assess recorded release evidence against a particular build manifest.

The caller must verify the actual build files against the manifest first. This
module reads only project-local release/evidence metadata and checks screenshot
file existence; it does not inspect installed NAM archives or run the game.
Human permission flags remain recorded assertions, not automatic legal proof.
"""
from __future__ import annotations

from datetime import date
import json
from pathlib import Path, PurePosixPath
import re

from .catalog import release_status


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def _portable_error(root, error):
    """Keep failure details without publishing this checkout's absolute root."""
    message = str(error)
    prefix = str(root)
    for value in sorted({prefix, repr(prefix)[1:-1]}, key=len, reverse=True):
        message = message.replace(value, '.')
    return message


def _relative(value):
    _require(isinstance(value, str) and value and '\\' not in value,
             'expected a relative POSIX path')
    path = PurePosixPath(value)
    _require(not path.is_absolute() and '..' not in path.parts and
             str(path) == value and path.parts and ':' not in path.parts[0],
             'unsafe relative path')
    return path


def _project_file(root, value):
    relative = _relative(value)
    target = root.joinpath(*relative.parts)
    # Inspect the supplied path before resolve(), which would hide symlinks.
    current = root
    for part in relative.parts:
        current = current / part
        _require(not current.is_symlink(), 'evidence paths may not contain symbolic links')
    target = target.resolve()
    _require(target.is_relative_to(root), 'evidence path escapes project')
    _require(target.is_file(), 'evidence or screenshot file is missing')
    return target


def _digest(value):
    _require(isinstance(value, str) and re.fullmatch(r'[0-9a-f]{64}', value) is not None,
             'invalid SHA-256 fingerprint')
    return value


def _donors(manifest):
    profile = manifest.get('profile')
    _require(isinstance(profile, dict), 'missing donor profile')
    records = profile.get('donors')
    _require(isinstance(records, list) and records, 'missing donor fingerprints')
    result = {}
    for record in records:
        _require(isinstance(record, dict), 'invalid donor record')
        name = record.get('filename')
        _require(isinstance(name, str) and name and '/' not in name and '\\' not in name,
                 'invalid donor filename')
        _require(name not in result, 'duplicate donor filename')
        result[name] = _digest(record.get('sha256'))
    return result


def _files(manifest):
    records = manifest.get('files')
    _require(isinstance(records, list) and records, 'missing build file fingerprints')
    result = {}
    for record in records:
        _require(isinstance(record, dict), 'invalid build file record')
        name = record.get('path')
        _relative(name)
        _require(name not in result, 'duplicate build file path')
        result[name] = _digest(record.get('sha256'))
    return result


def _check_evidence(root, piece, evidence, files, donors):
    _require(isinstance(evidence, dict), 'game evidence must be a JSON object')
    _require(evidence.get('piece_id') == piece['id'], 'game evidence belongs to another piece')
    asset = piece.get('asset_file')
    _relative(asset)
    _require(asset in files, 'piece asset is absent from build manifest')
    _require(evidence.get('asset_sha256') == files[asset],
             'game evidence asset fingerprint differs from this build')
    _require(isinstance(evidence.get('package_fingerprints'), dict) and
             evidence['package_fingerprints'] == files,
             'game evidence package fingerprints differ from this build')
    _require(isinstance(evidence.get('donor_fingerprints'), dict) and
             evidence['donor_fingerprints'] == donors,
             'game evidence donor fingerprints differ from this build')
    expected = piece.get('game_tests')
    _require(isinstance(expected, dict) and expected and
             all(value == 'passed' for value in expected.values()) and
             evidence.get('case_results') == expected,
             'game evidence must contain exactly the declared passing test cases')
    tester = evidence.get('tester')
    _require(isinstance(tester, str) and tester.strip(), 'game evidence needs a tester')
    tested_on = evidence.get('date')
    _require(isinstance(tested_on, str) and
             re.fullmatch(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', tested_on) is not None,
             'game evidence date must use YYYY-MM-DD')
    try:
        date.fromisoformat(tested_on)
    except ValueError as exc:
        raise ValueError('game evidence date is not a calendar date') from exc
    screenshots = evidence.get('screenshots')
    _require(isinstance(screenshots, list) and screenshots,
             'game evidence needs at least one screenshot')
    for screenshot in screenshots:
        _project_file(root, screenshot)


def assess_build(project_root: Path, manifest: dict) -> dict:
    """Return fail-closed release readiness for the manifest's selected pieces.

    Each ``game_evidence`` reference is relative to ``project_root``. The
    evidence binds every packaged DAT and the complete declared donor profile;
    it does not replace verification of files or establish permission itself.
    """
    root = Path(project_root).resolve()
    blocked = []
    try:
        _require(isinstance(manifest, dict), 'manifest must be a JSON object')
        pieces = manifest.get('pieces')
        _require(isinstance(pieces, list) and pieces and
                 all(isinstance(piece, dict) and isinstance(piece.get('id'), str) and
                     piece['id'] for piece in pieces), 'missing selected pieces')
        files, donors = _files(manifest), _donors(manifest)
    except (TypeError, ValueError) as exc:
        return {'public_release_ready': False, 'blocked': [f'build evidence metadata: {exc}']}

    try:
        blocked.extend(release_status(root, pieces)['blocked'])
    except (OSError, ValueError, KeyError, TypeError, AttributeError):
        blocked.append('project release gates are missing or invalid')

    # Current projects have one authoritative record per subject. A coarse
    # flag in an older candidate must never hide a failed or untested port.
    if (root/'project.jsonc').is_file():
        try:
            from .catalog import load_catalog, safe_relative
            from .content import summarize_manual_record
            current = load_catalog(root)
            registered = {piece['id']: piece for piece in current['pieces']}
            for piece in pieces:
                source = registered[piece['id']]
                domain = current['domains'][source['domain']]
                relative = str(Path(domain['path'])/'00_pieces'/source['id']/'checks/manual-tests.json')
                path = safe_relative(root, relative)
                record = json.loads(path.read_text())
                _require(record['subject'] == {'id': source['id'], 'kind': 'piece'},
                         'manual record identifies another subject')
                summary = summarize_manual_record(record)
                for kind, counts in summary['by_kind'].items():
                    if kind.startswith('software_'):
                        continue
                    pending = sum(counts.get(state, 0) for state in ('unverified', 'failed', 'stale'))
                    if pending:
                        blocked.append(f"{source['id']}: {kind}: {pending} current manual cases need confirmation")
        except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
            blocked.append(f'authoritative manual coverage is missing or invalid ({_portable_error(root, exc)})')

    for piece in pieces:
        reference = piece.get('game_evidence')
        if not reference:
            blocked.append(f"{piece['id']}: game_evidence is not recorded")
            continue
        try:
            path = _project_file(root, reference)
            evidence = json.loads(path.read_text())
            _check_evidence(root, piece, evidence, files, donors)
        except (OSError, ValueError, KeyError, TypeError) as exc:
            blocked.append(f"{piece['id']}: game evidence invalid ({_portable_error(root, exc)})")
    return {'public_release_ready': not blocked, 'blocked': blocked}

