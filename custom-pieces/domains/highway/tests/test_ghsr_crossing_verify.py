"""Independent crossing mutation controls, plus optional original-NAM checks."""
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
from scp.dbpf import decompress, entries, pack_dbpf
from scp.models import pack_s3d, parse_s3d
from scp.paths import local_settings
from scp.recipes import combine_meshes
from scp.track_paths import S3D, PATH
from scp.verify import parse_paths
from scp_highway import ghsr_crossing_verify as verify


def specification():
    return {'id': 'ddrhw-l1-and-l2-over-ghsr-ground-mixed-crossing-diagonal-90deg',
            'name': 'Diagonal DD/GHSR crossing', 'domain': 'highway',
            'recipe': 'highway_ddrhw_diagonal_ghsr_crossing', 'footprint': [1, 2],
            'cells': [[0, 0], [0, 1]], 'tile_ids': ['7f500000', '7f500100'],
            'preview_id': '7f50fff0'}


def fixture_routes():
    """Explicit saved fixture, not a call into either writer or verifier."""
    def route(transport, lane, entry, exit_, *points):
        return {'transport': transport, 'lane': lane, 'entry': entry, 'exit': exit_,
                'compatibility': 0, 'points': list(points)}
    return [
        [route(1, 0, 2, 3, (8., 3.2, 15.), (-3.2, -8., 15.)),
         route(1, 1, 2, 3, (8., -3.2, 15.), (3.2, -8., 15.)),
         route(1, 1, 3, 2, (-3.2, -8., 7.5), (8., 3.2, 7.5)),
         route(1, 0, 3, 2, (3.2, -8., 7.5), (8., -3.2, 7.5)),
         route(7, 0, 0, 3, (-8., -2.9, 1.), (-5.87867965644, -5.02132034356, 1.),
               (-3.60710678119, -7.29289321881, 1.), (-2.9, -8., 1.)),
         route(7, 0, 3, 0, (2.9, -8., 1.), (2.19289321881, -7.29289321881, 1.),
               (-5.85818525421, .799373999323, 1.), (-8., 2.9, 1.))],
        [route(1, 0, 1, 0, (-3.2, 8., 15.), (-8., 3.2, 15.)),
         route(1, 1, 1, 0, (3.2, 8., 15.), (-8., -3.2, 15.)),
         route(1, 1, 0, 1, (-8., -3.2, 7.5), (3.2, 8., 7.5)),
         route(1, 0, 0, 1, (-8., 3.2, 7.5), (-3.2, 8., 7.5)),
         route(7, 0, 2, 1, (8., 2.9, 1.), (5.87867965644, 5.02132034356, 1.),
               (3.60710678119, 7.29289321881, 1.), (2.9, 8., 1.)),
         route(7, 0, 1, 2, (-2.9, 8., 1.), (-2.19289321881, 7.29289321881, 1.),
               (5.85818525421, -.799373999323, 1.), (8., -2.9, 1.))],
    ]


def encode(routes, elevation=1):
    lines = ['SC4PATHS', '1.2', str(len(routes)), '0', str(elevation)]
    for route in routes:
        lines += [str(route[key]) for key in ('transport', 'lane', 'entry', 'exit', 'compatibility')]
        lines.append(str(len(route['points'])))
        lines += [','.join(format(value, '.12g') for value in point) for point in route['points']]
    return ('\r\n'.join(lines) + '\r\n').encode('ascii')


def path_resources(routes=None):
    return {(*PATH, int(tile, 16)): encode(records)
            for tile, records in zip(specification()['tile_ids'], routes or fixture_routes())}


def construction_fields():
    return {'CellLayout': ['a.<', 'b..', '^..'], 'ConsLayout': ['+.<', '+..', '^..'],
            'CheckType': ['a - dirtroad: 0x03010000 monorail: 0x01000003',
                          'b - dirtroad: 0x00000301 monorail: 0x00030100'], 'Costs': ['1000']}


