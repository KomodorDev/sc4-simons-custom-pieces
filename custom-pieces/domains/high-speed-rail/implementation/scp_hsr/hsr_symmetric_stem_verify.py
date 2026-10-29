"""Literal, independent saved-face contract for both southern stem parapets."""
from __future__ import annotations

import math

from scp.dbpf import require
from .hsr_mesh_verify import _intersection_polygon, _area, _minimum_strip_width
from .hsr_symmetric_parapet_verify import TOP, BED, _section, _union, _walls

INNER = 10.00345230102539
JOIN_SOUTH = 60.52424146049998
# Local south, outside roof edge, inside roof/wall edge. These describe the
# actual native paired profile and inspected branch ballast-line intersections.
STEM_SECTIONS = (
    (48., 5.372675514, 6.837625298),
    (50., 5.979215340, 7.438922396),
    (52., 6.557487794, 8.011010458),
    (54., 7.101708864, 8.548350280),
    (56., 7.606305927, 9.045952258),
    (58., 8.066792671, 9.499501525),
    (60., 8.479455089, 9.905406939),
    (60.524, 8.5, 10.00340848),
    (JOIN_SOUTH, 8.5, INNER),
    (61., 8.5, INNER),
    (62., 8.5, INNER),
    (64., 8.5, INNER),
    (68., 8.5, INNER),
    (72., 8.5, INNER),
    (80., 8.5, INNER),
    (87.9, 8.5, INNER),
)


def audit_symmetric_stem(triangles):
    """Reject the previous pinch, early turn, open wall, and duplicate roof."""
    roof_checks, wall_checks = 0, 0
    for south, outer, inner in STEM_SECTIONS:
        for low, high in ((outer, inner), (32.-inner, 32.-outer)):
            intervals = [(max(a, low-.03), min(b, high+.03))
                         for a, b in _section(triangles, south, TOP)
                         if b >= low-.03 and a <= high+.03]
            union = _union(intervals)
            require(len(union) == 1 and abs(union[0][0]-low) < 5e-5
                    and abs(union[0][1]-high) < 5e-5,
                    f'Symmetric HSR stem roof differs from its straight-to-ballast outline at south {south}: {union}')
            roof_checks += 1
            hits = _walls(triangles, south, (BED+TOP)/2.)
            require(all(any(abs(x-edge) < 5e-5 for x in hits) for edge in (low, high)),
                    f'Symmetric HSR stem lacks a matching inside wall at south {south}')
            wall_checks += 2
    roofs = [tuple((p[0], p[2]) for p in t) for t in triangles
             if all(abs(p[1]-TOP) < 4e-5 for p in t)
             and min(p[2] for p in t) <= 88. and max(p[2] for p in t) >= 48.]
    require(all(any(any(abs(p[0]-east) < 5e-5 and abs(p[1]-JOIN_SOUTH) < 5e-5
                        for p in triangle) for triangle in roofs)
                for east in (INNER, 32.-INNER)),
            'Symmetric HSR stem has no exact straight-to-curve roof join')
    bounds = [(min(p[0] for p in t), max(p[0] for p in t),
               min(p[1] for p in t), max(p[1] for p in t)) for t in roofs]
    buckets, checked, maximum = {}, set(), 0.
    for number, polygon in enumerate(roofs):
        for east in range(math.floor(min(p[0] for p in polygon)/4.),
                          math.floor(max(p[0] for p in polygon)/4.)+1):
            for south in range(math.floor(min(p[1] for p in polygon)/4.),
                               math.floor(max(p[1] for p in polygon)/4.)+1):
                for other in buckets.setdefault((east, south), []):
                    a, b = bounds[number], bounds[other]
                    if min(a[1], b[1])-max(a[0], b[0]) <= 1e-9 or min(a[3], b[3])-max(a[2], b[2]) <= 1e-9:
                        continue
                    if (other, number) in checked:
                        continue
                    checked.add((other, number))
                    overlap = _intersection_polygon(polygon, roofs[other])
                    area = _area(overlap) if len(overlap) >= 3 else 0.
                    maximum = max(maximum, area)
                    require(area <= 1e-6 or _minimum_strip_width(overlap) <= .0001,
                            'Symmetric HSR stem has overlapping concrete roofs')
                buckets[east, south].append(number)
    return {'symmetric_stem_top_sections_checked': roof_checks,
            'symmetric_stem_inside_wall_sections_checked': wall_checks,
            'symmetric_stem_straight_to_curve_joins_checked': 2,
            'symmetric_stem_join_local_south_m': JOIN_SOUTH,
            'symmetric_stem_native_inside_east_m': [INNER, 32.-INNER],
            'symmetric_stem_branch_inner_half_width_m': 2.6,
            'symmetric_stem_top_overlap_pairs_checked': len(checked),
            'symmetric_stem_maximum_top_overlap_area_m2': maximum,
            'symmetric_stem_meshing_tolerance_m': .0001}
