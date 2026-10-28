"""Independent negative controls for reusable stacked and graded HSR parts."""
from __future__ import annotations

from collections import defaultdict
from copy import deepcopy
import json
import math
from pathlib import Path
import sys
import struct
import unittest

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp.dbpf import entries, decompress
from scp_hsr.hsr_components_verify import (
    CONTRACTS, check_paths, check_models, check_construction_fields, audit_height_profile, audit_adapter_native_profiles,
)
from scp_hsr.hsr_mesh_verify import audit_bed_union, audit_supports
from scp_hsr.interchange_verify import PATH, S3D, _bed, _graph, _clearance_segments
from scp.verify import parse_paths, parse_rules
from scp_hsr.test_support import spec_for, floor


def encode_inspected(routes):
    lines = ['SC4PATHS', '1.2', str(len(routes)), '0', '0']
    for route in routes:
        lines.extend(str(route[key]) for key in ('transport', 'lane', 'entry', 'exit', 'compatibility'))
        lines.append(str(len(route['points'])))
        lines.extend(','.join(format(v, '.12g') for v in point) for point in route['points'])
    return ('\r\n'.join(lines)+'\r\n').encode('ascii')


def route(points, entry, exit_):
    return {'transport': 7, 'lane': 0, 'entry': entry, 'exit': exit_,
            'compatibility': 0, 'points': points}


def ramp_height(y):
    """Literal 128m ramp: 8m collars and 16m grade easements."""
    s = min(112., max(0., y+112.))
    if s < 16.:
        rise = .15625*s*s/32.
    elif s > 96.:
        rise = 15.-.15625*(112.-s)**2/32.
    else:
        rise = .15625*(s-8.)
    return 15.5+rise


def literal_core_paths(recipe):
    """Fixtures authored directly from the approved ports, without the writer."""
    spec = spec_for(recipe)
    result = {}
    for (x, row), raw_tile in zip(CONTRACTS[recipe]['cells'], spec['tile_ids']):
        if recipe.endswith('paired_ramp_l2_to_l4'):
            forward = [(2., -8.+n/2., ramp_height(-16.*row-8.+n/2.)) for n in range(33)]
            reverse = [(-2., y, h) for _, y, h in reversed(forward)]
            routes = [route(forward, 3, 1), route(reverse, 1, 3)]
        elif recipe.endswith('upper_paired_straight'):
            routes = [route([(2., -8., 30.5), (2., 8., 30.5)], 3, 1),
                      route([(-2., 8., 30.5), (-2., -8., 30.5)], 1, 3)]
        else:
            routes = []
            if x == 1:
                routes.extend([route([(2., -8., 30.5), (2., 8., 30.5)], 3, 1),
                               route([(-2., 8., 30.5), (-2., -8., 30.5)], 1, 3)])
            if row == 1:
                routes.extend([route([(-8., -2., 15.5), (8., -2., 15.5)], 0, 2),
                               route([(8., 2., 15.5), (-8., 2., 15.5)], 2, 0)])
        result[*PATH, int(raw_tile, 16)] = encode_inspected(routes)
    return spec, result


def sloped_pier(gradient=.1, top=14., x=0., z=5.):
    base = [(x+dx, 0., z+dz, .1, 0.) for dx, dz in ((-.65, -.65), (.65, -.65), (.65, .65), (-.65, .65))]
    head = [(p[0], top+gradient*(p[2]-z), p[2], .1, 1.) for p in base]
    result = [(base[0], base[2], base[1]), (base[0], base[3], base[2]),
              (head[0], head[1], head[2]), (head[0], head[2], head[3])]
    for n in range(4):
        a, b, c, d = base[n], base[(n+1)%4], head[(n+1)%4], head[n]
        result.extend([(a, b, c), (a, c, d)])
    return result


