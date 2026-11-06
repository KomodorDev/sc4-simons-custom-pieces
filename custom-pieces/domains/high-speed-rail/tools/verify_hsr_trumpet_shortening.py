#!/usr/bin/env python3
"""Verify the two removed HSR trumpet straights against the saved predecessor."""
from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/high-speed-rail/implementation'),
                str(ROOT / 'domains/highway/implementation')]

from scp.adaptive_network import rotate_flags
from scp.assembly_aliases import _sections
from scp.build import audit_inputs, RUL0
from scp.catalog import load_catalog, select_pieces
from scp.dbpf import require
from scp.models import parse_s3d, valid_frame
from scp.recipes import parse_donor_paths
from scp.track_paths import PATH, S3D, _parse_paths
from scp.verify import check_emitted_runtime_addresses, parse_rules, strict_dbpf
from scp_hsr.assembly_inspection import encoded_records, load_build, triangle_count, world_tiles
from scp_hsr.directional_t_verify import _journeys
from scp_hsr.hsr_components_verify import CONTRACTS
from scp_hsr.hsr_trumpet_verify import CONTRACT, key, rotate, split_flags
from scp_hsr.interchange_verify import _graph
from scp_hsr.rail_feature_verify import _triangles
from scp_hsr.trumpet_terminals import verify_native_inputs

ASSEMBLY = ROOT / 'domains/high-speed-rail/01_assemblies/hsr-trumpet-straight-stem'
BASELINE = ASSEMBLY / 'evidence/design-history/assembly-before-outer-straight-removal.json'
DIVERGE = 'hsr-l2-two-track-mainline-split-oblique-cut'
SOUTH = 'hsr-l2-two-track-mainline-split-merge-parallel-recessed-end'
NATIVE = 0x5DD31500
RUL1 = (*RUL0[:2], 0x10000001)
RUL2 = (*RUL0[:2], 0x10000002)
REMOVED = {(-112., 0.): 'P22', (192., 0.): 'P09'}
AFTER_PORTS = {'W_in': (-104., -2., 15.5), 'W_out': (-104., 2., 15.5),
               'E_in': (184., 2., 15.5), 'E_out': (184., -2., 15.5),
               'S_in': (2., -216., 15.5), 'S_out': (-2., -216., 15.5)}
BEFORE_PORTS = {**AFTER_PORTS, 'W_in': (-120., -2., 15.5), 'W_out': (-120., 2., 15.5),
                'E_in': (200., 2., 15.5), 'E_out': (200., -2., 15.5)}
# Arm, component, canonical outward face, helper grid, owner centre, native centre,
# placement quarter turns counterclockwise, and actual owner tile identifier.
TERMINALS = {
    'P01': ('W', DIVERGE, 'west', (0, 13), (-96., 0.), (-112., 0.), 0, 0x7F584000),
    'P08': ('E', DIVERGE, 'west', (19, 13), (176., 0.), (192., 0.), 2, 0x7F584000),
    'P04': ('S', SOUTH, 'south', (7, -1), (0., -208.), (0., -224.), 0, 0x7F58C150),
}
SAMPLES = ((0, (-2., 0., 2.), (16.189326,)),
           (0, (-7.3, -6.7, 6.7, 7.3), (16.989326,)),
           (1, (16.5,), (-7.5, -5.9965477, 5.9965477, 7.5)),
           (1, (15.5,), (-7., 7.)))
HEADER = """// title: "HSR trumpet outer straight removal audit"
// summary: "Verify the retained trumpet geometry, clipped journeys, and shortened native starter placements against the saved predecessor."
//
// Used when: Reviewing the shortened trumpet assembly and its prepared menu.
// Read by: The trumpet testing guide and maintainers reviewing the assembly.
// Updated by: A maintainer rerunning the shortened-layout verifier against the exact saved builds.
// Affects: Software evidence for the fixed placement plan, saved paths, native seams, and terminal selection states.
"""


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def plan_ports(scene):
    return {f'{arm}_{flow}': tuple(position) for arm, sockets in scene['external_ports'].items()
            for flow, position in sockets.items()}


