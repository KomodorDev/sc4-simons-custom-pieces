"""Close the two recessed paired-end wedges without resweeping native models.

Only this module's explicit alignment rule enables the repair. Existing model
faces remain byte-identical; new concrete fills uncovered areas of the roof,
underside, and the corresponding inside/end walls. Exact mitered boundaries
come from this piece's existing analytic branch samples, rather than a new
approximation of its tracks.
"""
from __future__ import annotations

import math
import struct

from scp.dbpf import require
from scp.models import parse_s3d, pack_s3d
from scp.recipes import combine_meshes
from scp.render_meshes import _triangles
from .directional_t import _floor_subtract, _plan_area, _partition_strict
from .rail_geometry import _route, _trim_sweep
from .single_track_models import _native, _pack, _quad

RECIPE = 'hsr_component_modular_south_junction'


def _world(models):
    result = []
    for (column, row), raw in models.items():
        model = parse_s3d(raw)
        for mesh in model['meshes']:
            for encoded in _triangles(model, mesh['frames'][0]):
                triangle = [struct.unpack('<5f', vertex) for vertex in encoded]
                result.append(tuple((x+16.*column, h, z+16.*row, u, v)
                                    for x, h, z, u, v in triangle))
    return result


def _uncovered(triangle, existing):
    """Subtract only genuinely coplanar saved faces in the candidate's plane."""
    a, b, c = triangle
    ab = [b[i]-a[i] for i in range(3)]
    ac = [c[i]-a[i] for i in range(3)]
    normal = (ab[1]*ac[2]-ab[2]*ac[1],
              ab[2]*ac[0]-ab[0]*ac[2],
              ab[0]*ac[1]-ab[1]*ac[0])
    magnitude = math.sqrt(sum(v*v for v in normal))
    if magnitude <= 1e-10:
        return []
    normal = tuple(v/magnitude for v in normal)
    omitted = max(range(3), key=lambda axis: abs(normal[axis]))
    kept = [axis for axis in range(3) if axis != omitted]
    # The shared convex subtractor uses vertex coordinates 0 and 2 in plan.
    def project(point):
        return point[kept[0]], point[omitted], point[kept[1]], point[3], point[4]
    def restore(point):
        result = [0., 0., 0., point[3], point[4]]
        result[kept[0]], result[omitted], result[kept[1]] = point[:3]
        return tuple(result)
    pieces = [[project(point) for point in triangle]]
    bounds = [(min(p[i] for p in triangle), max(p[i] for p in triangle)) for i in kept]
    for old in existing:
        if any(max(p[i] for p in old) <= low+1e-10 or min(p[i] for p in old) >= high-1e-10
               for i, (low, high) in zip(kept, bounds)):
            continue
        if any(abs(sum(normal[i]*(point[i]-a[i]) for i in range(3))) > 4e-5 for point in old):
            continue
        clip = [project(point) for point in old]
        if _plan_area(clip) < 1e-10:
            continue
        pieces = [part for piece in pieces for part in _floor_subtract(piece, clip)]
        if not pieces:
            break
    return [tuple(restore(point) for point in (piece[0], piece[index], piece[index+1]))
            for piece in pieces if _plan_area(piece) > 1e-9
            for index in range(1, len(piece)-1)]


