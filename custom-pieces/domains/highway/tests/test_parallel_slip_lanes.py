"""Independent shoulder profiles, retained geometry, and real saved mutations."""
from copy import deepcopy
import json
import math
import os
from pathlib import Path
import struct
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]
from scp.models import pack_s3d, parse_s3d, positions
from scp.track_paths import PATH, S3D
from scp.verify import parse_paths, strict_dbpf
from scp_highway import parallel_verify as verify


def fixture(profile=None):
    pieces, resources, scene = [], {}, {'id': verify.SUBJECT, 'placements': []}
    for index, (key, cells) in enumerate(verify.PARTITIONS.items()):
        origin = min(c[0] for c in cells), min(c[1] for c in cells)
        local = sorted(([c[0] - origin[0], c[1] - origin[1]] for c in cells), key=lambda c: (c[1], c[0]))
        piece = {'id': 'slip-fixture-' + key, 'domain': 'highway', 'geometry_key': 'parallel-' + key,
                 'recipe': verify.PREFIX + key.replace('-', '_'), 'cells': local,
                 'footprint': [max(c[a] for c in local) + 1 for a in (0, 1)],
                 'tile_ids': [f'{0x5F800000 + index * 0x1000 + c[0] * 256 + c[1] * 16:08x}' for c in local],
                 'engineering': {'max_grade_percent': 30., 'pavement_path_offset_m': 0.,
                                 'car_corridor_half_width_m': 1.25, 'car_corridor_height_m': 3.8}}
        if profile:
            piece['engineering']['highway_slip_profile'] = profile
        archive = {}
        for cell, tile in zip(local, piece['tile_ids']):
            world = cell[0] + origin[0], cell[1] + origin[1]
            routes = verify.expected_cell_routes(profile)[world]
            lines = ['SC4PATHS', '1.2', str(len(routes)), '0', '0']
            for lane, route in enumerate(routes, 1):
                points = [(p[0] - 16. * world[0], p[1] + 16. * world[1], p[2]) for p in route['points']]
                lines.extend(map(str, (route['transport'], lane,
                    verify._endpoint_edge(points[0], points[1]), verify._endpoint_edge(points[-1], points[-2]), 0, len(points))))
                lines.extend(','.join(f'{value:.9f}' for value in point) for point in points)
            archive[*PATH, int(tile, 16)] = ('\r\n'.join(lines) + '\r\n').encode()
        pieces.append(piece)
        resources[piece['id']] = archive
        scene['placements'].append({'piece_id': piece['id'], 'origin_m': [16. * origin[0], -16. * origin[1]],
                                    'rotation_degrees_ccw': 0})
    return {'pieces': pieces}, scene, resources


