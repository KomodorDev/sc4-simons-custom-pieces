"""Mutate saved runtime layers without bypassing the independent domain checks."""
from copy import deepcopy
import hashlib
from pathlib import Path
import struct
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp import adaptive_network
from scp.dbpf import encode_exemplar, exemplar, pack_dbpf
from scp.models import pack_s3d, parse_s3d
from scp.track_paths import PATH, S3D
from scp.verify import parse_paths as saved_paths, strict_dbpf
from scp_highway import adaptive_ground as writer, adaptive_verify as verify
from scp_highway.native import encode_paths
import test_adaptive_ground as fixture


def parse_paths(raw):
    # Runtime aliases may opt into header 1; the native donor parser is
    # intentionally restricted to the original header-0 donor resources.
    return saved_paths(raw)['routes']


def literal_routes():
    result = fixture.routes()
    result.append(dict(transport=1, lane=3, entry=1, exit=3, compatibility=1,
                       points=[(1.125, -8.0, 0.0), (0.25, -.5, 0.0), (1.125, 8.0, 0.0)]))
    return result


def quarter_turn(point, turns):
    east, north, height = point
    east, north = ((east, north), (north, -east), (-east, -north), (-north, east))[turns % 4]
    return east, north, height


def encode_active_routes(routes):
    # Mutate route content without accidentally testing the separate header
    # guard instead. The selected current fixture explicitly opts into 1.
    return encode_paths(routes).replace(b'\r\n0\r\n0\r\n', b'\r\n0\r\n1\r\n', 1)


def saved_fixture(piece):
    bindings = {tuple(row['cell']): row for row in adaptive_network.bindings(piece)}
    compiled = []
    for cell, raw, path in fixture.compiled(piece):
        row = bindings.get(cell)
        if row:
            path = encode_paths(literal_routes())
            if row['prop']:
                source = parse_s3d(raw)
                from scp.recipes import combine_meshes
                deck = fixture.model_mesh(b'Elevated deck\0', 0x5713000E, 15.0)
                support = fixture.model_mesh(b'Centre support\0', 0x5EB4BEEE)
                vb = bytearray(support['vertices'][0]['data'])
                struct.pack_into('<f', vb, 20 + 4, 15.0)
                support['vertices'][0]['data'] = bytes(vb)
                raw = pack_s3d(combine_meshes([(model, model['meshes'], (0.0, 0.0, 0.0))
                                             for model in (source, deck, support)]))
        compiled.append((cell, raw, path))
    capture = fixture.capture()
    resources = writer.build_resources(piece, {'adaptive_avenue': capture}, compiled)
    for cell, raw, path in compiled:
        tile = int(piece['tile_ids'][piece['cells'].index(list(cell))], 16)
        resources[*S3D, tile] = raw
        resources[*PATH, tile] = path
    # Only the synthetic texture identities replace the native audit hashes.
    hashes = {key: hashlib.sha256(raw).hexdigest() for key, raw in capture.items()
              if key[:2] == verify.TEXTURE}
    return strict_dbpf(pack_dbpf(resources)), hashes


def change_property(resources, key, identifier, transform):
    record = exemplar(resources[key])
    prop = next(row for row in record['properties'] if int(row['id'], 16) == identifier)
    transform(prop)
    resources[key] = encode_exemplar(record)


