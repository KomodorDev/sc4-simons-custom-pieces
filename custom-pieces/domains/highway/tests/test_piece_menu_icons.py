"""Verify current Highway standalone artwork and exact frozen compatibility."""
from io import BytesIO
from pathlib import Path
import struct
import sys
import unittest
from zlib import crc32

from PIL import Image

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'framework'))

from scp.catalog import load_catalog
from scp.check_bootstrap import SourcePackages

sys.meta_path.insert(0, SourcePackages(ROOT))

from scp_highway import menu, piece_icons


class HighwayPieceMenuIconsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        catalog = load_catalog(ROOT)
        cls.pieces = {p['id']: p for p in catalog['pieces']
                      if p['domain'] == 'highway' and p['status'] != 'draft'}
        cls.directory = ROOT / catalog['domains']['highway']['path'] / '00_pieces'

    def test_current_canonical_artwork_matches_each_registered_piece(self):
        for identifier, piece in self.pieces.items():
            with self.subTest(piece=identifier):
                expected = piece_icons.make_piece_icon(piece)
                canonical = (self.directory / identifier / 'icon.png').read_bytes()
                piece_icons.validate_piece_icon(canonical, expected=expected)

    def test_variant_icons_use_side_and_travel_independently(self):
        from scp_highway import diagonal_transition_variants, orthogonal_transition_variants
        for variants in (diagonal_transition_variants, orthogonal_transition_variants):
            with self.subTest(family=variants.__name__):
                strips = {piece_icons.make_piece_icon(self.pieces[identifier])
                          for identifier in variants.PIECE_IDS}
                self.assertEqual(len(strips), 4)
        for component in ('diagonal-stem-split', 'diagonal-branch', 'orthogonal-core'):
            with self.subTest(component=component):
                first, second = (self.pieces['ddrhw-y-'+phase+component] for phase in ('', 'reversed-'))
                self.assertNotEqual(piece_icons.make_piece_icon(first), piece_icons.make_piece_icon(second))

    def test_locked_state_rejects_colour_with_all_other_frames_retained(self):
        piece = self.pieces['ddrhw-y-orthogonal-core']
        strip = Image.open(BytesIO(piece_icons.make_piece_icon(piece)))
        strip.putpixel((22, 22), (200, 80, 20, 255))
        output = BytesIO()
        strip.save(output, format='PNG')
        with self.assertRaisesRegex(ValueError, 'locked icon must be greyscale'):
            piece_icons.validate_piece_icon(output.getvalue())

    def test_single_native_strip_rejects_apng_and_truncated_header(self):
        raw = piece_icons.make_piece_icon(self.pieces['ddrhw-y-orthogonal-core'])
        with self.assertRaisesRegex(ValueError, 'Wrong Highway icon PNG format'):
            piece_icons.validate_piece_icon(raw[:20])
        # Pillow's single-frame save emits a static PNG. Add real APNG
        # control chunks while keeping the original image data unchanged.
        def chunk(kind, data):
            return struct.pack('>I', len(data))+kind+data+struct.pack('>I', crc32(kind+data))
        control = chunk(b'acTL', struct.pack('>II', 1, 0))
        control += chunk(b'fcTL', struct.pack('>IIIIIHHBB', 0, 176, 44, 0, 0, 1, 10, 0, 0))
        with self.assertRaisesRegex(ValueError, 'single RGBA PNG'):
            piece_icons.validate_piece_icon(raw[:33]+control+raw[33:])

    def test_current_menu_accepts_equal_png_pixels_and_rejects_a_changed_pixel(self):
        piece = self.pieces['ddrhw-y-orthogonal-core']
        donor = menu.portable_baseline()
        resources, _report = menu.build_menu_resources(donor, piece)
        key = (*menu.ICON, int(piece['menu']['id'], 16))
        strip = Image.open(BytesIO(resources[key]))
        output = BytesIO()
        strip.save(output, format='PNG', compress_level=0)
        alternative = output.getvalue()
        self.assertNotEqual(alternative, resources[key])
        menu.validate_menu_resources({**resources, key: alternative}, donor, piece,
                                     icon_artwork=piece_icons.ARTWORK)
        strip.putpixel((44+22, 22), (200, 80, 20, 255))
        output = BytesIO()
        strip.save(output, format='PNG', compress_level=0)
        with self.assertRaisesRegex(ValueError, 'artwork pixels differ'):
            menu.validate_menu_resources({**resources, key: output.getvalue()}, donor, piece,
                                         icon_artwork=piece_icons.ARTWORK)

    def test_saved_menu_version_never_accepts_the_other_artwork(self):
        piece = self.pieces['ddrhw-y-orthogonal-core']
        donor = menu.portable_baseline()
        resources, report = menu.build_menu_resources(donor, piece)
        self.assertEqual(report['icon_artwork'], piece_icons.ARTWORK)
        key = (*menu.ICON, int(piece['menu']['id'], 16))
        self.assertEqual(resources[key], piece_icons.make_piece_icon(piece))
        with self.assertRaisesRegex(ValueError, 'Wrong highway menu icon'):
            menu.validate_menu_resources(resources, donor, piece)
        historical = {**resources, key: menu.make_icon(piece['menu']['style'])}
        self.assertNotIn('icon_artwork', menu.validate_menu_resources(historical, donor, piece))
        with self.assertRaisesRegex(ValueError, 'Wrong highway menu icon'):
            menu.validate_menu_resources(historical, donor, piece, icon_artwork=piece_icons.ARTWORK)
        with self.assertRaisesRegex(ValueError, 'Unknown Highway menu artwork revision'):
            menu.validate_menu_resources(resources, donor, piece, icon_artwork='unknown')


if __name__ == '__main__':
    unittest.main()
