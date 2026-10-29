"""Negative controls for independent stacked/sloped HSR mesh audits."""
from __future__ import annotations

from pathlib import Path
from collections import defaultdict
from copy import deepcopy
import json
import sys
import math
import unittest

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp_hsr.hsr_mesh_verify import (
    audit_bed_union, audit_crossings, audit_supports, _shared_prefix, measure_journey_quality,
    _TURN_LIMITS,
    _coalesce_grid_cuts, _component_union_area,

)
from scp_hsr.interchange_verify import _bed, PATH, S3D
from scp.track_paths import encode_paths
from scp.verify import parse_paths, parse_rules
from scp.dbpf import entries, decompress


def floor(x0, x1, z0, z1, *, height=15.5, gradient=.0, absolute_y=None):
    def point(x, z):
        return (x, (_bed(height) if absolute_y is None else absolute_y)+gradient*z, z, .61, 0.)
    a, b, c, d = point(x0, z0), point(x1, z0), point(x1, z1), point(x0, z1)
    return [(a, b, c), (a, c, d)]


def sloped_pier(gradient=.1, top=14., x=0., z=5.):
    bottom = [(x+dx, 0., z+dz, .1, 0.) for dx, dz in ((-.65, -.65), (.65, -.65), (.65, .65), (-.65, .65))]
    head = [(p[0], top+gradient*(p[2]-z), p[2], .1, 1.) for p in bottom]
    result = [(bottom[0], bottom[2], bottom[1]), (bottom[0], bottom[3], bottom[2]),
              (head[0], head[1], head[2]), (head[0], head[2], head[3])]
    for index in range(4):
        a, b, c, d = bottom[index], bottom[(index+1)%4], head[(index+1)%4], head[index]
        result.extend([(a, b, c), (a, c, d)])
    return result


def encode_inspected(routes):
    lines = ['SC4PATHS', '1.2', str(len(routes)), '0', '0']
    for route in routes:
        lines.extend(str(route[key]) for key in ('transport', 'lane', 'entry', 'exit', 'compatibility'))
        lines.append(str(len(route['points'])))
        lines.extend(','.join(format(v, '.12g') for v in point) for point in route['points'])
    return ('\r\n'.join(lines)+'\r\n').encode('ascii')


class HSRMeshJourneyQualityTests(unittest.TestCase):
    def test_deliberate_loop_has_bounded_total_turn_and_correct_signed_winding(self):
        points = [(100.*math.sin(t), 100.*(1.-math.cos(t)), 15.5)
                  for t in (1.5*math.pi*n/1024 for n in range(1025))]
        limits = {**_TURN_LIMITS, 'max_length_ratio': 4., 'min_total_turn_degrees': 265.,
                  'max_total_turn_degrees': 275., 'max_endpoint_curvature_per_m': .02,
                  'signed_turn_degrees': 270., 'max_signed_turn_error_degrees': 2.,
                  'min_length_m': 460., 'max_length_m': 480.}
        report = measure_journey_quality(points, limits)
        self.assertGreater(report['total_turn_degrees'], 268.)
        with self.assertRaisesRegex(ValueError, 'wrong signed winding'):
            measure_journey_quality([(x, -y, h) for x, y, h in points], limits)
        with self.assertRaisesRegex(ValueError, 'missing.*cumulative turn'):
            measure_journey_quality([(0., 0., 15.5), (100., 0., 15.5)], limits)

    def test_a_collinear_tile_cut_does_not_invent_a_tighter_curve(self):
        points = [(40.*math.sin(t), 40.*(1.-math.cos(t)), 15.5)
                  for t in (math.pi/2.*n/128 for n in range(129))]
        cut = []
        for a, b in zip(points, points[1:]):
            cut.extend([a, tuple(a[k]+.12*(b[k]-a[k]) for k in range(3))])
        cut.append(points[-1])
        limits = {**_TURN_LIMITS, 'min_radius_m': 39., 'max_endpoint_curvature_per_m': .03}
        report = measure_journey_quality(cut, limits)
        self.assertGreater(report['minimum_resolved_raw_radius_m'], 39.)
        self.assertEqual(len(_coalesce_grid_cuts(cut)), len(points))

    def test_short_vertical_zigzag_cannot_hide_between_two_metre_samples(self):
        points = [(0., 0., 15.5), (49.8, 0., 15.5), (49.9, 0., 15.51),
                  (50., 0., 15.5), (50.1, 0., 15.51), (50.2, 0., 15.5), (100., 0., 15.5)]
        with self.assertRaisesRegex(ValueError, 'raw encoded vertical grade changes abruptly'):
            measure_journey_quality(points, _TURN_LIMITS)


