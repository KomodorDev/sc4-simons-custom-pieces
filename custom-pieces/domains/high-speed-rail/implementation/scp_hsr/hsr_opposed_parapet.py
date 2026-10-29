"""Continue only the opposed-merge concrete borders along existing ballast.

The mainline, two actual branches, and unused analytic context retain their
native sweeps. This opt-in wrapper changes raised concrete only: continuous
inner outlines meet the existing wings, and both opposite strips continue
along their own native inside outlines without perpendicular end caps.
"""
from __future__ import annotations

from scp.dbpf import require


def sweep_opposed_parapet(source, deck, swept):
    """Wrap the original native sweep for one explicitly flagged junction."""
    from .rail_geometry import _route, _convex_parts
    from .single_track_models import _clip, _triangulate

    surfaces, corridors, points, lengths = swept
    rule = deck['opposed_parapet_alignment']
    east0, south0 = rule['source_east_offset_m'], rule['source_south_offset_m']
    half = rule['branch_inner_half_width_m']
    require(half == 2.6 and rule['mainline_half_width_m'] == 7.5
            and all(abs(point[1]-15.5) < 1e-8 for point in points),
            'Opposed border alignment requires its exact flat L2 profiles')
    require(rule['outer_join_mode'] == 'continuous_branch_inside_outline',
            'Opposed outer strips require their own continuous native outlines')
    name = deck['name']
    if name != rule['mainline']:
        require(deck['width'] == 8. and corridors,
                'Opposed border opening requires its native single branch')
        route, _, miters = _route(deck['points'], deck.get('start_tangent'), deck.get('end_tangent'))
        polygons = []
        for a, b, na, nb in zip(route, route[1:], miters, miters[1:]):
            polygons.extend(_convex_parts([
                (p[0]+cross*n[0], p[2]+cross*n[1])
                for p, n, cross in ((a, na, -half), (a, na, half),
                                    (b, nb, half), (b, nb, -half))]))
        corridors[0]['parapet_opening_polygons'] = polygons
        changed = list(surfaces)
        side = -1. if name == rule['north_branch'] else 1.
        if name in (rule['north_branch'], rule['south_branch']):
            split = east0+rule['north_selection_limit_local_east_m' if side < 0.
                               else 'south_selection_limit_local_east_m']
            for kind, triangle in surfaces:
                if kind != 'inner_wall':
                    continue
                for region in (lambda v: -side*(split-v[0]),
                               lambda v: side*(split-v[0])):
                    polygon = list(triangle)
                    for plane in (lambda v: side*(v[2]-south0)-source['inner'],
                                  lambda v: 7.5-side*(v[2]-south0), region):
                        polygon = _clip(polygon, plane)
                    # Keep the accepted bank's exact split first, then close
                    # the separate outer bank using the other native face.
                    changed.extend(('aligned_inner_wall', part)
                                   for part in _triangulate(polygon))
        return changed, corridors, points, lengths

    require(deck['width'] == 15. and len(points) == 2
            and all(abs(point[2]-south0) < 1e-8 for point in points),
            'Opposed border alignment requires its original straight mainline')
    changed = []
    for kind, triangle in surfaces:
        side = -1. if max(v[2] for v in triangle) < south0 else 1.
        if (kind != 'wall'
                or min(side*(v[2]-south0) for v in triangle) < source['inner']-1e-5
                or max(v[1] for v in triangle) <= source['bed_y']+1e-5):
            changed.append((kind, triangle))
            continue
        if min(v[1] for v in triangle) < source['bed_y']-1e-5:
            lower = _clip(list(triangle), lambda v: source['bed_y']-v[1])
            changed.extend((kind, part) for part in _triangulate(lower))
        upper = _clip(list(triangle), lambda v: v[1]-source['bed_y'])
        split = east0+rule['north_selection_limit_local_east_m' if side < 0.
                           else 'south_selection_limit_local_east_m']
        continuing = _clip(upper, lambda v: -side*(split-v[0]))
        following_kind = (kind if all(abs(side*(v[2]-south0)-source['outer']) < 1e-5
                                     for v in triangle) else 'following_parapet')
        changed.extend((following_kind, part) for part in _triangulate(continuing))
        opposite = _clip(upper, lambda v: side*(split-v[0]))
        changed.extend((following_kind, part) for part in _triangulate(opposite))
    # Both outer tops meet the original curved wings along the same inside
    # faces. Their outside contour still uses the original full-deck cuts;
    # no perpendicular cap or internal outer side wall interrupts the join.
    return changed, corridors, points, lengths