class AdaptiveGroundVerifierTests(unittest.TestCase):
    def setUp(self):
        self.piece = fixture.spec('access-core')
        self.resources, self.hashes = saved_fixture(self.piece)
        self.rows = adaptive_network.bindings(self.piece)
        self.row = next(row for row in self.rows if row['prop'])

    def check(self, resources=None, piece=None, hashes=None):
        # Inspect serialized DAT bytes after each mutation, not an in-memory
        # model or manifest whose new hashes could hide the changed resource.
        saved = strict_dbpf(pack_dbpf(self.resources if resources is None else resources))
        with patch.object(verify, '_texture_hashes', return_value=self.hashes if hashes is None else hashes):
            return verify.check_resources(saved, self.piece if piece is None else piece)

    def test_all_three_modules_preserve_every_runtime_route_and_retained_mesh(self):
        cells = props = routes = 0
        for key in ('access-core', 'northwest-junction', 'southeast-junction'):
            piece = fixture.spec(key)
            resources, hashes = saved_fixture(piece)
            report = self.check(resources, piece, hashes)
            self.assertTrue(report['canonical_geometry_and_traffic_preserved'])
            self.assertEqual(report['proper_rotations_checked'], 4)
            self.assertFalse(report['game_behavior_tested'])
            self.assertEqual(report['texture_resources_checked'], 20 * report['adaptive_cells_checked'])
            self.assertEqual(report['retained_meshes_checked'], 3 * report['props_checked'])
            cells += report['adaptive_cells_checked']
            props += report['props_checked']
            routes += report['posed_merged_path_routes_checked']
        self.assertEqual((cells, props, routes), (15, 14, 60))

    def test_actual_saved_aliases_and_prop_poses_match_canonical_in_all_four_rotations(self):
        self.check()
        for row in self.rows:
            tile, target = int(row['canonical_tile_id'], 16), int(row['resolved_tile_id'], 16)
            canonical = parse_paths(self.resources[*PATH, tile])
            runtime = parse_paths(self.resources[*verify.AVENUE_PATH, target])
            for turns in range(4):
                for expected, actual in zip(canonical, runtime):
                    self.assertEqual([quarter_turn(point, turns) for point in expected['points']],
                                     [quarter_turn(point, turns + row['rotation']) for point in actual['points']])
                    self.assertEqual((actual['entry'] + row['rotation'] + turns) % 4,
                                     (expected['entry'] + turns) % 4)
                    self.assertEqual((actual['exit'] + row['rotation'] + turns) % 4,
                                     (expected['exit'] + turns) % 4)
                    self.assertEqual((actual['transport'], actual['lane'], actual['compatibility']),
                                     (expected['transport'], expected['lane'], expected['compatibility']))
                if row['prop']:
                    props = exemplar(self.resources[*adaptive_network.T21, target])['properties']
                    lot = next(prop['values'] for prop in props if int(prop['id'], 16) == 0x88EDC900)
                    self.assertEqual((lot[2] + row['rotation'] + turns) % 4, turns)

    def test_missing_last_appearance_zoom_and_changed_native_texture_are_rejected(self):
        for donor in ('04000200', '04003800'):
            row = next(row for row in self.rows if row['texture_donor_id'] == donor)
            key = (*verify.TEXTURE, int(row['resolved_tile_id'], 16) + 0x34)
            for missing in (False, True):
                with self.subTest(donor=donor, missing=missing):
                    changed = dict(self.resources)
                    if missing:
                        del changed[key]
                        message = 'missing a texture'
                    else:
                        changed[key] += b' changed saved image'
                        message = 'audited appearance and zoom donor'
                    with self.assertRaisesRegex(ValueError, message):
                        self.check(changed)

    def test_removing_upper_lower_pedestrian_or_ground_junction_route_is_rejected(self):
        key = (*verify.AVENUE_PATH, int(self.row['resolved_tile_id'], 16))
        original = parse_paths(self.resources[key])
        for index, label in enumerate(('upper', 'lower', 'pedestrian', 'ground junction')):
            changed = dict(self.resources)
            changed[key] = encode_active_routes(original[:index] + original[index + 1:])
            with self.subTest(route=label), self.assertRaisesRegex(ValueError, 'every posed ground, highway, and ramp route'):
                self.check(changed)

    def test_moving_route_sample_or_changing_junction_bit_is_rejected(self):
        key = (*verify.AVENUE_PATH, int(self.row['resolved_tile_id'], 16))
        for index in range(4):
            for junction_bit in (False, True):
                changed, routes = dict(self.resources), parse_paths(self.resources[key])
                if junction_bit:
                    routes[index]['compatibility'] ^= 1
                else:
                    east, north, height = routes[index]['points'][1]
                    routes[index]['points'][1] = (east + .125, north, height)
                changed[key] = encode_active_routes(routes)
                with self.subTest(route=index, junction_bit=junction_bit), self.assertRaisesRegex(ValueError, 'every posed'):
                    self.check(changed)

    def test_flat_apron_removed_from_prop_is_rejected(self):
        key = (*S3D, int(self.row['prop_model_id'], 16))
        changed, overlay = dict(self.resources), parse_s3d(self.resources[key])
        from scp.recipes import combine_meshes
        retained = [mesh for mesh in overlay['meshes'] if mesh['name'].rstrip(b'\0') != b'SCP NAM ramp']
        changed[key] = pack_s3d(combine_meshes([(overlay, retained, (0.0, 0.0, 0.0))]))
        with self.assertRaisesRegex(ValueError, 'changes retained deck, ramp-mouth, slip-lane, or support geometry'):
            self.check(changed)

    def test_apron_uv_deck_vertex_and_support_triangle_mutations_are_rejected(self):
        key = (*S3D, int(self.row['prop_model_id'], 16))
        for name, kind in ((b'SCP NAM ramp', 'uv'), (b'Elevated deck', 'vertex'), (b'Centre support', 'indices')):
            changed, overlay = dict(self.resources), parse_s3d(self.resources[key])
            mesh = next(mesh for mesh in overlay['meshes'] if mesh['name'].rstrip(b'\0') == name)
            vi, ii, _pi, _mi = mesh['frames'][0]
            if kind == 'indices':
                overlay['indices'][ii]['values'] = (0, 2, 1)
            else:
                data = bytearray(overlay['vertices'][vi]['data'])
                offset = 12 if kind == 'uv' else 0
                struct.pack_into('<f', data, offset, struct.unpack_from('<f', data, offset)[0] + .125)
                overlay['vertices'][vi]['data'] = bytes(data)
            changed[key] = pack_s3d(overlay)
            with self.subTest(mesh=name), self.assertRaisesRegex(ValueError, 'changes retained deck'):
                self.check(changed)

    def test_native_ground_mesh_left_inside_prop_is_rejected(self):
        changed = dict(self.resources)
        changed[*S3D, int(self.row['prop_model_id'], 16)] = self.resources[*S3D, int(self.row['canonical_tile_id'], 16)]
        with self.assertRaisesRegex(ValueError, 'changes retained deck'):
            self.check(changed)

    def test_missing_or_wrongly_typed_rotation_capability_is_rejected(self):
        key = (*verify.PROP, int(self.row['prop_id'], 16))
        for missing in (False, True):
            changed, record = dict(self.resources), exemplar(self.resources[key])
            if missing:
                record['properties'] = [prop for prop in record['properties'] if int(prop['id'], 16) != 0xE83A081D]
            else:
                next(prop for prop in record['properties'] if int(prop['id'], 16) == 0xE83A081D)['type'] = '0x0100'
            changed[key] = encode_exemplar(record)
            with self.subTest(missing=missing), self.assertRaisesRegex(ValueError, 'full-geometry rotation encoding'):
                self.check(changed)

    def test_t21_base_rotation_cannot_ignore_the_resolved_tile_pose(self):
        row = next(row for row in self.rows if row['rotation'] == 2 and row['prop'])
        changed = dict(self.resources)
        change_property(changed, (*adaptive_network.T21, int(row['resolved_tile_id'], 16)), 0x88EDC900,
                        lambda prop: prop['values'].__setitem__(2, 0))
        with self.assertRaisesRegex(ValueError, 'prop pose or reference'):
            self.check(changed)

    def test_insufficient_prop_bounds_are_rejected_in_each_axis(self):
        key = (*verify.PROP, int(self.row['prop_id'], 16))
        for axis in range(3):
            changed = dict(self.resources)
            change_property(changed, key, 0x27812810, lambda prop: prop['values'].__setitem__(axis, .1))
            with self.subTest(axis=axis), self.assertRaisesRegex(ValueError, 'occupied size clips'):
                self.check(changed)

    def test_omitted_adaptive_cell_cannot_bypass_complete_corridor_coverage(self):
        changed = deepcopy(self.piece)
        changed['adaptive_ground']['cells'].pop()
        with self.assertRaisesRegex(ValueError, 'every and only the module Avenue cells'):
            self.check(piece=changed)

    def test_saved_elevation_flag_is_checked_for_current_and_legacy_specs(self):
        key = (*verify.AVENUE_PATH, int(self.row['resolved_tile_id'], 16))
        changed = dict(self.resources)
        changed[key] = changed[key].replace(b'\r\n0\r\n1\r\n', b'\r\n0\r\n0\r\n', 1)
        with self.assertRaisesRegex(ValueError, 'PATH elevation flag'):
            self.check(changed)
        for setting in (None, False):
            piece = deepcopy(self.piece)
            piece['adaptive_ground'].pop('use_path_elevation')
            if setting is False:
                piece['adaptive_ground']['use_path_elevation'] = False
            resources, hashes = saved_fixture(piece)
            self.assertTrue(self.check(resources, piece, hashes)['canonical_geometry_and_traffic_preserved'])

    def test_self_consistent_wrong_half_tile_pose_and_donor_are_rejected(self):
        changed_piece, changed = deepcopy(self.piece), dict(self.resources)
        row = next(row for row in changed_piece['adaptive_ground']['cells'] if row['rotation'] == 2)
        binding = next(binding for binding in self.rows if binding['cell'] == row['cell'])
        row['rotation'] = 0
        target, tile = int(row['resolved_tile_id'], 16), int(binding['canonical_tile_id'], 16)
        changed[*verify.AVENUE_PATH, target] = changed[*PATH, tile].replace(
            b'\r\n0\r\n0\r\n', b'\r\n0\r\n1\r\n', 1)
        change_property(changed, (*adaptive_network.T21, target), 0x88EDC900,
                        lambda prop: prop['values'].__setitem__(2, 0))
        with self.assertRaisesRegex(ValueError, 'donor, pose, or Avenue flags'):
            self.check(changed, changed_piece)
        changed_piece = deepcopy(self.piece)
        changed_piece['adaptive_ground']['cells'][0]['texture_donor_id'] = '04003800'
        with self.assertRaisesRegex(ValueError, 'donor, pose, or Avenue flags'):
            self.check(piece=changed_piece)


if __name__ == '__main__':
    unittest.main()
