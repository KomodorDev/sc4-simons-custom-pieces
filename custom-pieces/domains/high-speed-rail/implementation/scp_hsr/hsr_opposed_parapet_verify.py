"""Independent literal checks of saved opposed-merge concrete borders."""
from __future__ import annotations

import math

from scp.dbpf import require

INNER, OUTER, BED, TOP = 5.9965477, 7.5, 16.1893253, 16.9893265
NORTH_CAP, SOUTH_CAP = 43.76798391999034, 4.223921717723081
CONTINUOUS_SECTIONS = ((8., INNER, OUTER), (16., INNER, OUTER),
                       (20., INNER, OUTER),
                       (21., 6.087372560, 7.503469160),
                       (22., 6.243395951, 7.661687198),
                       (24., 6.589828567, 8.), (26., 6.985743322, 8.),
                       (28., 7.435250367, 8.), (30., 7.942643462, 8.))

# These independently measured native outlines have different source samples.
# Northern curve values must not be reflected from the southern curve.
OUTER_JOIN_POINTS = {
    'north': (
        (40.361872522872716, INNER), (40.49959012004575, 6.054360021125547),
        (40.69244178817003, 6.136462356674514), (40.882912920452895, 6.218276280396111),
        (41.07323363742216, 6.300763252994415), (41.26339746176359, 6.38393256537303),
        (41.45339781410213, 6.467793476528669), (41.643228011681444, 6.552355212202386),
        (41.83288126705301, 6.637626963504545), (42.022350686777486, 6.723617885514599),
        (42.211629270136484, 6.81033709585418), (42.400709907856296, 6.897793673233579),
        (42.589585380844596, 6.9859966559719595), (42.77824835893911, 7.074955040489911),
        (42.96669139966953, 7.164677779774792), (43.15490694703385, 7.255173781818556),
        (43.34288733028845, 7.346451908027632), (43.53062476275295, 7.438520971604575),
        (43.65474068840744, OUTER),
    ),
    'south': (
        (7.638127477127277, INNER), (7.498183417659945, 6.055294665339915),
        (7.083640643927524, 6.232687350697361), (6.669993955229849, 6.4131015316698665),
        (6.257269773156125, 6.596551049678709), (5.845494741096999, 6.783049131744306),
        (5.434695714200288, 6.972608383111506), (5.024899749078749, 7.1652407801775695),
        (4.616134093278291, 7.360957663730829), (4.330997170307948, OUTER),
    ),
}


def _outer_wall_facets(triangles, points, side):
    """Require complete bed-to-top faces without duplicate coplanar area."""
    from .hsr_compact_fan_verify import _clip_attribute_polygon
    from .hsr_mesh_verify import _component_union_area, _area

    measured = []
    for first, last in zip(points, points[1:]):
        a, b = (first[0], side*first[1]), (last[0], side*last[1])
        dx, dz = b[0]-a[0], b[1]-a[1]
        length = math.hypot(dx, dz)
        polygons = []
        for triangle in triangles:
            if not all(abs(dx*(v[2]-a[1])-dz*(v[0]-a[0]))/length <= .00005
                       for v in triangle):
                continue
            polygon = [(((v[0]-a[0])*dx+(v[2]-a[1])*dz)/length,
                        v[1], 0., 0., 0.) for v in triangle]
            for plane in (lambda v: v[0], lambda v: length-v[0],
                          lambda v: v[1]-BED, lambda v: TOP-v[1]):
                if polygon:
                    polygon = _clip_attribute_polygon(polygon, plane, True)
            if len(polygon) >= 3:
                polygons.append([(v[0], v[1]) for v in polygon])
        area = _component_union_area(polygons)
        overlap = sum(_area(poly) for poly in polygons)-area
        require(abs(area-length*(TOP-BED)) <= .0001,
                'Opposed outer curved inside wall has incomplete vertical coverage')
        require(overlap <= .0001,
                'Opposed outer curved inside wall has duplicate coplanar faces')
        measured.append({'start_east_distance_m': first, 'end_east_distance_m': last,
                         'saved_vertical_union_area_m2': area,
                         'expected_vertical_area_m2': length*(TOP-BED),
                         'duplicate_area_m2': overlap})
    return measured


