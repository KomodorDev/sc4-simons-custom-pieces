"""Reopen saved barrier models, then delete or reverse actual joint faces."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp.dbpf import pack_dbpf
from scp.models import pack_s3d, parse_s3d, positions
from scp.verify import strict_dbpf
from scp_highway import barrier_mouth_verify as check
from scp_highway import ramp_geometry as fixture_writer


def mutate_support(raw, section, *, reverse=False):
    """Remove indexed faces intersecting one independent missing-region ray."""
    model = parse_s3d(raw); changed = 0
    for mesh in model['meshes']:
        vi, ii, pi, _mi = mesh['frames'][0]
        vertices = positions(model['vertices'][vi]); indices = model['indices'][ii]['values']
        result = []
        for kind, start, count in model['primitives'][pi]:
            if kind != 0:
                raise AssertionError('Fixture must contain indexed triangle lists')
            for offset in range(start, start + count, 3):
                ids = indices[offset:offset + 3]
                points = [(vertices[index][0] + 64., -vertices[index][2] - 64., vertices[index][1])
                          for index in ids]
                interval = check._interval(section['first'], section['last'], check._face(points),
                                           section['outward_normal'])
                if interval and interval[1] - interval[0] > 1e-6:
                    changed += 1
                    if reverse:
                        result.extend(reversed(ids))
                else:
                    result.extend(ids)
        model['indices'][ii]['values'] = tuple(result)
        model['primitives'][pi] = [(0, 0, len(result))]
    if not changed:
        raise AssertionError('Mutation did not intersect an actual saved bridge face')
    return pack_s3d(model), changed


class SavedBarrierMouthTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # The fixture author is separate from the verifier. Expected sections
        # use an analytic cubic and literal profile, never these sweep helpers.
        cls.resources, cls.owners = {}, {}
        for index, ramp in enumerate(fixture_writer.compact_ramps()):
            tile = 0x7f700000 + index * 0x100
            raw = fixture_writer.pack_road_model(fixture_writer.compact_ramp_triangles(ramp), 0x5EB4BEE9)
            cls.resources[ramp['id']] = strict_dbpf(pack_dbpf({(*check.S3D, tile + 4): raw}))
            cls.owners[index, 0] = {'piece_id': ramp['id'], 'tile': tile, 'local_cell': (0, 0),
                                    'angle': 0, 'origin': (64., -64.)}

    def test_all_four_saved_mouths_cover_both_profiles_in_every_rotation(self):
        report = check.check_saved_barrier_mouths(self.owners, self.resources)
        self.assertTrue(report['passed'])
        self.assertEqual(report['ramp_mouths_checked'], 4)
        self.assertEqual(report['barriers_per_mouth'], 2)
        self.assertEqual(report['proper_rotations_checked'], 4)
        self.assertEqual(report['continuous_profile_sections_checked'], 640)
        self.assertTrue(report['outward_winding_checked'])
        self.assertFalse(report['game_rendering_tested'])

    def test_inner_triangle_cannot_disappear_at_any_saved_mouth(self):
        self._reject_each_missing_strip(barrier_side=-1, band=4)

    def test_outer_crown_cannot_disappear_at_any_saved_mouth(self):
        self._reject_each_missing_strip(barrier_side=1, band=2)

    def test_outer_side_cannot_disappear_at_any_saved_mouth(self):
        self._reject_each_missing_strip(barrier_side=1, band=0)

    def _reject_each_missing_strip(self, *, barrier_side, band):
        for ramp in self.resources:
            with self.subTest(ramp=ramp, barrier_side=barrier_side, band=band):
                section = next(row for row in check.section_contracts() if row['ramp_id'] == ramp
                               and row['barrier_side'] == barrier_side and row['profile_band'] == band)
                resources = deepcopy(self.resources)
                key = next(iter(resources[ramp]))
                resources[ramp][key], changed = mutate_support(resources[ramp][key], section)
                self.assertGreater(changed, 0)
                resources[ramp] = strict_dbpf(pack_dbpf(resources[ramp]))
                with self.assertRaisesRegex(ValueError, 'open or inward-facing profile strip'):
                    check.check_saved_barrier_mouths(self.owners, resources)

    def test_present_but_reversed_crown_faces_are_rejected(self):
        ramp = 'upper-off'
        section = next(row for row in check.section_contracts() if row['ramp_id'] == ramp
                       and row['barrier_side'] == 1 and row['profile_band'] == 2)
        resources = deepcopy(self.resources); key = next(iter(resources[ramp]))
        resources[ramp][key], _changed = mutate_support(resources[ramp][key], section, reverse=True)
        resources[ramp] = strict_dbpf(pack_dbpf(resources[ramp]))
        with self.assertRaisesRegex(ValueError, 'inward-facing'):
            check.check_saved_barrier_mouths(self.owners, resources)

    def test_no_barrier_faces_cannot_pass(self):
        with self.assertRaisesRegex(ValueError, 'open or inward-facing'):
            check.check_faces([])

    def test_reference_crown_anchors_are_independent_measured_values(self):
        # Continuous reference measurements differ from the retained 401-node
        # sweep by at most 0.33 mm. The explicit 3 mm guard does not hide the
        # former 0.5–2 m missing spans.
        cases = ((63.80184694319789, 1, 12.451671, 13.173514),
                 (63.80184694319789, -1, 25.680298, 25.164865),
                 (97.74297244015216, 1, 19.556721, 20.637803),
                 (97.74297244015216, -1, 38.629258, 37.907164))
        for length, side, old, miter in cases:
            self.assertAlmostEqual(check._anchor(length, side, .265625, 3.), old, places=6)
            self.assertAlmostEqual(check._anchor(length, side, .265625, 3. - .265625), miter, places=6)


if __name__ == '__main__':
    unittest.main()
