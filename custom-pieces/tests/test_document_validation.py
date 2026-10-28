"""Every writer rejects invalid current layouts before changing any selected file."""
from copy import deepcopy
import json
from pathlib import Path
import re
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

import test_content as manual_fixture
import test_piece_matrix as piece_fixture
from scp.content import (assembly_document_scaffold, compact_manual_record,
    piece_document_scaffold, record_observation_file, refresh_catalog_content,
    refresh_image_reviews_in_catalog, retire_connection_cases_in_catalog, write_subject_content)
from scp.document_validation import (ASSEMBLY_README_CHAPTERS,
    ASSEMBLY_TESTING_LAYOUT_MARKER, validate_subject_documents)
from scp.piece_matrix import LAYOUT_MARKER, SPLIT_LAYOUT_MARKER


def snapshot(directory):
    return {path.relative_to(directory): path.read_bytes()
            for path in directory.rglob('*') if path.is_file()}


def move_block(path, name, before):
    text = path.read_text()
    block = re.search(r'<!-- BEGIN '+name+r' -->.*?<!-- END '+name+r' -->', text, re.S).group()
    path.write_text(text.replace(block, '').replace(before, block+'\n\n'+before, 1))


class SubjectDocumentValidationTests(unittest.TestCase):
    def setUp(self):
        self.fixture = piece_fixture.PieceMatrixTests()
        self.fixture.setUp()

    def create(self, directory, *, kind='piece', identifier='fixture'):
        subject = {'id': identifier, 'kind': kind, 'name': 'Fixture '+identifier, 'footprint': [1, 2]}
        connections = {**deepcopy(self.fixture.connections), 'subject_id': identifier}
        write_subject_content(directory, subject, connections, self.fixture.hashes)
        return subject, connections

    def request(self, directory):
        record = json.loads((directory/'checks/manual-tests.json').read_text())
        case = next(case for case in record['cases'] if case['kind'] == 'in_game_render')
        request = directory/'observation.json'
        request.write_text(json.dumps({'case_id': case['id'], 'result': 'passed',
            'explicit_user_confirmation': True, 'reviewer': 'Synthetic fixture observer',
            'confirmed_at': '2026-10-28', 'evidence': ['Synthetic fixture; no real game observation.'],
            'environment': self.fixture.environment}))
        return request

    def test_current_scaffolds_are_pure_valid_pairs_with_no_claimed_evidence(self):
        for kind, scaffold in (('piece', piece_document_scaffold), ('assembly', assembly_document_scaffold)):
            subject = {'id': 'fixture', 'kind': kind, 'name': 'Fixture'}
            with self.subTest(kind=kind), TemporaryDirectory() as temporary:
                directory = Path(temporary)
                with patch.object(Path, 'read_text', side_effect=AssertionError('Pure scaffold')), \
                        patch.object(Path, 'write_text', side_effect=AssertionError('Pure scaffold')):
                    documents = scaffold(subject)
                self.assertEqual(set(documents), {'README.md', 'TESTING.md'})
                self.assertNotIn('passed', ''.join(documents.values()))
                for name, text in documents.items():
                    (directory/name).write_text(text)
                before = snapshot(directory)
                result = validate_subject_documents(directory, subject)
                self.assertEqual(result['layout'], 'piece-split-v2' if kind == 'piece' else 'assembly-numbered-v1')
                self.assertEqual(before, snapshot(directory))
                if kind == 'assembly':
                    self.assertEqual(re.findall(r'^## (.+)$', documents['README.md'], re.M), list(ASSEMBLY_README_CHAPTERS))

    def test_split_readme_requires_generated_blocks_in_their_chapters_and_exact_navigation(self):
        for corruption in ('views-in-placement', 'overview-in-views', 'connector-before-matrix', 'testing-target', 'missing-chapter-link'):
            with self.subTest(corruption=corruption), TemporaryDirectory() as temporary:
                directory = Path(temporary)
                subject, connections = self.create(directory)
                readme = directory/'README.md'
                if corruption == 'views-in-placement':
                    move_block(readme, 'PIECE VIEWS', '<!-- BEGIN PIECE OVERVIEW -->')
                elif corruption == 'overview-in-views':
                    move_block(readme, 'PIECE OVERVIEW', '<!-- BEGIN PIECE VIEWS -->')
                elif corruption == 'connector-before-matrix':
                    move_block(readme, 'CONNECTOR OVERVIEW', '<!-- BEGIN PIECE CONNECTION MATRIX -->')
                else:
                    old = '](TESTING.md)' if corruption == 'testing-target' else '[1. Views](#1-views)'
                    new = '](README.md#missing)' if corruption == 'testing-target' else '[Views](#missing)'
                    readme.write_text(readme.read_text().replace(old, new, 1))
                before = snapshot(directory)
                with self.assertRaises(ValueError):
                    write_subject_content(directory, subject, connections, self.fixture.hashes)
                self.assertEqual(before, snapshot(directory))

    def test_one_retained_pair_marker_cannot_downgrade_current_docs_to_legacy(self):
        for corruption in ('missing-readme-marker', 'contradictory-v1', 'piece-with-assembly-marker',
                           'assembly-with-piece-marker', 'assembly-with-piece-readme'):
            with self.subTest(corruption=corruption), TemporaryDirectory() as temporary:
                directory = Path(temporary)
                kind = 'assembly' if corruption.startswith('assembly-') else 'piece'
                subject, connections = self.create(directory, kind=kind)
                readme, testing = directory/'README.md', directory/'TESTING.md'
                if corruption in ('missing-readme-marker', 'contradictory-v1'):
                    readme.write_text(readme.read_text().replace(SPLIT_LAYOUT_MARKER,
                        '' if corruption == 'missing-readme-marker' else LAYOUT_MARKER))
                elif corruption == 'piece-with-assembly-marker':
                    testing.write_text(testing.read_text().replace('<!-- PIECE TESTING LAYOUT: 1 -->',
                                                                  ASSEMBLY_TESTING_LAYOUT_MARKER))
                elif corruption == 'assembly-with-piece-marker':
                    testing.write_text(testing.read_text().replace(ASSEMBLY_TESTING_LAYOUT_MARKER,
                                                                  '<!-- PIECE TESTING LAYOUT: 1 -->'))
                else:
                    readme.write_text(readme.read_text()+'\n'+SPLIT_LAYOUT_MARKER+'\n')
                before = snapshot(directory)
                for allow_missing in (False, True):
                    with self.assertRaisesRegex(ValueError, 'layout marker'):
                        validate_subject_documents(directory, subject, allow_missing=allow_missing)
                with self.assertRaisesRegex(ValueError, 'layout marker'):
                    write_subject_content(directory, subject, connections, self.fixture.hashes)
                self.assertEqual(before, snapshot(directory))

    def test_marked_testing_requires_its_own_overview_return_link(self):
        for kind in ('piece', 'assembly'):
            with self.subTest(kind=kind), TemporaryDirectory() as temporary:
                directory = Path(temporary)
                subject, connections = self.create(directory, kind=kind)
                testing = directory/'TESTING.md'
                link = '['+kind.capitalize()+' overview ↗ (README)](README.md)'
                testing.write_text(testing.read_text().replace(link, '[Wrong overview](elsewhere.md)'))
                before = snapshot(directory)
                with self.assertRaisesRegex(ValueError, 'overview'):
                    write_subject_content(directory, subject, connections, self.fixture.hashes)
                self.assertEqual(before, snapshot(directory))

    def test_marked_assembly_failures_reject_refresh_and_observation_before_any_write(self):
        for corruption in ('duplicate-marker', 'wrong-chapter', 'missing-navigation', 'checks-in-setup', 'nested-blocks'):
            for operation in ('metadata', 'views', 'observation'):
                with self.subTest(corruption=corruption, operation=operation), TemporaryDirectory() as temporary:
                    directory = Path(temporary)
                    subject, connections = self.create(directory, kind='assembly')
                    request = self.request(directory)
                    testing = directory/'TESTING.md'
                    if corruption == 'duplicate-marker':
                        testing.write_text(testing.read_text()+'\n'+ASSEMBLY_TESTING_LAYOUT_MARKER+'\n')
                    elif corruption == 'wrong-chapter':
                        testing.write_text(testing.read_text().replace('## 6. Design history', '## Invalid chapter'))
                    elif corruption == 'missing-navigation':
                        testing.write_text(testing.read_text().replace('[2. Test setup](#2-test-setup)', ''))
                    elif corruption == 'checks-in-setup':
                        move_block(testing, 'MANUAL CHECKS', '## 3. Software checks')
                    else:
                        move_block(testing, 'MANUAL CHECKS', '<!-- END CONNECTIONS -->')
                    before = snapshot(directory)
                    with self.assertRaises(ValueError):
                        if operation == 'observation':
                            record_observation_file(directory/'checks/manual-tests.json', request)
                        else:
                            write_subject_content(directory, subject, connections, self.fixture.hashes,
                                                  refresh_metadata=operation == 'metadata')
                    self.assertEqual(before, snapshot(directory))

    def test_missing_assembly_readme_preflights_existing_invalid_testing_without_recreation(self):
        with TemporaryDirectory() as temporary:
            directory = Path(temporary)
            self.create(directory, kind='assembly')
            request = self.request(directory)
            testing = directory/'TESTING.md'
            testing.write_text(testing.read_text().replace('## 6. Design history', '## Invalid chapter'))
            (directory/'README.md').unlink()
            before = snapshot(directory)
            with self.assertRaises(ValueError):
                record_observation_file(directory/'checks/manual-tests.json', request)
            self.assertEqual(before, snapshot(directory))
            self.assertFalse((directory/'README.md').exists())

    def test_whole_refresh_preflights_later_assembly_before_any_piece_or_class_write(self):
        for metadata in (False, True):
            with self.subTest(metadata=metadata), TemporaryDirectory() as temporary:
                root = Path(temporary)
                piece_directory = root/'domains/hsr/00_pieces/fixture'
                assembly_directory = root/'domains/hsr/01_assemblies/final'
                piece, connections = self.create(piece_directory)
                self.create(assembly_directory, kind='assembly', identifier='final')
                testing = assembly_directory/'TESTING.md'
                testing.write_text(testing.read_text().replace('## 6. Design history', '## Invalid chapter'))
                before = snapshot(root)
                catalog = {'pieces': [{**piece, 'domain': 'hsr'}], 'domains': {'hsr': {'path': 'domains/hsr'}},
                    '_assemblies': [{'id': 'final', 'path': 'domains/hsr/01_assemblies/final',
                                     'scene': {'placements': [{'piece_id': 'fixture'}]}}]}
                with patch('scp.catalog.load_catalog', return_value=catalog), \
                        patch('scp.inventory.write_inventories', side_effect=AssertionError('No inventory writes')), \
                        self.assertRaises(ValueError):
                    refresh_catalog_content(root, records={'fixture': connections} if metadata else None)
                self.assertEqual(before, snapshot(root))

    def test_batch_preflight_checks_all_required_v1_blocks_before_refreshing_current_piece(self):
        for metadata in (False, True):
            with self.subTest(metadata=metadata), TemporaryDirectory() as temporary:
                root = Path(temporary)
                first = root/'domains/hsr/00_pieces/a-current'
                last = root/'domains/hsr/00_pieces/z-legacy'
                first_piece, first_connections = self.create(first, identifier='a-current')
                last_piece, last_connections = self.create(last, identifier='z-legacy')
                readme = first/'README.md'
                readme.write_text(readme.read_text().replace('<!-- BEGIN PIECE OVERVIEW -->',
                    '<!-- BEGIN PIECE OVERVIEW -->\n\nStale generated text that a refresh would remove.'))
                legacy = piece_fixture.guide_skeleton()
                legacy = re.sub(r'<!-- BEGIN PIECE VIEWS -->.*?<!-- END PIECE VIEWS -->', '', legacy, flags=re.S)
                (last/'README.md').write_text(legacy)
                (last/'TESTING.md').unlink()
                before = snapshot(root)
                catalog = {'pieces': [{**piece, 'domain': 'hsr'} for piece in (first_piece, last_piece)],
                           'domains': {'hsr': {'path': 'domains/hsr'}}, '_assemblies': []}
                with patch('scp.catalog.load_catalog', return_value=catalog), \
                        patch('scp.inventory.write_inventories', side_effect=AssertionError('No inventory writes')), \
                        self.assertRaisesRegex(ValueError, 'ordered PIECE VIEWS block'):
                    refresh_catalog_content(root, records={'a-current': first_connections,
                        'z-legacy': last_connections} if metadata else None)
                self.assertEqual(before, snapshot(root))

    def test_image_binding_and_retirement_preflight_later_assembly_before_any_selected_write(self):
        for operation in (refresh_image_reviews_in_catalog, retire_connection_cases_in_catalog):
            with self.subTest(operation=operation.__name__), TemporaryDirectory() as temporary:
                root = Path(temporary)
                directory = root/'domains/hsr/00_pieces/fixture'
                piece, _ = self.create(directory)
                assembly_directory = root/'domains/hsr/01_assemblies/final'
                self.create(assembly_directory, kind='assembly', identifier='final')
                if operation == refresh_image_reviews_in_catalog:
                    (directory/'previews').mkdir()
                    (directory/'previews/preview-top.png').write_bytes(b'New synthetic image')
                else:
                    legacy = manual_fixture.ManualContentTests(); legacy.setUp()
                    (directory/'checks/manual-tests.json').write_text(json.dumps(compact_manual_record(legacy.legacy_record())))
                testing = assembly_directory/'TESTING.md'
                testing.write_text(testing.read_text().replace('## 6. Design history', '## Invalid chapter'))
                before = snapshot(root)
                catalog = {'pieces': [{**piece, 'domain': 'hsr'}], 'domains': {'hsr': {'path': 'domains/hsr'}},
                    '_assemblies': [{'id': 'final', 'path': 'domains/hsr/01_assemblies/final'}]}
                with patch('scp.catalog.load_catalog', return_value=catalog), self.assertRaises(ValueError):
                    operation(root, piece_ids=['fixture'], assembly_ids=['final'])
                self.assertEqual(before, snapshot(root))

    def test_legacy_piece_and_assembly_layouts_remain_unmigrated(self):
        for kind in ('piece', 'assembly'):
            with self.subTest(kind=kind), TemporaryDirectory() as temporary:
                directory = Path(temporary)
                readme = directory/'README.md'
                readme.write_text('# Authored legacy guide\n\nKeep its layout.\n')
                subject = {'id': 'fixture', 'kind': kind}
                before = snapshot(directory)
                self.assertEqual(validate_subject_documents(directory, subject)['layout'], 'legacy')
                self.assertEqual(before, snapshot(directory))
                if kind == 'assembly':
                    connections = {**self.fixture.connections, 'subject_id': 'fixture'}
                    write_subject_content(directory, subject, connections, self.fixture.hashes)
                    self.assertNotIn(ASSEMBLY_TESTING_LAYOUT_MARKER, (directory/'TESTING.md').read_text())
                    self.assertTrue(readme.read_text().startswith(before[Path('README.md')].decode()))

    def test_connector_writer_and_full_selection_reject_nested_blocks_before_output(self):
        from scp.connector_metadata import refresh_connections, write_exports
        from scp.connector_overview import _update_readme, render_overviews
        for operation in ('readme', 'exports', 'refresh-render', 'refresh-data', 'render'):
            with self.subTest(operation=operation), TemporaryDirectory() as temporary:
                root = Path(temporary)
                first = root/'domains/high-speed-rail/00_pieces/first'
                last = root/'domains/high-speed-rail/00_pieces/last'
                self.create(first, identifier='first')
                self.create(last, identifier='last')
                move_block(last/'README.md', 'PIECE CONNECTION MATRIX', '<!-- END CONNECTOR OVERVIEW -->')
                before = snapshot(root)
                exports = {'first': {}, 'last': {}}
                with self.assertRaisesRegex(ValueError, 'overlap or nest'):
                    if operation == 'readme':
                        _update_readme(last/'README.md', '## Connection overview\n\nSynthetic card.\n')
                    elif operation == 'exports':
                        write_exports(root, exports)
                    elif operation == 'render':
                        render_overviews(root, ['first', 'last'], resolved={'pieces': exports})
                    else:
                        with patch('scp.connector_metadata.build_exports', return_value=exports), \
                                patch('scp.connector_overview.render_overviews', side_effect=AssertionError('No rendering')):
                            refresh_connections(root, ['first', 'last'], root/'missing-build',
                                                render=operation == 'refresh-render')
                self.assertEqual(before, snapshot(root))


if __name__ == '__main__':
    unittest.main()
