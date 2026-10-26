"""Render groups retain exact authored XYZUV faces under conservative budgets."""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import struct
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, str(next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file()) / 'framework'))

from scp.models import parse_s3d, validate_s3d
from scp_hsr.single_track_models import _native, _pack
from scp_hsr.test_support import donor


def expanded_faces(model):
    """Independently decode every mesh's first frame, primitive and index."""
    result = []
    for mesh in model['meshes']:
        vi, ii, pi, _ = mesh['frames'][0]
        vertex_buffer = model['vertices'][vi]
        stride = vertex_buffer['stride']
        assert stride == 20
        indices = model['indices'][ii]['values']
        for kind, first, length in model['primitives'][pi]:
            assert kind == 0 and length % 3 == 0
            for index in indices[first:first+length]:
                result.append(vertex_buffer['data'][index*stride:(index+1)*stride])
    return b''.join(result)


def authored_faces(triangles):
    return b''.join(struct.pack('<5f', *vertex) for triangle in triangles for vertex in triangle)


def face():
    return ((0., 16., 0., 0., 0.), (1., 16., 0., 1., 0.), (0., 16., 1., 0., 1.))


def fan():
    center = (0., 16., 0., 0., 0.)
    ring = [(float(index+1), 16., 1., (index+1)/1024., 1.) for index in range(512)]
    return [(center, a, b) for a, b in zip(ring, ring[1:])]


