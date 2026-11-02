"""Reject stale B resource proofs across the complete verification context."""
from copy import deepcopy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp_highway import parallel_b_connector_contracts

TOOL = 'domains/highway/tools/freeze_parallel_b_connectors.py'
_spec = importlib.util.spec_from_file_location('_parallel_b_proof_reuse_freezer', ROOT / TOOL)
freezer = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(freezer)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


class ParallelBProofContextTests(unittest.TestCase):
    def test_actual_context_pins_shared_a_adaptive_native_and_framework_dependencies(self):
        context = freezer._verification_source_hashes(ROOT)
        dependencies = (
            'framework/scp/connectivity.py',
            'framework/scp/adaptive_network.py',
            'framework/scp/model_shadows.py',
            'domains/highway/implementation/scp_highway/parallel_verify.py',
            'domains/highway/implementation/scp_highway/parallel_geometry.py',
            'domains/highway/implementation/scp_highway/adaptive_ground.py',
            'domains/highway/implementation/scp_highway/adaptive_verify.py',
            'domains/highway/implementation/scp_highway/native.py',
            TOOL,
        )
        for name in dependencies:
            with self.subTest(dependency=name):
                self.assertIn(name, context)
                self.assertEqual(context[name], digest((ROOT / name).read_bytes()))


class ParallelBProofReuseTests(unittest.TestCase):
    """Use real guard execution with a small, explicitly synthetic proof record."""

    SOURCES = (
        'framework/scp/connectivity.py',
        'framework/scp/nested/native_validation.py',
        'domains/highway/implementation/scp_highway/parallel_verify.py',
        'domains/highway/implementation/scp_highway/parallel_geometry.py',
        'domains/highway/implementation/scp_highway/adaptive_ground.py',
        'domains/highway/implementation/scp_highway/adaptive_verify.py',
        TOOL,
    )

    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.root = Path(self.folder.name)
        for index, name in enumerate(self.SOURCES):
            self.write(name, f'# Synthetic source {index}: {name}\n'.encode())
        self.write('docs/notes.py', b'# Outside the owning verification packages.\n')
        self.write('framework/scp/__pycache__/connectivity.cpython-311.pyc', b'old cache')
        self.build = self.root / 'dist/candidate'
        payload = b'Synthetic saved payload; never a native validation fixture.'
        self.write('dist/candidate/pieces/component.dat', payload)
        self.manifest = {'files': [{'path': 'pieces/component.dat', 'bytes': len(payload),
                                    'sha256': digest(payload)}]}
        self.manifest_raw = json.dumps(self.manifest, sort_keys=True).encode()
        self.scene = self.root / 'domains/highway/01_assemblies/synthetic/assembly.jsonc'
        self.write(self.scene.relative_to(self.root), b'{"placements": []}\n')
        self.saved_checks = {'paths': {'passed': True, 'synthetic': True},
                             'models': {'passed': True, 'synthetic': True}}
        self.accepted = {'synthetic-recipe': {'reference_piece_id': 'synthetic-component',
                                              'saved_checks': deepcopy(self.saved_checks)}}
        prior = {
            'source': {'manifest_sha256': digest(self.manifest_raw),
                       'assembly_source_sha256': digest(self.scene.read_bytes()),
                       'approval_sha256': freezer.APPROVAL_SHA256,
                       'source_sha256': freezer._verification_source_hashes(self.root)},
            'verification': {
                'package': 'passed', 'all_fifteen_saved_path_and_model_checks': 'passed',
                'assembly': 'passed', 'native_wheeltrack_seam_uv': {'passed': True, 'synthetic': True},
                'assembly_resources_only_package_construction_status': 'not-run'},
        }
        self.prior_raw = json.dumps(prior, sort_keys=True).encode()
        self.write(freezer.REFERENCE, self.prior_raw)
        self.loader = self.enterContext(patch.object(parallel_b_connector_contracts, 'load_contracts',
                                                     return_value=self.accepted))

    def write(self, name, raw):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        return path

    def reuse(self):
        return freezer._reuse_accepted_checks(self.root, self.build, self.manifest_raw,
                                              self.manifest, self.scene)

    def assert_source_rejected(self):
        with self.assertRaisesRegex(ValueError, 'framework/provider source changes'):
            self.reuse()

    def test_context_has_the_exact_recursive_owned_source_roster_and_digests(self):
        expected = {name: digest((self.root / name).read_bytes()) for name in self.SOURCES}
        self.assertEqual(freezer._verification_source_hashes(self.root), expected)

    def test_unchanged_context_reuses_only_hash_bound_successful_saved_checks(self):
        pieces, assembly, acceptance_hash = self.reuse()
        self.assertEqual(pieces, {'synthetic-component': self.saved_checks})
        self.assertTrue(assembly['saved_resource_checks_passed'])
        self.assertEqual(assembly['package_construction_checks'], 'not-run')
        self.assertEqual(acceptance_hash, digest(self.prior_raw))
        self.loader.assert_called_once_with(self.root)
        pieces['synthetic-component']['paths']['passed'] = False
        self.assertTrue(self.accepted['synthetic-recipe']['saved_checks']['paths']['passed'])

    def test_shared_a_adaptive_and_framework_source_mutations_reject_reuse(self):
        for name in self.SOURCES:
            with self.subTest(source=name):
                path = self.root / name
                original = path.read_bytes()
                path.write_bytes(original + b'# Changed validation behavior.\n')
                try:
                    self.assert_source_rejected()
                finally:
                    path.write_bytes(original)

    def test_a_new_framework_or_provider_module_rejects_the_old_roster(self):
        for name in ('framework/scp/new_validator.py',
                     'domains/highway/implementation/scp_highway/nested/new_validator.py'):
            with self.subTest(source=name):
                path = self.write(name, b'# A newly introduced proof dependency.\n')
                try:
                    self.assert_source_rejected()
                finally:
                    path.unlink()

    def test_removing_a_framework_or_provider_module_rejects_the_old_roster(self):
        for name in ('framework/scp/nested/native_validation.py',
                     'domains/highway/implementation/scp_highway/parallel_geometry.py'):
            with self.subTest(source=name):
                path = self.root / name
                original = path.read_bytes()
                path.unlink()
                try:
                    self.assert_source_rejected()
                finally:
                    path.write_bytes(original)

    def test_bytecode_caches_and_sources_outside_the_owning_context_do_not_change_reuse(self):
        before = freezer._verification_source_hashes(self.root)
        self.write('framework/scp/__pycache__/connectivity.cpython-311.pyc', b'new cache')
        self.write('domains/highway/implementation/scp_highway/__pycache__/native.cpython-311.pyc',
                   b'new provider cache')
        self.write('docs/notes.py', b'# This remains outside the proof dependency context.\n')
        self.assertEqual(freezer._verification_source_hashes(self.root), before)
        self.assertTrue(self.reuse()[1]['saved_resource_checks_passed'])

    def test_changed_saved_package_bytes_cannot_reuse_a_matching_source_context(self):
        self.write('dist/candidate/pieces/component.dat', b'changed saved payload')
        with self.assertRaisesRegex(ValueError, 'changed package bytes'):
            self.reuse()

    def test_changed_scene_cannot_reuse_a_matching_source_context(self):
        self.scene.write_bytes(b'{"placements": [{"changed": true}]}\n')
        with self.assertRaisesRegex(ValueError, 'changed manifest, scene, or approval'):
            self.reuse()


if __name__ == '__main__':
    unittest.main()
