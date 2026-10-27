"""Final documentation can be packaged without changing compiled evidence."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile

from scp.build import package_build
from scp.export import compiled_manifest_sha256, documentation_members


class DocumentationHandoffTests(unittest.TestCase):
    def test_documentation_export_removes_raw_and_escaped_private_checkout_paths(self):
        with tempfile.TemporaryDirectory() as temporary:
            source = Path(temporary)/'private\\checkout'/'custom-pieces'
            source.mkdir(parents=True)
            missing = source/'evidence/missing.json'
            (source/'README.md').write_text(f'Inspect {missing} and {missing.resolve()} before publishing.\n')
            (source/'evidence.json').write_text(json.dumps({'source': str(missing),
                                                          'resolved': str(missing.resolve())}))

            members = documentation_members(source)

            for name, raw in members.items():
                with self.subTest(document=name):
                    for prefix in {str(source.parent), str(source.parent.resolve())}:
                        self.assertNotIn(prefix.encode(), raw)
                        self.assertNotIn(repr(prefix)[1:-1].encode(), raw)
                    self.assertIn(b'/path/to/sc4-simons-custom-pieces', raw)
                    self.assertIn(b'missing.json', raw)
            self.assertTrue(json.loads(members['docs/evidence.json'])['source'].startswith(
                '/path/to/sc4-simons-custom-pieces'))

    def test_manifest_fingerprint_ignores_only_docs_and_publication_state(self):
        manifest = {'schema_version': 1, 'files': [{'path': 'payload.dat', 'sha256': 'a'*64}],
                    'pieces': [{'id': 'piece', 'tile_ids': ['12340000']}],
                    'overlay': {'rul0': {'literal': 'rules'}}, 'dependency_audit': {'textures': ['texture']},
                    'profile': {'id': 'audited'}, 'documentation': [], 'release': {},
                    'installed': False, 'in_game_tested': False}
        digest = compiled_manifest_sha256(manifest)
        changed = deepcopy(manifest)
        changed.update(documentation=[{'path': 'docs/final.png'}], release={'public_release_ready': True},
                       installed=True, in_game_tested=True)
        self.assertEqual(compiled_manifest_sha256(changed), digest)
        for key in ('files', 'pieces', 'overlay', 'profile', 'dependency_audit', 'future_compiled_field'):
            changed = deepcopy(manifest)
            changed[key] = {'mutated': True}
            with self.subTest(key=key):
                self.assertNotEqual(compiled_manifest_sha256(changed), digest)

    def test_explicit_handoff_packages_current_docs_with_correct_hashes_and_unchanged_build(self):
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            source, output = base/'source', base/'build'
            source.mkdir()
            (output/'plugin').mkdir(parents=True)
            (output/'docs').mkdir()
            (source/'README.md').write_text('# Final documentation\n')
            (source/'previews').mkdir()
            (source/'previews/connection-overview.png').write_bytes(b'final cards')
            (source/'local').mkdir()
            (source/'local/private.json').write_text('{}')
            (output/'docs/README.md').write_text('# Old documentation\n')
            (output/'docs/removed.md').write_text('# Removed documentation\n')
            (output/'README.txt').write_bytes(b'Build instructions')
            (output/'plugin/payload.dat').write_bytes(b'unchanged verified DAT')
            manifest = {'files': [{'path': 'plugin/payload.dat'}], 'documentation': [
                {'path': name, 'bytes': len((output/name).read_bytes()),
                 'sha256': hashlib.sha256((output/name).read_bytes()).hexdigest()}
                for name in ('README.txt', 'docs/README.md', 'docs/removed.md')]}
            (output/'manifest.json').write_text(json.dumps(manifest))
            before = {path: path.read_bytes() for path in output.rglob('*') if path.is_file()}
            with patch('scp.build.verify_build', return_value={'static_checks_passed': True}) as verify:
                default = base/'default.zip'
                package_build(output, default)
                destination = base/'current.zip'
                result = package_build(output, destination, project_root=source, refresh_docs=True)
                self.assertEqual(verify.call_count, 2)
            self.assertTrue(result['documentation_refreshed'])
            self.assertEqual(before, {path: path.read_bytes() for path in before})
            with zipfile.ZipFile(default) as archive:
                self.assertEqual(archive.read('docs/README.md'), b'# Old documentation\n')
            with zipfile.ZipFile(destination) as archive:
                packaged = json.loads(archive.read('manifest.json'))
                self.assertEqual(compiled_manifest_sha256(packaged), compiled_manifest_sha256(manifest))
                self.assertEqual(archive.read('docs/README.md'), b'# Final documentation\n')
                self.assertEqual(archive.read('docs/previews/connection-overview.png'), b'final cards')
                self.assertNotIn('docs/removed.md', archive.namelist())
                self.assertNotIn('docs/local/private.json', archive.namelist())
                self.assertEqual(archive.read('plugin/payload.dat'), b'unchanged verified DAT')
                self.assertEqual(set(archive.namelist()), {'manifest.json', 'plugin/payload.dat'} |
                                 {item['path'] for item in packaged['documentation']})
                for item in packaged['documentation']:
                    raw = archive.read(item['path'])
                    self.assertEqual((len(raw), hashlib.sha256(raw).hexdigest()), (item['bytes'], item['sha256']))
            self.assertEqual(documentation_members(source), {'docs/README.md': b'# Final documentation\n',
                                                            'docs/previews/connection-overview.png': b'final cards'})

    def test_handoff_rejects_missing_source_or_failed_build_verification(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)/'build'
            output.mkdir()
            (output/'manifest.json').write_text('{"files": [], "documentation": []}')
            destination = Path(temporary)/'current.zip'
            with patch('scp.build.verify_build', return_value={}):
                with self.assertRaisesRegex(ValueError, 'current project root'):
                    package_build(output, destination, refresh_docs=True)
            self.assertFalse(destination.exists())
            with patch('scp.build.verify_build', side_effect=ValueError('Build is invalid')):
                with self.assertRaisesRegex(ValueError, 'Build is invalid'):
                    package_build(output, destination, project_root=Path(temporary), refresh_docs=True)
            self.assertFalse(destination.exists())
