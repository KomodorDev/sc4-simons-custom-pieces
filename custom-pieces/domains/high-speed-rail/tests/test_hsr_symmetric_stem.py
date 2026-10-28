"""Reject the old southern pinch and incomplete straight-to-curve repairs."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import unittest

from scp_hsr.hsr_symmetric_stem_verify import (
    TOP, BED, INNER, JOIN_SOUTH, STEM_SECTIONS, audit_symmetric_stem,
)

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'project.jsonc').is_file())
PIECE = ROOT/'domains/high-speed-rail/00_pieces/hsr-component-modular-south-junction'


def quad(points):
    vertices = [(*p, .18, 0.) for p in points]
    return [(vertices[0], vertices[1], vertices[2]),
            (vertices[0], vertices[2], vertices[3])]


def sample_stem():
    roofs, walls = [], []
    nodes = [(47., 5.05, 6.52), *STEM_SECTIONS, (88., 8.5, INNER)]
    for mirror in (False, True):
        transform = (lambda x: 32.-x) if mirror else (lambda x: x)
        for (a, ao, ai), (b, bo, bi) in zip(nodes, nodes[1:]):
            roofs.extend(quad(((transform(ao), TOP, a), (transform(ai), TOP, a),
                               (transform(bi), TOP, b), (transform(bo), TOP, b))))
            for x, y in ((ao, bo), (ai, bi)):
                walls.extend(quad(((transform(x), BED, a), (transform(x), TOP, a),
                                   (transform(y), TOP, b), (transform(y), BED, b))))
    return roofs, walls


class SymmetricStemSavedFaceTests(unittest.TestCase):
    def test_both_straight_stems_and_exact_ballast_curve_joins_pass(self):
        roofs, walls = sample_stem()
        result = audit_symmetric_stem(roofs+walls)
        self.assertEqual(result['symmetric_stem_top_sections_checked'], 32)
        self.assertEqual(result['symmetric_stem_inside_wall_sections_checked'], 64)
        self.assertEqual(result['symmetric_stem_straight_to_curve_joins_checked'], 2)

    def test_previous_early_pinched_inner_edge_is_rejected(self):
        roofs, walls = sample_stem()
        pinched = [tuple((min(p[0], 9.151094277) if p[0] < 16. else p[0], *p[1:])
                         for p in triangle) for triangle in roofs]
        with self.assertRaisesRegex(ValueError, 'straight-to-ballast outline'):
            audit_symmetric_stem(pinched+walls)

    def test_one_side_cannot_remain_unrepaired(self):
        roofs, walls = sample_stem()
        with self.assertRaisesRegex(ValueError, 'straight-to-ballast outline'):
            audit_symmetric_stem([t for t in roofs if max(p[0] for p in t) < 16.]+walls)

    def test_straight_roof_cannot_continue_past_the_ballast_line(self):
        roofs, walls = sample_stem()
        intrusion = quad(((8.5, TOP, 56.), (INNER, TOP, 56.),
                          (INNER, TOP, 58.), (8.5, TOP, 58.)))
        with self.assertRaisesRegex(ValueError, 'straight-to-ballast outline'):
            audit_symmetric_stem(roofs+intrusion+walls)

    def test_raised_roof_without_inside_walls_is_rejected(self):
        roofs, _ = sample_stem()
        with self.assertRaisesRegex(ValueError, 'matching inside wall'):
            audit_symmetric_stem(roofs)

    def test_missing_southern_straight_inside_wall_is_rejected(self):
        roofs, walls = sample_stem()
        missing = [t for t in walls if not(all(abs(p[0]-INNER) < 1e-8 for p in t)
                                          and min(p[2] for p in t) >= JOIN_SOUTH)]
        with self.assertRaisesRegex(ValueError, 'matching inside wall'):
            audit_symmetric_stem(roofs+missing)

    def test_flat_ballast_height_patch_is_rejected(self):
        roofs, walls = sample_stem()
        flat = [tuple((p[0], BED, *p[2:]) for p in triangle) for triangle in roofs]
        with self.assertRaisesRegex(ValueError, 'straight-to-ballast outline'):
            audit_symmetric_stem(flat+walls)

    def test_duplicate_positive_area_roof_is_rejected(self):
        roofs, walls = sample_stem()
        with self.assertRaisesRegex(ValueError, 'overlapping concrete roofs'):
            audit_symmetric_stem(roofs+roofs+walls)

    def test_only_new_stem_rule_changes_the_accepted_wedge_source(self):
        baseline = (PIECE/'evidence/design-history/before-stem-border-repair/geometry.json').read_bytes()
        self.assertEqual(hashlib.sha256(baseline).hexdigest(),
                         'd0c24a85209a56f0ac3e924b3f66e9ee291fd8362e65726c975b1033eaf3066a')
        current = json.loads((PIECE/'geometry.json').read_text())
        rule = current.pop('stem_parapet_alignment')
        self.assertEqual(current, json.loads(baseline))
        self.assertEqual(rule['branch_inner_half_width_m'], 2.6)
        self.assertEqual(rule['minimum_train_half_width_m'], 2.5)
        self.assertEqual(rule['stem_scope_local_south_m'], [48., 88.])


if __name__ == '__main__':
    unittest.main()
