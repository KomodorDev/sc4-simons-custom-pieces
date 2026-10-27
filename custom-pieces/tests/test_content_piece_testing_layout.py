"""Explicit piece document versions preserve observations and route case links."""
from copy import deepcopy
import json
from pathlib import Path
import re
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

import test_piece_matrix as fixture
import test_content as manual_fixture
from scp.content import (PIECE_README_CHAPTERS, PIECE_TESTING_CHAPTERS,
    PIECE_TESTING_LAYOUT_MARKER, _expanded_record, compact_manual_record,
    new_manual_record, piece_document_scaffold, record_observation_file,
    record_user_result, refresh_image_reviews_in_catalog,
    retire_connection_cases_in_catalog, write_subject_content)
from scp.piece_matrix import SPLIT_LAYOUT_MARKER, render_piece_connection_matrix


class PieceTestingLayoutTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixture.PieceMatrixTests()
        self.fixture.setUp()
        self.connections, self.hashes = self.fixture.connections, self.fixture.hashes
        self.subject = {'id': 'fixture', 'kind': 'piece', 'name': 'Fixture piece',
                        'description': 'Preserve the exact reusable definition.', 'footprint': [1, 2]}

    def write(self, directory, **kwargs):
        return write_subject_content(directory, self.subject, self.connections, self.hashes, **kwargs)

    def snapshot(self, directory):
        return {p.relative_to(directory): p.read_bytes() for p in directory.rglob('*') if p.is_file()}

    def observation_request(self, directory):
        record = json.loads((directory/'checks/manual-tests.json').read_text())
        case = next(c for c in record['cases'] if c['kind'] == 'in_game_render')
        request = directory/'observation.json'
        request.write_text(json.dumps({'case_id': case['id'], 'result': 'passed',
            'explicit_user_confirmation': True, 'reviewer': 'Fixture observer',
            'confirmed_at': '2026-10-27', 'evidence': ['Fixture only.'], 'environment': self.fixture.environment}))
        return request

    def overlap_blocks(self, path, outer, inner, *, crossing=False):
        text = path.read_text()
        inner_begin, inner_end = f'<!-- BEGIN {inner} -->', f'<!-- END {inner} -->'
        start, end = text.index(inner_begin), text.index(inner_end)+len(inner_end)
        block = text[start:end]
        text = text[:start]+text[end:]
        outer_end = f'<!-- END {outer} -->'
        replacement = (block[:-len(inner_end)]+outer_end+'\n'+inner_end
                       if crossing else block+'\n'+outer_end)
        path.write_text(text.replace(outer_end, replacement))

    def assert_routed(self, directory):
        readme, testing = [(directory/name).read_text() for name in ('README.md', 'TESTING.md')]
        self.assertEqual(re.findall(r'^## (.+)$', readme, re.M), list(PIECE_README_CHAPTERS))
        self.assertEqual(re.findall(r'^## (.+)$', testing, re.M), list(PIECE_TESTING_CHAPTERS))
        self.assertIn('[Testing](TESTING.md)', readme)
        self.assertIn(SPLIT_LAYOUT_MARKER, readme)
        self.assertEqual(testing.count(PIECE_TESTING_LAYOUT_MARKER), 1)
        for block, chapter, next_chapter in [('CONNECTIONS', '1. Test scope', '2. Test setup'),
                ('MANUAL SUMMARY', '5. Results and known issues', '6. Design history'),
                ('MANUAL CHECKS', '5. Results and known issues', '6. Design history')]:
            self.assertNotIn('<!-- BEGIN '+block+' -->', readme)
            self.assertLess(testing.index('## '+chapter), testing.index('<!-- BEGIN '+block+' -->'))
            self.assertLess(testing.index('<!-- END '+block+' -->'), testing.index('## '+next_chapter))
        anchors = set(re.findall(r'<a id="(case-[^"]+)"></a>', testing))
        self.assertTrue(anchors)
        record = _expanded_record(json.loads((directory/'checks/manual-tests.json').read_text()))
        self.assertLessEqual({'case-'+case['id'] for case in record['cases']}, anchors)
        self.assertEqual(len(anchors), len(re.findall(r'<a id="(case-[^"]+)"></a>', testing)))
        links = re.findall(r'\]\(([^)]*#case-[^)]*)\)', readme)
        self.assertTrue(links)
        for link in links:
            self.assertTrue(link.startswith('TESTING.md#case-'), link)
            self.assertIn(link.split('#', 1)[1], anchors)
        self.assertNotIn('<a id="case-', readme)
        self.assertIn('[the test checklist](TESTING.md#test-checklist)', readme)
        self.assertIn('[the exact test cases](#test-checklist)', testing)
        self.assertNotIn('TESTING.md#case-', testing)
        for anchor in re.findall(r'<a href="#(case-[^"]+)"', testing):
            self.assertIn(anchor, anchors)

    def test_new_documents_share_a_pure_scaffold_and_claim_no_evidence(self):
        with patch.object(Path, 'read_text', side_effect=AssertionError('No filesystem reads')), \
                patch.object(Path, 'write_text', side_effect=AssertionError('No filesystem writes')):
            documents = piece_document_scaffold(self.subject)
        self.assertEqual(set(documents), {'README.md', 'TESTING.md'})
        self.assertNotIn('passed', ''.join(documents.values()))
        self.assertNotIn('evidence/', ''.join(documents.values()))
        with TemporaryDirectory() as temporary:
            directory = Path(temporary)
            result = self.write(directory)
            self.assertIn('TESTING.md', result['files'])
            self.assert_routed(directory)
            first = {p: p.read_bytes() for p in directory.rglob('*') if p.is_file()}
            self.write(directory)
            self.assertEqual(first, {p: p.read_bytes() for p in first})

    def test_authored_split_documents_and_raw_records_survive_refresh_and_observations(self):
        with TemporaryDirectory() as temporary:
            directory = Path(temporary)
            self.write(directory)
            readme, testing = directory/'README.md', directory/'TESTING.md'
            readme.write_text(readme.read_text().replace('## 2. Piece and placement',
                'Keep this exact player paragraph.\n\n## 2. Piece and placement'))
            testing.write_text(testing.read_text().replace('## 4. Game checks',
                'Keep this exact command: `python -B check.py`.\n\n## 4. Game checks'))
            record_path, connection_path = directory/'checks/manual-tests.json', directory/'connections.json'
            initial = _expanded_record(json.loads(record_path.read_text()))
            record_path.write_text(json.dumps(compact_manual_record(initial), separators=(',', ':')))
            connection_path.write_text(json.dumps(self.connections, separators=(',', ':')))
            before = {p: p.read_bytes() for p in (record_path, connection_path)}
            with patch('scp.content.new_manual_record', side_effect=AssertionError('Do not regenerate cases')):
                self.write(directory, refresh_metadata=False)
            self.assertEqual(before, {p: p.read_bytes() for p in before})
            request = directory/'observation.json'
            with patch('scp.content.new_manual_record', side_effect=AssertionError('Do not regenerate cases')), \
                    patch('scp.connectivity.piece_connectivity', side_effect=AssertionError('Do not extract resources')):
                for case in initial['cases']:
                    if case['kind'] != 'in_game_route_query':
                        continue
                    request.write_text(json.dumps({'case_id': case['id'], 'result': 'passed',
                        'explicit_user_confirmation': True, 'reviewer': 'Fixture observer',
                        'confirmed_at': '2026-10-27', 'evidence': ['Literal test fixture.'],
                        'environment': self.fixture.environment}))
                    self.assertEqual(record_observation_file(record_path, request)['state'], 'passed')
            current = _expanded_record(json.loads(record_path.read_text()))
            without_observations = lambda r: [{k: v for k, v in case.items() if k != 'observations'} for case in r['cases']]
            self.assertEqual(without_observations(initial), without_observations(current))
            self.assertEqual(connection_path.read_bytes(), before[connection_path])
            self.assertIn('**Route Query:** [✅](TESTING.md#case-', readme.read_text())
            self.assertIn('**Visible train travel:** [?](TESTING.md#case-', readme.read_text())
            self.assertIn('Keep this exact player paragraph.', readme.read_text())
            self.assertIn('Keep this exact command: `python -B check.py`.', testing.read_text())
            self.assert_routed(directory)

    def test_explicit_migration_preserves_combined_observation_as_history_without_approving_split_cases(self):
        with TemporaryDirectory() as temporary:
            directory = Path(temporary)
            documents = piece_document_scaffold(self.subject)
            for name, text in documents.items():
                (directory/name).write_text(text)
            old = new_manual_record('fixture', 'piece', self.connections, self.hashes)
            combined = next(c for c in old['cases'] if c['kind'] == 'in_game_journey')
            old = record_user_result(old, combined['id'], 'passed', explicit_user_confirmation=True,
                reviewer='Fixture observer', confirmed_at='2026-10-27', evidence=['Historical combined fixture.'],
                environment=self.fixture.environment)
            (directory/'checks').mkdir()
            (directory/'checks/manual-tests.json').write_text(json.dumps(compact_manual_record(old)))
            self.write(directory)
            current = _expanded_record(json.loads((directory/'checks/manual-tests.json').read_text()))
            historical = next(c for c in current['removed_cases'] if c['id'] == combined['id'])
            observed = next(c for c in old['cases'] if c['id'] == combined['id'])
            self.assertEqual(historical['observations'], observed['observations'])
            self.assertTrue(all(not c['observations'] for c in current['cases']
                                if c['kind'] in ('in_game_route_query', 'in_game_visible_travel')))
            self.assert_routed(directory)

    def test_invalid_testing_layout_rejects_an_observation_before_any_write(self):
        with TemporaryDirectory() as temporary:
            directory = Path(temporary)
            self.write(directory)
            testing = directory/'TESTING.md'
            testing.write_text(testing.read_text().replace('## 6. Design history', '## Incorrect chapter'))
            record_path = directory/'checks/manual-tests.json'
            case = next(c for c in json.loads(record_path.read_text())['cases'] if c['kind'] == 'in_game_render')
            request = directory/'observation.json'
            request.write_text(json.dumps({'case_id': case['id'], 'result': 'passed',
                'explicit_user_confirmation': True, 'reviewer': 'Fixture observer',
                'confirmed_at': '2026-10-27', 'evidence': ['Fixture only.'], 'environment': self.fixture.environment}))
            before = {p: p.read_bytes() for p in directory.rglob('*') if p.is_file()}
            with self.assertRaisesRegex(ValueError, 'six numbered chapters'):
                record_observation_file(record_path, request)
            self.assertEqual(before, {p: p.read_bytes() for p in before})

    def test_nested_and_crossed_generated_blocks_reject_refresh_and_observation_without_writes(self):
        for filename, outer, inner in (
                ('TESTING.md', 'MANUAL SUMMARY', 'MANUAL CHECKS'),
                ('README.md', 'PIECE CONNECTION MATRIX', 'CONNECTOR OVERVIEW')):
            for crossing in (False, True):
                for operation in ('metadata', 'views', 'observation'):
                    with self.subTest(document=filename, crossing=crossing, operation=operation), TemporaryDirectory() as temporary:
                        directory = Path(temporary)
                        self.write(directory)
                        request = self.observation_request(directory)
                        self.overlap_blocks(directory/filename, outer, inner, crossing=crossing)
                        before = self.snapshot(directory)
                        with self.assertRaisesRegex(ValueError, 'overlap or nest'):
                            if operation == 'observation':
                                record_observation_file(directory/'checks/manual-tests.json', request)
                            else:
                                self.write(directory, refresh_metadata=operation == 'metadata')
                        self.assertEqual(before, self.snapshot(directory))

    def test_missing_readme_preflights_existing_testing_before_creating_or_recording(self):
        for corruption in ('chapters', 'nested'):
            for operation in ('metadata', 'views', 'observation'):
                with self.subTest(corruption=corruption, operation=operation), TemporaryDirectory() as temporary:
                    directory = Path(temporary)
                    self.write(directory)
                    request = self.observation_request(directory)
                    testing = directory/'TESTING.md'
                    if corruption == 'chapters':
                        testing.write_text(testing.read_text().replace('## 6. Design history', '## Incorrect chapter'))
                    else:
                        self.overlap_blocks(testing, 'MANUAL SUMMARY', 'MANUAL CHECKS')
                    (directory/'README.md').unlink()
                    before = self.snapshot(directory)
                    with self.assertRaisesRegex(ValueError, 'six numbered chapters|overlap or nest'):
                        if operation == 'observation':
                            record_observation_file(directory/'checks/manual-tests.json', request)
                        else:
                            self.write(directory, refresh_metadata=operation == 'metadata')
                    self.assertEqual(before, self.snapshot(directory))
                    self.assertFalse((directory/'README.md').exists())

    def test_selected_image_refresh_and_retirement_preflight_all_documents_before_any_write(self):
        for operation in ('images', 'retirement'):
            with self.subTest(operation=operation), TemporaryDirectory() as temporary:
                root = Path(temporary)
                pieces = [{'id': key, 'domain': 'hsr', 'name': key} for key in ('fixture', 'other')]
                directories = []
                for piece in pieces:
                    directory = root/'domains/hsr/00_pieces'/piece['id']
                    connections = {**self.connections, 'subject_id': piece['id']}
                    write_subject_content(directory, {**piece, 'kind': 'piece'}, connections, self.hashes)
                    directories.append(directory)
                    if operation == 'images':
                        (directory/'previews').mkdir()
                        (directory/'previews/preview-top.png').write_bytes(b'New image fixture')
                    else:
                        legacy = manual_fixture.ManualContentTests()
                        legacy.setUp()
                        record = legacy.legacy_record()
                        record['subject']['id'] = piece['id']
                        (directory/'checks/manual-tests.json').write_text(json.dumps(compact_manual_record(record)))
                testing = directories[-1]/'TESTING.md'
                testing.write_text(testing.read_text().replace('## 6. Design history', '## Incorrect chapter'))
                before = self.snapshot(root)
                catalog = {'pieces': pieces, 'domains': {'hsr': {'path': 'domains/hsr'}}, '_assemblies': []}
                with patch('scp.catalog.load_catalog', return_value=catalog), \
                        self.assertRaisesRegex(ValueError, 'six numbered chapters'):
                    function = (refresh_image_reviews_in_catalog if operation == 'images'
                                else retire_connection_cases_in_catalog)
                    function(root, piece_ids=['fixture', 'other'])
                self.assertEqual(before, self.snapshot(root))

    def test_v1_guides_and_existing_unmarked_testing_files_are_never_migrated(self):
        with TemporaryDirectory() as temporary:
            directory = Path(temporary)
            (directory/'README.md').write_text(fixture.guide_skeleton())
            legacy_testing = '# Unrelated authored test notes\n\nKeep these exact bytes.\n'
            (directory/'TESTING.md').write_text(legacy_testing)
            result = self.write(directory)
            self.assertNotIn('TESTING.md', result['files'])
            self.assertEqual((directory/'TESTING.md').read_text(), legacy_testing)
            readme = (directory/'README.md').read_text()
            self.assertEqual(re.findall(r'^## (.+)$', readme, re.M), fixture.HEADINGS)
            self.assertNotIn('](TESTING.md#case-', readme)
            self.assertIn('](#case-', readme)

    def test_matrix_routes_appearance_software_journeys_and_forbidden_cases_together(self):
        local = render_piece_connection_matrix(self.connections, self.fixture.record)
        split = render_piece_connection_matrix(self.connections, self.fixture.record, testing_document='TESTING.md')
        self.assertEqual(local.replace('](#case-', '](TESTING.md#case-')
                              .replace('](#test-checklist)', '](TESTING.md#test-checklist)'), split)
        self.assertIn('Source: [connections.json](connections.json).', split)


if __name__ == '__main__':
    unittest.main()
