"""Shared render names, real camera labels, and the three-row caption contract."""
from pathlib import Path
import sys
import unittest

from PIL import Image, ImageDraw

ROOT=next(p for p in Path(__file__).resolve().parents if (p/'project.jsonc').is_file())
sys.path.insert(0,str(ROOT/'framework'))
from scp.preview import font
from scp.render_headers import draw_header, piece_heading, piece_title, view_caption


class RenderHeaderTests(unittest.TestCase):
    def test_level_names_gain_measured_heights_without_repeating_nominal_levels(self):
        records=[{'id':'low','nominal_level':'L2','path_height_m':15.5},
                 {'id':'high','nominal_level':'L4','path_height_m':30.5}]
        title=piece_title('test-curve',records,'HSR Paired Quarter-Turn Level 2 to Level 4')
        self.assertEqual(title,'Piece - HSR Paired Quarter-Turn Level 2 (15.5 m) to Level 4 (30.5 m)')
        mixed=[{'id':'road','nominal_level':'L0','path_height_m':0.},records[0]]
        self.assertEqual(piece_title('test-road',mixed,'HSR Level 2 above Parallel Road Level 0'),
                         'Piece - HSR Level 2 (15.5 m) above Parallel Road Level 0 (0 m)')
        self.assertEqual(piece_title('test-custom',[{'id':'custom','nominal_level':None,'path_height_m':23.}],
                                     'HSR Custom End'),'Piece - HSR Custom End — Custom (23 m)')

    def test_piece_prefix_is_idempotent_and_does_not_change_an_internal_name_fragment(self):
        name='HSR Replacement Piece - Junction'
        for source in (name,'Piece - '+name,'Piece - Piece - '+name):
            with self.subTest(source=source):
                self.assertEqual(piece_heading(source),'Piece - '+name)
        for source in ('', ' ', 'Piece - ', None):
            with self.subTest(source=source),self.assertRaisesRegex(ValueError,'source-backed name'):
                piece_heading(source)

    def test_camera_caption_follows_world_direction_instead_of_an_invented_view(self):
        self.assertIn('Southeast view',view_caption(azimuth=45.,elevation=31.))
        self.assertIn('Southwest view',view_caption(azimuth=315.,elevation=31.))
        self.assertIn('Top view, north up',view_caption('top',0.,90.))
        self.assertIn('Connection overview',view_caption('connection-overview'))

    def test_second_row_leads_with_purpose_without_losing_camera_or_orientation(self):
        for role,azimuth,elevation,purpose,camera in (
                ('angled',45.,31.,'Clean view','Southeast view'),
                ('top',0.,90.,'Clean view','Top view, north up'),
                ('connection-overview',45.,31.,'Connection overview','Southeast view')):
            with self.subTest(role=role):
                self.assertEqual(view_caption(role,azimuth,elevation),
                                 f'{purpose} | {camera} | Authored orientation: 0°')
        with self.assertRaisesRegex(ValueError,'view purpose'):
            view_caption('not-a-real-view')

    def test_abbreviated_levels_normalize_without_an_extra_height_suffix(self):
        records=[{'id':'hsr','nominal_level':'L2','path_height_m':15.5},
                 {'id':'road','nominal_level':'L0','path_height_m':0.}]
        expected='Piece - HSR Level 2 (15.5 m) above Parallel Road Level 0 (0 m)'
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
                                 'Piece - HSR Level 2 (15.5 m)')

    def test_level_like_identifiers_and_unknown_levels_are_not_guessed(self):
        records=[{'id':'hsr','nominal_level':'L2','path_height_m':15.5}]
        self.assertEqual(piece_title('test-id',records,'XL2 L2Connector L20'),
                         'Piece - XL2 L2Connector L20 — Level 2 (15.5 m)')

    def test_an_ambiguous_level_keeps_both_verified_heights_visible(self):
        records=[{'id':'first','nominal_level':'L2','path_height_m':15.5},
                 {'id':'second','nominal_level':'L2','path_height_m':16.}]
        self.assertEqual(piece_title('test-ambiguous',records,'HSR L2'),
                         'Piece - HSR L2 — Level 2 (15.5 m) / Level 2 (16 m)')

    def test_canonical_names_identify_curve_ramps_and_crossings(self):
        cases=[
            ('hsr-h23000mm-and-l4-two-track-curve-ramp-90deg-tight',
             [{'id':'curve-end-b','nominal_level':None,'path_height_m':23.},
              {'id':'curve-end-a','nominal_level':'L4','path_height_m':30.5}],
             'HSR Custom (23 m) ↔ Level 4 (30.5 m) — Two-Track Curve 90° Ramp — Tight'),
            ('hsr-l4-over-hsr-l2-two-track-crossing-90deg',
             [{'id':'lower-end-a','nominal_level':'L2','path_height_m':15.5},
              {'id':'upper-end-a','nominal_level':'L4','path_height_m':30.5}],
             'HSR Level 4 (30.5 m) over HSR Level 2 (15.5 m) — Two-Track Crossing 90°')]
        for identifier,records,name in cases:
            with self.subTest(identifier=identifier):
                self.assertEqual(piece_title(identifier,records,name),'Piece - '+name)

    def test_mixed_services_keep_each_known_height_visible_once(self):
        records=[{'id':'hsr','nominal_level':'L2','path_height_m':15.5},
                 {'id':'road','nominal_level':'L0','path_height_m':0.},
                 {'id':'pedestrian','nominal_level':None,'path_height_m':0.}]
        name='HSR Level 2 (15.5 m) over Road Level 0 (0 m) — Parallel Stack'
        self.assertEqual(piece_title('hsr-l2-over-road-l0-mixed-parallel-stack',records,name),
                         'Piece - '+name)
        ground=[records[0],{'id':'tram','nominal_level':None,'path_height_m':0.}]
        tram='HSR Level 2 (15.5 m) over Tram Ground (0 m) — Crossing 90°'
        self.assertEqual(piece_title('hsr-l2-over-tram-ground-mixed-crossing-90deg',ground,tram),
                         'Piece - '+tram)

    def test_names_normalize_measured_levels_and_retain_unrepresented_heights(self):
        records=[{'id':'low','nominal_level':'L2','path_height_m':15.5},
                 {'id':'custom','nominal_level':None,'path_height_m':23.}]
        name='HSR Level 2 (16 m) — Two-Track Adapter'
        self.assertEqual(piece_title('test-adapter',records,name),
                         'Piece - HSR Level 2 (15.5 m) — Two-Track Adapter — Custom (23 m)')

    def test_header_rows_have_consistent_colours_and_fit_the_reserved_width(self):
        canvas=Image.new('RGB',(1600,300),'white');draw=ImageDraw.Draw(canvas)
        captions=['Piece - HSR Paired Quarter-Turn Level 2 (15.5 m) to Level 4 (30.5 m)',
                  view_caption(), 'Independent local X/Y grid / 1 tile = 16 m / Labels mark tile centres']
        result=draw_header(draw,captions,1600,font,margin=30,top=20)
        self.assertEqual([row['colour'] for row in result['rows']],['#172b42','#176eaf','#586a7e'])
        self.assertEqual([row['bold'] for row in result['rows']],[True,False,False])
        self.assertEqual(result['captions'],captions)
        self.assertTrue(all(row['bounds'][0]>=30 and row['bounds'][2]<=1570 for row in result['rows']))
        self.assertGreaterEqual(result['bottom'],result['rows'][-1]['bounds'][3])

    def test_draw_contract_rejects_unlabelled_or_duplicate_titles_and_camera_first_subtitles(self):
        draw=ImageDraw.Draw(Image.new('RGB',(1600,300),'white'))
        grid='Independent local X/Y grid / 1 tile = 16 m / Labels mark tile centres'
        for title in ('HSR example','Piece - Piece - HSR example'):
            with self.subTest(title=title),self.assertRaisesRegex(ValueError,'exactly one Piece - prefix'):
                draw_header(draw,[title,view_caption(),grid],1600,font)
        with self.assertRaisesRegex(ValueError,'lead with its view purpose'):
            draw_header(draw,['Piece - HSR example','Southeast view / Clean view',grid],1600,font)


if __name__=='__main__':unittest.main()