class IndependentSlipProfileTests(unittest.TestCase):
    def _assert_retained_physical_profile(self, actual, expected):
        length = 'length_total_plan_m'
        self.assertEqual(set(actual), set(expected))
        self.assertEqual({key: value for key, value in actual.items() if key != length},
                         {key: value for key, value in expected.items() if key != length})
        # Accumulated segment lengths can differ by one binary rounding step
        # across platforms. Only this aggregate gets an absolute metre bound.
        self.assertAlmostEqual(actual[length], expected[length], delta=1e-12)

    def test_actual_tiny_native_top_fragment_is_retained_only_with_explicit_opt_in(self):
        from scp_highway import ramp_geometry as geometry
        from scp_highway.ramp_verify import _covered
        from scp_highway.wheeltracks import NativeWheeltrackField
        # This genuine positive triangle was discarded in the saved01
        # shoulder remap. Its area is 4.2247689497647684e-10 square metres;
        # the resulting actual deck gap exceeded the unchanged 2 um bound.
        source = ((-44.612830095083524, -61.67852353342972, 15.),
                  (-44.61279844058805, -61.678497435858986, 15.),
                  (-44.6128297726691, -61.67849657460411, 15.))
        polygon = [(east, height, -north, 0., 0.) for east, north, height in source]
        self.assertEqual(geometry._triangulate(polygon), [])
        retained = geometry._triangulate(polygon, minimum_normal_squared=0.)
        self.assertEqual(retained, [tuple(polygon)])
        self.assertEqual(geometry._triangulate([polygon[0]] * 3, minimum_normal_squared=0.), [])
        painter = SimpleNamespace(road_segments={})
        legacy = NativeWheeltrackField([], painter)
        revised = NativeWheeltrackField([], painter, retain_nonzero_top_fragments=True)
        with patch.object(legacy, 'map_point', side_effect=lambda point, _region: point):
            self.assertEqual(list(legacy._sample(polygon, {})), [])
        with patch.object(revised, 'map_point', side_effect=lambda point, _region: point):
            self.assertEqual(list(revised._sample(polygon, {})), retained)
        # Encode in this actual cell's local float32 frame, then restore
        # ENH coordinates. The retained face still has positive area and
        # continuously supports the measured missing subsegment.
        encoded = []
        for east, north, height in source:
            x, h, south = struct.unpack('<3f', struct.pack('<3f', east + 48., height, -north - 64.))
            encoded.append((x - 48., -south - 64., h))
        a, b, c = encoded
        self.assertGreater((b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]), 0.)
        first = (-44.61282467842102, -61.67807364463806, 15.)
        last = (-44.61281967163086, -61.678523778915405, 15.)
        begin, end = [tuple(a + t * (b - a) for a, b in zip(first, last)) for t in (.95, .975)]
        face = {'points': tuple(encoded), 'upward': True}
        self.assertFalse(_covered(begin, end, []))
        self.assertTrue(_covered(begin, end, [face]))
        shifted = {**face, 'points': tuple((p[0] + .001, p[1], p[2]) for p in encoded)}
        self.assertFalse(_covered(begin, end, [shifted]))

    def test_literal_taper_parallel_samples_and_native_endpoints_match_actual_author(self):
        from scp_highway.parallel_geometry import routes
        expected = verify.revised_routes(verify.HIGHWAY_SLIP_PROFILE)
        for measured, authored in zip(expected, routes()):
            with self.subTest(ramp=measured['id']):
                self.assertEqual(len(measured['points']), 563 if measured['deck'] == 'lower' else 542)
                self.assertEqual(len(measured['points']), len(authored['points']))
                self.assertLess(max(math.dist(a, b) for a, b in zip(measured['points'], authored['points'])), 1e-11)
                self.assertEqual(measured['segments'], authored['segments'])
                outward = measured['points'] if measured['direction'] == 'off' else list(reversed(measured['points']))
                u0, _v0 = verify._uv(outward[0])
                direction = 1. if verify._uv(outward[1])[0] > u0 else -1.
                data = measured['independent_auxiliary_lane']
                parallel = [point for point in outward if abs(abs(verify._uv(point)[1]) - 5.5) < 1e-10]
                self.assertEqual(len(parallel), 33 if measured['deck'] == 'lower' else 9)
                stations = [direction * (verify._uv(point)[0] - u0) for point in parallel]
                self.assertAlmostEqual(stations[0], data['taper_m'], places=10)
                self.assertAlmostEqual(stations[-1] - stations[0], data['parallel_m'], places=10)
                self.assertAlmostEqual(math.dist(outward[0], outward[1]), .01, places=11)
                self.assertTrue(all(point[2] == measured['height_m'] for point in parallel))
        self.assertEqual(expected[0]['native_high_port'], [60.8, 56., 7.5])
        self.assertEqual(expected[1]['native_high_port'], [-56., -60.8, 7.5])
        self.assertEqual(expected[2]['native_high_port'], [-56., -67.2, 15.])
        self.assertEqual(expected[3]['native_high_port'], [67.2, 56., 15.])

    def test_all_original_physical_points_and_outside_routes_remain_exact(self):
        original = verify.approved_candidate()['routes']
        self.assertEqual(verify.revised_routes(), original)
        for old, new in zip(original, verify.revised_routes(verify.HIGHWAY_SLIP_PROFILE)):
            self.assertEqual(new['mesh_points'], old['points'])
            old_out = old['points'] if old['direction'] == 'off' else list(reversed(old['points']))
            new_out = new['points'] if new['direction'] == 'off' else list(reversed(new['points']))
            old_join = next(i for i, point in enumerate(old_out) if old['side'] * verify._uv(point)[1] >= 8.)
            new_join = next(i for i, point in enumerate(new_out) if old['side'] * verify._uv(point)[1] >= 8.)
            self.assertEqual([tuple(p) for p in old_out[old_join:]], new_out[new_join:])
            for segment in new['segments']:
                if segment['kind'] in ('straight-parallel-descent', 'ground-right-quarter-turn', 'native-avenue-lane-collar'):
                    actual = new['points'][segment['start_index']:segment['end_index'] + 1]
                    before = next(row for row in old['segments'] if row['kind'] == segment['kind'])
                    expected = old['points'][before['start_index']:before['end_index'] + 1]
                    self.assertEqual([tuple(p) for p in expected], actual)

    def test_revised_traffic_metadata_is_measured_separately_from_complete_retained_physical_profile(self):
        from scp_highway.parallel_geometry import routes
        original = verify.approved_candidate()['routes']
        independent = verify.revised_routes(verify.HIGHWAY_SLIP_PROFILE)
        for old, expected, actual in zip(original, independent, routes()):
            with self.subTest(ramp=actual['id']):
                self._assert_retained_physical_profile(actual['physical_profile'], old['profile'])
                retained_profile = deepcopy(actual['physical_profile'])
                self.assertIsNot(actual['physical_profile'], actual['profile'])
                self.assertIn('Revised traffic', actual['profile']['reference'])
                segment = next(row for row in expected['segments'] if row['kind'] == 'flat-high-departure')
                high = expected['points'][segment['start_index']:segment['end_index'] + 1]
                total = sum(math.dist(a[:2], b[:2]) for a, b in zip(expected['points'], expected['points'][1:]))
                high_length = sum(math.dist(a[:2], b[:2]) for a, b in zip(high, high[1:]))
                run = abs(verify._uv(high[-1])[0] - verify._uv(high[0])[0])
                radii = []
                for a, b, c in zip(high, high[1:], high[2:]):
                    twice_area = abs((b[0] - a[0]) * (c[1] - a[1])
                                     - (b[1] - a[1]) * (c[0] - a[0]))
                    if twice_area > 1e-10:
                        radii.append(math.dist(a[:2], b[:2]) * math.dist(b[:2], c[:2])
                                     * math.dist(c[:2], a[:2]) / (2. * twice_area))
                profile = actual['profile']
                self.assertAlmostEqual(profile['departure_station_u_m'], verify._uv(expected['native_high_port'])[0], places=10)
                self.assertAlmostEqual(profile['departure_plan_run_u_m'], run, places=10)
                self.assertAlmostEqual(profile['departure_length_plan_m'], high_length, places=10)
                self.assertAlmostEqual(profile['departure_minimum_sampled_radius_m'], min(radii), places=8)
                self.assertAlmostEqual(profile['length_total_plan_m'], total, places=10)
                # Updating the traffic measurements must not mutate the
                # retained model profile or the immutable source approval.
                profile['departure_station_u_m'] += 1.
                self.assertEqual(actual['physical_profile'], retained_profile)

    def test_retained_profile_comparison_allows_only_aggregate_length_roundoff(self):
        frozen = next(route['profile'] for route in verify.approved_candidate()['routes']
                      if route['id'] == 'upper-off')
        roundoff = deepcopy(frozen)
        roundoff['length_total_plan_m'] = math.nextafter(frozen['length_total_plan_m'], math.inf)
        self._assert_retained_physical_profile(roundoff, frozen)
        for drift in (-1e-8, 1e-8):
            with self.subTest(length_drift_m=drift):
                changed = deepcopy(frozen)
                changed['length_total_plan_m'] += drift
                with self.assertRaises(AssertionError):
                    self._assert_retained_physical_profile(changed, frozen)
        for field, value in (('parallel_offset_m', math.nextafter(frozen['parallel_offset_m'], math.inf)),
                             ('reference', 'Changed physical profile'), ('unexpected_field', True)):
            with self.subTest(changed_field=field):
                changed = {**frozen, field: value}
                with self.assertRaises(AssertionError):
                    self._assert_retained_physical_profile(changed, frozen)
        for field in ('length_total_plan_m', 'turn_radius_m'):
            with self.subTest(missing_field=field):
                changed = {key: value for key, value in frozen.items() if key != field}
                with self.assertRaises(AssertionError):
                    self._assert_retained_physical_profile(changed, frozen)

    def test_explicit_uniform_marker_rejects_unknown_and_mixed_revisions(self):
        manifest, scene, _ = fixture()
        pieces = {piece['id']: piece for piece in manifest['pieces']}
        self.assertIsNone(verify._assembly_highway_slip_profile(pieces, scene))
        first = manifest['pieces'][0]
        first['engineering']['highway_slip_profile'] = verify.HIGHWAY_SLIP_PROFILE
        with self.assertRaisesRegex(ValueError, 'consistent'):
            verify._assembly_highway_slip_profile(pieces, scene)
        for piece in pieces.values():
            piece['engineering']['highway_slip_profile'] = verify.HIGHWAY_SLIP_PROFILE
        self.assertEqual(verify._assembly_highway_slip_profile(pieces, scene), verify.HIGHWAY_SLIP_PROFILE)
        first['engineering']['highway_slip_profile'] = 'unknown'
        with self.assertRaisesRegex(ValueError, 'unknown'):
            verify._source_origin(first)
        with self.assertRaisesRegex(ValueError, 'Unknown'):
            verify.revised_routes('unknown')

    def test_encoded_full_graph_retains_all_native_services_in_four_rotations(self):
        manifest, scene, resources = fixture(verify.HIGHWAY_SLIP_PROFILE)
        result = verify.verify_assembly_resources(manifest, scene, resources, inspect_models=False)
        self.assertTrue(result['saved_path_checks_passed'])
        self.assertEqual(result['highway_slip_profile'], verify.HIGHWAY_SLIP_PROFILE)
        self.assertEqual(result['construction']['unique_owned_cells'], 31)
        self.assertEqual(result['paths']['external_native_channels'], 20)
        self.assertEqual(result['paths']['native_through_lane_and_sidewalk_journeys'], 10)
        self.assertEqual(result['paths']['right_turn_transfers'], 4)
        self.assertEqual(len(result['proper_rotation_paths']), 4)
        self.assertEqual(result['highway_slip_lanes']['status'], 'not-run')
        contracts = [verify.reviewed_contract(piece) for piece in manifest['pieces']]
        self.assertEqual(sum(len(row['ports']) for row in contracts), 180)
        self.assertEqual(sum(len(row['movements']) for row in contracts), 94)

    def test_marking_old_or_revised_real_encoded_paths_as_the_other_revision_fails(self):
        for profile in (None, verify.HIGHWAY_SLIP_PROFILE):
            manifest, _scene, resources = fixture(profile)
            piece = next(row for row in manifest['pieces'] if row['geometry_key'] == 'parallel-lower-exit-slip')
            with self.subTest(saved_profile=profile):
                verify.check_paths(resources[piece['id']], piece)
                piece['engineering']['highway_slip_profile'] = None if profile else verify.HIGHWAY_SLIP_PROFILE
                with self.assertRaisesRegex(ValueError, 'approved/native routes'):
                    verify.check_paths(resources[piece['id']], piece)

    def test_actual_saved_endpoint_wedge_keeps_finite_lateral_and_following_phase_tangent(self):
        # Numeric witness decoded from the first actual new native build.
        # At station 5.813617837633023, the nearest finite chord is 41,
        # while phase selection uses chord 42. Pairing chord 42's lateral
        # with its tangent incorrectly produced a 6.78068e-6 U error.
        face = {'texture': 0x5713000E, 'upward': True,
                'points': ((55.220731258392334, 55.14610004425049, 7.5),
                           (55.2262396812439, 55.076977252960205, 7.5),
                           (55.24186611175537, 55.09260368347168, 7.5)),
                'uv': ((.5160984396934509, .36335110664367676),
                       (.5167487859725952, .36396417021751404),
                       (.5162180066108704, .36335110664367676))}
        report = verify.check_wheeltrack_vertices([face], highway_slip_profile=verify.HIGHWAY_SLIP_PROFILE)
        self.assertEqual(report['mapped_native_dd_triangles_checked'], 1)
        self.assertLess(report['maximum_vertex_u_error'], 3e-8)
        self.assertEqual(report['vertex_uv_tolerance'], 5e-6)
        self.assertEqual(report['nearest_finite_segment_position_tie_radius_m'], math.sqrt(2.) * 4e-6)
        mutant = deepcopy(face)
        mutant['uv'] = ((face['uv'][0][0], face['uv'][0][1] + .01), *face['uv'][1:])
        with self.assertRaisesRegex(ValueError, 'approved native wear field'):
            verify.check_wheeltrack_vertices([mutant], highway_slip_profile=verify.HIGHWAY_SLIP_PROFILE)


class ActualSavedSlipProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        supplied = os.environ.get('SCP_TEST_PARALLEL_SLIP_BUILD')
        cls.build = Path(supplied).expanduser() if supplied else ROOT / 'dist/ddrhw-parallel-diamond-slip-lanes-02'
        if not cls.build.is_absolute():
            cls.build = ROOT / cls.build
        if not (cls.build / 'manifest.json').is_file():
            raise unittest.SkipTest('Saved revised parallel slip build is absent; set SCP_TEST_PARALLEL_SLIP_BUILD to its exact directory.')
        cls.manifest = json.loads((cls.build / 'manifest.json').read_text())
        cls.pieces = {piece['id']: piece for piece in cls.manifest['pieces']}
        if len(cls.pieces) != 15 or any(piece.get('engineering', {}).get('highway_slip_profile') != verify.HIGHWAY_SLIP_PROFILE for piece in cls.pieces.values()):
            raise ValueError('The saved build does not declare the complete revised highway-slip profile')
        cls.resources, cls.faces = {}, []
        for piece in cls.pieces.values():
            archive = strict_dbpf((cls.build / piece['asset_file']).read_bytes())
            cls.resources[piece['id']] = archive
            origin = verify._source_origin(piece)
            for cell, tile in zip(piece['cells'], piece['tile_ids']):
                cls.faces.extend(verify._decode_faces(archive[*S3D, int(tile, 16)], cell,
                    origin=(16. * origin[0], -16. * origin[1])))

    def test_all_actual_saved_path_fragments_match_the_explicit_revision(self):
        reports = [verify.check_paths(self.resources[piece['id']], piece) for piece in self.pieces.values()]
        self.assertEqual(sum(row['route_fragments_checked'] for row in reports), 126)

    def test_every_actual_parallel_lane_has_native_wear_on_its_saved_model(self):
        report = verify.check_highway_slip_lanes(self.faces, profile=verify.HIGHWAY_SLIP_PROFILE)
        self.assertTrue(report['passed'])
        self.assertEqual(report['actual_saved_parallel_wear_controls'], 20)

    def test_actual_saved_remap_retains_the_entire_formerly_missing_face_edge(self):
        first = (-44.61282467842102, -61.67807364463806, 15.)
        last = (-44.61281967163086, -61.678523778915405, 15.)
        faces = [face for face in self.faces if face['texture'] == 0x5713000E
                 and all(point[2] == 15. for point in face['points'])]
        precision = {'admitted_road_encoding_spans': 0,
                     'maximum_admitted_along_route_span_m': 0.,
                     'maximum_sampled_actual_face_distance_m': 0.}
        nearby = verify._FaceIndex(faces, size=.25).nearby(first, last, margin=2e-6)
        self.assertTrue(verify._continuous_support(first, last, nearby, precision))
        self.assertEqual(precision['admitted_road_encoding_spans'], 0)

    def test_a_real_encoded_parallel_lane_coordinate_mutation_is_rejected(self):
        piece = self.pieces['ddrhw-parallel-lower-exit-slip']
        archive = dict(self.resources[piece['id']])
        origin = verify._source_origin(piece)
        for cell, tile in zip(piece['cells'], piece['tile_ids']):
            key = *PATH, int(tile, 16)
            for route in parse_paths(archive[key])['routes']:
                for point in route['points'][1:-1]:
                    world = point[0] + 16. * (cell[0] + origin[0]), point[1] - 16. * (cell[1] + origin[1]), point[2]
                    if abs(world[2] - 7.5) > 1e-8 or abs(verify._uv(world)[1] - 5.5) > 1e-8:
                        continue
                    lines = archive[key].decode().splitlines()
                    at = next(i for i, line in enumerate(lines) if ',' in line and tuple(map(float, line.split(','))) == tuple(point))
                    lines[at] = ','.join(f'{value:.9f}' for value in (point[0] + .125, point[1], point[2]))
                    archive[key] = ('\r\n'.join(lines) + '\r\n').encode()
                    with self.assertRaisesRegex(ValueError, 'approved/native routes'):
                        verify.check_paths(archive, piece)
                    return
        self.fail('The mutation did not find an actual saved parallel PATH sample')

    def test_a_real_saved_road_texture_phase_reset_is_rejected(self):
        piece = self.pieces['ddrhw-parallel-lower-exit-slip']
        origin = verify._source_origin(piece)
        for cell, tile in zip(piece['cells'], piece['tile_ids']):
            model = parse_s3d(self.resources[piece['id']][*S3D, int(tile, 16)])
            for mesh in model['meshes']:
                vi, ii, pi, mi = mesh['frames'][0]
                if model['materials'][mi]['textures'] != [0x5713000E]:
                    continue
                vertices = positions(model['vertices'][vi]); block = model['vertices'][vi]
                for _kind, first, count in model['primitives'][pi]:
                    indices = model['indices'][ii]['values']
                    for at in range(first, first + count, 3):
                        selected = indices[at:at + 3]
                        uv = [struct.unpack_from('<2f', block['data'], index * block['stride'] + 12) for index in selected]
                        if not all(65.5 / 128. <= u <= 95.5 / 128. for u, _v in uv):
                            continue
                        points = [vertices[index] for index in selected]
                        if not all(abs(point[1] - 7.5) < 1e-8 for point in points):
                            continue
                        a, b, c = points
                        if ((b[0] - a[0]) * (c[2] - a[2])
                                - (b[2] - a[2]) * (c[0] - a[0])) >= -1e-12:
                            continue
                        data = bytearray(block['data']); offset = selected[0] * block['stride'] + 16
                        struct.pack_into('<f', data, offset, struct.unpack_from('<f', data, offset)[0] + .02)
                        block['data'] = bytes(data)
                        faces = verify._decode_faces(pack_s3d(model), cell,
                            origin=(16. * origin[0], -16. * origin[1]))
                        with self.assertRaisesRegex(ValueError, 'approved native wear field'):
                            verify.check_wheeltrack_vertices(faces, highway_slip_profile=verify.HIGHWAY_SLIP_PROFILE)
                        return
        self.fail('The mutation did not find a real encoded shoulder-wear triangle')


if __name__ == '__main__':
    unittest.main()