class GHSRCrossingPortableTests(unittest.TestCase):
    def test_independent_saved_fixture_has_all_lanes_and_four_rotations(self):
        report = verify.check_paths(path_resources(), specification())
        self.assertEqual(report['complete_directed_journeys'], 6)
        self.assertEqual(report['complete_native_boundary_members_checked'], 12)
        self.assertEqual(report['route_fragments_consumed'], 12)
        self.assertEqual(report['proper_rotations_checked'], 4)
        self.assertTrue(report['internal_seam_tangents_verified'])
        self.assertFalse(report['game_operation_tested'])

    def test_removed_lane_cannot_hide_behind_remaining_highway_and_rail_paths(self):
        routes = fixture_routes()
        routes[0].pop(1)
        with self.assertRaisesRegex(ValueError, 'independent lane, height, and collar contract'):
            verify.check_paths(path_resources(routes), specification())

    def test_path_header_must_explicitly_retain_elevation(self):
        resources = path_resources()
        resources[*PATH, 0x7F500000] = encode(fixture_routes()[0], elevation=0)
        with self.assertRaisesRegex(ValueError, 'UseElevation=1'):
            verify.check_paths(resources, specification())

    def test_each_transport_height_lane_direction_and_junction_bit_is_bound(self):
        mutations = [('transport', 3), ('lane', 1), ('entry', 2), ('exit', 2), ('compatibility', 1)]
        for field, value in mutations:
            with self.subTest(field=field):
                routes = fixture_routes()
                routes[0][4][field] = value
                with self.assertRaisesRegex(ValueError, 'independent lane, height, and collar contract'):
                    verify.check_paths(path_resources(routes), specification())
        routes = fixture_routes()
        routes[1][0]['points'] = [(x, n, 7.5) for x, n, _ in routes[1][0]['points']]
        with self.assertRaisesRegex(ValueError, 'independent lane, height, and collar contract'):
            verify.check_paths(path_resources(routes), specification())

    def test_restored_native_point_one_metre_gap_is_rejected(self):
        routes = fixture_routes()
        routes[0][4]['points'][-1] = (-2.8, -8., 1.)
        with self.assertRaisesRegex(ValueError, 'independent lane, height, and collar contract'):
            verify.check_paths(path_resources(routes), specification())

    def test_wrong_or_removed_exterior_and_internal_collars_fail(self):
        for node in (1, 2):
            with self.subTest(node=node):
                routes = fixture_routes()
                x, n, h = routes[0][4]['points'][node]
                routes[0][4]['points'][node] = (x + .02, n, h)
                with self.assertRaisesRegex(ValueError, 'independent lane, height, and collar contract'):
                    verify.check_paths(path_resources(routes), specification())
        routes = fixture_routes()
        del routes[1][5]['points'][1]
        with self.assertRaisesRegex(ValueError, 'independent lane, height, and collar contract'):
            verify.check_paths(path_resources(routes), specification())

    def test_added_capacity_only_ground_route_is_not_a_connection(self):
        routes = fixture_routes()
        routes[0].append({'transport': 1, 'lane': 0, 'entry': 0, 'exit': 3,
                          'compatibility': 0, 'points': [(-7., -7.1, 0.), (-7.1, -7., 0.)]})
        with self.assertRaisesRegex(ValueError, 'independent lane, height, and collar contract'):
            verify.check_paths(path_resources(routes), specification())

    def test_internal_heading_is_checked_independently_of_external_endpoint_graph(self):
        routes = fixture_routes()
        x, n, h = routes[0][4]['points'][-2]
        routes[0][4]['points'][-2] = (x + .03, n, h)
        with self.assertRaisesRegex(ValueError, 'internal seam.*heading'):
            verify._graph(routes)

    def test_native_helper_tangents_are_checked_beyond_endpoint_matches(self):
        routes = fixture_routes()
        x, n, h = routes[1][5]['points'][-2]
        routes[1][5]['points'][-2] = (x, n + .03, h)
        with self.assertRaisesRegex(ValueError, 'exterior collar tangent'):
            verify._check_helpers(routes)

    def test_wrong_west_dd_phase_is_not_accepted_as_a_full_directed_boundary(self):
        helpers = verify._native_helpers()
        for route in helpers[1][1]:
            route['points'] = [(x, n, 7.5 if h == 15. else 15.) for x, n, h in route['points']]
        with patch.object(verify, '_native_helpers', return_value=helpers):
            with self.assertRaisesRegex(ValueError, 'exterior collar tangent|No unique complete directed'):
                verify._check_helpers(fixture_routes())

    def test_reference_classifies_both_rail_directions_and_forbids_transfers(self):
        facts = verify.reviewed_facts(specification())
        self.assertEqual(len(facts['ports']), 12)
        self.assertEqual(len(facts['movements']), 6)
        self.assertEqual(len(facts['forbidden_transfers']), 30)
        rail = [p for p in facts['ports'] if p['engine_transport'] == 7]
        self.assertEqual(len(rail), 4)
        self.assertTrue(all(p['service_network'] == 'ghsr' and p['channel_kind'] == 'rail-track' for p in rail))

    def test_reviewed_ports_match_shared_extractor_first_and_last_saved_chords(self):
        facts = verify.reviewed_facts(specification())
        def classify(_piece, engine, height):
            return {'service_network': 'ghsr' if engine == 7 else 'road',
                    'service_family': 'high-speed-rail' if engine == 7 else 'road',
                    'variant': 'ghsr' if engine == 7 else 'dd-rhw-l2' if height == 15 else 'dd-rhw-l1',
                    'role': 'primary', 'channel_kind': 'rail-track' if engine == 7 else 'road-lane',
                    'traffic_modes': ['monorail'] if engine == 7 else ['car']}
        actual = piece_connectivity(specification(), path_resources(),
                                    contract=verify.reviewed_contract(specification()), service_classifier=classify)
        ports = {p['id']: p for p in actual['ports']}
        for expected in facts['ports']:
            port = ports[expected['id']]
            self.assertLessEqual(math.dist(port['sampled_tangent'], expected['sampled_tangent']), 1e-9)
            self.assertLessEqual(math.dist(port['tangent'], expected['tangent']), 1e-9)
        self.assertEqual({(j['entry_port'], j['exit_port']) for j in actual['journeys']}, set(facts['movements']))

    def test_core_construction_binds_two_cells_flags_anchors_and_cost(self):
        self.assertEqual(verify.check_construction_fields(specification(), construction_fields())['owned_tiles'], 2)
        for name, value in [('CheckType', ['a - dirtroad: 0x03010000 monorail: 0x00030100',
                                           construction_fields()['CheckType'][1]]),
                            ('CellLayout', ['a.<', '.b.', '^..']),
                            ('ConsLayout', ['+.<', '++.', '^..']), ('Costs', ['10'])]:
            with self.subTest(field=name):
                fields = construction_fields()
                fields[name] = value
                with self.assertRaises(ValueError):
                    verify.check_construction_fields(specification(), fields)

    def test_construction_cannot_add_a_second_definition_of_an_owned_network(self):
        fields = construction_fields()
        fields['CheckType'].append('a - dirtroad: 0x02000200')
        with self.assertRaisesRegex(ValueError, 'static network flags'):
            verify.check_construction_fields(specification(), fields)

    def test_all_four_rul0_helpers_bind_literal_flags_masks_and_unowned_cells(self):
        piece = {**specification(), 'native_ghsr_approaches': True}
        fields = construction_fields()
        fields['CellLayout'] = ['jah<', 'ibk.', '.^..']
        fields['ConsLayout'] = ['.+.<', '.+..', '.^..']
        fields['CheckType'] += [
            'h - monorail: 0x04000100 dirtroad: 0x00000301, 0xFFFFFFFF optional',
            'i - monorail: 0x04000100 dirtroad: 0x03010000, 0xFFFFFFFF optional',
            'j - rail: 0x01010000 monorail: 0x00030100, 0xFFFFFFFF optional',
            'k - rail: 0x00000101 monorail: 0x01000003, 0xFFFFFFFF optional']
        self.assertEqual(verify.check_construction_fields(piece, fields)['native_helper_check_flags_verified'], 4)
        for row in range(2, 6):
            for mutation in ('marker', 'mask', 'optional'):
                with self.subTest(row=row, mutation=mutation):
                    changed = deepcopy(fields)
                    text = changed['CheckType'][row]
                    if mutation == 'marker':
                        text = text.replace('0x04000100', '0x01000400') if row < 4 else text.replace('rail:', 'road:', 1)
                    elif mutation == 'mask':
                        text = text.replace('0xFFFFFFFF', '0x0000FFFF')
                    else:
                        text = text.replace(' optional', '')
                    changed['CheckType'][row] = text
                    with self.assertRaisesRegex(ValueError, 'native helper flags'):
                        verify.check_construction_fields(piece, changed)
        changed = deepcopy(fields)
        changed['CellLayout'][0] = 'haj<'
        with self.assertRaisesRegex(ValueError, 'native helper flags'):
            verify.check_construction_fields(piece, changed)
        changed = deepcopy(fields)
        changed['ConsLayout'][1] = '++..'
        with self.assertRaisesRegex(ValueError, 'helpers must not become owned'):
            verify.check_construction_fields(piece, changed)

    def test_changed_ownership_cannot_pass_using_matching_resource_ids(self):
        piece = specification()
        piece['footprint'] = [2, 2]
        with self.assertRaisesRegex(ValueError, 'two vertically adjacent'):
            verify.check_paths(path_resources(), piece)


