"""Consume source-owned exports and compare complete boundaries under one pose.

Source parsing, schema validation, physical-channel declarations, and exports
belong to SCP. This application adds pairwise placement matching only. A route
candidate does not establish physical clearance or operation inside SimCity 4.
"""
from copy import deepcopy
from ._source import source_module

_library = source_module('connector_metadata')
EPS, ROTATIONS = _library.EPS, _library.ROTATIONS
NORMALS, EDGES, LIMITATIONS = _library.NORMALS, _library.EDGES, _library.LIMITATIONS
_need, _validated, _close = _library._need, _library._validated, _library._close
rotate = _library.rotate
resolve_profiles, validate_piece = _library.resolve_profiles, _library.validate_piece
load_library = _library.load_library


def load_pilot(custom_root, piece_ids, domain_id='high-speed-rail'):
    """Read fresh generated connector-data.json exports through SCP's API."""
    return _library.load_exports(custom_root, piece_ids, domain_id=domain_id)


def _unique_bijection(first, second, compare):
    """Return one unambiguous complete mapping, or None; raw IDs are irrelevant."""
    if len(first) != len(second):
        return None
    solutions = []

    def visit(pending, remaining, pairs):
        if len(solutions) > 1:
            return
        if not pending:
            solutions.append(pairs)
            return
        for index, other in enumerate(remaining):
            match = compare(pending[0], other)
            if match is not None:
                visit(pending[1:], remaining[:index]+remaining[index+1:], pairs+[match])
    visit(first, second, [])
    return solutions[0] if len(solutions) == 1 else None


def _cut_pairs(first, second, angle, offset):
    """Compare normalized per-mode permissions, retaining raw-member provenance."""
    pairs, covered = [], set()
    for port in first:
        for mode in port['traffic_modes']:
            compatible = []
            for other in second:
                if mode not in other['traffic_modes'] or port['direction'] == other['direction']:
                    continue
                if any(port[key] != other[key] for key in ('service_network', 'engine_transport', 'role')):
                    continue
                point = rotate(other['endpoint_m'], angle)
                point[:2] = [point[i]+offset[i] for i in (0, 1)]
                if _close(port['endpoint_m'], point) and _close(port['tangent'], rotate(other['tangent'], angle)) and abs(port['grade']-other['grade']) <= EPS:
                    compatible.append(other)
            if not compatible:
                return None
            for other in compatible:
                covered.add((other['id'], mode))
                pair = {'a_port_id': port['id'], 'b_port_id': other['id'],
                        'a_source_port_id': port['source_port_id'], 'b_source_port_id': other['source_port_id']}
                if pair not in pairs:
                    pairs.append(pair)
    if covered != {(p['id'], mode) for p in second for mode in p['traffic_modes']}:
        return None
    return pairs


