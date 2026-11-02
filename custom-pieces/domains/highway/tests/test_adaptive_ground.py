"""Exercise active Avenue resources without changing canonical highway geometry."""
from copy import deepcopy
from pathlib import Path
import re
import struct
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp import adaptive_network, jsonc
from scp.dbpf import encode_exemplar, exemplar
from scp.models import pack_s3d, parse_s3d, positions
from scp_highway import adaptive_ground as ground
from scp_highway.native import encode_paths, parse_paths
from scp_highway.ramp_geometry import road_material


def model_mesh(name, texture, height=0.0):
    points = [(-3.0, height, -2.0, .2, .3), (5.0, height, -2.0, .8, .3),
              (-3.0, height, 6.0, .2, .9)]
    return {'version': (1, 5), 'vertices': [{'flags': 0, 'format': 2, 'stride': 20,
             'data': b''.join(struct.pack('<5f', *point) for point in points)}],
            'indices': [{'flags': 0, 'stride': 2, 'values': (0, 1, 2)}],
            'primitives': [[(0, 0, 3)]], 'materials': [road_material(texture)],
            'anim_header': struct.pack('<HffI', 1, 0.0, 0.0, 0),
            'meshes': [{'name': name, 'flags': 1, 'frames': [(0, 0, 0, 0)]}], 'trailing': []}


def model(*meshes):
    from scp.recipes import combine_meshes
    return pack_s3d(combine_meshes([(part, part['meshes'], (0.0, 0.0, 0.0)) for part in meshes]))


def native_prop():
    return encode_exemplar({'parent': [0, 0, 0], 'properties': [
        {'id': '0x00000010', 'type': '0x0300', 'key_type': '0x0000', 'values': [30]},
        {'id': '0xe83a081d', 'type': '0x0b00', 'key_type': '0x0000', 'values': [1]}]})


def routes():
    # Independent literal channels exercise both heights, pedestrians, native
    # entry/exit sides, interior samples, and a junction flag.
    return [dict(transport=1, lane=1, entry=0, exit=2, compatibility=1,
                 points=[(-8.0, 1.25, 15.0), (0.5, .75, 15.0), (8.0, 1.25, 15.0)]),
            dict(transport=1, lane=2, entry=2, exit=0, compatibility=0,
                 points=[(8.0, -1.25, 7.5), (-8.0, -1.25, 7.5)]),
            dict(transport=2, lane=1, entry=0, exit=2, compatibility=0,
                 points=[(-8.0, 6.5, 0.0), (8.0, 6.5, 0.0)])]


def spec(key):
    return jsonc.load(ROOT / 'domains/highway/00_pieces' / ('ddrhw-diagonal-' + key) / 'piece.jsonc')


def compiled(piece):
    adapted = {tuple(row['cell']): row for row in adaptive_network.bindings(piece)}
    result = []
    for cell in piece['cells']:
        row = adapted.get(tuple(cell))
        if row:
            texture = 0x0400380E if row['texture_donor_id'] == '04003800' else 0x0400020E
            parts = [model_mesh(b'SCP opened Avenue\0', texture)]
            if row['prop']:
                # Flat MIS aprons must survive the Avenue mesh filter.
                parts += [model_mesh(b'SCP NAM ramp\0', 0x5712000E)]
        else:
            parts = [model_mesh(b'SCP NAM ramp\0', 0x5712000E, 7.5)]
        empty = cell in piece['engineering']['model_only_cells']
        result.append((tuple(cell), model(*parts), encode_paths([] if empty else routes())))
    return result


def capture():
    result = {ground.NATIVE_PROP: native_prop()}
    for donor in (0x04000200, 0x04003800):
        for appearance in (0, 0x10, 0x20, 0x30):
            for zoom in range(5):
                result[*ground.TEXTURE, donor + appearance + zoom] = (
                    f'native image {donor:08x}/{appearance:02x}/{zoom}'.encode('ascii'))
    return result


