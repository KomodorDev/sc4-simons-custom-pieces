"""Broken documentation must fail read-only checks without native inputs."""
from pathlib import Path
import tempfile
import unittest

from scp.documentation_check import check_local_links


class LocalDocumentationLinksTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)

    def tearDown(self):
        self.temporary.cleanup()

    def check(self, text):
        source = self.root/'README.md'
        source.write_text(text)
        before = {p: p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        report = check_local_links([source], boundary=self.root)
        self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob('*') if p.is_file()})
        return report

    def test_exact_case_links_duplicate_heading_slugs_and_encoded_filenames(self):
        (self.root/'Testing notes.md').write_text(
            '# Testing notes\n\n## Current checks\n\n## Current checks\n\n<a id="case-exact-123"></a>\n')
        result = self.check('[case](Testing%20notes.md#case-exact-123)\n'
                            '[repeated](<Testing notes.md#current-checks-1>)\n')
        self.assertEqual(result, {'checked_links': 2, 'errors': []})

    def test_missing_file_and_exact_anchor_are_reported_at_their_source_lines(self):
        (self.root/'TESTING.md').write_text('# Testing\n\n<a id="case-current"></a>\n')
        result = self.check('# Piece\n\n[old](TESTING.md#case-deleted)\n[image](previews/missing.png)\n')
        self.assertEqual([error['line'] for error in result['errors']], [3, 4])
        self.assertIn('Missing Markdown anchor', result['errors'][0]['error'])
        self.assertIn('Missing local file', result['errors'][1]['error'])

    def test_html_reference_links_and_duplicate_explicit_case_anchors(self):
        (self.root/'target.md').write_text('# Target\n')
        result = self.check('<a id="case-same"></a>\n<a id="case-same"></a>\n'
                            '<a href="target.md#target">open</a>\n'
                            '[target][ref]\n\n[ref]: target.md#target\n')
        self.assertEqual(result['checked_links'], 2)
        self.assertEqual(len(result['errors']), 1)
        self.assertIn('Duplicate explicit anchor', result['errors'][0]['error'])

    def test_examples_and_remote_links_are_outside_local_link_scope(self):
        result = self.check('```md\n[example](missing-example.md)\n```\n'
                            '`[inline example](also-missing.md)`\n'
                            '[external](https://example.com/test#unfetched)\n')
        self.assertEqual(result, {'checked_links': 0, 'errors': []})

    def test_local_links_cannot_escape_the_checkout(self):
        result = self.check('[outside](../private-settings.json)\n')
        self.assertEqual(len(result['errors']), 1)
        self.assertIn('leaves the checkout', result['errors'][0]['error'])
