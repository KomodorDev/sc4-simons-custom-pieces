"""Mutation tests for saved-surface proof, independent of the road writer."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT/'framework'), str(ROOT/'domains/highway/implementation')]

from PIL import Image
from scp.track_paths import PATH
from scp_highway import orthogonal_transition_models_verify as check
from scp_highway import orthogonal_transition_verify as paths


def surfaces(role='upper-pier-12'):
    expected = tuple(deepcopy(face) for face in check._surface_contract() if face['role'] == role)
    actual = [{**deepcopy(face), 'material': {}, 'texture': 0, 'upward': check._normal(face['points'])[2] > 0.}
              for face in expected]
    return expected, actual


def surface_audit(expected, actual):
    # Material identity has its own byte-level check. This isolated fixture
    # tests geometric completeness, winding, and UV interpolation without
    # redistributing third-party native game materials in the test suite.
    with patch.object(check, '_surface_contract', return_value=expected), patch.object(check, '_material'):
        return check.check_complete_surfaces(actual, 0x7F700000)


class SavedTransitionSurfaceTests(unittest.TestCase):
    def test_complete_support_has_all_six_closed_faces(self):
        expected, actual = surfaces()
        self.assertEqual(len(expected), 12)
        self.assertTrue(surface_audit(expected, actual)['passed'])
        self.assertEqual(len(check.support_contract()), 14)
        self.assertTrue(all(row[-1] > row[-2] for row in check.support_contract()))

    def test_a_hole_or_duplicate_in_a_closed_support_is_rejected(self):
        expected, actual = surfaces()
        for corrupted in (actual[:-1], [*actual, deepcopy(actual[-1])]):
            with self.subTest(count=len(corrupted)), self.assertRaisesRegex(ValueError, 'missing or duplicate|duplicate cannot'):
                surface_audit(expected, corrupted)

    def test_equal_area_duplicate_half_cannot_conceal_a_missing_half(self):
        parent = {'role': 'upper-body', 'points': ((0., 0., 0.), (2., 0., 0.), (0., 2., 0.)),
                  'uv': ((0., 0.), (2., 0.), (0., 2.)), 'area': 2.}
        first = {'role': 'upper-body', 'points': ((0., 0., 0.), (2., 0., 0.), (1., 1., 0.)),
                 'uv': ((0., 0.), (2., 0.), (1., 1.)), 'material': {}, 'texture': 0}
        second = {'role': 'upper-body', 'points': ((0., 0., 0.), (1., 1., 0.), (0., 2., 0.)),
                  'uv': ((0., 0.), (1., 1.), (0., 2.)), 'material': {}, 'texture': 0}
        self.assertTrue(surface_audit((parent,), [first, second])['passed'])
        with self.assertRaisesRegex(ValueError, 'duplicate cannot conceal a hole'):
            surface_audit((parent,), [first, deepcopy(first)])

    def test_a_moved_pier_cannot_be_hidden_by_its_name_or_bounds(self):
        expected, actual = surfaces()
        actual[0]['points'] = tuple((x+.01, y, z) for x, y, z in actual[0]['points'])
        with self.assertRaisesRegex(ValueError, 'independent surface'):
            surface_audit(expected, actual)

    def test_backfacing_support_and_wrong_affine_uv_are_rejected(self):
        for mutation in ('winding', 'uv'):
            expected, actual = surfaces()
            if mutation == 'winding':
                actual[0]['points'] = tuple(reversed(actual[0]['points']))
                actual[0]['uv'] = tuple(reversed(actual[0]['uv']))
            else:
                actual[0]['uv'] = tuple((u+.001, v) for u, v in actual[0]['uv'])
            with self.subTest(mutation=mutation), self.assertRaisesRegex(ValueError, 'independent surface'):
                surface_audit(expected, actual)

    def test_missing_underside_is_rejected_even_when_pavement_exists(self):
        source = check._surface_contract()
        body = next(face for face in source if face['role'] == 'upper-body' and check._normal(face['points'])[2] < 0.)
        pavement = next(face for face in source if face['role'] == 'upper-pavement-native-dd')
        expected = (deepcopy(body), deepcopy(pavement))
        actual = [{**deepcopy(pavement), 'texture': 0, 'material': {}}]
        with self.assertRaisesRegex(ValueError, 'missing or duplicate'):
            surface_audit(expected, actual)

    def test_near_flat_native_barrier_uses_one_shared_xyz_uv_witness(self):
        parent = {'points': ((0., 0., 0.), (.05, 0., .0000005), (.05, .25, 0.)),
                  'uv': ((0., 0.), (0., 1.), (1., 1.))}
        point = (.05, 0., 0.)  # Sub-micrometre Float32/rounding envelope.
        self.assertIsNotNone(check._field_weights(point, (0., 1.), parent))
        self.assertIsNone(check._field_weights(point, (.001, 1.), parent))

    def test_city_clipping_cannot_extrapolate_beyond_the_original_station_strip(self):
        parent = {'role': 'upper-body', 'points': ((-8., -84.5, 0.), (8., -84.5, 0.), (8., -84.75, 0.)),
                  'uv': ((-1., 11.5625), (1., 11.5625), (1., 11.59375))}
        parent['area'] = check._area(parent['points'])
        actual = {**deepcopy(parent), 'material': {}, 'texture': 0}
        actual['points'] = (*actual['points'][:2], (8., -84.78614902496338, 0.))
        actual['uv'] = (*actual['uv'][:2], (1., (84.78614902496338+8.)/8.))
        with self.assertRaisesRegex(ValueError, 'independent surface'):
            surface_audit((parent,), [actual])

    def test_revised_first_upper_pier_is_outside_lower_shoulder(self):
        first = next(row for row in check.support_contract() if row[0] == 'upper-pier-12')
        self.assertEqual(first[3:5], (-9.6, -8.799999999999999))
        center, normal = check._frame('upper', 12.)
        eastmost = max(center[0]+u*normal[0]+t*normal[1]
                       for u in first[3:5] for t in (-.4, .4))
        self.assertLess(eastmost, 8.)

    def test_atlas_preserves_opaque_elevated_shoulders_and_adopts_ground_alpha_at_landing(self):
        native = {0x5713000E: Image.new('RGBA', (128, 128), (10, 20, 30, 255)),
                  0x5703000E: Image.new('RGBA', (128, 128), (110, 120, 130, 0))}
        pixels = check.reconstruct_atlas(native)
        def pixel(column, station):
            row = round(station*8.+128.-.5)
            offset = (row*512+column)*4
            return tuple(pixels[offset:offset+4])
        self.assertEqual(pixel(8, 20.)[3], 255)
        self.assertEqual(pixel(8, 70.)[3], 255)
        self.assertGreater(pixel(8, 20.)[0], 10)
        self.assertEqual(pixel(8, 94.), (110, 120, 130, 0))
        self.assertEqual(pixel(264, 70.), (110, 120, 130, 0))
        self.assertEqual(pixel(6, 20.), pixel(134, 20.))
        self.assertEqual(pixel(7, 20.), pixel(135, 20.))
        self.assertEqual(pixel(5, 20.), (0, 0, 0, 0))
        self.assertEqual(pixel(138, 20.), (0, 0, 0, 0))


def corridor_fixture():
    piece = {'tile_ids': [f'{0x7f700000+i*0x10:08x}' for i in range(12)]}
    empty = b'SC4PATHS\n1.2\n0\n0\n1\n'
    resources = {(*PATH, int(tile, 16)): empty for tile in piece['tile_ids']}
    resources[*PATH, int(piece['tile_ids'][-1], 16)] = (
        b'SC4PATHS\n1.2\n1\n0\n1\n1\n1\n3\n1\n0\n2\n-2.5,-8,0\n-2.5,0,0\n')
    points = ((12., -88., 0.), (15., -88., 0.), (15., -80., 0.), (12., -80., 0.))
    faces = [{'role': 'lower-pavement-native-ground', 'upward': True,
              'points': tuple(points[i] for i in indices)} for indices in ((0, 1, 2), (0, 2, 3))]
    return piece, resources, faces


class SavedTransitionCorridorTests(unittest.TestCase):
    def test_continuous_flat_lane_is_supported(self):
        piece, resources, faces = corridor_fixture()
        self.assertTrue(check.check_corridors(faces, resources, piece)['passed'])

    def test_wall_between_path_nodes_is_rejected(self):
        piece, resources, faces = corridor_fixture()
        faces.append({'role': 'upper-pier-12', 'upward': False,
                      'points': ((12., -84., .1), (15., -84., .1), (13.5, -84., 3.))})
        with self.assertRaisesRegex(ValueError, 'vehicle corridor intersects'):
            check.check_corridors(faces, resources, piece)

    def test_continuous_support_hole_between_nodes_is_rejected(self):
        piece, resources, faces = corridor_fixture()
        with self.assertRaisesRegex(ValueError, 'continuously support'):
            check.check_corridors(faces[:1], resources, piece)

    def test_opposite_deck_face_cannot_pierce_a_closed_support_outside_the_car_lanes(self):
        name, deck, s, low, high, half, bottom, top = check.support_contract()[0]
        center, normal = check._frame(deck, s)
        tangent = normal[1], -normal[0]
        height = (bottom+top)/2.
        triangle = tuple((center[0]+u*normal[0]+t*tangent[0], center[1]+u*normal[1]+t*tangent[1], height)
                         for u, t in ((low+.1, -.1), (high-.1, -.1), ((low+high)/2., .1)))
        with self.assertRaisesRegex(ValueError, 'closed support .* intersects opposite'):
            check.check_support_clearance([{'role': 'lower-barrier', 'points': triangle}])

    def test_decks_and_barriers_must_keep_their_vertical_order_where_their_plans_overlap(self):
        triangle = ((0., 0., 0.), (2., 0., 0.), (1., 2., 0.))
        def face(role, height):
            return {'role': role, 'points': tuple((x, y, height) for x, y, _ in triangle)}
        self.assertTrue(check.check_deck_clearance([face('upper-body', 5.), face('lower-barrier', 4.)])['passed'])
        for upper in (3., 4.):
            with self.subTest(upper=upper), self.assertRaisesRegex(ValueError, 'intersects or drops below'):
                check.check_deck_clearance([face('upper-body', upper), face('lower-barrier', 4.)])

    def test_native_ground_shoulder_contact_exception_cannot_hide_a_lane_or_elevated_overlap(self):
        def pair(east, width, altitude=0.):
            triangle = ((east, 0., altitude), (east+width, 0., altitude), (east, 1., altitude))
            return [{'role': 'upper-body', 'points': triangle},
                    {'role': 'lower-pavement-native-ground', 'points': tuple((x, y, 0.) for x, y, _ in triangle)}]
        self.assertTrue(check.check_deck_clearance(pair(8., .00001))['passed'])
        for args in ((8., .01), (13., .00001), (8., .00001, -.001)):
            with self.subTest(args=args), self.assertRaisesRegex(ValueError, 'intersects or drops below'):
                check.check_deck_clearance(pair(*args))


class MirroredTransitionSurfaceTests(unittest.TestCase):
    def test_inverse_reflection_corrects_winding_and_preserves_vertex_uvs(self):
        source = next(deepcopy(f) for f in check._surface_contract(True)
                      if f['role'] == 'upper-pavement-native-dd')
        actual = {**source, 'points': tuple((16.-source['points'][i][0], *source['points'][i][1:])
                                          for i in (0, 2, 1)),
                  'uv': tuple(source['uv'][i] for i in (0, 2, 1)), 'material': {}, 'texture': 0}
        canonical = check.canonical_surface_frame([actual], mirrored=True)
        self.assertEqual(canonical[0]['points'], source['points'])
        self.assertEqual(canonical[0]['uv'], source['uv'])
        with patch.object(check, '_surface_contract', return_value=(source,)), patch.object(check, '_material'):
            self.assertTrue(check.check_complete_surfaces(canonical, 0x7f700000, mirrored=True)['passed'])

    def test_reflection_without_corrected_saved_index_winding_is_rejected(self):
        source = next(deepcopy(f) for f in check._surface_contract(True)
                      if f['role'] == 'upper-pavement-native-dd')
        actual = {**source, 'points': tuple((16.-x, y, h) for x, y, h in source['points']),
                  'material': {}, 'texture': 0}
        canonical = check.canonical_surface_frame([actual], mirrored=True)
        with patch.object(check, '_surface_contract', return_value=(source,)), patch.object(check, '_material'):
            with self.assertRaisesRegex(ValueError, 'independent surface, winding, or UV'):
                check.check_complete_surfaces(canonical, 0x7f700000, mirrored=True)

    def test_mirrored_native_dd_phase_uses_measured_offset_and_not_one_minus_original(self):
        old = check._uv('upper', 0., 2.5, 'native-dd')
        mirrored = check._uv('upper', 0., 2.5, 'native-dd', mirrored=True)
        self.assertAlmostEqual(mirrored[1], (16.-check.DD_OFFSET)/check.DD_WIDTH, places=14)
        self.assertGreater(abs(mirrored[1]-(1.-old[1])), .0001)
        self.assertEqual(mirrored[0], old[0])
        self.assertEqual(check._uv('lower', 80., -2.5, 'native-ground', mirrored=True)[1], 5.)

    def test_retaining_original_native_surface_uvs_on_mirrored_geometry_is_rejected(self):
        for role in ('upper-pavement-native-dd', 'upper-pavement-native-ground', 'upper-barrier'):
            expected = next(deepcopy(f) for f in check._surface_contract(True) if f['role'] == role)
            original = next(f for f in check._surface_contract(False)
                            if f['role'] == role and f['points'] == expected['points'])
            corrupted = {**deepcopy(expected), 'uv': original['uv'], 'material': {}, 'texture': 0}
            with self.subTest(role=role), patch.object(check, '_surface_contract', return_value=(expected,)), patch.object(check, '_material'):
                with self.assertRaisesRegex(ValueError, 'independent surface, winding, or UV'):
                    check.check_complete_surfaces([corrupted], 0x7f700000, mirrored=True)

    def test_authored_concrete_uvs_and_original_geometry_contract_are_preserved(self):
        first, second = check._surface_contract(False), check._surface_contract(True)
        self.assertEqual([f['points'] for f in first], [f['points'] for f in second])
        self.assertEqual([(f['role'], f['uv']) for f in first if '-pavement-' not in f['role'] and not f['role'].endswith('-barrier')],
                         [(f['role'], f['uv']) for f in second if '-pavement-' not in f['role'] and not f['role'].endswith('-barrier')])
        self.assertNotEqual(check.ATLAS_RGBA_SHA256, check.MIRRORED_ATLAS_RGBA_SHA256)

    def test_reflected_native_ground_edge_contact_keeps_the_same_bounded_exception(self):
        original = [{'role': role, 'points': ((8., 0., 0.), (8.00001, 0., 0.), (8., 1., 0.)),
                     'uv': ((0., 0.), (1., 0.), (0., 1.))}
                    for role in ('upper-body', 'lower-pavement-native-ground')]
        reflected = check.canonical_surface_frame(original, mirrored=True)
        self.assertTrue(check.check_deck_clearance(check.canonical_surface_frame(reflected, mirrored=True))['passed'])


if __name__ == '__main__':
    unittest.main()