class GHSRCrossingNativeTests(unittest.TestCase):
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
            matches = list(plugins.rglob(filename)) if plugins.is_dir() else []
            if not matches:
                raise unittest.SkipTest('Original NAM DD and GHSR archives are unavailable')
            if len(matches) != 1:
                raise ValueError('Ambiguous original NAM input')
            raw = matches[0].read_bytes()
            if hashlib.sha256(raw).hexdigest() != fingerprint:
                raise ValueError('Original NAM input changed; re-audit rather than skip')
            cls.context[label] = {key: decompress(value) for key, value in entries(raw).items()}
        from scp_highway.ghsr_crossing import build_channels
        resources, preview = {}, []
        for tile, (cell, model_raw, path_raw) in zip(specification()['tile_ids'], build_channels(cls.context)):
            for zoom in range(5):
                resources[*S3D, int(tile, 16) + zoom] = model_raw
            resources[*PATH, int(tile, 16)] = path_raw
            model = parse_s3d(model_raw)
            preview.append((model, model['meshes'], (cell[0] * 16., 0., cell[1] * 16.)))
        resources[*S3D, int(specification()['preview_id'], 16)] = pack_s3d(combine_meshes(preview))
        cls.resources = {key: decompress(raw) for key, raw in entries(pack_dbpf(resources)).items()}

    def test_actual_saved_model_zooms_preview_paths_and_train_clearance(self):
        self.assertEqual(verify.check_paths(self.resources, specification())['ghsr_journeys'], 2)
        report = verify.check_models(self.resources, specification(), self.context)
        self.assertEqual(report['model_resources_checked'], 11)
        self.assertEqual(report['minimum_train_roof_clearance_m'], .5)
        self.assertGreater(report['rail_bed_corridor_samples'], 150)
        self.assertTrue(report['native_overhang_preserved'])
        self.assertFalse(report['game_rendering_tested'])

    def mutation(self, function, tile=0x7F500000, zoom=0):
        resources = dict(self.resources)
        model = parse_s3d(resources[*S3D, tile + zoom])
        function(model)
        resources[*S3D, tile + zoom] = pack_s3d(model)
        return resources

    def test_a_shifted_native_vertex_fails_the_independent_semantic_pin(self):
        def mutate(model):
            block = model['vertices'][0]
            raw = bytearray(block['data'])
            struct.pack_into('<f', raw, 0, struct.unpack_from('<f', raw)[0] + .01)
            block['data'] = bytes(raw)
        with self.assertRaisesRegex(ValueError, 'native mesh positions, attributes'):
            verify.check_models(self.mutation(mutate), specification())

    def test_a_changed_uv_or_material_cannot_pass_just_matching_geometry_bounds(self):
        def uv(model):
            raw = bytearray(model['vertices'][0]['data'])
            struct.pack_into('<f', raw, 12, struct.unpack_from('<f', raw, 12)[0] + .1)
            model['vertices'][0]['data'] = bytes(raw)
        def material(model):
            raw = bytearray(model['materials'][0]['raw'])
            raw[0] ^= 0x10
            model['materials'][0]['raw'] = bytes(raw)
        for change in (uv, material):
            with self.subTest(change=change.__name__):
                with self.assertRaisesRegex(ValueError, 'native mesh positions, attributes'):
                    verify.check_models(self.mutation(change), specification())

    def test_the_old_crashing_unpacked_vertex_format_is_rejected_at_any_zoom(self):
        def mutate(model):
            model['vertices'][0]['format'] = 2
        with self.assertRaisesRegex(ValueError, 'packed XYZ/UV'):
            verify.check_models(self.mutation(mutate, zoom=4), specification())

    def test_copying_the_top_cell_over_the_bottom_is_not_a_valid_rotation(self):
        resources = dict(self.resources)
        for zoom in range(5):
            resources[*S3D, 0x7F500100 + zoom] = resources[*S3D, 0x7F500000 + zoom]
        with self.assertRaisesRegex(ValueError, 'native mesh positions, attributes'):
            verify.check_models(resources, specification())

    def test_preview_translation_is_checked_against_both_placed_cells(self):
        resources = dict(self.resources)
        preview = parse_s3d(resources[*S3D, 0x7F50FFF0])
        block = preview['vertices'][7]
        raw = bytearray(block['data'])
        struct.pack_into('<f', raw, 8, struct.unpack_from('<f', raw, 8)[0] + 1.)
        block['data'] = bytes(raw)
        resources[*S3D, 0x7F50FFF0] = pack_s3d(preview)
        with self.assertRaisesRegex(ValueError, 'preview does not contain'):
            verify.check_models(resources, specification())

    def test_changing_a_native_input_cannot_refresh_expectations_silently(self):
        donors = {label: dict(values) for label, values in self.context.items()}
        key = (*S3D, 0x5DC01A00)
        donors['hsr'][key] += b'changed'
        with self.assertRaisesRegex(ValueError, 'source fingerprint changed'):
            verify.check_models(self.resources, specification(), donors)

    def test_actual_path_hashes_bind_the_saved_connector_reference(self):
        facts = verify.reviewed_facts(specification())
        for cell, expected in facts['path_hashes_by_cell']:
            index = specification()['cells'].index(cell)
            tile = int(specification()['tile_ids'][index], 16)
            self.assertEqual(hashlib.sha256(self.resources[*PATH, tile]).hexdigest(), expected)


if __name__ == '__main__':
    unittest.main()
