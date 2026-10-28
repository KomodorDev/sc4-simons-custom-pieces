"""Check authoritative reusable-module sources without a native NAM donor.

These regressions prove local traffic-byte preservation, source/manifest
agreement and selected-cell compilation boundaries. Full saved-model and
whole-assembly audits remain separate geometry checks.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json
import math
from pathlib import Path
import unittest
from unittest.mock import patch

from scp.track_paths import encode_paths
from scp_hsr.hsr_partition_components import (
    RECIPES, build_models, model_inputs, partition_info, partition_layout,
)
from scp_hsr.hsr_partition_components_verify import CONTRACTS, MODULE_TILE_FINGERPRINTS
from scp_hsr.hsr_components_verify import CONTRACTS as COMPONENT_CONTRACTS, _contract, check_paths
from scp_hsr.interchange_models import EMPTY_STRUCTURAL_PATH

ROOT = next(path for path in Path(__file__).resolve().parents if (path/'project.json').is_file())


class LiteralComponentSupportMetadataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        domain = ROOT/'domains/high-speed-rail'
        assembly = json.loads((domain/'01_assemblies/straight-stem-trumpet/assembly.json').read_text())
        cls.sources = {}
        for identifier in {row['piece_id'] for row in assembly['placements']}:
            directory = domain/'00_pieces'/identifier
            if (directory/'geometry.json').is_file():
                cls.sources[identifier] = (
                    json.loads((directory/'piece.json').read_text()),
                    json.loads((directory/'geometry.json').read_text())['metadata'])

    def test_all_nine_literal_trumpet_definitions_match_geometry_and_independent_supports(self):
        self.assertEqual(len(self.sources), 9)
        for identifier, (piece, geometry) in self.sources.items():
            with self.subTest(piece=identifier):
                self.assertEqual(piece['component']['support_centers'], geometry['support_centers'])
                contract = _contract(piece)
                self.assertIs(contract, COMPONENT_CONTRACTS[piece['recipe']])

    def test_changed_support_coordinates_are_rejected_for_every_literal_type(self):
        for identifier, (piece, _) in self.sources.items():
            with self.subTest(piece=identifier):
                changed = deepcopy(piece)
                changed['component']['support_centers'][0][0] += 1.
                with self.assertRaisesRegex(ValueError, 'declared supports differ'):
                    check_paths({}, changed)

    def test_obsolete_seven_support_fan_declaration_is_rejected(self):
        piece = json.loads((ROOT/'domains/high-speed-rail/00_pieces'/
                            'hsr-component-l2-paired-fan-compact-join/piece.json').read_text())
        changed = deepcopy(piece)
        changed['component']['support_centers'] = [
            [48., 0.], [48., -16.], [48., -32.], [40., -46.],
            [56., -46.], [32., -64.], [64., -64.]]
        with self.assertRaisesRegex(ValueError, 'declared supports differ'):
            check_paths({}, changed)


class ReusableModuleSourceTests(unittest.TestCase):
    def test_current_partition_geometry_keeps_its_frozen_source_bytes(self):
        expected = {
            'hsr-component-modular-crossing-core': '8a5cfc5a7b58063453447b47d525527dd58a3a46446173ae6c87d6f7e5fd2940',
            'hsr-component-modular-paired-climb': '0ffa98fb47a7040d8cd3ca7d6b1666aaa9e1c56e41515e8ec058569a36236601',
            'hsr-component-modular-south-junction': 'fda2275ea4013c2e9333e3904fc8e5f96de483ce12982c7d45e2fc4d3485ef5e',
        }
        self.assertEqual(set(RECIPES), {slug.replace('-', '_') for slug in expected})
        for slug, digest in expected.items():
            path = ROOT/'domains/high-speed-rail/00_pieces'/slug/'geometry.json'
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), digest)

    def test_every_local_path_matches_its_direct_current_module_fingerprint(self):
        self.assertEqual(set(RECIPES), set(MODULE_TILE_FINGERPRINTS))
        count = 0
        for recipe in RECIPES:
            layout = partition_layout(recipe)
            self.assertEqual(list(layout), CONTRACTS[recipe]['cells'])
            for cell, data in layout.items():
                raw = encode_paths(data['routes']) if data['routes'] else EMPTY_STRUCTURAL_PATH
                self.assertEqual(hashlib.sha256(raw).hexdigest(), MODULE_TILE_FINGERPRINTS[recipe][cell][1],
                                 (recipe, cell))
                count += 1
        self.assertEqual(count, 23)

    def test_local_metadata_matches_current_manifests_without_other_piece_dependencies(self):
        for recipe in RECIPES:
            with self.subTest(recipe=recipe):
                info = partition_info(recipe)
                piece = json.loads((ROOT/'domains/high-speed-rail/00_pieces'/
                                    recipe.replace('_', '-')/'piece.json').read_text())
                self.assertEqual(piece['name'], info['name'])
                self.assertEqual(piece['description'], info['description'])
                self.assertEqual(piece['cells'], [list(cell) for cell in info['cells']])
                self.assertEqual(piece['footprint'], list(info['footprint']))
                self.assertFalse(any('parent' in key for key in info))
                self.assertIsInstance(info['effect_donor'][0], tuple)
                self.assertEqual(len(info['effect_donor'][0]), 3)
                hash(info['effect_donor'][0])
                expected = {(round(x, 9), round(-z, 9))
                            for x, z in CONTRACTS[recipe]['support_centres_xz']}
                self.assertEqual({tuple(round(value, 9) for value in point)
                                  for point in info['support_centers']}, expected)

    def test_surface_context_packs_only_module_cells_and_owns_every_support(self):
        for recipe in RECIPES:
            with self.subTest(recipe=recipe):
                mapping, config = model_inputs(recipe)
                self.assertEqual(set(mapping), set(CONTRACTS[recipe]['cells']))
                self.assertEqual(len(set(mapping.values())), len(mapping))
                emitted = {tuple(cell) for cell, _ in config['layout']}
                self.assertEqual(emitted, set(mapping.values()))
                mask = [tuple(cell) for cell in config['surface_partition_cells']]
                self.assertEqual(len(mask), len(set(mask)))
                self.assertTrue(emitted <= set(mask))
                for x, north in config['support_centers']:
                    self.assertIn((math.floor((x+8.)/16.), math.floor((-north+8.)/16.)), emitted)
                self.assertTrue(config['surface_decks'])
                for deck in config['surface_decks']:
                    self.assertGreaterEqual(len(deck['points']), 2)

    def test_model_dispatch_uses_own_selected_context_and_local_cell_keys(self):
        for recipe in RECIPES:
            mapping, config = model_inputs(recipe)
            encoded = tuple((source, repr(source).encode()) for source in mapping.values())
            expected = {local: repr(source).encode() for local, source in mapping.items()}
            with patch('scp_hsr.hsr_components._cached_models', return_value=encoded) as compiler, \
                 patch('scp_hsr.hsr_symmetric_parapet.repair_models', return_value=expected) as repair, \
                 patch('scp_hsr.hsr_symmetric_stem.repair_stem_models', return_value=expected) as stem_repair:
                result = build_models(b'native donor', recipe)
            self.assertEqual(result, expected)
            self.assertEqual(json.loads(compiler.call_args.args[1]), config)
            if recipe == 'hsr_component_modular_south_junction':
                rule = json.loads((ROOT/'domains/high-speed-rail/00_pieces'/recipe.replace('_', '-')/'geometry.json').read_text())['junction_wedge_alignment']
                repair.assert_called_once_with(b'native donor', expected, mapping, rule)
                stem_rule = json.loads((ROOT/'domains/high-speed-rail/00_pieces'/recipe.replace('_', '-')/'geometry.json').read_text())['stem_parapet_alignment']
                stem_repair.assert_called_once_with(b'native donor', expected, mapping, stem_rule)
            else:
                repair.assert_not_called()
                stem_repair.assert_not_called()


if __name__ == '__main__':
    unittest.main()
