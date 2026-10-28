"""Reject interrupted banks, the old X3 gap, and open or duplicated concrete."""
from __future__ import annotations

import unittest

from scp_hsr.hsr_atomic_components_verify import CONTRACTS, audit_south_parapet_alignment


DIVERGE = 'hsr_component_l2_short_mainline_diverge_core'
MERGE = 'hsr_component_l2_short_opposed_merge_core'
INNER, OUTER, BED, TOP = 5.9965477, 7.5, 16.1893253, 16.9893265
OLD_LEFT, OLD_RIGHT = 20.97718809637104, 43.776078282276934
LEFT_SECTIONS = (
    (-8., INNER, OUTER), (8., INNER, OUTER), (16., INNER, OUTER),
    (20., INNER, OUTER), (21., 6.087372560, 7.503469160),
    (22., 6.243395951, 7.661687198), (24., 6.589828567, 8.),
    (26., 6.985743322, 8.), (28., 7.435250367, 8.),
    (30., 7.942643462, 8.), (30.212506, 8., 8.),
)
RIGHT_POINTS = CONTRACTS[DIVERGE]['south_parapet_right_join_points_east_south_m']


def quad(points):
    vertices = [(*point, .18, 0.) for point in points]
    return [(vertices[0], vertices[1], vertices[2]),
            (vertices[0], vertices[2], vertices[3])]


def left_top():
    result = []
    for (a, ai, ao), (b, bi, bo) in zip(LEFT_SECTIONS, LEFT_SECTIONS[1:]):
        result.extend(quad(((a, TOP, ai), (b, TOP, bi),
                            (b, TOP, bo), (a, TOP, ao))))
    return result


def left_walls(straight_only=False):
    result = []
    for (a, ai, _), (b, bi, _) in zip(LEFT_SECTIONS, LEFT_SECTIONS[1:]):
        if straight_only and b > 20.:
            continue
        result.extend(quad(((a, BED, ai), (a, TOP, ai),
                            (b, TOP, bi), (b, BED, bi))))
    return result


def right_top(old=False):
    if old:
        return quad(((OLD_RIGHT, TOP, INNER), (56., TOP, INNER),
                     (56., TOP, OUTER), (OLD_RIGHT, TOP, OUTER)))
    result = []
    points = [*RIGHT_POINTS, (56., OUTER)]
    for (a, outside_a), (b, outside_b) in zip(points, points[1:]):
        result.extend(quad(((a, TOP, INNER), (b, TOP, INNER),
                            (b, TOP, outside_b), (a, TOP, outside_a))))
    return result


def right_walls(curved=True, straight=True):
    result = []
    for (a, outside_a), (b, outside_b) in zip(RIGHT_POINTS, RIGHT_POINTS[1:]):
        if curved:
            result.extend(quad(((a, BED, outside_a), (a, TOP, outside_a),
                                (b, TOP, outside_b), (b, BED, outside_b))))
    if straight:
        start = RIGHT_POINTS[0][0]
        result.extend(quad(((start, BED, INNER), (start, TOP, INNER),
                            (56., TOP, INNER), (56., BED, INNER))))
    return result


def cap(east):
    return quad(((east, BED, INNER), (east, TOP, INNER),
                 (east, TOP, OUTER), (east, BED, OUTER)))


def complete():
    return left_top()+left_walls()+right_top()+right_walls()


