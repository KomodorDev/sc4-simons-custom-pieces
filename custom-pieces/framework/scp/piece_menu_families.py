"""Declarative alternative-piece Tab families in otherwise normal builds.

Only the generated Ordering rows and redundant member presentations change.
Construction definitions and native bytes remain reversible. An unselected
anchor is inert: a separately selected member retains its standalone button.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import re

from .catalog import number
from .dbpf import require
from .menu import MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION
from .rul0 import ORDERING_BEGIN, ORDERING_END, with_feature_sequence

KEY = 'piece_menu_families'
PREFIXES = (MENU_EXEMPLAR, ICON, TITLE, DESCRIPTION)
SLUG = re.compile(r'[a-z][a-z0-9-]{1,63}')


def declarations(pieces, *, available=None):
    """Validate declarations and return active families in selected order.

    Builders supply the entire catalogue as ``available`` to reject unknown
    anchors even in a member-only selection. Portable saved-build verification
    has only its selected definitions; an absent anchor then has no effect.
    Nested anchors are deliberately unsupported, which also excludes cycles.
    """
    require(isinstance(pieces, (list, tuple)), 'Menu families require piece definitions')
    universe = pieces if available is None else available
    require(isinstance(universe, (list, tuple)), 'Menu family catalogue must be a list')
    by_id = {}
    for piece in universe:
        require(isinstance(piece, dict) and isinstance(piece.get('id'), str)
                and SLUG.fullmatch(piece['id']) is not None,
                'Menu family has a malformed piece identifier')
        require(piece['id'] not in by_id, 'Duplicate menu family piece identifier')
        by_id[piece['id']] = piece
    selected = {}
    for piece in pieces:
        require(isinstance(piece, dict) and piece.get('id') in by_id
                and piece['id'] not in selected, 'Duplicate or unknown selected menu family piece')
        source = by_id[piece['id']]
        require(piece.get('domain', 'high-speed-rail') == source.get('domain', 'high-speed-rail')
                and piece.get('puzzle_id') == source.get('puzzle_id')
                and piece.get('menu', {}) == source.get('menu', {}),
                'Selected menu family declaration differs from its catalogue definition')
        selected[piece['id']] = piece
    for piece in universe:
        menu = piece.get('menu', {})
        require(isinstance(menu, dict), 'Malformed piece menu declaration')
        if 'family_anchor' not in menu:
            continue
        anchor = menu['family_anchor']
        require(isinstance(anchor, str) and SLUG.fullmatch(anchor) is not None,
                'Malformed menu family anchor')
        require(anchor != piece['id'], 'A menu family cannot anchor itself')
        target = by_id.get(anchor)
        require(target is not None or available is None, 'Unknown menu family anchor')
        if target is not None:
            require(piece.get('domain', 'high-speed-rail') == target.get('domain', 'high-speed-rail'),
                    'Menu family anchor is in a different domain')
            require(isinstance(target.get('menu', {}), dict), 'Malformed anchor menu declaration')
            require('family_anchor' not in target.get('menu', {}),
                    'Chained or cyclic menu family anchors are unsupported')
    groups = []
    for piece in pieces:
        if 'family_anchor' in piece.get('menu', {}):
            continue
        members = [other for other in pieces
                   if other.get('menu', {}).get('family_anchor') == piece['id']]
        if members:
            family = [piece, *members]
            roots = [number(member['puzzle_id']) for member in family]
            menus = [number(member['menu']['id']) for member in family]
            require(len(set(roots)) == len(roots) and len(set(menus)) == len(menus),
                    'Duplicate menu family construction or presentation identifier')
            groups.append(family)
    return groups


def manifest_record(pieces):
    groups = declarations(pieces)
    return ({'schema_version': 1, 'families': [
        {'anchor_id': group[0]['id'], 'member_ids': [piece['id'] for piece in group]}
        for group in groups]} if groups else None)


def hidden_members(pieces):
    return {piece['id'] for group in declarations(pieces) for piece in group[1:]}


def _rows(insertion):
    """Strict scanner independent of the Ordering transformation helper."""
    require(isinstance(insertion, str), 'Missing piece family Ordering insertion')
    lines = insertion.splitlines(keepends=True)
    starts = [index for index, line in enumerate(lines) if line.strip() == ORDERING_BEGIN]
    ends = [index for index, line in enumerate(lines) if line.strip() == ORDERING_END]
    require(len(starts) == len(ends) == 1 and starts[0] < ends[0]
            and all(not line.strip() for line in lines[:starts[0]]) and ends[0] == len(lines) - 1,
            'Malformed piece family Ordering markers')
    rows, states = [], set()
    for index in range(starts[0] + 1, ends[0]):
        active = lines[index].split(';', 1)[0].strip()
        match = re.fullmatch(r'(RotationRing|AddTypes)\s*=\s*(.+)', active, re.I)
        require(match is not None, 'Unexpected piece family Ordering property')
        tokens = [token.strip() for token in match[2].split(',')]
        require(len(tokens) == 8 and all(re.fullmatch(r'(?:0x)?[0-9a-f]{1,8}', token, re.I)
                                        for token in tokens), 'Malformed piece family rotation row')
        row = [int(token, 16) for token in tokens]
        require(len(set(row)) == 8 and not states.intersection(row),
                'Duplicate piece family rotation state')
        states.update(row)
        rows.append((index, match[1].lower(), row))
    require(rows, 'Missing piece family rotation rows')
    return lines, rows


def _replace_keyword(line, keyword):
    return re.sub(r'^(\s*)(?:RotationRing|AddTypes)\b', lambda match: match[1] + keyword,
                  line, count=1, flags=re.I)


def apply(controller, composition, menus, pieces, *, available=None):
    """Build declared alternatives while retaining each member's own assets."""
    groups = declarations(pieces, available=available)
    if not groups:
        return controller, composition, menus, None
    require(KEY not in composition, 'Piece menu families are already composed')
    roots = [[number(piece['puzzle_id']) for piece in group] for group in groups]
    changed, metadata = with_feature_sequence(controller, composition,
                                               [root for group in roots for root in group])
    insertion = metadata['ordering_insertion']
    lines, rows = _rows(insertion)
    anchors = {group[0] for group in roots}
    for index, _keyword, states in rows:
        if states[0] in anchors:
            lines[index] = _replace_keyword(lines[index], 'RotationRing')
    updated = ''.join(lines)
    changed = changed.replace(insertion.encode('ascii'), updated.encode('ascii'), 1)
    metadata.pop('feature_sequence')
    metadata.update(ordering_insertion=updated)
    metadata[KEY] = {'schema_version': 1, 'groups': roots,
                     'previous_ordering_insertion': composition['ordering_insertion'],
                     'previous_controller_sha256': hashlib.sha256(controller).hexdigest()}
    result = dict(menus)
    for group in groups:
        for piece in group[1:]:
            for prefix in PREFIXES:
                key = (*prefix, number(piece['menu']['id']))
                require(key in result, 'Missing redundant family member presentation')
                del result[key]
    return changed, metadata, result, manifest_record(pieces)


