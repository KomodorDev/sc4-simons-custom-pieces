"""A new, native-port-aligned diagonal version of the smooth at-grade HSR T.

All three arms turn forty-five degrees relative to the accepted grid version.
Its native diagonal lane spacing and asymmetric 2.8/2.9 m edge ports are
authored explicitly; rotating the old two-metre lanes would not fit NAM.
The original generator and every previously allocated piece stay unchanged.
"""
from __future__ import annotations

from functools import lru_cache
import json
import math

from scp.dbpf import require
from .directional_t import (_distance, _floor_clip, _floor_subtract,
                            _plan_area, _partition_strict)
from .interchange_layouts import _add_route, _normalize
from .interchange_models import EFFECT_DONOR, construction_symbols
from .rail_features import _construction_flags
from scp.track_paths import S3D, PATH, EXEMPLAR, EFFECT, LTEXT, encode_paths

RECIPE = 'directional_hsr_t_smooth_diagonal_at_grade'
RECIPES = (RECIPE,)
HEIGHT = 15.5
LANE_OFFSET = 2.9 / math.sqrt(2.)
PORTS = {'N': {'in': (173.1, 8., HEIGHT), 'out': (178.9, 8., HEIGHT)},
         'S': {'in': (-8., -178.9, HEIGHT), 'out': (-8., -173.2, HEIGHT)},
         'E': {'in': (184., -189.1, HEIGHT), 'out': (184., -194.9, HEIGHT)}}
PORT_PLANES = {'N': (1, 8.), 'S': (0, -8.), 'E': (0, 184.)}


def _transform(x, y, heading):
    """Scale by sqrt(2), rotate clockwise 45 degrees and align native phases."""
    return x+y+160., y-x-8., heading-math.pi/4.


def _line(start, finish, heading):
    """Sample native straight collars closely enough to retain exact tangents."""
    count = max(1, math.ceil(math.dist(start, finish)/.5))
    return [(start[0]+(finish[0]-start[0])*n/count,
             start[1]+(finish[1]-start[1])*n/count, heading)
            for n in range(count+1)]


def _quarter(reflected=False):
    count = 256
    headings = [-math.pi/2.+math.pi/2.*(10*t**3-15*t**4+6*t**5)
                for t in (n/count for n in range(count+1))]
    points = [(0., 0.)]
    for a, b in zip(headings, headings[1:]):
        x, y = points[-1]
        points.append((x+(math.cos(a)+math.cos(b))/2./count,
                       y+(math.sin(a)+math.sin(b))/2./count))
    scale = 80./points[-1][0]
    states = [(x*scale, 80.+y*scale, angle)
              for (x, y), angle in zip(points, headings)]
    states[0], states[-1] = (0., 80., -math.pi/2.), (80., 0., 0.)
    states = [*_line((0., 88. if reflected else 96.), (0., 80.), -math.pi/2.)[:-1],
              *states, *_line((80., 0.), (104., 0.), 0.)[1:]]
    if reflected:
        states = [(x, -y, -angle) for x, y, angle in states]
    return [_transform(x, y-80., angle) for x, y, angle in states]


def _states():
    return {'main': [_transform(x, y, angle)
                     for x, y, angle in _line((0., -168.), (0., 16.), math.pi/2.)],
            'north_curve': _quarter(), 'south_curve': _quarter(True)}


def _trim_start(points, axis, boundary):
    for index, (a, b) in enumerate(zip(points, points[1:])):
        if min(a[axis], b[axis])-1e-10 <= boundary <= max(a[axis], b[axis])+1e-10:
            delta = b[axis]-a[axis]
            if abs(delta) < 1e-12:
                continue
            fraction = max(0., min(1., (boundary-a[axis])/delta))
            point = tuple(boundary if k == axis else a[k]+fraction*(b[k]-a[k]) for k in range(3))
            rest = points[index+1:]
            if rest and math.dist(point, rest[0]) < 1e-9:
                rest = rest[1:]
            return [point, *rest]
    raise ValueError('A diagonal lane did not cross its declared native end plane')


