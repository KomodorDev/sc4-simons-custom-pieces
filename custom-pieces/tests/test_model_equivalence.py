"""Test saved S3D render equivalence without NAM or domain-specific donors."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import struct
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'framework'))

from scp.model_equivalence import audit_s3d_equivalence, s3d_render_fingerprint
from scp.models import ModelError, pack_s3d, parse_s3d


def model():
    """Two visible triangles, deliberately retaining duplicate vertices."""
    vertices = [(0., 0., 0., 0., 0.), (1., 0., 0., 1., 0.),
                (1., 0., 1., 1., 1.), (0., 0., 0., 0., 0.),
                (1., 0., 1., 1., 1.), (0., 0., 1., 0., 1.)]
    material = struct.pack('<IBBBBHIBB', 0xaa, 4, 3, 1, 0, 0x7fff, 0, 0, 0)
    return {'version': (1, 5),
            'vertices': [{'flags': 0, 'format': 2, 'stride': 20,
                          'data': b''.join(struct.pack('<5f', *v) for v in vertices)}],
            'indices': [{'flags': 0, 'stride': 2, 'values': tuple(range(6))}],
            'primitives': [[(0, 0, 6)]],
            'materials': [{'raw': material, 'textures': []}],
            'anim_header': struct.pack('<HffI', 1, 0., 0., 0),
            'meshes': [{'name': b'editor label\0', 'flags': 0,
                        'frames': [(0, 0, 0, 0)]}],
            'trailing': [(b'PROP', b'PROP\x0c\0\0\0\0\0\0\0')]}


class ModelEquivalenceTests(unittest.TestCase):
    def setUp(self):
        self.model = model()
        self.raw = pack_s3d(self.model)

    def test_editor_labels_and_cyclic_first_vertex_preserve_render(self):
        changed = deepcopy(self.model)
        changed['meshes'][0]['name'] = b'another editor label\0'
        audit = audit_s3d_equivalence(self.raw, pack_s3d(changed))
        self.assertEqual(audit['serialization_difference'], 'mesh_labels_only')
        changed['indices'][0]['values'] = (1, 2, 0, 4, 5, 3)
        self.assertTrue(audit_s3d_equivalence(
            self.raw, pack_s3d(changed))['exact_visible_draw_sequence_and_render_state_preserved'])

    def test_vertex_deduplication_preserves_actual_draws(self):
        changed = deepcopy(self.model)
        data = changed['vertices'][0]['data']
        changed['vertices'][0]['data'] = data[:60] + data[100:120]
        changed['indices'][0]['values'] = (0, 1, 2, 0, 2, 3)
        result = audit_s3d_equivalence(self.raw, pack_s3d(changed))
        self.assertEqual(result['semantics']['visible_triangles_per_frame'], [2])
        self.assertIn('vertex_index', result['serialization_difference'])

    def test_render_group_split_preserves_actual_draws(self):
        changed = deepcopy(self.model)
        data = changed['vertices'][0]['data']
        changed['vertices'] = [dict(changed['vertices'][0], data=data[:60]),
                               dict(changed['vertices'][0], data=data[60:])]
        changed['indices'] = [{'flags': 0, 'stride': 2, 'values': (0, 1, 2)}
                              for _ in range(2)]
        changed['primitives'] = [[(0, 0, 3)] for _ in range(2)]
        changed['meshes'] = [{'name': b'group\0', 'flags': 0,
                              'frames': [(i, i, i, 0)]} for i in range(2)]
        self.assertEqual(s3d_render_fingerprint(self.raw),
                         s3d_render_fingerprint(pack_s3d(changed)))

    def test_encoded_colour_attributes_are_preserved(self):
        colour = deepcopy(self.model)
        data = colour['vertices'][0]['data']
        colour['vertices'][0].update(format=1, stride=16,
            data=b''.join(data[i:i + 12] + b'\x11\x22\x33\xff'
                          for i in range(0, len(data), 20)))
        original = pack_s3d(colour)
        self.assertEqual(s3d_render_fingerprint(original)['visible_triangles_per_frame'], [2])
        changed = bytearray(colour['vertices'][0]['data'])
        changed[12] ^= 1
        colour['vertices'][0]['data'] = bytes(changed)
        with self.assertRaises(ModelError):
            audit_s3d_equivalence(original, pack_s3d(colour))

    def test_render_relevant_mutations_are_rejected(self):
        def vertex(m, offset):
            data = bytearray(m['vertices'][0]['data'])
            struct.pack_into('<f', data, offset, struct.unpack_from('<f', data, offset)[0] + .125)
            m['vertices'][0]['data'] = bytes(data)

        def material(m):
            raw = bytearray(m['materials'][0]['raw'])
            raw[4] ^= 1
            m['materials'][0]['raw'] = bytes(raw)

        def animation(m):
            raw = bytearray(m['anim_header'])
            raw[2] ^= 1
            m['anim_header'] = bytes(raw)

        def frames(m):
            raw = bytearray(m['anim_header'])
            struct.pack_into('<H', raw, 0, 2)
            m['anim_header'] = bytes(raw)
            m['meshes'][0]['frames'] *= 2

        def trailing(m):
            tag, raw = m['trailing'][0]
            data = bytearray(raw)
            data[-1] ^= 1
            m['trailing'][0] = (tag, bytes(data))

        def winding(m):
            m['indices'][0]['values'] = (1, 0, 2, 3, 4, 5)

        def extra(m):
            m['indices'][0]['values'] += (0, 1, 2)
            m['primitives'][0][0] = (0, 0, 9)

        def bounds(m):
            m['vertices'][0]['data'] += struct.pack('<5f', 100., 0., 0., 0., 0.)

        mutations = {
            'XYZ': lambda m: vertex(m, 0), 'UV': lambda m: vertex(m, 12),
            'mesh flags': lambda m: m['meshes'][0].update(flags=1),
            'vertex flags': lambda m: m['vertices'][0].update(flags=1),
            'index flags': lambda m: m['indices'][0].update(flags=1),
            'material': material, 'animation header': animation,
            'frame multiplicity': frames, 'trailing data': trailing,
            'winding': winding, 'extra visible triangle': extra,
            'missing visible triangle': lambda m: m['primitives'][0].__setitem__(0, (0, 0, 3)),
            'draw order': lambda m: m['indices'][0].update(values=(3, 4, 5, 0, 1, 2)),
            'unused vertex bounds': bounds,
        }
        for name, mutate in mutations.items():
            with self.subTest(name=name):
                changed = deepcopy(self.model)
                mutate(changed)
                with self.assertRaises(ModelError):
                    audit_s3d_equivalence(self.raw, pack_s3d(changed))

    def test_invalid_or_unsupported_models_fail_explicitly(self):
        invalid = deepcopy(self.model)
        invalid['meshes'][0]['frames'][0] = (99, 0, 0, 0)
        with self.assertRaises(ModelError):
            s3d_render_fingerprint(pack_s3d(invalid))
        invalid = deepcopy(self.model)
        invalid['primitives'][0][0] = (1, 0, 6)
        with self.assertRaises(ModelError):
            s3d_render_fingerprint(pack_s3d(invalid))
        invalid = parse_s3d(self.raw)
        invalid.update(vertices=[], indices=[], primitives=[], materials=[], meshes=[])
        with self.assertRaises(ModelError):
            s3d_render_fingerprint(pack_s3d(invalid))


if __name__ == '__main__':
    unittest.main()
