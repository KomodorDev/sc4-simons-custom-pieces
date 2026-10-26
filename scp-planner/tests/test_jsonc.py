"""Check comment-aware parsing, exact source locations and strict JSON remainder."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from scp_planner import jsonc


class JsoncTests(unittest.TestCase):
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