class CoreEncodedComponentTests(unittest.TestCase):
    recipes = ('hsr_component_upper_paired_straight', 'hsr_component_paired_ramp_l2_to_l4')

    def test_literal_ports_bidirectional_pair_and_isolated_crossing_levels(self):
        for recipe in self.recipes:
            with self.subTest(recipe=recipe):
                spec, paths = literal_core_paths(recipe)
                report = check_paths(paths, spec)
                self.assertEqual(report['rotations_checked'], 4)
                self.assertEqual(report['external_ports_checked'], len(CONTRACTS[recipe]['ports']))
                self.assertEqual(report['unique_complete_journeys_checked'], len(CONTRACTS[recipe]['movements']))
                self.assertEqual(report['grade_separated_crossings_checked'],
                                 4 if recipe.endswith('hsr_over_hsr') else 0)
                self.assertFalse(report['unwanted_cross_level_transfers'])
                self.assertFalse(report['collision_free_operation_claimed'])
                self.assertLessEqual(report['maximum_encoded_grade'], .156251)

    def test_missing_track_wrong_direction_and_shifted_native_offset_fail(self):
        spec, paths = literal_core_paths(self.recipes[0])
        key = next(iter(paths))
        original = parse_paths(paths[key])['routes']
        with self.assertRaisesRegex(ValueError, 'missing.*port'):
            check_paths({key: encode_inspected(original[:1])}, spec)
        changed = deepcopy(original)
        changed[0]['points'].reverse()
        changed[0]['entry'], changed[0]['exit'] = 1, 3
        with self.assertRaises(ValueError):
            check_paths({key: encode_inspected(changed)}, spec)
        changed = deepcopy(original)
        changed[0]['points'] = [(x+.1, y, h) for x, y, h in changed[0]['points']]
        with self.assertRaisesRegex(ValueError, 'missing.*port|disconnected'):
            check_paths({key: encode_inspected(changed)}, spec)

    def test_encoded_interior_seam_cannot_jump_height_or_change_track(self):
        spec, paths = literal_core_paths(self.recipes[1])
        key = *PATH, int(spec['tile_ids'][3], 16)
        routes = parse_paths(paths[key])['routes']
        routes[0]['points'][-1] = (*routes[0]['points'][-1][:2], routes[0]['points'][-1][2]-.01)
        with self.assertRaisesRegex(ValueError, 'seam|disconnected'):
            check_paths({**paths, key: encode_inspected(routes)}, spec)
        routes = parse_paths(paths[key])['routes']
        routes[0]['points'][-1] = (-2., *routes[0]['points'][-1][1:])
        with self.assertRaises(ValueError):
            check_paths({**paths, key: encode_inspected(routes)}, spec)

    def test_native_flat_collar_and_monotonic_grade_are_measured(self):
        contract = CONTRACTS[self.recipes[1]]
        valid = [(2., -120.+n/2., ramp_height(-120.+n/2.)) for n in range(257)]
        self.assertAlmostEqual(audit_height_profile(valid, contract), .15625)
        changed = list(valid)
        changed[3] = (2., -118.5, 15.50001)
        with self.assertRaisesRegex(ValueError, 'reverses|flat collar'):
            audit_height_profile(changed, contract)
        changed = list(valid)
        changed[1] = (2., -119.5, 15.501)
        with self.assertRaises(ValueError):
            audit_height_profile(changed, contract)
        changed = list(valid)
        changed[129] = (*changed[129][:2], changed[128][2]-.001)
        with self.assertRaisesRegex(ValueError, 'reverses'):
            audit_height_profile(changed, contract)

    def test_flat_collar_is_checked_even_when_one_long_segment_spans_its_boundary(self):
        contract = CONTRACTS[self.recipes[1]]
        points = [(2., -120., 15.5), (2., -119., 15.5), (2., -100., 16.),
                  (2., 0., 30.5), (2., 8., 30.5)]
        with self.assertRaisesRegex(ValueError, 'full flat collar'):
            audit_height_profile(points, contract)

    def test_an_interior_lateral_wobble_cannot_pass_as_a_straight_native_track(self):
        spec, paths = literal_core_paths(self.recipes[1])
        key = *PATH, int(spec['tile_ids'][3], 16)
        routes = parse_paths(paths[key])['routes']
        x, y, h = routes[0]['points'][16]
        routes[0]['points'][16] = x+.00001, y, h
        with self.assertRaisesRegex(ValueError, 'native offset'):
            check_paths({**paths, key: encode_inspected(routes)}, spec)

    def test_unknown_recipe_and_unreviewed_footprint_or_structural_cells_fail(self):
        spec, paths = literal_core_paths(self.recipes[0])
        for changed in ({**spec, 'recipe': 'hsr_component_unknown'},
                        {**spec, 'footprint': [1, 2]},
                        {**spec, 'structural_cells': [[0, 0]]},
                        {**spec, 'tile_ids': ['7f900010', '7f900020']}):
            with self.subTest(change=changed):
                with self.assertRaises(ValueError):
                    check_paths(paths, changed)