def repair_models(native_hsr, models, mapping, alignment):
    """Return local models with closed grey wedges at the recessed paired end.

    ``mapping`` maps local construction cells to the original analytic sweep
    cells. Its uniform six-row offset is removed from sampled model z values.
    No other module or external boundary is emitted or modified.
    """
    from .hsr_partition_components import _source
    source = _native(native_hsr)
    require(alignment['branch_inner_half_width_m'] == 2.6
            and alignment['recessed_end_local_south_m'] == 24.
            and alignment['paired_centre_east_m'] == 16.,
            'Symmetric HSR wedge alignment differs from its scoped contract')
    shifts = {(16.*(s[0]-l[0]), 16.*(s[1]-l[1])) for l, s in mapping.items()}
    require(shifts == {(0., 96.)}, 'Symmetric HSR wedge has an unexpected surface frame')
    context = _source(RECIPE)['surface_context']['surface_decks']
    branches = {deck['name']: deck for deck in context}
    existing = _world(models)
    desired, underside, walls = [], [], []
    bed, top, bottom = source['bed_y'], source['top'], source['bottom']
    native = [v for triangle in source['triangles'] for v in triangle]
    concrete_u = sum(v[3] for v in native if abs(v[1]-top) < 1e-4)/len(
        [v for v in native if abs(v[1]-top) < 1e-4])
    inner_u = [v[3] for v in native if abs(abs(v[0])-source['inner']) < 1e-3]
    require(inner_u, 'Symmetric HSR wedge has no native inside-wall material')
    wall_u = sum(inner_u)/len(inner_u)
    north = alignment['recessed_end_local_south_m']
    for name, side in ((alignment['left_branch'], 1.), (alignment['right_branch'], -1.)):
        deck = branches[name]
        require(deck['width'] == 8. and all(abs(p[2]-15.5) < 1e-8 for p in deck['points']),
                'Symmetric HSR wedge requires its original flat eight-metre branches')
        points, _, miters = _route(deck['points'], deck.get('start_tangent'), deck.get('end_tangent'))
        # These branch routes point north, so +side miter points into the gap.
        curves = {}
        for half in (2.6, 4.):
            curves[half] = [(p[0]-side*half*n[0], p[2]-96.-side*half*n[1])
                            for p, n in zip(points, miters)]
        central_inner = 16.-side*source['inner']
        central_outer = 16.-side*7.5
        planes = [(2, north, 1.), (0, central_inner, -side)]
        for a, b in zip(curves[2.6], curves[2.6][1:]):
            roof = _quad([(a[0], top, a[1], concrete_u, -a[1]/16.),
                          (central_inner, top, a[1], concrete_u, -a[1]/16.),
                          (central_inner, top, b[1], concrete_u, -b[1]/16.),
                          (b[0], top, b[1], concrete_u, -b[1]/16.)], (0., 1., 0.))
            desired.extend(triangle for _, triangle in _trim_sweep([('roof', t) for t in roof], [], planes)[0])
            face = _quad([(a[0], bed, a[1], wall_u, -a[1]/16.),
                          (a[0], top, a[1], wall_u, -a[1]/16.),
                          (b[0], top, b[1], wall_u, -b[1]/16.),
                          (b[0], bed, b[1], wall_u, -b[1]/16.)], (-side, 0., 0.))
            walls.extend(triangle for _, triangle in _trim_sweep([('wall', t) for t in face], [], planes)[0])
        # Restore the straight inside face only up to its exact meeting with
        # the branch inside line. The roof's same sampled polygons define it.
        for triangle in desired:
            if any(abs(p[0]-central_inner) < 1e-7 for p in triangle):
                line = sorted({p[2] for p in triangle if abs(p[0]-central_inner) < 1e-7})
                if len(line) < 2 or line[-1]-line[0] < 1e-8:
                    continue
                a, b = line[0], line[-1]
                walls.extend(_quad([(central_inner, bed, a, wall_u, -a/16.),
                                    (central_inner, top, a, wall_u, -a/16.),
                                    (central_inner, top, b, wall_u, -b/16.),
                                    (central_inner, bed, b, wall_u, -b/16.)], (side, 0., 0.)))
        for a, b in zip(curves[4.], curves[4.][1:]):
            floor = _quad([(a[0], bottom, a[1], .07, -a[1]/16.),
                           (central_outer, bottom, a[1], .07, -a[1]/16.),
                           (central_outer, bottom, b[1], .07, -b[1]/16.),
                           (b[0], bottom, b[1], .07, -b[1]/16.)], (0., -1., 0.))
            underside.extend(triangle for _, triangle in _trim_sweep([('bottom', t) for t in floor], [],
                [(2, north, 1.), (0, central_outer, -side)])[0])
        cut = []
        for a, b in zip(curves[4.], curves[4.][1:]):
            if min(a[1], b[1]) <= north <= max(a[1], b[1]) and abs(b[1]-a[1]) > 1e-10:
                cut.append(a[0]+(north-a[1])*(b[0]-a[0])/(b[1]-a[1]))
        require(cut, 'Symmetric HSR wedge has no recessed-plane branch intersection')
        edge = sum(cut)/len(cut)
        walls.extend(_quad([(edge, bottom, north, wall_u, -north/16.),
                            (edge, top, north, wall_u, -north/16.),
                            (central_outer, top, north, wall_u, -north/16.),
                            (central_outer, bottom, north, wall_u, -north/16.)], (0., 0., -1.)))
    additions = []
    for triangle in [*desired, *underside, *walls]:
        # Later additions participate in the union too; adjacent miter patches
        # and an existing wall never become duplicate positive-area faces.
        uncovered = _uncovered(triangle, [*existing, *additions])
        additions.extend(uncovered)
    local = _partition_strict(additions, list(models))
    result = dict(models)
    for cell, triangles in local.items():
        if not triangles:
            continue
        original = parse_s3d(models[cell])
        added = parse_s3d(_pack(source, triangles))
        added['meshes'][0]['name'] = b'SCP HSR symmetric recessed-end concrete wedges\0'
        result[cell] = pack_s3d(combine_meshes([
            (original, original['meshes'], (0., 0., 0.)),
            (added, added['meshes'], (0., 0., 0.))]))
    return result
