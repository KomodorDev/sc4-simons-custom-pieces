"""Native diagonal joins and independent full-model regression tests."""
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
from scp_hsr.directional_diagonal_t import (
    RECIPE, INFO, directional_layout, build_rules, build_directional,
)
from scp_hsr.directional_diagonal_t_verify import (
    CONTRACTS, PATH, S3D, _cached_models, audit_bed_union, audit_visible_rails,
    check_paths, check_models, check_construction_fields,
)
from scp_hsr.interchange_verify import _bed
from scp.models import parse_s3d, pack_s3d
from scp.track_paths import encode_paths
from scp.recipes import combine_meshes
from scp_hsr.rail_feature_verify import _rail_u
from scp.verify import parse_paths, parse_rules


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


class DirectionalDiagonalTVerifierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        contract = CONTRACTS[RECIPE]
        cls.spec = {'recipe': RECIPE, 'name': 'HSR Smooth Diagonal Full T — At Grade',
                    'footprint': [13, 14], 'cells': [list(cell) for cell in contract['cells']],
                    'tile_ids': [f'{0x7f900000+0x100*x+0x10*row:08x}' for x, row in contract['cells']],
                    'preview_id': '7f900ff5', 'puzzle_id': 'f8ff',
                    'effect_name': 'preview_scp_test_0000000000'}
        layout = directional_layout()
        cls.paths = {(*PATH, int(tile, 16)): encode_paths(layout[cell]['routes'])
                     for tile, cell in zip(cls.spec['tile_ids'], contract['cells'])}
        cls.models, cls.donors = None, None
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

    def test_literal_diagonal_offsets_six_journeys_and_four_proper_rotations(self):
        contract = CONTRACTS[RECIPE]
        self.assertEqual(set(INFO), {RECIPE})
        self.assertEqual(INFO[RECIPE]['cells'], contract['cells'])
        self.assertEqual(contract['ports'], {
            'Nin': (173.1, 8., 15.5), 'Nout': (178.9, 8., 15.5),
            'Sin': (-8., -178.9, 15.5), 'Sout': (-8., -173.2, 15.5),
            'Ein': (184., -189.1, 15.5), 'Eout': (184., -194.9, 15.5)})
        report = check_paths(self.paths, self.spec)
        self.assertEqual(report['tile_count'], 42)
        self.assertEqual(report['permitted_movements_checked'], 6)
        self.assertEqual(report['unique_complete_journeys_checked'], 6)
        self.assertEqual(report['rotations_checked'], 4)
        self.assertEqual(report['native_facing_port_tangents_checked'], 6)
        self.assertEqual(report['declared_at_grade_conflicts_checked'], 3)
        self.assertFalse(report['collision_free_operation_claimed'])
        self.assertTrue(report['all_encoded_tracks_used_by_intended_journeys'])
        for quality in report['journey_quality'].values():
            self.assertLessEqual(quality['length_ratio'], 1.55)
            if quality['minimum_sampled_radius_m'] is not None:
                self.assertGreaterEqual(quality['minimum_sampled_radius_m'], 24.)
            if quality['minimum_resolved_raw_radius_m'] is not None:
                self.assertGreaterEqual(quality['minimum_resolved_raw_radius_m'], 24.)

    def test_missing_reversed_crosslevel_and_wrong_asymmetric_ports_are_rejected(self):
        # Mutation coordinates refer to decoded PATH, not to model labels.
        key = *PATH, int(self.spec['tile_ids'][0], 16)
        original = parse_paths(self.paths[key])['routes']
        mutations = []
        mutations.append(original[1:])
        reversed_route = deepcopy(original)
        reversed_route[0]['points'].reverse()
        reversed_route[0]['entry'], reversed_route[0]['exit'] = (
            reversed_route[0]['exit'], reversed_route[0]['entry'])
        mutations.append(reversed_route)
        crosslevel = deepcopy(original)
        x, y, _ = crosslevel[0]['points'][0]
        crosslevel[0]['points'][0] = (x, y, 1.)
        mutations.append(crosslevel)
        southwest_index = self.spec['cells'].index([0, 11])
        southwest_key = *PATH, int(self.spec['tile_ids'][southwest_index], 16)
        offset = deepcopy(parse_paths(self.paths[southwest_key])['routes'])
        changed = False
        for route in offset:
            for index in (0, -1):
                x, y, h = route['points'][index]
                if abs(x+8.) < 1e-6 and abs(y-2.8) < 1e-6:
                    route['points'][index] = (x, 2.9, h)
                    changed = True
        self.assertTrue(changed)
        for index, routes in enumerate(mutations):
            with self.subTest(mutation=index):
                resources = dict(self.paths)
                resources[key] = _encode(routes)
                with self.assertRaises(ValueError):
                    check_paths(resources, self.spec)
        resources = dict(self.paths)
        resources[southwest_key] = _encode(offset)
        with self.assertRaises(ValueError):
            check_paths(resources, self.spec)

    def test_native_diagonal_endpoint_without_diagonal_tangent_is_rejected(self):
        northeast_index = self.spec['cells'].index([11, 0])
        key = *PATH, int(self.spec['tile_ids'][northeast_index], 16)
        routes = deepcopy(parse_paths(self.paths[key])['routes'])
        candidate = next(route for route in routes
                         if abs(route['points'][0][0]+2.9) < 1e-6 and
                         abs(route['points'][0][1]-8.) < 1e-6)
        x, y, height = candidate['points'][1]
        candidate['points'][1] = (x, y+.2, height)
        changed = dict(self.paths)
        changed[key] = _encode(routes)
        with self.assertRaisesRegex(ValueError, 'literal native-facing tangent'):
            check_paths(changed, self.spec)

    def test_construction_palette_must_preserve_native_diagonal_categories(self):
        _, rules = parse_rules(build_rules(self.spec))
        fields = defaultdict(list)
        for key, value in rules[int(self.spec['puzzle_id'], 16)]:
            fields[key].append(value)
        report = check_construction_fields(fields, self.spec, self.paths)
        self.assertEqual(report['occupied_cells_checked'], 42)
        self.assertEqual(report['native_external_edge_categories_checked'], 6)
        changed = deepcopy(fields)
        # Replacing every diagonal category with cardinal2 keeps edge presence
        # intact but must fail the independent actual-heading comparison.
        for index, value in enumerate(changed['CheckType']):
            label, encoded = value.split('0x')
            flag = int(encoded, 16)
            cardinal = sum((2 if (flag >> (8*edge)) & 255 else 0) << (8*edge)
                           for edge in range(4))
            changed['CheckType'][index] = label+f'0x{cardinal:08X}'
        with self.assertRaisesRegex(ValueError, 'construction edge heading'):
            check_construction_fields(changed, self.spec, self.paths)

    def test_external_native_plane_clipping_never_masks_a_nearby_interior_hole(self):
        contract = CONTRACTS[RECIPE]
        records = [((11, 0), {}, [(173.1, 8., 15.5), (169.1, 4., 15.5)])]
        report = audit_bed_union(_floor(166., 180., -8., 0.), records, contract)
        self.assertEqual(report['native_external_port_corridor_segments_clipped'], 1)
        self.assertEqual(report['bed_union_width_m'], 5.)
        with self.assertRaisesRegex(ValueError, 'substantive coplanar.*overlap'):
            audit_bed_union(_floor(166., 180., -8., 0.)*2, records, contract)
        # This0.02m² void lies inside the corridor,1m behind the join plane.
        floor = (_floor(166., 172., -8., 0.)+_floor(172.1, 180., -8., 0.)+
                 _floor(172., 172.1, -8., -6.9)+_floor(172., 172.1, -6.7, 0.))
        with self.assertRaisesRegex(ValueError, 'hole.*rail bed'):
            audit_bed_union(floor, records, contract)
        # A nearby undeclared endpoint receives no plane-clipping exception.
        interior = [((11, 0), {}, [(173., 7.9, 15.5), (169.1, 4., 15.5)])]
        with self.assertRaisesRegex(ValueError, 'hole.*rail bed'):
            audit_bed_union(_floor(166., 180., -8., 0.), interior, contract)

    def test_native_ribbon_cap_requires_exact_port_and_rejects_unused_nearby_rail(self):
        contract = CONTRACTS[RECIPE]
        root = contract['ports']['Nout']
        unit = 1./math.sqrt(2.)
        def vertex(along, across, rail_across=None):
            return (root[0]+unit*(along-across), _bed(15.5),
                    -root[1]-unit*(along+across),
                    _rail_u(2.+(across if rail_across is None else rail_across)), 0.)
        a, b, c, d = (vertex(-4., -1.), vertex(-4., 1.),
                      vertex(-2., 1.), vertex(-2., -1.))
        base = [(a, b, c), (a, c, d)]
        # This outer ribbon corner is within the north-cut face. Its rail
        # centre remains the actual PATH endpoint; its outer edge projects
        # beyond that point along the native45-degree tangent.
        corner = (vertex(.8, -1.), vertex(.9, -.9), vertex(1., -1.))
        records = [((11, 0), {}, [(root[0]-6.*unit, root[1]-6.*unit, 15.5), root])]
        report = audit_visible_rails(base+[corner], records, contract)
        self.assertEqual(report['native_external_cap_stripe_matches'], 1)
        self.assertTrue(report['native_external_rail_centres_clamped_to_actual_paths'])
        self.assertEqual(report['native_external_cap_rail_centre_matches'], 0)
        # No exact endpoint, no analytic-cap ownership.
        near = [((11, 0), {}, [records[0][2][0], (root[0]-.1, root[1]-.1, 15.5)])]
        with self.assertRaisesRegex(ValueError, 'visible native rail stripe'):
            audit_visible_rails(base+[corner], near, contract)
        offset = (vertex(.8, -1.5, -1.), vertex(.9, -1.4, -.9), vertex(1., -1.5, -1.))
        with self.assertRaisesRegex(ValueError, 'visible native rail stripe'):
            audit_visible_rails(base+[offset], records, contract)
        # A fake rail-centre line near the native join must still match an
        # actual used PATH within0.25m; the stripe exception cannot hide it.
        unused = (vertex(.3, -.5, 0.), vertex(.4, -.5, 0.), vertex(.3, -.6, 0.))
        with self.assertRaisesRegex(ValueError, 'rail centre.*no matching'):
            audit_visible_rails(base+[unused], records, contract)

    def test_actual_model_has_complete_clear_corridors_and_37_consolidated_piers(self):
        report = check_models(self.fixture(), self.spec)
        self.assertEqual(report['models_checked'], 211)
        self.assertEqual(report['authored_clearance_width_m'], 5.)
        self.assertEqual(report['authored_clearance_height_m'], 5.)
        self.assertTrue(report['preview_matches_tiles'])
        self.assertEqual(report['support_columns_checked'], 37)
        self.assertEqual(report['support_contact_points_checked'], 333)
        self.assertEqual(report['minimum_support_centre_distance_m'], 16.)
        self.assertTrue(report['support_foundations_within_reserved_cells'])
        self.assertTrue(report['support_tops_touch_deck'])
        self.assertFalse(report['unused_visible_native_rails'])
        self.assertGreater(report['visible_native_rail_centre_segments_matched_to_paths'], 0)
        self.assertGreaterEqual(report['native_external_port_corridor_segments_clipped'], 6)

    def test_crosscell_duplicate_pier_is_rejected_even_with_rebuilt_preview(self):
        resources = dict(self.fixture())
        source = parse_s3d(resources[*S3D, int(self.spec['tile_ids'][0], 16)])
        support = [mesh for mesh in source['meshes'] if b'consolidated directional' in mesh['name']]
        self.assertEqual(len(support), 1)
        target = parse_s3d(resources[*S3D, int(self.spec['tile_ids'][1], 16)])
        a, b = self.spec['cells'][:2]
        model = combine_meshes([(target, target['meshes'], (0., 0., 0.)),
                               (source, support, (16.*(a[0]-b[0]), 0., 16.*(a[1]-b[1])))])
        self._replace(resources, 1, model)
        with self.assertRaisesRegex(ValueError, 'Overlapping|duplicate support'):
            check_models(resources, self.spec)

    def test_preview_mismatch_and_changed_path_bytes_cannot_reuse_a_model_pass(self):
        resources = self.fixture()
        first = check_models(resources, self.spec)
        first.pop('texture_ids')
        self.assertIn('texture_ids', check_models(resources, self.spec))
        self.assertEqual(_cached_models.cache_info().maxsize, 8)
        changed = dict(resources)
        key = *S3D, int(self.spec['preview_id'], 16)
        preview = parse_s3d(changed[key])
        data = bytearray(preview['vertices'][0]['data'])
        struct.pack_into('<f', data, 0, struct.unpack_from('<f', data, 0)[0]+1.)
        preview['vertices'][0]['data'] = bytes(data)
        changed[key] = pack_s3d(preview)
        with self.assertRaisesRegex(ValueError, 'preview differs'):
            check_models(changed, self.spec)
        changed = dict(resources)
        key = *PATH, int(self.spec['tile_ids'][0], 16)
        routes = deepcopy(parse_paths(changed[key])['routes'])
        x, y, height = routes[0]['points'][1]
        routes[0]['points'][1] = (x, y, height+.1)
        changed[key] = _encode(routes)
        with self.assertRaisesRegex(ValueError, 'grade|height'):
            check_models(changed, self.spec)


if __name__ == '__main__':
    unittest.main()
