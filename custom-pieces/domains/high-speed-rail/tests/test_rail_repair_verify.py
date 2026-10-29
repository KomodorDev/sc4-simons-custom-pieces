"""Independent corrected-junction routing, clearance and global pier tests."""
from __future__ import annotations

from collections import defaultdict
from copy import deepcopy
import json
from pathlib import Path
import struct
import sys
import unittest

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp import jsonc
from scp.paths import local_settings
from scp.dbpf import entries, decompress
from scp.catalog import load_catalog
from scp.models import parse_s3d, pack_s3d
from scp_hsr.rail_repairs import INFO, repair_layout, build_repair, build_rules
from scp_hsr.rail_repair_verify import (
    CONTRACTS, PATH, S3D, audit_supports, check_paths, check_models,
    check_construction_fields, _cached_models,
)
from scp_hsr.interchange_verify import _clearance_segments, _bed
from scp.track_paths import encode_paths
from scp.recipes import combine_meshes
from scp.verify import parse_paths, parse_rules


def _box(x, z, top):
    """Literal1.3m square column, independent of the geometry writer."""
    vertices = [(x+dx, y, z+dz, .61, 0.) for y in (0., top)
                for dx, dz in ((-.65, -.65), (.65, -.65), (.65, .65), (-.65, .65))]
    return [tuple(vertices[i] for i in indices)
            for face in ((0, 3, 2, 1), (4, 5, 6, 7), (0, 1, 5, 4),
                         (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7))
            for indices in ((face[0], face[1], face[2]), (face[0], face[2], face[3]))]


def _roof(height=14.01067):
    a, b, c, d = ((-8., height, -8., .61, 0.), (24., height, -8., .61, 0.),
                  (24., height, 40., .61, 0.), (-8., height, 40., .61, 0.))
    return [(a, b, c), (a, c, d)]


def _encode(routes):
    lines = ['SC4PATHS', '1.2', str(len(routes)), '0', '0']
    for route in routes:
        lines += [str(route[k]) for k in ('transport', 'lane', 'entry', 'exit', 'compatibility')]
        lines += [str(len(route['points']))]
        lines += [','.join(format(v, '.12g') for v in point) for point in route['points']]
    return ('\r\n'.join(lines)+'\r\n').encode()


class RailRepairVerifierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.specs, cls.paths, cls.models = {}, {}, {}
        for piece in load_catalog(ROOT)['pieces']:
            if piece['recipe'] not in CONTRACTS:
                continue
            recipe = piece['recipe']
            cls.specs[recipe] = piece
            layout = repair_layout(recipe)
            cls.paths[recipe] = {(*PATH, int(tile, 16)): encode_paths(layout[tuple(cell)]['routes'])
                                 for cell, tile in zip(piece['cells'], piece['tile_ids'])}
        cls.donors = None
        local = local_settings(ROOT)
        if local.exists():
            candidates = list(Path(jsonc.load(local)['plugins']).rglob('High Speed Rail.dat'))
            if len(candidates) == 1:
                cls.donors = {k: decompress(v) for k, v in entries(candidates[0].read_bytes()).items()}

    @classmethod
    def fixture(cls, recipe):
        if cls.donors is None:
            raise unittest.SkipTest('Audited local native HSR donor unavailable')
        if recipe not in cls.models:
            cls.models[recipe] = build_repair(cls.specs[recipe], {'hsr': cls.donors})[0]
        return cls.models[recipe]

    def preview(self, resources, spec):
        parts = []
        for (x, row), tile in zip(spec['cells'], spec['tile_ids']):
            model = parse_s3d(resources[*S3D, int(tile, 16)])
            parts.append((model, model['meshes'], (16.*x, 0., 16.*row)))
        resources[*S3D, int(spec['preview_id'], 16)] = pack_s3d(combine_meshes(parts))

    def replace_model(self, resources, spec, index, model):
        tile = int(spec['tile_ids'][index], 16)
        raw = pack_s3d(model)
        for zoom in range(5):
            resources[*S3D, tile+zoom] = raw
        self.preview(resources, spec)

    def test_both_literal_port_matrices_and_rotations(self):
        self.assertEqual(set(INFO), set(CONTRACTS))
        self.assertEqual(set(self.specs), set(CONTRACTS))
        for recipe, spec in self.specs.items():
            with self.subTest(recipe=recipe):
                report = check_paths(self.paths[recipe], spec)
                self.assertEqual(report['rotations_checked'], 4)
                self.assertEqual(report['permitted_movements_checked'], 8)
                self.assertFalse(report['unwanted_u_turns'])

    def test_construction_matches_literal_native_ports(self):
        for recipe, spec in self.specs.items():
            _, rules = parse_rules(build_rules(spec))
            fields = defaultdict(list)
            for key, value in rules[int(spec['puzzle_id'], 16)]:
                fields[key].append(value)
            report = check_construction_fields(fields, spec, self.paths[recipe])
            self.assertEqual(report['native_external_edge_categories_checked'], len(CONTRACTS[recipe]['ports']))

    def test_missing_route_and_crosslevel_mutations_are_rejected(self):
        recipe = 'rail_hsr_adjacent_scissors_revised'
        spec = self.specs[recipe]
        tile = *PATH, int(spec['tile_ids'][0], 16)
        routes = parse_paths(self.paths[recipe][tile])['routes']
        resources = deepcopy(self.paths[recipe])
        resources[tile] = _encode(routes[1:])
        with self.assertRaises(ValueError):
            check_paths(resources, spec)
        x, y, _ = routes[0]['points'][0]
        routes[0]['points'][0] = (x, y, 1.)
        resources[tile] = _encode(routes)
        with self.assertRaisesRegex(ValueError, 'height|grade'):
            check_paths(resources, spec)

    def test_literal_six_pier_plan_has_nine_roof_contacts_per_column(self):
        contract = CONTRACTS['rail_hsr_adjacent_scissors_revised']
        triangles = _roof()+[tri for centre in contract['support_centres_xz'] for tri in _box(*centre, 14.01067)]
        report = audit_supports(triangles, contract)
        self.assertEqual(report['support_columns_checked'], 6)
        self.assertEqual(report['support_contact_points_checked'], 54)
        self.assertEqual(report['minimum_support_centre_distance_m'], 16.)

    def test_global_foundation_overlap_and_near_duplicates_are_rejected(self):
        contract = CONTRACTS['rail_hsr_adjacent_scissors_revised']
        triangles = _roof()+[tri for centre in contract['support_centres_xz'] for tri in _box(*centre, 14.01067)]
        # The duplicate could come from a different cell model; the check sees
        # their assembled world coordinates, where both foundations coincide.
        with self.assertRaisesRegex(ValueError, 'Overlapping|duplicate'):
            audit_supports(triangles+_box(0., 0., 14.01067), contract)
        with self.assertRaisesRegex(ValueError, 'too close'):
            audit_supports(triangles+_box(2., 0., 14.01067), contract)

    def test_short_or_missing_supports_cannot_avoid_duplication_check(self):
        contract = CONTRACTS['rail_hsr_adjacent_scissors_revised']
        triangles = _roof()+[tri for centre in contract['support_centres_xz'] for tri in _box(*centre, 10.)]
        with self.assertRaisesRegex(ValueError, 'floating|underside'):
            audit_supports(triangles, contract)
        with self.assertRaisesRegex(ValueError, 'no support foundations'):
            audit_supports(_roof(), contract)

    def test_five_metre_corridor_rejects_an_obstruction_missed_by_three_metres(self):
        height = _bed(15.5)
        wall = ((2., height+.3, -.5, .61, 0.), (2., height+.7, -.5, .61, 0.),
                (2., height+.7, .5, .61, 0.))
        records = [((0, 0), {}, [(0., -1., 15.5), (0., 1., 15.5)])]
        buckets = defaultdict(lambda: [wall])
        self.assertEqual(_clearance_segments(records, buckets, half_width=1.5), 1)
        with self.assertRaisesRegex(ValueError, 'clearance envelope'):
            _clearance_segments(records, buckets, half_width=2.5)

    def test_all_actual_revised_models_have_wide_clearance_and_consolidated_supports(self):
        for recipe, spec in self.specs.items():
            with self.subTest(recipe=recipe):
                report = check_models(self.fixture(recipe), spec)
                self.assertEqual(report['authored_clearance_width_m'], 5.)
                self.assertEqual(report['authored_clearance_height_m'], 5.)
                expected = 0 if recipe.startswith('rail_ghsr_') else 6
                self.assertEqual(report['support_columns_checked'], expected)
                self.assertEqual(report['support_contact_points_checked'], 9*expected)
                self.assertGreater(report['train_clearance_segments_checked'], 0)
                self.assertGreater(report['path_nodes_covered_by_visible_bed'], 0)

    def test_actual_crosscell_duplicate_pier_with_matching_preview_is_rejected(self):
        recipe = 'rail_hsr_adjacent_scissors_revised'
        spec = self.specs[recipe]
        resources = deepcopy(self.fixture(recipe))
        source = parse_s3d(resources[*S3D, int(spec['tile_ids'][0], 16)])
        support = [mesh for mesh in source['meshes'] if b'consolidated' in mesh['name']]
        self.assertEqual(len(support), 1)
        target = parse_s3d(resources[*S3D, int(spec['tile_ids'][1], 16)])
        # Cell1 is one column east. Local x=-16 puts its duplicate support on
        # top of cell0's pier after placement, beyond a per-cell-only check.
        changed = combine_meshes([(target, target['meshes'], (0., 0., 0.)),
                                  (source, support, (-16., 0., 0.))])
        self.replace_model(resources, spec, 1, changed)
        with self.assertRaisesRegex(ValueError, 'Overlapping|duplicate support'):
            check_models(resources, spec)

    def test_actual_shortened_pier_with_matching_preview_is_rejected(self):
        recipe = 'rail_hsr_adjacent_scissors_revised'
        spec = self.specs[recipe]
        resources = deepcopy(self.fixture(recipe))
        model = parse_s3d(resources[*S3D, int(spec['tile_ids'][0], 16)])
        mesh = next(mesh for mesh in model['meshes'] if b'consolidated' in mesh['name'])
        vb = model['vertices'][mesh['frames'][0][0]]
        data = bytearray(vb['data'])
        for offset in range(0, len(data), vb['stride']):
            y = struct.unpack_from('<f', data, offset+4)[0]
            struct.pack_into('<f', data, offset+4, min(y, 10.))
        vb['data'] = bytes(data)
        self.replace_model(resources, spec, 0, model)
        with self.assertRaisesRegex(ValueError, 'floating|underside'):
            check_models(resources, spec)

    def test_changed_uv_and_cached_report_mutation_do_not_reuse_a_pass(self):
        recipe = 'rail_ghsr_adjacent_scissors_revised'
        spec = self.specs[recipe]
        resources = self.fixture(recipe)
        report = check_models(resources, spec)
        report.pop('texture_ids')
        self.assertIn('texture_ids', check_models(resources, spec))
        self.assertEqual(_cached_models.cache_info().maxsize, 32)
        changed = deepcopy(resources)
        for key in changed:
            if key[:2] != S3D:
                continue
            model = parse_s3d(changed[key])
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
