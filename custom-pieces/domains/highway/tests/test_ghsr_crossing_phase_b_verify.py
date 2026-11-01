"""Independent alignment-B fixtures and mutations, plus pinned native checks."""
from copy import deepcopy
import hashlib
import math
from pathlib import Path
import struct
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp import jsonc
from scp.connectivity import piece_connectivity
from scp.dbpf import decompress, entries
from scp.models import pack_s3d, parse_s3d
from scp.paths import local_settings
from scp.recipes import combine_meshes
from scp.track_paths import PATH, S3D
from scp_highway import ghsr_crossing_verify as verify


def specification(alignment='B'):
    if alignment == 'A':
        return {'id': verify.PIECE_ID, 'domain': 'highway', 'recipe': verify.RECIPE,
                'footprint': [1, 2], 'cells': [[0, 0], [0, 1]],
                'tile_ids': ['7f500000', '7f500100'], 'preview_id': '7f50fff0'}
    return {'id': verify.PIECE_ID_B, 'domain': 'highway', 'recipe': verify.RECIPE_B,
            'footprint': [2, 1], 'cells': [[0, 0], [1, 0]],
            'tile_ids': ['7f510000', '7f510100'], 'preview_id': '7f51fff0'}


def route(transport, lane, entry, exit_, *points):
    return {'transport': transport, 'lane': lane, 'entry': entry, 'exit': exit_,
            'compatibility': 0, 'points': list(points)}


def fixture_routes():
    """Literal independent PATH fixture; does not call the writer or verifier."""
    return [
        [route(1, 0, 2, 3, (8., 3.2, 15.), (-3.2, -8., 15.)),
         route(1, 1, 2, 3, (8., -3.2, 15.), (3.2, -8., 15.)),
         route(1, 1, 3, 2, (-3.2, -8., 7.5), (8., 3.2, 7.5)),
         route(1, 0, 3, 2, (3.2, -8., 7.5), (8., -3.2, 7.5)),
         route(7, 0, 2, 1, (8., 2.9, 1.), (7.29289321881, 3.60710678119, 1.),
               (5.02132034356, 5.87867965644, 1.), (2.9, 8., 1.)),
         route(7, 0, 1, 2, (-2.8, 8., 1.), (-.65818525421, 5.899373999323, 1.),
               (7.29289321881, -2.19289321881, 1.), (8., -2.9, 1.))],
        [route(1, 0, 1, 0, (-3.2, 8., 15.), (-8., 3.2, 15.)),
         route(1, 1, 1, 0, (3.2, 8., 15.), (-8., -3.2, 15.)),
         route(1, 1, 0, 1, (-8., -3.2, 7.5), (3.2, 8., 7.5)),
         route(1, 0, 0, 1, (-8., 3.2, 7.5), (-3.2, 8., 7.5)),
         route(7, 0, 0, 3, (-8., -2.9, 1.), (-7.29289321881, -3.60710678119, 1.),
               (-5.02132034356, -5.87867965644, 1.), (-2.9, -8., 1.)),
         route(7, 0, 3, 0, (2.8, -8., 1.), (.65818525421, -5.899373999323, 1.),
               (-7.29289321881, 2.19289321881, 1.), (-8., 2.9, 1.))],
    ]


def encode(routes, elevation=1):
    lines = ['SC4PATHS', '1.2', str(len(routes)), '0', str(elevation)]
    for item in routes:
        lines += [str(item[key]) for key in ('transport', 'lane', 'entry', 'exit', 'compatibility')]
        lines += [str(len(item['points']))]
        lines += [','.join(format(value, '.12g') for value in point) for point in item['points']]
    return ('\r\n'.join(lines) + '\r\n').encode('ascii')


def path_resources(routes=None):
    return {(*PATH, int(tile, 16)): encode(records)
            for tile, records in zip(specification()['tile_ids'], routes or fixture_routes())}


def construction_fields(helpers=False):
    fields = {'CellLayout': ['ab<', '...', '^..'], 'ConsLayout': ['++<', '...', '^..'],
              'CheckType': ['a - dirtroad: 0x03010000 monorail: 0x00030100',
                            'b - dirtroad: 0x00000301 monorail: 0x01000003'], 'Costs': ['1000']}
    if helpers:
        fields['CellLayout'] = ['ji.', 'ab<', 'hk.', '^..']
        fields['ConsLayout'] = ['...', '++<', '...', '^..']
        fields['CheckType'] += [
            'h - monorail: 0x04000100 dirtroad: 0x00000301, 0xFFFFFFFF optional',
            'i - monorail: 0x04000100 dirtroad: 0x03010000, 0xFFFFFFFF optional',
            'j - rail: 0x00000101 monorail: 0x01000003, 0xFFFFFFFF optional',
            'k - rail: 0x01010000 monorail: 0x00030100, 0xFFFFFFFF optional']
    return fields


