"""Keep side, travel, family identity, and native cut selection distinct."""
from dataclasses import FrozenInstanceError
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'framework'))
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0, SourcePackages(ROOT))
from scp_highway import diagonal_transition_variants as variants


class DiagonalTransitionIdentityTests(unittest.TestCase):
    def spec(self, key):
        record = variants.record_for(key)
        return {'domain': 'highway', 'id': record.piece_id, 'recipe': record.recipe,
                'diagonal_transition_variant': key, 'diagonal_transition_alignment': 'a'}

    def test_four_finite_identities_keep_side_and_traffic_independent(self):
        expected = (('original', False, False, False), ('mirrored', True, True, False),
                    ('opposite-side', True, False, True),
                    ('opposite-side-mirrored', False, True, True))
        self.assertEqual(variants.VARIANTS, tuple(row[0] for row in expected))
        self.assertEqual(len(set(variants.PIECE_IDS)), 4)
        self.assertEqual(len(set(variants.RECIPES)), 4)
        for key, reflected, reversed_traffic, opposite in expected:
            with self.subTest(key=key):
                record = variants.record_for(key)
                self.assertEqual((record.physical_reflection, record.traffic_reversed,
                                  record.opposite_side), (reflected, reversed_traffic, opposite))
                self.assertEqual(variants.variant_of(self.spec(key)), key)
                self.assertLessEqual(len(record.piece_id), 64)
                self.assertTrue(record.piece_id.endswith('-alignment-a'))
                with self.assertRaises(FrozenInstanceError):
                    record.recipe = 'unreviewed_recipe'

    def test_old_family_unknown_prefixes_and_other_native_cuts_are_rejected(self):
        for field, value in (('id', 'ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile'),
                             ('id', variants.PIECE_ID + '-unreviewed'),
                             ('recipe', 'highway_ddrhw_orthogonal_l0_transition'),
                             ('diagonal_transition_alignment', 'b'),
                             ('domain', 'high-speed-rail')):
            with self.subTest(field=field, value=value):
                piece = self.spec('original'); piece[field] = value
                with self.assertRaises(ValueError):
                    variants.variant_of(piece)

    def test_every_mixed_variant_recipe_pair_is_rejected(self):
        for first in variants.VARIANTS:
            for second in variants.VARIANTS:
                if first != second:
                    with self.subTest(first=first, second=second):
                        piece = self.spec(first)
                        piece['recipe'] = variants.record_for(second).recipe
                        with self.assertRaises(ValueError):
                            variants.variant_of(piece)

    def test_new_sources_require_explicit_variant_and_alignment(self):
        for field in ('diagonal_transition_variant', 'diagonal_transition_alignment'):
            piece = self.spec('original'); del piece[field]
            with self.subTest(field=field), self.assertRaises(ValueError):
                variants.variant_of(piece)
        for value in (None, False, 0, '', 'alignment-b', 'original-extra'):
            with self.subTest(value=value), self.assertRaises(ValueError):
                variants.record_for(value)


if __name__ == '__main__':
    unittest.main()