def _fade(distance):
    """Keep four exact metres, then ease a native 0.1 m mismatch over 16 m."""
    t = max(0., min(1., (distance-4.)/16.))
    return 1.-(10*t**3-15*t**4+6*t**5)


def _lane(states, start_arm, finish_arm, reverse=False):
    if reverse:
        states = [(x, y, angle+math.pi) for x, y, angle in reversed(states)]
    first, last = states[0], states[-1]
    extended = [(first[0]-8.*math.cos(first[2]), first[1]-8.*math.sin(first[2]), first[2]),
                *states,
                (last[0]+8.*math.cos(last[2]), last[1]+8.*math.sin(last[2]), last[2])]
    points = [(x+LANE_OFFSET*math.sin(angle), y-LANE_OFFSET*math.cos(angle), HEIGHT)
              for x, y, angle in extended]
    start, finish = PORTS[start_arm]['in'], PORTS[finish_arm]['out']
    points = _trim_start(points, *PORT_PLANES[start_arm])
    points = list(reversed(_trim_start(list(reversed(points)), *PORT_PLANES[finish_arm])))
    distances = [0.]
    for a, b in zip(points, points[1:]):
        distances.append(distances[-1]+math.dist(a, b))
    start_delta, finish_delta = start[1]-points[0][1], finish[1]-points[-1][1]
    total = distances[-1]
    points = [(p[0], p[1]+start_delta*_fade(distance)+finish_delta*_fade(total-distance), HEIGHT)
              for p, distance in zip(points, distances)]
    # One complete four-metre segment at each native boundary lets the
    # verifier clip just that boundary corridor. Subsequent full-width
    # corridors are entirely inside the authored side of the port plane.
    start_vector = (math.cos(first[2]), math.sin(first[2]))
    finish_vector = (math.cos(last[2]), math.sin(last[2]))
    first_collar = (start[0]+4.*start_vector[0], start[1]+4.*start_vector[1], HEIGHT)
    last_collar = (finish[0]-4.*finish_vector[0], finish[1]-4.*finish_vector[1], HEIGHT)
    points = [start, first_collar,
              *(point for point, distance in zip(points, distances) if 4.+1e-8 < distance < total-4.-1e-8),
              last_collar, finish]
    return points


def directional_routes(recipe=RECIPE):
    require(recipe == RECIPE, 'Unknown diagonal directional rail recipe')
    states = _states()
    return {'S>N': _lane(states['main'], 'S', 'N'),
            'N>S': _lane(states['main'], 'N', 'S', True),
            'N>E': _lane(states['north_curve'], 'N', 'E'),
            'E>N': _lane(states['north_curve'], 'E', 'N', True),
            'S>E': _lane(states['south_curve'], 'S', 'E'),
            'E>S': _lane(states['south_curve'], 'E', 'S', True)}


def _physical_centers():
    return {name: [(x, y, HEIGHT) for x, y, _ in points]
            for name, points in _states().items()}


def directional_layout(recipe=RECIPE):
    layout = {}
    for movement, points in directional_routes(recipe).items():
        _add_route(layout, points, movement,
                   role='main' if movement in ('S>N', 'N>S') else 'branch', deck=False)
    anchor = min(layout, key=lambda cell: (cell[1], cell[0]))
    for name, states in _states().items():
        points = [(x-16.*anchor[0], y+16.*anchor[1], HEIGHT) for x, y, _ in states]
        layout[anchor]['decks'].append({
            'points': points, 'width': 15., 'geometry_id': 'directional_diagonal_'+name,
            'profile': 'hsr', 'precise_union': True, 'simplify_collinear': True,
            'extend_endpoints': 'ports', 'clearance_half_width': 2.6,
            'support': False,
            'start_tangent': (math.cos(states[0][2]), math.sin(states[0][2])),
            'end_tangent': (math.cos(states[-1][2]), math.sin(states[-1][2])),
        })
    result, shift = _normalize(layout)
    require(shift == (0., 0.), 'Diagonal T normalization unexpectedly changed')
    return result


