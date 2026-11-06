"""Assembly image headers keep identity separate from each view's purpose."""
from copy import deepcopy
import hashlib
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np

from scp.models import pack_s3d, parse_s3d
from scp.subject_sources import new_subject_document
from scp_hsr.test_support import donor
from scp_hsr_tools import render_hsr_assembly as renderer


class AssemblyImageHeaderTests(unittest.TestCase):
    def test_jsonc_scene_loads_actual_models_and_preserves_the_exact_source_fingerprint(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            raw = donor()
            (directory/'fixture.s3d').write_bytes(raw)
            plan = {'title':'Commented assembly fixture', 'placements':[
                {'instance_id':'P01', 'model_file':'fixture.s3d', 'origin_m':[0.,0.]}]}
            source = new_subject_document(plan, 'assembly').encode('utf-8')
            path = directory/'assembly.jsonc'
            path.write_bytes(source)
            model, provenance = renderer.load_scene(path)
        self.assertTrue(model['meshes'])
        self.assertEqual(provenance['title'], plan['title'])
        self.assertEqual(provenance['scene_sha256'], hashlib.sha256(source).hexdigest())
        self.assertEqual(provenance['sources'][0]['model_sha256'], hashlib.sha256(raw).hexdigest())

    def test_existing_prefix_is_idempotent_and_invalid_headers_are_rejected(self):
        rows = renderer.assembly_caption_rows('HSR \u2014 Trumpet \u2014 Straight Stem', 'Clean view', 'Top view | north up')
        self.assertEqual(rows, ('Assembly - HSR \u2014 Trumpet \u2014 Straight Stem', 'Clean view | Top view | north up'))
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
            'coordinate_system': {'origin_world_m': [0., 0.],
                                  'display_bounds_world_m': [-24., -8., 24., 8.]}}
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
        for image in report['images']:
            self.assertEqual(image['grid']['bounds_world_m'], [-24., -8., 24., 8.])
        drawn_rows = [call.args[1] for call in caption.call_args_list if call.args[2] in (22, 72)]
        self.assertEqual(drawn_rows, [row for image in report['images'] for row in image['header_rows']])
        all_visible_captions = ' '.join(call.args[1] for call in caption.call_args_list)
        self.assertNotRegex(all_visible_captions.lower(), r'\bunverified\b|\bpassed\b|\bfailed\b|not verified in.game')
        self.assertIn('software preview', all_visible_captions)
        self.assertEqual(report['render_model_sha256'], expected_model)
        self.assertFalse(report['geometry_hidden'])
        self.assertFalse(report['geometry_simplified'])
        self.assertFalse(report['in_game_evidence'])
        construction = next(image for image in report['images']
                            if image['variant']=='construction-plan')
        self.assertFalse(construction['construction_layers']['model_underlay'])
        self.assertEqual(construction['construction_layers']['ownership_fill_opacity'],1.)
        self.assertEqual(provenance, original)

    def test_explicit_display_grid_cannot_crop_or_cut_through_occupied_tiles(self):
        vertices = [(-8., 15.5, -8.), (8., 15.5, 8.)]
        sources = [{'occupied_world_cells': [[0., 0.], [16., 0.]]}]
        for bounds, error in (([-8., -8., 8., 8.], 'enclose'),
                              ([-8., -8., 32., 8.], 'tile edges')):
            with self.subTest(bounds=bounds), self.assertRaisesRegex(ValueError, error):
                renderer._grid_bounds(vertices, sources, bounds)

    def test_other_domain_can_supply_its_saved_textures_and_measured_caption_rows(self):
        model = parse_s3d(donor())
        source = 'Actual compiled S3D pavement, decks, barriers, and supports | software preview'
        heights = 'Car-path pavement heights: avenue 0 m | lower deck 7.5 m | upper deck 15 m'
        footer = 'All model geometry shown; no simulated traffic, terrain, or game lighting.'
        owned = {0x0bf6e09b: b'exact fixture FSH bytes'}
        provenance = {'title': 'Highway fixture', 'sources': [
            {'id': 'fixture', 'piece_id': 'fixture', 'label': 'P01',
             'menu_name': 'Highway fixture component', 'origin_m': [0., 0.],
             'rotation_ccw_degrees': 0., 'display_origin_tiles_en': [0., 0.],
             'label_anchor_world_m': [0., 0., 15.5],
             'occupied_world_cells': [[-16., -16.], [0., 0.], [16., 16.]]}]}
        with tempfile.TemporaryDirectory() as temporary, \
                patch.object(renderer, 'TextureLibrary') as library, \
                patch.object(renderer, '_caption', wraps=renderer._caption) as caption, \
                patch.object(renderer, 'render_fast_view',
                             side_effect=lambda *args, **kwargs: kwargs['background_image']):
            library.return_value.for_model.return_value = ({}, [])
            report = renderer.render_assembly(model, Path(temporary), Path(temporary)/'images',
                provenance=provenance, width=2000, height=1400, prefix='fixture',
                owned_texture_resources=owned, source_caption=source,
                height_caption=heights, footer_caption=footer, minimum_display_index=0)
        library.return_value.for_model.assert_called_once_with(model, owned_resources=owned)
        rows = [call.args[1] for call in caption.call_args_list]
        self.assertEqual(rows.count(source), 5)
        self.assertEqual(rows.count(heights), 3)
        self.assertEqual(rows.count(footer), 5)
        self.assertNotIn('Actual compiled S3D track, decks, and supports | software preview', rows)
        self.assertEqual(report['renderer']['presentation_captions'], {
            'source': source, 'height': heights, 'model_footer': footer})
        self.assertEqual(len(report['images']), 6)
        for image in report['images']:
            labels = image['grid']['tile_labels']
            self.assertTrue(labels)
            self.assertTrue(all(label['tile_index'] >= 0 for label in labels))
            self.assertEqual(image['grid']['display_coordinate_basis']['minimum_display_index'], 0)
            self.assertEqual(image['grid']['bounds_world_m'], [-24., -24., 24., 24.])
        palettes = [image['piece_labels']['palette'] for image in report['images']
                    if image.get('piece_labels')]
        self.assertTrue(all(palette == report['colour_assignment']['palette'] for palette in palettes))

    def test_construction_underlay_shares_camera_and_only_blends_owned_fills(self):
        from PIL import Image, ImageColor
        from scp.models import positions

        model = parse_s3d(donor())
        model_before = pack_s3d(model)
        vertices = [point for block in model['vertices'] for point in positions(block)]
        sources = [{'id':'fixture', 'piece_id':'fixture', 'label':'P01',
                    'menu_name':'Fixture component', 'origin_m':[0.,0.],
                    'rotation_ccw_degrees':0., 'display_origin_tiles_en':[0.,0.],
                    'label_anchor_world_m':[0.,0.,15.5], 'occupied_world_cells':[[0.,0.]]}]
        sources_before = deepcopy(sources)
        colours = renderer.colour_assignment_for_sources(sources)
        fill = ImageColor.getrgb(colours['ownership_fill_palette']['P01'])
        base = (20,40,60)
        textures = {0x0bf6e09b:np.ones((8,8,4))}

        def actual_view(*args, **kwargs):
            return Image.new('RGB', (args[4],args[5]), base)

        for opacity in (0.,.30,1.):
            with self.subTest(opacity=opacity), \
                    patch.object(renderer,'render_fast_view',side_effect=actual_view) as render, \
                    patch.object(renderer,'draw_piece_callouts',return_value={}):
                image, evidence = renderer._placement_plan(
                    vertices,sources,(-24.,-24.,24.,24.),(0.,0.),2000,1400,400,190,
                    title='Fixture junction',colour_assignment=colours,
                    model=model,textures=textures,fill_opacity=opacity)
            render.assert_called_once()
            self.assertIs(render.call_args.args[0],model)
            self.assertIs(render.call_args.args[1],textures)
            self.assertEqual(render.call_args.args[2:4],(0.,90.))
            camera = render.call_args.kwargs['camera']
            self.assertEqual(camera.metadata(),evidence['camera'])

            def pixel(east,north):
                x,y = camera.project_world(east,north)
                return image.getpixel((400+round(x),190+round(y)))

            alpha = round(255*opacity)/255.
            expected = tuple(round(alpha*colour+(1.-alpha)*background)
                             for colour,background in zip(fill,base))
            self.assertTrue(all(abs(a-b)<=1 for a,b in zip(pixel(3.,2.),expected)))
            self.assertEqual(pixel(16.,2.),base)  # Unowned cells retain the model underneath.
            self.assertEqual(pixel(8.,2.),(16,33,45))  # Ownership boundaries stay opaque.
            layers = evidence['construction_layers']
            self.assertTrue(layers['model_underlay_uses_ownership_camera'])
            self.assertEqual(layers['ownership_fill_opacity'],opacity)
            self.assertTrue(layers['unowned_cells_have_no_fill'])
            self.assertTrue(layers['boundaries_labels_and_callouts_opaque'])
        self.assertEqual(pack_s3d(model),model_before)
        self.assertEqual(sources,sources_before)


if __name__ == '__main__':
    unittest.main()
