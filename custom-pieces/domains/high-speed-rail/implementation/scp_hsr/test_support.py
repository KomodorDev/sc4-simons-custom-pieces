"""Original synthetic XYZ/UV donor and triangle reader used only by tests.

These deliberately small authored surfaces contain no NAM assets. Production
builders and verifiers must never import this optional testing helper.
"""
import struct
from scp.models import parse_s3d, pack_s3d


def donor():
    triangles = []
    def quad(points):
        triangles.extend((points[0], points[1], points[2], points[0], points[2], points[3]))
    # The only flat bed is a 12 m wide pair of triangles. UV U=1 at the
    # left edge and U=.25 at the right edge; V repeats once over 16 m.
    quad([(-6, 16.2, -8, 1, 0), (-6, 16.2, 8, 1, -1),
          (6, 16.2, 8, .25, -1), (6, 16.2, -8, .25, 0)])
    for sign in (-1, 1):
        outer, inner = sign * 7.5, sign * 6
        quad([(outer, 14, -8, .02, 0), (outer, 14, 8, .02, -1),
              (outer, 17, 8, .12, -1), (outer, 17, -8, .12, 0)])
        quad([(outer, 17, -8, .12, 0), (outer, 17, 8, .12, -1),
              (inner, 17, 8, .19, -1), (inner, 17, -8, .19, 0)])
        quad([(inner, 17, -8, .19, 0), (inner, 17, 8, .19, -1),
              (inner, 16.2, 8, .21, -1), (inner, 16.2, -8, .21, 0)])
    material = (struct.pack('<IBBBBHIBB', 0, 0, 0, 0, 0, 0, 0, 0, 1)
                + struct.pack('<IBBBBHHB', 0x0BF6E09B, 0, 0, 0, 0, 0, 0, 1) + b'\0')
    model = {'version': (1, 5),
             'vertices': [{'flags': 0, 'format': 2, 'stride': 20,
                           'data': b''.join(struct.pack('<5f', *v) for v in triangles)}],
             'indices': [{'flags': 0, 'stride': 2, 'values': tuple(range(len(triangles)))}],
             'primitives': [[(0, 0, len(triangles))]],
             'materials': [{'raw': material, 'textures': [0x0BF6E09B]}],
             'anim_header': struct.pack('<HfHHf', 1, 0, 0, 0, 0),
             'meshes': [{'name': b'original fixture\0', 'flags': 0, 'frames': [(0, 0, 0, 0)]}],
             'trailing': []}
    return pack_s3d(model)


def triangles(raw):
    model = parse_s3d(raw)
    result = []
    for mesh in model['meshes']:
        vi, ii, pi, mi = mesh['frames'][0]
        vb = model['vertices'][vi]
        vertices = [struct.unpack_from('<5f', vb['data'], offset)
                    for offset in range(0, len(vb['data']), vb['stride'])]
        indices = model['indices'][ii]['values']
        for kind, first, count in model['primitives'][pi]:
            assert kind == 0 and count % 3 == 0
            result.extend(tuple(vertices[i] for i in indices[pos:pos + 3])
                          for pos in range(first, first + count, 3))
    return result




from .hsr_components_verify import CONTRACTS
from .interchange_verify import _bed


def spec_for(recipe):
    contract = CONTRACTS[recipe]
    return {'id': recipe.replace('_', '-'), 'recipe': recipe, 'name': recipe,
            'footprint': list(contract['footprint']),
            'cells': [list(cell) for cell in contract['cells']],
            'structural_cells': [list(cell) for cell in contract.get('structural_cells', [])],
            'tile_ids': [f'{0x7f900000+0x100*x+0x10*row:08x}' for x, row in contract['cells']],
            'preview_id': '7f903ff5', 'puzzle_id': 'f8ff',
            'effect_name': 'preview_scp_test_0000000000'}


def floor(x0, x1, z0, z1, *, height=15.5, gradient=.0, absolute_y=None):
    def point(x, z):
        return (x, (_bed(height) if absolute_y is None else absolute_y)+gradient*z, z, .61, 0.)
    a, b, c, d = point(x0, z0), point(x1, z0), point(x1, z1), point(x0, z1)
    return [(a, b, c), (a, c, d)]
