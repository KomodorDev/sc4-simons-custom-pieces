"""Independent topology, design-quality, rail-union and support regressions."""
from __future__ import annotations

from collections import defaultdict
from copy import deepcopy
import json
import math
from pathlib import Path
import struct
import sys
import unittest

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp import jsonc
from scp.paths import local_settings
from scp.dbpf import entries, decompress
from scp_hsr.directional_t import INFO, directional_layout, build_rules, build_directional
from scp_hsr.directional_t_verify import (
    CONTRACTS, S3D, PATH, _TURN_LIMITS, _cached_models, _journeys,
    measure_route_quality, audit_bed_union, audit_visible_rails,
    _polygon_union_area,
    check_paths, check_models, check_construction_fields,
)
from scp_hsr.interchange_verify import _encoded_routes, _bed
from scp.models import parse_s3d, pack_s3d
from scp_hsr.rail_feature_verify import _rail_u
from scp.track_paths import encode_paths
from scp.recipes import combine_meshes
from scp.verify import parse_paths, parse_rules

RECIPE = 'directional_hsr_t_smooth_at_grade'


def _encode(routes):
    lines = ['SC4PATHS', '1.2', str(len(routes)), '0', '0']
    for route in routes:
        lines += [str(route[key]) for key in ('transport', 'lane', 'entry', 'exit', 'compatibility')]
        lines += [str(len(route['points']))]
        lines += [','.join(format(value, '.12g') for value in point) for point in route['points']]
    return ('\r\n'.join(lines)+'\r\n').encode()


def _floor(x0, x1, z0, z1):
    height = _bed(15.5)
    a, b, c, d = ((x0, height, z0, .61, 0.), (x1, height, z0, .61, 0.),
                  (x1, height, z1, .61, 0.), (x0, height, z1, .61, 0.))
    return [(a, b, c), (a, c, d)]


def _circle(radius, samples=256):
    return [(radius*math.sin(t), radius*(1.-math.cos(t)), 15.5)
            for t in (math.pi/2.*index/samples for index in range(samples+1))]


class DirectionalTVerifierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        contract = CONTRACTS[RECIPE]
        cls.spec = {'recipe': RECIPE, 'name': 'HSR Smooth Full T — At Grade',
                    'footprint': [7, 11], 'cells': [list(cell) for cell in contract['cells']],
                    'tile_ids': [f'{0x7f900000+0x100*x+0x10*row:08x}' for x, row in contract['cells']],
                    'preview_id': '7f900ff5', 'puzzle_id': 'f8ff',
                    'effect_name': 'preview_scp_test_0000000000'}
        assert len(cls.spec['effect_name']) == 27
        layout = directional_layout()
        cls.paths = {(*PATH, int(tile, 16)): encode_paths(layout[cell]['routes'])
                     for tile, cell in zip(cls.spec['tile_ids'], contract['cells'])}
        cls.models = None
        cls.donors = None
        if local_settings(ROOT).is_file():
            plugins = Path(jsonc.load(local_settings(ROOT))['plugins'])
            candidates = list(plugins.rglob('High Speed Rail.dat'))
            if len(candidates) == 1:
                cls.donors = {key: decompress(raw) for key, raw in entries(candidates[0].read_bytes()).items()}

    @classmethod
    def fixture(cls):
        if cls.donors is None:
            raise unittest.SkipTest('Audited local HSR native donor unavailable')
        if cls.models is None:
            cls.models = build_directional(cls.spec, {'hsr': cls.donors})[0]
        return cls.models

    def _preview(self, resources):
        parts = []
        for (x, row), tile in zip(self.spec['cells'], self.spec['tile_ids']):
            model = parse_s3d(resources[*S3D, int(tile, 16)])
            parts.append((model, model['meshes'], (16.*x, 0., 16.*row)))
        resources[*S3D, int(self.spec['preview_id'], 16)] = pack_s3d(combine_meshes(parts))

    def _replace(self, resources, index, model):
        raw = pack_s3d(model)
        tile = int(self.spec['tile_ids'][index], 16)
        for zoom in range(5):
            resources[*S3D, tile+zoom] = raw
        self._preview(resources)

    def test_literal_ports_six_unique_journeys_and_all_proper_rotations(self):
        self.assertEqual(set(INFO), {RECIPE})
        self.assertEqual(INFO[RECIPE]['cells'], CONTRACTS[RECIPE]['cells'])
        report = check_paths(self.paths, self.spec)
        self.assertEqual(report['permitted_movements_checked'], 6)
        self.assertEqual(report['unique_complete_journeys_checked'], 6)
        self.assertEqual(report['rotations_checked'], 4)
        self.assertEqual(report['native_facing_port_tangents_checked'], 6)
        self.assertTrue(report['all_encoded_tracks_used_by_intended_journeys'])
        self.assertFalse(report['unwanted_u_turns'])
        self.assertEqual(report['declared_at_grade_conflicts_checked'], 3)
        self.assertEqual(report['grade_separated_crossings_checked'], 0)
        self.assertFalse(report['collision_free_operation_claimed'])
        for movement, quality in report['journey_quality'].items():
            if movement in ('Nin>Sout', 'Sin>Nout'):
                self.assertEqual(quality['length_ratio'], 1.)
            else:
                self.assertLess(quality['length_ratio'], 1.22)
                self.assertGreater(quality['minimum_sampled_radius_m'], 47.)
                self.assertLess(abs(quality['total_turn_degrees']-90.), .001)

    def test_construction_uses_encoded_and_literal_native_headings(self):
        _, rules = parse_rules(build_rules(self.spec))
        fields = defaultdict(list)
        for key, value in rules[int(self.spec['puzzle_id'], 16)]:
            fields[key].append(value)
        report = check_construction_fields(fields, self.spec, self.paths)
        self.assertEqual(report['occupied_cells_checked'], 22)
        self.assertEqual(report['native_external_edge_categories_checked'], 6)

    def test_missing_reverse_and_crosslevel_routes_cannot_pass_the_matrix(self):
        tile = *PATH, int(self.spec['tile_ids'][0], 16)
        original = parse_paths(self.paths[tile])['routes']
        changed = deepcopy(self.paths)
        changed[tile] = _encode(original[1:])
        with self.assertRaises(ValueError):
            check_paths(changed, self.spec)
        routes = deepcopy(original)
        route = routes[0]
        route['points'].reverse()
        route['entry'], route['exit'] = route['exit'], route['entry']
        changed[tile] = _encode(routes)
        with self.assertRaises(ValueError):
            check_paths(changed, self.spec)
        routes = deepcopy(original)
        x, y, _ = routes[0]['points'][0]
        routes[0]['points'][0] = (x, y, 1.)
        changed[tile] = _encode(routes)
        with self.assertRaisesRegex(ValueError, 'grade|height'):
            check_paths(changed, self.spec)

    def test_redundant_alternative_is_rejected_even_with_the_same_external_matrix(self):
        records = _encoded_routes(self.paths, self.spec, CONTRACTS[RECIPE])
        cell, route, points = records[0]
        alternative = [points[0], ((points[0][0]+points[-1][0])/2.+.5,
                                   (points[0][1]+points[-1][1])/2., 15.5), points[-1]]
        with self.assertRaisesRegex(ValueError, 'ambiguous alternative'):
            _journeys(records+[(cell, route, alternative)], CONTRACTS[RECIPE])

    def test_long_rectangular_return_route_is_rejected(self):
        points = [(0., 0., 15.5), (0., -100., 15.5), (100., -100., 15.5),
                  (100., 100., 15.5), (0., 100., 15.5), (0., 80., 15.5)]
        with self.assertRaisesRegex(ValueError, 'excessive detour'):
            measure_route_quality(points, {**_TURN_LIMITS, 'max_raw_turn_degrees': 180.})

    def test_sub_two_metre_zigzag_cannot_hide_between_quality_samples(self):
        points = [(0., 0., 15.5), (49.9, 0., 15.5), (50., .2, 15.5),
                  (50.1, -.2, 15.5), (50.2, 0., 15.5), (100., 0., 15.5)]
        with self.assertRaisesRegex(ValueError, 'raw encoded tangent kink'):
            measure_route_quality(points, _TURN_LIMITS)
        # Micro-metre roundoff on a tiny straight grid cut is harmless.
        straight = [(0., 0., 15.5), (50., 0., 15.5),
                    (50.00001, .000001, 15.5), (100., 0., 15.5)]
        self.assertLess(measure_route_quality(straight, _TURN_LIMITS)['maximum_raw_encoded_turn_degrees'], .001)

    def test_densely_sampled_short_wave_cannot_evade_the_raw_angle_limit(self):
        points = [(0., 0., 15.5), (49., 0., 15.5)]
        headings = [*range(2, 12, 2), *range(8, -12, -2), *range(-8, 2, 2)]
        for angle in headings:
            x, y, height = points[-1]
            points.append((x+.01*math.cos(math.radians(angle)),
                           y+.01*math.sin(math.radians(angle)), height))
        points.append((100., 0., 15.5))
        with self.assertRaisesRegex(ValueError, 'tight raw encoded curve'):
            measure_route_quality(points, _TURN_LIMITS)

    def test_tight_radius_and_sharp_tangent_kink_are_rejected(self):
        limits = {**_TURN_LIMITS, 'max_sample_turn_degrees': 180.,
                   'max_endpoint_curvature_per_m': 1., 'max_raw_turn_degrees': 180.}
        with self.assertRaisesRegex(ValueError, 'undersized.*radius|tight raw encoded curve'):
            measure_route_quality(_circle(8.), limits)
        with self.assertRaisesRegex(ValueError, 'tangent kink'):
            measure_route_quality([(0., 0., 15.5), (50., 0., 15.5), (50., 50., 15.5)], _TURN_LIMITS)

    def test_curvature_must_ease_at_native_approaches_and_internal_joins(self):
        with self.assertRaisesRegex(ValueError, 'ease curvature continuously'):
            measure_route_quality(_circle(80.), _TURN_LIMITS)
        arc = _circle(80.)
        points = [(-30., 0., 15.5), *arc, (80., 110., 15.5)]
        with self.assertRaisesRegex(ValueError, 'curvature changes abruptly'):
            measure_route_quality(points, _TURN_LIMITS)

    def test_full_bed_union_rejects_a_hole_between_path_samples(self):
        records = [((0, 0), {}, [(0., 0., 15.5), (0., -10., 15.5)])]
        self.assertEqual(audit_bed_union(_floor(-2.5, 2.5, 0., 10.), records)[
            'full_width_bed_union_segments_checked'], 1)
        # A0.02m² void is away from both PATH endpoints and its centre line.
        floor = (_floor(-2.5, .9, 0., 10.)+_floor(1., 2.5, 0., 10.)+
                 _floor(.9, 1., 0., 4.2)+_floor(.9, 1., 4.4, 10.))
        with self.assertRaisesRegex(ValueError, 'hole.*rail bed'):
            audit_bed_union(floor, records)
        with self.assertRaisesRegex(ValueError, 'substantive coplanar.*overlap'):
            audit_bed_union(_floor(-2.5, 2.5, 0., 10.)*2, records)

    def test_exact_union_handles_three_coincident_floor_regions(self):
        rectangle = [(-2.5, 0.), (2.5, 0.), (2.5, 10.), (-2.5, 10.)]
        self.assertAlmostEqual(_polygon_union_area([rectangle]*3), 50., places=8)

    def test_unused_visible_rail_is_rejected(self):
        height = _bed(15.5)
        a, b, c, d = ((-1., height, 0., _rail_u(1.), 0.), (1., height, 0., _rail_u(3.), 0.),
                      (1., height, 10., _rail_u(3.), 1.), (-1., height, 10., _rail_u(1.), 1.))
        triangles = [(a, b, c), (a, c, d)]
        records = [((0, 0), {}, [(0., 0., 15.5), (0., -10., 15.5)])]
        self.assertEqual(audit_visible_rails(triangles, records)[
            'visible_native_rail_centre_segments_matched_to_paths'], 2)
        stray = [tuple((p[0]+4., *p[1:]) for p in triangle) for triangle in triangles]
        with self.assertRaisesRegex(ValueError, 'visible native rail.*no used train PATH'):
            audit_visible_rails(triangles+stray, records)

    def test_actual_models_have_five_metre_clearance_complete_bed_and_supported_decks(self):
        report = check_models(self.fixture(), self.spec)
        self.assertEqual(report['authored_clearance_width_m'], 5.)
        self.assertEqual(report['authored_clearance_height_m'], 5.)
        self.assertEqual(report['support_columns_checked'], 18)
        self.assertEqual(report['support_contact_points_checked'], 162)
        self.assertEqual(report['minimum_support_centre_distance_m'], 16.)
        self.assertTrue(report['support_foundations_within_reserved_cells'])
        self.assertTrue(report['support_tops_touch_deck'])
        self.assertFalse(report['unused_visible_native_rails'])
        self.assertGreater(report['full_width_bed_union_segments_checked'], 0)
        self.assertGreater(report['visible_native_rail_centre_segments_matched_to_paths'], 0)

    def test_crosscell_duplicate_pier_is_rejected_with_matching_preview(self):
        resources = deepcopy(self.fixture())
        first = parse_s3d(resources[*S3D, int(self.spec['tile_ids'][0], 16)])
        support = [mesh for mesh in first['meshes'] if b'consolidated directional' in mesh['name']]
        self.assertEqual(len(support), 1)
        next_model = parse_s3d(resources[*S3D, int(self.spec['tile_ids'][1], 16)])
        model = combine_meshes([(next_model, next_model['meshes'], (0., 0., 0.)),
                                (first, support, (0., 0., -16.))])
        self._replace(resources, 1, model)
        with self.assertRaisesRegex(ValueError, 'Overlapping|duplicate support'):
            check_models(resources, self.spec)

    def test_actual_duplicate_floor_faces_are_rejected_with_matching_preview(self):
        resources = deepcopy(self.fixture())
        model = parse_s3d(resources[*S3D, int(self.spec['tile_ids'][0], 16)])
        deck = [mesh for mesh in model['meshes'] if b'consolidated directional' not in mesh['name']]
        doubled = combine_meshes([(model, model['meshes'], (0., 0., 0.)),
                                  (model, deck, (0., 0., 0.))])
        self._replace(resources, 0, doubled)
        with self.assertRaisesRegex(ValueError, 'substantive coplanar.*overlap'):
            check_models(resources, self.spec)

    def test_changed_uv_invalidates_cached_model_pass_and_reports_are_fresh(self):
        resources = self.fixture()
        report = check_models(resources, self.spec)
        report.pop('texture_ids')
        self.assertIn('texture_ids', check_models(resources, self.spec))
        self.assertEqual(_cached_models.cache_info().maxsize, 8)
        changed = deepcopy(resources)
        for key, raw in list(changed.items()):
            if key[:2] != S3D:
                continue
            model = parse_s3d(raw)
            for buffer in model['vertices']:
                data = bytearray(buffer['data'])
                for offset in range(0, len(data), buffer['stride']):
                    struct.pack_into('<f', data, offset+12, struct.unpack_from('<f', data, offset+12)[0]+.1)
                buffer['data'] = bytes(data)
            changed[key] = pack_s3d(model)
        with self.assertRaisesRegex(ValueError, 'native rail band'):
            check_models(changed, self.spec)


if __name__ == '__main__':
    unittest.main()
