"""Portable semantic checks for the expanded fixed rail construction kit."""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import struct
import sys
import unittest

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp.dbpf import entries, decompress
from scp.models import parse_s3d, pack_s3d
from scp_hsr.rail_features import INFO, build_feature, feature_layout, native_model, native_paths
from scp_hsr.rail_feature_verify import (
    CONSTRUCTION, RECIPES, RAMP_GEOMETRY, PATH, S3D,
    _native_fingerprint, _triangles, check_paths, check_models, construction_expectations,
)
from scp.track_paths import encode_paths
from scp.verify import parse_paths, parse_rules, compact


def encode_inspected(routes):
    lines = ['SC4PATHS', '1.2', str(len(routes)), '0', '0']
    for route in routes:
        lines += [str(value) for value in (route['transport'], route['lane'], route['entry'],
                  route['exit'], route['compatibility'], len(route['points']))]
        lines += [','.join(format(value, '.12g') for value in point) for point in route['points']]
    return ('\r\n'.join(lines) + '\r\n').encode('ascii')


class RailFeatureVerifierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        local = ROOT / 'local/settings.json'
        if not local.is_file():
            raise unittest.SkipTest('Audited local NAM donor is unavailable')
        plugins = Path(json.loads(local.read_text())['plugins'])
        candidates = list(plugins.rglob('High Speed Rail.dat'))
        if len(candidates) != 1:
            raise unittest.SkipTest('One audited native HSR donor is required')
        cls.donors = {key: decompress(raw) for key, raw in entries(candidates[0].read_bytes()).items()}
        cls.models = {}
        cls.paths = {}
        cls.specs = {}
        for n, (recipe, info) in enumerate(INFO.items()):
            base = 0x7F550000 + n*0x1000
            spec = {'recipe': recipe, 'name': recipe, 'footprint': list(info['footprint']),
                    'cells': [list(cell) for cell in info['cells']],
                    'tile_ids': [f'{base + 0x100*x + 0x10*y:08x}' for x, y in info['cells']],
                    'preview_id': f'{base+0xff5:08x}', 'puzzle_id': 'f7ff',
                    'effect_name': f'preview_scp_test_{n:010d}'}
            resources = {}
            for cell, raw_tile in zip(info['cells'], spec['tile_ids']):
                data = feature_layout(recipe)[cell]
                routes = (native_paths(cls.donors[*PATH, data['native_source']], data['native_rotation'])
                          if 'native_source' in data else data['routes'])
                resources[*PATH, int(raw_tile, 16)] = encode_paths(routes)
            cls.specs[recipe], cls.paths[recipe] = spec, resources

    @classmethod
    def fixture(cls, recipe):
        if recipe not in cls.models:
            cls.models[recipe] = build_feature(cls.specs[recipe], {'hsr': cls.donors})[0]
        return cls.models[recipe]

    def mutate_paths(self, recipe, mutation, tile_index=0):
        resources = deepcopy(self.paths[recipe])
        key = *PATH, int(self.specs[recipe]['tile_ids'][tile_index], 16)
        routes = parse_paths(resources[key])['routes']
        mutation(routes)
        resources[key] = encode_inspected(routes)
        return resources

    def test_all_nine_encoded_port_graphs_have_only_intended_movements(self):
        self.assertEqual(set(INFO), RECIPES)
        for recipe in INFO:
            with self.subTest(recipe=recipe):
                report = check_paths(self.paths[recipe], self.specs[recipe])
                self.assertTrue(report['cell_seams_match_exactly'])
                self.assertEqual(report['rotations_checked'], 4)
                self.assertEqual(report['permitted_movements_checked'],
                                 6 if '_crossover_' in recipe else 2)

    def test_unknown_rail_recipe_is_never_accepted(self):
        spec = dict(self.specs['rail_hsr_adjacent_crossover_right'], recipe='rail_unknown')
        with self.assertRaisesRegex(ValueError, 'Unknown'):
            check_paths({}, spec)

    def test_level_path_cannot_jump_to_the_other_height(self):
        recipe = 'rail_hsr_adjacent_crossover_right'
        resources = self.mutate_paths(recipe, lambda routes: routes[0]['points'].__setitem__(
            0, (*routes[0]['points'][0][:2], 1.)))
        with self.assertRaisesRegex(ValueError, 'height|grade'):
            check_paths(resources, self.specs[recipe])

    def test_transition_preserves_every_native_grade_sample(self):
        recipe = 'rail_hsr_ghsr_transition'
        def mutate(routes):
            x, y, height = routes[0]['points'][3]
            routes[0]['points'][3] = x, y, height+.005
        resources = self.mutate_paths(recipe, mutate, tile_index=2)
        with self.assertRaisesRegex(ValueError, 'exact audited native slope'):
            check_paths(resources, self.specs[recipe])

    def test_external_wrong_direction_is_rejected(self):
        recipe = 'rail_ghsr_diagonal_s_right'
        def mutate(routes):
            routes[0]['points'].reverse()
            routes[0]['entry'], routes[0]['exit'] = routes[0]['exit'], routes[0]['entry']
        resources = self.mutate_paths(recipe, mutate)
        with self.assertRaisesRegex(ValueError, 'seam|direction|port'):
            check_paths(resources, self.specs[recipe])

    def test_disconnected_internal_seam_is_rejected(self):
        recipe = 'rail_hsr_adjacent_crossover_right'
        def mutate(routes):
            x, y, height = routes[0]['points'][-1]
            routes[0]['points'][-1] = x+.01, y, height
        resources = self.mutate_paths(recipe, mutate)
        with self.assertRaisesRegex(ValueError, 'seam|port'):
            check_paths(resources, self.specs[recipe])

    def test_negative_path_class_is_rejected(self):
        recipe = 'rail_hsr_adjacent_crossover_right'
        resources = self.mutate_paths(recipe, lambda routes: routes[0].__setitem__('lane', -1))
        with self.assertRaisesRegex(ValueError, 'class'):
            check_paths(resources, self.specs[recipe])

    def test_missing_branch_junction_flag_is_rejected(self):
        recipe = 'rail_hsr_adjacent_crossover_right'
        def mutate(routes):
            for route in routes:
                route['compatibility'] = 0
        resources = self.mutate_paths(recipe, mutate, tile_index=4)
        with self.assertRaisesRegex(ValueError, 'junction'):
            check_paths(resources, self.specs[recipe])

    def test_native_visible_geometry_fingerprints_survive_every_proper_rotation(self):
        for row in range(8):
            for turns in range(4):
                with self.subTest(row=row, turns=turns):
                    model = parse_s3d(native_model(self.donors[*S3D, 0x5DCF1700+row*0x10], turns))
                    self.assertEqual(_native_fingerprint(model, -turns % 4), RAMP_GEOMETRY[row])

    def test_all_authored_model_families_cover_their_paths_and_match_the_preview(self):
        recipes = list(INFO)
        for recipe in recipes:
            with self.subTest(recipe=recipe):
                report = check_models(self.fixture(recipe), self.specs[recipe])
                self.assertTrue(report['preview_matches_tiles'])
                self.assertTrue(report['native_texture_bands_checked'])

    def test_tampered_transition_geometry_is_rejected_without_local_donors(self):
        recipe = 'rail_hsr_ghsr_transition'
        # Prime an identical-input pass first: changed bytes must never reuse it.
        check_models(self.fixture(recipe), self.specs[recipe])
        resources = deepcopy(self.fixture(recipe))
        tile = int(self.specs[recipe]['tile_ids'][0], 16)
        model = parse_s3d(resources[*S3D, tile])
        data = bytearray(model['vertices'][0]['data'])
        struct.pack_into('<f', data, 0, struct.unpack_from('<f', data)[0]+.1)
        model['vertices'][0]['data'] = bytes(data)
        for zoom in range(5):
            resources[*S3D, tile+zoom] = pack_s3d(model)
        with self.assertRaisesRegex(ValueError, 'visible geometry'):
            check_models(resources, self.specs[recipe])

    def test_memoized_reports_are_fresh_objects_and_cover_all_input_resources(self):
        from scp_hsr.rail_feature_verify import _check_models_cached
        recipe = 'rail_hsr_ghsr_transition'
        resources, spec = self.fixture(recipe), self.specs[recipe]
        first = check_models(resources, spec)
        before = _check_models_cached.cache_info().hits
        first.pop('texture_ids')
        second = check_models(resources, spec)
        self.assertEqual(_check_models_cached.cache_info().hits, before+1)
        self.assertEqual(second['texture_ids'], [0x0BF6E09B, 0xEBF6E069])
        self.assertEqual(_check_models_cached.cache_info().maxsize, 64)
        changed = deepcopy(resources)
        tile = int(spec['tile_ids'][0], 16)
        parsed = parse_paths(changed[*PATH, tile])['routes']
        parsed[0]['points'][0] = 7., -8., 15.354
        changed[*PATH, tile] = encode_inspected(parsed)
        misses = _check_models_cached.cache_info().misses
        # Native model audits pin the exact model independently of PATH. The
        # PATH bytes nevertheless belong to the key and trigger a new audit;
        # the separate check_paths entry point rejects the altered PATH.
        check_models(changed, spec)
        self.assertEqual(_check_models_cached.cache_info().misses, misses+1)

    def test_added_above_bed_wall_cannot_block_a_connected_train_path(self):
        from scp_hsr.single_track_models import _native, _pack
        recipe = 'rail_hsr_adjacent_crossover_right'
        resources = deepcopy(self.fixture(recipe))
        tile = int(self.specs[recipe]['tile_ids'][0], 16)
        triangles = list(_triangles(parse_s3d(resources[*S3D, tile])))
        # This vertical concrete barrier crosses both tracks between their
        # PATH nodes, so checking only sampled node positions would miss it.
        a, b, c, d = ((-5., 16.45, 4., .61, 0.), (5., 16.45, 4., .61, 0.),
                      (5., 17., 4., .61, 1.), (-5., 17., 4., .61, 1.))
        triangles.extend(((a, b, c), (a, c, d)))
        raw = _pack(_native(self.donors[*S3D, 0x5DD31500]), triangles)
        for zoom in range(5):
            resources[*S3D, tile+zoom] = raw
        with self.assertRaisesRegex(ValueError, 'above-bed wall'):
            check_models(resources, self.specs[recipe])

    def test_construction_has_one_literal_table_per_recipe(self):
        from scp_hsr.rail_features import build_rules
        self.assertEqual(set(CONSTRUCTION), RECIPES)
        for recipe in INFO:
            with self.subTest(recipe=recipe):
                _, parsed = parse_rules(build_rules(self.specs[recipe]))
                root = int(self.specs[recipe]['puzzle_id'], 16)
                fields = {}
                for key, value in parsed[root]:
                    fields.setdefault(key, []).append(value)
                cells, cons, flags, cost = construction_expectations(self.specs[recipe])
                self.assertEqual(list(map(compact, fields['CellLayout'])), cells)
                self.assertEqual(list(map(compact, fields['ConsLayout'])), cons)
                self.assertEqual(set(map(compact, fields['CheckType'])), flags)
                self.assertEqual(fields['Costs'], [str(cost)])
                self.assertEqual(sum(row.count('+') for row in cons), len(self.specs[recipe]['tile_ids']))


if __name__ == '__main__':
    unittest.main()
