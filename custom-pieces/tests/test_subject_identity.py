"""Keep migrated folder aliases separate from recipes, names, and game IDs."""
from copy import deepcopy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp import jsonc
from scp.subject_identity import (canonical_piece_id, canonical_piece_name,
                                  canonical_subject_id, legacy_piece_id,
                                  piece_directory)


class SubjectIdentityTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix='scp-subject-identity-')
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.recipe = 'hsr_original_recipe'
        self.record = {
            'old_id': 'historical-piece', 'new_id': 'hsr-l2-two-track-straight',
            'old_name': 'Historical Name', 'new_name': 'Migration-Time Name',
            'recipe': self.recipe, 'domain': 'high-speed-rail',
            'rationale': 'Keep one recipe and its permanent numeric resources.',
        }
        self.assembly = {
            'old_id': 'historical-layout', 'new_id': 'hsr-trumpet-straight-stem',
            'domain': 'high-speed-rail',
        }
        self._write('project.jsonc', {'schema_version': 1, 'domains': {
            'high-speed-rail': {'path': 'domains/high-speed-rail',
                                'registry': 'domains/high-speed-rail/domain.jsonc'}}})
        self._write('domains/high-speed-rail/domain.jsonc', {'pieces': []})

    def _write(self, relative, data):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.suffix == '.jsonc':
            jsonc.dump(path, data, title='Identity test source', summary='Exercise declared subject aliases.')
        else:
            path.write_text(json.dumps(data) + '\n', encoding='utf-8')
        return path

    def _ledger(self, *, pieces=None, assemblies=None, version=1):
        return self._write('config/subject-id-migration.jsonc', {
            'schema_version': version,
            'pieces': [deepcopy(self.record)] if pieces is None else pieces,
            'assemblies': [deepcopy(self.assembly)] if assemblies is None else assemblies,
        })

    def _register(self, *, identifier=None, name='Current Authoritative Name', recipe=None):
        identifier = identifier or self.record['new_id']
        path = self._write(f'domains/high-speed-rail/00_pieces/{identifier}/piece.json', {
            'id': identifier, 'domain': 'high-speed-rail',
            'recipe': recipe or self.recipe, 'name': name,
            'puzzle_id': 'f7a0', 'tile_ids': ['7f500000'],
        })
        self._write('domains/high-speed-rail/domain.jsonc', {
            'pieces': [str(path.relative_to(self.root / 'domains/high-speed-rail'))]})
        return path

    def test_absent_migration_keeps_recipe_fallback_and_unknown_names(self):
        self.assertEqual(canonical_piece_id(self.recipe, self.root), 'hsr-original-recipe')
        self.assertEqual(canonical_piece_name(self.recipe, 'Fallback', self.root), 'Fallback')
        self.assertEqual(canonical_subject_id('unmapped-piece', root=self.root), 'unmapped-piece')
        self.assertEqual(legacy_piece_id('unmapped-style', self.root), 'unmapped-style')

    def test_only_declared_aliases_translate_and_namespaces_stay_separate(self):
        self._ledger()
        self.assertEqual(canonical_piece_id(self.recipe, self.root), self.record['new_id'])
        self.assertEqual(canonical_subject_id(self.record['old_id'], root=self.root), self.record['new_id'])
        self.assertEqual(canonical_subject_id(self.record['new_id'], root=self.root), self.record['new_id'])
        self.assertEqual(legacy_piece_id(self.record['new_id'], self.root), self.record['old_id'])
        self.assertEqual(legacy_piece_id(self.record['old_id'], self.root), self.record['old_id'])
        self.assertEqual(canonical_subject_id(self.assembly['old_id'], 'assembly', self.root),
                         self.assembly['new_id'])
        self.assertEqual(canonical_subject_id(self.assembly['old_id'], root=self.root),
                         self.assembly['old_id'])
        self.assertEqual(canonical_subject_id('historical-unlisted', root=self.root),
                         'historical-unlisted')

    def test_current_manifest_name_overrides_historical_ledger_and_changes_immediately(self):
        self._ledger()
        path = self._register()
        self.assertEqual(canonical_piece_name(self.recipe, 'Fallback', self.root),
                         'Current Authoritative Name')
        data = jsonc.load(path)
        data['name'] = 'Later Reviewed Name'
        path.write_text(json.dumps(data), encoding='utf-8')
        self.assertEqual(canonical_piece_name(self.recipe, 'Fallback', self.root), 'Later Reviewed Name')
        self.assertEqual(jsonc.load(path)['recipe'], self.recipe)
        self.assertEqual(jsonc.load(path)['puzzle_id'], 'f7a0')
        self.assertEqual(jsonc.load(path)['tile_ids'], ['7f500000'])

    def test_unregistered_migration_does_not_make_ledger_name_authoritative(self):
        self._ledger()
        self.assertEqual(canonical_piece_name(self.recipe, 'Unregistered Fallback', self.root),
                         'Unregistered Fallback')

    def test_registered_owner_can_have_an_independently_allocated_unmapped_id(self):
        path = self._register(identifier='independently-allocated')
        self.assertEqual(canonical_piece_name(self.recipe, 'Fallback', self.root),
                         'Current Authoritative Name')
        self.assertEqual(piece_directory(self.recipe, self.root), path.parent)

    def test_piece_directory_uses_declared_domain_and_no_files_are_written(self):
        record = dict(self.record, domain='highway')
        self._ledger(pieces=[record])
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(piece_directory(self.recipe, self.root),
                         self.root / 'domains/highway/00_pieces' / self.record['new_id'])
        self.assertEqual(before, {p.relative_to(self.root): p.read_bytes()
                                  for p in self.root.rglob('*') if p.is_file()})

    def test_piece_directory_fallback_and_default_root_are_explicit(self):
        with patch('scp.subject_identity.project_root', return_value=self.root):
            self.assertEqual(piece_directory(self.recipe),
                             self.root / 'domains/high-speed-rail/00_pieces/hsr-original-recipe')
            self.assertEqual(canonical_piece_id(self.recipe), 'hsr-original-recipe')

    def test_rejects_unknown_kind_and_unsafe_identifiers_without_guessing_aliases(self):
        for identifier in ('../outside', 'two--hyphens', 'trailing-', '/absolute', 'Has Spaces'):
            with self.subTest(identifier=identifier), self.assertRaises(ValueError):
                canonical_subject_id(identifier, root=self.root)
        with self.assertRaisesRegex(ValueError, 'kind'):
            canonical_subject_id('ordinary-piece', 'placement', self.root)
        with self.assertRaisesRegex(ValueError, 'Recipe'):
            piece_directory('../unsafe_recipe', self.root)

    def test_rejects_duplicate_alias_targets_recipe_owners_and_chains(self):
        variants = [
            dict(self.record, new_id='another-current-id', recipe='another_recipe'),
            dict(self.record, old_id='another-historical-id', recipe='another_recipe'),
            dict(self.record, old_id='another-historical-id', new_id='another-current-id'),
            dict(self.record, old_id=self.record['new_id'], new_id='another-current-id', recipe='another_recipe'),
        ]
        for other in variants:
            with self.subTest(other=other):
                self._ledger(pieces=[self.record, other])
                with self.assertRaisesRegex(ValueError, 'Ambiguous'):
                    canonical_piece_id(self.recipe, self.root)

    def test_rejects_unsafe_domain_and_unsupported_ledger_schema(self):
        self._ledger(pieces=[dict(self.record, domain='../outside')])
        with self.assertRaisesRegex(ValueError, 'domain'):
            piece_directory(self.recipe, self.root)
        self._ledger(version=2)
        with self.assertRaisesRegex(ValueError, 'schema'):
            canonical_piece_id(self.recipe, self.root)

    def test_rejects_ambiguous_registered_recipe_owners(self):
        first = self._register()
        other = self._write('domains/high-speed-rail/00_pieces/another-owner/piece.json', {
            'id': 'another-owner', 'domain': 'high-speed-rail',
            'recipe': self.recipe, 'name': 'Another Name'})
        domain_root = self.root / 'domains/high-speed-rail'
        self._write('domains/high-speed-rail/domain.jsonc', {
            'pieces': [str(path.relative_to(domain_root)) for path in (first, other)]})
        with self.assertRaisesRegex(ValueError, 'Ambiguous registered recipe owner'):
            canonical_piece_name(self.recipe, 'Fallback', self.root)

    def test_rejects_manifest_identity_or_registry_path_mismatch(self):
        path = self._register()
        data = jsonc.load(path)
        data['id'] = 'wrong-owner'
        path.write_text(json.dumps(data), encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'disagrees'):
            canonical_piece_name(self.recipe, 'Fallback', self.root)
        self._write('domains/high-speed-rail/domain.jsonc', {'pieces': ['../../outside.json']})
        with self.assertRaisesRegex(ValueError, 'escapes'):
            canonical_piece_name(self.recipe, 'Fallback', self.root)

    def test_changed_migration_source_invalidates_cached_aliases(self):
        self._ledger()
        self.assertEqual(canonical_piece_id(self.recipe, self.root), self.record['new_id'])
        other = dict(self.record, new_id='different-current-identity')
        self._ledger(pieces=[other])
        self.assertEqual(canonical_piece_id(self.recipe, self.root), other['new_id'])


if __name__ == '__main__':
    unittest.main()
