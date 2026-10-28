"""Validate maintained JSONC sources and their explicit strict-JSON boundaries."""
import json
from pathlib import Path
import tempfile
import unittest

from scp import jsonc
from scp.export import public_files


ROOT = Path(__file__).resolve().parents[1]
LIBRARY_SOURCES = {
    'project.jsonc',
    'config/allocations.jsonc',
    'config/installer.jsonc',
    'config/local.example.jsonc',
    'config/profiles/nam50-rhd.jsonc',
    'config/release.jsonc',
    'config/subject-id-migration.jsonc',
    'docs/templates/assembly-two-hsr-straights.jsonc',
    'schemas/connector-data.schema.jsonc',
    'schemas/connector-groups.schema.jsonc',
    'schemas/connector-profiles.schema.jsonc',
    'domains/high-speed-rail/domain.jsonc',
    'domains/high-speed-rail/collections.jsonc',
    'domains/high-speed-rail/connector-profiles.jsonc',
    'domains/high-speed-rail/menu-layout.jsonc',
    'domains/high-speed-rail/junction-design-review.jsonc',
    'domains/high-speed-rail/native-diagonal-port-cap-audit.jsonc',
    'domains/high-speed-rail/connection-classes.jsonc',
    'domains/high-speed-rail/inventory.jsonc',
    'domains/high-speed-rail/00_pieces/inventory.jsonc',
    'domains/high-speed-rail/01_assemblies/inventory.jsonc',
    'domains/highway/domain.jsonc',
    'domains/highway/collections.jsonc',
    'domains/highway/connection-classes.jsonc',
    'domains/highway/inventory.jsonc',
    'domains/highway/00_pieces/inventory.jsonc',
    'domains/highway/01_assemblies/inventory.jsonc',
}
LEGACY_VIEWS = {
    'domains/high-speed-rail/connection-classes.json',
    'domains/highway/connection-classes.json',
    'domains/high-speed-rail/junction-design-review.json',
    'domains/high-speed-rail/native-diagonal-port-cap-audit.json',
}
GITHUB_SOURCES = {'branch-protection.jsonc', 'branch-protection-main.jsonc'}


def shared_files():
    """Exclude individual subjects while retaining their parent inventories."""
    for relative, path in public_files(ROOT):
        parts = relative.parts
        if (len(parts) >= 5 and parts[0] == 'domains'
                and parts[2] in {'00_pieces', '01_assemblies'}):
            continue
        yield relative.as_posix(), path


class SharedJsoncSourceTests(unittest.TestCase):
    def assert_document(self, path):
        source = path.read_text(encoding='utf-8')
        lines = source.splitlines()
        self.assertGreaterEqual(len(lines), 3, str(path))
        for line, field in zip(lines[:2], ('title', 'summary')):
            prefix = f'// {field}: '
            self.assertTrue(line.startswith(prefix), f'{path}: missing {field} comment')
            value = json.loads(line[len(prefix):])
            self.assertIsInstance(value, str, f'{path}: {field} must be text')
            self.assertTrue(value.strip(), f'{path}: {field} must explain the document')
        stripped = jsonc.strip_comments(source)
        payload_start = len(stripped) - len(stripped.lstrip())
        header = source[:payload_start]
        for label in ('Used when', 'Read by', 'Updated by', 'Affects'):
            prefix = f'// {label}: '
            entries = [line[len(prefix):] for line in header.splitlines() if line.startswith(prefix)]
            self.assertEqual(len(entries), 1, f'{path}: needs one {label} explanation')
            self.assertTrue(entries[0].strip(), f'{path}: {label} explanation must be nonempty')
        payload = jsonc.loads(source)
        self.assertIsInstance(payload, dict, str(path))
        self.assertTrue(jsonc.document(payload, source=source).startswith(header),
                        f'{path}: regeneration must preserve the complete usage header')
        return payload

    def test_real_library_source_roster_has_readable_metadata_and_valid_payloads(self):
        sources = {relative: path for relative, path in shared_files() if path.suffix == '.jsonc'}
        self.assertEqual(set(sources), LIBRARY_SOURCES)
        self.assertEqual(len(sources), 27)
        for relative, path in sources.items():
            with self.subTest(source=relative):
                self.assert_document(path)

    def test_only_declared_legacy_views_remain_strict_json_and_match_their_sources(self):
        views = {relative: path for relative, path in shared_files() if path.suffix == '.json'}
        self.assertEqual(set(views), LEGACY_VIEWS)
        for relative, path in views.items():
            with self.subTest(view=relative):
                self.assertEqual(json.loads(path.read_text(encoding='utf-8')),
                                 jsonc.load(path.with_suffix('.jsonc')))

    def test_actual_github_templates_export_locally_without_changing_sources(self):
        directory = ROOT.parent / '.github'
        if not directory.is_dir():
            self.skipTest('Outer repository .github templates are absent from this library-only source copy')
        sources = {path.name: path for path in directory.glob('*.jsonc')}
        self.assertEqual(set(sources), GITHUB_SOURCES)
        self.assertFalse(list(directory.glob('branch-protection*.json')))
        with tempfile.TemporaryDirectory(prefix='scp-protection-export-') as temporary:
            for name, path in sources.items():
                with self.subTest(source=name):
                    before = path.read_bytes()
                    expected = self.assert_document(path)
                    target = Path(temporary) / path.with_suffix('.json').name
                    jsonc.export(path, target)
                    self.assertEqual(json.loads(target.read_text(encoding='utf-8')), expected)
                    self.assertEqual(path.read_bytes(), before)


if __name__ == '__main__':
    unittest.main()
