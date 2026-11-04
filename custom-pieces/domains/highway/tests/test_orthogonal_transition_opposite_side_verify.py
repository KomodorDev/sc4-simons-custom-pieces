"""Independent phase, native-lane, and source-profile controls for the two new types."""
from copy import deepcopy
import hashlib
import math
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT/'framework'), str(ROOT/'domains/highway/implementation')]

from PIL import Image
from scp.models import parse_s3d, pack_s3d
from scp.track_paths import PATH
from scp.verify import parse_paths
from scp_highway import orthogonal_transition_verify as paths
from scp_highway import orthogonal_transition_models_verify as models
from test_orthogonal_transition_verify import encode, fixture

NEW = ('opposite-side', 'opposite-side-mirrored')


def new_fixture(variant):
    phase = paths.PHASES[variant]
    piece, _ = fixture()
    piece.update(id=phase.piece_id, recipe=phase.recipe, transition_variant=variant)
    piece['engineering']['model_only_cells'] = [[1 if phase.physical_reflection else 0, 0]]
    piece['engineering']['max_grade_percent'] = 20.
    expected = paths.expected_cell_routes(variant=variant)
    resources = {(*PATH, int(tile, 16)): encode(expected[cell])
                 for cell, tile in zip(paths.CELLS, piece['tile_ids'])}
    return piece, resources