class SouthParapetSavedFaceTests(unittest.TestCase):

    def test_both_continuous_banks_and_closed_inside_faces_pass(self):
        report = audit_south_parapet_alignment(complete(), CONTRACTS[DIVERGE])
        self.assertEqual(report['south_parapet_top_sections_checked'], 23)
        self.assertEqual(report['south_parapet_inside_wall_sections_checked'], 27)
        self.assertEqual(report['south_parapet_closed_end_faces_checked'], 0)
        self.assertTrue(report['south_parapet_right_perpendicular_cap_absent'])

    def test_old_square_left_end_still_rejects(self):
        old = quad(((-8.0, TOP, INNER),
                    (OLD_LEFT, TOP, INNER),
                    (OLD_LEFT, TOP, OUTER),
                    (-8.0, TOP, OUTER)))
        with self.assertRaisesRegex(ValueError, 'continuous ballast outline'):
            audit_south_parapet_alignment(
                old + left_walls() + right_top() + right_walls(),
                CONTRACTS[DIVERGE],
            )

    def test_previously_accepted_short_right_strip_now_rejects(self):
        with self.assertRaisesRegex(ValueError, 'continuous ballast outline'):
            audit_south_parapet_alignment(
                left_top() + left_walls() + right_top(old=True) + right_walls() + cap(OLD_RIGHT),
                CONTRACTS[DIVERGE],
            )

    def test_shifted_square_cap_cannot_replace_the_curved_right_join(self):
        square = quad(((RIGHT_POINTS[0][0], TOP, INNER),
                       (56.0, TOP, INNER),
                       (56.0, TOP, OUTER),
                       (RIGHT_POINTS[0][0], TOP, OUTER)))
        with self.assertRaisesRegex(ValueError, 'continuous ballast outline'):
            audit_south_parapet_alignment(
                left_top() + left_walls() + square + right_walls(),
                CONTRACTS[DIVERGE],
            )

    def test_right_join_requires_curved_inside_wall(self):
        with self.assertRaisesRegex(ValueError, 'no closed inside face'):
            audit_south_parapet_alignment(
                left_top() + left_walls() + right_top() + right_walls(curved=False),
                CONTRACTS[DIVERGE],
            )

    def test_extended_right_strip_requires_straight_inside_wall(self):
        with self.assertRaisesRegex(ValueError, 'no straight inside face'):
            audit_south_parapet_alignment(
                left_top() + left_walls() + right_top() + right_walls(straight=False),
                CONTRACTS[DIVERGE],
            )

    def test_left_curve_requires_original_inside_wall(self):
        with self.assertRaisesRegex(ValueError, 'no closed inside face'):
            audit_south_parapet_alignment(
                left_top() + left_walls(True) + right_top() + right_walls(),
                CONTRACTS[DIVERGE],
            )

    def test_neither_old_perpendicular_cap_can_interrupt_the_join(self):
        for east in (OLD_LEFT, OLD_RIGHT):
            with self.subTest(east=east), self.assertRaisesRegex(ValueError, 'retains a perpendicular end cap'):
                audit_south_parapet_alignment(complete() + cap(east), CONTRACTS[DIVERGE])

    def test_duplicate_top_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'overlapping concrete tops'):
            audit_south_parapet_alignment(complete() + right_top()[-1:], CONTRACTS[DIVERGE])

    def test_a_roof_across_branch_opening_rejects(self):
        roof = quad(((32.0, TOP, INNER),
                     (40.0, TOP, INNER),
                     (40.0, TOP, OUTER),
                     (32.0, TOP, OUTER)))
        with self.assertRaisesRegex(ValueError, 'continuous ballast outline'):
            audit_south_parapet_alignment(complete() + roof, CONTRACTS[DIVERGE])

    def test_existing_wing_remains_outside_mainline_band_check(self):
        wing = quad(((42.0, TOP, OUTER), (44.0, TOP, OUTER), (44.0, TOP, 7.56), (42.0, TOP, 7.56)))
        self.assertTrue(audit_south_parapet_alignment(complete() + wing, CONTRACTS[DIVERGE])['south_parapet_right_perpendicular_cap_absent'])

    def test_a_low_apron_cannot_replace_raised_right_concrete(self):
        low = [tuple(((p[0], BED, *p[2:]) for p in tri)) for tri in right_top()]
        with self.assertRaisesRegex(ValueError, 'continuous ballast outline'):
            audit_south_parapet_alignment(left_top() + left_walls() + low + right_walls(), CONTRACTS[DIVERGE])

    def test_merge_has_no_diverge_alignment_exception(self):
        self.assertEqual(audit_south_parapet_alignment([], CONTRACTS[MERGE]), {})
        self.assertEqual(CONTRACTS[DIVERGE]['clearance_width_m'], 5.0)


if __name__ == '__main__':
    unittest.main()