def _support_centers(cells):
    segments = [(a, b) for points in _physical_centers().values() for a, b in zip(points, points[1:])]
    return [(16.*x, -16.*row) for x, row in cells
            if all(any(_distance((16.*x+dx, -16.*row+dy), a, b) < 7.49 for a, b in segments)
                   for dx in (-.65, 0., .65) for dy in (-.65, 0., .65))]


_LAYOUT = directional_layout()
_CELLS = list(_LAYOUT)
INFO = {RECIPE: {
    'recipe': RECIPE, 'name': 'HSR Smooth Diagonal Full T — At Grade',
    'kind': 'smooth_diagonal_at_grade_t', 'category': 'directional-review-prototype',
    'height': HEIGHT, 'footprint': (13, 14), 'cells': _CELLS,
    'cost': 100*len(_CELLS), 'effect_donor': EFFECT_DONOR,
    'ports': PORTS,
    'movements': [(a, b) for a in 'NSE' for b in 'NSE' if a != b],
    'construction_flags': {cell: _construction_flags(data['routes']) for cell, data in _LAYOUT.items()},
    'support_centers': _support_centers(_CELLS),
    'support_foundation_width': 1.3, 'support_min_spacing': 16.,
    'clearance_width': 5., 'clearance_height': 5.,
    'minimum_radius_m': 24., 'maximum_turn_directness': 1.55,
    'at_grade_conflicts': True,
    'provenance': 'New smooth diagonal dual-track T; exact native diagonal ports; intentional at-grade conflicts; no game tests',
}}


def _number(value):
    return int(value, 16) if isinstance(value, str) else int(value)


def _spec(spec):
    require(spec['recipe'] in INFO, 'Unknown diagonal directional T recipe')
    info = INFO[spec['recipe']]
    cells = [tuple(cell) for cell in spec.get('cells', info['cells'])]
    require(cells == info['cells'] and tuple(spec['footprint']) == info['footprint'],
            'Diagonal T cells/footprint differ from its implementation')
    tiles = list(map(_number, spec['tile_ids']))
    require(len(tiles) == len(cells), 'Diagonal T allocation differs from its cell count')
    base = tiles[0]-0x100*cells[0][0]-0x10*cells[0][1]
    require(tiles == [base+0x100*x+0x10*row for x, row in cells],
            'Diagonal T allocation differs from its AutoTileBase grid')
    return info, dict(zip(cells, tiles)), base


def build_rules(spec):
    info, tiles, base = _spec(spec)
    letters, by_flag = construction_symbols(list(tiles), info['construction_flags'])
    width, depth = info['footprint']
    def grid(construct=False):
        rows = ['.'*(width+3)]
        for row in range(depth):
            rows.append('.'+''.join(('+' if construct else letters[x, row]) if (x, row) in letters else '.'
                                    for x in range(width))+'.'+('<' if row == 0 else '.'))
        return rows+['.^'+'.'*(width+1)]
    puzzle, preview = _number(spec['puzzle_id']), _number(spec['preview_id'])
    lines = [f'[HighwayIntersectionInfo_0x{puzzle:08X}]', f'Piece = 0.0, 0.0, 0, 0, 0x{preview:08X}',
             f"PreviewEffect = {spec['effect_name']}", '']
    lines += ['CellLayout = '+row for row in grid()]
    lines += ['']+[f'CheckType = {symbol} - monorail: 0x{flag:08X}' for flag, symbol in by_flag.items()]
    lines += ['']+['ConsLayout = '+row for row in grid(True)]
    lines += ['', f'AutoTileBase = 0x{base:08X}', 'ReplacementIntersection = 0, 0',
              f'PlaceQueryID = 0x{next(iter(tiles.values())):08X}', f'Costs = {info["cost"]}']
    for slot in range(1, 8):
        lines += ['', f'[HighwayIntersectionInfo_0x{puzzle+slot*0x10000:08X}]',
                  f'CopyFrom = 0x{puzzle+(slot%4)*0x10000 if slot >= 4 else puzzle:X}']
        if slot < 4:
            lines.append(f'Rotate = {slot}')
    return '\r\n'.join(lines)+'\r\n'


