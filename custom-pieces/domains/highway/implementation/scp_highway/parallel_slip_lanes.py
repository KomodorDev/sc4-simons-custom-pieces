"""Use the existing straight deck shoulder for bounded auxiliary lanes.

The physical ramp, its barriers, its deck-edge opening, and every point past
that opening stay unchanged. Only traffic on the native shoulder and its
quarter-metre white markings receive the longer merge/diverge treatment.
"""
from copy import deepcopy
import math

from . import ramp_geometry as geometry
from . import ramp_paths
from . import slip_lanes as paint

PROFILE = 'shoulder-auxiliary-lower-8m-4m-upper-5m-1m'
AUXILIARY_Q = 5.5


def apply(route):
    result = deepcopy(route)
    original = route['points']
    outward = original if route['direction'] == 'off' else list(reversed(original))
    old_u, v0 = geometry.highway_coordinates(outward[0])
    direction = 1 if geometry.highway_coordinates(outward[1])[0] > old_u else -1
    side, height = route['side'], route['height_m']
    lower = route['deck'] == 'lower'
    first = (60.8, 56., height) if route['direction'] == 'off' else (-56., -60.8, height)
    first = first if lower else tuple(outward[0])
    u0, _ = geometry.highway_coordinates(first)
    join = next(i for i, point in enumerate(outward)
                if side * geometry.highway_coordinates(point)[1] >= 8.)
    uj, vj = geometry.highway_coordinates(outward[join])
    following = geometry.highway_coordinates(outward[join + 1])
    finish = direction * (uj - u0)
    slope = side * (following[1] - vj) / (direction * (following[0] - uj))
    taper, parallel = (8., 4.) if lower else (5., 1.)
    prefix = [first, geometry.world_coordinates(u0 + direction * .01, v0, height)]
    for index in range(1, int(taper * 8) + 1):
        station = index / 8.
        t = station / taper
        q = abs(v0) + (AUXILIARY_Q - abs(v0)) * t**3 * (10. - 15.*t + 6.*t*t)
        prefix.append(geometry.world_coordinates(u0 + direction * station, side * q, height))
    for index in range(1, int(parallel * 8) + 1):
        prefix.append(geometry.world_coordinates(u0 + direction * (taper + index / 8.),
                                                  side * AUXILIARY_Q, height))
    span = finish - taper - parallel
    if span <= 0.:
        raise ValueError('Parallel auxiliary lane cannot reach its retained physical opening')
    count = max(8, math.ceil(span * 8))
    for index in range(1, count):
        t = index / count
        q = ((2*t**3 - 3*t*t + 1)*AUXILIARY_Q
             + (-2*t**3 + 3*t*t)*side*vj + (t**3 - t*t)*span*slope)
        prefix.append(geometry.world_coordinates(u0 + direction * (taper + parallel + t*span),
                                                  side * q, height))
    revised = prefix + outward[join:]
    points = revised if route['direction'] == 'off' else list(reversed(revised))
    delta = len(points) - len(original)
    old_last = len(original) - 1
    for segment in result['segments']:
        if route['direction'] == 'off':
            for key in ('start_index', 'end_index'):
                if segment[key] >= join:
                    segment[key] += delta
        else:
            for key in ('start_index', 'end_index'):
                if segment[key] > old_last - join:
                    segment[key] += delta
    result.update({'points': [list(point) for point in points],
                   'points_uvh': [[*geometry.highway_coordinates(point), point[2]] for point in points],
                   'mesh_points': deepcopy(original),
                   'mesh_segments': deepcopy(route['segments']),
                   'shoulder_points': [list(point) for point in points],
                   'native_high_port': list(first),
                   'path_cells': [list(cell) for cell in sorted({cell for cell, _ in
                                  ramp_paths.polyline_fragments(points)}, key=lambda c: (c[1], c[0]))],
                   'highway_slip_profile': PROFILE,
                   'auxiliary_lane': {'taper_m': taper, 'parallel_m': parallel,
                                      'centre_q_m': AUXILIARY_Q,
                                      'upstream_extension_m': abs(u0 - old_u),
                                      'retained_physical_mesh': True}})
    # Keep the retained model's measurements intact and explicitly separate
    # the traffic alignment, whose upstream collar and inside-deck run differ.
    result['physical_profile'] = deepcopy(route['profile'])
    lengths, _ = geometry.route_frames(points)
    departure = next(segment for segment in result['segments'] if segment['kind'] == 'flat-high-departure')
    first_index, last_index = departure['start_index'], departure['end_index']
    high_points = points[first_index:last_index + 1]
    from .parallel_ramp_review import _radius
    result['profile'].update({
        'reference': 'Revised traffic alignment; physical_profile retains the unchanged model measurements',
        'departure_station_u_m': u0,
        'departure_plan_run_u_m': abs(geometry.highway_coordinates(high_points[-1])[0]
                                     - geometry.highway_coordinates(high_points[0])[0]),
        'departure_length_plan_m': lengths[last_index] - lengths[first_index],
        'departure_minimum_sampled_radius_m': _radius(high_points),
        'length_total_plan_m': lengths[-1],
    })
    return result


