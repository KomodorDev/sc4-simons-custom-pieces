"""Locate canonical JSONC projects and retain one unambiguous private settings file."""
from pathlib import Path
import tempfile
import unittest

from scp import jsonc
from scp.paths import local_settings, project_root


class SourcePathTests(unittest.TestCase):
    def test_project_search_finds_jsonc_above_a_nested_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            jsonc.dump(root/'project.jsonc', {}, title='Project', summary='Project-root fixture.')
            module = root/'nested/module.py'
            module.parent.mkdir()
            module.write_text('')
            self.assertEqual(project_root(module), root)
            self.assertEqual(project_root(module.parent), root)

    def test_new_private_settings_use_jsonc_without_creating_a_file(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertEqual(local_settings(root), root/'local/settings.jsonc')
            self.assertFalse((root/'local').exists())

    def test_existing_legacy_settings_remain_readable_without_migration(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            legacy = root/'local/settings.json'
            legacy.parent.mkdir()
            raw = '{"plugins":"fixture/Plugins"}\n'
            legacy.write_text(raw)
            self.assertEqual(local_settings(root), legacy)
            self.assertEqual(jsonc.load(local_settings(root)), {'plugins': 'fixture/Plugins'})
            self.assertEqual(legacy.read_text(), raw)
            self.assertFalse(legacy.with_suffix('.jsonc').exists())

    def test_ambiguous_private_settings_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            legacy = root/'local/settings.json'
            legacy.parent.mkdir()
            legacy.write_text('{}')
            legacy.with_suffix('.jsonc').write_text('{}')
            with self.assertRaisesRegex(ValueError, 'Both local/settings.jsonc and local/settings.json'):
                local_settings(root)


if __name__ == '__main__':
    unittest.main()
