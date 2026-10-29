"""Broken documentation must fail read-only checks without native inputs."""
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scp.documentation_check import (check_documentation, check_local_links,
                                     check_shared_document_navigation)
from scp.markdown_navigation import NAVIGATION_BEGIN, NAVIGATION_END, format_markdown_navigation


class SharedDocumentNavigationTests(unittest.TestCase):
    valid = ('# Contributor guide\n\n'+NAVIGATION_BEGIN+'\n'
             '[1. Prepare](#1-prepare) · [2. Build](#2-build)\n'
             +NAVIGATION_END+'\n\n'
             'An authored introduction.\n\n'
             '<a id="old-prepare"></a>\n\n## 1. Prepare\n\n'
             '### 1.1 Select inputs\n\n#### 1.1.1 Inspect resources\n\n'
             '## 2. Build\n\n### 2.1 Check output\n')

    def test_numbered_chapters_subsections_and_legacy_aliases_are_valid(self):
        metadata = '---\ntitle: "Contributor guide"\nsummary: "Preserved metadata"\n---\n\n'
        self.assertEqual(check_shared_document_navigation(metadata+self.valid), [])

    def test_required_layout_markers_can_stay_between_the_title_and_navigation(self):
        text = self.valid.replace('# Contributor guide\n',
                                  '# Contributor guide\n\n<!-- FIXTURE README LAYOUT: 2 -->\n')
        self.assertEqual(check_shared_document_navigation(text), [])

    def test_year_leading_title_without_a_numbering_period_is_valid(self):
        text = format_markdown_navigation('# 2026 guide\n\n## Chapter\n')
        self.assertEqual(check_shared_document_navigation(text), [])

    def test_missing_numbering_and_missing_navigation_report_source_lines(self):
        result = check_shared_document_navigation('# Guide\n\n## Prepare\n')
        self.assertTrue(any(item['line'] == 3 and 'numbered 1.' in item['error'] for item in result))
        self.assertTrue(any('exactly one DOCUMENT NAVIGATION' in item['error'] for item in result))
        result = check_shared_document_navigation('# Guide\n')
        self.assertTrue(any('at least one numbered H2' in item['error'] for item in result))

    def test_title_must_be_unique_unnumbered_and_first(self):
        for text, expected in [
            (self.valid.replace('# Contributor guide', '# 1. Contributor guide'), 'must be unnumbered'),
            (self.valid+'\n# Another title\n', 'exactly one unnumbered H1'),
            (self.valid.replace('# Contributor guide\n', ''), 'exactly one unnumbered H1'),
            ('## 1. Earlier chapter\n\n'+self.valid, 'must precede all chapters'),
        ]:
            with self.subTest(expected=expected):
                self.assertTrue(any(expected in item['error'] for item in check_shared_document_navigation(text)))

    def test_numbering_starts_at_one_resets_children_and_rejects_skipped_parents(self):
        for old, new, expected in [
            ('## 1. Prepare', '## 0. Prepare', 'numbered 1.'),
            ('## 2. Build', '## 3. Build', 'numbered 2.'),
            ('### 2.1 Check output', '### 1.2 Check output', 'numbered 2.1'),
            ('### 1.1 Select inputs', '### 1.2 Select inputs', 'numbered 1.1'),
            ('### 1.1 Select inputs', '### 1.1. Select inputs', 'no trailing period'),
            ('### 1.1 Select inputs\n\n', '', 'skips its H3 parent'),
        ]:
            with self.subTest(heading=new):
                result = check_shared_document_navigation(self.valid.replace(old, new))
                self.assertTrue(any(expected in item['error'] for item in result), result)

    def test_navigation_rejects_stale_labels_fragments_order_and_subsection_links(self):
        original = '[1. Prepare](#1-prepare) · [2. Build](#2-build)'
        for row in [
            '[1. Old label](#1-prepare) · [2. Build](#2-build)',
            '[1. Prepare](#old-prepare) · [2. Build](#2-build)',
            '[2. Build](#2-build) · [1. Prepare](#1-prepare)',
            original+' · [1.1 Select inputs](#11-select-inputs)',
            '[1. Prepare](#1-prepare)',
        ]:
            with self.subTest(row=row):
                result = check_shared_document_navigation(self.valid.replace(original, row))
                self.assertEqual(len(result), 1)
                self.assertEqual(result[0]['line'], 4)
                self.assertIn('exact label and fragment, in chapter order', result[0]['error'])

    def test_navigation_requires_one_block_one_link_line_and_placement_after_title(self):
        start = self.valid.index(NAVIGATION_BEGIN)
        end = self.valid.index(NAVIGATION_END)+len(NAVIGATION_END)
        block = self.valid[start:end]
        for text, expected in [
            (self.valid+'\n'+block+'\n', 'exactly one DOCUMENT NAVIGATION'),
            (self.valid.replace(NAVIGATION_END, ''), 'exactly one DOCUMENT NAVIGATION'),
            (self.valid.replace(NAVIGATION_BEGIN, NAVIGATION_END).replace(
                NAVIGATION_END+'\n\nAn authored', NAVIGATION_BEGIN+'\n\nAn authored'), 'END must follow'),
            (self.valid.replace(' · [2.', '\n[2.'), 'exactly one physical line'),
            (self.valid.replace(block, '').replace('## 1. Prepare', block+'\n\n## 1. Prepare'),
             'immediately after the H1 title'),
        ]:
            with self.subTest(expected=expected):
                result = check_shared_document_navigation(text)
                self.assertTrue(any(expected in item['error'] for item in result), result)

    def test_fenced_and_commented_examples_do_not_count_as_headings_or_navigation(self):
        example = ('\n```markdown\n# 0. Example title\n## Unnumbered example\n'
                   +NAVIGATION_BEGIN+'\n[example](#missing)\n'+NAVIGATION_END+'\n```\n'
                   '\n<!--\n# Hidden title\n## Hidden chapter\n-->\n'
                   '\n1. A list example:\n\n   ~~~md\n   ## Unnumbered nested example\n   ~~~\n')
        self.assertEqual(check_shared_document_navigation(self.valid+example), [])
        for marker in (NAVIGATION_BEGIN, NAVIGATION_END):
            with self.subTest(commented_marker=marker):
                example = '\n<!-- Commented example\n## Hidden chapter\n'+marker+'\n'
                self.assertEqual(check_shared_document_navigation(self.valid+example), [])


class SharedDocumentationScopeTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.base = Path(self.temporary.name)

    def tearDown(self):
        self.temporary.cleanup()

    def fixture(self, name='framework', *, repository=False):
        root = self.base/name
        paths = ['README.md', 'STRUCTURE.md', 'AGENTS.md',
                 'domains/fixture/README.md', 'domains/fixture/AGENTS.md',
                 'domains/fixture/NETWORK_SPEC.md', 'domains/fixture/00_pieces/INVENTORY.md',
                 'domains/fixture/01_assemblies/INVENTORY.md']
        for name in paths:
            path = root/name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(SharedDocumentNavigationTests.valid)
        if repository:
            (self.base/'.git').write_text('gitdir: /example/managed-worktree\n')
            for name in ['README.md', 'AGENTS.md', 'docs/GITHUB.md']:
                path = self.base/name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(SharedDocumentNavigationTests.valid)
        return root

    def check(self, root, **selectors):
        before = {path: path.read_bytes() for path in self.base.rglob('*') if path.is_file()}
        catalog = {'pieces': [], '_assemblies': [], 'domains': {'fixture': {'path': 'domains/fixture'}}}
        with patch('scp.documentation_check.load_catalog', return_value=catalog):
            result = check_documentation(root, **selectors)
        self.assertEqual(before, {path: path.read_bytes() for path in self.base.rglob('*') if path.is_file()})
        return result

    def test_default_checks_inventory_numbering_and_links_without_modifying_files(self):
        root = self.fixture()
        inventory = root/'domains/fixture/00_pieces/INVENTORY.md'
        inventory.write_text(inventory.read_text().replace('## 2. Build', '## 3. Build')
                             +'\n[Missing inventory detail](missing.md)\n')
        result = self.check(root)
        self.assertFalse(result['all_passed'])
        self.assertTrue(any('Expected H2' in item['error'] for item in result['errors']))
        self.assertTrue(any('Missing local file' in item['error'] for item in result['errors']))
        self.assertTrue(all(item['file'].endswith('00_pieces/INVENTORY.md') for item in result['errors']))

    def test_standalone_library_ignores_unrelated_parent_guides(self):
        root = self.fixture()
        (self.base/'.git').mkdir()
        (self.base/'README.md').write_text('# Unrelated parent guide\n[missing](missing.md)\n')
        result = self.check(root)
        self.assertTrue(result['all_passed'], result['errors'])
        self.assertEqual(result['documents_checked'], 8)

    def test_repository_checkout_includes_root_guides_and_inventory_catalogues(self):
        root = self.fixture('custom-pieces', repository=True)
        (self.base/'docs/GITHUB.md').write_text('# Contributor guide\n\n## Unnumbered chapter\n'
                                               '\n[Missing contributor detail](missing.md)\n')
        result = self.check(root)
        self.assertFalse(result['all_passed'])
        self.assertEqual(result['documents_checked'], 11)
        self.assertTrue(all(item['file'] == 'docs/GITHUB.md' for item in result['errors']))
        self.assertTrue(any('Missing local file' in item['error'] for item in result['errors']))

    def test_unpacked_library_named_custom_pieces_does_not_require_repository_guides(self):
        result = self.check(self.fixture('custom-pieces'))
        self.assertTrue(result['all_passed'], result['errors'])
        self.assertEqual(result['documents_checked'], 8)

    def test_subject_selection_does_not_apply_shared_navigation_rules(self):
        root = self.fixture()
        (root/'README.md').write_text('# Shared guide awaiting maintenance\n')
        result = self.check(root, piece_ids=[], assembly_ids=[])
        self.assertTrue(result['all_passed'])
        self.assertEqual(result['documents_checked'], 0)


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
