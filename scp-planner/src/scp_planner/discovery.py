"""Discover pairwise compatibility from fresh registered library exports only.

The library owns parsing, declarations, source validation, and export freshness.
Planner qualifies those inputs, calls its existing complete-boundary matcher,
and reports candidates without writing back to the library.
"""
from copy import deepcopy
from itertools import combinations_with_replacement
import json
from pathlib import Path

from ._source import configured_root, source_module
from .metadata import _library, find_matches


def _check_source_root(custom_root):
    """Require data and imported library code to come from the same checkout."""
    code_root = configured_root()
    imported_root = Path(_library.__file__).resolve().parents[2]
    if custom_root != code_root or imported_root != code_root:
        raise ValueError(
            'Discovery code and data roots must match. Set SCP_CUSTOM_PIECES_ROOT '
            'and --custom-pieces-root to the same library directory before starting '
            f'Python (configured code: {code_root}; imported code: {imported_root}; '
            f'data: {custom_root}).')
    return code_root


def _validation_reason(error):
    """Preserve source-owned reason codes; never infer them from error wording."""
    code = getattr(error, 'code', None)
    if isinstance(code, str) and code:
        return code
    if isinstance(error, FileNotFoundError):
        return 'missing_source'
    if isinstance(error, OSError):
        return 'unreadable_source_or_export'
    return 'validation_failed'


def _qualify_piece(custom_root, directory, identifier, domain_id):
    declaration, export = (directory / name for name in
                           ('connector-groups.jsonc', 'connector-data.json'))
    record = {'piece_id': identifier,
              'declaration': declaration.relative_to(custom_root).as_posix(),
              'export': export.relative_to(custom_root).as_posix()}
    if not declaration.exists() and not declaration.is_symlink():
        return {**record, 'status': 'not_migrated',
                'reason': 'missing_connector_declaration',
                'detail': 'No authored connector-groups.jsonc; compatibility was not searched.'}, None, None
    if not declaration.is_file():
        return {**record, 'status': 'excluded', 'reason': 'invalid_declaration_file',
                'detail': 'connector-groups.jsonc is not a readable regular source file.'}, None, None
    if not export.exists() and not export.is_symlink():
        return {**record, 'status': 'excluded', 'reason': 'missing_export',
                'detail': 'Authored declarations exist, but connector-data.json is missing; use the library refresh workflow.'}, None, None
    if not export.is_file():
        return {**record, 'status': 'excluded', 'reason': 'invalid_export_file',
                'detail': 'connector-data.json is not a readable regular export file.'}, None, None
    try:
        loaded = _library.load_exports(custom_root, [identifier], domain_id=domain_id)
    except (ValueError, OSError) as error:
        return {**record, 'status': 'excluded', 'reason': _validation_reason(error),
                'detail': str(error), 'error_type': type(error).__name__}, None, None
    return ({**record, 'status': 'eligible', 'reason': 'fresh_validated_export',
             'detail': 'Library load_exports validated declarations, source bindings, export content, and saved route agreement.'},
            loaded['pieces'][identifier], loaded['exports'][identifier])


def _canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def _deduplicate_matches(matches, first, second, boundary_id=None):
    """Merge group-level rows into complete boundary-pair/pose candidates."""
    first_groups = {group['id']: group['boundary_bundle_id'] for group in first['groups']}
    second_groups = {group['id']: group['boundary_bundle_id'] for group in second['groups']}
    candidates = {}
    for match in matches:
        a_boundary = first_groups[match['a_group_id']]
        b_boundary = second_groups[match['b_group_id']]
        if boundary_id is not None and a_boundary != boundary_id:
            continue
        key = (first['id'], a_boundary, second['id'], b_boundary,
               match['relative_rotation_ccw'], tuple(match['relative_position_m']))
        if key not in candidates:
            candidates[key] = {
                'a_piece_id': first['id'], 'a_boundary_id': a_boundary,
                'b_piece_id': second['id'], 'b_boundary_id': b_boundary,
                'relative_rotation_ccw': match['relative_rotation_ccw'],
                'relative_position_m': list(match['relative_position_m']),
                'bundle_group_pairs': [], 'status': 'candidate',
                'checks': {**deepcopy(match['checks']),
                           'complete_boundary_metadata': 'passed',
                           'full_scene': 'unverified', 'terrain_construction': 'unverified'},
            }
        target = candidates[key]['bundle_group_pairs']
        for pair in match['bundle_group_pairs']:
            existing = next((item for item in target if
                             (item['a_group_id'], item['b_group_id']) ==
                             (pair['a_group_id'], pair['b_group_id'])), None)
            if existing is None:
                target.append(deepcopy(pair))
            else:
                known = {_canonical(member) for member in existing['member_pairs']}
                for member in pair['member_pairs']:
                    if _canonical(member) not in known:
                        existing['member_pairs'].append(deepcopy(member))
                        known.add(_canonical(member))
    for candidate in candidates.values():
        candidate['bundle_group_pairs'].sort(key=lambda pair: (pair['a_group_id'], pair['b_group_id']))
        for pair in candidate['bundle_group_pairs']:
            pair['member_pairs'].sort(key=_canonical)
        candidate['member_pairs'] = [
            {'a_group_id': pair['a_group_id'], 'b_group_id': pair['b_group_id'], **deepcopy(member)}
            for pair in candidate['bundle_group_pairs'] for member in pair['member_pairs']]
    return [candidates[key] for key in sorted(candidates)]


