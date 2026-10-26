"""Markdown metadata is deterministic, safely quoted, and retained by view refreshes."""
from pathlib import Path
import json
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'framework'))

from scp.content import (markdown_metadata, split_markdown_metadata, _replace_generated,
                         _write_subject_views, new_manual_record)


class MarkdownMetadataTests(unittest.TestCase):
    def test_four_quoted_strings_round_trip_without_physical_paragraph_breaks(self):
        values = ('Title: "quoted" — example', 'First line\nSecond line\u2028third',
                  'players', 'catalogue')
        result = markdown_metadata(*values)
        self.assertEqual(result, markdown_metadata(*values))
        self.assertTrue(result.endswith('---\n\n'))
        lines = result.splitlines()
        self.assertEqual(len(lines), 7)
        decoded = {}
        for line in lines[1:5]:
            key, value = line.split(': ', 1)
            self.assertTrue(value.startswith('"') and value.endswith('"'))
            decoded[key] = json.loads(value)
        self.assertEqual(tuple(decoded), ('title', 'summary', 'audience', 'document_type'))
        self.assertEqual(tuple(decoded.values()), values)

    def test_metadata_rejects_missing_or_nonstrings(self):
        for value in ('', '  ', 1, True, None, ['guide']):
            with self.subTest(value=value), self.assertRaises(ValueError):
                markdown_metadata('Title', 'Summary', 'players', value)

    def test_split_preserves_exact_existing_header_and_newlines(self):
        metadata = markdown_metadata('Title', 'Summary', 'players', 'guide')
        body = '# Title\n\nAn authored paragraph.\n'
        self.assertEqual(split_markdown_metadata(metadata + body), (metadata, body))
        crlf = metadata.replace('\n', '\r\n')
        self.assertEqual(split_markdown_metadata(crlf + body), (crlf, body))
        self.assertEqual(split_markdown_metadata(body), ('', body))
        with self.assertRaisesRegex(ValueError, 'closing'):
            split_markdown_metadata('---\ntitle: "Unclosed"\n')

    def test_generated_block_refresh_preserves_frontmatter_and_authored_prose(self):
        metadata = markdown_metadata('Title', 'Summary', 'players', 'guide')
        before = metadata + '# Title\n\nKeep the introduction.\n\n'
        after = '\n\nKeep the final paragraph.\n'
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / 'README.md'
            path.write_text(before + '<!-- BEGIN FIXTURE -->\nOld\n<!-- END FIXTURE -->' + after)
            _replace_generated(path, 'FIXTURE', 'New generated content.\n')
            first = path.read_text()
            self.assertTrue(first.startswith(before))
            self.assertTrue(first.endswith(after))
            _replace_generated(path, 'FIXTURE', 'New generated content.\n')
            self.assertEqual(path.read_text(), first)

    def test_assembly_readme_and_testing_headers_survive_view_refresh(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            connections = {'subject_id': 'fixture', 'ports': [], 'journeys': [], 'forbidden_transfers': []}
            subject = {'id': 'fixture', 'kind': 'assembly', 'name': 'Fixture assembly'}
            record = new_manual_record('fixture', 'assembly', connections, {})
            headers = {}
            for name in ('README.md', 'TESTING.md'):
                headers[name] = markdown_metadata(name, 'Authored summary.', 'contributors', 'guide')
                (directory / name).write_text(headers[name] + '# Fixture\n\nKeep authored instructions.\n')
            _write_subject_views(directory, subject, connections, record)
            first = {name: (directory / name).read_text() for name in headers}
            for name, text in first.items():
                self.assertTrue(text.startswith(headers[name]))
                self.assertIn('Keep authored instructions.', text)
            _write_subject_views(directory, subject, connections, record)
            self.assertEqual(first, {name: (directory / name).read_text() for name in headers})

    def test_new_assembly_readme_and_testing_start_with_metadata_without_body_purpose(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            connections = {'subject_id': 'fixture', 'ports': [], 'journeys': [], 'forbidden_transfers': []}
            subject = {'id': 'fixture', 'kind': 'assembly', 'name': 'Fixture assembly'}
            record = new_manual_record('fixture', 'assembly', connections, {})
            _write_subject_views(directory, subject, connections, record)
            for name, expected_type in (('README.md', 'guide'), ('TESTING.md', 'reference')):
                header, body = split_markdown_metadata((directory / name).read_text())
                fields = {key: json.loads(value) for key, value in
                          (line.split(': ', 1) for line in header.splitlines()[1:5])}
                self.assertEqual(set(fields), {'title', 'summary', 'audience', 'document_type'})
                self.assertEqual(fields['document_type'], expected_type)
                self.assertTrue(body.startswith('# '))
                self.assertNotIn('Purpose:', body)

    def test_new_piece_readme_keeps_existing_creation_format(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            connections = {'subject_id': 'fixture', 'ports': [], 'journeys': [], 'forbidden_transfers': []}
            subject = {'id': 'fixture', 'kind': 'piece', 'name': 'Fixture piece'}
            record = new_manual_record('fixture', 'piece', connections, {})
            _write_subject_views(directory, subject, connections, record)
            text = (directory / 'README.md').read_text()
            self.assertTrue(text.startswith('# Fixture piece\n\nPurpose: explain this reusable piece and its connections and test coverage.\n'))
            self.assertEqual(split_markdown_metadata(text), ('', text))

    def test_legacy_piece_conversion_retains_header_and_does_not_repeat_purpose(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            subject = {'id': 'fixture', 'kind': 'piece', 'name': 'Fixture', 'description': 'Description.'}
            connections = {'subject_id': 'fixture', 'ports': [], 'journeys': [], 'forbidden_transfers': []}
            record = new_manual_record('fixture', 'piece', connections, {})
            header = markdown_metadata('Fixture', 'Existing summary.', 'players', 'guide')
            legacy = '\n'.join(['# Fixture', '', 'Purpose: explain this reusable type, show its exact preview and expose its connection and manual-test coverage.',
                                '', 'Description.', '', 'Exact reusable identifier: `fixture`.', '',
                                '- [Connections and directed journeys](CONNECTIONS.md)',
                                '- [Authoritative manual checks](checks/MANUAL_TESTS.md)', ''])
            (directory / 'README.md').write_text(header + legacy + '\nKeep authored ending.\n')
            _write_subject_views(directory, subject, connections, record)
            text = (directory / 'README.md').read_text()
            self.assertTrue(text.startswith(header))
            self.assertIn('Keep authored ending.', text)
            self.assertIn('<!-- BEGIN PIECE OVERVIEW -->', text)
            self.assertNotIn('Purpose: explain this reusable', text)


if __name__ == '__main__':
    unittest.main()
