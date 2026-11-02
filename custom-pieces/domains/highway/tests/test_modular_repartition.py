"""Independent saved-triangle ownership and exact re-encoding controls."""
from copy import deepcopy
from pathlib import Path
import struct
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT/'framework'), str(ROOT/'domains/highway/implementation')]
from scp.models import parse_s3d, pack_s3d
from scp.verify import S3D
from scp_highway import modular_partition_verify as audit
from scp_highway.ramp_geometry import pack_road_model


def fixture():
    vertices = ((40.12345504760742, 7.5, -48., .4, .6),
                (41.12345504760742, 7.5, -48., .5, .6),
                (40.12345504760742, 7.5, -49., .4, .7))
    old = parse_s3d(pack_road_model([vertices], 0x5712000E))
    old['meshes'][0]['name'] = b'SCP NAM ramp\0'
    new = deepcopy(old)
    data = bytearray(new['vertices'][0]['data'])
    for offset in range(0, len(data), 20):
        value = struct.unpack_from('<f', data, offset)[0]
        struct.pack_into('<f', data, offset, value-64.)
    new['vertices'][0]['data'] = bytes(data)
    new['meshes'][0]['name'] = b'SCP moved saved source ramp\0'
    def rows(model, owner, east):
        return [({'id': owner, 'geometry_key': owner, 'cells': [[0, 0]], 'tile_ids': ['00000100']},
                 {'origin_m': [east, -64.]}, {(*S3D, 0x104): pack_s3d(model)})]
    return rows(old, audit.STAMP, 64.), rows(new, 'lower-exit-r40', 128.)