def support_centres(scene):
    points = set()
    for placement in scene['placements']:
        east, north = placement['origin_m']
        turns = placement['rotation_degrees_ccw'] // 90
        for x, south in CONTRACTS[placement['recipe']]['support_centres_xz']:
            dx, dy, _ = rotate((x, -south, 0.), turns)
            points.add(key((east + dx, north + dy, 0.))[:2])
    return points


def check_paths(old_tiles, tiles):
    old, new = encoded_records(old_tiles), encoded_records(tiles)
    require((len(old), len(new)) == (166, 162), 'Exactly four straight PATH fragments must be removed')
    previous = _journeys(old, {**CONTRACT, 'ports': BEFORE_PORTS})
    current = _journeys(new, {**CONTRACT, 'ports': AFTER_PORTS})
    rows = []
    for (entry, exit_), points in sorted(previous.items()):
        trimmed = points[int(entry[0] in 'WE'):len(points) - int(exit_[0] in 'WE')]
        require(current[entry, exit_] == trimmed, f'Unexpected retained PATH change for {entry} to {exit_}')
        rows.append({'journey': [entry, exit_], 'previous_point_count': len(points),
                     'retained_point_count': len(trimmed), 'retained_points_identical': True})
    require(len(rows) == len(current) == 6, 'The six previous journeys must all remain available')
    for turns in range(4):
        ports = {name: key(rotate(point, turns)) for name, point in AFTER_PORTS.items()}
        records = [(cell, meta, [key(rotate(p, turns)) for p in path]) for cell, meta, path in new]
        require(_graph(records, {**CONTRACT, 'ports': ports}) == (6, 6) and split_flags(records) == 3,
                'The rotated shortened route graph or its three split points changed')
    return {'previous_fragments': len(old), 'retained_fragments': len(new), 'allowed': 6, 'forbidden': 6,
            'splits': 3, 'proper_rotations_checked': 4, 'journeys': rows}


def edge_sockets(routes, face, turns, centre):
    axis = 1 if face[1] else 0
    found = defaultdict(list)
    for route in routes:
        points = route['points']
        for entry, a, b in ((True, points[0], points[1]), (False, points[-2], points[-1])):
            endpoint = a if entry else b
            if endpoint[axis] != 8 * face[axis]:
                continue
            delta = [last - first for first, last in zip(a, b)]
            length = abs(delta[axis])
            require(length > 0, 'An external PATH chord has no outward component')
            direction = rotate(tuple(value / length for value in delta), turns)
            east, north, height = rotate(endpoint, turns)
            found[entry, (east + centre[0], north + centre[1], height), direction, route['transport']].append(
                [route.get('class', route.get('lane')), route.get('junction')])
    return found


def section_profile(model, face, turns):
    outward = rotate((*face, 0), turns)
    along = 1 if outward[1] else 0
    station = outward[along] * (8 - .000005)
    segments = []
    for triangle in _triangles(model):
        points = [rotate((x, -south, h), turns) for x, h, south, _, _ in triangle]
        cuts = []
        for a, b in zip(points, points[1:] + points[:1]):
            if min(a[along], b[along]) < station < max(a[along], b[along]):
                fraction = (station - a[along]) / (b[along] - a[along])
                cuts.append(tuple(a[i] + fraction * (b[i] - a[i]) for i in (1 - along, 2)))
        if len(cuts) == 2:
            segments.append(cuts)

    result = []
    for axis, values, expected in SAMPLES:
        other = 1 - axis
        for value in values:
            found = [a[other] + (value - a[axis]) / (b[axis] - a[axis]) * (b[other] - a[other])
                     for a, b in segments if a[axis] != b[axis]
                     and min(a[axis], b[axis]) <= value <= max(a[axis], b[axis])]
            require(found, 'Saved model lacks a native boundary profile sample')
            for target in expected:
                actual = min(found, key=lambda point: abs(point - target))
                require(abs(actual - target) <= .00005, 'Saved native boundary model sample differs')
                result.append(actual)
    return result


