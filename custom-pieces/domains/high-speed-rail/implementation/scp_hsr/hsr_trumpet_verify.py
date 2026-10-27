"""Independent literal trumpet contract and saved-resource inspection helpers.

Production verification imports this module, never a unittest module. The
expected external ports and journeys are independently authored literals,
compared with the current assembly acceptance record. Saved-resource checks
read actual DAT PATH bytes and independently frozen support contracts.
Geometry writers never supply the expected answers for verification.
"""
from __future__ import annotations

from collections import defaultdict
import hashlib
import json
import math

from pathlib import Path
from scp.paths import project_root

def _root(root=None):
    return Path(root or project_root()).resolve()

# Independently authored external geometry. Never derive expected ports or
# movements from a route writer or from the candidate acceptance JSON.
PORTS = {'W_in': (-120., -2., 15.5), 'W_out': (-120., 2., 15.5),
         'E_in': (200., 2., 15.5), 'E_out': (200., -2., 15.5),
         'S_in': (2., -216., 15.5), 'S_out': (-2., -216., 15.5)}
MOVEMENTS = [('W_in', 'E_out'), ('W_in', 'S_out'), ('E_in', 'W_out'),
             ('E_in', 'S_out'), ('S_in', 'W_out'), ('S_in', 'E_out')]
CROSSINGS = [(-2., -2., 30.5, 15.5), (-2., 2., 30.5, 15.5),
             (2., -2., 30.5, 15.5), (2., 2., 30.5, 15.5)]
CONTRACT = {'ports': PORTS, 'movements': MOVEMENTS, 'minimum_clearance': 5.,
            'required_grade_separated_crossings': 4,
            'expected_crossings_xyz': CROSSINGS}


def physical_layout(scene):
    """Select physical placement facts, excluding names and document links."""
    instances = scene.get('placements', scene.get('instances'))
    if not isinstance(instances, list) or not instances:
        raise ValueError('Reviewed assembly needs actual piece placements')
    placed = []
    for item in instances:
        degrees = item.get('rotation_degrees_ccw', item.get('rotation_degrees', 0))
        if degrees not in (0, 90, 180, 270):
            raise ValueError('Reviewed layout requires a proper cardinal rotation')
        position = [float(value) for value in item['origin_m']]
        if len(position) != 2 or not all(math.isfinite(value) for value in position):
            raise ValueError('Reviewed layout has an invalid physical position')
        placed.append({'piece_id': item['piece_id'], 'position_m': position,
                       'rotation_degrees_ccw': int(degrees)})
    placed.sort(key=lambda item: (item['position_m'], item['piece_id'],
                                 item['rotation_degrees_ccw']))
    return {'construction_rectangle_tiles': scene['construction_rectangle_tiles'],
            'occupied_tiles': scene['occupied_tiles'], 'external_ports': scene['external_ports'],
            'coordinate_system': {name: scene['coordinate_system'][name] for name in (
                'origin_world_m', 'tile_size_m', 'display_tile_centres_bounds_en',
                'construction_bounds_world_m')},
            'placements': placed}


def audit_approved_layout(scene, assembly_id, root=None):
    """Compare against the independently reviewed current layout, never a writer."""
    if assembly_id != 'straight-stem-trumpet':
        raise ValueError('No independently reviewed physical layout for this assembly')
    path = _root(root)/'domains/high-speed-rail/01_assemblies'/assembly_id/'checks/layout.json'
    frozen = json.loads(path.read_text())
    raw = json.dumps(frozen['layout'], sort_keys=True, separators=(',', ':')).encode()
    if (frozen.get('schema_version') != 1 or frozen.get('assembly_id') != assembly_id
            or hashlib.sha256(raw).hexdigest() != frozen.get('layout_sha256')):
        raise ValueError('Independent assembly layout record is malformed or changed')
    actual = physical_layout(scene)
    if actual != frozen['layout']:
        raise ValueError('Assembly physical layout differs from its reviewed placement contract')
    return {'assembly_id': assembly_id, 'layout_sha256': frozen['layout_sha256'],
            'reviewed_placements_preserved': len(actual['placements']),
            'positions_rotations_ports_and_display_reference_unchanged': True}


def key(point):
    return tuple(round(value, 6) for value in point)


def rotate(point, turns):
    """Independent cardinal rotation, preserving north and physical height."""
    x, north, height = point
    for _ in range(turns % 4):
        x, north = -north, x
    return x, north, height


def horizontal_length(points):
    return sum(math.dist(a[:2], b[:2]) for a, b in zip(points, points[1:]))


def split_flags(records):
    starts = defaultdict(list)
    for cell, metadata, points in records:
        starts[cell, points[0]].append(metadata)
    choices = [items for items in starts.values() if len(items) > 1]
    if any(not any(route['junction'] == 1 for route in items) for items in choices):
        raise ValueError('An encoded split choice lacks its explicit junction flag')
    return len(choices)


def core_section(points, first, last):
    """Locate literal module connection planes without changing any point."""
    if first not in points or last not in points or points.index(first) >= points.index(last):
        raise ValueError('A journey is missing its reviewed core connection planes')
    return points[points.index(first):points.index(last)+1]


def direct_slip_symmetry(journeys):
    """Compare the actual fork-to-merge cores; external arms may be trimmed."""
    south_east = core_section(journeys['S_in', 'E_out'], (2., -216., 15.5), (120., -2., 15.5))
    west_south = core_section(journeys['W_in', 'S_out'], (-120., -2., 15.5), (-2., -216., 15.5))
    reflected = [(-x, north, height) for x, north, height in reversed(south_east)]
    if len(reflected) != len(west_south):
        raise ValueError('Mirrored direct slips have different encoded sampling or core approach lengths')
    error = max(math.dist(a, b) for a, b in zip(reflected, west_south))
    if error > 2e-6:
        raise ValueError('The fork-to-merge direct slips are not mirror symmetric')
    return {'mirrored_encoded_points_checked': len(reflected),
            'maximum_3d_reflection_error_m': error,
            'south_east_length_m': horizontal_length(south_east),
            'west_south_length_m': horizontal_length(west_south),
            'external_approaches_included': False, 'reflection_axis_east_m': 0.,
            'native_fork_and_merge_connection_planes_included': True}


