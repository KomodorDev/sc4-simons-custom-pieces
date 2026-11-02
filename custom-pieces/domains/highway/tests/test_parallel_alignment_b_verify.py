"""Independent B lattice, serialized PATH, and directed-traffic mutations."""
from copy import deepcopy
import math
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp.track_paths import PATH
from scp_highway import parallel_alignment_b_verify as verify
from scp_highway import parallel_verify as reference
from scp_highway.assembly_verify import decode_placed_routes


def encode(routes, cell):
    """A test-only serializer, separate from both native and B writers."""
    lines = ['SC4PATHS', '1.2', str(len(routes)), '0', '0']
    for index, route in enumerate(routes):
        points = [(p[0] - 16. * cell[0], p[1] + 16. * cell[1], p[2]) for p in route['points']]
        entry = reference._endpoint_edge(points[0], points[1])
        exit_ = reference._endpoint_edge(points[-1], points[-2])
        lines.extend(map(str, (route['transport'], index + 1, entry, exit_, 0, len(points))))
        lines.extend(','.join(format(value, '.9f') for value in point) for point in points)
    return ('\r\n'.join(lines) + '\r\n').encode('ascii')


def fixture():
    pieces, resources, scene = [], {}, {'id': verify.SUBJECT, 'placements': []}
    for index, (key, cells) in enumerate(verify.PARTITIONS.items()):
        origin = min(c[0] for c in cells), min(c[1] for c in cells)
        local = sorted(([c[0] - origin[0], c[1] - origin[1]] for c in cells), key=lambda c: (c[1], c[0]))
        tiles = [f'{0x5F900000 + index * 0x1000 + cell[0] * 256 + cell[1] * 16:08x}' for cell in local]
        piece = {'id': 'b-fixture-' + key, 'domain': 'highway',
                 'recipe': verify.PREFIX + key.replace('-', '_'), 'geometry_key': 'parallel-b-' + key,
                 'cells': local, 'tile_ids': tiles,
                 'footprint': [max(cell[a] for cell in local) + 1 for a in (0, 1)],
                 'shadow_mode': 'model-carrier', 'model_shadows': {'enabled': False},
                 'engineering': {'max_grade_percent': 30., 'pavement_path_offset_m': 0.,
                    'grid_alignment': 'B', 'alignment_a_translation_en_m': [8., 8.], 'avenue_phase_offset': 1,
                    'car_corridor_half_width_m': 1.25, 'car_corridor_height_m': 3.8,
                    'highway_slip_profile': reference.HIGHWAY_SLIP_PROFILE,
                    **({'ground_mouth_profile': reference.GROUND_MOUTH_PROFILE} if key.endswith('terminal') else {})}}
        archive = {}
        for cell, tile in zip(local, tiles):
            source = cell[0] + origin[0], cell[1] + origin[1]
            archive[*PATH, int(tile, 16)] = encode(verify.expected_cell_routes()[source], source)
        pieces.append(piece)
        resources[piece['id']] = archive
        scene['placements'].append({'piece_id': piece['id'], 'origin_m': [16. * (origin[0] + 3),
                                                                       -16. * (origin[1] + 4)],
                                    'rotation_degrees_ccw': 0})
    return {'pieces': pieces}, scene, resources


