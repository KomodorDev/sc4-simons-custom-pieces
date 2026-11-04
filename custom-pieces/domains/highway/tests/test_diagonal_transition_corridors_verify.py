"""Reject finite width holes and millimetre obstacles above real roof fields."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT/'framework'), str(ROOT/'domains/highway/implementation')]
from scp_highway.diagonal_transition_corridors_verify import check_corridors


def sheet(x0=-4., x1=4., y0=-2., y1=2., field=lambda x, y: 0., deck='upper', **extra):
    points = [(x, y, field(x, y)) for x, y in ((x0, y0), (x1, y0), (x1, y1), (x0, y1))]
    return [{'role': deck+'-pavement-fixture', 'kind': 'pavement', 'deck': deck,
             'points': tuple(points[i] for i in indices), **extra}
            for indices in ((0, 1, 2), (0, 2, 3))]


def wall(bottom, top, *, x=0., role='fixture-support', reference=False):
    points = ((x, -.5, bottom), (x, .5, bottom), (x, .5, top), (x, -.5, top))
    return [{'role': role, 'kind': 'support', 'deck': 'lower', 'native_reference': reference,
             'points': tuple(points[i] for i in indices)} for indices in ((0, 1, 2), (0, 2, 3))]


def route(first=(-2., 0., 0.), last=(2., 0., 0.), component='upper'):
    return {'component': component, 'points': (first, last)}


class FiniteDiagonalCorridorTests(unittest.TestCase):
    def run_check(self, faces, routes=None, **keywords):
        return check_corridors(faces, [route()] if routes is None else routes,
                               owned_cells=[(0, 0)], **keywords)

    def test_complete_flat_and_nonuniform_finite_sloped_roofs_support_full_width(self):
        for field in (lambda x, y: 0., lambda x, y: .04*x+.013*y+.001):
            with self.subTest(field=field):
                result = self.run_check(sheet(field=field))
                self.assertTrue(result['passed'])
                self.assertTrue(result['local_finite_roof_envelope_used'])
                self.assertFalse(result['centreline_datum_broadcast'])

    def test_missing_inside_owned_width_rejects_without_area_exemption(self):
        # The 9um gap leaves a positive finite hole after the two4um bounds.
        faces = sheet(y1=.4)+sheet(y0=.400009)
        with self.assertRaisesRegex(ValueError, 'full-width corridor lacks'):
            self.run_check(faces)

    def test_centreline_only_pavement_cannot_supply_a_full_vehicle_strip(self):
        with self.assertRaisesRegex(ValueError, 'full-width corridor lacks'):
            self.run_check(sheet(y0=-.1, y1=.1))

    def test_two_millimetres_above_local_roof_rejects_even_for_original_reference(self):
        for reference in (False, True):
            with self.subTest(native_reference=reference), self.assertRaisesRegex(ValueError, 'above the local roof'):
                self.run_check(sheet()+wall(.002, .003, reference=reference))

    def test_an_obstacle_in_an_admitted_seven_micrometre_roof_gap_cannot_disappear(self):
        faces = sheet(y1=-3.5e-6)+sheet(y0=3.5e-6)
        self.assertTrue(self.run_check(faces)['passed'])
        obstacle = {'role': 'finite-gap-support', 'kind': 'support', 'deck': 'lower',
                    'points': ((-1., 0., .002), (1., 0., .002), (1., 0., 2.))}
        with self.assertRaisesRegex(ValueError, 'finite-gap-support'):
            self.run_check(faces+[obstacle])

    def test_horizontal_and_vertical_gap_cannot_each_spend_the_four_micrometre_bound(self):
        faces = sheet(y1=-3.5e-6)+sheet(y0=3.5e-6)
        obstacle = {'role': 'combined-distance-gap-support', 'kind': 'support', 'deck': 'lower',
                    'points': ((-1., 0., 2e-6), (1., 0., 2e-6), (1., 0., 3e-6))}
        with self.assertRaisesRegex(ValueError, 'combined-distance-gap-support'):
            self.run_check(faces+[obstacle])

    def test_unassigned_parts_below_every_finite_roof_do_not_enter_vehicle_space(self):
        faces = sheet(y1=-3.5e-6)+sheet(y0=3.5e-6)
        self.assertTrue(self.run_check(faces+wall(-1., 0.))['passed'])
        with self.assertRaisesRegex(ValueError, 'fixture-support'):
            self.run_check(faces+wall(-1., 2e-6))

    def test_vertical_step_wall_at_finite_local_maximum_is_not_an_obstacle(self):
        faces = sheet(x1=0.)+sheet(x0=0., field=lambda x, y: .001)
        self.assertTrue(self.run_check(faces+wall(0., .001))['passed'])
        with self.assertRaisesRegex(ValueError, 'above the local roof'):
            self.run_check(faces+wall(0., .003))

    def test_higher_remote_pavement_cannot_occlude_an_obstacle_outside_its_finite_patch(self):
        faces = sheet()+sheet(x0=3., x1=4., field=lambda x, y: 1.)
        with self.assertRaisesRegex(ValueError, 'above the local roof'):
            self.run_check(faces+wall(.002, .003))

    def test_obstacle_above_the_full_height_is_clear_but_opposing_deck_below_ceiling_rejects(self):
        self.assertTrue(self.run_check(sheet()+sheet(field=lambda x, y: 4., deck='lower'))['passed'])
        with self.assertRaisesRegex(ValueError, 'above the local roof'):
            self.run_check(sheet()+sheet(field=lambda x, y: 3.7, deck='lower'))

    def test_complete_support_side_faces_are_checked_in_their_own_plane(self):
        with self.assertRaisesRegex(ValueError, 'fixture-support'):
            self.run_check(sheet()+wall(-1., 2.))

    def test_native_wedges_require_exact_explicit_unowned_cells_and_full_roof(self):
        native_route = route((7., 0., 0.), (10., 0., 0.))
        faces = sheet(x1=12.)
        with self.assertRaisesRegex(ValueError, 'unowned non-native'):
            self.run_check(faces, native_routes=[native_route])
        result = self.run_check(faces, native_routes=[native_route], native_cells={'upper': [(1, 0)]})
        self.assertEqual(result['native_approach_segments_checked'], 1)
        self.assertGreater(result['outside_owned_segment_wedges_checked'], 0)
        with self.assertRaisesRegex(ValueError, 'must not relabel an owned cell'):
            self.run_check(faces, native_cells={'upper': [(0, 0)]})
        with self.assertRaisesRegex(ValueError, 'unowned non-native'):
            self.run_check(faces, native_routes=[native_route], native_cells={'lower': [(1, 0)]})

    def test_a_native_cell_allowance_cannot_cover_an_inside_owned_width_hole(self):
        with self.assertRaisesRegex(ValueError, 'full-width corridor lacks'):
            self.run_check(sheet(y0=-.1, y1=.1), native_cells={'upper': [(1, 0)]})

    def test_zero_chords_and_wrong_component_roofs_reject(self):
        with self.assertRaisesRegex(ValueError, 'zero horizontal'):
            self.run_check(sheet(), [route((0., 0., 0.), (0., 0., 1.))])
        with self.assertRaisesRegex(ValueError, 'no certified finite pavement'):
            self.run_check(sheet(deck='lower'))


if __name__ == '__main__':
    unittest.main()
