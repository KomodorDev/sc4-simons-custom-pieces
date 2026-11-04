"""Keep native halves contributed after an earlier host cell is visited."""
from contextlib import ExitStack
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp.models import parse_s3d, positions
from scp_highway import parallel_modules as compiler
from scp_highway import ramp_geometry as geometry


class ParallelModelTransferTests(unittest.TestCase):
    def test_later_city_source_survives_in_earlier_host_actual_s3d(self):
        # Real approved source/host pair. Row -2 sorts before source row -1.
        source, host = (1, -1), (2, -2)
        packed = geometry.pack_road_model

        def face(height):
            return [(0., height, 0., .125, .5),
                    (2., height, 0., .125, .5),
                    (0., height, 2., .125, .5)]

        models = {cell: parse_s3d(packed([face(height)], 0))
                  for cell, height in ((source, 7.5), (host, 15.))}
        # The source still has its actual separate ramp geometry after its
        # native half moves. These synthetic surfaces test packaging order,
        # not the separately verified native material/geometry fingerprints.
        authored = [tuple((p[0] + 16 * source[0], p[1], p[2] + 16 * source[1], *p[3:])
                          for p in face(3.))]
        native_route = {'transport': 1, 'lane': 0, 'entry': 0, 'exit': 2,
                        'compatibility': 0, 'points': [(-8., 0., 7.5), (8., 0., 7.5)]}

        def native_cell(_context, cell):
            model = models[cell]
            return [(model, model['meshes'], (0., 0., 0.))], [native_route], []

        # Exercise the actual compiler and binary mesh combine/pack/decode.
        # Only private native acquisition and appearance are replaced here.
        with ExitStack() as stack:
            replacements = {
                'procedural_geometry': ([], {'lower-exit-grade': authored}),
                'module_catalog': {'occupied_cells': [list(host), list(source)]},
                'ParallelRoadPainter': object(), 'NativeWheeltrackField': object(),
                'channels': (models[source], []), 'material_template': None,
            }
            for name, value in replacements.items():
                stack.enter_context(patch.object(compiler, name, return_value=value))
            stack.enter_context(patch.object(compiler.paths, '_native_cell', side_effect=native_cell))
            stack.enter_context(patch.object(compiler.geometry, 'cut_native_branch_openings',
                                            side_effect=lambda raw, *a, **kw: (raw, {'changed': False})))
            stack.enter_context(patch.object(compiler.geometry, 'pack_road_model',
                                            side_effect=lambda triangles, texture, **kw: packed(triangles, texture)))
            saved = compiler._build_world({'dd_rhw': {}})
        host_heights = {p[1] for block in parse_s3d(saved[host][0])['vertices'] for p in positions(block)}
        source_heights = {p[1] for block in parse_s3d(saved[source][0])['vertices'] for p in positions(block)}
        self.assertEqual(host_heights, {7.5, 15.})
        self.assertEqual(source_heights, {3.})
        self.assertEqual(set(saved), {host, source})


if __name__ == '__main__':
    unittest.main()
