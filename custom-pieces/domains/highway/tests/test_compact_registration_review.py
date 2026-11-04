"""Protect permanent identities during the bounded unpublished ramp revision."""
from copy import deepcopy
import importlib.util
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp.catalog import load_catalog, number, tile_base
from scp_highway.ramp_paths import module_catalog

_spec = importlib.util.spec_from_file_location(
    'compact_registration_review', ROOT / 'domains/highway/tools/register_highway_pieces.py')
registration = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(registration)


class CompactRegistrationReviewTests(unittest.TestCase):
    def setUp(self):
        self.catalog = load_catalog(ROOT)
        self.modules = module_catalog()

    def test_original_one_cell_branch_expands_within_its_reserved_identity(self):
        identifier = 'ddrhw-diagonal-lower-exit-branch'
        before = next(piece for piece in self.catalog['pieces'] if piece['id'] == identifier)
        identity = deepcopy({key: before[key] for key in ('id', 'puzzle_id', 'preview_id', 'menu', 'effect_name')})
        base = tile_base(before)
        before.update(footprint=[1, 1], cells=[[0, 0]], tile_ids=[f'{base:08x}'])
        before['shadow_mappings'] = [{'tile': f'{base:08x}', 'source': f'{base:08x}', 'rotation': 0}]
        self.catalog['_allocations']['pieces'][identifier].update(cells=[[0, 0]], tile_ids=[f'{base:08x}'])
        revised = registration.reviewed_extension(self.catalog, self.modules)
        after = next(piece for piece in revised['pieces'] if piece['id'] == identifier)
        self.assertEqual({key: after[key] for key in identity}, identity)
        self.assertEqual(after['footprint'], [2, 2])
        self.assertEqual(after['cells'], [[0, 0], [1, 0], [0, 1]])
        self.assertEqual([number(value) for value in after['tile_ids']], [base, base + 0x100, base + 0x10])
        self.assertEqual(tile_base(after), base)
        self.assertNotIn('authored_texture_ids', after)
        self.assertIn('mis', after['dependencies'])
        self.assertEqual(after['engineering']['max_grade_percent'], 30.0)

    def test_review_cannot_change_a_published_or_installed_allocation(self):
        self.catalog['_allocations']['pieces']['ddrhw-diagonal-access-core']['state'] = 'published'
        with self.assertRaisesRegex(ValueError, 'locally reserved'):
            registration.reviewed_extension(self.catalog, self.modules)

    def test_review_rejects_an_unapproved_curve_partition(self):
        branch = next(record for record in self.modules['types'] if record['key'] == 'upper-exit-branch')
        branch['cells'] = branch['cells'][:-1]
        with self.assertRaisesRegex(ValueError, 'independently reviewed partition'):
            registration.reviewed_extension(self.catalog, self.modules)

    def test_review_cannot_use_an_unreserved_model_block(self):
        self.catalog['_allocations']['pieces']['ddrhw-diagonal-access-core']['resource_blocks'] = []
        with self.assertRaisesRegex(ValueError, 'reserved resource blocks'):
            registration.reviewed_extension(self.catalog, self.modules)


if __name__ == '__main__':
    unittest.main()
