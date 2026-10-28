"""Reject disappearing opposed-merge borders and missing raised faces."""
from __future__ import annotations

from collections import defaultdict
import hashlib
import json
import math
from pathlib import Path
import unittest

from scp_hsr.hsr_opposed_parapet_verify import (
    audit_opposed_parapet_alignment, BED, CONTINUOUS_SECTIONS,
    INNER, NORTH_CAP, OUTER, OUTER_JOIN_POINTS, SOUTH_CAP, TOP,
)


def quad(points):
    vertices = [(*point, .18, 0.) for point in points]
    return [(vertices[0], vertices[1], vertices[2]), (vertices[0], vertices[2], vertices[3])]


def accepted_bank(side):
    sections = [(-8., INNER, OUTER), *CONTINUOUS_SECTIONS, (30.212506, 8., 8.)]
    transform = (lambda x: x) if side < 0. else (lambda x: 48.-x)
    top, wall = [], []
    for (a, ai, ao), (b, bi, bo) in zip(sections, sections[1:]):
        a, b = transform(a), transform(b)
        top.extend(quad(((a, TOP, side*ai), (b, TOP, side*bi),
                         (b, TOP, side*bo), (a, TOP, side*ao))))
        wall.extend(quad(((a, BED, side*ai), (a, TOP, side*ai),
                          (b, TOP, side*bi), (b, BED, side*bi))))
    return top, wall


def old_cap(side):
    cap = NORTH_CAP if side < 0. else SOUTH_CAP
    return quad(((cap, BED, side*INNER), (cap, BED, side*OUTER),
                 (cap, TOP, side*OUTER), (cap, TOP, side*INNER)))


def outer_top(side, old=False):
    end = 56. if side < 0. else -8.
    if old:
        cap = NORTH_CAP if side < 0. else SOUTH_CAP
        return quad(((cap, TOP, side*INNER), (end, TOP, side*INNER),
                     (end, TOP, side*OUTER), (cap, TOP, side*OUTER)))
    curve = OUTER_JOIN_POINTS['north' if side < 0. else 'south']
    points = [*curve, (end, OUTER)]
    result = []
    for (a, outside_a), (b, outside_b) in zip(points, points[1:]):
        result.extend(quad(((a, TOP, side*INNER), (b, TOP, side*INNER),
                            (b, TOP, side*outside_b), (a, TOP, side*outside_a))))
    return result


def outer_walls(side, curved=True, straight=True):
    curve = OUTER_JOIN_POINTS['north' if side < 0. else 'south']
    result = []
    if curved:
        for (a, outside_a), (b, outside_b) in zip(curve, curve[1:]):
            result.extend(quad(((a, BED, side*outside_a), (a, TOP, side*outside_a),
                                (b, TOP, side*outside_b), (b, BED, side*outside_b))))
    if straight:
        start, end = curve[0][0], 56. if side < 0. else -8.
        result.extend(quad(((start, BED, side*INNER), (start, TOP, side*INNER),
                            (end, TOP, side*INNER), (end, BED, side*INNER))))
    return result


def border(side):
    top, wall = accepted_bank(side)
    return top+outer_top(side), wall+outer_walls(side)


def complete():
    return [tri for side in (-1., 1.) for group in border(side) for tri in group]


