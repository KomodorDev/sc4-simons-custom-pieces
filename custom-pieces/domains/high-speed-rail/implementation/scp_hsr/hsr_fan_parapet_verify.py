"""Independent saved-face sections for the compact fan's central border."""
from __future__ import annotations

from scp.dbpf import require
from .hsr_atomic_components_verify import _section_intervals
from .hsr_compact_fan_verify import _clip_attribute_polygon
from .hsr_mesh_verify import _component_union_area
from .directional_t_verify import _area

BED, TOP = 16.1893253, 16.9893265
SECTIONS = (
    (48., ()), (49., ()),
    (50., ((47.730789429, 48.269210964),)),
    (52., ((46.935293122, 49.064706878),)),
    (54., ((45.998660419, 47.602892730), (48.397107845, 50.001339581))),
    (56., ((44.924741434, 46.557391878), (49.442608583, 51.075258566))),
)


def _wall_cuts(triangles, south, height):
    found = []
    for triangle in triangles:
        if max(v[1] for v in triangle)-min(v[1] for v in triangle) < .1:
            continue
        cuts = []
        for a, b in zip(triangle, triangle[1:]+triangle[:1]):
            if abs(a[2]-south) < 1e-8:
                cuts.append(a)
            if min(a[2], b[2]) < south < max(a[2], b[2]):
                t = (south-a[2])/(b[2]-a[2])
                cuts.append(tuple(x+t*(y-x) for x, y in zip(a, b)))
        for a, b in zip(cuts, cuts[1:]+cuts[:1]):
            if abs(a[1]-height) < 1e-8:
                found.append(a[0])
            if min(a[1], b[1]) < height < max(a[1], b[1]):
                t = (height-a[1])/(b[1]-a[1])
                found.append(a[0]+t*(b[0]-a[0]))
    return found


def audit_central_parapet(triangles):
    """Require the raised fork nose, both inside faces, and disjoint caps.

    Literal expected sections use the unchanged tapered ballast boundaries.
    The complete model's existing five-metre train envelope remains separate.
    """
    triangles = list(triangles)
    tolerance = .00005
    wall_checks = 0
    for south, expected in SECTIONS:
        actual = [(max(a+48., 44.), min(b+48., 52.)) for a, b in
                  _section_intervals(triangles, 'north', -south, TOP, 48.)
                  if min(b+48., 52.)-max(a+48., 44.) > tolerance]
        require(len(actual) == len(expected) and all(
            abs(a-c) <= tolerance and abs(b-d) <= tolerance
            for (a, b), (c, d) in zip(actual, expected)),
            f'Compact fan central parapet has an interrupted ballast outline: '
            f'south={south}, actual={actual}, expected={expected}')
        # The untouched wing at south56m retains its historical native
        # triangulation. Closed-face checks target the repaired nose and join.
        if expected and south <= 54.:
            positions = _wall_cuts(triangles, south, (BED+TOP)/2.)
            for east in (expected[0][0], expected[-1][1]):
                require(any(abs(east-value) <= tolerance for value in positions),
                        f'Compact fan central parapet has no closed inside face: '
                        f'south={south}, east={east}')
                wall_checks += 1
    polygons = []
    for triangle in triangles:
        if not all(abs(v[1]-TOP) <= tolerance for v in triangle):
            continue
        polygon = list(triangle)
        for plane in (lambda v: v[0]-44., lambda v: 52.-v[0],
                      lambda v: v[2]-49., lambda v: 56.-v[2]):
            polygon = _clip_attribute_polygon(polygon, plane, True) if polygon else []
        if len(polygon) >= 3:
            polygons.append([(v[0], v[2]) for v in polygon])
    summed = sum(_area(polygon) for polygon in polygons)
    union = _component_union_area(polygons)
    require(summed-union <= .0001,
            'Compact fan central parapet has overlapping concrete top faces')
    return {'central_parapet_top_sections_checked': len(SECTIONS),
            'central_parapet_inside_wall_sections_checked': wall_checks,
            'central_parapet_top_union_area_m2': union,
            'central_parapet_top_overlap_area_m2': max(0., summed-union),
            'central_parapet_reflection_axis_local_east_m': 48.}
