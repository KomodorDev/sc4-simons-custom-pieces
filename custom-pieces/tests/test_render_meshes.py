"""Compiled-resource repacking must preserve exact ordered encoded geometry."""
from copy import deepcopy
from pathlib import Path
import struct
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, str(next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file()) / 'framework'))

from scp.models import ModelError, pack_s3d, parse_s3d, validate_s3d
from scp.render_meshes import MAX_TRIANGLES, MAX_VERTICES, assert_render_budget, repack_s3d


def fixture(count=600, name=b'SCP test deck\0'):
    material = (struct.pack('<IBBBBHIBB', 0, 0, 0, 0, 0, 0, 0, 0, 1)
                + struct.pack('<IBBBBHHB', 0x0BF6E09B, 0, 0, 0, 0, 0, 0, 1) + b'\0')
    vertices = []
    for n in range(count):
        x = float(n)
        vertices.extend(((x, 15., -0., -.0, 0.),
                         (x + .5, 15., 0., 1., .25),
                         (x, 15., .5, 0., 1.)))
    return {'version': (1, 5),
            'vertices': [{'flags': 17, 'format': 2, 'stride': 20,
                          'data': b''.join(struct.pack('<5f', *v) for v in vertices)}],
            'indices': [{'flags': 23, 'stride': 2, 'values': tuple(range(len(vertices)))}],
            'primitives': [[(0, 0, len(vertices))]],
            'materials': [{'raw': material, 'textures': [0x0BF6E09B]}],
            'anim_header': struct.pack('<HfHHf', 1, 17.5, 3, 5, 2.25),
            'meshes': [{'name': name, 'flags': 7, 'frames': [(0, 0, 0, 0)]}],
            'trailing': [(b'PROP', b'PROP' + struct.pack('<II', 12, 0)),
                         (b'REGP', b'REGP' + struct.pack('<II', 12, 0))]}


def expanded(model, frame_number=0):
    """Independent expected sequence; include material and original vertex bytes."""
    result = []
    for mesh in model['meshes']:
        vi, ii, pi, mi = mesh['frames'][frame_number]
        vb, ib = model['vertices'][vi], model['indices'][ii]
        stride = vb['stride']
        for kind, first, count in model['primitives'][pi]:
            assert kind == 0
            for index in range(first, first + count, 3):
                result.append((model['materials'][mi]['raw'], tuple(
                    vb['data'][n * stride:(n + 1) * stride]
                    for n in ib['values'][index:index + 3])))
    return result