class AdaptiveGroundResourcesTests(unittest.TestCase):
    def test_filter_preserves_raised_deck_and_flat_mis_apron_buffers_exactly(self):
        raw = model(model_mesh(b'Avenue\0', 0x0400380E),
                    model_mesh(b'SCP opened Avenue\0', 0x0400020E),
                    model_mesh(b'Deck\0', 0x5713000E, 15.0),
                    model_mesh(b'SCP NAM ramp\0', 0x5712000E))
        source, filtered = parse_s3d(raw), parse_s3d(ground.filter_overlay_model(raw))
        before = source['meshes'][2:]
        self.assertEqual([mesh['name'] for mesh in filtered['meshes']], [mesh['name'] for mesh in before])
        for expected, actual in zip(before, filtered['meshes']):
            self.assertEqual(expected['flags'], actual['flags'])
            for old, new in zip(expected['frames'], actual['frames']):
                for key, i in (('vertices', 0), ('indices', 1), ('primitives', 2), ('materials', 3)):
                    self.assertEqual(source[key][old[i]], filtered[key][new[i]])

    def test_filter_does_not_create_an_empty_prop_or_remove_unaudited_surfaces(self):
        self.assertIsNone(ground.filter_overlay_model(model(model_mesh(b'Avenue\0', 0x0400380E))))
        for part, message in ((model_mesh(b'Avenue\0', 0x0400380E, 7.5), 'elevated'),
                              (model_mesh(b'Avenue\0', 0x5712000E), 'unaudited'),
                              (model_mesh(b'SCP NAM ramp\0', 0x5712000E), 'no audited')):
            with self.subTest(message=message):
                with self.assertRaisesRegex(ValueError, message):
                    ground.filter_overlay_model(model(part))

    def test_merged_path_inverse_pose_retains_every_channel_in_four_world_rotations(self):
        original = encode_paths(routes())
        self.assertIs(ground.posed_path_alias(original, 0), original)
        for pose in (0, 2):
            saved = parse_paths(ground.posed_path_alias(original, pose))
            self.assertEqual(len(saved), 3)
            for quarter in range(4):
                for source, alias in zip(routes(), saved):
                    self.assertEqual((source['transport'], source['lane'], source['compatibility']),
                                     (alias['transport'], alias['lane'], alias['compatibility']))
                    self.assertEqual((alias['entry'] + pose + quarter) % 4,
                                     (source['entry'] + quarter) % 4)
                    for old, point in zip(source['points'], alias['points']):
                        x, y, height = point
                        actual = ((x, y), (y, -x), (-x, -y), (-y, x))[(pose + quarter) % 4]
                        x, y, old_height = old
                        expected = ((x, y), (y, -x), (-x, -y), (-y, x))[quarter]
                        self.assertEqual((*actual, height), (*expected, old_height))

    def test_inverse_alias_preserves_nine_decimal_authored_samples_and_junction_metadata(self):
        # This is a literal canonical-style PATH, independent of either
        # alias generation or the native donor encoder's .9g formatting.
        raw = b'\r\n'.join([
            b'SC4PATHS', b'1.2', b'3', b'0', b'0',
            b'1', b'1', b'0', b'2', b'1', b'3',
            b'-8.000000000,1.123456789,15.000000000',
            b'7.123456789,0.000000123,14.987654321',
            b'8.000000000,1.123456789,15.000000000',
            b'1', b'2', b'2', b'0', b'0', b'2',
            b'8.000000000,-1.987654321,7.500000000',
            b'-8.000000000,-1.987654321,7.500000000',
            b'2', b'1', b'0', b'2', b'0', b'2',
            b'-8.000000000,6.123456789,0.000000000',
            b'8.000000000,6.123456789,0.000000000', b''])
        source = parse_paths(raw)
        saved = parse_paths(ground.posed_path_alias(raw, 2))
        self.assertEqual(len(saved), 3)
        self.assertEqual(saved[0]['points'][1], (-7.123456789, -0.000000123, 14.987654321))
        for before, after in zip(source, saved):
            self.assertEqual((before['transport'], before['lane'], before['compatibility']),
                             (after['transport'], after['lane'], after['compatibility']))
            self.assertEqual([(x, y, h) for x, y, h in before['points']],
                             [(-x, -y, h) for x, y, h in after['points']])

    def test_all_fifteen_cells_copy_exact_native_images_and_leave_canonical_inputs_unchanged(self):
        total_cells, total_props, total_resources = 0, 0, 0
        inputs = capture()
        for key in ('access-core', 'northwest-junction', 'southeast-junction'):
            piece, before_capture = spec(key), deepcopy(inputs)
            source = compiled(piece)
            before_source = deepcopy(source)
            resources = ground.build_resources(piece, {'adaptive_avenue': inputs}, source)
            rows = ground.bindings(piece)
            self.assertEqual(set(resources), adaptive_network.resource_keys(piece))
            adaptive_network.validate_active_resources(resources, piece)
            self.assertEqual(source, before_source)
            self.assertEqual(inputs, before_capture)
            total_cells += len(rows)
            total_props += sum(row['prop'] for row in rows)
            total_resources += len(resources)
            for row in rows:
                target, donor = int(row['resolved_tile_id'], 16), int(row['texture_donor_id'], 16)
                for appearance in (0, 0x10, 0x20, 0x30):
                    for zoom in range(5):
                        self.assertEqual(resources[*ground.TEXTURE, target + appearance + zoom],
                                         inputs[*ground.TEXTURE, donor + appearance + zoom])
                if row['prop']:
                    prop = {int(p['id'], 16): p for p in exemplar(resources[*ground.PROP,
                                        int(row['prop_id'], 16)])['properties']}
                    self.assertGreater(prop[0x27812810]['values'][1], 0.0)
                    self.assertEqual(prop[0xE83A081D]['type'], '0x0b00')
                    self.assertEqual(prop[0xE83A081D]['key_type'], '0x0000')
                    self.assertEqual(prop[0xE83A081D]['values'], [1])
                    saved = parse_s3d(resources[*ground.S3D, int(row['prop_model_id'], 16)])
                    self.assertTrue(all(p[1] == 0.0 for vb in saved['vertices'] for p in positions(vb)))
        self.assertEqual((total_cells, total_props, total_resources), (15, 14, 357))

    def test_partial_capture_wrong_pose_and_false_prop_declarations_cannot_silently_build(self):
        piece, source = spec('access-core'), compiled(spec('access-core'))
        inputs = capture()
        del inputs[*ground.TEXTURE, 0x04000234]
        with self.assertRaisesRegex(ValueError, 'appearance or zoom'):
            ground.build_resources(piece, {'adaptive_avenue': inputs}, source)
        for field, value in (('rotation', 0), ('texture_donor_id', '04003800'), ('prop', False)):
            changed = deepcopy(piece)
            changed['adaptive_ground']['cells'][0][field] = value
            with self.subTest(field=field):
                with self.assertRaises(ValueError):
                    ground.bindings(changed)
        with self.assertRaisesRegex(ValueError, 'capture is required'):
            ground.build_resources(piece, {}, source)