def marking_layout(route):
    """Join one consistent white core to the retained physical ramp stripes."""
    outward = route['points'] if route['direction'] == 'off' else list(reversed(route['points']))
    physical = route['mesh_points'] if route['direction'] == 'off' else list(reversed(route['mesh_points']))
    u0, _ = geometry.highway_coordinates(outward[0])
    direction = 1 if geometry.highway_coordinates(outward[1])[0] > u0 else -1
    side = route['side']
    centre = [(direction * (geometry.highway_coordinates(p)[0] - u0),
               side * geometry.highway_coordinates(p)[1]) for p in outward]
    original = [(direction * (geometry.highway_coordinates(p)[0] - u0),
                 side * geometry.highway_coordinates(p)[1]) for p in physical]
    offset = 3. - .828125 - .4
    inner = paint._trim_paint_curve(paint._offset_paint_curve(centre, -offset), 4.5, 8.)
    outer_hit, _, outer_tangent = paint._paint_intersection(
        paint._offset_paint_curve(original, offset), 8.)
    taper = route['auxiliary_lane']['taper_m']
    connector = min(2., outer_hit[0] - taper - .25)
    if connector <= 0.:
        raise ValueError('Parallel shoulder paint cannot reach its native ramp stripe')
    start = outer_hit[0] - connector
    handle = min(connector / 3., .5 / outer_tangent[1])
    controls = ((start, 7.), (start + connector / 3., 7.),
                (outer_hit[0] - handle * outer_tangent[0], 8. - handle * outer_tangent[1]), outer_hit)
    from .parallel_layout import GROUPS
    owned = {cell for _name, cells, _role in GROUPS.values() for cell in cells}
    edge = [geometry.world_coordinates(u0 + direction * station, side * 4.5, route['height_m'])
            for station in (-20., 20.)]
    def edge_station(point, cell):
        world = point[0] + 16.*cell[0], point[1] - 16.*cell[1]
        return direction * (geometry.highway_coordinates(world)[0] - u0)
    opening_start = min(max(0., edge_station(points[0], cell))
                        for cell, points in ramp_paths.polyline_fragments(edge)
                        if cell in owned and edge_station(points[-1], cell) >= 0.)
    if opening_start >= taper:
        raise ValueError('Shoulder taper begins outside its existing construction cells')
    outer = []
    for index in range(int(taper * 8) + 1):
        station = index / 8.
        t = max(0., (station - opening_start) / (taper - opening_start))
        outer.append((station, 4.5 + 2.5 * t**3 * (10. - 15.*t + 6.*t*t)))
    outer.append((start, 7.))
    outer.extend(paint._bezier_paint(controls)[1:])
    nose = inner[0]
    outline = [(inner[-1][0], 4.5), *inner]
    margin = paint.WHITE_CORE_WIDTH + paint.HATCH_CLEAR_GAP
    limit = paint._offset_paint_curve(inner, -margin)
    hatches = []
    for index in range(1, math.ceil((inner[-1][0] - nose[0]) / paint.HATCH_PITCH)):
        a = nose[0] + index * paint.HATCH_PITCH, 4.5 + margin
        constant = sum(a)
        for first, last in zip(limit, limit[1:]):
            low, high = sum(first) - constant, sum(last) - constant
            if low <= 0. < high:
                t = -low / (high - low)
                b = tuple(x + t * (y-x) for x, y in zip(first, last))
                if math.dist(a, b) >= 2. * paint.WHITE_CORE_WIDTH:
                    hatches.append((a, b))
                break
    dashes = []
    for index in range(math.ceil(nose[0] / 4.)):
        start = max(index * 4., .65 * taper)
        end = min(index * 4. + 2., nose[0] - .25)
        if end - start > .05:
            dashes.append(((start, 4.5), (end, 4.5)))
    return {'outer_edge': outer, 'gore_outline': outline, 'gore_inner': inner,
            'gore_nose': nose, 'hatches': hatches, 'dashes': dashes,
            'core_width_m': paint.WHITE_CORE_WIDTH, 'outer_controls': controls}


def surfaces(route):
    layout = marking_layout(route)
    faces = []
    for first, last in layout['dashes'] + layout['hatches']:
        faces.extend(paint._stripe(route, first, last))
    faces.extend(paint._stripe_path(route, layout['outer_edge'], maximum_q=8.))
    faces.extend(paint._stripe_path(route, layout['gore_outline'], maximum_q=8.))
    # A lane's diagonal outer port is not a perpendicular road-width cut.
    # Clip the complete white core at the actual city edge; the adjoining
    # native highway supplies its own continuing shoulder outside this plot.
    from .parallel_layout import GROUPS
    cells = {cell for _name, owned, _role in GROUPS.values() for cell in owned}
    return [tuple((p[0] + 16.*cell[0], p[1], p[2] + 16.*cell[1], *p[3:]) for p in face)
            for cell, triangles in geometry.partition_triangles(faces).items() if cell in cells
            for face in triangles]