class OppositeSideIndependentPathTests(unittest.TestCase):
    def test_exact_four_phase_identities_keep_shape_and_traffic_independent(self):
        expected = {'original': (False, False, False), 'mirrored': (True, True, False),
                    'opposite-side': (True, False, True), 'opposite-side-mirrored': (False, True, True)}
        for key, flags in expected.items():
            phase = paths.PHASES[key]
            self.assertEqual(phase[3:], flags)
            self.assertEqual(paths.phase_for_piece({'id': phase.piece_id, 'transition_variant': key}), phase)
            with self.assertRaises(ValueError):
                paths.phase_for_piece({'id': paths.PIECE_ID, 'transition_variant': key+'-unknown'})
        with self.assertRaises(TypeError):
            paths.PHASES['original'] = paths.PHASES['mirrored']

    def test_literal_native_endpoints_have_correct_class_offsets_and_directions(self):
        # Each pair is (source class0 DD-x, class0 ground-x); class1 is the
        # opposite measured lane. These are independently posed native values.
        literal = {
            'opposite-side': {'upper': ((-2.5, 13.5), (2.5, 18.5)),
                              'lower': ((2.5, 2.5), (-2.5, -2.5))},
            'opposite-side-mirrored': {'upper': ((18.5, 2.5), (13.5, -2.5)),
                                       'lower': ((13.5, 13.5), (18.5, 18.5))},
        }
        for key, decks in literal.items():
            ports = paths.external_ports(variant=key)
            for deck, lanes in decks.items():
                for source_class, (dd_x, ground_x) in enumerate(lanes):
                    members = [p for p in ports if p['component'] == deck and p['source_class'] == source_class]
                    dd = next(p for p in members if p['point_m'][2] > 0.)
                    ground = next(p for p in members if p['point_m'][2] == 0.)
                    self.assertEqual(dd['point_m'], (dd_x, 8., 15. if deck == 'upper' else 7.5))
                    self.assertEqual(ground['point_m'], (ground_x, -88., 0.))
                    dd_in = (deck == 'upper') != paths.PHASES[key].traffic_reversed
                    self.assertEqual(dd['direction'], 'in' if dd_in else 'out')
                    self.assertEqual(ground['direction'], 'out' if dd_in else 'in')

    def test_saved_four_lanes_eight_endpoints_and_four_rotations_keep_signed_grades(self):
        for key in NEW:
            piece, resources = new_fixture(key)
            report = paths.check_paths(resources, piece)
            self.assertEqual(report['complete_directed_journeys'], 4)
            self.assertEqual(report['complete_native_boundary_members_checked'], 8)
            self.assertEqual(report['model_only_cells'], piece['engineering']['model_only_cells'])
            self.assertEqual(report['proper_rotations_checked'], 4)
            expected = paths.expected_cell_routes(variant=key)
            for cell, records in expected.items():
                for row in records:
                    self.assertEqual(row['lane'], row['source_class']+(1 if cell[1] == 5 else 0))
                    signed = [b[2]-a[2] for a, b in zip(row['points'], row['points'][1:]) if abs(b[2]-a[2]) > 1e-10]
                    positive = (row['component'] == 'lower') != paths.PHASES[key].traffic_reversed
                    self.assertTrue(all((value > 0.) == positive for value in signed))
            self.assertLess(report['maximum_grade_percent'], 20.)

    def test_upper_bend_handedness_is_not_any_existing_proper_rotation(self):
        for key in ("original", "mirrored", *NEW):
            ports = paths.external_ports(variant=key)
            upper = [p for p in ports if p['component'] == 'upper' and p['source_class'] == 0]
            dd = next(p for p in upper if p['point_m'][2] == 15.)
            ground = next(p for p in upper if p['point_m'][2] == 0.)
            tangent = (*dd['tangent'], 0.)
            delta = (ground['point_m'][0]-dd['point_m'][0], ground['point_m'][1]-dd['point_m'][1], 0.)
            for rotation in range(4):
                a, b = paths._rotate(tangent, rotation), paths._rotate(delta, rotation)
                determinant = a[0]*b[1]-a[1]*b[0]
                self.assertAlmostEqual(determinant, 16. if key in NEW else -16.)

    def test_new_facing_pair_preserves_all_four_directed_native_dd_lanes(self):
        report = paths.check_opposite_end_direction_pair(opposite_side=True)
        self.assertEqual(report['native_dd_lanes_checked'], 4)
        self.assertEqual(report['mirrored_quarter_turns'], 2)
        self.assertFalse(report['construction_or_game_connection_tested'])

    def test_reverse_without_swapping_native_lane_classes_is_rejected(self):
        for key in NEW:
            phase = paths.PHASES[key]
            piece, _ = new_fixture(key)
            _, old = fixture(mirrored=phase.physical_reflection)
            wrong = {}
            for address, raw in old.items():
                rows = parse_paths(raw)['routes']
                for row in rows:
                    row['points'].reverse()
                    row['entry'], row['exit'] = row['exit'], row['entry']
                wrong[address] = encode(rows)
            with self.assertRaisesRegex(ValueError, 'independent|omits'):
                paths.check_paths(wrong, piece)

    def test_new_types_cannot_relax_the_retained_twenty_percent_ceiling(self):
        for key in NEW:
            piece, resources = new_fixture(key)
            piece['engineering']['max_grade_percent'] = 30.
            with self.assertRaisesRegex(ValueError, 'twenty-percent'):
                paths.check_paths(resources, piece)

    def test_shape_words_and_new_flat_base_policy_are_independent_of_traffic(self):
        for key in NEW:
            phase = paths.PHASES[key]
            piece, resources = new_fixture(key)
            words = paths.MIRRORED_CORE_ROAD_WORDS if phase.physical_reflection else paths.CORE_ROAD_WORDS
            fields = {'CellLayout': ['ab.<', 'cd..', 'ef..', 'gh..', 'ij..', 'kl..', '^...'],
                      'ConsLayout': ['##.<', '##..', '##..', '##..', '##..', '##..', '^...'],
                      'Costs': ['1000'], 'CheckType': [f'{chr(97+i)} - dirtroad: 0x{word:08x}'
                                                      for i, word in enumerate(words)]}
            proof = paths.check_construction_fields(fields, piece, resources)
            self.assertEqual(proof['terrain_constraints']['proper_rotations_checked'], 4)
            fields['ConsLayout'][0] = '+#.<'
            with self.assertRaises(ValueError):
                paths.check_construction_fields(fields, piece, resources)


