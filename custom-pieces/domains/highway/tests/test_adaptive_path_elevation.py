"""Replay the bounded surface-copy height branch, without claiming a game test."""
from copy import deepcopy
import math
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp import adaptive_network, jsonc
from scp.verify import parse_paths
from scp_highway import adaptive_ground as writer
from scp_highway.native import encode_paths
import test_adaptive_ground as fixture


def turn(point, quarter):
    east, north, height = point
    east, north = ((east, north), (north, -east), (-east, -north), (-north, east))[quarter % 4]
    return east, north, height


def flat_surface_copy(raw, rotation, datum):
    """Synthetic replay of the confirmed normal-group height branch only.

    Windows 641 GetPathInfo does not promote ordinary group69668828 resources.
    Its CreateTransformedCopy calls UseElevation (0x5410a1): false overwrites
    height with occupant GetAltitude (0x5410b6); true keeps the transformed
    authored height. Flat terrain makes that branch independently exact.
    This is not a pathfinder, construction engine, or in-game join test.
    """
    paths = parse_paths(raw)
    result = deepcopy(paths['routes'])
    for route in result:
        route['entry'] = (route['entry'] + rotation) % 4
        route['exit'] = (route['exit'] + rotation) % 4
        route['points'] = [(*turn(point, rotation)[:2], datum + (point[2] if paths['terrain'] else 0.0))
                           for point in route['points']]
    return result


class AdaptivePathElevationTests(unittest.TestCase):
    def test_zero_pose_changes_only_the_header_token_and_never_canonical_bytes(self):
        original = b'-- retained heading\r\n' + encode_paths(fixture.routes())
        before = bytes(original)
        active = writer.posed_path_alias(original, 0, use_path_elevation=True)
        self.assertEqual(active, original.replace(b'\r\n0\r\n0\r\n', b'\r\n0\r\n1\r\n', 1))
        self.assertEqual(parse_paths(active)['terrain'], 1)
        self.assertEqual(parse_paths(active)['routes'], parse_paths(original)['routes'])
        self.assertEqual(original, before)

    def test_absent_and_false_preserve_legacy_alias_bytes_in_every_pose(self):
        original = encode_paths(fixture.routes())
        for pose in range(4):
            with self.subTest(pose=pose):
                legacy = writer.posed_path_alias(original, pose)
                self.assertEqual(writer.posed_path_alias(original, pose, use_path_elevation=False), legacy)
                self.assertEqual(parse_paths(legacy)['terrain'], 0)
                elevated = writer.posed_path_alias(original, pose, use_path_elevation=True)
                self.assertEqual(elevated, legacy.replace(b'\r\n0\r\n0\r\n', b'\r\n0\r\n1\r\n', 1))

    def test_alias_api_rejects_boolean_lookalikes(self):
        for value in (0, 1, None, 'true', [], {}):
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, 'must be a boolean'):
                writer.posed_path_alias(encode_paths(fixture.routes()), 0, use_path_elevation=value)

    def test_historical_alias_flattens_both_decks_and_loses_synthetic_elevated_join(self):
        original = encode_paths(fixture.routes())
        # The 4 m radius is the game's lane-continuity endpoint query. This
        # control reproduces its height failure, without simulating its graph.
        for pose in (0, 2):
            raw = writer.posed_path_alias(original, pose)
            for quarter in range(4):
                runtime = flat_surface_copy(raw, pose + quarter, 40.0)
                for index, height in ((0, 15.0), (1, 7.5)):
                    source_start = turn(fixture.routes()[index]['points'][0], quarter)
                    fixed_neighbor_end = (*source_start[:2], 40.0 + height)
                    with self.subTest(pose=pose, quarter=quarter, deck=height):
                        self.assertTrue(all(point[2] == 40.0 for point in runtime[index]['points']))
                        self.assertAlmostEqual(math.dist(runtime[index]['points'][0], fixed_neighbor_end), height)
                        self.assertGreater(math.dist(runtime[index]['points'][0], fixed_neighbor_end), 4.0)

    def test_elevation_opt_in_retains_both_real_deck_heights_and_flat_ground_in_four_rotations(self):
        original = encode_paths(fixture.routes())
        for pose in (0, 2):
            raw = writer.posed_path_alias(original, pose, use_path_elevation=True)
            for quarter in range(4):
                runtime = flat_surface_copy(raw, pose + quarter, 40.0)
                for source, actual in zip(fixture.routes(), runtime):
                    expected = [(*turn(point, quarter)[:2], 40.0 + point[2]) for point in source['points']]
                    with self.subTest(pose=pose, quarter=quarter, height=source['points'][0][2]):
                        self.assertEqual(actual['points'], expected)
                        self.assertEqual((actual['transport'], actual['lane'], actual['compatibility']),
                                         (source['transport'], source['lane'], source['compatibility']))
                        self.assertEqual(actual['entry'], (source['entry'] + quarter) % 4)
                        self.assertEqual(actual['exit'], (source['exit'] + quarter) % 4)
                        self.assertEqual(math.dist(actual['points'][0], expected[0]), 0.0)
                self.assertEqual({point[2] - 40.0 for route in runtime for point in route['points']}, {0.0, 7.5, 15.0})

    def test_build_changes_only_active_path_headers_and_preserves_legacy_resources(self):
        for key in ('access-core', 'northwest-junction', 'southeast-junction'):
            piece = fixture.spec(key)
            source = fixture.compiled(piece)
            source_before = deepcopy(source)
            context = {'adaptive_avenue': fixture.capture()}
            active = writer.build_resources(piece, context, source)
            legacy_piece = deepcopy(piece)
            legacy_piece['adaptive_ground'].pop('use_path_elevation')
            legacy = writer.build_resources(legacy_piece, context, source)
            explicit_false = deepcopy(legacy_piece)
            explicit_false['adaptive_ground']['use_path_elevation'] = False
            self.assertEqual(writer.build_resources(explicit_false, context, source), legacy)
            self.assertEqual(active.keys(), legacy.keys())
            for resource, raw in legacy.items():
                with self.subTest(piece=key, resource=resource):
                    expected = (raw.replace(b'\r\n0\r\n0\r\n', b'\r\n0\r\n1\r\n', 1)
                                if resource[:2] == writer.AVENUE_PATH else raw)
                    self.assertEqual(active[resource], expected)
            self.assertEqual(source, source_before)

    def test_exactly_nine_current_owners_opt_in_for_all_forty_six_cells(self):
        expected = {'ddrhw-diagonal-access-core', 'ddrhw-diagonal-northwest-junction',
                    'ddrhw-diagonal-southeast-junction', 'ddrhw-modular-highway-stamp',
                    'ddrhw-modular-northwest-terminal-r40', 'ddrhw-modular-southeast-terminal-r40',
                    'ddrhw-parallel-crossing', 'ddrhw-parallel-northwest-terminal',
                    'ddrhw-parallel-southeast-terminal'}
        owners, count = set(), 0
        for path in (ROOT / 'domains/highway/00_pieces').glob('*/piece.jsonc'):
            piece = jsonc.load(path)
            if 'adaptive_ground' not in piece:
                continue
            owners.add(piece['id'])
            self.assertIs(piece['adaptive_ground']['use_path_elevation'], True)
            count += len(adaptive_network.bindings(piece))
        self.assertEqual(owners, expected)
        self.assertEqual(count, 46)


if __name__ == '__main__':
    unittest.main()