def _restore(controller, composition):
    """Check and undo one exact family-only Ordering replacement."""
    require(isinstance(controller, bytes) and isinstance(composition, dict),
            'Piece menu families require controller bytes and metadata')
    metadata = composition.get(KEY)
    require(isinstance(metadata, dict) and set(metadata) == {
        'schema_version', 'groups', 'previous_ordering_insertion', 'previous_controller_sha256'}
        and type(metadata['schema_version']) is int and metadata['schema_version'] == 1,
        'Malformed piece menu family evidence')
    groups = metadata['groups']
    require(type(groups) is list and groups and all(type(group) is list and len(group) >= 2
            and all(type(root) is int and 0 <= root <= 0xFFFFFFFF for root in group)
            for group in groups), 'Malformed piece menu family root metadata')
    insertion = composition.get('ordering_insertion')
    previous = metadata['previous_ordering_insertion']
    _rows(insertion); _rows(previous)
    require(controller.count(insertion.encode('ascii')) == 1,
            'Missing or nonunique piece family Ordering insertion')
    restored = controller.replace(insertion.encode('ascii'), previous.encode('ascii'), 1)
    require(hashlib.sha256(restored).hexdigest() == metadata['previous_controller_sha256'],
            'Piece menu family evidence does not restore the original controller')
    original = {key: deepcopy(value) for key, value in composition.items() if key != KEY}
    original['ordering_insertion'] = previous
    return restored, original


