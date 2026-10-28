"""Shared document navigation remains stable without rewriting authored content."""
import unittest

from scp.markdown_navigation import (NAVIGATION_BEGIN, NAVIGATION_END,
                                     _active_lines, format_markdown_navigation,
                                     markdown_headings)


class MarkdownNavigationTests(unittest.TestCase):
    def test_numbering_navigation_and_legacy_fragments_are_idempotent(self):
        source = ('# Guide\n\nAn unchanged introduction.\n\n## 0. First\n\n'
                  '### 4. Child\n\n#### 4.8 Detail\n\n### Another child\n\n'
                  '## 7. Second\n\nKeep this exact paragraph.\n')
        result = format_markdown_navigation(source)
        self.assertEqual([(item.level, item.title) for item in markdown_headings(result)],
                         [(1, 'Guide'), (2, '1. First'), (3, '1.1 Child'),
                          (4, '1.1.1 Detail'), (3, '1.2 Another child'), (2, '2. Second')])
        self.assertIn('[1. First](#1-first) · [2. Second](#2-second)', result)
        self.assertNotIn('[1.1 Child]', result)
        for old in ('0-first', '4-child', '48-detail', 'another-child', '7-second'):
            self.assertIn('<a id="'+old+'"></a>', result)
        self.assertIn('An unchanged introduction.\n', result)
        self.assertTrue(result.endswith('Keep this exact paragraph.\n'))
        self.assertEqual(format_markdown_navigation(result), result)

    def test_front_matter_fences_comments_and_authored_blocks_are_preserved(self):
        metadata = '---\ntitle: Guide\nsummary: |\n  ## This is YAML\n---\n'
        code = ('```markdown\n## Example only\n'+NAVIGATION_BEGIN+'\n'+NAVIGATION_END+'\n```\n\n'
                '1. List\n\n    ~~~~markdown\n## Nested-list example\n    ~~~~\n\n'
                '<!--\n## Comment example\n-->\n')
        prose = '| Col | Value |\n| --- | --- |\n| 1 | A |\n\n- Preserve this list.\n'
        result = format_markdown_navigation(metadata+'\n# Guide\n\n## Real chapter\n\n'+code+prose)
        self.assertTrue(result.startswith(metadata))
        self.assertIn(code+prose, result)
        self.assertEqual([heading.title for heading in markdown_headings(result)],
                         ['Guide', '1. Real chapter'])
        self.assertEqual(format_markdown_navigation(result), result)

    def test_stale_navigation_is_replaced_and_does_not_number_the_title(self):
        source = ('# 2026 guide\n\n'+NAVIGATION_BEGIN+'\n[old](#gone)\n'+NAVIGATION_END
                  +'\n\nIntro.\n\n## 8. Current ###\n')
        result = format_markdown_navigation(source)
        self.assertEqual(result.count(NAVIGATION_BEGIN), 1)
        self.assertIn('# 2026 guide\n', result)
        self.assertIn('## 1. Current ###\n', result)
        self.assertNotIn('[old]', result)
        self.assertLess(result.index('[1. Current]'), result.index('Intro.'))
        self.assertEqual(format_markdown_navigation(result), result)

    def test_markers_and_fences_inside_multiline_comments_never_become_active(self):
        for marker in (NAVIGATION_BEGIN, NAVIGATION_END):
            with self.subTest(marker=marker):
                # The marker's closing --> also closes the surrounding comment;
                # that does not make a line that began inside the comment active.
                comment = '<!-- A commented marker example:\n'+marker+'\n'
                source = '# Guide\n\n'+comment+'\n## Real chapter\n'
                source_lines = source.splitlines(keepends=True)
                marker_line = source_lines.index(marker+'\n')
                self.assertFalse(_active_lines(source_lines)[marker_line])
                result = format_markdown_navigation(source)
                self.assertIn(comment, result)
                self.assertEqual([heading.title for heading in markdown_headings(result)],
                                 ['Guide', '1. Real chapter'])
                active_markers = [line.strip() for line, active in
                                  zip(result.splitlines(keepends=True),
                                      _active_lines(result.splitlines(keepends=True)))
                                  if active and line.strip() in (NAVIGATION_BEGIN, NAVIGATION_END)]
                self.assertEqual(active_markers, [NAVIGATION_BEGIN, NAVIGATION_END])
                self.assertEqual(format_markdown_navigation(result), result)
        comment = '<!-- A commented code example:\n```markdown\n## Hidden\n-->\n'
        result = format_markdown_navigation('# Guide\n\n'+comment+'\n## Visible\n')
        self.assertIn(comment, result)
        self.assertEqual([heading.title for heading in markdown_headings(result)],
                         ['Guide', '1. Visible'])
        self.assertEqual(format_markdown_navigation(result), result)
        fence = '```html <!-- literal info text\n## Hidden\n```\n'
        result = format_markdown_navigation('# Guide\n\n'+fence+'\n## Visible\n')
        self.assertIn(fence, result)
        self.assertEqual([heading.title for heading in markdown_headings(result)],
                         ['Guide', '1. Visible'])

    def test_required_layout_markers_stay_between_the_title_and_navigation(self):
        marker = '<!-- PIECE README LAYOUT: 2 -->'
        source = '# Guide\n\n'+marker+'\n\n## Views\n'
        result = format_markdown_navigation(source)
        self.assertLess(result.index(marker), result.index(NAVIGATION_BEGIN))
        self.assertLess(result.index(NAVIGATION_END), result.index('## 1. Views'))
        self.assertEqual(format_markdown_navigation(result), result)

    def test_existing_explicit_anchors_never_receive_duplicate_aliases(self):
        source = ('# Guide\n\n<a id="first"></a>\n\n## First\n\n'
                  '<a name="third"></a>\n\n## Third\n')
        result = format_markdown_navigation(source)
        self.assertEqual(result.count('id="first"'), 1)
        self.assertNotIn('id="1-first"', result)
        self.assertEqual(result.count('name="third"'), 1)
        self.assertNotIn('id="third"', result)
        self.assertEqual(format_markdown_navigation(result), result)

    def test_ambiguous_legacy_fragment_cannot_silently_retarget_to_another_heading(self):
        source = '# Guide\n\n## First\n\n## 1. First\n'
        with self.assertRaisesRegex(ValueError, 'Cannot preserve heading fragment #1-first') as context:
            format_markdown_navigation(source)
        message = str(context.exception)
        self.assertIn('from "1. First" (line 5)', message)
        self.assertIn('retarget it to "1. First" (line 3)', message)

    def test_duplicate_headings_keep_all_old_fragments(self):
        source = '# Guide\n\n## Repeated\n\n## Repeated\n\n## Repeated-1\n'
        self.assertEqual([heading.slug for heading in markdown_headings(source)],
                         ['guide', 'repeated', 'repeated-1', 'repeated-1-1'])
        result = format_markdown_navigation(source)
        for anchor in ('repeated', 'repeated-1', 'repeated-1-1'):
            self.assertIn('<a id="'+anchor+'"></a>', result)
        self.assertEqual(format_markdown_navigation(result), result)

    def test_title_only_and_child_first_documents_receive_an_overview(self):
        for source in ('# Guide\n\nKeep this introduction.', '# Guide\n\n### Child\n'):
            with self.subTest(source=source):
                result = format_markdown_navigation(source)
                self.assertIn('## 1. Overview\n', result)
                self.assertIn('[1. Overview](#1-overview)', result)
                if 'Child' in source:
                    self.assertIn('### 1.1 Child\n', result)
                self.assertTrue(result.endswith('\n'))
                self.assertEqual(format_markdown_navigation(result), result)

    def test_skipped_parent_headings_and_incomplete_markers_are_explicit_errors(self):
        for source, message in (('# Guide\n\n## Chapter\n\n#### Detail\n', 'skips its H3 parent'),
                                ('# Guide\n\n'+NAVIGATION_BEGIN+'\n', 'BEGIN has no END'),
                                ('# Guide\n\n'+NAVIGATION_END+'\n', 'END has no BEGIN')):
            with self.subTest(source=source):
                with self.assertRaisesRegex(ValueError, message):
                    format_markdown_navigation(source)

    def test_navigation_flattens_heading_links_and_preserves_heading_markup(self):
        result = format_markdown_navigation('# Guide\n\n## [Files](files.md) and `IDs`\n')
        self.assertIn('## 1. [Files](files.md) and `IDs`', result)
        self.assertIn('[1. Files and `IDs`](#1-files-and-ids)', result)

    def test_crlf_content_keeps_its_line_endings(self):
        result = format_markdown_navigation('# Guide\r\n\r\n## Chapter\r\n\r\nText.\r\n')
        self.assertNotIn('\n', result.replace('\r\n', ''))
        self.assertEqual(format_markdown_navigation(result), result)


if __name__ == '__main__':
    unittest.main()
