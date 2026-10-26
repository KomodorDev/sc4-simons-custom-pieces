"""Shared render names, real camera labels, and the three-row caption contract."""
from pathlib import Path
import sys
import unittest

from PIL import Image, ImageDraw

ROOT=next(p for p in Path(__file__).resolve().parents if (p/'project.json').is_file())
sys.path.insert(0,str(ROOT/'framework'))
from scp.preview import font
from scp.render_headers import draw_header, piece_title, view_caption


class RenderHeaderTests(unittest.TestCase):
    def test_level_names_gain_measured_heights_without_repeating_nominal_levels(self):
        records=[{'id':'low','nominal_level':'L2','path_height_m':15.5},
                 {'id':'high','nominal_level':'L4','path_height_m':30.5}]
        title=piece_title('test-curve',records,'HSR Paired Quarter-Turn Level 2 to Level 4')
        self.assertEqual(title,'HSR Paired Quarter-Turn Level 2 (15.5 m) to Level 4 (30.5 m)')
        mixed=[{'id':'road','nominal_level':'L0','path_height_m':0.},records[0]]
        self.assertEqual(piece_title('test-road',mixed,'HSR Level 2 above Parallel Road Level 0'),
                         'HSR Level 2 (15.5 m) above Parallel Road Level 0 (0 m)')
        self.assertEqual(piece_title('test-custom',[{'id':'custom','nominal_level':None,'path_height_m':23.}],
                                     'HSR Custom End'),'HSR Custom End — Custom (23 m)')

    def test_camera_caption_follows_world_direction_instead_of_an_invented_view(self):
        self.assertIn('Southeast view',view_caption(azimuth=45.,elevation=31.))
        self.assertIn('Southwest view',view_caption(azimuth=315.,elevation=31.))
        self.assertIn('Top view, north up',view_caption('top',0.,90.))
        self.assertIn('Connection overview',view_caption('connection-overview'))

    def test_abbreviated_levels_normalize_without_an_extra_height_suffix(self):
        records=[{'id':'hsr','nominal_level':'L2','path_height_m':15.5},
                 {'id':'road','nominal_level':'L0','path_height_m':0.}]
        expected='HSR Level 2 (15.5 m) above Parallel Road Level 0 (0 m)'
        for name in ('HSR L2 above Parallel Road L0',
                     'HSR l2 above Parallel Road LEVEL 0',
                     'HSR L2 (15.5 m) above Parallel Road L0 (0 m)'):
            with self.subTest(name=name):
                self.assertEqual(piece_title('test-stack',records,name),expected)

    def test_measured_height_replaces_an_old_annotation_in_the_source_name(self):
        records=[{'id':'hsr','nominal_level':'L2','path_height_m':15.5}]
        for name in ('HSR L2 (16 m)', 'HSR Level 2 (1.6e1 m)'):
            with self.subTest(name=name):
                self.assertEqual(piece_title('test-height',records,name),
                                 'HSR Level 2 (15.5 m)')

    def test_level_like_identifiers_and_unknown_levels_are_not_guessed(self):
        records=[{'id':'hsr','nominal_level':'L2','path_height_m':15.5}]
        self.assertEqual(piece_title('test-id',records,'XL2 L2Connector L20'),
                         'XL2 L2Connector L20 — Level 2 (15.5 m)')

    def test_an_ambiguous_level_keeps_both_verified_heights_visible(self):
        records=[{'id':'first','nominal_level':'L2','path_height_m':15.5},
                 {'id':'second','nominal_level':'L2','path_height_m':16.}]
        self.assertEqual(piece_title('test-ambiguous',records,'HSR L2'),
                         'HSR L2 — Level 2 (15.5 m) / Level 2 (16 m)')

    def test_header_rows_have_consistent_colours_and_fit_the_reserved_width(self):
        canvas=Image.new('RGB',(1600,300),'white');draw=ImageDraw.Draw(canvas)
        captions=['HSR Paired Quarter-Turn Level 2 (15.5 m) to Level 4 (30.5 m)',
                  view_caption(), 'Independent local X/Y grid / 1 tile = 16 m / Labels mark tile centres']
        result=draw_header(draw,captions,1600,font,margin=30,top=20)
        self.assertEqual([row['colour'] for row in result['rows']],['#172b42','#176eaf','#586a7e'])
        self.assertEqual([row['bold'] for row in result['rows']],[True,False,False])
        self.assertEqual(result['captions'],captions)
        self.assertTrue(all(row['bounds'][0]>=30 and row['bounds'][2]<=1570 for row in result['rows']))
        self.assertGreaterEqual(result['bottom'],result['rows'][-1]['bounds'][3])


if __name__=='__main__':unittest.main()
