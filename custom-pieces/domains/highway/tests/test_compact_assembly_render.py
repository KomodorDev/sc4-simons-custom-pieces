"""Compiled-render captions read active elevated and legacy saved PATHs."""
import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT/'framework'))
from scp.dbpf import pack_dbpf

spec = importlib.util.spec_from_file_location('compact_assembly_render', ROOT/'domains/highway/tools/render_compact_assembly.py')
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)


def paths(heights, elevation):
    lines = ['SC4PATHS', '1.2', str(len(heights)), '0', str(elevation)]
    for lane, height in enumerate(heights):
        lines += ['1', str(lane), '0', '2', '0', '2', f'-8,0,{height}', f'8,0,{height}']
    return ('\r\n'.join(lines)+'\r\n').encode('ascii')


class CompiledAssemblyHeightTests(unittest.TestCase):
    def read_heights(self, heights, elevation):
        piece = {'id': 'caption-fixture', 'asset_file': 'fixture.dat', 'preview_id': '7f000ff5'}
        resources = {(0x5AD0E817, 0xBADB57F1, 0x7F000FF5): b'unparsed preview fingerprint',
                     (0x296678F7, 0xA966883F, 0x7F000000): paths(heights, elevation)}
        with tempfile.TemporaryDirectory() as directory:
            build = Path(directory)
            (build/'fixture.dat').write_bytes(pack_dbpf(resources))
            _textures, _sources, levels = renderer.saved_resources(build, {'pieces': [piece]}, {piece['id']})
            return levels

    def test_active_elevated_paths_supply_actual_y_caption_levels(self):
        self.assertEqual(self.read_heights([7.5, 15.], 1), [7.5, 15.])

    def test_legacy_ground_and_decks_keep_their_three_levels(self):
        self.assertEqual(self.read_heights([0., 7.5, 15.], 0), [0., 7.5, 15.])

    def test_empty_elevated_model_cell_adds_no_invented_height(self):
        self.assertEqual(self.read_heights([], 1), [])


if __name__ == '__main__':
    unittest.main()