class OpposedParapetSavedFaceTests(unittest.TestCase):
    def test_all_four_continuous_raised_banks_pass(self):
        result = audit_opposed_parapet_alignment(complete())
        self.assertEqual(result['opposed_parapet_top_sections_checked'], 55)
        self.assertEqual(result['opposed_parapet_inside_wall_sections_checked'], 72)
        self.assertEqual(result['opposed_parapet_closed_end_faces_checked'], 0)
        self.assertTrue(result['opposed_parapet_outer_perpendicular_caps_absent'])
        self.assertEqual(sum(len(j['curved_wall_facets'])
                             for j in result['opposed_parapet_outer_joins']), 27)

    def test_either_missing_continuous_top_is_rejected(self):
        for side in (-1., 1.):
            with self.subTest(side=side):
                triangles = [tri for group in border(-side) for tri in group]
                triangles += border(side)[1]
                with self.assertRaisesRegex(ValueError, 'continuous ballast outline'):
                    audit_opposed_parapet_alignment(triangles)

    def test_either_missing_inside_wall_is_rejected(self):
        for side in (-1., 1.):
            with self.subTest(side=side):
                triangles = [tri for group in border(-side) for tri in group]
                triangles += border(side)[0]
                with self.assertRaisesRegex(ValueError, 'no closed inside face'):
                    audit_opposed_parapet_alignment(triangles)

    def test_either_previously_short_outer_strip_is_rejected(self):
        for side in (-1., 1.):
            with self.subTest(side=side):
                triangles = [tri for group in border(-side) for tri in group]
                top, wall = accepted_bank(side)
                with self.assertRaisesRegex(ValueError, 'continuous ballast outline'):
                    audit_opposed_parapet_alignment(
                        triangles+top+wall+outer_top(side, old=True)+old_cap(side))

    def test_either_outer_join_requires_its_curved_inside_wall(self):
        for side in (-1., 1.):
            with self.subTest(side=side):
                triangles = [tri for group in border(-side) for tri in group]
                top, wall = accepted_bank(side)
                with self.assertRaisesRegex(ValueError, 'no closed inside face'):
                    audit_opposed_parapet_alignment(
                        triangles+top+wall+outer_top(side)+outer_walls(side, curved=False))

    def test_a_half_missing_between_wall_stations_is_rejected(self):
        side = -1.
        triangles = [tri for group in border(1.) for tri in group]
        top, wall = accepted_bank(side)
        curve = outer_walls(side, straight=False)
        curve.pop(4)
        with self.assertRaisesRegex(ValueError, 'incomplete vertical coverage'):
            audit_opposed_parapet_alignment(
                triangles+top+wall+outer_top(side)+curve+outer_walls(side, curved=False))

    def test_duplicate_curved_inside_wall_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'duplicate coplanar faces'):
            audit_opposed_parapet_alignment(complete()+outer_walls(-1., straight=False)[:1])

    def test_neither_old_perpendicular_cap_can_interrupt_its_join(self):
        for side in (-1., 1.):
            with self.subTest(side=side), self.assertRaisesRegex(ValueError, 'retains a perpendicular end cap'):
                audit_opposed_parapet_alignment(complete()+old_cap(side))

    def test_concrete_roof_in_either_opening_is_rejected(self):
        for side in (-1., 1.):
            a, b = (32., 40.) if side < 0. else (8., 16.)
            roof = quad(((a, TOP, side*INNER), (b, TOP, side*INNER),
                         (b, TOP, side*OUTER), (a, TOP, side*OUTER)))
            with self.subTest(side=side), self.assertRaisesRegex(ValueError, 'continuous ballast outline'):
                audit_opposed_parapet_alignment(complete()+roof)

    def test_duplicate_top_surface_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'overlapping concrete tops'):
            audit_opposed_parapet_alignment(complete()+outer_top(-1.)[:1])

    def test_low_apron_cannot_replace_raised_top(self):
        triangles = [tuple((v[0], BED if abs(v[1]-TOP) < 1e-6 else v[1], *v[2:])
                           for v in tri) for tri in complete()]
        with self.assertRaisesRegex(ValueError, 'continuous ballast outline'):
            audit_opposed_parapet_alignment(triangles)

    def test_existing_five_metre_train_corridor_accepts_the_reviewed_margin(self):
        self.assertEqual(self._check_train_corridor(2.6), 1)

    def test_wall_between_route_samples_cannot_enter_the_train_corridor(self):
        with self.assertRaisesRegex(ValueError, 'train-clearance envelope'):
            self._check_train_corridor(2.49)

    @staticmethod
    def _check_train_corridor(south):
        from scp_hsr.interchange_verify import _clearance_segments
        triangles = quad(((5., BED, south), (5., TOP, south),
                          (6., TOP, south), (6., BED, south)))
        buckets = defaultdict(list)
        for triangle in triangles:
            for x in range(math.floor(min(p[0] for p in triangle)/4.),
                           math.floor(max(p[0] for p in triangle)/4.)+1):
                for z in range(math.floor(min(p[2] for p in triangle)/4.),
                               math.floor(max(p[2] for p in triangle)/4.)+1):
                    buckets[x, z].append(triangle)
        return _clearance_segments([((0, 0), {}, [(0., 0., 15.5), (10., 0., 15.5)])],
                                   buckets, half_width=2.5)

    @staticmethod
    def _collar_fixture():
        from scp_hsr.single_track_models import _native, _pack
        from scp_hsr.test_support import donor
        native = donor()
        source = _native(native)
        bed, top = source['bed_y'], source['top']
        faces = quad(((-8., top, -INNER), (-5.5, top, -INNER),
                      (-5.5, top, -OUTER), (-8., top, -OUTER)))
        faces += quad(((-8., bed, -5.), (-5.5, bed, -5.),
                       (-5.5, bed, -OUTER), (-8., bed, -OUTER)))
        faces += quad(((-8., bed, -INNER), (-8., top, -INNER),
                       (-5.5, top, -INNER), (-5.5, bed, -INNER)))
        raw = _pack(source, faces)
        piece = Path(__file__).resolve().parents[1]/'00_pieces/hsr-component-l2-short-opposed-merge-core'
        collar = json.loads((piece/'geometry.json').read_text())['west_straight_extraction']['native_west_parapet_collar']
        collar['baseline_cell_model_sha256'] = hashlib.sha256(raw).hexdigest()
        return native, raw, collar, bed, top

    def test_already_native_west_border_is_not_warped_twice(self):
        from scp_hsr.hsr_atomic_junctions import normalize_west_parapet
        from scp_hsr.hsr_atomic_components_verify import _section_intervals
        from scp_hsr.test_support import triangles
        native, raw, collar, _, top = self._collar_fixture()
        corrected = normalize_west_parapet(raw, native,
                                          {**collar, 'preserve_native_upper_concrete': True})
        intervals = _section_intervals(triangles(corrected), 'east', -7.99999925, top, 0.)
        self.assertEqual(len(intervals), 1)
        self.assertAlmostEqual(intervals[0][0], INNER, places=5)
        doubled = normalize_west_parapet(raw, native, collar)
        old = _section_intervals(triangles(doubled), 'east', -7.99999925, top, 0.)
        self.assertLess(old[0][0], INNER-.003)

    def test_original_west_ballast_floor_warp_is_preserved_exactly(self):
        from scp_hsr.hsr_atomic_junctions import normalize_west_parapet
        from scp_hsr.test_support import triangles
        native, raw, collar, bed, _ = self._collar_fixture()
        original = normalize_west_parapet(raw, native, collar)
        corrected = normalize_west_parapet(raw, native,
                                          {**collar, 'preserve_native_upper_concrete': True})
        def floor_values(model):
            return sorted(tri for tri in triangles(model) if all(abs(p[1]-bed) < 1e-5 for p in tri))
        self.assertEqual(floor_values(original), floor_values(corrected))
        self.assertNotEqual(floor_values(raw), floor_values(corrected))

    def test_native_upper_exception_still_requires_exact_raw_model_hash(self):
        from scp_hsr.hsr_atomic_junctions import normalize_west_parapet
        native, raw, collar, _, _ = self._collar_fixture()
        with self.assertRaisesRegex(ValueError, 'exact reviewed retained model'):
            normalize_west_parapet(raw, native,
                                  {**collar, 'preserve_native_upper_concrete': True,
                                   'baseline_cell_model_sha256': '0'*64})

    def test_original_authored_source_values_are_preserved(self):
        piece = Path(__file__).resolve().parents[1]/'00_pieces/hsr-component-l2-short-opposed-merge-core'
        original = json.loads((piece/'evidence/design-history/before-ballast-border-repair/geometry.json').read_text())
        revised = json.loads((piece/'geometry.json').read_text())
        revised.pop('opposed_parapet_alignment')
        self.assertEqual(revised, original)


if __name__ == '__main__':
    unittest.main()