def build_models(native_hsr, recipe=RECIPE):
    require(recipe in INFO, 'Unknown diagonal directional rail recipe')
    config = {'layout': [[list(cell), data] for cell, data in directional_layout(recipe).items()],
              'ground': False, 'support_centers': INFO[recipe]['support_centers'],
              'support_foundation_width': INFO[recipe]['support_foundation_width'],
              'support_min_spacing': INFO[recipe]['support_min_spacing']}
    signature = json.dumps(config, sort_keys=True, separators=(',', ':'), allow_nan=False)
    return dict(_cached_models(native_hsr, signature))


@lru_cache(maxsize=2)
def _cached_models(native_hsr, signature):
    config = json.loads(signature)
    layout = {tuple(cell): data for cell, data in config['layout']}
    return tuple(_compile_models(native_hsr, layout, config).items())


def _compile_models(native_hsr, layout, config):
    """Compile walls once and construct the robust flat union directly.

    The shared compiler first unions its flat surfaces. The smooth
    junction then discards every one of those faces before constructing its
    robust union. This new-only path preserves the exact wall-cutting order
    and all physical corridors, while omitting that discarded work.
    """
    from scp.models import parse_s3d, pack_s3d
    from .rail_geometry import (_global_decks, _sweep, _index_corridors,
                                _subtract_corridors, _pack_junction)
    from .single_track_models import _native, _pack, _pillar
    from scp.recipes import combine_meshes
    source = _native(native_hsr)
    decks = _global_decks(layout)
    swept = [_sweep(source, deck, False) for deck in decks]
    triangles = []
    for index, (surfaces, corridors, _, _) in enumerate(swept):
        other_corridors = _index_corridors(
            [corridor for number, other in enumerate(swept) if number != index
             for corridor in other[1]], True)
        own_clearance = _index_corridors(
            [{**corridor, 'polygon': polygon} for corridor in corridors
             for polygon in corridor.get('clearance_polygons', [])], True)
        for kind, triangle in surfaces:
            if kind in ('bed', 'rail', 'underside'):
                continue
            for fragment in _subtract_corridors(triangle, other_corridors, wall=True):
                triangles.extend(_subtract_corridors(fragment, own_clearance, wall=True))
    triangles = [tri for tri in triangles
                 if not any(all(abs(point[1]-height) < 1e-4 for point in tri)
                            for height in (source['bed_y'], source['bottom']))]
    floors = [triangle for kind in ('rail', 'bed') for surfaces, _, _, _ in reversed(swept)
              for actual, triangle in surfaces if actual == kind]
    undersides = [triangle for surfaces, _, _, _ in reversed(swept)
                  for kind, triangle in surfaces if kind == 'underside']
    triangles.extend(_flat_union(floors))
    triangles.extend(_flat_union(undersides))
    result = {cell: _pack_junction(source, parts)
              for cell, parts in _partition_strict(triangles, list(layout)).items()}
    support = parse_s3d(_pack(source, _pillar((0., 0.), source['bottom'])))
    support['meshes'][0]['name'] = b'SCP consolidated directional support\0'
    require(config['support_foundation_width'] == 1.3,
            'Diagonal support donor uses a 1.3 m foundation')
    for x, north in config['support_centers']:
        cell = round(x/16.), round(-north/16.)
        model = parse_s3d(result[cell])
        result[cell] = pack_s3d(combine_meshes([
            (model, model['meshes'], (0., 0., 0.)),
            (support, support['meshes'], (0., 0., 0.))]))
    return result