class HSRMeshHeightAwareBedTests(unittest.TestCase):
    def test_both_stacked_levels_have_their_own_full_width_floor(self):
        records = [((0, 0), {}, [(0., 0., 15.5), (0., -10., 15.5)]),
                   ((0, 0), {}, [(0., 0., 30.5), (0., -10., 30.5)])]
        surfaces = floor(-2.5, 2.5, 0., 10.)+floor(-2.5, 2.5, 0., 10., height=30.5)
        report = audit_bed_union(surfaces, records)
        self.assertEqual(report['full_width_bed_union_segments_checked'], 2)
        self.assertTrue(report['height_aware_bed_union_checked'])
        with self.assertRaisesRegex(ValueError, 'hole.*at its height'):
            audit_bed_union(surfaces[:2], records)

    def test_full_width_sloping_floor_and_upper_hole_negative_control(self):
        records = [((0, 0), {}, [(0., 0., 15.5), (0., -10., 16.5)])]
        self.assertEqual(audit_bed_union(floor(-2.5, 2.5, 0., 10., gradient=.1), records)[
            'full_width_bed_union_segments_checked'], 1)
        # A narrow off-centre gap cannot be covered by the lower flat deck.
        surfaces = floor(-2.5, .9, 0., 10., gradient=.1)+floor(1., 2.5, 0., 10., gradient=.1)
        surfaces += floor(.9, 1., 0., 4.2, gradient=.1)+floor(.9, 1., 4.4, 10., gradient=.1)
        with self.assertRaisesRegex(ValueError, 'hole.*rail bed'):
            audit_bed_union(surfaces, records)

    def test_disjoint_union_optimization_keeps_duplicate_and_triple_overlap_area_exact(self):
        first = [(0., 0.), (2., 0.), (2., 2.), (0., 2.)]
        second = [(1., 1.), (3., 1.), (3., 3.), (1., 3.)]
        other = [(10., 0.), (12., 0.), (12., 2.), (10., 2.)]
        self.assertEqual(_component_union_area([first, second, first, other]), 11.)

    def test_genuine_coplanar_overlap_fails_but_different_level_is_preserved(self):
        records = [((0, 0), {}, [(0., 0., 15.5), (0., -10., 16.5)])]
        surfaces = floor(-2.5, 2.5, 0., 10., gradient=.1)
        with self.assertRaisesRegex(ValueError, 'substantive coplanar.*overlap'):
            audit_bed_union(surfaces*2, records)
        self.assertEqual(audit_bed_union(surfaces+floor(-2.5, 2.5, 0., 10., height=30.5), records)[
            'maximum_uncovered_bed_area_m2'], 0.)


