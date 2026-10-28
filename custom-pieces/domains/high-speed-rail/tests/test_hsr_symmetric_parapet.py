"""Reject missing recessed-end concrete, open walls, and double roof faces."""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json
from pathlib import Path
import unittest

from scp_hsr.hsr_symmetric_parapet_verify import (
    TOP, BED, BOTTOM, INNER, SECTIONS, audit_symmetric_wedges,
)

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'project.json').is_file())
PIECE = ROOT/'domains/high-speed-rail/00_pieces/hsr-component-modular-south-junction'


def quad(points):
    v = [(*p, .18, 0.) for p in points]
    return [(v[0], v[1], v[2]), (v[0], v[2], v[3])]


def sample_wedges():
    roof, wall, bottom = [], [], []
    nodes = [(24., 4.954047742), *SECTIONS, (41., 10.064)]
    for mirror in (False, True):
        transform = (lambda x: 32.-x) if mirror else (lambda x: x)
        for (a, ai), (b, bi) in zip(nodes, nodes[1:]):
            if bi >= INNER:
                b = a+(b-a)*(INNER-ai)/(bi-ai)
                bi = INNER
            x, y, edge = transform(ai), transform(bi), transform(INNER)
            roof.extend(quad(((x, TOP, a), (edge, TOP, a),
                              (edge, TOP, b), (y, TOP, b))))
            wall.extend(quad(((x, BED, a), (x, TOP, a),
                              (y, TOP, b), (y, BED, b))))
            wall.extend(quad(((edge, BED, a), (edge, TOP, a),
                              (edge, TOP, b), (edge, BED, b))))
        bottom.extend(quad(((transform(4.), BOTTOM, 24.), (transform(10.), BOTTOM, 24.),
                            (transform(10.), BOTTOM, 32.), (transform(4.), BOTTOM, 32.))))
    for low, high in ((6.393693924, 8.5), (23.5, 25.606306076)):
        wall.extend(quad(((low, BOTTOM, 24.), (high, BOTTOM, 24.),
                          (high, TOP, 24.), (low, TOP, 24.))))
    return roof, wall, bottom


class SymmetricParapetSavedFaceTests(unittest.TestCase):
    def test_raised_continuous_symmetric_wedges_with_closed_walls_pass(self):
        roof, wall, bottom = sample_wedges()
        report = audit_symmetric_wedges(roof+wall+bottom)
        self.assertEqual(report['symmetric_wedge_top_sections_checked'], 18)
        self.assertEqual(report['symmetric_wedge_inside_wall_sections_checked'], 36)
        self.assertEqual(report['symmetric_wedge_underside_sections_checked'], 6)

    def test_one_missing_roof_patch_is_rejected(self):
        roof, wall, bottom = sample_wedges()
        with self.assertRaisesRegex(ValueError, 'roof is interrupted'):
            audit_symmetric_wedges(roof[4:]+wall+bottom)

    def test_the_old_empty_wedge_is_rejected(self):
        roof, wall, bottom = sample_wedges()
        with self.assertRaisesRegex(ValueError, 'roof is interrupted'):
            audit_symmetric_wedges(wall+bottom)

    def test_one_side_cannot_be_left_unrepaired(self):
        roof, wall, bottom = sample_wedges()
        left_only = [t for t in roof if all(p[0] < 16. for p in t)]
        with self.assertRaisesRegex(ValueError, 'roof is interrupted'):
            audit_symmetric_wedges(left_only+wall+bottom)

    def test_a_ballast_height_patch_cannot_replace_the_raised_border(self):
        roof, wall, bottom = sample_wedges()
        flat = [tuple((p[0], BED, *p[2:]) for p in t) for t in roof]
        with self.assertRaisesRegex(ValueError, 'roof is interrupted'):
            audit_symmetric_wedges(flat+wall+bottom)

    def test_roof_without_inside_faces_is_rejected(self):
        roof, wall, bottom = sample_wedges()
        with self.assertRaisesRegex(ValueError, 'matching inside wall'):
            audit_symmetric_wedges(roof+bottom)

    def test_missing_underside_is_rejected(self):
        roof, wall, bottom = sample_wedges()
        with self.assertRaisesRegex(ValueError, 'closed underside'):
            audit_symmetric_wedges(roof+wall)

    def test_missing_recessed_end_cap_is_rejected(self):
        roof, wall, bottom = sample_wedges()
        open_walls = [t for t in wall if not all(abs(p[2]-24.) < 1e-8 for p in t)]
        with self.assertRaisesRegex(ValueError, 'open recessed-plane end cap'):
            audit_symmetric_wedges(roof+open_walls+bottom)

    def test_duplicate_positive_area_roof_is_rejected(self):
        roof, wall, bottom = sample_wedges()
        with self.assertRaisesRegex(ValueError, 'overlapping concrete roofs'):
            audit_symmetric_wedges(roof+roof+wall+bottom)

    def test_clearance_intrusion_is_rejected_by_the_literal_boundary(self):
        roof, wall, bottom = sample_wedges()
        intrusion = quad(((4., TOP, 24.), (5., TOP, 24.), (6., TOP, 28.), (4., TOP, 28.)))
        with self.assertRaisesRegex(ValueError, 'roof is interrupted'):
            audit_symmetric_wedges(roof+intrusion+wall+bottom)

    def test_source_changes_only_the_explicit_wedge_rule(self):
        baseline = (PIECE/'evidence/design-history/missing-junction-wedges/geometry.json').read_bytes()
        self.assertEqual(hashlib.sha256(baseline).hexdigest(),
                         '72005262cfa843a3c380da08e5cab2f03106e3dce7b350b126b70ca5df595fdd')
        current = json.loads((PIECE/'evidence/design-history/before-stem-border-repair/geometry.json').read_text())
        rule = current.pop('junction_wedge_alignment')
        self.assertEqual(current, json.loads(baseline))
        self.assertEqual(rule['branch_inner_half_width_m'], 2.6)
        self.assertEqual(rule['minimum_train_half_width_m'], 2.5)


if __name__ == '__main__':
    unittest.main()