def _boundary_pairs(aa, bb, angle, offset):
    """Compare atomic edges; authoring group partitions do not control matching."""
    first, second = aa[0], bb[0]
    if not _close(first['outward_normal'], [-x for x in rotate(second['outward_normal'], angle)]):
        return None
    seam = rotate(second['tile_seam_center_m'], angle)
    if not _close(first['tile_seam_center_m'][:2], [seam[i]+offset[i] for i in (0, 1)]):
        return None
    def flatten(groups):
        reference, channels, members, member_groups = groups[0], {}, {}, {}
        for group in groups:
            if not _close(group['outward_normal'], reference['outward_normal']) or not _close(group['tile_seam_center_m'][:2], reference['tile_seam_center_m'][:2]):
                return None
            for port in group['members']:
                _need(port['id'] not in members, 'Duplicate resolved member ID')
                members[port['id']], member_groups[port['id']] = port, group['id']
            for channel in group['channels']:
                identifier = channel['id']
                if identifier not in channels:
                    channels[identifier] = {**deepcopy(channel), 'cuts': [],
                                            'construction_network': group.get('construction_network')}
                merged = channels[identifier]
                _need(merged['kind'] == channel['kind'] and set(merged['traffic_modes']) == set(channel['traffic_modes']) and merged['construction_network'] == group.get('construction_network'), 'Inconsistent resolved physical channel')
                for cut in channel['cuts']:
                    existing = next((c for c in merged['cuts'] if c['id'] == cut['id']), None)
                    if existing is None:
                        merged['cuts'].append(deepcopy(cut))
                    else:
                        existing['member_ids'].extend(x for x in cut['member_ids'] if x not in existing['member_ids'])
        return list(channels.values()), members, member_groups
    a, b = flatten(aa), flatten(bb)
    if a is None or b is None:
        return None
    channels_a, members_a, groups_a = a
    channels_b, members_b, groups_b = b

    def channel_match(a, b):
        if a['kind'] != b['kind'] or set(a['traffic_modes']) != set(b['traffic_modes']) or a['construction_network'] != b['construction_network']:
            return None
        def cut_match(c, d):
            pairs = _cut_pairs([members_a[x] for x in c['member_ids']], [members_b[x] for x in d['member_ids']], angle, offset)
            return None if pairs is None else pairs
        cuts = _unique_bijection(a['cuts'], b['cuts'], cut_match)
        return None if cuts is None else [pair for cut in cuts for pair in cut]
    channels = _unique_bijection(channels_a, channels_b, channel_match)
    if channels is None:
        return None
    result = {}
    for pair in (p for channel in channels for p in channel):
        key = (groups_a[pair['a_port_id']], groups_b[pair['b_port_id']])
        result.setdefault(key, {'a_group_id': key[0], 'b_group_id': key[1], 'member_pairs': []})['member_pairs'].append(pair)
    return list(result.values())


@_validated
def find_matches(a, b):
    """Find pairwise candidates with complete boundaries and disjoint owned tiles."""
    results = []
    own = {(16.*c, -16.*r) for c, r in a['cells']}
    states = b.get('supported_orientations', [])
    allowed = {s['rotation_ccw_degrees'] for s in states if not s.get('construction_transposed', False)} if states else set(ROTATIONS)
    for first in a['groups']:
        aa = [g for g in a['groups'] if g['boundary_bundle_id'] == first['boundary_bundle_id']]
        for second in b['groups']:
            bb = [g for g in b['groups'] if g['boundary_bundle_id'] == second['boundary_bundle_id']]
            for angle in ROTATIONS:
                if angle not in allowed or not _close(first['outward_normal'], [-x for x in rotate(second['outward_normal'], angle)]):
                    continue
                # Placement comes from the complete tile edge, never a profile
                # origin or an independently moved service section.
                seam = rotate(second['tile_seam_center_m'], angle)
                offset = [first['tile_seam_center_m'][i]-seam[i] for i in (0, 1)]
                if any(abs(x/16.-round(x/16.)) > EPS for x in offset):
                    continue
                offset = [16.*round(x/16.) for x in offset]
                posed = {tuple(round(rotate((16.*c, -16.*r), angle)[i]+offset[i], 6) for i in (0, 1)) for c, r in b['cells']}
                if own & posed:
                    continue
                bundle_pairs = _boundary_pairs(aa, bb, angle, offset)
                if bundle_pairs is None:
                    continue
                selected = next((p for p in bundle_pairs if p['a_group_id'] == first['id'] and p['b_group_id'] == second['id']), None)
                if selected is not None:
                    results.append({'a_piece_id': a['id'], 'a_group_id': first['id'], 'b_piece_id': b['id'], 'b_group_id': second['id'],
                                    'relative_rotation_ccw': angle, 'relative_position_m': offset, 'member_pairs': selected['member_pairs'],
                                    'bundle_group_pairs': bundle_pairs, 'status': 'candidate',
                                    'checks': {'occupied_cells': 'passed', **{k: 'unverified' for k in LIMITATIONS}}})
    return results
