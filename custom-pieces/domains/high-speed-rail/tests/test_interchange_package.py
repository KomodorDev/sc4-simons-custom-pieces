"""Real-DAT regression, portable packaging and tampering for the rail expansion.

The full layout matrix is covered by the independent interchange tests. This
fixture exercises the shared packaging/install boundary with representative
current modular families. It never installs anything.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import posixpath
import re
import shutil
import sys
import tempfile
import unittest
import zipfile
from urllib.parse import unquote

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file())
sys.path.insert(0, str(ROOT / 'framework'))
from scp.build import build_project, package_build
from scp.catalog import load_catalog
from scp.dbpf import entries, decompress, pack_dbpf
from scp.verify import PATH, verify_build


class InterchangePackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        local = ROOT / 'local/settings.json'
        config = json.loads(local.read_text()) if local.exists() else {}
        plugins = os.environ.get('SCP_TEST_NAM_PLUGINS', config.get('plugins'))
        if not plugins or not Path(plugins).is_dir():
            raise unittest.SkipTest('Audited local NAM unavailable; set SCP_TEST_NAM_PLUGINS')
        catalog = load_catalog(ROOT)
        selected = ['hsr-diagonal-ghsr',
            'interchange-hsr-split-90-compact',
            'interchange-ground-merge-45-wide',
            'interchange-l4-split-135-wide',
            'interchange-oneway-grade-ground-to-hsr',
            'interchange-oneway-grade-hsr-to-l4',
            'interchange-l4-oneway-over-hsr',
            'interchange-l4-oneway-over-ground']
        known = {piece['id'] for piece in catalog['pieces']}
        if not set(selected) <= known:
            raise unittest.SkipTest('New interchange catalog has not been registered yet')
        cls.sandbox = tempfile.TemporaryDirectory(prefix='scp-interchange-package-')
        cls.base = Path(cls.sandbox.name).resolve()
        cls.fixture = cls.base/'fixture'
        try:
            build_project(ROOT, plugins, cls.fixture, include=selected,
                          extra_roots=config.get('extra_plugins', []))
        except BaseException:
            cls.sandbox.cleanup()
            raise
        cls.manifest = json.loads((cls.fixture/'manifest.json').read_text())
        cls.pieces = {piece['id']:piece for piece in cls.manifest['pieces']}

    @classmethod
    def tearDownClass(cls):
        cls.sandbox.cleanup()

    def setUp(self):
        self.case = Path(tempfile.mkdtemp(prefix='case-', dir=self.base))
        self.output = self.case/'portable'
        shutil.copytree(self.fixture, self.output)
        (self.output/'input-audit.json').unlink()

    def tearDown(self):
        shutil.rmtree(self.case)

    def test_new_families_verify_without_local_donors(self):
        report = verify_build(self.output, write_report=False)
        self.assertTrue(report['static_checks_passed'])
        self.assertFalse(report['local_donor_comparison'])
        self.assertFalse(self.manifest['in_game_tested'])
        self.assertFalse(self.manifest['installed'])

    def test_portable_ZIP_contains_the_human_domain_reference(self):
        archive = self.case/'pieces.zip'
        package_build(self.output, archive)
        with zipfile.ZipFile(archive) as zipped:
            self.assertIsNone(zipped.testzip())
            domain = 'docs/domains/high-speed-rail/'
            guides = [domain+'README.md', domain+'INVENTORY.md',
                      domain+'00_pieces/INVENTORY.md', domain+'01_assemblies/INVENTORY.md']
            for name in guides:
                self.assertIn(name, zipped.namelist())
            self.assertNotIn('input-audit.json', zipped.namelist())
            for name in guides:
                self.assertNotIn(b'/Users/', zipped.read(name))
            names = set(zipped.namelist())
            for name in names:
                if not name.endswith('.md'):
                    continue
                for target in re.findall(r'\]\((<[^>]+>|[^)\s]+)(?:\s+"[^"\n]*")?\)',
                                         zipped.read(name).decode()):
                    target = unquote(target.strip('<>'))
                    if '://' in target or target.startswith(('#', 'mailto:', 'codex:')):
                        continue
                    relative = target.split('#', 1)[0]
                    if relative:
                        self.assertFalse(relative.startswith('/'), (name, target))
                        resolved = posixpath.normpath(posixpath.join(posixpath.dirname(name), relative))
                        self.assertTrue(resolved in names or any(
                            member.startswith(resolved.rstrip('/')+'/') for member in names),
                            (name, target, resolved))

    def test_rehashed_height_collapse_cannot_pass_the_portable_verifier(self):
        piece = self.pieces['interchange-l4-oneway-over-hsr']
        path = self.output/piece['asset_file']
        resources = {key:decompress(value) for key,value in entries(path.read_bytes()).items()}
        changed = False
        for key, raw in resources.items():
            if key[:2] == PATH:
                replacement, count = re.subn(rb',30\.5(?=\r?\n)', b',15.5', raw, count=1)
                if count:
                    resources[key] = replacement
                    changed = True
                    break
        self.assertTrue(changed)
        raw = pack_dbpf(resources)
        path.write_bytes(raw)
        manifest_path = self.output/'manifest.json'
        manifest = json.loads(manifest_path.read_text())
        record = next(item for item in manifest['files'] if item['path'] == piece['asset_file'])
        record.update(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
        manifest_path.write_text(json.dumps(manifest,indent=2)+'\n')
        with self.assertRaises(ValueError):
            verify_build(self.output, write_report=False)


if __name__ == '__main__':
    unittest.main()