def check_native_seams(tiles, pieces, context):
    controller, hsr = context['controller'], context['hsr']
    tables = re.split(rb'(?m)^\[([^]\r\n]+)\][^\n]*\n', controller[RUL1])
    roads = dict(zip(tables[1::2], tables[2::2]))[b'RoadMonoRailIntersectionSolutions']
    native_path = parse_donor_paths(hsr[*PATH, NATIVE])
    native_model = parse_s3d(hsr[*S3D, NATIVE])
    native_model['meshes'] = [m for m in native_model['meshes']
                              if all(valid_frame(native_model, f) for f in m['frames'])]
    require(len(native_model['meshes']) == 1 and native_model['meshes'][0]['name'] == b'support\0',
            'The pinned native straight has a different valid model mesh')
    report = {}
    for label, (arm, piece, side, grid, centre, helper, pose, iid) in TERMINALS.items():
        tile = tiles[centre]
        declared = pieces[piece]
        cell_index = declared['cells'].index(list(tile['cell']))
        require((tile['instance_id'], tile['piece_id'], tile['rotation']) == (label, piece, pose)
                and int(declared['tile_ids'][cell_index], 16) == iid and helper not in tiles,
                'Wrong terminal owner, rotated cell, or occupied helper')
        path = _parse_paths(tile['resources']['path'])
        models = [parse_s3d(tile['resources'][f'model_{zoom}']) for zoom in range(5)]
        face, rotation = ((-1, 0), 1) if side == 'west' else ((0, -1), 0)
        maximum = 0.
        for turns in range(4):
            native_cw = (rotation - turns) % 4
            road, monorail = [rotate_flags(flags, native_cw) for flags in (0x00010100, 0x02000200)]
            rule = f'Rot{native_cw+1}=0x{road:08X},0x{monorail:08X},0x{NATIVE:08X},{native_cw},0'
            require(roads.splitlines().count(rule.encode()) == 1, 'The original RUL1 lacks an exact starter rotation')
            dx, dy, _ = rotate((16 * face[0], 16 * face[1], 0), turns)
            neighbor = (centre[0] + dx, centre[1] + dy)
            owner = edge_sockets(path, face, turns, centre)
            donor = edge_sockets(native_path, (0, 1), -native_cw, neighbor)
            require(len(owner) == len(donor) == 2
                    and {(not entry, point, tangent, transport) for entry, point, tangent, transport in owner}
                    == set(donor), 'The two directed native PATH sockets must coincide exactly')
            original = section_profile(native_model, (0, 1), -native_cw)
            for model in models:
                actual = section_profile(model, face, turns)
                maximum = max(maximum, *(abs(a - b) for a, b in zip(original, actual, strict=True)))
            if turns == pose:
                require(neighbor == helper, 'The rotated helper does not reach the declared native cell')
                sockets = []
                for (entry, point, tangent, transport), rows in sorted(owner.items(), reverse=True):
                    flow = 'in' if entry else 'out'
                    require(point == AFTER_PORTS[f'{arm}_{flow}'], 'The saved PATH misses the shortened outer port')
                    sockets.append({'direction': flow, 'position_m': point, 'tangent_and_grade': tangent,
                                    'transport_class': transport, 'custom_lane_and_junction': rows,
                                    'native_lane_and_junction': donor[not entry, point, tangent, transport]})
                report[label] = {'helper_grid_east_north': grid, 'helper_centre_m': helper,
                                 'native_cw_rotation': native_cw, 'native_rul1': rule,
                                 'registered_sockets': sockets}
        require(maximum <= .00005, 'Saved model profile no longer matches the native seam')
        report[label]['maximum_model_sample_difference_m'] = round(maximum, 9)
    return {'native_tile': f'{NATIVE:08x}', 'rul1_sha256': digest(controller[RUL1]),
            'rul2_sha256': digest(controller[RUL2]), 'native_path_sha256': digest(hsr[*PATH, NATIVE]),
            'native_model_sha256': digest(hsr[*S3D, NATIVE]), 'proper_rotations_per_terminal': 4,
            'paired_directed_socket_comparisons': 24, 'model_profile_comparisons': 60, 'terminals': report}