class HSRMeshGlobalSupportTests(unittest.TestCase):
    contract = {'support_centres_xz': [(0., 5.)], 'foundation_width_m': 1.3,
                'minimum_support_spacing_m': 16.}

    def test_sloping_head_touches_underside_at_all_nine_required_contacts(self):
        pier = sloped_pier()
        underside = floor(-4., 4., 0., 10., absolute_y=13.5, gradient=.1)
        report = audit_supports(pier+underside, self.contract)
        self.assertEqual(report['support_columns_checked'], 1)
        self.assertEqual(report['support_contact_points_checked'], 9)
        self.assertEqual(report['sloped_support_heads_checked'], 1)

    def test_missing_head_face_fails_even_if_contact_vertices_still_exist(self):
        pier = sloped_pier()
        underside = floor(-4., 4., 0., 10., absolute_y=13.5, gradient=.1)
        del pier[2]
        with self.assertRaisesRegex(ValueError, 'incomplete.*cap surface'):
            audit_supports(pier+underside, self.contract)

    def test_flat_head_under_sloping_deck_does_not_pass_with_one_centre_contact(self):
        underside = floor(-4., 4., 0., 10., absolute_y=13.5, gradient=.1)
        with self.assertRaisesRegex(ValueError, 'floats below|cuts through'):
            audit_supports(sloped_pier(gradient=0.)+underside, self.contract)
        with self.assertRaisesRegex(ValueError, 'floats below|cuts through'):
            audit_supports(sloped_pier(top=13.8)+underside, self.contract)

    def test_duplicate_or_close_piers_fail_across_the_placed_union(self):
        pier = sloped_pier()
        underside = floor(-4., 4., 0., 10., absolute_y=13.5, gradient=.1)
        with self.assertRaisesRegex(ValueError, 'duplicate support foundations'):
            audit_supports(pier+pier+underside, self.contract)
        with self.assertRaisesRegex(ValueError, 'too close'):
            audit_supports(pier+sloped_pier(x=2.)+underside,
                           {**self.contract, 'support_centres_xz': [(0., 5.), (2., 5.)]})


class HSRMeshConflictTests(unittest.TestCase):
    def test_same_incoming_label_does_not_waive_a_later_independent_crossing(self):
        journeys = {('Nin', 'Sout'): [(0., 10., 15.5), (0., 0., 15.5), (0., -10., 15.5), (12., -22., 15.5)],
                    ('Nin', 'Eout'): [(0., 10., 15.5), (0., 0., 15.5), (0., -6., 15.5),
                                      (.1, -7., 15.5), (1., -8., 15.5), (10., -15., 15.5),
                                      (10., -25., 15.5), (-5., -25., 15.5), (-5., -15., 15.5), (15., -15., 15.5)]}
        # The connected, nearly tangent fork at(0,-6) must be allowed;
        # only the later independent crossing at(10,-20) rejects this case.
        with self.assertRaisesRegex(ValueError, r'XY \(10\.0, -20\.0\)'):
            audit_crossings(journeys, {'required_grade_separated_crossings': 0})

    def test_real_upper_crossing_clears_both_actual_native_profiles(self):
        journeys = {('Win', 'Eout'): [(-10., 0., 30.5), (10., 0., 30.5)],
                    ('Sin', 'Nout'): [(0., -10., 15.5), (0., 10., 15.5)]}
        report = audit_crossings(journeys, {'required_grade_separated_crossings': 1})
        self.assertEqual(report['grade_separated_crossings_checked'], 1)
        self.assertAlmostEqual(report['grade_separated_crossings'][0]['structural_clearance_m'], 12.02134)
        journeys['Win', 'Eout'] = [(-10., 0., 23.), (10., 0., 23.)]
        with self.assertRaisesRegex(ValueError, 'insufficient deck clearance'):
            audit_crossings(journeys, {'required_grade_separated_crossings': 1})

    def test_opposite_coincident_tracks_inside_one_cell_cannot_escape_crossing_check(self):
        journeys = {('Win', 'Eout'): [(-6., 0., 15.5), (6., 0., 15.5)],
                    ('Ein', 'Wout'): [(6., 0., 15.5), (-6., 0., 15.5)]}
        with self.assertRaisesRegex(ValueError, 'independent same-level crossing'):
            audit_crossings(journeys, {'required_grade_separated_crossings': 0})

    def test_shared_geometric_prefix_survives_different_sampling(self):
        first = [(0., 0., 15.5), (0., 10., 15.5), (10., 20., 15.5)]
        second = [(0., 0., 15.5), (0., 2., 15.5), (0., 10., 15.5), (-10., 20., 15.5)]
        self.assertEqual(_shared_prefix(first, second), [((0., 0., 15.5), (0., 2., 15.5)),
                                                       ((0., 2., 15.5), (0., 10., 15.5))])


if __name__ == '__main__':
    unittest.main()
