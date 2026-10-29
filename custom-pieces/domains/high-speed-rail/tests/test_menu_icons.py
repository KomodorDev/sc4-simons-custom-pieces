"""Category labels survive native size, greyscale, and binary menu encoding."""
from copy import deepcopy
from contextlib import redirect_stdout
from io import BytesIO
from io import StringIO
import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from PIL import Image

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp.dbpf import encode_exemplar, exemplar
from scp.catalog import load_catalog
from scp_hsr.icons import icon_identity, main as icons_main, make_icon, validate_icon
from scp_hsr.menu import (DESCRIPTION, EDITED_PROPERTIES, ICON, MENU_EXEMPLAR,
                      TITLE, _read_ltext, build_menu_resources, validate_menu_resources)


def donor():
    ids = (0x10, 0x20, 0x4001, 0x49CAC341, 0x8A2602B8, 0x8A2602B9,
           0x8A2602BB, 0x8A416A99, 0x8A94EEE0, 0xCA416AB5)
    properties = []
    for index, pid in enumerate(ids):
        properties.append({'id': f'{pid:08x}',
                           'type': '0c00' if pid == 0x20 else '0300',
                           'key_type': '0080' if pid in (0x20, 0x8A416A99, 0xCA416AB5) else '0000',
                           'values': ('Native donor' if pid == 0x20 else
                                      [40] if pid == 0x10 else
                                      [1, 2, 3] if pid in (0x8A416A99, 0xCA416AB5) else [100 + index])})
    return encode_exemplar({'parent': [11, 22, 33], 'properties': properties})


def piece(style):
    return {'id': 'menu-label-probe', 'name': 'Example HSR Piece',
            'description': 'A deterministic menu-only test.', 'status': 'experimental',
            'puzzle_id': 'f864',
            'menu': {'id': '6a47f864', 'order': '7011f864', 'style': style}}


