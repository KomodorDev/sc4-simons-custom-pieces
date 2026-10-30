"""Keep the accepted outer ramp geometry during shoulder-only revisions."""
import hashlib
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT/'framework'), str(ROOT/'domains/highway/implementation')]

from scp_highway.ramp_geometry import compact_ramps, highway_coordinates


class ShoulderRevisionPreservationTests(unittest.TestCase):
    def test_outer_curves_and_every_graded_sample_match_the_accepted_revision(self):
        # Measured from source commit be7efce before the shoulder revision.
        # Hashes cover all 279 samples outside the native 8 m half-deck,
        # including the complete height transitions and ground landings.
        expected = {
            'lower-off': 'aa702383626d49ad837dbb2f13acdb23292f05d87c441251102e85508e6ef5e5',
            'lower-on': '3103d3e1005795fb9ec34923618f10ffc2e89fe4372787fb499478bd19437a9a',
            'upper-off': '224214dd438eb5cdc69fb3050f97a34a78087818c9cec527bec773a7a5c615d2',
            'upper-on': '1d1fb4235def89c2fcc47382493d79cdae1c27adb1765c93f94050e2364940ea',
        }
        ramps = compact_ramps()
        self.assertEqual({ramp['id'] for ramp in ramps}, set(expected))
        for ramp in ramps:
            with self.subTest(ramp=ramp['id']):
                points = [[round(value, 7) for value in point] for point in ramp['points']
                          if abs(highway_coordinates(point)[1]) >= 8.]
                self.assertEqual(len(points), 279)
                digest = hashlib.sha256(json.dumps(points, separators=(',', ':')).encode()).hexdigest()
                self.assertEqual(digest, expected[ramp['id']],
                                 'A shoulder-only change moved the accepted outer ramp or grade')


if __name__ == '__main__':
    unittest.main()
