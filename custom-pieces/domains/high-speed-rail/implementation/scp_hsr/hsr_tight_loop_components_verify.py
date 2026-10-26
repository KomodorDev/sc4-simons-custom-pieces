"""Reviewed literal contracts for the two new 56 m paired graded corners.

Expected ports, masks, physical profiles and supports do not come from the
writer or INFO tables. All established curvature, grade, native collar and
train-clearance limits are retained.
"""
import math

from scp.dbpf import require

COMMON = {
    'clearance_width_m': 5., 'minimum_clearance': 5.,
    'foundation_width_m': 1.3, 'minimum_support_spacing_m': 16.,
    'allow_same_edge': False, 'required_grade_separated_crossings': 0,
    'flat_collar_m': 8., 'max_grade': .156251,
    'kind': 'tight_paired_curved_grade', 'footprint': (4, 4), 'cost': 1000,
    'cells': [(0, 0), (1, 0), (2, 0), (3, 0),
              (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (0, 3)],
    'structural_cells': [(0, 0), (2, 1), (1, 2)],
    'port_vectors': {'Sin': (0., 1.), 'Sout': (0., -1.),
                     'Eout': (1., 0.), 'Ein': (-1., 0.)},
    'movements': [('Sin', 'Eout'), ('Ein', 'Sout')],
    'support_centres_xz': [(16., 0.), (32., 0.), (48., 0.),
                            (0., 16.), (0., 32.), (0., 48.)],
}
QUALITY = {
    'max_length_ratio': 1.55, 'min_total_turn_degrees': 89.,
    'max_total_turn_degrees': 91., 'max_sample_turn_degrees': 8.,
    'max_raw_turn_degrees': 3., 'min_radius_m': 24.,
    'max_curvature_change_per_m2': .0015,
    'max_endpoint_curvature_per_m': .0005, 'max_grade_change_per_m': .011,
}


def _contract(first, last):
    return {
        **COMMON, 'min_height': min(first, last), 'max_height': max(first, last),
        'ports': {'Sin': (2., -56., first), 'Sout': (-2., -56., first),
                  'Ein': (56., 2., last), 'Eout': (56., -2., last)},
        'quality_limits': {
            ('Sin', 'Eout'): {**QUALITY, 'min_length_m': 93., 'max_length_m': 95.,
                              'signed_turn_degrees': -90.},
            ('Ein', 'Sout'): {**QUALITY, 'min_length_m': 99., 'max_length_m': 101.,
                              'signed_turn_degrees': 90.},
        },
    }


CONTRACTS = {
    'hsr_component_tight_paired_curve90_l4_to_mid': _contract(30.5, 23.),
    'hsr_component_tight_paired_curve90_mid_to_l2': _contract(23., 15.5),
}


def audit_tight_journeys(journeys, recipe):
    """Ensure both offset paths follow one physical graded sheet.

    Independently encoded grid cuts differ between the two tracks. Exclude
    those exact tile-boundary cuts, then match every remaining actual vertex
    to its four-metre, equal-height counterpart. This avoids comparing a
    vertex with an unrelated nearest chord station. Native ports, boundary
    cuts and complete physical rail beds are checked by the existing audits.
    """
    CONTRACTS[recipe]
    first = journeys['Sin', 'Eout']
    second = list(reversed(journeys['Ein', 'Sout']))
    maximum_distance_error = maximum_height_error = 0.
    checked = boundary_cuts = 0
    for line, opposite in ((first, second), (second, first)):
        for point in line:
            if any(abs(value-(16.*round((value+8.)/16.)-8.)) <= 2e-6
                   for value in point[:2]):
                boundary_cuts += 1
                continue
            candidates = [(abs(math.dist(point[:2], other[:2])-4.),
                           abs(point[2]-other[2])) for other in opposite
                          if abs(point[2]-other[2]) <= 2e-6]
            require(bool(candidates),
                    'Tight paired corner tracks do not follow one shared-height sheet at four-metre spacing')
            distance_error, height_error = min(candidates)
            maximum_distance_error = max(maximum_distance_error, distance_error)
            maximum_height_error = max(maximum_height_error, height_error)
            require(distance_error <= 3e-6 and height_error <= 2e-6,
                    'Tight paired corner tracks do not follow one shared-height sheet at four-metre spacing')
            checked += 1
    require(checked >= 1000, 'Tight paired corner lacks its complete encoded shared-sheet vertex proof')
    return {'paired_shared_sheet_points_checked': checked,
            'tile_boundary_cuts_checked_by_seam_and_bed_audits': boundary_cuts,
            'paired_track_spacing_m': 4.,
            'maximum_paired_spacing_error_m': maximum_distance_error,
            'maximum_paired_shared_height_error_m': maximum_height_error,
            'custom_midpoint_height_m': 23.}


def audit_tight_native_profiles(triangles, recipe):
    """Check both full native collars, including underneath and parapets."""
    from .hsr_components_verify import _section_intervals
    contract = CONTRACTS[recipe]
    triangles = list(triangles)
    swapped = [tuple((p[2], p[1], p[0], p[3], p[4]) for p in tri) for tri in triangles]
    checked = 0
    for surfaces, height in ((triangles, contract['ports']['Sin'][2]),
                              (swapped, contract['ports']['Ein'][2])):
        for distance in (.5, 4., 7.5):
            plane = 56.-distance
            for absolute, floor in ((height+.689326, True), (height-1.48933, False)):
                actual = _section_intervals(surfaces, plane, absolute, floor=floor)
                require(len(actual) == 1 and abs(actual[0][0]+7.5) < .00005
                        and abs(actual[0][1]-7.5) < .00005,
                        'Tight paired corner native slab width, continuity or thickness differs')
                checked += 1
            caps = _section_intervals(surfaces, plane, height+1.48933)
            expected = [(-7.5, -5.9965477), (5.9965477, 7.5)]
            require(len(caps) == 2 and all(abs(a-c) < .00005 and abs(b-d) < .00005
                    for (a, b), (c, d) in zip(caps, expected)),
                    'Tight paired corner native parapet widths differ')
            for triangle in surfaces:
                intersections = []
                for a, b in zip(triangle, triangle[1:]+triangle[:1]):
                    if abs(a[2]-plane) <= 2e-6:
                        intersections.append(a)
                    if (a[2] < plane < b[2]) or (b[2] < plane < a[2]):
                        t = (plane-a[2])/(b[2]-a[2])
                        intersections.append(tuple(a[k]+t*(b[k]-a[k]) for k in range(5)))
                require(not any(-5.9964 < p[0] < 5.9964 and
                                height+.889326 < p[1] < height+1.4894 for p in intersections),
                        'Tight paired corner retains an internal wall in a native collar')
    return {'native_tight_corner_profile_sections_checked': checked,
            'native_paired_slab_width_m': 15.,
            'native_tight_corner_physical_end_heights_m': [contract['ports']['Sin'][2],
                                                          contract['ports']['Ein'][2]],
            'paired_collar_internal_walls': False}
