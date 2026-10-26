"""Independent encoded-resource audits for the two current scissors switches.

Expectations below are literal native ports and city cells. No geometry or
layout writer is imported. Foundations are assembled across *all* placed cell
meshes before overlap, spacing and deck-contact checks are performed.
"""
from __future__ import annotations

from collections import defaultdict
from functools import lru_cache
import json
import math

from scp.dbpf import require
from scp.models import parse_s3d
from .rail_feature_verify import _triangles, _weights
from .interchange_verify import (
    S3D, PATH, EXEMPLAR, _encoded_routes, _graph, _native_port_headings,
    _models, check_construction_fields as _construction,
)

EPS = 5e-5
CONTRACTS = {}
for _level, _height in (('hsr', 15.5), ('ghsr', 1.)):
    _cells = [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2)]
    _ports = {'Nin': (-2., 8., _height), 'Nout': (2., 8., _height),
              'Sin': (2., -40., _height), 'Sout': (-2., -40., _height),
              'BNin': (14., 8., _height), 'BNout': (18., 8., _height),
              'BSin': (18., -40., _height), 'BSout': (14., -40., _height)}
    _vectors = {'Nin': (0., -1.), 'Nout': (0., 1.),
                'Sin': (0., 1.), 'Sout': (0., -1.),
                'BNin': (0., -1.), 'BNout': (0., 1.),
                'BSin': (0., 1.), 'BSout': (0., -1.)}
    _moves = [('Sin', 'Nout'), ('Nin', 'Sout'), ('BSin', 'BNout'), ('BNin', 'BSout'),
              ('Sin', 'BNout'), ('BNin', 'Sout'), ('BSin', 'Nout'), ('Nin', 'BSout')]
    CONTRACTS[f'rail_{_level}_adjacent_scissors_revised'] = {
        'cells': _cells, 'footprint': (2, 3), 'ports': _ports, 'port_vectors': _vectors,
        'movements': _moves, 'min_height': _height, 'max_height': _height,
        'max_grade': 0., 'cost': 100*len(_cells), 'kind': 'scissors_switch',
        'clearance_width_m': 5.,
        'support_centres_xz': [(16.*x, 16.*row) for x, row in _cells] if _height > 1. else [],
        'minimum_support_spacing_m': 16., 'foundation_width_m': 1.3,
    }


def _number(value):
    return int(value, 16) if isinstance(value, str) else int(value)


def _contract(spec):
    require(spec['recipe'] in CONTRACTS, 'Unknown revised rail recipe requires a literal independent contract')
    contract = CONTRACTS[spec['recipe']]
    cells = [tuple(cell) for cell in spec['cells']]
    require(cells == contract['cells'] and tuple(spec['footprint']) == contract['footprint'],
            'Revised rail footprint differs from its literal native-port contract')
    require(not spec.get('structural_cells'), 'Revised junctions have no structural-only cells')
    tiles = list(map(_number, spec['tile_ids']))
    require(len(tiles) == len(cells), 'Revised rail tile count differs from its footprint')
    base = tiles[0]-0x100*cells[0][0]-0x10*cells[0][1]
    require(tiles == [base+0x100*x+0x10*row for x, row in cells],
            'Revised rail allocation does not follow its native AutoTileBase grid')
    return contract


def check_paths(resources, spec, donors=None):
    contract = _contract(spec)
    records = _encoded_routes(resources, spec, contract)
    ports, movements = _graph(records, contract)
    native = _native_port_headings(records, contract)
    return {'tile_count': len(contract['cells']), 'encoded_routes_checked': len(records),
            'external_ports_checked': ports, 'permitted_movements_checked': movements,
            'rotations_checked': 4, 'exact_3d_cell_seams': True, 'unwanted_u_turns': False,
            'native_facing_port_tangents_checked': len(native), 'constant_native_height': True}


def check_construction_fields(fields, spec, resources):
    return _construction(fields, spec, resources, contract=_contract(spec))


def _world_triangles(resources, spec):
    for (x, row), tile in zip(_contract(spec)['cells'], spec['tile_ids']):
        for triangle in _triangles(parse_s3d(resources[*S3D, _number(tile)])):
            yield tuple((px+16.*x, h, pz+16.*row, u, v) for px, h, pz, u, v in triangle)


def _area(polygon):
    return abs(sum(a[0]*b[1]-b[0]*a[1] for a, b in zip(polygon, polygon[1:]+polygon[:1])))/2.