class GHSRAlignmentBPortableTests(unittest.TestCase):
    def test_literal_b_fixture_has_six_journeys_twelve_complete_boundaries_and_four_rotations(self):
        report = verify.check_paths(path_resources(), specification())
        self.assertEqual(report['complete_directed_journeys'], 6)
        self.assertEqual(report['complete_native_boundary_members_checked'], 12)
        self.assertEqual(report['proper_rotations_checked'], 4)
        self.assertEqual(report['native_core_rail_exterior_endpoint_correction_m'], .1)
        self.assertEqual(report['railway_internal_endpoint_correction_m'], 0.)
        self.assertFalse(report['game_operation_tested'])

    def test_rotating_a_cannot_replace_b_while_retaining_deck_directions(self):
        for turns in range(4):
            with self.subTest(turns=turns):
                records = deepcopy(verify.expected_paths())
                for routes in records:
                    for item in routes:
                        item['entry'] = (item['entry'] + turns) % 4
                        item['exit'] = (item['exit'] + turns) % 4
                        item['points'] = [verify._point(point, rotation=turns) for point in item['points']]
                with self.assertRaisesRegex(ValueError, 'independent lane, height, and collar'):
                    verify.check_paths(path_resources(records), specification())

    def test_missing_phase_is_rejected_by_alignment_coverage(self):
        a = specification('A')
        with self.assertRaisesRegex(ValueError, 'Both distinct alignment A and alignment B'):
            verify.check_alignment_coverage({}, a, {}, a)

    def test_two_classes_cover_adjacent_diagonal_rail_grids_without_reversing_highway(self):
        a = specification('A')
        resources_a = {(*PATH, int(tile, 16)): encode(records)
                       for tile, records in zip(a['tile_ids'], verify.expected_paths())}
        report = verify.check_alignment_coverage(resources_a, a, path_resources(), specification())
        self.assertEqual(report['alignment_classes_checked'], 2)
        self.assertEqual(report['crossing_centres_east_north_m'], [[0., -8.], [8., 0.]])
        self.assertAlmostEqual(report['adjacent_diagonal_railway_spacing_m'], 16. / math.sqrt(2.))
        self.assertTrue(report['both_highway_deck_directions_preserved'])
        self.assertFalse(report['game_alignment_tested'])

    def test_reversed_deck_directions_are_rejected_even_with_unchanged_physical_road(self):
        records = fixture_routes()
        for routes in records:
            for item in routes[:4]:
                item['entry'], item['exit'] = item['exit'], item['entry']
                item['points'].reverse()
        with self.assertRaisesRegex(ValueError, 'independent lane, height, and collar'):
            verify.check_paths(path_resources(records), specification())

    def test_raw_native_core_exteriors_leave_point_one_metre_gaps_and_fail(self):
        for tile, route_no, endpoint, original in ((0, 4, -1, (2.8, 8., 1.)),
                                                  (0, 5, 0, (-2.9, 8., 1.)),
                                                  (1, 4, -1, (-2.8, -8., 1.)),
                                                  (1, 5, 0, (2.9, -8., 1.))):
            with self.subTest(tile=tile, route=route_no):
                records = fixture_routes()
                records[tile][route_no]['points'][endpoint] = original
                with self.assertRaisesRegex(ValueError, 'independent lane, height, and collar'):
                    verify.check_paths(path_resources(records), specification())

    def test_internal_join_gap_and_tangent_kink_fail_independently(self):
        records = fixture_routes()
        records[0][4]['points'][0] = (8., 2.8, 1.)
        with self.assertRaisesRegex(ValueError, 'complete internal lane|route stops|Ambiguous'):
            verify._graph(records, cells=verify.CELLS_B)
        records = fixture_routes()
        x, n, h = records[0][4]['points'][1]
        records[0][4]['points'][1] = (x + .03, n, h)
        with self.assertRaisesRegex(ValueError, 'internal seam.*heading'):
            verify._graph(records, cells=verify.CELLS_B)

    def test_native_helper_endpoint_and_tangent_both_matter(self):
        records = fixture_routes()
        x, n, h = records[0][5]['points'][1]
        records[0][5]['points'][1] = (x + .03, n, h)
        with self.assertRaisesRegex(ValueError, 'exterior collar tangent'):
            verify._check_helpers(records, specification())
        helpers = verify._native_helpers(specification())
        helpers[2] = ((-1, 0), helpers[2][1])
        with patch.object(verify, '_native_helpers', return_value=helpers):
            with self.assertRaisesRegex(ValueError, 'No unique complete directed'):
                verify._check_helpers(fixture_routes(), specification())

    def test_missing_lane_capacity_path_height_or_transfer_cannot_pass(self):
        mutations = ('missing', 'extra', 'height', 'mode', 'transfer')
        for mutation in mutations:
            with self.subTest(mutation=mutation):
                records = fixture_routes()
                if mutation == 'missing':
                    records[1].pop(0)
                elif mutation == 'extra':
                    records[0].append(route(1, 0, 0, 3, (-7., -7.1, 0.), (-7.1, -7., 0.)))
                elif mutation == 'height':
                    records[0][4]['points'] = [(x, n, 0.) for x, n, h in records[0][4]['points']]
                elif mutation == 'mode':
                    records[0][4]['transport'] = 1
                else:
                    records[0][0]['points'][-1] = records[0][4]['points'][-1]
                with self.assertRaisesRegex(ValueError, 'independent lane, height, and collar'):
                    verify.check_paths(path_resources(records), specification())

    def test_use_elevation_header_cannot_be_disabled(self):
        resources = path_resources()
        resources[*PATH, 0x7F510000] = encode(fixture_routes()[0], elevation=0)
        with self.assertRaisesRegex(ValueError, 'UseElevation=1'):
            verify.check_paths(resources, specification())

    def test_reviewed_facts_classify_both_rail_tracks_and_thirty_forbidden_transfers(self):
        facts = verify.reviewed_facts(specification())
        self.assertEqual(facts['cells'], [[0, 0], [1, 0]])
        self.assertEqual(facts['reference_piece_id'], specification()['id'])
        self.assertEqual(len(facts['ports']), 12)
        self.assertEqual(len(facts['movements']), 6)
        self.assertEqual(len(facts['forbidden_transfers']), 30)
        self.assertEqual(sum(port['engine_transport'] == 7 for port in facts['ports']), 4)

    def test_reviewed_connectors_match_actual_shared_saved_path_extraction(self):
        def classify(_piece, engine, height):
            return {'service_network': 'ghsr' if engine == 7 else 'road',
                    'service_family': 'high-speed-rail' if engine == 7 else 'road',
                    'variant': 'ghsr' if engine == 7 else 'dd-rhw-l2' if height == 15 else 'dd-rhw-l1',
                    'role': 'primary', 'channel_kind': 'rail-track' if engine == 7 else 'road-lane',
                    'traffic_modes': ['monorail'] if engine == 7 else ['car']}
        actual = piece_connectivity(specification(), path_resources(),
            contract=verify.reviewed_contract(specification()), service_classifier=classify)
        ports = {port['id']: port for port in actual['ports']}
        for expected in verify.reviewed_facts(specification())['ports']:
            self.assertLessEqual(math.dist(ports[expected['id']]['sampled_tangent'], expected['sampled_tangent']), 1e-9)
        self.assertEqual(len(actual['journeys']), 6)

    def test_horizontal_core_and_top_bottom_native_helpers_are_exact(self):
        report = verify.check_construction_fields(specification(), construction_fields())
        self.assertEqual(report['owned_tiles'], 2)
        piece = {**specification(), 'native_ghsr_approaches': True}
        report = verify.check_construction_fields(piece, construction_fields(helpers=True))
        self.assertEqual(report['native_helper_check_flags_verified'], 4)
        self.assertFalse(report['game_construction_tested'])

    def test_wrong_a_ownership_core_flags_helper_phase_or_owned_helpers_fail(self):
        piece = {**specification(), 'native_ghsr_approaches': True}
        for mutation in ('ownership', 'coreflags', 'helpercell', 'helperpose', 'ownedhelper'):
            with self.subTest(mutation=mutation):
                fields = construction_fields(helpers=True)
                changed_piece = dict(piece)
                if mutation == 'ownership':
                    changed_piece.update(footprint=[1, 2], cells=[[0, 0], [0, 1]])
                elif mutation == 'coreflags':
                    fields['CheckType'][0] = fields['CheckType'][0].replace('0x00030100', '0x01000003')
                elif mutation == 'helpercell':
                    fields['CellLayout'][0] = 'ij.'
                elif mutation == 'helperpose':
                    fields['CheckType'][4] = fields['CheckType'][4].replace('0x00000101', '0x01010000')
                else:
                    fields['ConsLayout'][0] = '+..'
                with self.assertRaises(ValueError):
                    verify.check_construction_fields(changed_piece, fields)


class GHSRAlignmentBNativeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        settings = local_settings(ROOT)
        if not settings.is_file():
            raise unittest.SkipTest('Private NAM settings are unavailable')
        plugins = Path(jsonc.load(settings)['plugins'])
        cls.context = {}
        for label, filename, fingerprint in (
            ('dd_rhw', 'RealHighway_DD_RHW-4.dat', 'ccf8dabd3930fce92d0baa872ff974e3a536ddcc40762505a2e70eafcf9c0dfb'),
            ('hsr', 'High Speed Rail.dat', 'e72def6bf460ed1f9f6969e68b146bfc046e3f05a34ede522d94d69da5c5473a')):
            found = list(plugins.rglob(filename)) if plugins.is_dir() else []
            if not found:
                raise unittest.SkipTest('Original NAM DD and GHSR archives are unavailable')
            if len(found) != 1:
                raise ValueError('Ambiguous original NAM input')
            raw = found[0].read_bytes()
            if hashlib.sha256(raw).hexdigest() != fingerprint:
                raise ValueError('Original NAM input changed; re-audit rather than skip')
            cls.context[label] = {key: decompress(value) for key, value in entries(raw).items()}
        # The writer is used only to produce the candidate under test. All
        # verifier expectations and portable saved fixtures above are independent.
        from scp_highway.ghsr_crossing import build_alignment_b_channels
        cls.resources = {}
        preview = []
        for tile, (cell, raw_model, raw_path) in zip(specification()['tile_ids'],
                                                  build_alignment_b_channels(cls.context)):
            for zoom in range(5):
                cls.resources[*S3D, int(tile, 16) + zoom] = raw_model
            cls.resources[*PATH, int(tile, 16)] = raw_path
            model = parse_s3d(raw_model)
            preview.append((model, model['meshes'], (16. * cell[0], 0., 16. * cell[1])))
        cls.resources[*S3D, int(specification()['preview_id'], 16)] = pack_s3d(combine_meshes(preview))

    def test_actual_b_candidate_matches_independent_native_streams_corridor_and_saved_paths(self):
        self.assertEqual(verify.native_mesh_measurements(self.context, specification()),
                         (verify.EXPECTED_MESHES_B, verify.EXPECTED_ANIMATION, verify.EXPECTED_TRAILING))
        self.assertEqual(verify.check_paths(self.resources, specification())['complete_directed_journeys'], 6)
        report = verify.check_models(self.resources, specification(), self.context)
        self.assertEqual(report['minimum_train_roof_clearance_m'], .5)
        self.assertGreater(report['rail_bed_corridor_samples'], 150)
        self.assertTrue(report['preview_matches_all_cells'])
        self.assertFalse(report['game_rendering_tested'])

    def test_path_byte_pins_follow_literal_helper_corrected_expectation(self):
        for cell, fingerprint in verify.reviewed_facts(specification())['path_hashes_by_cell']:
            tile = int(specification()['tile_ids'][specification()['cells'].index(cell)], 16)
            self.assertEqual(hashlib.sha256(self.resources[*PATH, tile]).hexdigest(), fingerprint)

    def test_wrong_a_rail_pose_fails_even_when_highway_meshes_are_identical(self):
        from scp_highway.ghsr_crossing import build_channels
        resources = dict(self.resources)
        for tile, (_, raw_model, _) in zip(specification()['tile_ids'], build_channels(self.context)):
            for zoom in range(5):
                resources[*S3D, int(tile, 16) + zoom] = raw_model
        with self.assertRaisesRegex(ValueError, 'native mesh positions, attributes'):
            verify.check_models(resources, specification())

    def test_small_vertex_or_uv_change_fails_the_native_signature(self):
        for offset in (0, 12):
            with self.subTest(attribute_offset=offset):
                resources = dict(self.resources)
                model = parse_s3d(resources[*S3D, 0x7F510000])
                data = bytearray(model['vertices'][6]['data'])
                struct.pack_into('<f', data, offset, struct.unpack_from('<f', data, offset)[0] + .01)
                model['vertices'][6]['data'] = bytes(data)
                resources[*S3D, 0x7F510000] = pack_s3d(model)
                with self.assertRaisesRegex(ValueError, 'native mesh positions, attributes'):
                    verify.check_models(resources, specification())

    def test_preview_must_place_second_tile_east_not_south(self):
        resources = dict(self.resources)
        first = parse_s3d(resources[*S3D, 0x7F510000])
        second = parse_s3d(resources[*S3D, 0x7F510100])
        resources[*S3D, 0x7F51FFF0] = pack_s3d(combine_meshes([
            (first, first['meshes'], (0., 0., 0.)), (second, second['meshes'], (0., 0., 16.))]))
        with self.assertRaisesRegex(ValueError, 'preview does not contain'):
            verify.check_models(resources, specification())


if __name__ == '__main__':
    unittest.main()