class SavedRepartitionTests(unittest.TestCase):
    def test_one_exact_target_float32_translation_preserves_the_triangle(self):
        before, after = fixture()
        report = audit.compare_union(before, after, alternative='default')
        self.assertTrue(report['target_frame_float32_encoding_exact'])
        self.assertEqual(report['attributed_triangles'], 1)
        self.assertEqual(report['triangles_assigned_to_a_different_owner'], 1)

    def test_geometry_owner_uv_material_and_winding_are_each_required(self):
        before, original = fixture()
        for mutation in ('owner', 'position', 'uv', 'material', 'winding'):
            after = deepcopy(original)
            piece, _placement, resources = after[0]
            model = parse_s3d(resources[*S3D, 0x104])
            if mutation == 'owner':
                piece['geometry_key'] = 'upper-exit-r40'
            elif mutation in ('position', 'uv'):
                data = bytearray(model['vertices'][0]['data'])
                at = 0 if mutation == 'position' else 12
                struct.pack_into('<f', data, at, struct.unpack_from('<f', data, at)[0]+.001)
                model['vertices'][0]['data'] = bytes(data)
            elif mutation == 'material':
                model['materials'][0]['raw'] += b'changed'
            else:
                model['indices'][0]['values'] = list(reversed(model['indices'][0]['values']))
            if mutation != 'material':
                resources[*S3D, 0x104] = pack_s3d(model)
            else:
                # Keep a structurally valid material while changing its bytes.
                material = model['materials'][0]
                material['raw'] = material['raw'][:-7].replace(struct.pack('<I', 0x5712000E), struct.pack('<I', 0x5713000E))
                material['textures'] = [0x5713000E]
                resources[*S3D, 0x104] = pack_s3d(model)
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                audit.compare_union(before, after, alternative='default')

    def test_missing_checkpoint_face_cannot_be_hidden_by_an_empty_candidate(self):
        before, _after = fixture()
        with self.assertRaisesRegex(ValueError, 'omits'):
            audit.compare_union(before, [], alternative='default')

    def test_curved_stamp_wing_fails_the_literal_straight_envelope(self):
        before, _after = fixture()
        with self.assertRaisesRegex(ValueError, 'outside its straight native envelope'):
            audit.straight_envelope(before)

    def test_owned_city_path_bytes_and_unique_ownership_are_required(self):
        path = b'independently retained complete path bytes'
        piece = {'id': 'p', 'cells': [[0, 0]], 'tile_ids': ['00000100']}
        before = [(piece, {'origin_m': [0., 0.]}, {(*audit.PATH, 0x100): path})]
        self.assertTrue(audit.compare_paths(before, deepcopy(before))['every_owned_cell_path_byte_exact'])
        after = deepcopy(before)
        after[0][2][*audit.PATH, 0x100] += b'changed'
        with self.assertRaisesRegex(ValueError, 'PATH'):
            audit.compare_paths(before, after)
        with self.assertRaisesRegex(ValueError, 'two independent pieces'):
            audit.compare_paths(before, before+deepcopy(before))

    def test_inherited_support_precision_is_region_material_height_and_distance_bounded(self):
        from scp_highway import ramp_verify as v
        from scp_highway.ramp_geometry import road_material
        import hashlib
        def faces(gap):
            result = []
            for left, right in ((0., 1.), (1.+gap, 2.)):
                points = ((left, 0., 7.5), (right, 0., 7.5),
                          (right, 1., 7.5), (left, 1., 7.5))
                for ids in ((0, 1, 2), (0, 2, 3)):
                    result.append({'points': tuple(points[i] for i in ids), 'upward': True,
                        'texture': 0x5713000E, 'material_sha256': pin})
            return result
        pin = hashlib.sha256(road_material(0x5713000E)['raw']).hexdigest()
        first, last = (.1, .5, 7.5), (1.9, .5, 7.5)
        with patch.object(v, 'DD_MATERIAL_SHA256', pin):
            admitted = []
            self.assertTrue(audit._union_covered(first, last, faces(1e-6), (2, -2), 0, admitted))
            self.assertEqual(len(admitted), 1)
            self.assertLess(admitted[0]['maximum_sampled_distance_m'], 2e-6)
            self.assertFalse(audit._union_covered(first, last, faces(1e-6), (0, 0), 0, []))
            self.assertFalse(audit._union_covered(first, last, faces(5e-6), (2, -2), 0, []))
            wrong = faces(3e-6)
            for face in wrong[2:]:
                face['texture'] = 0x5712000E
            self.assertFalse(audit._union_covered(first, last, wrong, (2, -2), 0, []))

    def test_shared_model_dispatch_reports_every_referenced_native_texture(self):
        import hashlib
        from scp import jsonc
        from scp.recipes import combine_meshes
        from scp.verify import check_piece_models
        piece = jsonc.load(ROOT/'domains/highway/00_pieces/ddrhw-modular-lower-exit-r40/piece.jsonc')
        face = ((0., 7.5, 0., .4, .6), (1., 7.5, 0., .5, .6), (0., 7.5, -1., .4, .7))
        parts = [parse_s3d(pack_road_model([face], texture)) for texture in (0x5712000E, 0x5EB4BEE9)]
        model = combine_meshes([(m, m['meshes'], (0., 0., 0.)) for m in parts])
        raw = pack_s3d(model)
        resources, records, preview = {}, [], []
        for cell, tile in zip(piece['cells'], piece['tile_ids']):
            for zoom in range(5):
                resources[*S3D, int(tile, 16)+zoom] = raw
            path = b'fixture-complete-path'
            resources[*audit.PATH, int(tile, 16)] = path
            records.append({'cell': cell, 'model_sha256': hashlib.sha256(raw).hexdigest(),
                            'path_sha256': hashlib.sha256(path).hexdigest()})
            preview.append((model, model['meshes'], (16.*cell[0], 0., 16.*cell[1])))
        preview_raw = pack_s3d(combine_meshes(preview))
        resources[*S3D, int(piece['preview_id'], 16)] = preview_raw
        expected = {'pieces': {piece['id']: {key: piece[key] for key in
                    ('recipe', 'geometry_key', 'cells', 'footprint')}}}
        expected['pieces'][piece['id']].update(cell_resources=records,
            preview_sha256=hashlib.sha256(preview_raw).hexdigest())
        with patch.object(audit, 'reviewed_models', return_value=expected):
            report = check_piece_models(resources, piece, None)
        self.assertEqual(report.pop('texture_ids'), [0x5712000E, 0x5EB4BEE9])
        self.assertTrue(report['render_groups']['all_authored_groups_within_budget'])


if __name__ == '__main__':
    unittest.main()
