"""Reject the fan's interrupted central caps and open inside faces."""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import unittest
from unittest.mock import patch

from scp_hsr.hsr_fan_parapet import corrected_fan_sweeps
from scp_hsr.hsr_atomic_components_verify import _section_intervals
from scp_hsr.directional_t_verify import _area, _intersection_polygon
from scp_hsr.hsr_fan_parapet_verify import audit_central_parapet, SECTIONS

ROOT = next(path for path in Path(__file__).resolve().parents if (path/'project.json').is_file())
NATIVE_DONOR = ROOT/'local/validation-inputs/Plugins/High Speed Rail.dat'


RULE = {'reflection_axis_source_east_m': 96.,
        'inside_sides': {'native_y_left': 1, 'native_y_right': -1}}
BED, TOP = 16.1893253, 16.9893265


def quad(points):
    vertices = [(*point, .18, 0.) for point in points]
    return [(vertices[0], vertices[1], vertices[2]),
            (vertices[0], vertices[2], vertices[3])]


def fixture():
    decks, results = [], {}
    for name, centre, inner, outer in (('native_y_left', 92., 94.6, 97.5),
                                        ('native_y_right', 100., 97.4, 94.5)):
        deck = {'name': name, 'width': 8., 'clearance_half_width': 2.6,
                'flat_paired_collar_height': 15.5}
        cap = quad(((inner, TOP, 40.), (outer, TOP, 40.),
                    (outer, TOP, 56.), (inner, TOP, 56.)))
        wall = quad(((inner, BED, 40.), (inner, TOP, 40.),
                     (inner, TOP, 56.), (inner, BED, 56.)))
        opposite = centre-(inner-centre)
        wall += quad(((opposite, BED, 40.), (opposite, TOP, 40.),
                      (opposite, TOP, 56.), (opposite, BED, 56.)))
        rail = quad(((centre-.5, BED, 40.), (centre+.5, BED, 40.),
                     (centre+.5, BED, 56.), (centre-.5, BED, 56.)))
        corridor = {'polygon': [(centre-4., 40.), (centre+4., 40.),
                                  (centre+4., 56.), (centre-4., 56.)],
                    'clearance_polygons': [[(centre-2.6, 40.), (centre+2.6, 40.),
                                            (centre+2.6, 56.), (centre-2.6, 56.)]],
                    'low': BED, 'high': TOP, 'bed_low': BED, 'bed_high': BED}
        results[name] = ([('wall', t) for t in cap]+[('inner_wall', t) for t in wall]
                         +[('rail', t) for t in rail], [corridor],
                         [(centre, 15.5, 40.), (centre, 15.5, 56.)], [16.])
        decks.append(deck)
    return decks, results


class FanParapetSweepTests(unittest.TestCase):
    def corrected(self):
        decks, old = fixture()
        with patch('scp_hsr.hsr_components._sweep_component_profile',
                   side_effect=lambda source, deck: deepcopy(old[deck['name']])):
            result = corrected_fan_sweeps({'top': TOP}, decks, RULE)
        return old, result

    def test_inside_caps_meet_without_the_old_triangle(self):
        _, changed = self.corrected()
        faces = [tri for surfaces, _, _, _ in changed.values()
                 for kind, tri in surfaces if kind == 'preclipped_parapet']
        intervals = _section_intervals(faces, 'north', -48., TOP, 96.)
        self.assertEqual(len(intervals), 1)
        self.assertAlmostEqual(intervals[0][0], -1.4, places=7)
        self.assertAlmostEqual(intervals[0][1], 1.4, places=7)

    def test_reflection_plane_ownership_prevents_overlapping_caps(self):
        _, changed = self.corrected()
        caps = [[tri for kind, tri in item[0] if kind == 'preclipped_parapet']
                for item in changed.values()]
        overlap = sum(_area(_intersection_polygon([(v[0], v[2]) for v in a],
                                                   [(v[0], v[2]) for v in b]))
                      for a in caps[0] for b in caps[1])
        self.assertAlmostEqual(overlap, 0., places=10)
        self.assertTrue(all(v[0] <= 96.+1e-9 for tri in caps[0] for v in tri))
        self.assertTrue(all(v[0] >= 96.-1e-9 for tri in caps[1] for v in tri))

    def test_rails_and_existing_tapered_clearance_polygons_are_exactly_preserved(self):
        before, changed = self.corrected()
        for name in before:
            self.assertEqual(before[name][1:], changed[name][1:])
            self.assertEqual([tri for kind, tri in before[name][0] if kind == 'rail'],
                             [tri for kind, tri in changed[name][0] if kind == 'rail'])

    def test_both_matching_inside_walls_are_retained(self):
        _, changed = self.corrected()
        for name, east in (('native_y_left', 94.6), ('native_y_right', 97.4)):
            walls = [tri for kind, tri in changed[name][0] if kind == 'aligned_inner_wall']
            self.assertEqual(len(walls), 2)
            self.assertTrue(all(abs(v[0]-east) < 1e-10 for tri in walls for v in tri))
            self.assertEqual({v[1] for tri in walls for v in tri}, {BED, TOP})

    def test_unexpected_recipe_axes_are_rejected(self):
        decks, _ = fixture()
        rule = deepcopy(RULE)
        rule['reflection_axis_source_east_m'] = 95.
        with self.assertRaisesRegex(ValueError, 'exact reflected arms'):
            corrected_fan_sweeps({'top': TOP}, decks, rule)


