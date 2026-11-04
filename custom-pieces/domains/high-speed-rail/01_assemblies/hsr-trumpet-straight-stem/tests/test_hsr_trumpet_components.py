"""Exact trumpet component membership, placements, and fan joins."""
import json
import math
from pathlib import Path
import unittest

from scp.subject_sources import piece_id_for_recipe
from scp_hsr.hsr_atomic_junctions import atomic_info
from scp_hsr.hsr_compact_fan import compact_info


ROOT = next(path for path in Path(__file__).resolve().parents if (path/'project.jsonc').is_file())
ASSEMBLY = Path(__file__).resolve().parents[1]
CORE = 'hsr_component_l2_paired_fan_compact_core'
DIVERGE = 'hsr_component_l2_short_mainline_diverge_core'
MERGE = 'hsr_component_l2_short_opposed_merge_core'


class TrumpetComponentPlacementTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scene = json.loads((ASSEMBLY/'assembly.json').read_text())

    def test_literal_geometry_members_are_the_nine_reviewed_reusable_types(self):
        pieces = ROOT/'domains/high-speed-rail/00_pieces'
        actual = {row['piece_id'] for row in self.scene['placements']
                  if (pieces/row['piece_id']/'geometry.json').is_file()}
        self.assertEqual(actual, {
            'hsr-l2-and-l4-two-track-ramp',
            'hsr-l2-mixed-fan-compact-recessed-web',
            'hsr-l2-single-track-oneway-curve-oblique-entry',
            'hsr-l2-single-track-oneway-curve-oblique-exit',
            'hsr-l2-two-track-mainline-opposed-merges-oblique-cuts',
            'hsr-l2-two-track-mainline-split-merge-parallel-recessed-end',
            'hsr-l2-two-track-mainline-split-oblique-cut',
            'hsr-l2-two-track-straight-recessed-web',
            'hsr-l4-over-hsr-l2-two-track-crossing-90deg',
        })

    def test_fan_joins_and_extracted_straight_keep_the_approved_placements(self):
        copies = [row for row in self.scene['placements']
                  if row['piece_id'] == piece_id_for_recipe(DIVERGE, ROOT)]
        self.assertEqual([(row['origin_m'], row['rotation_degrees_ccw']) for row in copies],
                         [([-96., 0.], 0), ([176., 0.], 180)])
        by_label = {row['label']: row for row in self.scene['placements']}
        self.assertEqual((by_label['P06']['piece_id'], by_label['P06']['origin_m'],
                          by_label['P06']['rotation_degrees_ccw']),
                         (piece_id_for_recipe(CORE, ROOT), [80., 48.], 0))
        # P26 owns the extracted western approach, so P07's local origin
        # moves east by one tile while this fan connection stays fixed.
        self.assertEqual((by_label['P07']['piece_id'], by_label['P07']['origin_m'],
                          by_label['P07']['rotation_degrees_ccw']),
                         (piece_id_for_recipe(MERGE, ROOT), [48., 0.], 0))
        self.assertEqual((by_label['P26']['piece_id'], by_label['P26']['origin_m'],
                          by_label['P26']['rotation_degrees_ccw']),
                         ('hsr-l2-two-track-straight', [32., 0.], 270))
        self.assertFalse(any(row['piece_id'] == 'hsr-component-l2-compact-fan-diverge'
                             for row in self.scene['placements']))
        info = compact_info(CORE)
        diverge, merge = atomic_info(DIVERGE), atomic_info(MERGE)
        sx, sy, sh = diverge['ports']['S']['out']
        fan_east_world = tuple(value+offset for value, offset in
                               zip(info['ports']['E']['in'], (*by_label['P06']['origin_m'], 0.)))
        self.assertLess(math.dist(fan_east_world, (176.-sx, -sy, sh)), 1e-9)
        fan_west_world = tuple(value+offset for value, offset in
                               zip(info['ports']['W']['out'], (*by_label['P06']['origin_m'], 0.)))
        merge_world = tuple(value+offset for value, offset in
                            zip(merge['ports']['N']['in'], (*by_label['P07']['origin_m'], 0.)))
        self.assertLess(math.dist(fan_west_world, merge_world), 1e-9)


if __name__ == '__main__':
    unittest.main()
