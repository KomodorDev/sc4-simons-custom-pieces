"""Pin the actual game processor word without changing authored attributes.

The supported executable's SerialRead stores the raw VERT format word;
SetModel compares it with 0x80004001. This binary contract is independent
of the generic parser, which can decode the legacy value 2 as well.
These tests establish processor eligibility, not a new in-game observation.
"""
from pathlib import Path
import struct
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp.models import pack_s3d, parse_s3d, validate_s3d, vertex_stride
from scp.recipes import combine_meshes
from scp_highway.ramp_geometry import pack_road_model


def triangle(x=0.):
    return ((x, 7.5, 0., .625, .25),
            (x + .125, 7.5, 0., .6875, .3125),
            (x, 7.5, .125, .5625, .375))


def indexed_attributes(model):
    result = []
    for mesh in model['meshes']:
        vi, ii, pi, mi = mesh['frames'][0]
        block = model['vertices'][vi]
        vertices = [struct.unpack_from('<5f', block['data'], at)
                    for at in range(0, len(block['data']), block['stride'])]
        for kind, first, count in model['primitives'][pi]:
            for at in range(first, first + count, 3):
                result.append((kind, tuple(vertices[index] for index in model['indices'][ii]['values'][at:at + 3]),
                               model['materials'][mi]['raw']))
    return result


class HighwayVertexFormatTests(unittest.TestCase):
    def test_serialized_processor_word_changes_no_xyz_uv_triangle_or_material_bytes(self):
        raw = pack_road_model([triangle()], 0x5713000E)
        model = parse_s3d(raw)
        # The field is an actual serialized uint32, following VERT's chunk
        # header, group count, flags, and vertex count. Do not infer it from
        # stride: the old parser accepted both descriptors as 20 bytes.
        vert = raw.index(b'VERT')
        offset = vert + 16
        self.assertEqual(struct.unpack_from('<I', raw, offset)[0], 0x80004001)
        self.assertEqual(vertex_stride(2), vertex_stride(0x80004001))
        self.assertEqual(model['vertices'][0]['data'], b''.join(struct.pack('<5f', *point) for point in triangle()))
        legacy = bytearray(raw)
        struct.pack_into('<I', legacy, offset, 2)
        previous = parse_s3d(bytes(legacy))
        validate_s3d(previous)
        self.assertNotEqual(previous['vertices'][0]['format'], 0x80004001)
        self.assertEqual(indexed_attributes(model), indexed_attributes(previous))
        for key in ('indices', 'primitives', 'materials', 'anim_header', 'meshes', 'trailing'):
            self.assertEqual(model[key], previous[key], key)
        restored = bytearray(raw)
        struct.pack_into('<I', restored, offset, 2)
        self.assertEqual(bytes(restored), bytes(legacy))

    def test_every_split_authored_buffer_uses_the_compatible_word(self):
        source = [triangle(at / 4.) for at in range(200)]
        model = parse_s3d(pack_road_model(source, 0x5713000E))
        self.assertGreater(len(model['vertices']), 1)
        self.assertEqual({block['format'] for block in model['vertices']}, {0x80004001})
        self.assertEqual([face[1] for face in indexed_attributes(model)], source)
        self.assertTrue(all(len(block['data']) // block['stride'] <= 512 for block in model['vertices']))
        self.assertEqual(validate_s3d(model)['triangles'], len(source))

    def test_combined_preview_keeps_processor_words_and_exact_uvs(self):
        model = parse_s3d(pack_road_model([triangle()], 0x5713000E))
        combined = combine_meshes([(model, model['meshes'], (0., 0., 0.)),
                                   (model, model['meshes'], (16., 0., -16.))])
        preview = parse_s3d(pack_s3d(combined))
        self.assertEqual({block['format'] for block in preview['vertices']}, {0x80004001})
        faces = [face[1] for face in indexed_attributes(preview)]
        self.assertEqual(faces[0], triangle())
        self.assertEqual(faces[1], tuple((x + 16., h, south - 16., u, v) for x, h, south, u, v in triangle()))
        self.assertEqual(validate_s3d(preview)['triangles'], 2)


if __name__ == '__main__':
    unittest.main()