def saved_menu(path):
    manifest = json.loads((path / 'manifest.json').read_bytes())
    menu = manifest['menu_experiment']
    matches = [row for row in menu['assemblies'] if row['assembly_id'] == 'hsr-trumpet-straight-stem']
    require(len(matches) == 1, 'The saved trumpet assembly cycle is missing or duplicated')
    raw = (path / manifest['plugin_folder'] / '00_SCP_Controller_NAM50.dat').read_bytes()
    controller = strict_dbpf(raw)
    require(RUL2 not in controller, 'The saved menu must use the stock RUL2 controller')
    return matches[0]['terminal_components'], dict(_sections(controller[RUL0])), digest(raw)


def check_menu(baseline, candidate, pieces):
    previous, before, _ = saved_menu(baseline)
    terminals, sections, controller_sha = saved_menu(candidate)
    require([(row['placement_id'], row['cycle_position']) for row in terminals]
            == [('P04', 15), ('P08', 16), ('P01', 17)],
            'The saved terminal cycle must end with south, east, and west, in that order')
    previous_south = [int(row['puzzle_id'], 16) for row in previous if row['placement_id'] == 'P04']
    require(len(previous_south) == 1, 'The previous menu must contain one southern terminal')
    states, addresses = set(), {}
    for item in terminals:
        label = item['placement_id']
        _, piece_id, side, grid, _, _, turns, _ = TERMINALS[label]
        require((item['piece_id'], item['helper_edge'], tuple(item['helper_cell_xy']), item['rotation_degrees_ccw'])
                == (piece_id, side, grid, turns * 90), 'The saved menu selects the wrong terminal placement')
        piece = pieces[piece_id]
        root, variant = int(piece['puzzle_id'], 16), int(item['puzzle_id'], 16)
        body = sections[variant]
        flags = (b'monorail: 0x00020002 road: 0x01010000' if side == 'west' else
                 b'monorail: 0x02000200 road: 0x00010100')
        check = b'CheckType = Z - ' + flags + b' optional\r\n'
        require(body.count(check) == 1, 'The saved alias is missing the correct optional Road/Monorail marker')
        if side == 'west':
            extended, original = b'CellLayout = ZAABA.<\r\n', b'CellLayout = .AABA.<\r\n'
            require(body.count(extended) == 1
                    and body.replace(extended, original, 1).replace(check, b'', 1) == sections[root],
                    'The west helper must be the only change to the canonical diverge body')
        else:
            require(body == before[previous_south[0]], 'The southern starter construction changed')
        fragment = f'[HighwayIntersectionInfo_0x{variant:08X}]'.encode() + body
        fields = defaultdict(list)
        for field, value in parse_rules(fragment.decode('ascii'))[1][variant]:
            fields[field].append(value)
        addresses[label] = check_emitted_runtime_addresses(fields, piece)['cells_checked']
        for state in range(8):
            original_id, saved_id = root + state * 0x10000, variant + state * 0x10000
            states.add(saved_id)
            if state:
                original = sections[original_id]
                copies = [line for line in original.splitlines() if line.startswith(b'CopyFrom')]
                require(len(copies) == 1, 'The canonical orientation must copy its source root or rotation')
                target = int(copies[0].split(b'=')[1].strip(), 16)
                copied = variant + target - root
                require(sections[saved_id] == original.replace(copies[0], f'CopyFrom = 0x{copied:X}'.encode(), 1),
                        'An alias orientation changed more than its source reference')
    require(len(states) == 24, 'The three terminal selections need eight distinct states each')
    return {'controller_dat_sha256': controller_sha, 'owned_model_addresses_checked': addresses,
            'unique_terminal_construction_states': len(states), 'south_root_body_identical': True}