def verify(controller, composition, pieces, record):
    """Independently check declarations, actual rows, and reversible evidence.

    Return the plain controller/composition for the pre-existing construction
    verifier. This never uses ``apply`` or its transformation as expected truth.
    """
    if record is None and KEY not in composition and not any(
            'family_anchor' in piece.get('menu', {}) for piece in pieces):
        return controller, composition, None
    expected = manifest_record(pieces)
    require(record is None or isinstance(record, dict) and type(record.get('schema_version')) is int,
            'Malformed piece menu family manifest')
    require(record == expected, 'Piece menu family manifest differs from selected declarations')
    if expected is None:
        require(KEY not in composition, 'Unexpected piece menu family composition')
        return controller, composition, None
    restored, original = _restore(controller, composition)
    groups = declarations(pieces)
    roots = [[number(piece['puzzle_id']) for piece in group] for group in groups]
    require(composition[KEY]['groups'] == roots,
            'Piece menu family roots differ from selected declarations')
    old_lines, old_rows = _rows(original['ordering_insertion'])
    new_lines, new_rows = _rows(composition['ordering_insertion'])
    expected_rows = [[number(piece['puzzle_id']) + turn * 0x10000 for turn in range(8)]
                     for piece in pieces]
    require([row for _, keyword, row in old_rows if keyword == 'rotationring'] == expected_rows
            and all(keyword == 'rotationring' for _, keyword, _ in old_rows),
            'Original piece family rows differ from selected construction states')
    selected = {root for group in roots for root in group}
    by_root = {row[0]: (index, row) for index, _keyword, row in old_rows}
    first = min(index for index, _keyword, row in old_rows if row[0] in selected)
    wanted = []
    for index, line in enumerate(old_lines):
        if index == first:
            for group in roots:
                for position, root in enumerate(group):
                    wanted.append(_replace_keyword(old_lines[by_root[root][0]],
                                  'RotationRing' if position == 0 else 'AddTypes'))
        if index not in {by_root[root][0] for root in selected}:
            wanted.append(line)
    require(''.join(new_lines) == ''.join(wanted),
            'Actual piece menu family changes unrelated rows, order, states, or keywords')
    require([row for _, _, row in new_rows] and len(new_rows) == len(old_rows),
            'Piece menu family loses construction rows')
    return restored, original, {'families': len(groups), 'hidden_member_buttons': len(hidden_members(pieces)),
                                'native_and_construction_bytes_preserved': True,
                                'in_game_menu_tested': False}


def with_feature_sequence_preserving_families(controller, composition, base_states):
    """Add a disjoint assembly family without disturbing piece alternatives.

    Assembly builders still independently compare their original/final rows
    and re-verify the frozen normal build, including its declarations.
    """
    require(isinstance(controller, bytes) and isinstance(composition, dict),
            'Feature sequence requires controller bytes and composition metadata')
    if KEY not in composition:
        return with_feature_sequence(controller, composition, base_states)
    require('feature_sequence' not in composition and 'feature_sequences' not in composition,
            'Cannot nest assembly feature sequences')
    _restore(controller, composition)
    lines, rows = _rows(composition['ordering_insertion'])
    groups = composition[KEY]['groups']
    require(isinstance(groups, list) and groups and all(
        isinstance(group, list) and len(group) >= 2 and all(type(root) is int for root in group)
        for group in groups), 'Malformed preserved piece menu family roots')
    protected = {root for group in groups for root in group}
    require(len(protected) == sum(len(group) for group in groups),
            'Preserved piece menu families overlap')
    require(isinstance(base_states, (list, tuple))
            and all(type(root) is int for root in base_states), 'Invalid assembly family roots')
    require(not protected.intersection(base_states),
            'Assembly selection overlaps a declared alternative-piece family')
    by_root = {states[0]: (index, keyword, states) for index, keyword, states in rows}
    continuations = {root for group in groups for root in group[1:]}
    require({states[0] for _, keyword, states in rows if keyword == 'addtypes'} == continuations,
            'Preserved piece family AddTypes rows differ from declared roots')
    for group in groups:
        require(all(root in by_root for root in group), 'Missing preserved piece family row')
        indices = [by_root[root][0] for root in group]
        require(indices == list(range(indices[0], indices[0] + len(group)))
                and by_root[group[0]][1] == 'rotationring',
                'Preserved piece menu family is not contiguous and anchored')
    for index, keyword, _states in rows:
        if keyword == 'addtypes':
            lines[index] = _replace_keyword(lines[index], 'RotationRing')
    plain = ''.join(lines)
    original_insert = composition['ordering_insertion']
    normalized = controller.replace(original_insert.encode('ascii'), plain.encode('ascii'), 1)
    normal_meta = {key: deepcopy(value) for key, value in composition.items() if key != KEY}
    normal_meta['ordering_insertion'] = plain
    changed, metadata = with_feature_sequence(normalized, normal_meta, base_states)
    insertion = metadata['ordering_insertion']
    lines, rows = _rows(insertion)
    for index, _keyword, states in rows:
        if states[0] in continuations:
            lines[index] = _replace_keyword(lines[index], 'AddTypes')
    updated = ''.join(lines)
    changed = changed.replace(insertion.encode('ascii'), updated.encode('ascii'), 1)
    metadata['ordering_insertion'] = updated
    metadata[KEY] = deepcopy(composition[KEY])
    metadata['feature_sequence']['previous_ordering_insertion'] = original_insert
    metadata['feature_sequence']['previous_controller_sha256'] = hashlib.sha256(controller).hexdigest()
    return changed, metadata
