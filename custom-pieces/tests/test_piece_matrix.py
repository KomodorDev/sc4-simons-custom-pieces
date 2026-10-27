"""Piece guides must distinguish resource facts from exact human observations."""
from copy import deepcopy
import json
from pathlib import Path
import re
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

sys.path.insert(0, str(next(p for p in Path(__file__).resolve().parents
                          if (p/'project.json').is_file())/'framework'))

from scp.content import (
    _expanded_record, case_state, compact_manual_record, fingerprint, new_manual_record,
    record_observation_file, record_software_result, record_user_result,
    summarize_manual_record, write_subject_content,
)
from scp.piece_matrix import LAYOUT_MARKER, SPLIT_LAYOUT_MARKER, render_piece_connection_matrix


HEADINGS = ['1. Views', '2. Piece and placement', '3. Connection matrix', '4. Testing']


def guide_skeleton():
    def block(name):
        return f'<!-- BEGIN {name} -->\n\n<!-- END {name} -->\n'
    return ('---\ntitle: "Fixture guide"\nsummary: "Preserve authored guide text."\n'
            'audience: "Players"\ndocument_type: "guide"\n---\n\n'
            '# Fixture\n\n'+LAYOUT_MARKER+'\n\n'
            'Keep this exact authored paragraph, including its punctuation.\n\n'
            '## '+HEADINGS[0]+'\n\n'+block('PIECE VIEWS')+'\n'
            '## '+HEADINGS[1]+'\n\n'+block('PIECE OVERVIEW')+'\n'
            'Keep this exact placement explanation.\n\n'
            '## '+HEADINGS[2]+'\n\n'+block('PIECE CONNECTION MATRIX')+'\n'
            '<!-- BEGIN CONNECTOR OVERVIEW -->\n\n'
            '### Connection overview\n\nPreserve this existing card block.\n\n'
            '<!-- END CONNECTOR OVERVIEW -->\n\n'
            '## '+HEADINGS[3]+'\n\n'+block('MANUAL SUMMARY')+'\n'+
            block('CONNECTIONS')+'\n'+block('MANUAL CHECKS'))


