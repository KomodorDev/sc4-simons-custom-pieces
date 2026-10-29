"""Independent saved-face contract for the two recessed-end concrete wedges."""
from __future__ import annotations

import math
from scp.dbpf import require
from .hsr_mesh_verify import _intersection_polygon, _area, _minimum_strip_width

TOP = 16.98932647705078
BED = 16.1893253326416
BOTTOM = 14.01067066192627
INNER = 10.00345230102539
SECTIONS = ((24.01, 4.956438471), (26., 5.451649720),
            (28., 5.988989542), (30., 6.561077604),
            (32., 7.162374702), (34., 7.786913230),
            (36., 8.428414018), (38., 9.080398640),
            (40., 9.736297220))


def _section(triangles, z, height):
    intervals = []
    for triangle in triangles:
        if not all(abs(p[1]-height) < 4e-5 for p in triangle):
            continue
        hits = []
        for a, b in zip(triangle, triangle[1:]+triangle[:1]):
            if abs(b[2]-a[2]) < 1e-10:
                continue
            fraction = (z-a[2])/(b[2]-a[2])
            if -1e-9 <= fraction <= 1.+1e-9:
                hits.append(a[0]+fraction*(b[0]-a[0]))
        if len(hits) >= 2:
            intervals.append((min(hits), max(hits)))
    return intervals


def _union(intervals):
    result = []
    for low, high in sorted(intervals):
        if high-low < 1e-7:
            continue
        if result and low <= result[-1][1]+4e-5:
            result[-1] = (result[-1][0], max(high, result[-1][1]))
        else:
            result.append((low, high))
    return result


def _walls(triangles, z, height):
    hits = []
    for triangle in triangles:
        if max(p[1] for p in triangle)-min(p[1] for p in triangle) < .1:
            continue
        horizontal = []
        for a, b in zip(triangle, triangle[1:]+triangle[:1]):
            if abs(b[1]-a[1]) < 1e-10:
                continue
            f = (height-a[1])/(b[1]-a[1])
            if -1e-9 <= f <= 1.+1e-9:
                horizontal.append((a[0]+f*(b[0]-a[0]), a[2]+f*(b[2]-a[2])))
        if len(horizontal) < 2:
            continue
        a, b = horizontal[0], horizontal[-1]
        if abs(b[1]-a[1]) < 1e-10:
            continue
        f = (z-a[1])/(b[1]-a[1])
        if -1e-8 <= f <= 1.+1e-8:
            hits.append(a[0]+f*(b[0]-a[0]))
    return hits


def audit_symmetric_wedges(triangles):
    """Reject the old gaps, a flat patch, missing walls, and overlapping roofs."""
    roof_checks, wall_checks = 0, 0
    for z, left in SECTIONS:
        for low, high in ((left, INNER), (32.-INNER, 32.-left)):
            nearby = [(max(a, low-.01), min(b, high+.01))
                      for a, b in _section(triangles, z, TOP) if b >= low-.01 and a <= high+.01]
            union = _union(nearby)
            require(len(union) == 1 and abs(union[0][0]-low) < 5e-5
                    and abs(union[0][1]-high) < 5e-5,
                    f'Symmetric HSR concrete wedge roof is interrupted at south {z}: {union}')
            roof_checks += 1
            hits = _walls(triangles, z, (BED+TOP)/2.)
            require(all(any(abs(x-boundary) < 5e-5 for x in hits) for boundary in (low, high)),
                    f'Symmetric HSR wedge lacks a matching inside wall at south {z}')
            wall_checks += 2
    bottom_checks = 0
    for z, low in ((26., 6.898289123), (28., 7.442510416), (30., 8.020782870)):
        for a, b in ((low, 8.5), (23.5, 32.-low)):
            intervals = _union([(max(x, a), min(y, b)) for x, y in _section(triangles, z, BOTTOM)
                                if y > a and x < b])
            require(len(intervals) == 1 and abs(intervals[0][0]-a) < 5e-5
                    and abs(intervals[0][1]-b) < 5e-5,
                    'Symmetric HSR wedge is missing its closed underside')
            bottom_checks += 1
    cap_checks = 0
    for low, high in ((6.393693924, 8.5), (23.5, 25.606306076)):
        target = [(low, BOTTOM), (high, BOTTOM), (high, TOP), (low, TOP)]
        area = 0.
        for triangle in triangles:
            if all(abs(p[2]-24.) < 4e-5 for p in triangle):
                cut = _intersection_polygon([(p[0], p[1]) for p in triangle], target)
                if len(cut) >= 3:
                    area += _area(cut)
        require(abs(area-(high-low)*(TOP-BOTTOM)) < .0002,
                'Symmetric HSR wedge has an open recessed-plane end cap')
        cap_checks += 1
    # Inspect actual float32 roof intersections, independently of generation.
    roofs = [tuple((p[0], p[2]) for p in t) for t in triangles
             if all(abs(p[1]-TOP) < 4e-5 for p in t)
             and min(p[2] for p in t) <= 42. and max(p[2] for p in t) >= 24.
             and max(p[0] for p in t) >= 4.8 and min(p[0] for p in t) <= 27.2]
    bounds = [(min(p[0] for p in t), max(p[0] for p in t), min(p[1] for p in t), max(p[1] for p in t)) for t in roofs]
    buckets, checked, maximum = {}, set(), 0.
    for number, polygon in enumerate(roofs):
        for x in range(math.floor(min(p[0] for p in polygon)/4.), math.floor(max(p[0] for p in polygon)/4.)+1):
            for z in range(math.floor(min(p[1] for p in polygon)/4.), math.floor(max(p[1] for p in polygon)/4.)+1):
                for other in buckets.setdefault((x, z), []):
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
                            'Symmetric HSR wedge has overlapping concrete roofs')
                buckets[x, z].append(number)
    return {'symmetric_wedge_top_sections_checked': roof_checks,
            'symmetric_wedge_inside_wall_sections_checked': wall_checks,
            'symmetric_wedge_underside_sections_checked': bottom_checks,
            'symmetric_wedge_closed_end_caps_checked': cap_checks,
            'symmetric_wedge_top_overlap_pairs_checked': len(checked),
            'symmetric_wedge_maximum_top_overlap_area_m2': maximum,
            'symmetric_wedge_branch_inner_half_width_m': 2.6,
            'symmetric_wedge_meshing_tolerance_m': .0001,
            'symmetric_wedge_end_plane_local_south_m': 24.}
