"""Close the compact fan's central parapet against its actual ballast faces.

Only the inside cap and inside wall of each explicitly named arm change.
Their existing tapered clearance polygons supply the curved inside limit;
the exact reflection plane gives disjoint ownership where the caps meet.
"""
from __future__ import annotations

import math

from scp.dbpf import require


def corrected_fan_sweeps(source, decks, rule):
    from .hsr_components import _sweep_component_profile
    from .rail_geometry import _convex_parts, _index_corridors, _subtract_corridors
    from .single_track_models import _clip, _triangulate

    require(rule['reflection_axis_source_east_m'] == 96.
            and rule['inside_sides'] == {'native_y_left': 1, 'native_y_right': -1}
            and {deck['name'] for deck in decks} == set(rule['inside_sides']),
            'Central fan parapet requires its two exact reflected arms')
    swept = [_sweep_component_profile(source, deck) for deck in decks]
    # The shoulder warp is nonlinear. Warping the expanded clearance mask
    # and warping the native inside face separately differs by fractions of
    # a millimetre at a miter. Use the actual retained wall's top edges for
    # both sides of each new cap, rather than accepting that small open seam.
    exact_clearance = {}
    for deck, (surfaces, corridors, _, _) in zip(decks, swept):
        by_station = {}
        for kind, triangle in surfaces:
            if kind != 'inner_wall':
                continue
            edge = [v for v in triangle if abs(v[1]-source['top']) < 1e-5]
            if len(edge) == 2:
                edge.sort(key=lambda v: v[4])
                key = tuple(round(v[4], 9) for v in edge)
                by_station.setdefault(key, []).append(edge)
        polygons = []
        for edges in by_station.values():
            if len(edges) != 2:
                # Endpoint clipping can create additional short edge fans;
                # it lies far outside this central repair's literal window.
                continue
            a, b = edges
            polygons.extend(_convex_parts([(v[0], v[2]) for v in (a[0], a[1], b[1], b[0])]))
        require(polygons and corridors, 'Fan parapet lacks paired native inside-wall edges')
        exact_clearance[deck['name']] = [{**corridors[0], 'polygon': polygon} for polygon in polygons]
    all_clearance = _index_corridors([
        corridor for corridors in exact_clearance.values() for corridor in corridors], True)
    axis = rule['reflection_axis_source_east_m']
    result = {}
    for deck, (surfaces, corridors, points, lengths) in zip(decks, swept):
        require(deck['width'] == 8. and deck['clearance_half_width'] == 2.6
                and deck['flat_paired_collar_height'] == 15.5
                and all(abs(point[1]-15.5) < 1e-8 for point in points),
                'Central fan parapet requires unchanged flat L2 fan profiles')
        side = rule['inside_sides'][deck['name']]
        buckets = {}
        for number, (a, b) in enumerate(zip(points, points[1:])):
            for x in range(math.floor((min(a[0], b[0])-6.)/8.),
                           math.floor((max(a[0], b[0])+6.)/8.)+1):
                for z in range(math.floor((min(a[2], b[2])-6.)/8.),
                               math.floor((max(a[2], b[2])+6.)/8.)+1):
                    buckets.setdefault((x, z), []).append(number)

        def inside(triangle):
            x = sum(v[0] for v in triangle)/3.
            z = sum(v[2] for v in triangle)/3.
            nearest = None
            for number in buckets.get((math.floor(x/8.), math.floor(z/8.)), []):
                a, b = points[number:number+2]
                dx, dz = b[0]-a[0], b[2]-a[2]
                length = lengths[number]
                t = max(0., min(1., ((x-a[0])*dx+(z-a[2])*dz)/(length*length)))
                ox, oz = x-a[0]-t*dx, z-a[2]-t*dz
                candidate = ox*ox+oz*oz, (ox*dz-oz*dx)/length
                if nearest is None or candidate[0] < nearest[0]:
                    nearest = candidate
            require(nearest is not None, 'Fan parapet lacks its existing route segment')
            return side*nearest[1] > 0.

        changed = []
        other_clearance = _index_corridors([
            corridor for name, cs in exact_clearance.items() if name != deck['name']
            for corridor in cs], True)
        for kind, triangle in surfaces:
            cap = kind == 'wall' and all(abs(v[1]-source['top']) < 1e-5 for v in triangle)
            wall = kind == 'inner_wall'
            # Only the central fork collar can contain this overlap. The
            # literal window leaves the retained distant wings on the exact
            # original compilation path, including their triangulation.
            near_fork = (min(v[2] for v in triangle) <= 54.
                         and max(v[2] for v in triangle) >= 44.
                         and min(v[0] for v in triangle) <= 104.
                         and max(v[0] for v in triangle) >= 88.)
            if not (cap or wall) or not near_fork or not inside(triangle):
                changed.append((kind, triangle))
                continue
            # Each half retains its native UVs and exact curved inner edge.
            # The meeting plane is internal to the solid, not an exposed end.
            polygon = _clip(list(triangle), lambda v: side*(axis-v[0]))
            for part in _triangulate(polygon):
                cuts = all_clearance if cap else other_clearance
                for fragment in _subtract_corridors(part, cuts, wall=True):
                    # Both kinds have already been cut against the exact
                    # original wall boundaries. Do not apply the separately
                    # warped clearance mask to the new top a second time.
                    changed.append(('preclipped_parapet' if cap else 'aligned_inner_wall', fragment))
        result[deck['name']] = changed, corridors, points, lengths
    return result
