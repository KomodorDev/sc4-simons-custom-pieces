"""Independent routing, level, construction and physical-clearance regressions."""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import struct
import sys
import unittest
from unittest.mock import patch

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp import jsonc
from scp.paths import local_settings
from scp.dbpf import entries, decompress
from scp_hsr.interchange_layouts import INFO, interchange_layout
from scp_hsr.interchange_models import build_interchange, build_rules
from scp_hsr.interchange_verify import (
    CONTRACTS, PATH, S3D, _crossing_audit, _models_cached, _clearance_segments, _bed, _neighbour_rail_ribbon,
    check_paths, check_models, check_construction_fields,
)
from scp.models import parse_s3d, pack_s3d
from scp_hsr.rail_feature_verify import _triangles
from scp.track_paths import encode_paths
from scp.verify import parse_paths, parse_rules


def encode_inspected(routes):
    result = ['SC4PATHS', '1.2', str(len(routes)), '0', '0']
    for route in routes:
        result += list(map(str, (route['transport'], route['lane'], route['entry'], route['exit'],
                                route['compatibility'], len(route['points']))))
        result += [','.join(format(value, '.12g') for value in point) for point in route['points']]
    return ('\r\n'.join(result)+'\r\n').encode('ascii')


class InterchangeVerifierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.specs, cls.routes, cls.models = {}, {}, {}
        for index, (recipe, info) in enumerate(INFO.items()):
            base = 0x7F600000+index*0x4000
            spec = {'recipe': recipe, 'name': recipe, 'footprint': list(info['footprint']),
                    'cells': [list(cell) for cell in info['cells']],
                    'structural_cells': [list(cell) for cell in info.get('structural_cells', [])],
                    'tile_ids': [f'{base+0x100*x+0x10*y:08x}' for x, y in info['cells']],
                    'preview_id': f'{base+0x3ff5:08x}', 'puzzle_id': 'f8ff',
                    'effect_name': f'preview_scp_test_{index:010d}'}
            layout = interchange_layout(recipe)
            cls.specs[recipe] = spec
            cls.routes[recipe] = {(*PATH, int(tile, 16)): encode_paths(layout[cell]['routes'])
                                 for cell, tile in zip(info['cells'], spec['tile_ids'])}
        local = local_settings(ROOT)
        cls.donors = None
        if local.is_file():
            plugins = Path(jsonc.load(local)['plugins'])
            donors = list(plugins.rglob('High Speed Rail.dat'))
            if len(donors) == 1:
                cls.donors = {key: decompress(raw) for key, raw in entries(donors[0].read_bytes()).items()}

    @classmethod
    def fixture(cls, recipe):
        if cls.donors is None:
            raise unittest.SkipTest('Audited local native HSR model donor unavailable')
        if recipe not in cls.models:
            cls.models[recipe] = build_interchange(cls.specs[recipe], {'hsr': cls.donors})[0]
        return cls.models[recipe]

    def mutate(self, recipe, mutation, tile_index=0):
        result = deepcopy(self.routes[recipe])
        key = *PATH, int(self.specs[recipe]['tile_ids'][tile_index], 16)
        routes = parse_paths(result[key])['routes']
        mutation(routes)
        result[key] = encode_inspected(routes)
        return result

    def test_all_registered_modules_have_independent_ports_and_exact_movement_graphs(self):
        self.assertEqual(set(INFO), set(CONTRACTS))
        for recipe in INFO:
            with self.subTest(recipe=recipe):
                report = check_paths(self.routes[recipe], self.specs[recipe])
                self.assertEqual(report['rotations_checked'], 4)
                self.assertTrue(report['exact_3d_cell_seams'])
                self.assertEqual(report['native_facing_port_tangents_checked'], report['external_ports_checked'])

    def test_all_construction_palettes_match_encoded_path_edges(self):
        for recipe in INFO:
            with self.subTest(recipe=recipe):
                _, parsed = parse_rules(build_rules(self.specs[recipe]))
                fields = {}
                for key, value in parsed[0xF8FF]:
                    fields.setdefault(key, []).append(value)
                self.assertTrue(check_construction_fields(fields, self.specs[recipe], self.routes[recipe])[
                    'encoded_path_edge_headings_checked'])

    def test_l4_split_and_merge_are_single_track_rather_than_dual_mainlines(self):
        for mode in ('split', 'merge'):
            for angle in (45, 90, 135):
                for radius in ('compact', 'wide'):
                    recipe = f'interchange_l4_{mode}_{angle}_{radius}'
                    report = check_paths(self.routes[recipe], self.specs[recipe])
                    self.assertEqual(report['external_ports_checked'], 3)
                    self.assertEqual(report['permitted_movements_checked'], 2)

    def test_new_wide_radius_is_larger_than_compact_for_every_branch_angle(self):
        from scp_hsr.interchange_verify import BRANCH_CONTROLS
        for angle in (45, 90, 135):
            compact, wide = BRANCH_CONTROLS[angle, 'compact'], BRANCH_CONTROLS[angle, 'wide']
            self.assertGreater(wide[-1][0]-wide[0][0], compact[-1][0]-compact[0][0])
            self.assertGreater(abs(wide[0][1]), abs(compact[0][1]))

    def test_one_way_path_cannot_be_reversed(self):
        recipe = 'interchange_oneway_l3_straight'
        def reverse(routes):
            routes[0]['points'].reverse()
            routes[0]['entry'], routes[0]['exit'] = routes[0]['exit'], routes[0]['entry']
        with self.assertRaisesRegex(ValueError, 'direction|movement|port'):
            check_paths(self.mutate(recipe, reverse), self.specs[recipe])

    def test_port_coordinates_alone_cannot_mask_a_wrong_native_facing_tangent(self):
        recipe = 'interchange_oneway_l3_straight'
        def skew(routes):
            # External endpoints stay exact, but the intermediate train route
            # approaches them diagonally instead of along native north/south.
            routes[0]['points'] = [(0., -8., 23.), (.2, 0., 23.), (0., 8., 23.)]
        with self.assertRaisesRegex(ValueError, 'native-facing tangent'):
            check_paths(self.mutate(recipe, skew), self.specs[recipe])

    def test_height_jump_and_excessive_grade_are_rejected(self):
        recipe = 'interchange_oneway_grade_hsr_to_l4'
        def jump(routes):
            x, y, _ = routes[0]['points'][0]
            routes[0]['points'][0] = x, y, 1.
        with self.assertRaisesRegex(ValueError, 'grade|height|seam'):
            check_paths(self.mutate(recipe, jump), self.specs[recipe])

    def test_flat_visual_flyover_is_not_a_real_grade_separated_crossing(self):
        lower = [(0., -8., 15.5), (0., 8., 15.5)]
        for height in (15.5, 23.):
            records = [((0, 0), {}, [(-8., 0., height), (8., 0., height)]), ((0, 0), {}, lower)]
            with self.assertRaisesRegex(ValueError, 'vertical deck clearance'):
                _crossing_audit(records, {'required_grade_separated_crossings': 1})
        records = [((0, 0), {}, [(-8., 0., 30.5), (8., 0., 30.5)]), ((0, 0), {}, lower)]
        self.assertEqual(_crossing_audit(records, {'required_grade_separated_crossings': 1}), 1)

    def test_zero_path_is_allowed_only_for_an_explicit_structural_cell(self):
        recipe = 'interchange_test_structural'
        contract = {'cells': [(0, 0), (1, 0)], 'structural_cells': [(1, 0)], 'footprint': (2, 1),
                    'ports': {'in': (0., -8., 15.5), 'out': (0., 8., 15.5)},
                    'movements': [('in', 'out')], 'port_vectors': {'in': (0., 1.), 'out': (0., 1.)}, 'min_height': 15.5, 'max_height': 15.5, 'cost': 200, 'kind': 'single'}
        spec = {'recipe': recipe, 'cells': [[0, 0], [1, 0]], 'structural_cells': [[1, 0]],
                'footprint': [2, 1], 'tile_ids': ['7f900000', '7f900100']}
        route = {'transport': 7, 'lane': 0, 'entry': 3, 'exit': 1, 'compatibility': 0,
                 'points': [(0., -8., 15.5), (0., 8., 15.5)]}
        resources = {(*PATH, 0x7F900000): encode_inspected([route]),
                     (*PATH, 0x7F900100): b'SC4PATHS\r\n1.2\r\n0\r\n0\r\n0\r\n'}
        with patch.dict(CONTRACTS, {recipe: contract}):
            self.assertEqual(check_paths(resources, spec)['encoded_routes_checked'], 1)
            bad = deepcopy(spec)
            bad['structural_cells'] = []
            with self.assertRaisesRegex(ValueError, 'structural'):
                check_paths(resources, bad)

    def test_representative_actual_models_cover_tracks_and_clear_lower_routes(self):
        recipes = ('interchange_hsr_split_90_compact', 'interchange_hsr_merge_90_compact',
                   'interchange_oneway_l3_diagonal', 'interchange_oneway_grade_ground_to_hsr',
                   'interchange_oneway_grade_hsr_to_l4', 'interchange_l4_oneway_over_ground',
                   'interchange_l4_oneway_over_hsr')
        for recipe in recipes:
            with self.subTest(recipe=recipe):
                report = check_models(self.fixture(recipe), self.specs[recipe])
                self.assertTrue(report['preview_matches_tiles'])
                self.assertGreater(report['train_clearance_segments_checked'], 0)
                self.assertEqual(report['authored_clearance_width_m'], 3.)

    def test_close_coflow_ribbon_requires_native_uv_on_the_actual_neighbour(self):
        from scp_hsr.rail_feature_verify import _rail_u, _weights
        height, u = _bed(15.5), _rail_u(2.)
        # A narrow clipped fragment contains this train sample, while the
        # actual neighbour lies just beyond it. The affine stripe remains the
        # same, and the continuation is bounded by the real neighbour distance.
        triangle = ((.17, height, -1., u+.17*.09, 0.), (.19, height, -1., u+.19*.09, 0.),
                    (.18, height, 1., u+.18*.09, 0.))
        point = (.18, 0., 15.5)
        candidates = [(triangle, _weights(point[0], -point[1], triangle))]
        neighbour = [(1, (0., -1., 15.5), (0., 1., 15.5))]
        self.assertTrue(_neighbour_rail_ribbon(point, candidates, neighbour, 0))
        far = [(1, (-5., -1., 15.5), (-5., 1., 15.5))]
        self.assertFalse(_neighbour_rail_ribbon(point, candidates, far, 0))
        upper = [(1, (0., -1., 30.5), (0., 1., 30.5))]
        self.assertFalse(_neighbour_rail_ribbon(point, candidates, upper, 0))
        shifted = tuple((*v[:3], v[3]+.1, v[4]) for v in triangle)
        candidates = [(shifted, _weights(point[0], -point[1], shifted))]
        self.assertFalse(_neighbour_rail_ribbon(point, candidates, neighbour, 0))

    def test_large_beam_containing_the_entire_route_envelope_is_rejected(self):
        from collections import defaultdict
        # No triangle corner enters this short corridor, and no edges cross:
        # the beam contains its entire projected rectangle. Containment must
        # still count as a collision, alongside edge and corner intersections.
        records = [((0, 0), {}, [(0., -.5, 15.5), (0., .5, 15.5)])]
        height = _bed(15.5)+3.
        beam = ((-20., height, -20., .61, 0.), (20., height, -20., .61, 0.),
                (0., height, 20., .61, 0.))
        buckets = defaultdict(lambda: [beam])
        with self.assertRaisesRegex(ValueError, 'beam|clearance envelope'):
            _clearance_segments(records, buckets)

    def test_support_pillar_through_a_lower_track_is_rejected(self):
        from scp_hsr.single_track_models import _native, _pack
        recipe = 'interchange_l4_oneway_over_hsr'
        resources = deepcopy(self.fixture(recipe))
        tile = int(self.specs[recipe]['tile_ids'][1], 16)
        triangles = list(_triangles(parse_s3d(resources[*S3D, tile])))
        # Local x=-2 is the lower southbound lane. This narrow pillar misses
        # the centreline and all PATH samples, but lies inside the authored 3 m-wide
        # train envelope. A check of centre points alone would wrongly pass.
        a, b, c, d = ((-1.3, 16.4, 0., .61, 0.), (-1.1, 16.4, 0., .61, 0.),
                      (-1.1, 28., 0., .61, 1.), (-1.3, 28., 0., .61, 1.))
        triangles.extend(((a, b, c), (a, c, d)))
        raw = _pack(_native(self.donors[*S3D, 0x5DD31500]), triangles)
        for zoom in range(5):
            resources[*S3D, tile+zoom] = raw
        with self.assertRaisesRegex(ValueError, 'pillar|clearance envelope'):
            check_models(resources, self.specs[recipe])

    def test_model_cache_returns_fresh_reports_and_invalidates_changed_bytes(self):
        recipe = 'interchange_l4_oneway_over_hsr'
        resources, spec = self.fixture(recipe), self.specs[recipe]
        report = check_models(resources, spec)
        report.pop('texture_ids')
        hits = _models_cached.cache_info().hits
        self.assertEqual(check_models(resources, spec)['texture_ids'], [0x0BF6E09B])
        self.assertEqual(_models_cached.cache_info().hits, hits+1)
        self.assertEqual(_models_cached.cache_info().maxsize, 256)

    def test_uv_shift_is_rejected_even_when_the_preview_and_all_zooms_agree(self):
        recipe = 'interchange_oneway_l3_straight'
        resources = deepcopy(self.fixture(recipe))
        for key in list(resources):
            if key[:2] != S3D:
                continue
            model = parse_s3d(resources[key])
            for vb in model['vertices']:
                raw = bytearray(vb['data'])
                for offset in range(0, len(raw), vb['stride']):
                    struct.pack_into('<f', raw, offset+12, struct.unpack_from('<f', raw, offset+12)[0]+.1)
                vb['data'] = bytes(raw)
            resources[key] = pack_s3d(model)
        with self.assertRaisesRegex(ValueError, 'native rail band'):
            check_models(resources, self.specs[recipe])


if __name__ == '__main__':
    unittest.main()