def _cross(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def _overlap(first, second):
    """Exact convex clipping distinguishes shared seams from duplicate area."""
    polygon = list(first)
    orientation = 1. if sum(a[0]*b[1]-b[0]*a[1] for a, b in zip(second, second[1:]+second[:1])) > 0 else -1.
    for a, b in zip(second, second[1:]+second[:1]):
        result = []
        if not polygon:
            break
        for c, d in zip(polygon, polygon[1:]+polygon[:1]):
            vc, vd = orientation*_cross(a, b, c), orientation*_cross(a, b, d)
            if vc >= -1e-8:
                result.append(c)
            if (vc > 1e-8 and vd < -1e-8) or (vc < -1e-8 and vd > 1e-8):
                t = vc/(vc-vd)
                result.append(tuple(c[axis]+t*(d[axis]-c[axis]) for axis in (0, 1)))
        polygon = result
    return _area(polygon) if len(polygon) >= 3 else 0.


def _inside(point, triangle):
    values = [_cross(a, b, point) for a, b in zip(triangle, triangle[1:]+triangle[:1])]
    return all(v >= -EPS for v in values) or all(v <= EPS for v in values)


def audit_supports(triangles, contract):
    """Measure native square foundations in the placed union, never per cell."""
    triangles = list(triangles)
    bases = [[(v[0], v[2]) for v in triangle] for triangle in triangles
             if all(abs(v[1]) < EPS for v in triangle)]
    bases = [triangle for triangle in bases if _area(triangle) > 1e-8]
    expected = contract['support_centres_xz']
    if not expected:
        require(not bases, 'Ground revised junction unexpectedly contains elevated support foundations')
        return {'support_columns_checked': 0, 'global_support_spacing_checked': True,
                'minimum_support_centre_distance_m': None, 'support_tops_touch_deck': True,
                'support_centres_sc4path_xy': [], 'support_contact_points_checked': 0}
    require(bases, 'Elevated revised junction has no support foundations')
    parent = list(range(len(bases)))
    def find(index):
        while parent[index] != index:
            parent[index] = parent[parent[index]]
            index = parent[index]
        return index
    for i, a in enumerate(bases):
        ax, az = [p[0] for p in a], [p[1] for p in a]
        for j, b in enumerate(bases[:i]):
            bx, bz = [p[0] for p in b], [p[1] for p in b]
            if min(ax) > max(bx)+EPS or min(bx) > max(ax)+EPS or min(az) > max(bz)+EPS or min(bz) > max(az)+EPS:
                continue
            require(_overlap(a, b) < 1e-7,
                    'Overlapping or duplicate support foundations occur in the placed union')
            if any(_inside(p, b) for p in a) or any(_inside(p, a) for p in b):
                parent[find(i)] = find(j)
    groups = defaultdict(list)
    for index, triangle in enumerate(bases):
        groups[find(index)].append(triangle)
    centres, tops = [], []
    width = contract['foundation_width_m']
    for group in groups.values():
        xs, zs = [p[0] for tri in group for p in tri], [p[1] for tri in group for p in tri]
        xmin, xmax, zmin, zmax = min(xs), max(xs), min(zs), max(zs)
        require(abs(xmax-xmin-width) < EPS and abs(zmax-zmin-width) < EPS and
                abs(sum(_area(t) for t in group)-width*width) < 4*EPS,
                'A support foundation is incomplete, merged with a near duplicate, or not the native1.3m square')
        centre = (xmin+xmax)/2., (zmin+zmax)/2.
        centres.append(centre)
        walls = [tri for tri in triangles if all(xmin-EPS <= v[0] <= xmax+EPS and zmin-EPS <= v[2] <= zmax+EPS for v in tri)
                 and min(v[1] for v in tri) <= EPS and max(v[1] for v in tri) > 3.]
        require(walls, 'A support footing has no continuous elevated column')
        top = max(v[1] for tri in walls for v in tri)
        tops.append(top)
        # Exclude the column itself: the nearest horizontal deck surface above
        # its top must be within2cm, and carry a full rail bed above that point.
        for x in (xmin, centre[0], xmax):
            for z in (zmin, centre[1], zmax):
                roofs = []
                for tri in triangles:
                    if min(v[1] for v in tri) < top-EPS:
                        continue
                    if all(xmin-EPS <= v[0] <= xmax+EPS and zmin-EPS <= v[2] <= zmax+EPS for v in tri):
                        continue
                    weights = _weights(x, z, tri)
                    if weights:
                        roofs.append(sum(v[1]*w for v, w in zip(tri, weights)))
                require(roofs and -.001 <= min(roofs)-top <= .021,
                        'A revised support column stops below its actual deck underside and is floating')
    minimum = min(math.dist(a, b) for i, a in enumerate(centres) for b in centres[:i]) if len(centres)>1 else None
    require(minimum is None or minimum >= contract['minimum_support_spacing_m']-EPS,
            'Near-duplicate support columns are too close across placed cell meshes')
    require(len(centres) == len(expected) and all(any(math.dist(a, b) < EPS for b in centres) for a in expected),
            'Revised support centres differ from the literal consolidated six-pier plan')
    return {'support_columns_checked': len(centres), 'support_contact_points_checked': 9*len(centres),
            'global_support_spacing_checked': True,
            'minimum_support_centre_distance_m': minimum, 'support_tops_touch_deck': True,
            'support_centres_sc4path_xy': sorted((round(x, 6), round(-z, 6)) for x, z in centres)}


def check_models(resources, spec, donors=None):
    _contract(spec)
    keys = {(*S3D, _number(spec['preview_id']))}
    for tile in map(_number, spec['tile_ids']):
        keys.update({(*S3D, tile+zoom) for zoom in range(5)})
        keys.update({(*PATH, tile), (*EXEMPLAR, tile)})
    immutable = tuple((key, resources[key]) for key in sorted(keys))
    return json.loads(_cached_models(json.dumps(spec, sort_keys=True, separators=(',', ':')), immutable))


@lru_cache(maxsize=32)
def _cached_models(spec_json, immutable):
    spec, resources = json.loads(spec_json), dict(immutable)
    contract = _contract(spec)
    report = _models(resources, spec, contract=contract)
    report.update(audit_supports(_world_triangles(resources, spec), contract))
    report['revised_native_ports_and_supports'] = True
    return json.dumps(report, sort_keys=True, separators=(',', ':'))