class PieceMatrixTests(unittest.TestCase):
    def setUp(self):
        self.hashes = {'path:fixture:saved': fingerprint(b'saved routes'),
                       'model:fixture:saved': fingerprint(b'saved model'),
                       'construction:fixture': fingerprint(b'emitted rules')}
        self.connections = {
            'subject_id': 'fixture',
            'source': {'resource_fingerprints': self.hashes.copy()},
            'software_status': {'path_extraction': 'passed'},
            'supported_orientations': [
                {'rotation_ccw_degrees': angle, 'construction_transposed': False}
                for angle in (0, 90, 180, 270)],
            'ports': [
                {'id': 'S.in', 'direction': 'in', 'service_network': 'hsr', 'role': 'primary'},
                {'id': 'N.out', 'direction': 'out', 'service_network': 'hsr', 'role': 'primary'},
                {'id': 'S.out', 'direction': 'out', 'service_network': 'hsr', 'role': 'primary'},
                {'id': 'E.out', 'direction': 'out', 'service_network': 'hsr', 'role': 'primary'}],
            'journeys': [{'id': 'south-north', 'service_network': 'hsr', 'role': 'primary',
                          'entry_port': 'S.in', 'exit_port': 'N.out'}],
            'forbidden_transfers': [{'from_port': 'S.in', 'to_port': 'S.out',
                                     'from_service': 'hsr', 'to_service': 'hsr',
                                     'reason': 'No return route in the saved graph.'}]}
        self.record = new_manual_record('fixture', 'piece', self.connections, self.hashes,
                                        split_journey_observations=True)
        self.environment = {'platform': 'fixture-platform', 'game_version': 'fixture-version',
                            'nam_profile': 'fixture-profile'}

    def observe(self, record, kind, result='passed', angles=None):
        output = record
        for case in record['cases']:
            if case['kind'] != kind or (angles is not None and
                    case['scope'].get('rotation_ccw_degrees') not in angles):
                continue
            output = record_user_result(output, case['id'], result,
                explicit_user_confirmation=True, reviewer='Fixture observer',
                confirmed_at='2026-10-27T12:00:00+01:00',
                evidence=['Literal fixture observation; no real game result.'],
                environment=self.environment)
        return output

    def software_pass(self, record):
        case = next(case for case in record['cases'] if case['kind'] == 'software_connectivity')
        return record_software_result(record, case['id'], 'passed', verifier='Fixture verifier',
            checked_at='2026-10-27', evidence=['Literal saved-resource fixture.'])

    def cells(self, record=None, connections=None):
        text = render_piece_connection_matrix(connections or self.connections,
                                              record or self.record)
        row = next(line for line in text.splitlines()
                   if line.startswith('| **HSR · South entrance**'))
        return row.strip('| ').split(' | ')[1:]

    def test_saved_path_route_query_and_visible_travel_have_independent_evidence(self):
        record = self.software_pass(self.record)
        record = self.observe(record, 'in_game_route_query')
        cell = self.cells(record)[0]
        self.assertIn('**Saved PATH:** [✅]', cell)
        self.assertIn('**Route Query:** [✅]', cell)
        self.assertIn('**Visible train travel:** [?]', cell)
        record = self.observe(record, 'in_game_visible_travel', angles={0})
        self.assertIn('**Visible train travel:** [?]', self.cells(record)[0])
        record = self.observe(record, 'in_game_visible_travel')
        self.assertIn('**Visible train travel:** [✅]', self.cells(record)[0])

    def test_legacy_combined_journey_pass_does_not_certify_split_observations(self):
        legacy = new_manual_record('fixture', 'piece', self.connections, self.hashes)
        legacy = self.observe(legacy, 'in_game_journey')
        cell = self.cells(legacy)[0]
        self.assertIn('**Route Query:** ?', cell)
        self.assertIn('**Visible train travel:** ?', cell)
        self.assertNotIn('✅', cell)

    def test_stale_route_resources_invalidate_saved_and_manual_travel_status(self):
        record = self.observe(self.software_pass(self.record), 'in_game_route_query')
        changed = deepcopy(self.connections)
        changed['source']['resource_fingerprints']['path:fixture:saved'] = fingerprint(b'changed routes')
        cell = self.cells(record, changed)[0]
        self.assertIn('**Saved PATH:** [?]', cell)
        self.assertIn('**Route Query:** [?]', cell)
        self.assertNotIn('✅', cell)

    def test_appearance_requires_every_current_orientation_and_reports_failure(self):
        partial = self.observe(self.record, 'in_game_render', angles={0, 90, 180})
        self.assertIn('**Game appearance:** [?]', render_piece_connection_matrix(self.connections, partial))
        complete = self.observe(partial, 'in_game_render', angles={270})
        self.assertIn('**Game appearance:** [✅]', render_piece_connection_matrix(self.connections, complete))
        changed = deepcopy(self.connections)
        changed['source']['resource_fingerprints']['model:fixture:saved'] = fingerprint(b'changed model')
        self.assertIn('**Game appearance:** [?]', render_piece_connection_matrix(changed, complete))
        failed = self.observe(partial, 'in_game_render', 'failed', angles={270})
        self.assertIn('**Game appearance:** [❌]', render_piece_connection_matrix(self.connections, failed))

    def test_missing_or_duplicate_orientation_cases_cannot_certify_coverage(self):
        complete = self.observe(self.record, 'in_game_route_query')
        query = next(case for case in complete['cases'] if case['kind'] == 'in_game_route_query')
        for cases in ([case for case in complete['cases'] if case['id'] != query['id']],
                      complete['cases']+[deepcopy(query)]):
            with self.subTest(case_count=len(cases)):
                self.assertIn('**Route Query:** [?]', self.cells({**complete, 'cases': cases})[0])

    def test_forbidden_pairs_are_explicit_and_unknown_pairs_remain_unknown(self):
        record = self.software_pass(self.record)
        permitted, forbidden, unknown = self.cells(record)
        self.assertNotIn('**Forbidden**', permitted)
        self.assertIn('**Forbidden**', forbidden)
        self.assertIn('**Saved PATH:** [✅]', forbidden)
        self.assertIn('In-game check: [?]', forbidden)
        self.assertNotIn('**Forbidden**', unknown)
        self.assertIn('**Saved PATH:** ?', unknown)
        self.assertNotIn('✅', unknown)
        failed = self.observe(record, 'in_game_forbidden_transfer', 'failed', angles={90})
        self.assertIn('In-game check: [❌]', self.cells(failed)[1])

    def test_service_role_and_variant_mismatches_do_not_borrow_journey_passes(self):
        record = self.observe(self.software_pass(self.record), 'in_game_route_query')
        for key, value in (('service_network', 'road'), ('role', 'auxiliary'), ('variant', 'different')):
            with self.subTest(key=key):
                changed = deepcopy(self.connections)
                changed['journeys'][0][key] = value
                self.assertNotIn('✅', self.cells(record, changed)[0])
        changed = deepcopy(self.connections)
        changed['ports'][1]['service_network'] = 'road'
        self.assertNotIn('✅', self.cells(record, changed)[0])

    def test_software_result_without_graph_dependency_cannot_certify_movements(self):
        record = deepcopy(self.record)
        case = next(case for case in record['cases'] if case['kind'] == 'software_connectivity')
        del case['dependencies']['graph:fixture']
        record = self.software_pass(record)
        self.assertIn('**Saved PATH:** [?]', self.cells(record)[0])

    def test_contradictory_permitted_and_forbidden_movement_is_rejected(self):
        changed = deepcopy(self.connections)
        changed['forbidden_transfers'][0]['to_port'] = 'N.out'
        with self.assertRaisesRegex(ValueError, 'both permitted and forbidden'):
            render_piece_connection_matrix(changed, self.record)

    def test_inventory_requires_both_split_checks_and_preserves_legacy_fallback(self):
        from scp.inventory import _coverage

        def coverage(record):
            summary = summarize_manual_record(record)
            return _coverage({'record_present': True, 'summary': summary}, 'in_game_journey')

        query_only = self.observe(self.record, 'in_game_route_query')
        self.assertEqual(coverage(query_only),
                         '[ ] 4/8 passed; 4 unverified; 0 failed; 0 stale')
        complete = self.observe(query_only, 'in_game_visible_travel')
        self.assertEqual(coverage(complete),
                         '[x] 8/8 passed; 0 unverified; 0 failed; 0 stale')
        failed = self.observe(complete, 'in_game_visible_travel', 'failed', angles={90})
        self.assertEqual(coverage(failed),
                         '[ ] 7/8 passed; 0 unverified; 1 failed; 0 stale')
        legacy = new_manual_record('fixture', 'piece', self.connections, self.hashes)
        legacy = self.observe(legacy, 'in_game_journey')
        self.assertNotIn('journey_coverage', summarize_manual_record(legacy))
        self.assertEqual(coverage(legacy),
                         '[x] 4/4 passed; 0 unverified; 0 failed; 0 stale')

    def create_guide(self, directory):
        directory.mkdir(parents=True)
        (directory/'README.md').write_text(guide_skeleton())
        subject = {'id': 'fixture', 'kind': 'piece', 'name': 'Fixture paired piece',
                   'description': 'A literal guide fixture.', 'footprint': [1, 2]}
        (directory/'piece.json').write_text(json.dumps(subject))
        (directory/'previews').mkdir(exist_ok=True)
        (directory/'previews/preview.png').write_bytes(b'fixture angled image')
        (directory/'previews/preview-top.png').write_bytes(b'fixture top image')
        write_subject_content(directory, subject, self.connections, self.hashes)
        return subject

    def test_missing_piece_guide_starts_numbered_with_split_unverified_observations(self):
        with TemporaryDirectory() as temporary:
            directory = Path(temporary)/'fixture'
            subject = {'id': 'fixture', 'kind': 'piece', 'name': 'Fixture paired piece',
                       'description': 'A literal guide fixture.', 'footprint': [1, 2]}
            write_subject_content(directory, subject, self.connections, self.hashes)
            text = (directory/'README.md').read_text()
            self.assertEqual(re.findall(r'^## (.+)$', text, re.MULTILINE), HEADINGS[:3])
            self.assertEqual(text.count(SPLIT_LAYOUT_MARKER), 1)
            self.assertIn('[Testing](TESTING.md)', text)
            for chapter in HEADINGS[:3]:
                anchor = chapter.replace('.', '').lower().replace(' ', '-')
                self.assertIn(f'[{chapter}](#{anchor})', text)
            for marker in ('PIECE VIEWS', 'PIECE OVERVIEW', 'PIECE CONNECTION MATRIX',
                           'CONNECTOR OVERVIEW'):
                self.assertEqual(text.count(f'<!-- BEGIN {marker} -->'), 1)
                self.assertEqual(text.count(f'<!-- END {marker} -->'), 1)
            self.assertLess(text.index('<!-- END PIECE CONNECTION MATRIX -->'),
                            text.index('<!-- BEGIN CONNECTOR OVERVIEW -->'))
            self.assertIn('Placement steps, required approaches, interface families, and known limitations have not yet been documented.', text)
            record_path = directory/'checks/manual-tests.json'
            record = _expanded_record(json.loads(record_path.read_text()))
            for kind in ('in_game_route_query', 'in_game_visible_travel'):
                cases = [case for case in record['cases'] if case['kind'] == kind]
                self.assertEqual(len(cases), 4)
                self.assertEqual({case['scope']['rotation_ccw_degrees'] for case in cases},
                                 {0, 90, 180, 270})
            self.assertFalse(any(case['kind'] == 'in_game_journey' for case in record['cases']))
            self.assertTrue(all(case_state(case, record['fingerprints']) == 'unverified'
                                for case in record['cases']))
            before = {path: path.read_bytes() for path in directory.rglob('*') if path.is_file()}
            write_subject_content(directory, subject, self.connections, self.hashes)
            self.assertEqual(before, {path: path.read_bytes() for path in directory.rglob('*') if path.is_file()})

    def test_new_guide_does_not_migrate_existing_unmarked_guide_or_rewrite_prose_only_records(self):
        with TemporaryDirectory() as temporary:
            directory = Path(temporary)/'fixture'
            directory.mkdir()
            authored = '# Legacy fixture\n\nKeep this exact legacy placement paragraph.\n'
            (directory/'README.md').write_text(authored)
            subject = {'id': 'fixture', 'kind': 'piece', 'name': 'Fixture paired piece'}
            write_subject_content(directory, subject, self.connections, self.hashes)
            record_path = directory/'checks/manual-tests.json'
            record = _expanded_record(json.loads(record_path.read_text()))
            self.assertEqual(sum(case['kind'] == 'in_game_journey' for case in record['cases']), 4)
            self.assertFalse(any(case['kind'] in ('in_game_route_query', 'in_game_visible_travel')
                                 for case in record['cases']))
            record = self.observe(record, 'in_game_journey')
            record_path.write_text(json.dumps(compact_manual_record(record), indent=2)+'\n')
            paths = (directory/'connections.json', record_path)
            before = {path: path.read_bytes() for path in paths}
            with patch('scp.content.new_manual_record', side_effect=AssertionError('No new resource facts')):
                write_subject_content(directory, subject, self.connections, {}, refresh_metadata=False)
            self.assertEqual(before, {path: path.read_bytes() for path in paths})
            text = (directory/'README.md').read_text()
            self.assertTrue(text.startswith(authored))
            self.assertNotIn(LAYOUT_MARKER, text)
            self.assertNotIn('PIECE CONNECTION MATRIX', text)

    def test_missing_authoritative_record_does_not_create_guide_or_other_files(self):
        with TemporaryDirectory() as temporary:
            directory = Path(temporary)/'fixture'
            with self.assertRaisesRegex(ValueError, 'No authoritative manual record'):
                write_subject_content(directory, {'id': 'fixture', 'kind': 'piece'},
                                      self.connections, {}, refresh_metadata=False)
            self.assertFalse(directory.exists())

    def test_observation_recording_recreates_missing_guide_without_replacing_observations(self):
        with TemporaryDirectory() as temporary:
            directory = Path(temporary)/'fixture'
            self.create_guide(directory)
            (directory/'README.md').unlink()
            record_path = directory/'checks/manual-tests.json'
            initial = _expanded_record(json.loads(record_path.read_text()))
            case = next(case for case in initial['cases'] if case['kind'] == 'in_game_route_query')
            observation = directory/'observation.json'
            observation.write_text(json.dumps({
                'case_id': case['id'], 'result': 'passed', 'explicit_user_confirmation': True,
                'reviewer': 'Fixture observer', 'confirmed_at': '2026-10-27',
                'evidence': ['Literal fixture observation.'], 'environment': self.environment}))
            connections_before = (directory/'connections.json').read_bytes()
            with patch('scp.content.new_manual_record', side_effect=AssertionError('Do not regenerate cases')):
                record_observation_file(record_path, observation)
            text = (directory/'README.md').read_text()
            self.assertEqual(re.findall(r'^## (.+)$', text, re.MULTILINE), HEADINGS[:3])
            self.assertIn('# Fixture paired piece\n', text)
            after = _expanded_record(json.loads(record_path.read_text()))
            self.assertEqual(connections_before, (directory/'connections.json').read_bytes())
            self.assertEqual(initial['fingerprints'], after['fingerprints'])
            self.assertEqual([{k: v for k, v in item.items() if k != 'observations'} for item in initial['cases']],
                             [{k: v for k, v in item.items() if k != 'observations'} for item in after['cases']])
            updated = next(item for item in after['cases'] if item['id'] == case['id'])
            self.assertEqual(case_state(updated, after['fingerprints']), 'passed')

    def test_missing_connections_prevent_observation_scaffold_before_any_write(self):
        with TemporaryDirectory() as temporary:
            directory = Path(temporary)/'fixture'
            self.create_guide(directory)
            (directory/'README.md').unlink()
            (directory/'connections.json').unlink()
            record_path = directory/'checks/manual-tests.json'
            record = _expanded_record(json.loads(record_path.read_text()))
            case = next(case for case in record['cases'] if case['kind'] == 'in_game_route_query')
            observation = directory/'observation.json'
            observation.write_text(json.dumps({
                'case_id': case['id'], 'result': 'passed', 'explicit_user_confirmation': True,
                'reviewer': 'Fixture observer', 'confirmed_at': '2026-10-27',
                'evidence': ['Literal fixture observation.'], 'environment': self.environment}))
            before = {path: path.read_bytes() for path in directory.rglob('*') if path.is_file()}
            with self.assertRaisesRegex(ValueError, 'No measured connections'):
                record_observation_file(record_path, observation)
            self.assertEqual(before, {path: path.read_bytes() for path in directory.rglob('*') if path.is_file()})

    def test_numbered_refresh_is_idempotent_and_preserves_authored_and_raw_records(self):
        with TemporaryDirectory() as temporary:
            directory = Path(temporary)/'fixture'
            subject = self.create_guide(directory)
            paths = [directory/'connections.json', directory/'checks/manual-tests.json']
            before = {path: path.read_bytes() for path in paths}
            with patch('scp.content.new_manual_record', side_effect=AssertionError('No new resource facts')):
                for _ in range(2):
                    write_subject_content(directory, subject, self.connections, {}, refresh_metadata=False)
                    self.assertEqual(before, {path: path.read_bytes() for path in paths})
                    text = (directory/'README.md').read_text()
                    self.assertEqual(re.findall(r'^## (.+)$', text, re.MULTILINE), HEADINGS)
                    self.assertIn('Keep this exact authored paragraph, including its punctuation.', text)
                    self.assertIn('Keep this exact placement explanation.', text)
                    self.assertIn('Preserve this existing card block.', text)
                    self.assertIn('### Connections and journeys', text)
                    self.assertIn('#### Directed journeys', text)
                    self.assertIn('### Test checklist', text)
                    self.assertEqual(text.count('(previews/preview.png)'), 1)
                    self.assertEqual(text.count('(previews/preview-top.png)'), 1)
                    if _ == 0:
                        first = {path: path.read_bytes() for path in directory.rglob('*') if path.is_file()}
                    else:
                        self.assertEqual(first, {path: path.read_bytes() for path in first})
            record = _expanded_record(json.loads(paths[1].read_text()))
            self.assertEqual(sum(case['kind'] == 'in_game_route_query' for case in record['cases']), 4)
            self.assertEqual(sum(case['kind'] == 'in_game_visible_travel' for case in record['cases']), 4)
            self.assertFalse(any(case['kind'] == 'in_game_journey' for case in record['cases']))

    def test_observation_file_refreshes_matrix_without_reconstructing_resource_facts(self):
        with TemporaryDirectory() as temporary:
            directory = Path(temporary)/'fixture'
            self.create_guide(directory)
            record_path = directory/'checks/manual-tests.json'
            connections_before = (directory/'connections.json').read_bytes()
            initial = _expanded_record(json.loads(record_path.read_text()))
            query_cases = [case for case in initial['cases'] if case['kind'] == 'in_game_route_query']
            observation = directory/'observation.json'
            with patch('scp.content.new_manual_record', side_effect=AssertionError('Do not regenerate cases')), \
                    patch('scp.connectivity.piece_connectivity', side_effect=AssertionError('Do not extract PATHs')):
                for case in query_cases:
                    observation.write_text(json.dumps({
                        'case_id': case['id'], 'result': 'passed', 'explicit_user_confirmation': True,
                        'reviewer': 'Fixture observer', 'confirmed_at': '2026-10-27',
                        'evidence': ['Literal fixture observation.'], 'environment': self.environment}))
                    result = record_observation_file(record_path, observation)
                    self.assertEqual(result['state'], 'passed')
            after = _expanded_record(json.loads(record_path.read_text()))
            self.assertEqual(connections_before, (directory/'connections.json').read_bytes())
            self.assertEqual(initial['fingerprints'], after['fingerprints'])
            self.assertEqual([{k: v for k, v in case.items() if k != 'observations'} for case in initial['cases']],
                             [{k: v for k, v in case.items() if k != 'observations'} for case in after['cases']])
            text = (directory/'README.md').read_text()
            self.assertIn('**Route Query:** [✅]', text)
            self.assertIn('**Visible train travel:** [?]', text)
            self.assertIn('Fixture paired piece', text)
            self.assertIn('Footprint: **1 × 2 tiles**', text)
            self.assertEqual(re.findall(r'^## (.+)$', text, re.MULTILINE), HEADINGS)

    def test_connector_overview_nests_under_numbered_connection_chapter(self):
        from scp.connector_overview import _update_readme
        content = ('## Connection overview\n\nCard conventions.\n\n'
                   '### Boundary A\n\n#### Service group 1 / 1\n\nMeasured members.\n')
        with TemporaryDirectory() as temporary:
            directory = Path(temporary)/'fixture'
            self.create_guide(directory)
            path = directory/'README.md'
            for _ in range(2):
                _update_readme(path, content)
                text = path.read_text()
                self.assertEqual(re.findall(r'^## (.+)$', text, re.MULTILINE), HEADINGS)
                self.assertIn('### Connection overview', text)
                self.assertIn('#### Boundary A', text)
                self.assertIn('##### Service group 1 / 1', text)
                self.assertEqual(text.count('<!-- BEGIN CONNECTOR OVERVIEW -->'), 1)
                if _ == 0:
                    first = path.read_bytes()
                else:
                    self.assertEqual(first, path.read_bytes())


if __name__ == '__main__':
    unittest.main()
