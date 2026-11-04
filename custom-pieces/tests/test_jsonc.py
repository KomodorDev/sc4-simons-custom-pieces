"""Check comment-aware parsing, exact source locations and strict JSON remainder."""
import json
import contextlib
import io
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))
from scp import jsonc


class JsoncTests(unittest.TestCase):
    def test_metadata_is_human_readable_without_adding_payload_fields(self):
        value = {'purpose': 'Existing explanation', 'id': 'permanent-id'}
        text = jsonc.dumps(value, title='Allocation "ledger"', summary='Reserve identifiers.\nKeep cities valid.')
        self.assertEqual(text.splitlines()[:2], [
            '// title: "Allocation \\"ledger\\""',
            '// summary: "Reserve identifiers.\\nKeep cities valid."'])
        self.assertEqual(jsonc.loads(text), value)

    def test_serialization_requires_nonempty_metadata_and_finite_values(self):
        for title, summary in [('', 'Summary'), ('Title', '  '), (None, 'Summary')]:
            with self.subTest(title=title, summary=summary), self.assertRaises(ValueError):
                jsonc.dumps({}, title=title, summary=summary)
        with self.assertRaises(ValueError):
            jsonc.dumps({'invalid': float('nan')}, title='Title', summary='Summary')

    def test_rewriting_keeps_authored_leading_comments_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'ledger.jsonc'
            prefix = ('// title: "My ledger"\n// summary: "My explanation"\n//\n'
                      '// Used when: Registering an approved piece.\n'
                      '// Read by: Catalogue validation.\n'
                      '// Updated by: The registration tool.\n'
                      '// Affects: Permanent resource reservations.\n'
                      '/* Retain this note. */\n\n')
            path.write_text(prefix+'{"old":1}\n', encoding='utf-8')
            jsonc.dump(path, {'new': 2}, title='Default title', summary='Default summary')
            self.assertEqual(path.read_text(), prefix+'{\n  "new": 2\n}\n')
            before = path.read_bytes(), path.stat().st_mtime_ns
            jsonc.dump(path, {'new': 2})
            self.assertEqual((path.read_bytes(), path.stat().st_mtime_ns), before)

    def test_rewriting_rejects_incomplete_or_duplicate_existing_metadata(self):
        for source in ['// title: "Only a title"\n{}',
                       '// title: "One"\n// title: "Two"\n// summary: "Summary"\n{}']:
            with self.subTest(source=source), self.assertRaises(ValueError):
                jsonc.document({}, source=source, title='Default', summary='Default')

    def test_metadata_examples_inside_block_comments_do_not_override_header(self):
        prefix = ('/* Example only:\n// title: "Example"\n// summary: "Example"\n*/\n'
                  '// title: "Actual title"\n// summary: "Actual explanation"\n')
        self.assertEqual(jsonc.document({'a': 1}, source=prefix+'{}'), prefix+'{\n  "a": 1\n}\n')

    def test_strict_export_is_byte_stable_and_cannot_replace_source(self):
        with tempfile.TemporaryDirectory() as directory:
            source, target = [Path(directory)/name for name in ('source.jsonc','view.json')]
            value = {'purpose': 'Preserved', 'values': [1, 2.0], 'url': 'https://example.test'}
            jsonc.dump(source, value, title='Source', summary='Read this source; export its data.')
            before = source.read_bytes()
            jsonc.export(source, target)
            self.assertEqual(target.read_bytes(), (json.dumps(value, indent=2)+'\n').encode())
            self.assertEqual(source.read_bytes(), before)
            exported = target.read_bytes(), target.stat().st_mtime_ns
            jsonc.export(source, target)
            self.assertEqual((target.read_bytes(),target.stat().st_mtime_ns), exported)
            with self.assertRaises(ValueError):
                jsonc.export(source, source)

    def test_module_cli_outputs_strict_json_or_writes_explicit_destination(self):
        with tempfile.TemporaryDirectory() as directory:
            source, target = [Path(directory)/name for name in ('source.jsonc','view.json')]
            jsonc.dump(source, {'a': 1}, title='Source', summary='CLI input.')
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                self.assertEqual(jsonc.main([str(source)]), 0)
            self.assertEqual(json.loads(output.getvalue()), {'a': 1})
            self.assertNotIn('// title', output.getvalue())
            self.assertEqual(jsonc.main([str(source), '--output', str(target)]), 0)
            self.assertEqual(target.read_text(), output.getvalue())

    def test_module_cli_printing_json_does_not_create_a_source_sibling(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory)/'source.jsonc'
            jsonc.dump(source, {'record': 'source'}, title='Shared source', summary='Explicit conversion fixture.')
            before = source.read_bytes()
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                self.assertEqual(jsonc.main([str(source)]), 0)
            self.assertEqual(json.loads(output.getvalue()), {'record': 'source'})
            self.assertEqual(source.read_bytes(), before)
            self.assertEqual(list(Path(directory).iterdir()), [source])

    def test_line_and_block_comments_are_supported(self):
        source = '// heading\n{"a": /* value */ 1, "b": [2, 3]} // final'
        self.assertEqual(jsonc.loads(source), {"a": 1, "b": [2, 3]})

    def test_quoted_comment_markers_and_escape_sequences_remain_literal(self):
        samples = ['https://example.test/a/*x*/#y', 'quoted " // still text',
                   'escaped backslash \\', 'backslash and quote \\"', '#not a comment']
        for sample in samples:
            with self.subTest(sample=sample):
                encoded = json.dumps(sample)
                source = '{"text":' + encoded + ', // actual comment\n"n": 2}'
                self.assertIn(encoded, jsonc.strip_comments(source))
                self.assertEqual(jsonc.loads(source), {"text": sample, "n": 2})

    def test_comments_preserve_every_character_index_and_newline(self):
        source = '// first\r\n{\n  "a": 1, /* αβ\nγ */\n  "b": 2\n}\n'
        expected = list(source)
        ranges = [(0, source.index('\r\n')), (source.index('/*'), source.index('*/')+2)]
        for first, last in ranges:
            for index in range(first, last):
                if source[index] not in '\r\n':
                    expected[index] = ' '
        stripped = jsonc.strip_comments(source)
        self.assertEqual(stripped, ''.join(expected))
        self.assertEqual(len(stripped), len(source))
        self.assertEqual(jsonc.loads(source), {"a": 1, "b": 2})

    def test_hash_comment_is_rejected_at_its_original_location(self):
        with self.assertRaises(json.JSONDecodeError) as caught:
            jsonc.loads('{\n  # unsupported\n}')
        self.assertEqual((caught.exception.lineno, caught.exception.colno), (2, 3))

    def test_hash_inside_supported_comments_is_ordinary_comment_text(self):
        self.assertEqual(jsonc.loads('{/* # explanation */"a":1}// # end'), {"a": 1})

    def test_unterminated_block_comment_is_rejected_at_its_start(self):
        with self.assertRaises(json.JSONDecodeError) as caught:
            jsonc.loads('{\n /* unfinished')
        self.assertEqual((caught.exception.lineno, caught.exception.colno), (2, 2))

    def test_trailing_comma_error_keeps_original_line_and_column(self):
        with self.assertRaises(json.JSONDecodeError) as caught:
            jsonc.loads('{\n // explanation\n "a":1,\n}')
        self.assertEqual((caught.exception.lineno, caught.exception.colno), (4, 1))

    def test_removed_comments_cannot_join_invalid_adjacent_tokens(self):
        for source in ('{"a":1/* comment */2}', '{"a":true/* comment */false}'):
            with self.subTest(source=source), self.assertRaises(ValueError):
                jsonc.loads(source)

    def test_other_non_json_syntax_remains_invalid(self):
        for source in ('{"a":1,}', '[1,]', "{'a':1}", '{"a":NaN}', '{"a":Infinity}', '{"a":-Infinity}'):
            with self.subTest(source=source), self.assertRaises(ValueError):
                jsonc.loads(source)

    def test_duplicate_keys_cannot_silently_override_authored_values(self):
        with self.assertRaises(ValueError):
            jsonc.loads('{"direction":"in", /* hidden override */ "direction":"out"}')

    def test_utf8_file_reader_is_read_only(self):
        source = '// readable comment\n{"name":"Straße"}\n'
        with tempfile.TemporaryDirectory(prefix="scp-jsonc-") as directory:
            path = Path(directory) / 'example.jsonc'
            path.write_text(source, encoding='utf-8')
            before = path.read_bytes()
            self.assertEqual(jsonc.load(path), {"name": "Straße"})
            self.assertEqual(path.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