class RenderMeshPackingTests(unittest.TestCase):
    def setUp(self):
        self.native = _native(donor())

    def assert_packed(self, triangles, native=None):
        model = parse_s3d(_pack(self.native if native is None else native, triangles))
        report = validate_s3d(model)
        self.assertTrue(report['all_output_buffers_used'])
        self.assertEqual(expanded_faces(model), authored_faces(triangles))
        self.assertEqual(len(model['vertices']), len(model['meshes']))
        self.assertEqual(len(model['indices']), len(model['meshes']))
        self.assertEqual(len(model['primitives']), len(model['meshes']))
        self.assertEqual(len(model['materials']), 1)
        for number, mesh in enumerate(model['meshes']):
            for frame in mesh['frames']:
                self.assertEqual(frame, (number, number, number, 0))
            vertex_buffer = model['vertices'][number]
            self.assertLessEqual(len(vertex_buffer['data'])//vertex_buffer['stride'], 512)
            self.assertLessEqual(sum(length//3 for _, _, length in model['primitives'][number]), 512)
        return model

    def test_small_quad_reuses_exact_vertices_and_preserves_corner_order(self):
        a, b, d = face()
        c = (1., 16., 1., 1., 1.)
        triangles = [(a, b, c), (a, c, d)]
        model = self.assert_packed(triangles)
        self.assertEqual(len(model['meshes']), 1)
        self.assertEqual(len(model['vertices'][0]['data'])//20, 4)
        self.assertEqual(model['indices'][0]['values'], (0, 1, 2, 0, 2, 3))

    def test_uv_seams_position_signed_zero_and_texture_signed_zero_stay_distinct(self):
        a, b, c = face()
        negative_position = (-0., 16., 0., 0., 0.)
        seam = (0., 16., 0., .5, 0.)
        negative_texture = (0., 16., 0., -0., 0.)
        triangles = [(a, b, c), (negative_position, c, b),
                     (seam, b, c), (negative_texture, b, c)]
        model = self.assert_packed(triangles)
        self.assertEqual(len(model['vertices'][0]['data'])//20, 6)
        for vertex in (a, negative_position, seam, negative_texture):
            self.assertIn(struct.pack('<5f', *vertex), model['vertices'][0]['data'])

    def test_different_python_floats_with_identical_float32_bytes_share_a_vertex(self):
        _, b, c = face()
        a = (.1, 16., 0., 0., 0.)
        rounded_same = (.1+1e-10, 16., 0., 0., 0.)
        self.assertNotEqual(a, rounded_same)
        self.assertEqual(struct.pack('<5f', *a), struct.pack('<5f', *rounded_same))
        model = self.assert_packed([(a, b, c), (rounded_same, b, c)])
        self.assertEqual(len(model['vertices'][0]['data'])//20, 3)
        self.assertEqual(model['indices'][0]['values'], (0, 1, 2, 0, 1, 2))

    def test_triangle_budget_splits_repeated_faces_even_with_three_unique_vertices(self):
        exactly = self.assert_packed([face()]*512)
        over = self.assert_packed([face()]*513)
        self.assertEqual(len(exactly['meshes']), 1)
        self.assertEqual(len(over['meshes']), 2)
        self.assertEqual([len(block['values'])//3 for block in over['indices']], [512, 1])
        self.assertEqual([len(block['data'])//20 for block in over['vertices']], [3, 3])

    def test_vertex_budget_splits_before_overflow_without_reordering_a_face(self):
        triangles = fan()
        exactly = self.assert_packed(triangles[:510])
        over = self.assert_packed(triangles)
        self.assertEqual(len(exactly['meshes']), 1)
        self.assertEqual(len(exactly['vertices'][0]['data'])//20, 512)
        self.assertEqual(len(over['meshes']), 2)
        self.assertEqual([len(block['values'])//3 for block in over['indices']], [510, 1])
        self.assertEqual([len(block['data'])//20 for block in over['vertices']], [512, 3])

    def test_mixed_vertex_and_face_pressure_preserves_the_complete_global_sequence(self):
        triangles = fan()+[fan()[0]]*600
        model = self.assert_packed(triangles)
        self.assertEqual([len(block['values'])//3 for block in model['indices']], [510, 512, 89])

    def test_total_model_can_exceed_old_unwelded_16bit_vertex_count_safely(self):
        triangles = [face()]*22000
        self.assertGreater(len(triangles)*3, 65535)
        model = self.assert_packed(triangles)
        self.assertEqual(len(model['meshes']), 43)

    def test_native_metadata_and_every_frame_remain_valid_without_mutating_the_donor(self):
        native = deepcopy(self.native)
        native['vb']['flags'] = 0x123
        native['model']['indices'][native['mesh']['frames'][0][1]]['flags'] = 0x45
        native['mesh']['flags'] = 0x67
        native['model']['anim_header'] = struct.pack('<HfHHf', 2, 12.5, 4, 8, .125)
        native['model']['trailing'] = [(b'TEST', b'TEST'+struct.pack('<I', 12)+b'\x04\x03\x02\x01')]
        before = deepcopy(native)
        model = self.assert_packed([face()]*513, native)
        self.assertEqual(native, before)
        self.assertEqual(model['version'], native['model']['version'])
        self.assertEqual(model['anim_header'], native['model']['anim_header'])
        self.assertEqual(model['trailing'], native['model']['trailing'])
        self.assertEqual(model['materials'], [native['material']])
        for vb, ib, mesh in zip(model['vertices'], model['indices'], model['meshes']):
            self.assertEqual((vb['flags'], vb['format'], vb['stride']),
                             (native['vb']['flags'], native['vb']['format'], native['vb']['stride']))
            self.assertEqual((ib['flags'], ib['stride']), (0x45, 2))
            self.assertEqual(mesh['flags'], native['mesh']['flags'])
            self.assertEqual(mesh['name'], b'SCP one-way HSR\0')
            self.assertEqual(len(mesh['frames']), 2)

    def test_existing_degenerate_filter_and_empty_input_rejection_are_retained(self):
        good = face()
        degenerate = (good[0], good[0], good[0])
        model = parse_s3d(_pack(self.native, [degenerate, good, degenerate]))
        self.assertEqual(expanded_faces(model), authored_faces([good]))
        for triangles in ([], [degenerate]):
            with self.assertRaisesRegex(ValueError, 'nondegenerate'):
                _pack(self.native, triangles)

    def test_encoded_repack_mode_retains_faces_collapsed_by_float32_rounding(self):
        original = ((1e6, 16., 1e6, 0., 0.), (1e6+.01, 16., 1e6, 1., 0.),
                    (1e6, 16., 1e6+.01, 0., 1.))
        compiled = tuple(struct.unpack('<5f', struct.pack('<5f', *point)) for point in original)
        self.assertEqual({point[:3] for point in compiled}, {(1e6, 16., 1e6)})
        triangles = [face(), compiled, face()]
        default = parse_s3d(_pack(self.native, triangles))
        kept = parse_s3d(_pack(self.native, triangles, preserve_encoded_triangles=True))
        self.assertEqual(expanded_faces(default), authored_faces([face(), face()]))
        self.assertEqual(expanded_faces(kept), authored_faces(triangles))
        self.assertTrue(validate_s3d(kept)['all_output_buffers_used'])


if __name__ == '__main__':
    unittest.main()
