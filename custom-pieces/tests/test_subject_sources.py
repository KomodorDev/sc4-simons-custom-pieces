"""Resolve recipe ownership from current registries and source manifests."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp import jsonc
from scp.subject_sources import piece_directory, piece_id_for_recipe, piece_name_for_recipe


class SubjectSourceTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix='scp-subject-sources-')
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.recipe = 'hsr_test_recipe'
        self.identifier = 'hsr-l2-two-track-straight'
        self.domain = 'high-speed-rail'
        self._write('project.jsonc', {'schema_version': 1, 'domains': {
            self.domain: {'path': f'domains/{self.domain}',
                          'registry': f'domains/{self.domain}/domain.jsonc'}}})
        self._write(f'domains/{self.domain}/domain.jsonc', {'pieces': []})

    def _write(self, relative, data):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data) + '\n', encoding='utf-8')
        return path

    def _register(self, *, identifier=None, name='Current Authoritative Name', recipe=None):
        identifier = self.identifier if identifier is None else identifier
        path = self._write(f'domains/{self.domain}/00_pieces/{identifier}/piece.json', {
            'id': identifier, 'domain': self.domain,
            'recipe': recipe or self.recipe, 'name': name,
            'puzzle_id': 'f7a0', 'tile_ids': ['7f500000'],
        })
        self._write(f'domains/{self.domain}/domain.jsonc', {
            'pieces': [str(path.relative_to(self.root / f'domains/{self.domain}'))]})
        return path

    def test_unregistered_recipe_can_supply_a_new_scaffold_identifier_and_name(self):
        self.assertEqual(piece_id_for_recipe(self.recipe, self.root), 'hsr-test-recipe')
        self.assertEqual(piece_name_for_recipe(self.recipe, 'New Piece', self.root), 'New Piece')
        self.assertEqual(piece_directory(self.recipe, self.root),
                         self.root / 'domains/high-speed-rail/00_pieces/hsr-test-recipe')

    def test_registered_owner_drives_id_name_and_folder_without_modifying_sources(self):
        path = self._register()
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(piece_id_for_recipe(self.recipe, self.root), self.identifier)
        self.assertEqual(piece_name_for_recipe(self.recipe, 'Unused Fallback', self.root),
                         'Current Authoritative Name')
        self.assertEqual(piece_directory(self.recipe, self.root), path.parent)
        self.assertEqual(before, {p.relative_to(self.root): p.read_bytes()
                                  for p in self.root.rglob('*') if p.is_file()})

    def test_current_registered_name_changes_immediately(self):
        path = self._register()
        self.assertEqual(piece_name_for_recipe(self.recipe, 'Fallback', self.root),
                         'Current Authoritative Name')
        data = jsonc.load(path)
        data['name'] = 'Later Reviewed Name'
        path.write_text(json.dumps(data), encoding='utf-8')
        self.assertEqual(piece_name_for_recipe(self.recipe, 'Fallback', self.root), 'Later Reviewed Name')
        self.assertEqual(jsonc.load(path)['recipe'], self.recipe)
        self.assertEqual(jsonc.load(path)['puzzle_id'], 'f7a0')
        self.assertEqual(jsonc.load(path)['tile_ids'], ['7f500000'])

    def test_recipe_and_folder_identifier_are_independent(self):
        path = self._register(identifier='independently-allocated')
        self.assertEqual(piece_id_for_recipe(self.recipe, self.root), 'independently-allocated')
        self.assertEqual(piece_directory(self.recipe, self.root), path.parent)

    def test_unregistered_files_do_not_acquire_recipe_ownership(self):
        self._register()
        self._write(f'domains/{self.domain}/domain.jsonc', {'pieces': []})
        self.assertEqual(piece_id_for_recipe(self.recipe, self.root), 'hsr-test-recipe')
        self.assertEqual(piece_name_for_recipe(self.recipe, 'New Piece', self.root), 'New Piece')

    def test_declared_domain_and_default_root_are_respected(self):
        self.domain = 'highway'
        self._write('project.jsonc', {'domains': {
            self.domain: {'path': f'domains/{self.domain}',
                          'registry': f'domains/{self.domain}/domain.jsonc'}}})
        path = self._register()
        with patch('scp.subject_sources.project_root', return_value=self.root):
            self.assertEqual(piece_directory(self.recipe), path.parent)
            self.assertEqual(piece_id_for_recipe(self.recipe), self.identifier)

    def test_unsafe_recipe_cannot_become_a_path(self):
        for recipe in ('../outside', '/absolute', 'Has Spaces', 'double-hyphen'):
            with self.subTest(recipe=recipe), self.assertRaisesRegex(ValueError, 'Recipe'):
                piece_directory(recipe, self.root)

    def test_rejects_ambiguous_registered_recipe_owners(self):
        first = self._register()
        other = self._write(f'domains/{self.domain}/00_pieces/another-owner/piece.json', {
            'id': 'another-owner', 'domain': self.domain,
            'recipe': self.recipe, 'name': 'Another Name'})
        domain_root = self.root / f'domains/{self.domain}'
        self._write(f'domains/{self.domain}/domain.jsonc', {
            'pieces': [str(path.relative_to(domain_root)) for path in (first, other)]})
        with self.assertRaisesRegex(ValueError, 'Ambiguous registered recipe owner'):
            piece_id_for_recipe(self.recipe, self.root)

    def test_rejects_manifest_identity_or_registry_path_mismatch(self):
        path = self._register()
        data = jsonc.load(path)
        data['id'] = 'wrong-owner'
        path.write_text(json.dumps(data), encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'disagrees'):
            piece_name_for_recipe(self.recipe, 'Fallback', self.root)
        self._write(f'domains/{self.domain}/domain.jsonc', {'pieces': ['../../outside.json']})
        with self.assertRaisesRegex(ValueError, 'escapes'):
            piece_directory(self.recipe, self.root)

    def test_rejects_domain_paths_outside_project(self):
        for field in ('path', 'registry'):
            project = jsonc.load(self.root/'project.jsonc')
            project['domains'][self.domain][field] = '../outside'
            self._write('project.jsonc', project)
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, 'escapes'):
                piece_id_for_recipe(self.recipe, self.root)

    def test_rejects_empty_registered_name_and_unsafe_current_identifier(self):
        self._register(name='')
        with self.assertRaisesRegex(ValueError, 'nonempty current name'):
            piece_name_for_recipe(self.recipe, 'Fallback', self.root)
        path = self._register()
        data = jsonc.load(path)
        data['id'] = 'Bad Identifier'
        path.write_text(json.dumps(data), encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'Piece identifier'):
            piece_id_for_recipe(self.recipe, self.root)


if __name__ == '__main__':
    unittest.main()
