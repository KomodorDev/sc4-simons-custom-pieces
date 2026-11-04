"""Mutation controls for independently measured whole-cell parallel traffic."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp.track_paths import PATH
from scp_highway import parallel_verify as verify
from scp_highway.assembly_verify import decode_placed_routes


def fixture():
    """Encode a distinct test stream from literal independently split routes."""
    pieces, resources, scene = [], {}, {'id': verify.SUBJECT, 'placements': []}
    for index, (key, cells) in enumerate(verify.PARTITIONS.items()):
        origin = min(c[0] for c in cells), min(c[1] for c in cells)
        local = sorted(([c[0] - origin[0], c[1] - origin[1]] for c in cells), key=lambda c: (c[1], c[0]))
        tile_ids = [f'{0x5F900000 + index * 0x1000 + c[0] * 256 + c[1] * 16:08x}' for c in local]
        piece = {'id': 'parallel-fixture-' + key, 'domain': 'highway',
                 'recipe': verify.PREFIX + key.replace('-', '_'), 'geometry_key': 'parallel-' + key,
                 'cells': local, 'tile_ids': tile_ids,
                 'footprint': [max(c[a] for c in local) + 1 for a in (0, 1)],
                 'engineering': {'max_grade_percent': 30., 'pavement_path_offset_m': 0.,
                                 'car_corridor_half_width_m': 1.25, 'car_corridor_height_m': 3.8}}
        archive = {}
        for cell, tile in zip(local, tile_ids):
            source = cell[0] + origin[0], cell[1] + origin[1]
            routes = verify.expected_cell_routes()[source]
            lines = ['SC4PATHS', '1.2', str(len(routes)), '0', '0']
            for route_index, route in enumerate(routes):
                points = [(p[0] - 16. * source[0], p[1] + 16. * source[1], p[2]) for p in route['points']]
                entry = verify._endpoint_edge(points[0], points[1])
                exit_ = verify._endpoint_edge(points[-1], points[-2])
                lines.extend(map(str, (route['transport'], route_index + 1, entry, exit_, 0, len(points))))
                lines.extend(','.join(f'{v:.6f}' for v in p) for p in points)
            archive[*PATH, int(tile, 16)] = ('\r\n'.join(lines) + '\r\n').encode('ascii')
        pieces.append(piece)
        resources[piece['id']] = archive
        scene['placements'].append({'piece_id': piece['id'], 'origin_m': [16. * (origin[0] + 3),
                                                                       -16. * (origin[1] + 3)],
                                    'rotation_degrees_ccw': 0})
    return {'pieces': pieces}, scene, resources


class ParallelSavedTrafficTests(unittest.TestCase):
    def setUp(self):
        self.manifest, self.scene, self.resources = fixture()

    def test_all_native_services_and_exact_four_approved_transfers_survive_saved_encoding(self):
        report = verify.verify_assembly_resources(self.manifest, self.scene, self.resources, inspect_models=False)
        self.assertTrue(report['saved_path_checks_passed'])
        self.assertTrue(report['saved_ownership_checks_passed'])
        self.assertFalse(report['saved_path_and_construction_checks_passed'])
        self.assertEqual(report['package_construction_checks'], 'not-run')
        self.assertFalse(report['saved_resource_checks_passed'])
        self.assertEqual(report['construction']['unique_owned_cells'], 31)
        self.assertEqual(report['paths']['external_native_channels'], 20)
        self.assertEqual(report['paths']['native_through_lane_and_sidewalk_journeys'], 10)
        self.assertEqual(report['paths']['pedestrian_external_channels'], 4)
        self.assertEqual(report['paths']['right_turn_transfers'], 4)
        self.assertTrue(report['paths']['no_cross_avenue_transfers'])
        self.assertEqual([r['quarter_turns_ccw'] for r in report['proper_rotation_paths']], [0, 1, 2, 3])
        self.assertEqual(report['game_operation'], 'unverified')

    def test_a_missing_native_pedestrian_channel_fails_before_graph_extraction(self):
        piece = self.manifest['pieces'][0]
        archive = self.resources[piece['id']]
        key = next(iter(archive))
        raw = archive[key].decode('ascii')
        # An actual encoded coordinate change, rather than a declaration-only
        # mutation, must invalidate the independent complete route contract.
        self.assertIn('7.300000', raw)
        archive[key] = raw.replace('7.300000', '7.000000', 1).encode('ascii')
        with self.assertRaisesRegex(ValueError, 'approved/native routes'):
            verify.check_paths(archive, piece)

    def test_a_shifted_ramp_height_cannot_be_hidden_by_the_engineering_declaration(self):
        piece = next(p for p in self.manifest['pieces'] if p['geometry_key'] == 'parallel-upper-exit-departure')
        archive = self.resources[piece['id']]
        key = next(iter(archive))
        archive[key] = archive[key].replace(b'15.000000', b'14.000000', 1)
        with self.assertRaisesRegex(ValueError, 'approved/native routes'):
            verify.check_paths(archive, piece)

    def test_duplicate_or_moved_owner_is_rejected_even_when_resources_remain_valid(self):
        self.scene['placements'][-1]['origin_m'][0] += 16.
        with self.assertRaisesRegex(ValueError, 'approved union'):
            verify.verify_assembly_resources(self.manifest, self.scene, self.resources, inspect_models=False)

    def test_changed_sparse_partition_or_corridor_is_rejected(self):
        for field, value in (('cells', [[0, 0]]), ('engineering', {'max_grade_percent': 40.})):
            piece = deepcopy(self.manifest['pieces'][0])
            piece[field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                verify.check_paths(self.resources[piece['id']], piece)

    def test_intrinsic_connector_contracts_include_hybrid_native_and_ramp_services(self):
        counts = {}
        for piece in self.manifest['pieces']:
            contract = verify.reviewed_contract(piece)
            counts[piece['geometry_key']] = len(contract['ports']), len(contract['movements'])
            self.assertEqual(set(contract['ports']), set(contract['port_transports']))
            self.assertEqual(set(contract['ports']), set(contract['port_directions']))
        self.assertEqual(counts['parallel-crossing'], (24, 12))
        self.assertEqual(counts['parallel-lower-exit-grade'], (10, 5))
        self.assertEqual(counts['parallel-upper-entry-departure'], (2, 1))

    def test_reversing_an_actual_exit_creates_a_forbidden_transfer_and_fails(self):
        pieces = {p['id']: p for p in self.manifest['pieces']}
        owners, _shift = verify.check_owned_cells(pieces, self.scene)
        routes = decode_placed_routes(owners, self.resources)
        approved = [route for records in verify.expected_cell_routes().values()
                    for route in records if route.get('approved_ramp') == 'lower-off']
        for route in list(routes):
            if any(verify._same_routes([route], [expected]) for expected in approved):
                routes.append({**route, 'id': len(routes), 'entry': route['exit'], 'exit': route['entry'],
                               'points': list(reversed(route['points']))})
        with self.assertRaisesRegex(ValueError, 'disconnected native boundary|forbidden cross-Avenue turn'):
            verify.check_saved_routes(routes)

    def test_missing_a_saved_ramp_fragment_fails_whole_graph_even_without_source_comparison(self):
        pieces = {p['id']: p for p in self.manifest['pieces']}
        owners, _shift = verify.check_owned_cells(pieces, self.scene)
        routes = decode_placed_routes(owners, self.resources)
        target = next(route for route in routes if 'upper-exit-departure' in route['piece_id'])
        routes.remove(target)
        with self.assertRaisesRegex(ValueError, 'disconnected native boundary|required right turn'):
            verify.check_saved_routes(routes)


if __name__ == '__main__':
    unittest.main()