class HeightAwarePhysicalNegativeControls(unittest.TestCase):
    def test_lower_deck_cannot_fill_a_hole_in_an_upper_deck(self):
        records = [((0, 0), {}, [(0., 0., 15.5), (0., -10., 15.5)]),
                   ((0, 0), {}, [(0., 0., 30.5), (0., -10., 30.5)])]
        surfaces = floor(-2.5, 2.5, 0., 10.)+floor(-2.5, 2.5, 0., 10., height=30.5)
        self.assertEqual(audit_bed_union(surfaces, records)['full_width_bed_union_segments_checked'], 2)
        with self.assertRaisesRegex(ValueError, 'hole.*at its height'):
            audit_bed_union(surfaces[:2], records)

    def test_adapter_requires_full_native_pair_and_two_separate_output_profiles(self):
        planes = []
        for height in (31.189326, 29.01067):
            planes += floor(-7.5, 7.5, 112., 120., absolute_y=height)
            planes += floor(-4., 4., -8., 0., absolute_y=height)
            planes += floor(12., 20., -8., 0., absolute_y=height)
        for x0, x1 in ((-7.5, -5.9965477), (5.9965477, 7.5)):
            planes += floor(x0, x1, 112., 120., absolute_y=31.98933)
        for x0, x1 in ((-4., -2.6), (2.6, 4.), (12., 13.4), (18.6, 20.)):
            planes += floor(x0, x1, -8., 0., absolute_y=31.98933)
        report = audit_adapter_native_profiles(planes)
        self.assertEqual(report['native_adapter_profile_sections_checked'], 12)
        narrow = []
        for height in (31.189326, 29.01067):
            narrow += floor(-4., 4., 112., 120., absolute_y=height)
            narrow += floor(-4., 4., -8., 0., absolute_y=height)
            narrow += floor(12., 20., -8., 0., absolute_y=height)
        with self.assertRaisesRegex(ValueError, 'width, continuity or thickness'):
            audit_adapter_native_profiles(narrow)
        wall = ((0., 31.5, 112., .1, 0.), (0., 31.8, 120., .1, 0.),
                (0., 31.5, 120., .1, 0.))
        with self.assertRaisesRegex(ValueError, 'internal wall'):
            audit_adapter_native_profiles(planes+[wall])
        wrong_caps = [tri for tri in planes if min(p[1] for p in tri) < 31.9]
        for x0, x1 in ((-7.5, -5.7967), (5.7967, 7.5)):
            wrong_caps += floor(x0, x1, 112., 120., absolute_y=31.98933)
        for x0, x1 in ((-4., -2.6), (2.6, 4.), (12., 13.4), (18.6, 20.)):
            wrong_caps += floor(x0, x1, -8., 0., absolute_y=31.98933)
        with self.assertRaisesRegex(ValueError, 'parapet top widths'):
            audit_adapter_native_profiles(wrong_caps)
        no_underside = [tri for tri in planes if min(p[1] for p in tri) > 30.]
        with self.assertRaisesRegex(ValueError, 'width, continuity or thickness'):
            audit_adapter_native_profiles(no_underside)

    def test_an_obstruction_between_path_samples_blocks_the_full_inclined_train_volume(self):
        records = [((0, 0), {}, [(0., 0., 15.5), (0., -10., 16.5)])]
        h = _bed(16.)
        wall = ((2.2, h+.3, 4.9, .1, 0.), (2.2, h+1., 4.9, .1, 0.),
                (2.2, h+1., 5.1, .1, 0.))
        buckets = defaultdict(lambda: [wall])
        # Its lateral position lies outside a narrower3m envelope, but inside
        # the new component family's required5m envelope.
        self.assertEqual(_clearance_segments(records, buckets, half_width=1.5), 1)
        with self.assertRaisesRegex(ValueError, 'clearance envelope'):
            _clearance_segments(records, buckets, half_width=2.5)

    def test_support_head_must_follow_inclined_underside_across_nine_contacts(self):
        contract = {'support_centres_xz': [(0., 5.)], 'foundation_width_m': 1.3,
                    'minimum_support_spacing_m': 16.}
        underside = floor(-4., 4., 0., 10., absolute_y=13.5, gradient=.1)
        report = audit_supports(sloped_pier()+underside, contract)
        self.assertEqual(report['support_contact_points_checked'], 9)
        self.assertEqual(report['sloped_support_heads_checked'], 1)
        with self.assertRaisesRegex(ValueError, 'floats below|cuts through'):
            audit_supports(sloped_pier(gradient=0.)+underside, contract)
        with self.assertRaisesRegex(ValueError, 'duplicate support foundations'):
            audit_supports(sloped_pier()*2+underside, contract)


class GeneratedComponentContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from scp_hsr.hsr_components_layout import component_layout
        from scp.track_paths import encode_paths
        from scp_hsr.interchange_models import EMPTY_STRUCTURAL_PATH
        cls.specs, cls.paths = {}, {}
        for recipe in CONTRACTS:
            spec = spec_for(recipe)
            layout = component_layout(recipe)
            cls.specs[recipe] = spec
            cls.paths[recipe] = {
                (*PATH, int(tile, 16)): encode_paths(layout[cell]['routes'])
                if layout[cell]['routes'] else EMPTY_STRUCTURAL_PATH
                for cell, tile in zip(CONTRACTS[recipe]['cells'], spec['tile_ids'])}

    def test_all_generated_paths_match_literal_ports_and_quality_limits(self):
        # The obsolete compact diverge is replaced by a second placement of
        # the existing mainline diverge; its recipe contract is reused.
        # The nine-cell core and matching recessed-web straight replace
        # the superseded full fan build type.
        self.assertEqual(len(self.specs), 34)
        self.assertNotIn('hsr_component_l2_paired_fan_compact_join', self.specs)
        self.assertIn('hsr_component_l2_paired_fan_compact_core', self.specs)
        self.assertIn('hsr_component_l2_paired_straight_recessed_web', self.specs)
        self.assertNotIn('hsr_component_l2_compact_fan_diverge', self.specs)
        for recipe, spec in self.specs.items():
            with self.subTest(recipe=recipe):
                report = check_paths(self.paths[recipe], spec)
                self.assertEqual(report['unique_complete_journeys_checked'], len(CONTRACTS[recipe]['movements']))
                if 'curve90' in recipe:
                    for measured in report['journey_quality'].values():
                        minimum = 24. if CONTRACTS[recipe]['kind'] == 'tight_paired_curved_grade' else 50.
                        self.assertGreater(measured['minimum_sampled_radius_m'], minimum)
                        self.assertAlmostEqual(abs(measured['signed_turn_degrees']), 90., delta=1.)

    def test_emitted_rules_have_native_headings_and_unique_real_engine_addresses(self):
        from scp_hsr.hsr_components import build_rules
        for recipe, spec in self.specs.items():
            with self.subTest(recipe=recipe):
                fields = defaultdict(list)
                for key, value in parse_rules(build_rules(spec))[1][int(spec['puzzle_id'], 16)]:
                    fields[key].append(value)
                report = check_construction_fields(fields, spec, self.paths[recipe])
                self.assertEqual(report['runtime_addresses']['unique_byte_keys'], len(spec['cells']))
                self.assertEqual(report['runtime_addresses']['wrong_model_selections'], 0)
                wrong = deepcopy(fields)
                wrong['AutoTileBase'] = [hex(int(fields['AutoTileBase'][0], 0)+16)]
                with self.assertRaisesRegex(ValueError, 'AutoTileBase selects the wrong'):
                    check_construction_fields(wrong, spec, self.paths[recipe])

    def test_structural_slab_cell_cannot_silently_gain_a_foreign_route(self):
        recipe = 'hsr_component_upper_paired_curve90_right'
        spec, paths = self.specs[recipe], self.paths[recipe]
        index = spec['cells'].index([1, 0])
        key = *PATH, int(spec['tile_ids'][index], 16)
        extra = route([(0., -8., 30.5), (0., 8., 30.5)], 3, 1)
        with self.assertRaisesRegex(ValueError, 'Structural.*empty PATH'):
            check_paths({**paths, key: encode_inspected([extra])}, spec)


class NativeComponentModelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.donors, cls.models = None, {}
        local = ROOT/'local/settings.json'
        if local.is_file():
            plugins = Path(json.loads(local.read_text())['plugins'])
            candidates = list(plugins.rglob('High Speed Rail.dat'))
            if len(candidates) == 1:
                cls.donors = {key: decompress(raw) for key, raw in entries(candidates[0].read_bytes()).items()}

    @classmethod
    def fixture(cls, recipe):
        if cls.donors is None:
            raise unittest.SkipTest('Audited local HSR native donor unavailable')
        if recipe not in cls.models:
            from scp_hsr.hsr_components import build_hsr_component
            cls.models[recipe] = build_hsr_component(spec_for(recipe), {'hsr': cls.donors})[0]
        return cls.models[recipe]

    def replace_model(self, resources, spec, index, model):
        from scp.models import pack_s3d, parse_s3d
        from scp.recipes import combine_meshes
        raw = pack_s3d(model)
        tile = int(spec['tile_ids'][index], 16)
        for zoom in range(5):
            resources[*S3D, tile+zoom] = raw
        parts = []
        for cell, tile in zip(spec['cells'], spec['tile_ids']):
            source = parse_s3d(resources[*S3D, int(tile, 16)])
            parts.append((source, source['meshes'], (16.*cell[0], 0., 16.*cell[1])))
        resources[*S3D, int(spec['preview_id'], 16)] = pack_s3d(combine_meshes(parts))

    def test_all_actual_native_meshes_have_full_beds_clearance_contacts_and_render_budgets(self):
        from scp_hsr.hsr_partition_components_verify import CONTRACTS as partition_contracts
        from scp_hsr.hsr_compact_fan_verify import CONTRACTS as compact_fan_contracts
        from scp_hsr.hsr_atomic_components_verify import CONTRACTS as atomic_contracts
        for recipe, contract in CONTRACTS.items():
            with self.subTest(recipe=recipe):
                report = check_models(self.fixture(recipe), spec_for(recipe))
                self.assertEqual(report['models_checked'], 5*len(contract['cells'])+1)
                self.assertEqual(report['render_budget_models_checked'], 5*len(contract['cells'])+1)
                self.assertEqual(report['authored_clearance_width_m'], 5.)
                self.assertEqual(report['authored_clearance_height_m'], 5.)
                self.assertEqual(report['support_columns_checked'], len(contract['support_centres_xz']))
                self.assertEqual(report['support_contact_points_checked'], 9*len(contract['support_centres_xz']))
                self.assertTrue(report['preview_matches_tiles'])
                if recipe in partition_contracts:
                    # Every reusable module uses its direct current-resource
                    # proof, including parts with native cardinal ends. Some
                    # curved cuts need the adjacent module to complete the
                    # corridor; the whole current assembly audit checks it.
                    self.assertTrue(report['all_module_local_model_bytes_unchanged'])
                    self.assertTrue(report['all_module_local_path_bytes_unchanged'])
                    self.assertEqual(report['frozen_module_model_zooms_checked'], 5*len(contract['cells']))
                    self.assertEqual(report['frozen_module_path_files_checked'], len(contract['cells']))
                    self.assertEqual(report['frozen_module_recipe'], recipe)
                    self.assertFalse(report['custom_curve_ends_reswept'])
                    continue
                self.assertTrue(report['height_aware_bed_union_checked'])
                if recipe in compact_fan_contracts or recipe in atomic_contracts:
                    self.assertFalse(report['unused_visible_rails_outside_declared_custom_caps'])
                    if recipe in atomic_contracts:
                        expected = 6 if recipe == 'hsr_component_l2_short_opposed_merge_core' else 3
                        self.assertEqual(report['complete_native_join_sections_checked'], expected)
                else:
                    self.assertFalse(report['unused_visible_native_rails'])
                if contract['kind'] == 'paired_to_single_adapter':
                    self.assertEqual(report['native_adapter_profile_sections_checked'], 12)
                    self.assertFalse(report['paired_collar_internal_walls'])
                if 'ramp' in recipe or 'l2_to_l4' in recipe or 'l4_to_l2' in recipe:
                    self.assertGreater(report['sloped_support_heads_checked'], 0)

    def test_shortened_actual_support_fails_with_all_zooms_and_preview_updated(self):
        from scp.models import parse_s3d
        recipe = 'hsr_component_upper_paired_straight'
        spec = spec_for(recipe)
        resources = deepcopy(self.fixture(recipe))
        model = parse_s3d(resources[*S3D, int(spec['tile_ids'][0], 16)])
        supports = [mesh for mesh in model['meshes'] if b'consolidated' in mesh['name']]
        self.assertTrue(supports)
        for vertex_index in {mesh['frames'][0][0] for mesh in supports}:
            vb = model['vertices'][vertex_index]
            data = bytearray(vb['data'])
            for offset in range(0, len(data), vb['stride']):
                y = struct.unpack_from('<f', data, offset+4)[0]
                struct.pack_into('<f', data, offset+4, min(y, 10.))
            vb['data'] = bytes(data)
        self.replace_model(resources, spec, 0, model)
        with self.assertRaisesRegex(ValueError, 'floats below|cuts through'):
            check_models(resources, spec)

    def test_duplicate_actual_support_is_rejected_across_different_cell_models(self):
        from scp.models import parse_s3d
        from scp.recipes import combine_meshes
        recipe = 'hsr_component_paired_ramp_l2_to_l4'
        spec = spec_for(recipe)
        resources = deepcopy(self.fixture(recipe))
        source = parse_s3d(resources[*S3D, int(spec['tile_ids'][0], 16)])
        target = parse_s3d(resources[*S3D, int(spec['tile_ids'][1], 16)])
        supports = [mesh for mesh in source['meshes'] if b'consolidated' in mesh['name']]
        self.assertTrue(supports)
        duplicate = combine_meshes([(target, target['meshes'], (0., 0., 0.)),
                                    (source, supports, (0., 0., -16.))])
        self.replace_model(resources, spec, 1, duplicate)
        with self.assertRaisesRegex(ValueError, 'duplicate support foundations'):
            check_models(resources, spec)

    def test_changed_rail_uv_cannot_reuse_a_cached_pass(self):
        from scp.models import parse_s3d, pack_s3d
        recipe = 'hsr_component_upper_paired_straight'
        spec, original = spec_for(recipe), self.fixture(recipe)
        first = check_models(original, spec)
        first.pop('texture_ids')
        self.assertIn('texture_ids', check_models(original, spec))
        changed = dict(original)
        for key, raw in list(changed.items()):
            if key[:2] != S3D:
                continue
            model = parse_s3d(raw)
            for vb in model['vertices']:
                data = bytearray(vb['data'])
                for offset in range(0, len(data), vb['stride']):
                    u = struct.unpack_from('<f', data, offset+12)[0]
                    struct.pack_into('<f', data, offset+12, u+.1)
                vb['data'] = bytes(data)
            changed[key] = pack_s3d(model)
        with self.assertRaisesRegex(ValueError, 'rail band'):
            check_models(changed, spec)


if __name__ == '__main__':
    unittest.main()