class MenuIconCategoryTests(unittest.TestCase):
    def test_artwork_command_writes_only_piece_icons_to_the_source_tree(self):
        catalog = {'domains': {'high-speed-rail': {'path': 'domains/high-speed-rail'}},
                   'pieces': [{'id': 'hsr-test', 'domain': 'high-speed-rail',
                               'menu': {'style': 'cross-dd'}},
                              {'id': 'other-test', 'domain': 'other',
                               'menu': {'style': 'unsupported-other-network'}}]}
        with TemporaryDirectory() as folder:
            root = Path(folder)
            with patch('scp.catalog.load_catalog', return_value=catalog), \
                    patch('sys.argv', ['scp_hsr.icons', '--root', str(root)]), \
                    redirect_stdout(StringIO()):
                icons_main()
            self.assertEqual({p.relative_to(root).as_posix() for p in root.rglob('*')
                              if p.is_file()},
                             {'domains/high-speed-rail/00_pieces/hsr-test/icon.png'})
            icon = root/'domains/high-speed-rail/00_pieces/hsr-test/icon.png'
            self.assertEqual(validate_icon(icon.read_bytes())['state_dimensions'], [44, 44])

    def test_artwork_review_keeps_all_outputs_in_the_explicit_directory(self):
        catalog = {'domains': {'high-speed-rail': {'path': 'domains/high-speed-rail'}},
                   'pieces': [{'id': 'hsr-test', 'domain': 'high-speed-rail',
                               'menu': {'style': 'cross-dd'}}]}
        with TemporaryDirectory() as folder:
            root = Path(folder)/'source'
            output = Path(folder)/'review'
            with patch('scp.catalog.load_catalog', return_value=catalog), \
                    patch('sys.argv', ['scp_hsr.icons', '--root', str(root),
                                       '--output', str(output)]), \
                    redirect_stdout(StringIO()):
                icons_main()
            self.assertFalse(root.exists())
            self.assertEqual({p.relative_to(output).as_posix() for p in output.rglob('*')
                              if p.is_file()},
                             {'hsr-test/icon.png', 'icon-contact-sheet.png'})
            with Image.open(output/'icon-contact-sheet.png') as image:
                self.assertGreater(image.height, 0)

    def test_only_the_two_registered_complete_ts_are_pnp(self):
        result = {}
        for spec in load_catalog(ROOT)['pieces']:
            result[spec['id']] = icon_identity(spec['menu']['style'])['badge']
        self.assertEqual({slug for slug, badge in result.items() if badge == 'PNP'}, {
            'hsr-l2-two-track-t-junction-at-grade-smooth',
            'hsr-l2-two-track-t-junction-diagonal-at-grade-smooth'})

    def test_network_and_type_codes_distinguish_ground_mixed_and_upper_parts(self):
        expected = {
            'interchange-ground-split-45-compact': ('GSR', 'SPL'),
            'interchange-hsr-merge-90-wide': ('HSR', 'MRG'),
            'interchange-l4-oneway-over-ground': ('MIX', 'XNG'),
            'interchange-l4-oneway-over-hsr': ('HSR', 'XNG'),
            'interchange-oneway-grade-ground-to-hsr': ('MIX', 'RMP'),
            'interchange-oneway-grade-l3-to-l4': ('HSR', 'RMP'),
            'rail-ghsr-s-left': ('GSR', 'CRV'),
            'rail-transition': ('MIX', 'RMP'),
            'tram-hsr': ('TRAM', 'XNG'),
            'cross-dd': ('MIX', 'XNG'),
            'hsr-component-tight-paired-curve90-l4-to-mid': ('HSR', 'CRV'),
        }
        for style, wanted in expected.items():
            with self.subTest(style=style):
                result = icon_identity(style)
                self.assertEqual((result['network'], result['kind']), wanted)

    def test_current_reusable_module_kinds_keep_their_part_classification(self):
        expected = {
            'modular-south-junction': 'JCT', 'modular-paired-climb': 'RMP',
            'modular-crossing-core': 'XNG',
            'l2-paired-fan-compact-core': 'JCT',
            'l2-paired-straight-recessed-web': 'STR',
            'l2-short-mainline-diverge-core': 'SPL', 'l2-short-opposed-merge-core': 'MRG',
            'l2-shortened-departure-curve': 'CRV', 'l2-shortened-return-curve': 'CRV',
        }
        for suffix, kind in expected.items():
            with self.subTest(suffix=suffix):
                identity = icon_identity('hsr-component-'+suffix)
                self.assertEqual((identity['kind'], identity['badge'], identity['network']),
                                 (kind, 'PART', 'HSR'))

    def test_native_four_state_strips_include_distinct_colours_and_greyscale(self):
        for style in ('cross-dd', 'rail-ghsr-scissors-revised',
                      'directional-hsr-t-smooth-at-grade',
                      'directional-hsr-t-smooth-diagonal-at-grade'):
            with self.subTest(style=style):
                report = validate_icon(make_icon(style))
                self.assertEqual((report['width'], report['height']), (176, 44))
                self.assertEqual(report['states'], ['locked', 'normal', 'selected', 'highlighted'])
        part = Image.open(BytesIO(make_icon('cross-dd'))).convert('RGBA')
        pnp = Image.open(BytesIO(make_icon('directional-hsr-t-smooth-at-grade'))).convert('RGBA')
        # Antialiasing can move a boundary pixel's RGB value slightly. The
        # channel relationships still independently identify teal and purple.
        teal, purple = part.getpixel((44 + 10, 4)), pnp.getpixel((44 + 10, 4))
        self.assertGreater(teal[1], teal[0] + 100)
        self.assertGreater(purple[2], purple[1] + 60)

    def test_part_word_is_literal_crisp_pixels_in_the_lower_half_of_all_states(self):
        # Independent bitmap samples spell PART. These checks operate on the
        # final PNG, rather than trusting the artwork's own metadata.
        expected = ('110', '101', '101', '110', '100', '100', '100')
        image = Image.open(BytesIO(make_icon('cross-dd'))).convert('RGBA')
        # PART MIX has seven letters plus the three-pixel inter-word advance.
        x0 = 7
        for state in range(4):
            for y, row in enumerate(expected):
                for x, on in enumerate(row):
                    pixel = image.getpixel((state * 44 + x0 + x, 33 + y))
                    if on == '1':
                        self.assertEqual(pixel[3], 255)
                        self.assertGreater(min(pixel[:3]), 230)
                    else:
                        self.assertLess(max(pixel[:3]), 40)

    def test_pnp_word_remains_readable_without_colour(self):
        image = Image.open(BytesIO(make_icon('directional-hsr-t-smooth-at-grade'))).convert('RGBA')
        # Centre PNP HSR in 44 pixels: the P starts at x=9.
        n = ('101', '111', '111', '111', '111', '111', '101')
        for y, row in enumerate(n):
            for x, on in enumerate(row):
                pixel = image.getpixel((13 + x, 33 + y))
                self.assertEqual(pixel[0], pixel[1])
                self.assertEqual(pixel[1], pixel[2])
                self.assertEqual(pixel[0] > 230, on == '1')

    def test_menu_category_is_explicit_in_native_title_and_tooltip(self):
        for style, badge in (('cross-dd', 'PART'),
                             ('directional-hsr-t-smooth-at-grade', 'PNP')):
            spec = piece(style)
            resources, report = build_menu_resources(donor(), spec)
            iid = int(spec['menu']['id'], 16)
            self.assertEqual(_read_ltext(resources[*TITLE, iid]),
                             f'SCP | [{badge}] Example HSR Piece')
            description = _read_ltext(resources[*DESCRIPTION, iid])
            self.assertIn(f'({badge})', description)
            self.assertIn('Experimental', description)
            self.assertEqual(report['icon_identity']['badge'], badge)
            self.assertTrue(report['retained_native_properties_verified'])
            before, after = exemplar(donor()), exemplar(resources[*MENU_EXEMPLAR, iid])
            self.assertEqual(before['parent'], after['parent'])
            self.assertEqual([p['id'] for p in before['properties']],
                             [p['id'] for p in after['properties']])
            for a, b in zip(before['properties'], after['properties']):
                if int(a['id'], 16) not in EDITED_PROPERTIES:
                    self.assertEqual(a, b)

    def test_category_does_not_hide_design_warning(self):
        spec = piece('cross-dd')
        spec['design_review'] = {'status': 'review-needed', 'summary': 'Inspect pillar spacing.',
                                 'reasons': ['Spacing needs a visual review.']}
        resources, _ = build_menu_resources(donor(), spec)
        iid = int(spec['menu']['id'], 16)
        self.assertIn('[PART] [REVIEW NEEDED]', _read_ltext(resources[*TITLE, iid]))
        self.assertTrue(_read_ltext(resources[*DESCRIPTION, iid]).startswith(
            'REVIEW NEEDED: Inspect pillar spacing.'))

    def test_wrong_category_artwork_is_rejected_even_with_valid_png(self):
        spec = piece('cross-dd')
        resources, _ = build_menu_resources(donor(), spec)
        resources = deepcopy(resources)
        resources[*ICON, int(spec['menu']['id'], 16)] = make_icon('directional-hsr-t-smooth-at-grade')
        with self.assertRaisesRegex(ValueError, 'artwork does not match'):
            validate_menu_resources(resources, donor(), spec)


if __name__ == '__main__':
    unittest.main()
