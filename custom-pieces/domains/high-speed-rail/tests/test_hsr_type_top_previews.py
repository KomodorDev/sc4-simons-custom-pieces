"""Verify optional top views use canonical saved geometry without changing angled previews."""
from pathlib import Path
import hashlib
import json
import sys
import tempfile
import unittest
from unittest.mock import patch

from PIL import Image

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'project.json').is_file())
sys.path.insert(0, str(ROOT/'framework'))

from scp_hsr.test_support import donor
from scp_hsr_tools import render_hsr_assembly_parts as renderer


class CanonicalTypeTopPreviewTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.build = self.root/'build'
        self.build.mkdir()
        self.raw = donor()
        self.pieces, sources = [], []
        for index, identifier in enumerate(('generic-diverge', 'generic-fan')):
            asset = f'{identifier}.dat'
            (self.build/asset).write_bytes(self.raw)
            piece = {'id': identifier, 'name': f'HSR Generic {index}', 'asset_file': asset,
                     'preview_id': f'7f50{index}ff5', 'cells': [[0, 0], [1, 0], [1, 1]]}
            self.pieces.append(piece)
            sources.append({'piece_id': identifier, 'menu_name': piece['name'],
                            'source_dat_sha256': hashlib.sha256(self.raw).hexdigest(),
                            'model_sha256': hashlib.sha256(self.raw).hexdigest(),
                            'label': f'P{index:02}', 'origin_m': [96.*index, 208.],
                            'display_origin_tiles_en': [6.*index, 13.],
                            'rotation_ccw_degrees': 270.})
        (self.build/'manifest.json').write_text(json.dumps({'pieces': self.pieces}))
        self.provenance = {'sources': sources, 'scene_file': 'fixture.json',
                           'scene_sha256': 'fixture-scene', 'coordinate_system': {'scope': 'assembly'},
                           'compiled_source_verification': {'status': 'fixture'}}
        import numpy as np
        self.textures = {0x0bf6e09b: np.ones((8, 8, 4))}

    def render(self, output, **kwargs):
        with patch.object(renderer, 'load_scene', return_value=(None, self.provenance)), \
                patch.object(renderer, 'read_piece_preview', return_value=self.raw), \
                patch.object(renderer, 'TextureLibrary') as library:
            library.return_value.for_model.return_value = (self.textures, [])
            return renderer.render_parts(self.root/'fixture.json', self.build, self.root,
                                         output, prefix='test-part', width=800, height=800,
                                         thumbnail_width=200, **kwargs)

    def test_selected_top_view_keeps_all_angled_images_and_their_evidence_identical(self):
        before, after = self.root/'before', self.root/'after'
        original = self.render(before)
        extended = self.render(after, top_piece_ids=['generic-fan'])
        self.assertEqual(original['schema_version'], 2)
        self.assertNotIn('top_images', original)
        self.assertEqual(extended['schema_version'], 3)
        self.assertEqual(original['images'], extended['images'])
        self.assertEqual(original['placement_images'], extended['placement_images'])
        for image in original['images']:
            for entry in (image, image['thumbnail']):
                self.assertEqual((before/entry['file']).read_bytes(), (after/entry['file']).read_bytes())
        self.assertEqual([image['piece_id'] for image in extended['top_images']], ['generic-fan'])
        self.assertFalse((after/'generic-diverge-top-local-xy.png').exists())

    def test_top_view_is_north_up_and_reuses_exact_saved_geometry_and_local_coordinates(self):
        report = self.render(self.root/'views', top_piece_ids=['generic-diverge', 'generic-fan'])
        angles = {item['piece_id']: item for item in report['images']}
        self.assertEqual(len(report['top_images']), 2)
        for image in report['top_images']:
            angle = angles[image['piece_id']]
            self.assertEqual(image['source'], angle['source'])
            self.assertEqual(image['render_model_sha256'], angle['render_model_sha256'])
            self.assertEqual(image['coordinate_system'], angle['coordinate_system'])
            self.assertEqual(image['display_title'], angle['display_title'])
            self.assertEqual(image['header']['rows'][1]['colour'], '#176eaf')
            self.assertEqual(angle['header']['rows'][1]['colour'], '#176eaf')
            self.assertFalse(image['grid']['tile_scale']['caption_visible'])
            self.assertFalse(angle['grid']['tile_scale']['caption_visible'])
            self.assertEqual(image['view_role'], 'top-down')
            self.assertEqual(image['canonical_filename'], 'preview-top.png')
            self.assertEqual(image['azimuth_degrees'], 0.)
            self.assertEqual(image['elevation_degrees'], 90.)
            self.assertEqual(image['displayed_rotation_ccw_degrees'], 0.)
            self.assertEqual(image['camera']['right_s3d'], [1., 0., -0.])
            self.assertAlmostEqual(image['camera']['up_s3d'][2], -1.)
            self.assertFalse(image['assembly_labels_visible'])
            self.assertFalse(image['coordinate_system']['model_coordinates_changed'])
            self.assertFalse(image['grid']['origin_marker_visible'])
            self.assertTrue(all(label['tile_index'] >= 0 for label in image['grid']['tile_labels']))
            self.assertFalse(any('P00' in caption or 'P01' in caption or 'trumpet' in caption.lower()
                                 for caption in image['captions']))
            self.assertIn('in-game placement and traffic remain unverified', image['captions'][-1])
            with Image.open(self.root/'views'/image['file']) as bitmap:
                self.assertEqual(bitmap.size, (800, 800))

    def test_unknown_top_type_is_rejected_before_output_is_created(self):
        output = self.root/'invalid'
        with self.assertRaisesRegex(ValueError, 'must be used by the audited assembly'):
            self.render(output, top_piece_ids=['absent-type'])
        self.assertFalse(output.exists())

    def test_a_bare_string_cannot_be_misread_as_a_collection_of_type_ids(self):
        output = self.root/'invalid'
        with self.assertRaisesRegex(ValueError, 'collection of exact piece IDs'):
            self.render(output, top_piece_ids='generic-fan')
        self.assertFalse(output.exists())


if __name__ == '__main__':
    unittest.main()