class CompiledRenderMeshTests(unittest.TestCase):
    def test_large_group_splits_without_changing_encoded_geometry(self):
        original = fixture()
        raw, report = repack_s3d(pack_s3d(original))
        repaired = parse_s3d(raw)
        self.assertTrue(report['changed'])
        self.assertEqual(expanded(original), expanded(repaired))
        self.assertEqual(validate_s3d(repaired)['triangles'], 600)
        self.assertEqual(repaired['anim_header'], original['anim_header'])
        self.assertEqual(repaired['materials'], original['materials'])
        self.assertEqual(repaired['trailing'], original['trailing'])
        self.assertTrue(all(m['name'] == original['meshes'][0]['name'] and m['flags'] == 7
                            for m in repaired['meshes']))
        self.assertTrue(all(v['flags'] == 17 for v in repaired['vertices']))
        self.assertTrue(all(i['flags'] == 23 for i in repaired['indices']))
        self.assertLessEqual(report['max_authored_vertices_after'], MAX_VERTICES)
        self.assertLessEqual(report['max_authored_triangles_after'], MAX_TRIANGLES)

    def test_small_model_is_returned_byte_for_byte_including_native_prim_lengths(self):
        raw = bytearray(pack_s3d(fixture(2)))
        pos = raw.index(b'PRIM')
        struct.pack_into('<I', raw, pos + 4, struct.unpack_from('<I', raw, pos + 4)[0] + 4)
        raw = bytes(raw)
        repaired, report = repack_s3d(raw)
        self.assertIs(repaired, raw)
        self.assertFalse(report['changed'])

    def test_oversized_native_mesh_is_not_repacked_or_subject_to_authored_budget(self):
        original = fixture(name=b'native donor\0')
        raw = pack_s3d(original)
        repaired, report = repack_s3d(raw)
        self.assertIs(repaired, raw)
        self.assertEqual(report['authored_frames_checked'], 0)

    def test_degenerate_and_signed_zero_vertices_survive_exactly(self):
        original = fixture()
        vb = original['vertices'][0]
        data = bytearray(vb['data'])
        data[20:60] = data[:20] * 2
        vb['data'] = bytes(data)
        raw, _ = repack_s3d(pack_s3d(original))
        self.assertEqual(expanded(original), expanded(parse_s3d(raw)))

    def test_native_shared_buffer_and_materials_survive_remapping(self):
        original = fixture()
        original['materials'].append(deepcopy(original['materials'][0]))
        original['materials'][1]['raw'] = bytes([1]) + original['materials'][1]['raw'][1:]
        original['indices'].append({'flags': 31, 'stride': 2, 'values': (2, 1, 0)})
        original['primitives'].append([(0, 0, 3)])
        original['meshes'].insert(0, {'name': b'untouched native\0', 'flags': 19,
                                     'frames': [(0, 1, 1, 1)]})
        raw, _ = repack_s3d(pack_s3d(original))
        repaired = parse_s3d(raw)
        mesh = repaired['meshes'][0]
        self.assertEqual(mesh['name'], b'untouched native\0')
        self.assertEqual(mesh['flags'], 19)
        self.assertEqual(mesh['frames'][0][3], 1)
        for number, array in enumerate(('vertices', 'indices', 'primitives', 'materials')):
            self.assertEqual(repaired[array][mesh['frames'][0][number]],
                             original[array][original['meshes'][0]['frames'][0][number]])
        self.assertEqual(expanded(original), expanded(repaired))

    def test_separate_small_authored_mesh_and_primitive_order_remain_exact(self):
        original = fixture()
        # Draw two disjoint ranges in reversed order; unused indices must not
        # accidentally become triangles, and primitive order is significant.
        original['primitives'][0] = [(0, 900, 900), (0, 0, 600)]
        small = fixture(2)
        for array in ('vertices', 'indices', 'primitives'):
            original[array].extend(deepcopy(small[array]))
        small_mesh = {'name': b'SCP small support\0', 'flags': 11, 'frames': [(1, 1, 1, 0)]}
        original['meshes'].append(small_mesh)
        raw, _ = repack_s3d(pack_s3d(original))
        repaired = parse_s3d(raw)
        untouched = repaired['meshes'][-1]
        self.assertEqual(untouched['name'], small_mesh['name'])
        self.assertEqual(untouched['flags'], small_mesh['flags'])
        for number, array in enumerate(('vertices', 'indices', 'primitives')):
            self.assertEqual(repaired[array][untouched['frames'][0][number]], small[array][0])
        self.assertEqual(expanded(original), expanded(repaired))

    def test_triangle_budget_applies_even_when_vertices_are_shared(self):
        original = fixture(1)
        original['indices'][0]['values'] = (0, 1, 2) * 700
        original['primitives'][0] = [(0, 0, 2100)]
        raw, report = repack_s3d(pack_s3d(original))
        self.assertEqual(len(parse_s3d(raw)['meshes']), 2)
        self.assertEqual(expanded(original), expanded(parse_s3d(raw)))
        self.assertEqual(report['max_authored_triangles_after'], 512)

    def test_identical_static_frames_and_native_animation_are_preserved(self):
        original = fixture()
        original['anim_header'] = struct.pack('<H', 2) + original['anim_header'][2:]
        original['meshes'][0]['frames'] *= 2
        original['indices'].append({'flags': 31, 'stride': 2, 'values': (2, 1, 0)})
        original['primitives'].append([(0, 0, 3)])
        original['meshes'].append({'name': b'animated donor\0', 'flags': 19,
                                   'frames': [(0, 1, 1, 0), (0, 0, 1, 0)]})
        raw, _ = repack_s3d(pack_s3d(original))
        repaired = parse_s3d(raw)
        for frame in (0, 1):
            self.assertEqual(expanded(original, frame), expanded(repaired, frame))
        self.assertEqual(repaired['anim_header'], original['anim_header'])

    def test_authored_animation_is_rejected_when_later_frame_exceeds_budget(self):
        original = fixture(1)
        original['anim_header'] = struct.pack('<H', 2) + original['anim_header'][2:]
        original['indices'].append({'flags': 0, 'stride': 2, 'values': (0, 1, 2) * 600})
        original['primitives'].append([(0, 0, 1800)])
        original['meshes'][0]['frames'].append((0, 1, 1, 0))
        with self.assertRaisesRegex(ModelError, 'Animated authored'):
            repack_s3d(pack_s3d(original))
        with self.assertRaisesRegex(ModelError, 'conservative render budget'):
            assert_render_budget(original)

    def test_dangling_authored_reference_and_nontriangle_primitive_are_rejected(self):
        original = fixture()
        original['meshes'][0]['frames'] = [(0, 0, 9, 0)]
        with self.assertRaisesRegex(ModelError, 'dangling'):
            repack_s3d(pack_s3d(original))
        original = fixture()
        original['primitives'][0] = [(1, 0, 1800)]
        with self.assertRaisesRegex(ModelError, 'triangle-list'):
            repack_s3d(pack_s3d(original))

    def test_repacking_is_idempotent(self):
        repaired, _ = repack_s3d(pack_s3d(fixture()))
        again, report = repack_s3d(repaired)
        self.assertIs(again, repaired)
        self.assertFalse(report['changed'])


if __name__ == '__main__':
    unittest.main()
