"""Model audit reuse requires exact worker and saved-verification inputs."""

import unittest
from unittest.mock import patch

from scp import build, verify


class CompiledHighwayModelAuditTests(unittest.TestCase):
    def setUp(self):
        self.piece = {'id': 'highway-fixture', 'domain': 'highway', 'footprint': [1, 2]}
        self.resources = {(*verify.S3D, 0x100): b'authored model',
                          (*verify.PATH, 0x100): b'authored traffic path'}
        self.donors = {verify.RUL0: b'native rules', verify.NETWORK_INI: b'native configuration'}
        self.report = {'texture_ids': [0x200], 'details': {'checked': True}}

    def test_exact_inputs_reuse_a_copy_of_the_checked_report(self):
        with verify.compiled_highway_model_audits() as cache, \
                patch.object(verify, 'check_piece_models') as check:
            cache.update(donors=self.donors, pieces={
                self.piece['id']: (self.piece, self.resources, self.report),
            })
            donors = dict(self.donors)
            audits = verify._matching_compiled_highway_models(donors)
            result = verify._check_saved_piece_models(dict(self.resources), dict(self.piece), donors, audits)
            self.assertEqual(result, self.report)
            result.pop('texture_ids')
            result['details']['checked'] = False
            self.assertEqual(self.report, {'texture_ids': [0x200], 'details': {'checked': True}})
            check.assert_not_called()

    def test_changed_donors_record_or_resource_requires_a_new_check(self):
        with verify.compiled_highway_model_audits() as cache:
            cache.update(donors=self.donors, pieces={
                self.piece['id']: (self.piece, self.resources, self.report),
            })
            changed = (
                (self.piece, self.resources, {**self.donors, verify.RUL0: b'changed'}),
                (self.piece, self.resources, {}),
                ({**self.piece, 'footprint': [True, 2]}, self.resources, self.donors),
                ({**self.piece, 'domain': 'high-speed-rail'}, self.resources, self.donors),
                (self.piece, {**self.resources, (*verify.PATH, 0x100): b'changed'}, self.donors),
                (self.piece, {**self.resources, (*verify.S3D, 0x101): b'extra'}, self.donors),
            )
            for piece, resources, donors in changed:
                with self.subTest(piece=piece, resources=resources, donors=donors), \
                        patch.object(verify, 'check_piece_models') as check:
                    audits = verify._matching_compiled_highway_models(donors)
                    result = verify._check_saved_piece_models(resources, piece, donors, audits)
                    self.assertIs(result, check.return_value)
                    check.assert_called_once_with(resources, piece, donors)

    def test_scope_is_reentrant_and_clears_after_error(self):
        with self.assertRaisesRegex(RuntimeError, 'build failed'):
            with verify.compiled_highway_model_audits() as outer:
                outer.update(donors=self.donors, pieces={self.piece['id']: self.report})
                with verify.compiled_highway_model_audits() as inner:
                    self.assertIs(outer, inner)
                    self.assertEqual(verify._matching_compiled_highway_models(self.donors), outer['pieces'])
                    raise RuntimeError('build failed')
        self.assertEqual(verify._matching_compiled_highway_models(self.donors), {})


class BuildWorkerDispatchTests(unittest.TestCase):
    def test_worker_imports_source_recipes_and_reports_piece_failure(self):
        pieces = [
            {'id': f'worker-probe-{number}', 'domain': 'highway',
             'recipe': 'invalid_worker_recipe', 'tile_ids': []}
            for number in (1, 2)
        ]
        groups = build._compile_groups(pieces)
        with self.assertRaisesRegex(ValueError, r'worker-probe-[12]: Unsupported highway recipe'):
            build._compile_in_parallel(groups, 2, {}, {}, 'test', None)
