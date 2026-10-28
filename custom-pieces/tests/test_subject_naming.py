"""Check current subject identities, copied names, and source-backed heights."""
import json
from pathlib import Path
import re
import unittest

from scp import jsonc
from scp.catalog import load_catalog
from scp.subject_identity import canonical_piece_id, legacy_piece_id, piece_directory
from scp_hsr.menu import _spec_fields

ROOT = Path(__file__).resolve().parents[1]


class SubjectNamingIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = load_catalog(ROOT)
        cls.migration = jsonc.load(ROOT/'config/subject-id-migration.jsonc')
        cls.pieces = {piece['id']: piece for piece in cls.catalog['pieces']}

    def test_every_migrated_piece_resolves_to_its_registered_folder_and_original_recipe(self):
        for entry in self.migration['pieces']:
            with self.subTest(piece=entry['new_id']):
                identifier = entry['new_id']
                piece = self.pieces[identifier]
                self.assertEqual(piece['recipe'], entry['recipe'])
                self.assertEqual(canonical_piece_id(piece['recipe'], ROOT), identifier)
                self.assertEqual(legacy_piece_id(identifier, ROOT), entry['old_id'])
                directory = piece_directory(piece['recipe'], ROOT)
                self.assertEqual(directory.name, identifier)
                self.assertTrue((directory/'piece.json').is_file())
                self.assertFalse((directory.with_name(entry['old_id'])/'piece.json').exists())
                self.assertRegex(identifier, r'^[a-z](?:[a-z0-9]|-[a-z0-9])+$')
                self.assertLessEqual(len(identifier), 64)

    def test_migrated_names_retain_measured_heights_and_drive_the_actual_menu_title(self):
        for entry in self.migration['pieces']:
            with self.subTest(piece=entry['new_id']):
                piece = self.pieces[entry['new_id']]
                name = piece['name']
                self.assertIn(' — ', name)
                self.assertEqual(name, name.strip())
                self.assertNotRegex(name, r'[\t\r\n]|  ')
                directory = piece_directory(piece['recipe'], ROOT)
                measurements = json.loads((directory/'connections.json').read_text())
                heights = [port['endpoint_m'][2] for port in measurements['ports']]
                declared = re.findall(r'\(([+-]?[\d.]+) m\)', name)
                self.assertTrue(declared)
                for height in declared:
                    self.assertTrue(any(abs(float(height)-value) < 1e-6 for value in heights),
                                    f'{height} m is not a measured interface of {name}')
                actual = _spec_fields(piece)['title']
                self.assertTrue(actual.endswith(name))
                self.assertEqual(actual.count(name), 1)

    def test_assembly_placements_and_installed_button_use_canonical_names(self):
        for assembly in self.catalog['_assemblies']:
            scene = assembly['scene']
            for placement in scene.get('placements', scene.get('instances', [])):
                piece = self.pieces[placement['piece_id']]
                self.assertEqual(placement['recipe'], piece['recipe'])
                if 'menu_name' in placement:
                    self.assertEqual(placement['menu_name'], piece['name'])
                if 'name' in placement:
                    self.assertTrue(placement['name'].startswith(piece['name']))
            domain = ROOT/self.catalog['domains'][assembly['domain']]['path']
            layouts = jsonc.load(domain/'menu-layout.jsonc')['layouts']
            for layout in layouts.values():
                if layout['assembly_id'] == assembly['id']:
                    self.assertEqual(layout['cycle_button']['title'], 'SCP | ASSEMBLY | '+scene['title'])


if __name__ == '__main__':
    unittest.main()
