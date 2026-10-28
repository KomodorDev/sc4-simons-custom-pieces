"""Assembly image headers keep identity separate from each view's purpose."""
from copy import deepcopy
import hashlib
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np

from scp.models import pack_s3d, parse_s3d
from scp_hsr.test_support import donor
from scp_hsr_tools import render_hsr_assembly as renderer


class AssemblyImageHeaderTests(unittest.TestCase):
    def test_existing_prefix_is_idempotent_and_invalid_headers_are_rejected(self):
        rows = renderer.assembly_caption_rows('Straight-stem HSR trumpet', 'Clean view', 'Top view | north up')
        self.assertEqual(rows, ('Assembly - Straight-stem HSR trumpet', 'Clean view | Top view | north up'))
        self.assertEqual(renderer.assembly_caption_rows(rows[0], 'Clean view', 'Top view | north up'), rows)
        self.assertEqual(renderer.assembly_caption_rows('Assembly - '+rows[0], 'Clean view', 'Top view | north up'), rows)
        for arguments in (('', 'Clean view', 'Top view'), ('Assembly - ', 'Clean view', 'Top view'),
                          ('Assembly - Assembly - ', 'Clean view', 'Top view'),
                          ('Fixture', 'unknown', 'Top view'), ('Fixture', 'Clean view', '')):
            with self.subTest(arguments=arguments), self.assertRaises(ValueError):
                renderer.assembly_caption_rows(*arguments)

    def test_actual_six_image_render_uses_class_first_second_rows_and_one_assembly_name(self):
        model = parse_s3d(donor())
        expected_model = hashlib.sha256(pack_s3d(model)).hexdigest()
        provenance = {'title': 'Fixture junction',
            'placement_plan_title': 'Legacy plan role must not enter the assembly name',
            'sources': [{'id': 'fixture', 'piece_id': 'fixture', 'label': 'P01',
                'menu_name': 'Fixture track', 'origin_m': [0., 0.],
                'rotation_ccw_degrees': 0., 'display_origin_tiles_en': [0., 0.],
                'label_anchor_world_m': [0., 0., 15.5], 'occupied_world_cells': [[0., 0.]]}],
            'coordinate_system': {'origin_world_m': [0., 0.]}}
        original = deepcopy(provenance)
        with tempfile.TemporaryDirectory() as temporary, \
                patch.object(renderer, 'TextureLibrary') as library, \
                patch.object(renderer, '_caption', wraps=renderer._caption) as caption:
            library.return_value.for_model.return_value = ({0x0bf6e09b: np.ones((8, 8, 4))}, [])
            report = renderer.render_assembly(model, Path(temporary), Path(temporary)/'images',
                provenance=provenance, width=2000, height=1400, prefix='fixture')
        expected_second_rows = [
            'Component guide | Southeast view | looking northwest',
            'Clean view | Southeast view | looking northwest',
            'Component guide | Northwest view | looking southeast',
            'Component guide | Top view | north up',
            'Clean view | Top view | north up',
            'Construction view | Top view | north up',
        ]
        self.assertEqual(len(report['images']), 6)
        self.assertEqual([image['header_rows'][1] for image in report['images']], expected_second_rows)
        self.assertEqual({image['header_rows'][0] for image in report['images']}, {'Assembly - Fixture junction'})
        self.assertEqual([image['label'] for image in report['images']], expected_second_rows)
        drawn_rows = [call.args[1] for call in caption.call_args_list if call.args[2] in (22, 72)]
        self.assertEqual(drawn_rows, [row for image in report['images'] for row in image['header_rows']])
        all_visible_captions = ' '.join(call.args[1] for call in caption.call_args_list)
        self.assertNotRegex(all_visible_captions.lower(), r'\bunverified\b|\bpassed\b|\bfailed\b|not verified in.game')
        self.assertIn('software preview', all_visible_captions)
        self.assertEqual(report['render_model_sha256'], expected_model)
        self.assertFalse(report['geometry_hidden'])
        self.assertFalse(report['geometry_simplified'])
        self.assertFalse(report['in_game_evidence'])
        self.assertEqual(provenance, original)


if __name__ == '__main__':
    unittest.main()