def audit_opposed_parapet_alignment(triangles):
    """Preserve both accepted banks and require continuous outer X0/X3 joins."""
    from .hsr_atomic_components_verify import _section_intervals, _wall_section_south_positions
    from .hsr_compact_fan_verify import _clip_attribute_polygon
    from .hsr_mesh_verify import _component_union_area, _area

    triangles = list(triangles)
    tolerance, top_sections, inside_sections = .00005, 0, 0
    joins, overlap_areas = [], []
    for name, side, old_cap, split in (('north', -1., NORTH_CAP, 32.),
                                        ('south', 1., SOUTH_CAP, 16.)):
        transform = (lambda east: east) if side < 0. else (lambda east: 48.-east)
        sections = [(transform(east), inside, outside)
                    for east, inside, outside in CONTINUOUS_SECTIONS]
        curve = OUTER_JOIN_POINTS[name]
        samples = [(east, [(inside, outside)], 8.) for east, inside, outside in sections]
        samples.extend((transform(east), [], OUTER) for east in (31., 32., 40.))
        samples.extend((east, [(INNER, distance)], OUTER) for east, distance in curve[1:])
        samples.extend((east, [(INNER, OUTER)], OUTER)
                       for east in ((48., 55.) if side < 0. else (0., -7.)))
        for east, expected, limit in samples:
            intervals = _section_intervals(triangles, 'east', east, TOP, 0.)
            distances = sorted((min(-side*a, -side*b), max(-side*a, -side*b))
                               for a, b in intervals)
            actual = [(max(a, INNER), min(b, limit)) for a, b in distances
                      if min(b, limit)-max(a, INNER) > tolerance]
            require(len(actual) == len(expected) and all(
                abs(a-c) <= tolerance and abs(b-d) <= tolerance
                for (a, b), (c, d) in zip(actual, expected)),
                f'Opposed parapet does not follow its continuous ballast outline: side={side}, '
                f'east={east}, actual={actual}, expected={expected}')
            top_sections += 1
        wall_sections = [(east, inside) for east, inside, _ in sections]
        wall_sections.extend(curve[1:])
        wall_sections.extend((east, INNER) for east, _ in curve[1:])
        for east, inside in wall_sections:
            actual = _wall_section_south_positions(triangles, east, (BED+TOP)/2.)
            require(any(abs(south-side*inside) <= tolerance for south in actual),
                    f'Opposed parapet has no closed inside face: side={side}, east={east}')
            inside_sections += 1

        outer_tops, cap_polygons, all_tops = [], [], []
        for triangle in triangles:
            if all(abs(p[1]-TOP) <= tolerance for p in triangle):
                polygon = list(triangle)
                for plane in (lambda p: p[0]+8., lambda p: 56.-p[0],
                              lambda p: side*p[2]-INNER, lambda p: OUTER-side*p[2]):
                    if polygon:
                        polygon = _clip_attribute_polygon(polygon, plane, True)
                if len(polygon) >= 3:
                    all_tops.append([(p[0], p[2]) for p in polygon])
                    polygon = _clip_attribute_polygon(polygon, lambda p: side*(split-p[0]), True)
                    if len(polygon) >= 3:
                        outer_tops.append([(p[0], p[2]) for p in polygon])
            if all(abs(p[0]-old_cap) <= tolerance for p in triangle):
                polygon = list(triangle)
                for plane in (lambda p: side*p[2]-INNER, lambda p: OUTER-side*p[2],
                              lambda p: p[1]-BED, lambda p: TOP-p[1]):
                    if polygon:
                        polygon = _clip_attribute_polygon(polygon, plane, True)
                if len(polygon) >= 3:
                    cap_polygons.append([(p[1], p[2]) for p in polygon])
        overlap_area = sum(_area(poly) for poly in all_tops)-_component_union_area(all_tops)
        require(overlap_area <= .0001, 'Opposed parapet has overlapping concrete tops')
        overlap_areas.append(overlap_area)
        end = 56. if side < 0. else -8.
        reference = [curve[0], (end, INNER), (end, OUTER), *reversed(curve[1:])]
        expected_area = _area(reference)
        saved_area = _component_union_area(outer_tops)
        require(abs(saved_area-expected_area) <= .0003,
                'Opposed outer parapet has an incomplete curved join or a roof in its opening')
        require(_component_union_area(cap_polygons) <= .0001,
                'Opposed continuous outer parapet retains a perpendicular end cap')
        joins.append({'side': name, 'inner_join_east_m': curve[0][0],
                      'outer_join_east_m': curve[-1][0],
                      'saved_top_union_area_m2': saved_area,
                      'expected_top_union_area_m2': expected_area,
                      'curved_wall_facets': _outer_wall_facets(triangles, curve, side)})
    return {'opposed_parapet_top_sections_checked': top_sections,
            'opposed_parapet_inside_wall_sections_checked': inside_sections,
            'opposed_parapet_closed_end_faces_checked': 0,
            'opposed_parapet_outer_perpendicular_caps_absent': True,
            'opposed_parapet_outer_joins': joins,
            'opposed_parapet_maximum_top_overlap_area_m2': max(overlap_areas)}
