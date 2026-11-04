"""B ground-phase and active height/pose regressions on serialized resources."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp import adaptive_network
from scp.track_paths import PATH
from scp.verify import parse_paths
from scp_highway import adaptive_verify as verify
from test_parallel_alignment_b_verify import fixture
import test_adaptive_ground_verifier as saved


def specification(key):
    piece = next(piece for piece in fixture()[0]['pieces'] if piece['geometry_key'] == 'parallel-b-' + key)
    piece['name'] = 'Independent B adaptive fixture ' + key
    piece['engineering']['model_only_cells'] = []
    # Independently reviewed source origins and the native Avenue phases.
    origin = {'crossing': (0, -1), 'northwest-terminal': (-1, -2),
              'southeast-terminal': (1, 0)}[key]
    rows = []
    for index, cell in enumerate(piece['cells']):
        difference = cell[0] + origin[0] - cell[1] - origin[1] - 1
        rows.append({'cell': cell, 'rotation': 2 if difference == 1 else 0,
            'texture_donor_id': '04003800' if difference == 0 else '04000200',
            'street_flags': f'{0x01000100 + index * 0x10000:08x}',
            'avenue_flags': {0: '01030103', 1: '01000003', -1: '00030100'}[difference],
            'prop': True, 'resolved_tile_id': f'{0x5F980000 + index * 0x100:08x}'})
    piece['adaptive_ground'] = {'schema_version': 1, 'use_path_elevation': True,
        'construction_helper': [1, 1] if key == 'southeast-terminal' else [0, 0], 'cells': rows}
    return piece


class ParallelAlignmentBAdaptiveTests(unittest.TestCase):
    def check(self, piece, resources, hashes):
        with patch.object(verify, '_texture_hashes', return_value=hashes):
            return verify.check_resources(resources, piece)

    def test_all_eight_b_cells_preserve_each_runtime_deck_lane_sidewalk_and_apron(self):
        count = routes = textures = 0
        for key in ('crossing', 'northwest-terminal', 'southeast-terminal'):
            piece = specification(key)
            resources, hashes = saved.saved_fixture(piece)
            report = self.check(piece, resources, hashes)
            self.assertTrue(report['canonical_geometry_and_traffic_preserved'])
            self.assertEqual(report['proper_rotations_checked'], 4)
            self.assertFalse(report['game_behavior_tested'])
            count += report['adaptive_cells_checked']
            routes += report['posed_merged_path_routes_checked']
            textures += report['texture_resources_checked']
        self.assertEqual((count, routes, textures), (8, 32, 160))

    def test_b_active_height_header_cannot_flatten_both_elevated_decks(self):
        piece = specification('crossing')
        resources, hashes = saved.saved_fixture(piece)
        row = adaptive_network.bindings(piece)[0]
        key = (*verify.AVENUE_PATH, int(row['resolved_tile_id'], 16))
        self.assertEqual(parse_paths(resources[key])['terrain'], 1)
        self.assertEqual({point[2] for route in parse_paths(resources[key])['routes'] for point in route['points']},
                         {0., 7.5, 15.})
        resources[key] = resources[key].replace(b'\r\n0\r\n1\r\n', b'\r\n0\r\n0\r\n', 1)
        with self.assertRaisesRegex(ValueError, 'elevation flag'):
            self.check(piece, resources, hashes)

    def test_b_alias_cannot_drop_an_upper_lower_pedestrian_or_ramp_journey(self):
        piece = specification('crossing')
        resources, hashes = saved.saved_fixture(piece)
        row = adaptive_network.bindings(piece)[0]
        key = (*verify.AVENUE_PATH, int(row['resolved_tile_id'], 16))
        routes = parse_paths(resources[key])['routes']
        for index in range(4):
            changed = dict(resources)
            changed[key] = saved.encode_active_routes(routes[:index] + routes[index + 1:])
            with self.subTest(route=index), self.assertRaisesRegex(ValueError, 'every posed'):
                self.check(piece, changed, hashes)

    def test_b_t21_and_full_geometry_prop_rotation_are_both_required(self):
        piece = specification('crossing')
        resources, hashes = saved.saved_fixture(piece)
        row = adaptive_network.bindings(piece)[0]
        t21 = (*adaptive_network.T21, int(row['resolved_tile_id'], 16))
        prop = (*verify.PROP, int(row['canonical_tile_id'], 16))
        for key, identifier, mutate, message in (
            (t21, 0x88EDC900, lambda value: value['values'].__setitem__(2, 1), 'prop pose'),
            (prop, 0xE83A081D, lambda value: value.update(values=[0]), 'full-geometry rotation')):
            changed = dict(resources)
            saved.change_property(changed, key, identifier, mutate)
            with self.subTest(property=identifier), self.assertRaisesRegex(ValueError, message):
                self.check(piece, changed, hashes)

    def test_copying_a_ground_phase_cannot_be_hidden_by_matching_texture_bytes(self):
        piece = specification('crossing')
        changed = deepcopy(piece)
        resources, hashes = saved.saved_fixture(piece)
        # The actual B full centre is local(1,1), world(1,0). Under A it is
        # the opposite native half, so a complete A metadata copy must fail.
        row = next(row for row in changed['adaptive_ground']['cells'] if row['cell'] == [1, 1])
        row['texture_donor_id'] = '04000200'
        capture = saved.fixture.capture()
        for appearance in (0, 0x10, 0x20, 0x30):
            for zoom in range(5):
                resources[*verify.TEXTURE, int(row['resolved_tile_id'], 16) + appearance + zoom] = (
                    capture[*verify.TEXTURE, 0x04000200 + appearance + zoom])
        with self.assertRaisesRegex(ValueError, 'donor, pose, or Avenue flags'):
            self.check(changed, resources, hashes)

    def test_b_origins_are_not_added_as_mutable_aliases_of_the_accepted_a_origins(self):
        originals = dict(verify.ORIGINS)
        for key, expected in (('crossing', ((0, -1), 1)), ('northwest-terminal', ((-1, -2), 1)),
                              ('southeast-terminal', ((1, 0), 1))):
            self.assertEqual(verify._source_frame(specification(key)), expected)
        self.assertEqual(verify.ORIGINS, originals)
        self.assertEqual(verify._source_frame({'geometry_key': 'parallel-crossing'}), ((0, 0), 0))
        self.assertEqual(verify._source_frame({'geometry_key': 'parallel-northwest-terminal'}), ((-1, -1), 0))


if __name__ == '__main__':
    unittest.main()