class OppositeSideIndependentModelTests(unittest.TestCase):
    def test_native_cross_section_uses_exact_negated_asymmetric_source(self):
        self.assertEqual(models._bounds('upper', 0., profile_reflected=True), (-models.DD_MAX, -models.DD_MIN))
        self.assertEqual(models._bounds('upper', 96., profile_reflected=True), (-8., 8.))
        for key in NEW:
            native = models._uv('upper', 0., -2.5, 'native-dd', variant=key)
            self.assertEqual(native[0], (2.5-models.DD_MIN)/models.DD_WIDTH)
            station = 16. if paths.PHASES[key].traffic_reversed else 0.
            self.assertEqual(native[1], (station-models.DD_OFFSET)/models.DD_WIDTH)
            original = models._uv('upper', 0., -2.5, 'native-dd')
            self.assertGreater(abs(native[0]-(1.-original[0])), 1e-5)

    def test_atlas_pixels_follow_traffic_phase_while_surface_u_handles_source_reflection(self):
        for key in NEW:
            low, high = models._bounds('upper', 20., profile_reflected=True)
            first = models._uv('upper', 20., low, 'atlas', variant=key)
            last = models._uv('upper', 20., high, 'atlas', variant=key)
            self.assertGreater(first[0], last[0])
        native = {}
        for iid, offset in ((0x5713000E, 0), (0x5703000E, 20)):
            image = Image.new('RGBA', (128, 128))
            image.putdata([(x, y, offset, 255) for y in range(128) for x in range(128)])
            native[iid] = image
        values = [models.reconstruct_atlas(native, variant=key) for key in NEW]
        self.assertNotEqual(hashlib.sha256(values[0]).hexdigest(), hashlib.sha256(values[1]).hexdigest())
        # At an elevated native end station, the vertical image coordinate
        # differs, while the atlas itself retains source-normal lateral wear.
        row, column = 128, 8
        index = (row*512+column)*4
        self.assertEqual(values[0][index], values[1][index])
        self.assertNotEqual(values[0][index+1], values[1][index+1])

    def test_opposite_source_profile_winding_and_uv_cannot_use_an_old_face(self):
        for key in NEW:
            expected = next(deepcopy(p) for p in models._surface_contract(variant=key)
                            if p['role'] == 'upper-pavement-native-dd')
            old = next(p for p in models._surface_contract(paths.PHASES[key].traffic_reversed)
                       if p['role'] == expected['role'])
            actual = {**expected, 'texture': 0, 'material': {}}
            with patch.object(models, '_surface_contract', return_value=(expected,)), patch.object(models, '_material'):
                self.assertTrue(models.check_complete_surfaces([actual], 0x7f700000, variant=key)['passed'])
                for kind in ('old_xyz', 'old_uv', 'winding', 'missing'):
                    bad = deepcopy(actual)
                    if kind == 'old_xyz': bad['points'] = old['points']
                    elif kind == 'old_uv': bad['uv'] = old['uv']
                    elif kind == 'winding':
                        bad['points'] = tuple(reversed(bad['points']))
                        bad['uv'] = tuple(reversed(bad['uv']))
                    with self.subTest(key=key, mutation=kind), self.assertRaises(ValueError):
                        models.check_complete_surfaces([] if kind == 'missing' else [bad], 0x7f700000, variant=key)

    def test_saved_model_overhang_follows_native_pose_instead_of_physical_shape(self):
        from scp_highway.ramp_geometry import pack_road_model
        for key, sign in (('opposite-side', 1.), ('opposite-side-mirrored', -1.)):
            x = sign*8.0005
            raw = pack_road_model([((x, 15., 0., 0., 0.), (x, 15., 1., 0., 1.),
                                    (sign*7.9, 15., 0., 1., 0.))], 0x5713000e)
            parsed = parse_s3d(raw)
            parsed['meshes'][0]['name'] = b'SCP DD transition upper-pavement-native-dd\0'
            raw = pack_s3d(parsed)
            cell = (1, 0) if sign > 0. else (0, 0)
            self.assertTrue(models.decode_faces(raw, cell, variant=key))
            old_shape = 'mirrored' if paths.PHASES[key].physical_reflection else 'original'
            with self.assertRaisesRegex(ValueError, 'envelope|unowned geometry'):
                models.decode_faces(raw, cell, variant=old_shape)

    def test_new_phase_does_not_inherit_the_old_positive_ground_shoulder_exception(self):
        points = ((8., 0., 0.), (8.00001, 0., 0.), (8., 1., 0.))
        faces = [{'role': role, 'points': points}
                 for role in ('upper-body', 'lower-pavement-native-ground')]
        self.assertTrue(models.check_deck_clearance(faces)['passed'])
        with self.assertRaisesRegex(ValueError, 'intersects or drops below'):
            models.check_deck_clearance(faces, profile_reflected=True)


if __name__ == '__main__':
    unittest.main()