def discover_compatibility(custom_root, *, domain_id='high-speed-rail',
                           query_piece_id=None, query_boundary_id=None):
    """Search every eligible registered type, optionally from one piece/boundary.

    No result limit is applied. Without a query, each unordered type pair is
    searched once, including repeated instances of one type. With a query,
    that type stays fixed at its authored orientation and every eligible type
    is considered as the second instance. Boundaries are always atomic.
    """
    custom_root = Path(custom_root).expanduser().resolve()
    code_root = _check_source_root(custom_root)
    if query_boundary_id is not None and query_piece_id is None:
        raise ValueError('A boundary query requires --piece / query_piece_id.')
    catalog = source_module('catalog').load_catalog(custom_root)
    if domain_id not in catalog['domains']:
        raise ValueError(f'Unknown registered transport domain: {domain_id}')
    domain = custom_root / catalog['domains'][domain_id]['path']
    registered = sorted(piece['id'] for piece in catalog['pieces'] if piece['domain'] == domain_id)
    if query_piece_id is not None and query_piece_id not in registered:
        raise ValueError(f'Unknown registered piece in {domain_id}: {query_piece_id}')
    eligibility, pieces, exports = [], {}, {}
    for identifier in registered:
        directory = domain / '00_pieces' / identifier
        record, piece, export = _qualify_piece(custom_root, directory, identifier, domain_id)
        eligibility.append(record)
        if piece is not None:
            pieces[identifier], exports[identifier] = piece, export
    query = {'piece_id': query_piece_id, 'boundary_id': query_boundary_id,
             'status': 'all_eligible_pairs' if query_piece_id is None else 'eligible'}
    if query_piece_id is not None and query_piece_id not in pieces:
        query['status'] = 'not_eligible'
        query['eligibility'] = next(record for record in eligibility if record['piece_id'] == query_piece_id)
        pairs = []
    elif query_piece_id is not None:
        first = pieces[query_piece_id]
        if query_boundary_id is not None and query_boundary_id not in {
                bundle['id'] for bundle in first['boundary_bundles']}:
            raise ValueError(f'{query_piece_id}: unknown complete boundary: {query_boundary_id}')
        pairs = [(query_piece_id, identifier) for identifier in sorted(pieces)]
    else:
        pairs = list(combinations_with_replacement(sorted(pieces), 2))
    candidates, raw_count = [], 0
    for first, second in pairs:
        raw = find_matches(pieces[first], pieces[second])
        if query_boundary_id is not None:
            boundaries = {group['id']: group['boundary_bundle_id'] for group in pieces[first]['groups']}
            raw = [match for match in raw if boundaries[match['a_group_id']] == query_boundary_id]
        raw_count += len(raw)
        candidates.extend(_deduplicate_matches(raw, pieces[first], pieces[second], query_boundary_id))
    return {
        'schema_version': 1,
        'purpose': 'Discover pairwise complete-boundary metadata and owned-cell candidates from fresh library exports; not a game or physical-fit verdict.',
        'status': 'completed', 'domain_id': domain_id,
        'custom_pieces_root': str(custom_root), 'library_code_root': str(code_root),
        'query': query, 'piece_eligibility': eligibility,
        'eligible_piece_ids': sorted(pieces), 'source_exports': exports,
        'counts': {'registered_pieces': len(registered), 'eligible_pieces': len(pieces),
                   'not_migrated': sum(record['status'] == 'not_migrated' for record in eligibility),
                   'excluded': sum(record['status'] == 'excluded' for record in eligibility),
                   'searched_type_pairs': len(pairs), 'raw_group_matches': raw_count,
                   'boundary_pose_candidates': len(candidates)},
        'candidate_placements': candidates,
        'search_scope': 'Entire eligible set in the selected registered domain; no per-port shortlist, candidate cap, authored-data fallback, or cross-domain search.',
        'placement_convention': 'First instance at authored 0 degrees and [0,0] metres; second anchor and proper rotation are relative to it. Unqueried type pairs use stable sorted IDs once, including self-pairs.',
        'checks_not_established': {name: 'unverified' for name in
                                   ('full_scene', 'physical_seams', 'construction_clearance',
                                    'geometry_collisions', 'terrain_construction', 'in_game')},
        'library_files_changed': False, 'installed': False,
    }