def saved_face_fixture():
    # Independent literal saved-space sections, including the fork nose and
    # the retained two separate walls farther south. No generator is called.
    left = [(49., 48., 48.)]
    right = [(49., 48., 48.)]
    for south, intervals in SECTIONS:
        if south <= 49.:
            continue
        left.append((south, intervals[0][0], min(intervals[0][1], 48.)))
        right.append((south, intervals[-1][1], max(intervals[-1][0], 48.)))
    tops, walls = [], []
    for sections in (left, right):
        for (za, ia, oa), (zb, ib, ob) in zip(sections, sections[1:]):
            tops.extend(quad(((ia, TOP, za), (oa, TOP, za),
                              (ob, TOP, zb), (ib, TOP, zb))))
            walls.extend(quad(((ia, BED, za), (ia, TOP, za),
                               (ib, TOP, zb), (ib, BED, zb))))
    return tops, walls


class FanParapetSavedFaceTests(unittest.TestCase):
    def test_continuous_closed_fork_nose_passes(self):
        tops, walls = saved_face_fixture()
        report = audit_central_parapet(tops+walls)
        self.assertEqual(report['central_parapet_top_sections_checked'], 6)
        self.assertEqual(report['central_parapet_inside_wall_sections_checked'], 6)
        self.assertLess(report['central_parapet_top_overlap_area_m2'], 1e-9)

    def test_the_old_missing_triangle_is_rejected(self):
        tops, walls = saved_face_fixture()
        old = [tri for tri in tops if min(v[2] for v in tri) >= 52.]
        with self.assertRaisesRegex(ValueError, 'interrupted ballast outline'):
            audit_central_parapet(old+walls)

    def test_a_flat_patch_at_ballast_height_cannot_replace_the_raised_top(self):
        tops, walls = saved_face_fixture()
        low = [tuple((v[0], BED, *v[2:]) for v in tri) for tri in tops]
        with self.assertRaisesRegex(ValueError, 'interrupted ballast outline'):
            audit_central_parapet(low+walls)

    def test_the_new_nose_requires_both_vertical_inside_faces(self):
        tops, walls = saved_face_fixture()
        with self.assertRaisesRegex(ValueError, 'no closed inside face'):
            audit_central_parapet(tops+[tri for tri in walls if min(v[0] for v in tri) > 48.])

    def test_duplicate_coplanar_caps_are_rejected(self):
        tops, walls = saved_face_fixture()
        with self.assertRaisesRegex(ValueError, 'overlapping concrete top'):
            audit_central_parapet(tops+walls+tops[:2])

    def test_concrete_intruding_into_the_adjacent_track_is_rejected(self):
        tops, walls = saved_face_fixture()
        blocked = quad(((47., TOP, 49.9), (47.8, TOP, 49.9),
                        (47.8, TOP, 50.1), (47., TOP, 50.1)))
        with self.assertRaisesRegex(ValueError, 'interrupted ballast outline'):
            audit_central_parapet(tops+walls+blocked)


class FanParapetNativeSweepTests(unittest.TestCase):
    @unittest.skipUnless(NATIVE_DONOR.is_file(), 'Optional audited native HSR donor is unavailable')
    def test_actual_tapered_walls_and_caps_match_through_the_full_surface_dispatch(self):
        from scp.dbpf import entries, decompress
        from scp_hsr.single_track_models import _native
        from scp_hsr.hsr_compact_fan import model_inputs
        from scp_hsr.hsr_components import _sweep_component_profile
        from scp_hsr.hsr_mesh import _surface_triangles
        source = _native(decompress(entries(NATIVE_DONOR.read_bytes())[
            0x5ad0e817, 0xbadb57f1, 0x5dd31500]))
        config = model_inputs('hsr_component_l2_paired_fan_compact_join')[1]
        original = {}

        def capture(source, deck):
            result = _sweep_component_profile(source, deck)
            original[deck['name']] = result
            return result

        with patch('scp_hsr.hsr_components._sweep_component_profile', side_effect=capture):
            corrected = corrected_fan_sweeps(source, config['surface_decks'],
                                            config['central_parapet_alignment'])

        def actual_faces(sweeps):
            # The floor/underside union is unchanged and expensive. Exercise
            # every real wall clipping/dispatch branch, omitting only floors.
            with patch('scp_hsr.hsr_mesh._height_aware_union', return_value=[]):
                faces, _ = _surface_triangles(source, config['surface_decks'],
                                               lambda source, deck: sweeps[deck['name']])
            return [tuple((v[0]-48., *v[1:]) for v in tri) for tri in faces]

        report = audit_central_parapet(actual_faces(corrected))
        self.assertEqual(report['central_parapet_inside_wall_sections_checked'], 6)
        with self.assertRaisesRegex(ValueError, 'interrupted ballast outline'):
            audit_central_parapet(actual_faces(original))
        recut = {name: ([(('aligned_parapet' if kind == 'preclipped_parapet' else kind), tri)
                        for kind, tri in surfaces], corridors, points, lengths)
                 for name, (surfaces, corridors, points, lengths) in corrected.items()}
        # Reapplying the separately warped mask restores the measured0.4mm
        # seam. The unchanged0.05mm tolerance must reject this real failure.
        with self.assertRaisesRegex(ValueError, 'interrupted ballast outline'):
            audit_central_parapet(actual_faces(recut))


if __name__ == '__main__':
    unittest.main()