def _floor_bucket_keys(polygon):
    """Conservatively index only four-metre cells touched by a floor polygon.

    A long diagonal triangle has a large square bounding box despite its
    narrow floor strip. Clip that polygon to each exact horizontal grid
    strip, then retain every column between its exact minimum and maximum.
    This excludes no intersecting triangle and requires no sampled mask.
    Boundary-only contacts remain indexed as well.
    """
    result = []
    first = math.floor(min(point[2] for point in polygon)/4.)
    last = math.floor(max(point[2] for point in polygon)/4.)
    for row in range(first, last+1):
        lower, upper = 4.*row, 4.*(row+1)
        strip = _floor_clip(list(polygon), (0., 0., lower), (1., 0., lower), True)
        strip = _floor_clip(strip, (1., 0., upper), (0., 0., upper), True)
        if not strip:
            continue
        left = math.floor(min(point[0] for point in strip)/4.)
        right = math.floor(max(point[0] for point in strip)/4.)
        result.extend((column, row) for column in range(left, right+1))
    return result


def _flat_union(triangles):
    """Union exact four-metre patches, bounding diagonal fragmentation.

    Every accepted fragment stays inside one exact grid cell. Long mainline
    triangles therefore cannot accumulate thousands of fragments while
    passing both curved arms. Original surface priority and interpolated UVs
    are retained independently in every cell; no geometry is sampled away.
    """
    accepted, buckets = [], {}
    for triangle in triangles:
        for cell in _floor_bucket_keys(triangle):
            left, right, lower, upper = 4.*cell[0], 4.*(cell[0]+1), 4.*cell[1], 4.*(cell[1]+1)
            polygon = list(triangle)
            for a, b in (((left, 0., 1.), (left, 0., 0.)),
                         ((right, 0., 0.), (right, 0., 1.)),
                         ((0., 0., lower), (1., 0., lower)),
                         ((1., 0., upper), (0., 0., upper))):
                polygon = _floor_clip(polygon, a, b, True)
            if len(polygon) < 3 or _plan_area(polygon) <= 1e-10:
                continue
            pieces = [polygon]
            previous = buckets.setdefault(cell, [])
            for other in previous:
                xmin, xmax = min(p[0] for p in other), max(p[0] for p in other)
                zmin, zmax = min(p[2] for p in other), max(p[2] for p in other)
                remaining = []
                for polygon in pieces:
                    if (min(p[0] for p in polygon) >= xmax or max(p[0] for p in polygon) <= xmin or
                            min(p[2] for p in polygon) >= zmax or max(p[2] for p in polygon) <= zmin):
                        remaining.append(polygon)
                    else:
                        remaining.extend(_floor_subtract(polygon, list(other)))
                pieces = remaining
                if not pieces:
                    break
            for polygon in pieces:
                for number in range(1, len(polygon)-1):
                    part = (polygon[0], polygon[number], polygon[number+1])
                    if _plan_area(list(part)) > 1e-10:
                        previous.append(part)
                        accepted.append(part)
    return accepted


def build_directional(spec, context):
    from scp.models import parse_s3d, pack_s3d
    from scp.recipes import combine_meshes, effect_clone, label, tile_exemplar
    from scp.shadows import build_shadows
    info, tiles, _ = _spec(spec)
    layout = directional_layout(spec['recipe'])
    hsr = context['hsr']
    models = build_models(hsr[*S3D, 0x5DD31500], spec['recipe'])
    assets, parts = {}, []
    for cell, tile in tiles.items():
        raw = models[cell]
        for zoom in range(5):
            assets[*S3D, tile+zoom] = raw
        assets.update(build_shadows(raw, tile))
        assets[*PATH, tile] = encode_paths(layout[cell]['routes'])
        assets[*EXEMPLAR, tile] = tile_exemplar(hsr[*EXEMPLAR, 0x5DCF0A00], tile, 'SCP | '+spec['name'])
        assets[*LTEXT, tile] = label('SCP | '+spec['name']+' (Experimental)')
        model = parse_s3d(raw)
        parts.append((model, model['meshes'], (16.*cell[0], 0., 16.*cell[1])))
    preview = _number(spec['preview_id'])
    assets[*S3D, preview] = pack_s3d(combine_meshes(parts))
    donor, name, model = info['effect_donor']
    assets[*EFFECT, preview] = effect_clone(hsr[donor], name, spec['effect_name'], model, preview)
    return assets, build_rules(spec)
