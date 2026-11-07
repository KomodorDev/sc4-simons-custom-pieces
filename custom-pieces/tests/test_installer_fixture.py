"""Synthetic player fixtures exercise packaging without native game inputs."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'installer'))
import prepare_fixture as fixture
from scp import jsonc
from scp.dbpf import entries
from scp.install import FOLDER
from scp.player_manifest import build_install_manifest
from scp.prebuilt import verify_payload


COMMIT = '1234567890abcdef1234567890abcdef12345678'


class InstallerFixtureTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix='scp-player-fixture-test-')
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name).resolve()

    def test_complete_fixture_is_deterministic_and_uses_only_synthetic_resources(self):
        first, second = self.base / 'first', self.base / 'second'
        manifest = fixture.prepare_fixture(ROOT, first, COMMIT)
        self.assertEqual(manifest, fixture.prepare_fixture(ROOT, second, COMMIT))
        self.assertEqual(manifest, verify_payload(first, COMMIT))
        self.assertEqual((first / 'manifest.json').read_bytes(), (second / 'manifest.json').read_bytes())
        project = jsonc.load(ROOT / 'project.jsonc')
        expected_ids, labels = [], {'controller'}
        for domain in project['domains'].values():
            registry = jsonc.load(ROOT / domain['registry'])
            for relative in registry.get('pieces', []):
                piece = jsonc.load(ROOT / domain['path'] / relative)
                if piece['status'] != 'draft':
                    expected_ids.append(piece['id'])
                    labels.update(piece['dependencies'])
        profile = jsonc.load(ROOT / project['profile'])
        self.assertEqual([row['id'] for row in manifest['pieces']], expected_ids)
        self.assertEqual(manifest['profile'], {'id': profile['id'], 'donors': [
            {key: profile['files'][label][key] for key in ('filename', 'sha256')} for label in sorted(labels)]})
        self.assertEqual(manifest['dependency_audit'], {'textures': [], 'shadows': []})
        self.assertEqual(len(manifest['files']), len(expected_ids) + 2)
        identities = set()
        for row in manifest['files']:
            raw = (first / row['path']).read_bytes()
            self.assertEqual(raw, (second / row['path']).read_bytes())
            self.assertEqual(sha256(raw).hexdigest(), row['sha256'])
            resources = entries(raw)
            self.assertFalse(identities & resources.keys())
            identities.update(resources)
            self.assertTrue(all(value.startswith(fixture.MARKER) for value in resources.values()))
        compact = build_install_manifest(ROOT, first)
        self.assertEqual([row['id'] for row in compact['pieces']], expected_ids)
        self.assertEqual(compact['source_commit'], COMMIT)
        self.assertEqual(compact['policy'], jsonc.load(ROOT / 'config/installer.jsonc'))
        self.assertTrue(compact['captures'])
        self.assertLess(sum(row['bytes'] for row in manifest['files']), 1024 * 1024)
        self.assertEqual({path.name for path in first.iterdir()}, {FOLDER, 'manifest.json'})

    def test_output_refuses_existing_paths_and_paths_inside_the_checkout(self):
        existing = self.base / 'existing'
        existing.mkdir()
        for output in (existing, ROOT / 'local/synthetic-fixture-must-not-exist', ROOT.parent / 'fixture-must-not-exist',
                       ROOT.parent / '..' / ROOT.parent.name / 'fixture-must-not-exist'):
            with self.subTest(output=output), self.assertRaisesRegex(ValueError, 'new, outside the checkout'):
                fixture.prepare_fixture(ROOT, output, COMMIT)
        self.assertEqual(list(existing.iterdir()), [])
        self.assertFalse((ROOT / 'local/synthetic-fixture-must-not-exist').exists())
        self.assertFalse((ROOT.parent / 'fixture-must-not-exist').exists())

    def test_invalid_commit_is_rejected_before_creating_output(self):
        output = self.base / 'invalid'
        for commit in ('main', 'a' * 12, 'A' * 40, 'a' * 39):
            with self.subTest(commit=commit), self.assertRaisesRegex(ValueError, 'complete lowercase Git commit'):
                fixture.prepare_fixture(ROOT, output, commit)
        self.assertFalse(output.exists())

    def test_cli_uses_only_standard_library_and_reports_review_only_scope(self):
        code = """
import builtins
from pathlib import Path
import sys
root = Path(sys.argv[1])
sys.path.insert(0, str(root / 'installer'))
original = builtins.__import__
def checked(name, *args, **kwargs):
    if name in {'scp.catalog', 'scp.build', 'scp.verify', 'scp.menu', 'scp.resource_audit', 'scp.track_paths'} or name.split('.')[0] in {'scp_hsr', 'scp_highway', 'shapely', 'numpy', 'PIL'}:
        raise AssertionError('Fixture imported authoring dependency: ' + name)
    return original(name, *args, **kwargs)
builtins.__import__ = checked
import prepare_fixture
raise SystemExit(prepare_fixture.main(['--source', str(root), '--output', sys.argv[2], '--source-commit', sys.argv[3]]))
"""
        output = self.base / 'cli'
        result = subprocess.run([sys.executable, '-B', '-c', code, str(ROOT), str(output), COMMIT],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        report = json.loads(result.stdout)
        self.assertTrue(report['synthetic_review_fixture'])
        self.assertFalse(report['playable'])
        self.assertEqual(report['source_commit'], COMMIT)
        self.assertEqual(verify_payload(output, COMMIT)['source_commit'], COMMIT)

    def test_prepared_fixture_self_test_records_its_synthetic_scope(self):
        import build_bundle
        payload = self.base / 'payload'
        fixture.prepare_fixture(ROOT, payload, COMMIT)
        runtime = self.base / 'runtime'
        build_bundle.prepare_runtime(ROOT, runtime, COMMIT, 'windows-x64', prebuilt_payload=payload)
        report = self.base / 'report.json'
        result = subprocess.run([sys.executable, '-I', '-S', '-B', str(runtime / 'installer/main.py'),
                                 '--self-test', '--report', str(report)], capture_output=True, text=True, timeout=60)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        checked = json.loads(report.read_text())
        self.assertTrue(checked['synthetic_payload_only'])
        self.assertTrue(checked['synthetic_review_fixture'])
        self.assertTrue(checked['repeat_install_and_rollback'])


if __name__ == '__main__':
    unittest.main()
