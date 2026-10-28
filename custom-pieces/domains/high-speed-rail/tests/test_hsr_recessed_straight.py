"""Check the separately reusable straight's exact fan-family physical profile."""
from copy import deepcopy
import json
from pathlib import Path
import unittest
from unittest.mock import patch

from scp.autotile import validate_auto_tile_addresses
from scp.track_paths import PATH, encode_paths
from scp_hsr.hsr_compact_fan import build_models, compact_info, compact_layout, model_inputs
from scp_hsr.hsr_compact_fan_verify import check_paths
from scp_hsr.hsr_recessed_straight_verify import (
    MODEL_SHA256, PATH_SHA256, SHADOW_SHA256, audit_retained_straight_paths,
)

ROOT = next(path for path in Path(__file__).resolve().parents if (path/'project.json').is_file())
PIECES = ROOT/'domains/high-speed-rail/00_pieces'
RECIPE = 'hsr_component_l2_paired_straight_recessed_web'
FULL = 'hsr_component_l2_paired_fan_compact_join'


class RecessedStraightTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.directory = PIECES/RECIPE.replace('_', '-')
        cls.spec = json.loads((cls.directory/'piece.json').read_text())
        cls.source = json.loads((cls.directory/'geometry.json').read_text())
        cls.tile = int(cls.spec['tile_ids'][0], 16)
        cls.raw_path = encode_paths(compact_layout(RECIPE)[0, 0]['routes'])
        cls.resources = {(*PATH, cls.tile): cls.raw_path}

    def test_full_original_configuration_is_preserved_but_one_cell_is_emitted(self):
        mapping, config = model_inputs(RECIPE)
        self.assertEqual(config, model_inputs(FULL)[1])
        self.assertEqual(mapping, {(0, 0):(6, 1)})
        self.assertEqual(len(config['layout']), 11)
        self.assertEqual(len(config['support_centers']), 6)
        self.assertEqual(compact_info(RECIPE)['support_centers'], [(0., 0.)])

    def test_exact_original_interior_path_bytes_are_retained(self):
        source = json.loads((PIECES/FULL.replace('_', '-')/'geometry.json').read_text())
        old = next(value for cell, value in source['layout'] if cell == [3, 1])
        self.assertEqual(self.raw_path, encode_paths(old['routes']))
        self.assertEqual(self.source['extraction']['canonical_old_local_cell'], [3, 1])
        self.assertEqual({route['movement'] for route in self.source['layout'][0][1]['routes']},
                         {'N>S', 'S>N'})

    def test_independent_graph_has_only_two_flat_native_directed_journeys(self):
        report = check_paths(self.resources, self.spec)
        self.assertEqual(report['external_ports_checked'], 4)
        self.assertEqual(report['unique_complete_journeys_checked'], 2)
        self.assertEqual(report['maximum_encoded_grade'], 0.)
        self.assertEqual(report['native_port_heights_m'], [15.5])

    def test_changed_path_is_rejected(self):
        changed = {(*PATH, self.tile): self.raw_path+b'changed'}
        with self.assertRaisesRegex(ValueError, 'changed its approved directed local PATHs'):
            audit_retained_straight_paths(changed, self.spec)

    def test_missing_tile_identity_cannot_pass_a_partial_audit(self):
        changed = deepcopy(self.spec)
        changed['tile_ids'] = []
        with self.assertRaisesRegex(ValueError, 'exact one-cell piece'):
            audit_retained_straight_paths(self.resources, changed)

    def test_full_context_cannot_leak_other_ten_cells_or_five_supports(self):
        _, config = model_inputs(RECIPE)
        complete = tuple((tuple(cell), repr(cell).encode()) for cell, _ in config['layout'])
        with patch('scp_hsr.hsr_compact_fan._cached_fan_models', return_value=complete):
            actual = build_models(b'controlled native input', RECIPE)
        self.assertEqual(actual, {(0, 0): b'[6, 1]'})

    def test_pins_identify_the_independent_approved_interior_model_and_shadows(self):
        report = json.loads((PIECES/FULL.replace('_', '-')/'evidence/saved-resource-checks.json').read_text())
        actual = report['actual_saved_resource_fingerprints']
        for zoom in range(5):
            model_key = f'model:{FULL.replace("_", "-")}:5ad0e817-badb57f1-{0x7f580310+zoom:08x}'
            shadow_key = f'shadow:{FULL.replace("_", "-")}:7ab50e44-2bc2759a-{0x7f580310+zoom:08x}'
            self.assertEqual(actual[model_key], MODEL_SHA256)
            self.assertEqual(actual[shadow_key], SHADOW_SHA256[zoom])
        self.assertEqual(audit_retained_straight_paths(self.resources, self.spec),
                         {'exact_recessed_web_path_cells_checked': 1})

    def test_profile_variant_has_its_own_safe_allocation_and_rotation_policy(self):
        validate_auto_tile_addresses(self.spec)
        self.assertEqual(self.spec['puzzle_id'], 'f829')
        self.assertEqual(self.spec['tile_ids'], ['7f586000'])
        self.assertEqual(self.spec['orientation_policy'], 'rotate-only-preserve-direction')
        self.assertEqual(self.spec['orientation_count'], 8)
        self.assertEqual(self.spec['component']['support_centers'], [[0., 0.]])


if __name__ == '__main__':
    unittest.main()
