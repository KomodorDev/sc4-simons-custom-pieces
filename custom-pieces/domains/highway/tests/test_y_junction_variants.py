"""Require finite variant identities before accepting another Y component."""
from pathlib import Path
import sys
import unittest

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]
from scp_highway import y_junction_variants as variants


class YVariantIdentityTests(unittest.TestCase):
    def spec(self, variant):
        row = variants.records_for(variant)[0]
        return {**row, 'domain': 'highway', 'y_junction_variant': variant}

    def test_original_absent_field_retains_its_existing_identity(self):
        piece = self.spec('original')
        piece.pop('y_junction_variant')
        self.assertEqual(variants.variant_of(piece), 'original')
        self.assertEqual(variants.assembly_for(), 'ddrhw-compact-diagonal-y-junction')

    def test_reversed_component_requires_its_own_recipe_and_explicit_field(self):
        piece = self.spec('reversed')
        self.assertEqual(variants.variant_of(piece), 'reversed')
        for key, value in (('recipe', 'highway_ddrhw_y_diagonal_stem_split'),
                           ('geometry_key', 'y-diagonal-stem-split'),
                           ('y_junction_variant', 'original')):
            with self.subTest(key=key), self.assertRaises(ValueError):
                variants.variant_of({**piece, key: value})
        piece.pop('y_junction_variant')
        with self.assertRaises(ValueError):
            variants.variant_of(piece)

    def test_an_original_component_cannot_opt_into_reversed_artwork(self):
        piece = self.spec('original')
        with self.assertRaises(ValueError):
            variants.variant_of({**piece, 'y_junction_variant': 'reversed'})

    def test_unknown_prefixed_types_do_not_gain_support(self):
        with self.assertRaises(ValueError):
            variants.variant_of({'id': 'ddrhw-y-reversed-unreviewed',
                                 'recipe': 'highway_ddrhw_y_reversed_unreviewed',
                                 'y_junction_variant': 'reversed'})
        with self.assertRaises(ValueError):
            variants.records_for('other')


if __name__ == '__main__':
    unittest.main()
