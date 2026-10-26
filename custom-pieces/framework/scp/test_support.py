"""Synthetic opaque S3D deck for shared renderer/shadow negative-control tests."""
import struct


def plane(x0=-2., x1=2., z0=-8., z1=8., height=15.5):
    """A four-metre-wide opaque deck; deliberately no native input dependency."""
    points = [(x0, height, z0), (x1, height, z0),
              (x1, height, z1), (x0, height, z1)]
    material = struct.pack('<IBBBBHIBB', 0, 0, 0, 0, 0, 0, 0, 0, 0)
    return {'version': (1, 5),
            'vertices': [{'flags': 0, 'format': 2, 'stride': 20,
                          'data': b''.join(struct.pack('<5f', *p, 0., 0.) for p in points)}],
            'indices': [{'flags': 0, 'stride': 2, 'values': (0, 1, 2, 0, 2, 3)}],
            'primitives': [[(0, 0, 6)]],
            'materials': [{'raw': material, 'textures': []}],
            'anim_header': struct.pack('<H', 1) + b'\0' * 12,
            'meshes': [{'name': b'opaque deck\0', 'flags': 0, 'frames': [(0, 0, 0, 0)]}],
            'trailing': [(b'PROP', b'PROP' + struct.pack('<II', 12, 0)),
                         (b'REGP', b'REGP' + struct.pack('<II', 12, 0))]}