class AdaptiveGroundConstructionTests(unittest.TestCase):
    RUL0 = b'[Ordering]\r\nRotationRing=1000,11000\r\n'
    RUL1 = (b'[StreetAvenueIntersectionSolutions]\r\n'
            b'TYPE1=0x00000002,0x03010000,0x04004500,0,0\r\n[Next]\r\n')

    def test_core_has_only_the_tested_temporary_handle_and_all_twenty_real_solutions(self):
        piece = spec('access-core')
        result = ground.build_construction(piece, compiled(piece), self.RUL0, self.RUL1)
        self.assertEqual(set(result), {'rul0', 'rul1'})
        self.assertIn('AutoTileBase = 0x55387000', result['rul0'])
        self.assertIn('CheckType = Z - road: 0x02000200\r\n', result['rul0'])
        self.assertIn('CellLayout = .a.Z<\r\n', result['rul0'])
        constraints = re.findall(r'^ConsLayout = (.*)', result['rul0'], re.M)
        self.assertEqual(sum(row.count('+') for row in constraints), 1)
        self.assertEqual(sum('optional' in line for line in result['rul0'].splitlines()), 5)
        self.assertEqual(len(adaptive_network.solution_rows(result['rul1'].encode('ascii'))), 20)

    def test_hybrid_junctions_keep_two_real_static_cells_without_a_synthetic_handle(self):
        for key in ('northwest-junction', 'southeast-junction'):
            piece = spec(key)
            result = ground.build_construction(piece, compiled(piece), self.RUL0, self.RUL1)
            self.assertNotIn('CheckType = Z', result['rul0'])
            self.assertNotIn('0x55387000', result['rul0'])
            self.assertEqual(sum('optional' in line for line in result['rul0'].splitlines()),
                             4 if key == 'northwest-junction' else 6)
            constraints = re.findall(r'^ConsLayout = (.*)', result['rul0'], re.M)
            self.assertEqual(sum(row.count('+') for row in constraints), 2)

    def test_native_marker_target_and_rotation_state_conflicts_are_rejected(self):
        piece = spec('access-core')
        source = compiled(piece)
        row = piece['adaptive_ground']['cells'][0]
        collisions = [f'TYPE1=0x{row["street_flags"]},0x{row["avenue_flags"]},0x12340000,0,0',
                      f'TYPE1=0x01010101,0x03010000,0x{row["resolved_tile_id"]},0,0']
        for conflict in collisions:
            native = ('[StreetAvenueIntersectionSolutions]\r\n' + conflict + '\r\n').encode('ascii')
            with self.assertRaisesRegex(ValueError, 'conflict'):
                ground.build_construction(piece, source, self.RUL0, native)
        native = self.RUL0 + f'AddTypes = {piece["puzzle_id"]}\r\n'.encode('ascii')
        with self.assertRaisesRegex(ValueError, 'state conflicts'):
            ground.build_construction(piece, source, native, self.RUL1)


if __name__ == '__main__':
    unittest.main()
