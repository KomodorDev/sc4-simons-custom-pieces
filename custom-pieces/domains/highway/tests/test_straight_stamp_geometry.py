"""Check the physical face split, including shared concrete meshes and paint."""
from collections import Counter
from pathlib import Path
import struct
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp.models import pack_s3d, parse_s3d
from scp.recipes import combine_meshes
from scp_highway.ramp_geometry import pack_road_model
from scp_highway.straight_stamp_geometry import split_model


def _model(triangles, name):
    model = parse_s3d(pack_road_model(triangles, 0x12345678))
    for mesh in model['meshes']:
        mesh['name'] = name
    return model


def _faces(model):
    result = Counter()
    for mesh in model['meshes']:
        vi, ii, pi, mi = mesh['frames'][0]
        vertices, indices = model['vertices'][vi]['data'], model['indices'][ii]['values']
        for kind, first, count in model['primitives'][pi]:
            for index in range(first, first + count, 3):
                triangle = tuple(vertices[20 * vertex:20 * (vertex + 1)] for vertex in indices[index:index + 3])
                result[model['materials'][mi]['raw'], triangle] += 1
    return result


class StraightStampGeometryTests(unittest.TestCase):
    def test_shared_concrete_mesh_keeps_the_ground_to_deck_pier_and_moves_the_bridge(self):
        pier = ((-.4, 0, -.4, .375, .5), (.4, 0, -.4, .375, .5), (.4, 15, -.4, .375, .5))
        bridge = ((4, 7.5, 1, .375, .5), (5, 8.890625, 1, .375, .5), (5, 8.890625, 2, .375, .5))
        paint = ((0, 7.51, 0, 1.375, .2), (1, 7.51, 0, 1.375, .8), (1, 7.51, 1, 1.375, .8))
        concrete = _model([pier, bridge], b'SCP NAM concrete\0')
        markings = _model([paint], b'SCP NAM highway\0')
        original = combine_meshes([(m, m['meshes'], (0., 0., 0.)) for m in (concrete, markings)])
        roles = split_model(pack_s3d(original), (4, -4))
        self.assertEqual(set(roles), {'stamp', 'lower-off'})
        self.assertEqual(sum(_faces(roles['stamp']).values()), 2)
        self.assertEqual(sum(_faces(roles['lower-off']).values()), 1)
        self.assertEqual(_faces(roles['stamp']) + _faces(roles['lower-off']), _faces(original))
        self.assertTrue(all(mesh['name'].startswith(b'SCP moved 4,-4 ') for mesh in roles['lower-off']['meshes']))
        kept_x = [struct.unpack_from('<f', v['data'], n)[0] for v in roles['stamp']['vertices']
                  for n in range(0, len(v['data']), 20)]
        self.assertLessEqual(max(kept_x), 1.0, 'Unused curved vertices must not inflate straight-stamp bounds')

    def test_a_paint_face_outside_the_native_corridor_cannot_be_kept_by_name(self):
        outside = ((-8, 7.51, -8, 1.375, .2), (-7, 7.51, -8, 1.375, .8), (-7, 7.51, -7, 1.375, .8))
        raw = pack_s3d(_model([outside], b'SCP NAM highway\0'))
        with self.assertRaisesRegex(ValueError, 'leaves the straight native corridor'):
            split_model(raw, (4, -4))


if __name__ == '__main__':
    unittest.main()
