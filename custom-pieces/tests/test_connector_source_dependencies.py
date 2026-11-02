"""Reviewed numeric sources participate in exact connector-export freshness."""
import hashlib
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from scp.connector_metadata import _source_files


class ConnectorDependencyTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.identifier = 'example'
        self.reference = 'domains/test/01_assemblies/example/checks/accepted.jsonc'
        for name, content in {
            'domains/test/00_pieces/example/piece.jsonc': '{}',
            'domains/test/00_pieces/example/connections.json': '{}',
            'domains/test/00_pieces/example/connector-groups.jsonc': '{}',
            'domains/test/domain.jsonc': '{}',
            'dist/example/piece.dat': 'saved native fixture',
            self.reference: '// Reviewed numeric measurements\n{}',
        }.items():
            path = self.root/name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
        self.compiled = {'pieces': {'example': {'dat_path': 'dist/example/piece.dat'}}}

    def sources(self, adapter):
        with patch('scp.connector_metadata._registered_adapter', return_value=adapter):
            return _source_files(self.root, 'test', self.identifier, self.compiled)

    def test_adapter_measurement_source_is_bound_and_comment_change_invalidates_it(self):
        adapter = SimpleNamespace(connector_source_files=lambda piece: [self.reference])
        before = self.sources(adapter)
        path = self.root/self.reference
        self.assertEqual(before[self.reference], hashlib.sha256(path.read_bytes()).hexdigest())
        path.write_text(path.read_text()+'\n// Changed reviewed input.\n')
        self.assertNotEqual(before[self.reference], self.sources(adapter)[self.reference])

    def test_absent_hook_preserves_existing_source_set(self):
        self.assertNotIn(self.reference, self.sources(SimpleNamespace()))

    def test_escaping_missing_or_malformed_dependencies_are_rejected(self):
        for value in (['../outside.jsonc'], ['/outside.jsonc'], ['missing.jsonc'], 'not-a-list', [1]):
            with self.subTest(value=value), self.assertRaises((ValueError, FileNotFoundError)):
                self.sources(SimpleNamespace(connector_source_files=lambda piece: value))


if __name__ == '__main__':
    unittest.main()
