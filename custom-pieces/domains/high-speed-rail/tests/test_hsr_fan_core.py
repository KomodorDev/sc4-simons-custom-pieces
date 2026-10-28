"""Check exact fan-core extraction, independent routes, and emission bounds."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import unittest
from unittest.mock import patch

from scp.autotile import validate_auto_tile_addresses
from scp.track_paths import PATH, encode_paths
from scp_hsr.hsr_compact_fan import (
    build_models, compact_info, compact_layout, model_inputs,
)
from scp_hsr.hsr_compact_fan_verify import check_paths
from scp_hsr.hsr_fan_core_verify import PINS, audit_retained_core_paths
from scp_hsr.interchange_models import EMPTY_STRUCTURAL_PATH

ROOT = next(path for path in Path(__file__).resolve().parents if (path/'project.json').is_file())
PIECES = ROOT/'domains/high-speed-rail/00_pieces'
CORE = 'hsr_component_l2_paired_fan_compact_core'
FULL = 'hsr_component_l2_paired_fan_compact_join'


class FanCoreExtractionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.directory = PIECES/CORE.replace('_', '-')
        cls.spec = json.loads((cls.directory/'piece.json').read_text())
        cls.source = json.loads((cls.directory/'geometry.json').read_text())
        cls.full_source = json.loads((PIECES/FULL.replace('_', '-')/'geometry.json').read_text())
        cls.paths = {
            (*PATH, int(tile, 16)): encode_paths(data['routes']) if data['routes'] else EMPTY_STRUCTURAL_PATH
            for (_, data), tile in zip(compact_layout(CORE).items(), cls.spec['tile_ids'])
        }

    def test_original_full_fan_source_and_identity_are_unchanged(self):
        directory = PIECES/FULL.replace('_', '-')
        self.assertEqual(hashlib.sha256((directory/'geometry.json').read_bytes()).hexdigest(),
                         'd5366120c1f9c38b8b1eccc7fc8927dabb6e28d8ba1dd08427ed4e0b1c74aa0b')
        self.assertEqual(len(compact_info(FULL)['cells']), 11)
        self.assertEqual(len(compact_info(FULL)['support_centers']), 6)

    def test_complete_computation_signature_is_exactly_the_approved_full_fan(self):
        full_mapping, full_configuration = model_inputs(FULL)
        mapping, configuration = model_inputs(CORE)
        self.assertEqual(configuration, full_configuration)
        self.assertEqual(len(configuration['layout']), 11)
        self.assertEqual(len(configuration['support_centers']), 6)
        self.assertEqual(len(mapping), 9)
        self.assertEqual(set(mapping.values()), set(full_mapping.values())-{(6, 0), (6, 1)})

    def test_nine_retained_local_fragments_have_no_resampling_or_reshaping(self):
        old = {tuple(cell): value for cell, value in self.full_source['layout']}
        self.assertEqual(len(self.source['layout']), 9)
        for cell, value in self.source['layout']:
            self.assertEqual(value, old[cell[0]+1, cell[1]+2])
        self.assertEqual(self.source['central_parapet_alignment'],
                         self.full_source['central_parapet_alignment'])

    def test_only_four_original_supports_are_owned(self):
        self.assertEqual(compact_info(CORE)['support_centers'],
                         [(32., 0.), (32., -16.), (16., -32.), (48., -32.)])
        self.assertEqual(self.spec['component']['support_centers'],
                         self.source['metadata']['support_centers'])

    def test_model_dispatch_filters_the_full_context_to_nine_outputs(self):
        mapping, configuration = model_inputs(CORE)
        complete = tuple((tuple(cell), repr(cell).encode()) for cell, _ in configuration['layout'])
        with patch('scp_hsr.hsr_compact_fan._cached_fan_models', return_value=complete) as compiler:
            emitted = build_models(b'controlled native input', CORE)
        self.assertEqual(set(emitted), set(PINS))
        self.assertEqual(len(emitted), 9)
        self.assertEqual(json.loads(compiler.call_args.args[1]), configuration)
        self.assertEqual(emitted, {local: repr(list(source)).encode() for local, source in mapping.items()})

    def test_incomplete_full_computation_context_is_rejected(self):
        changed = deepcopy(self.source)
        changed['surface_context']['compilation_cells'].pop()
        with patch('scp_hsr.hsr_compact_fan._source', return_value=changed):
            with self.assertRaisesRegex(ValueError, 'eleven-cell computation context'):
                model_inputs(CORE)

    def test_duplicate_computation_cell_is_rejected(self):
        changed = deepcopy(self.source)
        cells = changed['surface_context']['compilation_cells']
        cells[-1] = cells[0]
        with patch('scp_hsr.hsr_compact_fan._source', return_value=changed):
            with self.assertRaisesRegex(ValueError, 'eleven-cell computation context'):
                model_inputs(CORE)

    def test_full_context_opt_in_cannot_change_the_existing_full_fan(self):
        with patch('scp_hsr.hsr_compact_fan._source', return_value=self.source):
            with self.assertRaisesRegex(ValueError, 'Only the extracted fan pieces'):
                model_inputs(FULL)

    def test_curved_first_core_cell_was_not_extracted_as_a_straight(self):
        first = compact_layout(CORE)[2, 0]
        self.assertGreater(max(abs(abs(point[0])-2.) for route in first['routes']
                               for point in route['points']), .28)
        self.assertNotIn((2, -1), compact_layout(CORE))
        self.assertNotIn((2, -2), compact_layout(CORE))

    def test_exact_retained_path_pins_pass_and_literal_graph_has_two_journeys(self):
        report = audit_retained_core_paths(self.paths, self.spec)
        self.assertEqual(report['exact_retained_path_cells_checked'], 9)
        geometry = check_paths(self.paths, self.spec)
        self.assertEqual(geometry['tile_count'], 9)
        self.assertEqual(geometry['unique_complete_journeys_checked'], 2)

    def test_changed_saved_path_is_rejected(self):
        changed = dict(self.paths)
        key = next(iter(changed))
        changed[key] += b'changed'
        with self.assertRaisesRegex(ValueError, 'changed an approved retained PATH'):
            audit_retained_core_paths(changed, self.spec)

    def test_incomplete_tile_list_cannot_pass_a_partial_pin_audit(self):
        changed = deepcopy(self.spec)
        changed['tile_ids'].pop()
        with self.assertRaisesRegex(ValueError, 'tile list is incomplete'):
            audit_retained_core_paths(self.paths, changed)

    def test_pins_match_the_frozen_actual_saved_full_fan_report(self):
        report = json.loads((PIECES/FULL.replace('_', '-')/'evidence/saved-resource-checks.json').read_text())
        actual = report['actual_saved_resource_fingerprints']
        for cell, pin in PINS.items():
            x, row = pin['old_cell']
            base = 0x7f580000+0x100*x+0x10*row
            for zoom in range(5):
                identity = f'5ad0e817-badb57f1-{base+zoom:08x}'
                self.assertEqual(actual[f'model:{FULL.replace("_", "-")}:{identity}'], pin['model_sha256'])
                identity = f'7ab50e44-2bc2759a-{base+zoom:08x}'
                self.assertEqual(actual[f'shadow:{FULL.replace("_", "-")}:{identity}'], pin['shadow_sha256'][zoom])

    def test_sparse_new_allocation_has_unique_native_addresses(self):
        validate_auto_tile_addresses(self.spec)
        ledger = json.loads((ROOT/'config/allocations.json').read_text())['pieces'][CORE.replace('_', '-')]
        self.assertEqual(ledger['cells'], self.spec['cells'])
        self.assertEqual(ledger['tile_ids'], self.spec['tile_ids'])
        self.assertEqual(ledger['tile_base'], '7f505000')
        self.assertEqual(self.spec['puzzle_id'], 'f7a8')
        self.assertNotIn([0, 0], self.spec['cells'])

    def test_new_core_menu_identifies_a_junction_component(self):
        from scp_hsr.icons import icon_identity
        identity = icon_identity(CORE.replace('_', '-'))
        self.assertEqual(identity['kind'], 'JCT')
        self.assertEqual(identity['badge'], 'PART')


if __name__ == '__main__':
    unittest.main()