def verify(baseline_build, candidate_build, plugins):
    source = (ASSEMBLY / 'assembly.json').read_bytes()
    old_source = BASELINE.read_bytes()
    scene, old_scene = json.loads(source), json.loads(old_source)
    require(plan_ports(scene) == AFTER_PORTS and plan_ports(old_scene) == BEFORE_PORTS,
            'The fixed trumpet ends differ from the two exact one-tile cuts')
    current_grid, previous_grid = scene['coordinate_system'], old_scene['coordinate_system']
    require(all(current_grid[name] == previous_grid[name] for name in (
                'origin_world_m', 'tile_size_m', 'display_tile_centres_bounds_en',
                'authoring_to_display_tile_offset_en'))
            and scene['construction_rectangle_tiles'] == [18, 23]
            and current_grid['construction_bounds_world_m'] == [-104., -216., 184., 152.],
            'The fixed footprint must shrink while the displayed grid retains its coordinates')
    expected_approaches = {label: {'arm': arm, 'helper_edge': side, 'helper_cell_xy': list(grid)}
                           for label, (arm, _, side, grid, *_) in TERMINALS.items()}
    require(scene['terminal_approaches'] == expected_approaches, 'The fixed grid has a different terminal plan')
    old, current = load_build(baseline_build), load_build(candidate_build)
    old_tiles, old_places = world_tiles(old_scene, old)
    tiles, places = world_tiles(scene, current)
    require(len(old_tiles) == 105 and len(tiles) == 103 and set(tiles) <= set(old_tiles)
            and {point: old_tiles[point]['instance_id'] for point in old_tiles.keys() - tiles.keys()} == REMOVED
            and all(tile == old_tiles[point] for point, tile in tiles.items()),
            'The two removals must preserve every retained cell, pose, and model/PATH/shadow payload')
    before = {row['instance']: row for row in old_places}
    require(len(before) == 28 and len(places) == 26 and all(row == before[row['instance']] for row in places),
            'The retained placements must use the same saved DAT bytes and preview faces')
    retained_dats = {row['piece_id']: row['dat_sha256'] for row in places}
    require(len(retained_dats) == 14, 'The fourteen component types must all remain in use')
    previous_supports, supports = support_centres(old_scene), support_centres(scene)
    require(len(previous_supports) == 74 and len(supports) == 72 and supports <= previous_supports
            and previous_supports - supports == REMOVED.keys(),
            'Only the support centred on each removed straight may be lost')
    catalog = load_catalog(ROOT)
    selected = select_pieces(catalog, [DIVERGE, SOUTH])
    context, installed, donors, _ = audit_inputs(catalog, plugins, selected, extra_roots=[])
    verify_native_inputs(context, installed, donors)
    return {
        'schema_version': 1, 'status': 'passed',
        'baseline_manifest_sha256': old['manifest_sha256'], 'candidate_manifest_sha256': current['manifest_sha256'],
        'baseline_scene_sha256': digest(old_source), 'candidate_scene_sha256': digest(source),
        'baseline_scene': BASELINE.relative_to(ASSEMBLY).as_posix(), 'candidate_scene': 'assembly.json',
        'removed': [{'placement': label, 'centre_m': point} for point, label in sorted(REMOVED.items())],
        'retained_fixed_cells': len(tiles), 'retained_placements_and_DATs_identical': len(places),
        'fixed_construction_rectangle_tiles': scene['construction_rectangle_tiles'],
        'retained_piece_dat_sha256': dict(sorted(retained_dats.items())),
        'retained_fixed_payload_comparisons': len(tiles) * 11,
        'retained_source_support_positions': len(supports),
        'retained_actual_tile_triangles': sum(triangle_count(tile['resources']['model_0']) for tile in tiles.values()),
        'paths': check_paths(old_tiles, tiles), 'native_seams': check_native_seams(tiles, current['pieces'], context),
        'saved_menu': check_menu(baseline_build, candidate_build, current['pieces']),
        'limits': ['Native dependencies were audited in the supplied stock-only NAM input directory. The full installed Plugins collision scan is outside this audit.',
                   'Software checks cover the saved construction rules, route geometry, and sampled model profile.',
                   'Starter creation, dragging, visible trains, and live selection of coincident branch records remain unverified.'],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline-build', type=Path, required=True)
    parser.add_argument('--candidate-build', type=Path, required=True)
    parser.add_argument('--plugins', type=Path, required=True, help='Directory containing the pinned native NAM inputs')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = verify(args.baseline_build, args.candidate_build, args.plugins)
    args.output.write_text(HEADER + json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(f'Shortened trumpet software checks passed. Report written to {args.output.name}.')


if __name__ == '__main__':
    main()
