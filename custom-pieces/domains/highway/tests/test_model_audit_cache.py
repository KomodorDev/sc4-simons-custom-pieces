"""Exact-input cache controls without running expensive native mesh audits."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT/'framework'),str(ROOT/'domains/highway/implementation')]

from scp_highway import ramp_verify as verifier


class ModelAuditCacheTests(unittest.TestCase):
    def setUp(self):
        verifier._MODEL_AUDIT_CACHE.clear()
        self.addCleanup(verifier._MODEL_AUDIT_CACHE.clear)
        self.resources = {
            (0x5AD0E817,0xBADB57F1,0x100): b'model with material and UV bytes',
            (0x5AD0E817,0xBADB57F1,0x101): b'zoom',
            (0x5AD0E817,0xBADB57F1,0x200): b'preview',
            (0x296678F7,0xA966883F,0x100): b'PATH',
            (0x6534284A,0xC977C536,0x100): b'exemplar',
            (0x7AB50E44,0x1ABE787D,0x300): b'texture',
        }
        self.piece = {'id':'cache-control','cells':[[0,0]],'tile_ids':['00000100'],
                      'engineering':{'max_grade_percent':30.,'extra':{'nested':[1,2]}}}
        self.report = {'passed':True,'texture_ids':[0x300],'atlas':{'checks':[True]},
                       'game_rendering_tested':False}
        self.audit = self.enterContext(patch.object(verifier,'_check_models_uncached',
                                                   return_value=self.report))

    def test_equal_inputs_reuse_success_and_return_independent_nested_reports(self):
        first = verifier.check_models(self.resources,self.piece)
        first.pop('texture_ids')
        first['atlas']['checks'].append(False)
        second = verifier.check_models(dict(reversed(list(self.resources.items()))),deepcopy(self.piece))
        self.assertEqual(second,self.report)
        second['atlas']['checks'].clear()
        self.assertEqual(verifier.check_models(self.resources,self.piece),self.report)
        self.assertEqual(self.audit.call_count,1)

    def test_every_resource_class_invalidates_even_same_length_or_unreferenced(self):
        verifier.check_models(self.resources,self.piece)
        for key in self.resources:
            with self.subTest(resource=key):
                changed = dict(self.resources)
                changed[key] = bytes([changed[key][0]^1])+changed[key][1:]
                verifier.check_models(changed,self.piece)
        self.assertEqual(self.audit.call_count,1+len(self.resources))
        removed = dict(self.resources);removed.pop(next(iter(removed)))
        verifier.check_models(removed,self.piece)
        added = {**self.resources,(1,2,3):b'unreferenced'}
        verifier.check_models(added,self.piece)
        self.assertEqual(self.audit.call_count,3+len(self.resources))

    def test_complete_nested_specification_invalidates_and_is_snapshotted(self):
        verifier.check_models(self.resources,self.piece)
        self.piece['engineering']['extra']['nested'][1] = 3
        verifier.check_models(self.resources,self.piece)
        self.assertEqual(self.audit.call_count,2)
        audited_piece = self.audit.call_args.args[1]
        self.piece['engineering']['extra']['nested'].append(4)
        self.assertEqual(audited_piece['engineering']['extra']['nested'],[1,3])

    def test_mutable_resource_buffers_are_snapshotted_and_rehashed(self):
        key = next(iter(self.resources))
        mutable = bytearray(self.resources[key]);self.resources[key] = mutable
        verifier.check_models(self.resources,self.piece)
        audited_resources = self.audit.call_args.args[0]
        mutable[0] ^= 1
        self.assertNotEqual(audited_resources[key],bytes(mutable))
        verifier.check_models(self.resources,self.piece)
        self.assertEqual(self.audit.call_count,2)

    def test_raised_failures_and_negative_reports_are_never_cached(self):
        self.audit.side_effect = ValueError('saved input rejected')
        for _ in range(2):
            with self.assertRaisesRegex(ValueError,'saved input rejected'):
                verifier.check_models(self.resources,self.piece)
        self.audit.side_effect = None;self.audit.return_value = {'passed':False}
        for _ in range(2):
            self.assertFalse(verifier.check_models(self.resources,self.piece)['passed'])
        self.assertEqual(self.audit.call_count,4)
        self.assertFalse(verifier._MODEL_AUDIT_CACHE)

    def test_live_tolerance_and_validator_replacement_invalidate(self):
        verifier.check_models(self.resources,self.piece)
        with patch.object(verifier,'SUPPORT_ENCODING_DISTANCE_M',3e-6):
            verifier.check_models(self.resources,self.piece)
        self.assertEqual(self.audit.call_count,2)
        with patch.object(verifier,'check_pavement'):
            verifier.check_models(self.resources,self.piece)
        self.assertEqual(self.audit.call_count,3)

    def test_frozen_native_evidence_change_invalidates(self):
        from scp_highway import native_overhangs
        verifier.check_models(self.resources,self.piece)
        with patch.object(native_overhangs,'NATIVE_OVERHANG_TRIANGLES',frozenset({'changed'})):
            verifier.check_models(self.resources,self.piece)
        self.assertEqual(self.audit.call_count,2)

    def test_validator_source_bytes_change_invalidates_without_a_disk_write(self):
        verifier.check_models(self.resources,self.piece)
        original = Path.read_bytes
        def source_bytes(path):
            raw = original(path)
            return raw+b'\n# changed validator source' if path.name=='wheeltrack_verify.py' else raw
        with patch.object(Path,'read_bytes',source_bytes):
            verifier.check_models(self.resources,self.piece)
        self.assertEqual(self.audit.call_count,2)

    def test_success_cache_is_bounded_and_uses_least_recently_used_eviction(self):
        for number in range(32):
            verifier.check_models(self.resources,{**self.piece,'sequence':number})
        self.assertEqual(len(verifier._MODEL_AUDIT_CACHE),32)
        verifier.check_models(self.resources,{**self.piece,'sequence':0})
        verifier.check_models(self.resources,{**self.piece,'sequence':32})
        verifier.check_models(self.resources,{**self.piece,'sequence':0})
        self.assertEqual(self.audit.call_count,33)
        verifier.check_models(self.resources,{**self.piece,'sequence':1})
        self.assertEqual(self.audit.call_count,34)
        self.assertEqual(len(verifier._MODEL_AUDIT_CACHE),32)


if __name__=='__main__':
    unittest.main()
