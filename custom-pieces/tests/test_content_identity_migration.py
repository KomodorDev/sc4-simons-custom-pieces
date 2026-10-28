"""Declared identity changes retain history without transferring observations."""
from copy import deepcopy
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(next(p for p in Path(__file__).resolve().parents
                          if (p / 'project.jsonc').is_file()) / 'framework'))
from scp import jsonc
from scp.content import (
    _expanded_record, case_state, compact_manual_record, declare_not_applicable,
    fingerprint, new_manual_record, record_software_result, record_user_result,
    record_observation_file,
    refresh_manual_record, refresh_renamed_manual_record, validate_manual_record,
    write_subject_content,
)


class ManualIdentityMigrationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / 'config').mkdir()
        jsonc.dump(self.root / 'project.jsonc', {}, title='Fixture project',
                   summary='Locate an isolated source root for identity migration tests.')
        jsonc.dump(self.root / 'config/subject-id-migration.jsonc', {
            'schema_version': 1,
            'pieces': [{'old_id': 'old-track', 'new_id': 'current-track',
                        'domain': 'high-speed-rail', 'recipe': 'old_track'}],
            'assemblies': [{'old_id': 'old-layout', 'new_id': 'current-layout',
                            'domain': 'high-speed-rail'}],
        }, title='Fixture subject identity migrations',
            summary='Declare exact allowed aliases without changing game resource identities.')

    def record(self, identifier, kind='piece'):
        connections = {'subject_id': identifier, 'subject_kind': kind,
                       'ports': [], 'journeys': [], 'forbidden_transfers': []}
        fingerprints = {f'model:{identifier}:fixture': fingerprint(b'unchanged model'),
                        f'path:{identifier}:fixture': fingerprint(b'unchanged traffic path')}
        return new_manual_record(identifier, kind, connections, fingerprints,
                                 {'canonical': fingerprint(b'original image')})

    def observed(self, record):
        preview = next(case for case in record['cases'] if case['kind'] == 'preview_review')
        output = record_user_result(record, preview['id'], 'passed',
            explicit_user_confirmation=True, reviewer='Fixture reviewer',
            confirmed_at='2026-10-28', evidence=['Original explicit preview observation.'])
        software = next(case for case in output['cases'] if case['kind'] == 'software_resources')
        output = record_software_result(output, software['id'], 'passed',
            verifier='Fixture verifier', checked_at='2026-10-28',
            evidence=['Original software report.'])
        render = next(case for case in output['cases'] if case['kind'] == 'in_game_render')
        output = record_user_result(output, render['id'], 'failed',
            explicit_user_confirmation=True, reviewer='Fixture reviewer',
            confirmed_at='2026-10-28', evidence=['Original explicit game observation.'],
            environment={'platform': 'fixture', 'game_version': 'fixture', 'nam_profile': 'fixture'})
        save = next(case for case in output['cases'] if case['kind'] == 'in_game_save_reload')
        return declare_not_applicable(output, save['id'], explicit_user_confirmation=True,
            reviewer='Fixture reviewer', confirmed_at='2026-10-28', reason='Original scoped declaration.')

    def test_all_old_cases_and_hashes_survive_only_as_history(self):
        old = self.observed(self.record('old-track'))
        # Previously removed, unobserved cases also remain part of the record.
        old['removed_cases'] = [old['cases'].pop()]
        old = compact_manual_record(old)
        fresh = self.record('current-track')
        before_old, before_fresh = deepcopy(old), deepcopy(fresh)
        migrated = refresh_renamed_manual_record(old, fresh, root=self.root)
        self.assertEqual(old, before_old)
        self.assertEqual(fresh, before_fresh)
        expanded = _expanded_record(old)
        self.assertEqual(migrated['removed_cases'], expanded['removed_cases'] + expanded['cases'])
        self.assertEqual(migrated['cases'], fresh['cases'])
        self.assertEqual(migrated['fingerprints'], fresh['fingerprints'])
        self.assertTrue(all(case['scope']['subject_id'] == 'old-track'
                            for case in migrated['removed_cases']))
        self.assertTrue(all(case['scope']['subject_id'] == 'current-track'
                            and case_state(case) == 'unverified'
                            for case in migrated['cases']))
        current_ids = {case['id'] for case in migrated['cases']}
        self.assertFalse(current_ids.intersection(case['id'] for case in migrated['removed_cases']))
        self.assertTrue(validate_manual_record(compact_manual_record(migrated)))
        later = refresh_manual_record(compact_manual_record(migrated), self.record('current-track'))
        self.assertEqual(later['removed_cases'], migrated['removed_cases'])

    def test_exact_assembly_migration_is_supported(self):
        old = self.record('old-layout', 'assembly')
        fresh = self.record('current-layout', 'assembly')
        migrated = refresh_renamed_manual_record(old, fresh, root=self.root)
        self.assertEqual(migrated['cases'], fresh['cases'])
        self.assertEqual(migrated['removed_cases'], old['cases'])

    def test_ordinary_refresh_still_rejects_other_subjects(self):
        with self.assertRaisesRegex(ValueError, 'different subjects'):
            refresh_manual_record(self.record('old-track'), self.record('current-track'))

    def test_unknown_old_or_new_identity_and_kind_changes_are_rejected(self):
        pairs = [
            (self.record('unknown-track'), self.record('current-track')),
            (self.record('old-track'), self.record('unknown-track')),
            (self.record('old-track'), self.record('current-track', 'assembly')),
            (self.record('old-track'), self.record('old-track')),
        ]
        for previous, generated in pairs:
            with self.subTest(previous=previous['subject'], generated=generated['subject']):
                snapshot = deepcopy(previous), deepcopy(generated)
                with self.assertRaises(ValueError):
                    refresh_renamed_manual_record(previous, generated, root=self.root)
                self.assertEqual((previous, generated), snapshot)

    def test_migration_requires_fresh_unverified_current_cases(self):
        old = self.record('old-track')
        for fresh in (self.observed(self.record('current-track')),
                      {**self.record('current-track'), 'removed_cases': deepcopy(old['cases'])}):
            with self.subTest(has_history=bool(fresh.get('removed_cases'))):
                with self.assertRaisesRegex(ValueError, 'newly generated unverified'):
                    refresh_renamed_manual_record(old, fresh, root=self.root)

    def test_future_metadata_refresh_uses_declared_bridge_and_preserves_evidence(self):
        directory = self.root / 'domains/high-speed-rail/00_pieces/current-track'
        (directory / 'checks').mkdir(parents=True)
        (directory / 'evidence').mkdir()
        old = compact_manual_record(self.observed(self.record('old-track')))
        path = directory / 'checks/manual-tests.json'
        path.write_text(json.dumps(old, indent=2) + '\n')
        evidence = directory / 'evidence/original-report.json'
        original_evidence = b'{"subject_id":"old-track","original_fingerprint":"preserved"}\n'
        evidence.write_bytes(original_evidence)
        connections = {'subject_id': 'current-track', 'subject_kind': 'piece',
                       'ports': [], 'journeys': [], 'forbidden_transfers': []}
        write_subject_content(directory, {'id': 'current-track', 'kind': 'piece',
            'name': 'Current Track', 'description': 'Fixture only.'}, connections,
            self.record('current-track')['fingerprints'],
            preview_hashes={'canonical': fingerprint(b'current image')})
        saved = _expanded_record(json.loads(path.read_text()))
        self.assertEqual(saved['subject'], {'id': 'current-track', 'kind': 'piece'})
        self.assertEqual(saved['removed_cases'], _expanded_record(old)['cases'])
        self.assertTrue(all(case_state(case) == 'unverified' for case in saved['cases']))
        self.assertEqual(evidence.read_bytes(), original_evidence)
        self.assertEqual(json.loads((directory / 'connections.json').read_text()), connections)

    def test_unknown_writer_identity_fails_before_creating_or_rewriting_views(self):
        directory = self.root / 'domains/high-speed-rail/00_pieces/current-track'
        (directory / 'checks').mkdir(parents=True)
        path = directory / 'checks/manual-tests.json'
        path.write_text(json.dumps(compact_manual_record(self.record('unknown-track')), indent=2) + '\n')
        original = path.read_bytes()
        with self.assertRaisesRegex(ValueError, 'not a declared subject migration'):
            write_subject_content(directory, {'id': 'current-track', 'kind': 'piece'},
                {'subject_id': 'current-track', 'ports': [], 'journeys': []}, {})
        self.assertEqual(path.read_bytes(), original)
        self.assertFalse((directory / 'README.md').exists())
        self.assertFalse((directory / 'TESTING.md').exists())
        self.assertFalse((directory / 'connections.json').exists())

    def test_observations_cannot_update_historical_records_or_roll_back_current_guides(self):
        for kind, old_id, current_id in (('piece', 'old-track', 'current-track'),
                                         ('assembly', 'old-layout', 'current-layout')):
            with self.subTest(kind=kind):
                directory = self.root / 'domains/high-speed-rail' / (
                    '00_pieces' if kind == 'piece' else '01_assemblies') / current_id
                (directory / 'checks').mkdir(parents=True)
                source = {'id': current_id, 'name': 'Current Track'} if kind == 'piece' else {'title': 'Current Layout'}
                (directory / (kind + '.json')).write_text(json.dumps(source) + '\n')
                record = self.record(old_id, kind)
                path = directory / 'checks/manual-tests.json'
                path.write_text(json.dumps(compact_manual_record(record), indent=2) + '\n')
                (directory / 'README.md').write_text('# Current Guide\n\nKeep the current identifier: `' + current_id + '`.\n')
                (directory / 'TESTING.md').write_text('# Current Testing\n\nHistorical observations require a scoped refresh.\n')
                case = next(case for case in record['cases'] if case['kind'] == 'preview_review')
                request = directory / 'checks/observation.json'
                request.write_text(json.dumps({'case_id': case['id'], 'result': 'passed',
                    'explicit_user_confirmation': True, 'reviewer': 'Fixture reviewer',
                    'confirmed_at': '2026-10-28', 'evidence': ['Explicit fixture observation.']}))
                before = {file.relative_to(directory): file.read_bytes()
                          for file in directory.rglob('*') if file.is_file()}
                with self.assertRaisesRegex(ValueError, 'historical subject.*' + current_id + '.*refresh measured metadata'):
                    record_observation_file(path, request)
                self.assertEqual({file.relative_to(directory): file.read_bytes()
                                  for file in directory.rglob('*') if file.is_file()}, before)


if __name__ == '__main__':
    unittest.main()
