"""Numbered assembly chapters remain authored while exact generated cases refresh."""
from copy import deepcopy
import json
from pathlib import Path
import re
import sys
from tempfile import TemporaryDirectory
import unittest

sys.path.insert(0, str(next(path for path in Path(__file__).resolve().parents
                          if (path/'project.json').is_file())/'framework'))
from scp.content import (ASSEMBLY_TESTING_CHAPTERS, ASSEMBLY_TESTING_LAYOUT_MARKER,
                         _ensure_testing_document, fingerprint,
                         new_manual_record, record_observation_file, record_user_result,
                         render_connections, render_manual_checklist, write_subject_content)


class AssemblyTestingLayoutTests(unittest.TestCase):
    def setUp(self):
        self.subject = {'id': 'fixture-assembly', 'kind': 'assembly', 'name': 'Fixture assembly'}
        self.connections = {'subject_id': self.subject['id'],
            'ports': [{'id': 'W.in', 'direction': 'in', 'service_network': 'hsr', 'role': 'primary'},
                      {'id': 'E.out', 'direction': 'out', 'service_network': 'hsr', 'role': 'primary'}],
            'journeys': [{'id': 'west-east', 'entry_port': 'W.in', 'exit_port': 'E.out',
                          'service_network': 'hsr', 'role': 'primary'}],
            'forbidden_transfers': []}
        self.hashes = {'path:fixture:route': fingerprint(b'actual saved route'),
                       'model:fixture:model': fingerprint(b'actual saved model'),
                       'construction:fixture': fingerprint(b'actual saved rules')}
        self.environment = {'platform': 'fixture platform', 'game_version': 'fixture game',
                            'nam_profile': 'fixture NAM'}

    def write(self, directory, **kwargs):
        return write_subject_content(directory, self.subject, self.connections, self.hashes, **kwargs)

    def authored_bytes(self, text):
        for name in ('CONNECTIONS', 'MANUAL CHECKS'):
            text = re.sub(r'<!-- BEGIN '+name+r' -->.*?<!-- END '+name+r' -->',
                          '<!-- '+name+' generated -->', text, flags=re.S)
        return text

    def assert_numbered_layout(self, text):
        self.assertEqual(text.count(ASSEMBLY_TESTING_LAYOUT_MARKER), 1)
        self.assertEqual(re.findall(r'^## (.+)$', text, flags=re.M), list(ASSEMBLY_TESTING_CHAPTERS))
        for chapter in ASSEMBLY_TESTING_CHAPTERS:
            slug = chapter.replace('.', '').lower().replace(' ', '-')
            self.assertIn('['+chapter+'](#'+slug+')', text)
        scope, setup = text.index('## 1. Test scope'), text.index('## 2. Test setup')
        results, history = text.index('## 5. Results and known issues'), text.index('## 6. Design history')
        self.assertLess(scope, text.index('<!-- BEGIN CONNECTIONS -->'))
        self.assertLess(text.index('<!-- END CONNECTIONS -->'), setup)
        self.assertLess(results, text.index('<!-- BEGIN MANUAL CHECKS -->'))
        self.assertLess(text.index('<!-- END MANUAL CHECKS -->'), history)
        self.assertEqual(text.count('### Connections and journeys\n'), 1)
        self.assertEqual(text.count('### Test checklist\n'), 1)
        self.assertIn('#### Directed journeys\n', text)
        self.assertIn('#### Forbidden transfers\n', text)
        self.assertIn('#### Record an observation\n', text)
        self.assertIn('#### Detailed current checks\n', text)
        # The unchanged H3 titles supply the existing automatic GitHub anchors.
        self.assertNotIn('<a id="test-checklist">', text)
        self.assertNotIn('<a id="connections-and-journeys">', text)

    def test_new_scaffold_has_only_pending_authored_guidance_and_six_numbered_chapters(self):
        with TemporaryDirectory() as temporary:
            directory = Path(temporary)
            path = _ensure_testing_document(directory, self.subject)
            pending = path.read_text()
            self.assertIn('[assembly overview](README.md)', pending)
            self.assertEqual(re.findall(r'^## (.+)$', pending, flags=re.M), list(ASSEMBLY_TESTING_CHAPTERS))
            self.assertNotIn('```', pending)
            self.assertNotIn('passed', pending)
            self.assertNotIn('evidence/', pending)
            self.assertFalse((directory/'README.md').exists())
            self.assertEqual(_ensure_testing_document(directory, self.subject).read_text(), pending)
            self.write(directory)
            self.assert_numbered_layout(path.read_text())
            self.assertIn('TESTING.md#test-checklist', (directory/'README.md').read_text())
            self.assertNotIn('<!-- BEGIN CONNECTIONS -->', (directory/'README.md').read_text())

    def test_refresh_and_confirmed_observation_preserve_authored_chapters_and_case_ids_in_both_modes(self):
        for matrix in (False, True):
            with self.subTest(matrix=matrix), TemporaryDirectory() as temporary:
                directory = Path(temporary)
                authored_readme = '# Fixture assembly\n\nKeep this exact player introduction.\n'
                if matrix:
                    authored_readme += ('\n<!-- BEGIN ASSEMBLY CONNECTION MATRIX -->\nPending.\n'
                                        '<!-- END ASSEMBLY CONNECTION MATRIX -->\n')
                (directory/'README.md').write_text(authored_readme)
                testing = _ensure_testing_document(directory, self.subject)
                text = testing.read_text().replace('## 2. Test setup',
                    '<a id="prepare-the-test-layout"></a>\n\n## 2. Test setup')
                text = text.replace('## 3. Software checks',
                    '### Exact authored setup detail\n\nKeep these bytes, commas, and links.\n\n## 3. Software checks')
                testing.write_text(text)
                authored = self.authored_bytes(text)
                self.write(directory)
                first = testing.read_text()
                self.assert_numbered_layout(first)
                self.assertEqual(self.authored_bytes(first), authored)
                record_path, connections_path = directory/'checks/manual-tests.json', directory/'connections.json'
                record = json.loads(record_path.read_text())
                ids = [case['id'] for case in record['cases']]
                self.assertEqual(set(re.findall(r'<a id="case-([^"]+)"></a>', first)), set(ids))
                self.assertEqual(len(re.findall(r'<a id="case-', first)), len(ids))
                self.write(directory)
                self.assertEqual(testing.read_text(), first)
                # Exact nondefault JSON formatting detects an accidental metadata write.
                record_path.write_text(json.dumps(record, separators=(',', ':')))
                connections_path.write_text(json.dumps(self.connections, separators=(',', ':')))
                original = {path: path.read_bytes() for path in (record_path, connections_path)}
                self.write(directory, refresh_metadata=False)
                self.assertEqual({path: path.read_bytes() for path in original}, original)
                self.assertEqual(testing.read_text(), first)
                observed = next(case for case in record['cases'] if case['kind'] == 'in_game_render'
                                and case['scope']['rotation_ccw_degrees'] == 0)
                request = {'case_id': observed['id'], 'result': 'failed', 'explicit_user_confirmation': True,
                    'reviewer': 'Fixture human', 'confirmed_at': '2026-10-27',
                    'environment': self.environment, 'evidence': ['Observed this exact appearance defect.']}
                observation = directory/'checks/observation.json'
                observation.write_text(json.dumps(request))
                record_observation_file(record_path, observation)
                updated = testing.read_text()
                self.assert_numbered_layout(updated)
                self.assertEqual(self.authored_bytes(updated), authored)
                self.assertIn('#### Failed and stale cases\n', updated)
                self.assertIn('Observed this exact appearance defect.', updated)
                self.assertEqual([case['id'] for case in json.loads(record_path.read_text())['cases']], ids)
                self.assertTrue((directory/'README.md').read_text().startswith(authored_readme.split('<!-- BEGIN')[0]))
                self.assertNotIn('<!-- BEGIN CONNECTIONS -->', (directory/'README.md').read_text())

    def test_observation_recreates_missing_assembly_testing_with_the_shared_layout(self):
        with TemporaryDirectory() as temporary:
            directory = Path(temporary)
            self.write(directory)
            (directory/'TESTING.md').unlink()
            record_path = directory/'checks/manual-tests.json'
            record = json.loads(record_path.read_text())
            case = next(case for case in record['cases'] if case['kind'] == 'in_game_render')
            observation = directory/'checks/observation.json'
            observation.write_text(json.dumps({'case_id': case['id'], 'result': 'passed',
                'explicit_user_confirmation': True, 'reviewer': 'Fixture human', 'confirmed_at': '2026-10-27',
                'environment': self.environment, 'evidence': ['Observed this exact appearance.']}))
            record_observation_file(record_path, observation)
            self.assert_numbered_layout((directory/'TESTING.md').read_text())

    def test_piece_and_unmarked_assembly_keep_existing_heading_style(self):
        for kind in ('piece', 'assembly'):
            with self.subTest(kind=kind), TemporaryDirectory() as temporary:
                directory = Path(temporary)
                subject = {**self.subject, 'kind': kind}
                if kind == 'assembly':
                    (directory/'TESTING.md').write_text('# Authored legacy tests\n\nKeep the legacy structure.\n')
                write_subject_content(directory, subject, self.connections, self.hashes)
                path = directory/('README.md' if kind == 'piece' else 'TESTING.md')
                text = path.read_text()
                self.assertNotIn(ASSEMBLY_TESTING_LAYOUT_MARKER, text)
                self.assertIn('## Test checklist\n', text)
                self.assertIn('### Detailed current checks\n', text)
                self.assertNotIn('#### Detailed current checks\n', text)
                self.assertIn('## Connections and journeys\n', (directory/'README.md').read_text())
                if kind == 'piece':
                    self.assertFalse((directory/'TESTING.md').exists())

    def test_custom_heading_depth_preserves_exact_cases_failures_and_legacy_history(self):
        record = new_manual_record(self.subject['id'], 'assembly', self.connections, self.hashes)
        case = next(case for case in record['cases'] if case['kind'] == 'in_game_render')
        record = record_user_result(record, case['id'], 'failed', explicit_user_confirmation=True,
            reviewer='Fixture human', confirmed_at='2026-10-27', environment=self.environment,
            evidence=['Exact failed observation retained.'])
        old = deepcopy(case)
        old['id'] = 'historical-fixture-case'
        old['kind'] = 'in_game_connection'
        record['removed_cases'] = [old]
        original = deepcopy(record)
        default = render_manual_checklist(record)
        nested = render_manual_checklist(record, heading_level=3)
        self.assertEqual(record, original)
        self.assertIn('#### Legacy connection history\n', nested)
        self.assertIn('#### Failed and stale cases\n', nested)
        self.assertEqual(re.findall(r'<a id="case-[^"]+"></a>', default),
                         re.findall(r'<a id="case-[^"]+"></a>', nested))
        self.assertIn('Exact failed observation retained.', nested)
        self.assertEqual(default, render_manual_checklist(record, heading_level=2))
        self.assertEqual(render_connections(self.connections), render_connections(self.connections, heading_level=2))
        for bad in (True, 1, 6, '3'):
            for render, value in ((render_manual_checklist, record), (render_connections, self.connections)):
                with self.subTest(bad=bad, renderer=render.__name__), self.assertRaises(ValueError):
                    render(value, heading_level=bad)


if __name__ == '__main__':
    unittest.main()