class ParallelAlignmentBVerifyTests(unittest.TestCase):
    def setUp(self):
        self.manifest, self.scene, self.resources = fixture()

    def decoded(self):
        pieces = {piece['id']: piece for piece in self.manifest['pieces']}
        owners, _shift = verify.check_owned_cells(pieces, self.scene)
        return decode_placed_routes(owners, self.resources)

    def test_all_native_lanes_sidewalks_right_turns_and_proper_rotations_are_preserved(self):
        report = verify.verify_assembly_resources(self.manifest, self.scene, self.resources, inspect_models=False)
        self.assertEqual(report['construction']['unique_owned_cells'], 34)
        self.assertEqual(report['construction']['bounding_rectangle_tiles'], [9, 9])
        self.assertEqual(report['paths']['external_native_channels'], 20)
        self.assertEqual(report['paths']['native_through_lane_and_sidewalk_journeys'], 10)
        self.assertEqual(report['paths']['constant_height_straight_native_journeys'], 10)
        self.assertEqual(report['paths']['pedestrian_external_channels'], 4)
        self.assertEqual(report['paths']['right_turn_transfers'], 4)
        self.assertTrue(report['paths']['no_cross_avenue_transfers'])
        self.assertEqual([row['quarter_turns_ccw'] for row in report['proper_rotation_paths']], [0, 1, 2, 3])
        self.assertTrue(report['saved_path_checks_passed'])
        self.assertFalse(report['saved_resource_checks_passed'])
        self.assertEqual(report['game_operation'], 'unverified')

    def test_measured_eight_end_collars_are_flat_on_the_next_native_grid_edge(self):
        expected = {'lower-off': ((72., 67.2, 7.5), (-8., 35.2, 0.)),
                    'lower-on': ((-19.2, 24., 0.), (-51.2, -56., 7.5)),
                    'upper-off': ((-56., -67.2, 15.), (24., -19.2, 0.)),
                    'upper-on': ((35.2, -8., 0.), (83.2, 72., 15.))}
        for ramp in verify.traffic_routes():
            with self.subTest(ramp=ramp['id']):
                for actual, literal in zip((ramp['points'][0], ramp['points'][-1]), expected[ramp['id']]):
                    for value, wanted in zip(actual, literal):
                        self.assertAlmostEqual(value, wanted, places=9)
                self.assertEqual(ramp['points'][0][2], ramp['points'][1][2])
                self.assertEqual(ramp['points'][-1][2], ramp['points'][-2][2])

    def test_adjacent_ground_phase_keeps_the_same_directed_highway_and_cannot_be_a_rotation(self):
        for cell in verify.OWNED_CELLS:
            wanted = [route for route in reference.expected_cell_routes()[cell]
                      if route['points'][0][2] > 1.] if cell in reference.OWNED_CELLS else []
            highway = [{**route, 'points': [(p[0] + 16. * cell[0], p[1] - 16. * cell[1], p[2])
                                           for p in route['points']]}
                       for route in verify.native_routes(*cell) if route['points'][0][2] > 1.]
            if wanted:
                wanted = [route for route in wanted if 'approved_ramp' not in route]
                self.assertTrue(reference._same_routes(highway, wanted))
            for route in highway:
                progress = route['points'][-1][0] - route['points'][0][0]
                self.assertGreater(progress, 0.) if route['points'][0][2] == 15. else self.assertLess(progress, 0.)
        self.assertEqual(verify.TRANSLATION_M, (8., 8.))
        self.assertEqual({round(p[0] + p[1], 1) for route in verify.native_routes(1, 0)
                          if route['transport'] == 1 and route['points'][0][2] == 0.
                          for p in route['points']}, {-11.2, -4.8, 4.8, 11.2})

    def test_every_native_external_lane_has_its_actual_outside_neighbour(self):
        report = verify.check_native_boundary_neighbours()
        self.assertEqual(report['complete_directed_native_counterparts_checked'], 20)
        southeast = [row for row in report['boundaries'] if row['outside_cell'] == [2, 1]]
        self.assertEqual(len(southeast), 6)
        self.assertEqual(sum(row['transport'] == 1 for row in southeast), 4)
        self.assertEqual(sum(row['transport'] == 2 for row in southeast), 2)
        self.assertFalse(report['native_dragging_observed'])

    def test_using_alignment_a_avenue_phase_fails_its_actual_saved_bytes(self):
        piece = next(piece for piece in self.manifest['pieces'] if piece['geometry_key'] == 'parallel-b-crossing')
        local, tile = piece['cells'][0], piece['tile_ids'][0]
        origin = verify._source_origin(piece)
        source = local[0] + origin[0], local[1] + origin[1]
        from scp_highway.assembly_verify import _native_routes
        wrong = [{**route, 'points': [(p[0] + 16. * source[0], p[1] - 16. * source[1], p[2])
                                       for p in route['points']]} for route in _native_routes(*source)]
        self.resources[piece['id']][*PATH, int(tile, 16)] = encode(wrong, source)
        with self.assertRaisesRegex(ValueError, 'native phase'):
            verify.check_paths(self.resources[piece['id']], piece)

    def test_missing_pedestrian_channel_is_not_hidden_by_working_car_routes(self):
        routes = self.decoded()
        target = next(route for route in routes if route['transport'] == 2)
        routes.remove(target)
        with self.assertRaisesRegex(ValueError, 'disconnected native boundary|pedestrian channel|through lane'):
            verify.check_saved_routes(routes)

    def test_missing_ramp_fragment_is_rejected_by_the_full_directed_graph(self):
        routes = self.decoded()
        target = next(route for route in routes if route['piece_id'] == 'b-fixture-upper-exit-departure')
        routes.remove(target)
        with self.assertRaisesRegex(ValueError, 'disconnected native boundary|required right turn'):
            verify.check_saved_routes(routes)

    def test_ground_detour_with_connected_endpoints_cannot_replace_a_native_bridge_lane(self):
        routes = self.decoded()
        target = next(route for route in routes if route['points'][0][2] == 15.
                      and route['piece_id'] == 'b-fixture-crossing')
        first, last = target['points'][0], target['points'][-1]
        # Endpoints, first/last tangent, and the route graph remain connected;
        # only the interior descends. Endpoint-only reachability must fail.
        target['points'] = [first,
            tuple(.75 * a + .25 * b for a, b in zip(first, last)),
            ((first[0] + last[0]) / 2., (first[1] + last[1]) / 2., 0.),
            tuple(.25 * a + .75 * b for a, b in zip(first, last)), last]
        with self.assertRaisesRegex(ValueError, 'takes a ramp|straight spine'):
            verify.check_saved_routes(routes)

    def test_a_removed_rotation_or_owned_tile_is_not_mistaken_for_same_alignment(self):
        pieces = {piece['id']: piece for piece in self.manifest['pieces']}
        self.scene['placements'][0]['rotation_degrees_ccw'] = 180
        with self.assertRaisesRegex(ValueError, 'proper rotation'):
            verify.check_owned_cells(pieces, self.scene)
        self.scene['placements'][0]['rotation_degrees_ccw'] = 0
        self.scene['placements'][0]['origin_m'][0] += 16.
        with self.assertRaisesRegex(ValueError, '34-cell union'):
            verify.check_owned_cells(pieces, self.scene)

    def test_enabled_shadows_and_wider_ground_mouths_are_rejected(self):
        piece = next(piece for piece in self.manifest['pieces'] if piece['geometry_key'] == 'parallel-b-northwest-terminal')
        for change, message in ((lambda p: p['model_shadows'].update(enabled=True), 'no-shadow'),
                                (lambda p: p['engineering'].pop('ground_mouth_profile'), 'narrowed')):
            changed = deepcopy(piece)
            change(changed)
            with self.subTest(message=message), self.assertRaisesRegex(ValueError, message):
                verify.check_paths(self.resources[piece['id']], changed)

    def test_old_accepted_alignment_a_fixture_remains_reproducible(self):
        from test_parallel_saved_paths import fixture as old_fixture
        manifest, scene, resources = old_fixture()
        report = reference.verify_assembly_resources(manifest, scene, resources, inspect_models=False)
        self.assertEqual(report['construction']['unique_owned_cells'], 31)
        self.assertEqual(report['paths']['native_through_lane_and_sidewalk_journeys'], 10)
        self.assertEqual(report['paths']['right_turn_transfers'], 4)
        self.assertEqual(report['construction']['bounding_rectangle_tiles'], [8, 8])

    def test_b_reference_reconstruction_never_mutates_the_cached_a_shoulder_revision(self):
        original = deepcopy(reference.revised_routes(reference.HIGHWAY_SLIP_PROFILE))
        verify.physical_routes.cache_clear()
        verify.traffic_routes.cache_clear()
        verify.expected_cell_routes.cache_clear()
        verify.physical_routes()
        self.assertEqual(reference.revised_routes(reference.HIGHWAY_SLIP_PROFILE), original)

    def test_b_native_neighbor_pose_changes_are_rejected_independently(self):
        original = verify.native_routes
        def wrong(column, row):
            rows = original(column, row)
            if (column, row) == (2, 1):
                rows = deepcopy(rows)
                rows[0]['points'][0] = (rows[0]['points'][0][0] + .1, *rows[0]['points'][0][1:])
            return rows
        with patch.object(verify, 'native_routes', side_effect=wrong):
            with self.assertRaisesRegex(ValueError, 'native neighbour counterpart|heading'):
                verify.check_native_boundary_neighbours()

    def test_complete_intrinsic_semantics_agree_with_the_shared_saved_path_reader(self):
        from scp.connectivity import piece_connectivity
        from scp_highway.connections import service_classifier
        totals = [0, 0]
        for piece in self.manifest['pieces']:
            contract, facts = verify.reviewed_contract(piece), verify.reviewed_facts(piece)
            actual = piece_connectivity(piece, self.resources[piece['id']], contract=contract,
                                        service_classifier=service_classifier)
            ports = {port['id']: port for port in actual['ports']}
            self.assertEqual(set(ports), {port['id'] for port in facts['ports']})
            for expected in facts['ports']:
                saved = ports[expected['id']]
                with self.subTest(piece=piece['geometry_key'], port=expected['id']):
                    self.assertLessEqual(math.dist(saved['endpoint_m'], expected['endpoint_m']), 1e-6)
                    self.assertLessEqual(math.dist(saved['sampled_tangent'], expected['sampled_tangent']), 1e-9)
                    self.assertAlmostEqual(saved['grade'], expected['grade'], places=9)
                    for key in ('direction', 'engine_transport', 'edge', 'service_network', 'service_family',
                                'variant', 'role', 'channel_kind', 'traffic_modes'):
                        self.assertEqual(saved[key], expected[key])
            self.assertEqual({(journey['entry_port'], journey['exit_port']) for journey in actual['journeys']},
                             set(facts['movements']))
            self.assertEqual({(row['from_port'], row['to_port']) for row in actual['forbidden_transfers']},
                             set(facts['forbidden_transfers']))
            self.assertEqual(facts['path_hashes_by_cell'], [])
            self.assertEqual(facts['raw_path_fingerprint_status'], 'requires-independent-saved-build-freeze')
            totals[0] += len(facts['ports'])
            totals[1] += len(facts['movements'])
        self.assertEqual(totals, [200, 104])


if __name__ == '__main__':
    unittest.main()
