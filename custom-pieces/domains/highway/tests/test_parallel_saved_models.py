"""Saved S3D encoding, overhang, and native-candidate mutation checks."""
from copy import deepcopy
import json
from pathlib import Path
import struct
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp.models import pack_s3d, parse_s3d
from scp.test_support import plane
from scp.track_paths import S3D
from scp.verify import strict_dbpf
from scp_highway import parallel_verify as verify


class ParallelIndexedModelTests(unittest.TestCase):
    def test_saved_model_projection_is_indexed_at_actual_overhang_position(self):
        model = plane(height=0.)
        # A synthetic one-texture material is enough for indexed projection;
        # the separate native-material validator is not invoked here.
        raw = (struct.pack('<IBBBBHIBB', 0, 0, 1, 1, 0, 0, 0, 0, 1)
               + struct.pack('<IBBBBHHB', 0x5712000E, 0, 0, 1, 1, 0, 0, 1) + b'\0')
        model['materials'] = [{'raw': raw, 'textures': [0x5712000E]}]
        block = model['vertices'][0]
        data = bytearray(block['data'])
        for at in range(0, len(data), block['stride']):
            x = struct.unpack_from('<f', data, at)[0]
            struct.pack_into('<f', data, at, x + 16.)
        block['data'] = bytes(data)
        faces = verify._decode_faces(pack_s3d(model), origin=(16., -16.))
        index = verify._FaceIndex(faces)
        self.assertTrue(index.nearby((32., -16., 0.)))
        self.assertFalse(index.nearby((16., -16., 0.)))

    def test_an_oversized_actual_render_group_is_rejected(self):
        model = plane()
        block = model['vertices'][0]
        first = block['data'][:block['stride']]
        block['data'] = first * 513
        with self.assertRaisesRegex(ValueError, '512-vertex budget'):
            verify._decode_faces(pack_s3d(model))

    def test_exact_native_avenue_fragment_keeps_measured_uvs_and_triangle_half(self):
        face = {'texture': 0x0400020E,
                'source_vertices': ((-8., 0., -8., 1., 1.), (-8., 0., 8., 1., 0.), (8., 0., 8., 0., 0.))}
        self.assertTrue(verify._native_avenue_fragment(face))
        bad = deepcopy(face)
        bad['source_vertices'] = tuple((*p[:3], p[3] + .01, p[4]) for p in bad['source_vertices'])
        self.assertFalse(verify._native_avenue_fragment(bad))

    def test_finite_3d_capsules_keep_the_two_micrometre_distance_bound(self):
        first, last = (0., 0., 0.), (1., 0., 1.)
        self.assertTrue(verify._edge_capsule_intervals_3d(first, last, (0., 1e-6, 0.), (1., 1e-6, 1.), 2e-6))
        self.assertFalse(verify._edge_capsule_intervals_3d(first, last, (0., 1e-5, 0.), (1., 1e-5, 1.), 2e-6))
        short = verify._edge_capsule_intervals_3d(first, last, (.4, 0., .4), (.6, 0., .6), 2e-6)
        self.assertTrue(short)
        self.assertGreater(min(a for a, b in short), .39)
        self.assertLess(max(b for a, b in short), .61)


class ParallelNativeSavedModelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.build = ROOT / 'dist/ddrhw-parallel-diamond-parts-01'
        manifest_path = cls.build / 'manifest.json'
        if not manifest_path.is_file():
            raise unittest.SkipTest('The independently checked native parallel build is absent; native NAM inputs and a saved candidate build are required.')
        cls.manifest = json.loads(manifest_path.read_text())
        cls.pieces = {piece['id']: piece for piece in cls.manifest['pieces']}
        cls.resources = {piece['id']: strict_dbpf((cls.build / piece['asset_file']).read_bytes())
                         for piece in cls.manifest['pieces']}

    def test_an_actual_saved_zoom_mutation_is_rejected_before_visual_checks(self):
        piece = self.pieces['ddrhw-parallel-upper-exit-departure']
        resources = dict(self.resources[piece['id']])
        key = *S3D, int(piece['tile_ids'][0], 16) + 4
        model = parse_s3d(resources[key])
        block = model['vertices'][0]
        data = bytearray(block['data'])
        x = struct.unpack_from('<f', data, 0)[0]
        struct.pack_into('<f', data, 0, x + .125)
        block['data'] = bytes(data)
        resources[key] = pack_s3d(model)
        with self.assertRaisesRegex(ValueError, 'saved zoom differs'):
            verify.check_models(resources, piece)

    def test_actual_separate_physical_profiles_include_cross_owner_overhang(self):
        faces = []
        for piece in self.pieces.values():
            origin = verify._source_origin(piece)
            for cell, tile in zip(piece['cells'], piece['tile_ids']):
                faces.extend({**face, 'geometry_key': piece['geometry_key'].removeprefix('parallel-')}
                             for face in verify._decode_faces(self.resources[piece['id']][*S3D, int(tile, 16) + 4],
                                 cell, origin=(16. * origin[0], -16. * origin[1])))
        report = verify.check_physical_cuts(faces)
        self.assertEqual(report['functional_physical_interfaces_checked'], 8)
        self.assertTrue(report['checked_physical_cuts_outside_traffic_owner_cells'])
        removed = [face for face in faces if not (face['geometry_key'] == 'upper-exit-departure'
                                                 and face['texture'] == 0x5EB4BEE9)]
        with self.assertRaisesRegex(ValueError, 'separately owned complete barrier'):
            verify.check_physical_cuts(removed)

    def test_a_real_saved_wheeltrack_cannot_reset_its_native_longitudinal_phase(self):
        face = None
        for piece in self.pieces.values():
            origin = verify._source_origin(piece)
            for cell, tile in zip(piece['cells'], piece['tile_ids']):
                candidates = verify._decode_faces(self.resources[piece['id']][*S3D, int(tile, 16)], cell,
                                                   origin=(16. * origin[0], -16. * origin[1]))
                face = next((f for f in candidates if f['texture'] == 0x5713000E and f['upward']
                             and all(.55 < uv[0] < .7 for uv in f['uv'])
                             and min(abs(f['points'][0][2] - 7.5), abs(f['points'][0][2] - 15.)) < 1e-5), None)
                if face is not None:
                    break
            if face is not None:
                break
        self.assertIsNotNone(face)
        verify.check_wheeltrack_vertices([face])
        mutant = {**face, 'uv': tuple((u, v + .01) for u, v in face['uv'])}
        with self.assertRaisesRegex(ValueError, 'approved native wear field'):
            verify.check_wheeltrack_vertices([mutant])


if __name__ == '__main__':
    unittest.main()
