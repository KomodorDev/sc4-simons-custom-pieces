"""Keep the adjacent B phase isolated through shared dispatch and extraction."""
from copy import deepcopy
import importlib.util
import math
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp import jsonc
from scp.connectivity import assembly_connectivity, piece_connectivity
from scp_highway import adaptive_ground, connections, icons, recipes, verify
from scp_highway import parallel_alignment_b_verify as b
from scp_highway import parallel_verify as a
from scp_highway import parallel_b_connector_contracts as contracts
from test_parallel_alignment_b_verify import fixture


def piece(identifier):
    return jsonc.load(ROOT / 'domains/highway/00_pieces' / identifier / 'piece.jsonc')


def tool(name):
    spec = importlib.util.spec_from_file_location('_integration_' + name,
        ROOT / 'domains/highway/tools' / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def tiny_grade_seam(*, discontinuity=False, precise_contract=False):
    """Literal actual B seam, isolated from all highway route generators."""
    from scp.track_paths import PATH
    definitions = [
        ('left', '5ff10000', 0, 2, [(-8., -7.9, 16.),
            (7.861678590, -1.108884159, 13.308317297), (8., -.970562748, 13.253147845)]),
        ('right', '5ff20000', 0, 1, [(-8., -.970562748, 13.253147845),
            (-7.996935385, -.967498134, 13.251925525 - (.00001 if discontinuity else 0.)),
            (.970562748, 8., 10.)])]
    pieces, records = {}, {}
    for name, tile, entry, exit_, points in definitions:
        spec = {'id': name, 'domain': 'highway', 'recipe': 'precision-test',
                'footprint': [1, 1], 'cells': [[0, 0]], 'tile_ids': [tile]}
        lines = ['SC4PATHS', '1.2', '1', '0', '0', '1', '0', str(entry), str(exit_), '0', str(len(points))]
        lines.extend(','.join(format(value, '.9f') for value in point) for point in points)
        raw = ('\r\n'.join(lines) + '\r\n').encode('ascii')
        contract = {'boundary_measurement_precision': 'saved-path'} if precise_contract else None
        pieces[name] = spec
        records[name] = piece_connectivity(spec, {(*PATH, int(tile, 16)): raw}, contract=contract,
                                          service_classifier=connections.service_classifier)
    scene = {'placements': [{'piece_id': 'left', 'origin_m': [0., 0.]},
                            {'piece_id': 'right', 'origin_m': [16., 0.]}]}
    return scene, pieces, records


class ParallelBIntegrationTests(unittest.TestCase):
    def test_path_model_and_construction_dispatch_b_before_the_generic_a_prefix(self):
        resources, fields, donors = {'saved': 'resources'}, {'saved': 'construction'}, {'native': 'donors'}
        for key in ('check_paths', 'check_models', 'check_construction_fields'):
            selected = getattr(verify, key)
            for recipe, target, other in (('highway_ddrhw_parallel_b_crossing', b, a),
                                           ('highway_ddrhw_parallel_crossing', a, b)):
                spec = {'recipe': recipe}
                args = ((resources, spec) if key == 'check_paths' else
                        (resources, spec, donors) if key == 'check_models' else (fields, spec, resources))
                with self.subTest(function=key, recipe=recipe), \
                     patch.object(target, key, return_value='selected') as chosen, \
                     patch.object(other, key, side_effect=AssertionError('Wrong alignment verifier')):
                    self.assertEqual(selected(*args), 'selected')
                    chosen.assert_called_once_with(*args)

    def test_builder_dispatch_retains_a_and_routes_b_to_its_own_compiler(self):
        from scp_highway import parallel_b_modules, parallel_modules
        for recipe, target, other in (('highway_ddrhw_parallel_b_crossing', parallel_b_modules, parallel_modules),
                                       ('highway_ddrhw_parallel_crossing', parallel_modules, parallel_b_modules)):
            spec, context = {'recipe': recipe}, {'native': 'context'}
            with self.subTest(recipe=recipe), patch.object(target, 'build_piece', return_value=('assets', 'rules')) as chosen, \
                 patch.object(other, 'build_piece', side_effect=AssertionError('Wrong alignment compiler')):
                self.assertEqual(recipes.build_piece(spec, context), ('assets', 'rules'))
                chosen.assert_called_once_with(spec, context)

    def test_actual_adaptive_metadata_uses_the_correct_owning_origin_and_avenue_phase(self):
        from scp_highway import parallel_b_modules, parallel_modules
        for identifier, origin, target, other in (
            ('ddrhw-parallel-b-crossing', [0, -1], parallel_b_modules, parallel_modules),
            ('ddrhw-parallel-crossing', [0, 0], parallel_modules, parallel_b_modules)):
            spec = piece(identifier)
            before = deepcopy(spec)
            with self.subTest(piece=identifier), \
                 patch.object(target, 'declaration', return_value={'world_origin_cell': origin}) as chosen, \
                 patch.object(other, 'declaration', side_effect=AssertionError('Wrong adaptive source frame')):
                rows = adaptive_ground.bindings(spec)
                self.assertEqual(len(rows), 3)
                self.assertTrue(all(row['prop'] for row in rows))
                chosen.assert_called_once_with(spec)
            self.assertEqual(spec, before)

    def test_assembly_icon_uses_b_boundaries_without_reading_a_routes(self):
        spec = {'id': 'b-icon', 'domain': 'highway', 'recipe': b.PREFIX + 'crossing', 'geometry_key': 'parallel-b-crossing'}
        scene = {'placements': [{'piece_id': 'b-icon', 'origin_m': [32., -48.], 'rotation_ccw_degrees': 90}]}
        records = {(2, -3): [{'points': [(34., 49., 15.), (36., 51., 15.)]}]}
        with patch.object(b, 'expected_cell_routes', return_value=records) as chosen, \
             patch.object(b, '_source_origin', return_value=(2, -3)), \
             patch.object(b, 'PARTITIONS', {'crossing': ((2, -3),)}), \
             patch.object(a, 'expected_cell_routes', side_effect=AssertionError('B icon read A routes')):
            self.assertEqual(icons.assembly_icon_routes(scene, [spec]), [[(31., -46., 15.), (29., -44., 15.)]])
            chosen.assert_called_once_with()
        self.assertEqual(icons.assembly_icon_network(b.SUBJECT), 'HWY')

    def test_b_evidence_path_names_the_actual_registered_assembly(self):
        expected = ('domains/highway/01_assemblies/' + b.SUBJECT + '/checks/accepted-connector-contracts.jsonc')
        self.assertEqual(contracts.REFERENCE, expected)
        self.assertTrue((ROOT / Path(expected).parent.parent / 'assembly.jsonc').is_file())
        self.assertEqual(tool('freeze_parallel_b_connectors').ASSEMBLY, b.SUBJECT)

    def test_missing_or_incomplete_raw_pins_stop_strict_extraction_before_any_record_acceptance(self):
        spec = fixture()[0]['pieces'][0]
        semantic = b.reviewed_facts(spec)
        with patch.object(contracts, 'load_contracts', return_value={}):
            self.assertEqual(connections._reviewed_facts(spec)['path_hashes_by_cell'], [])
            self.assertEqual(set(connections.reviewed_contract(spec)['ports']),
                             set(b.reviewed_contract(spec)['ports']))
            self.assertEqual(connections.reviewed_contract(spec)['boundary_measurement_precision'], 'saved-path')
            with self.assertRaisesRegex(ValueError, 'strict extraction requires independently checked saved PATH fingerprints'):
                connections.validate_connection_record(spec, {})
        for hashes in ([[spec['cells'][0], '0' * 64]],
                       [[[99, 99], '0' * 64] for _ in spec['cells']]):
            changed = deepcopy(semantic)
            changed['path_hashes_by_cell'] = hashes
            with self.subTest(hashes=hashes), patch.object(connections, '_reviewed_facts', return_value=changed):
                with self.assertRaisesRegex(ValueError, 'strict extraction requires'):
                    connections.validate_connection_record(spec, {})

    def test_a_connector_lookup_never_consults_b_bootstrap_or_accepted_evidence(self):
        spec = piece('ddrhw-parallel-crossing')
        from scp_highway.parallel_connector_contracts import CONTRACTS
        with patch.object(contracts, 'load_contracts', side_effect=AssertionError('A read B evidence')), \
             patch.object(b, 'reviewed_facts', side_effect=AssertionError('A read B semantics')):
            self.assertEqual(connections._reviewed_facts(spec), CONTRACTS[spec['recipe']])

    def test_b_loader_requires_complete_native_byte_fingerprints_for_all_fifteen_types(self):
        evidence = {'schema_version': 1, 'state': 'accepted-independently-checked-saved-resources',
                    'game_operation': 'unverified', 'source': {'manifest_sha256': '0' * 64}, 'contracts': {}}
        for spec in fixture()[0]['pieces']:
            facts = b.reviewed_facts(spec)
            facts['path_hashes_by_cell'] = [[cell, '1' * 64] for cell in spec['cells']]
            evidence['contracts'][spec['recipe']] = facts
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = root / contracts.REFERENCE
            path.parent.mkdir(parents=True)
            path.write_text(jsonc.document(evidence, title='Independent B contract fixture', summary='Exercise complete numeric saved-PATH fingerprint validation.'))
            accepted = contracts.load_contracts(root)
            self.assertEqual(len(accepted), 15)
            self.assertEqual(sum(len(facts['cells']) for facts in accepted.values()), 34)
            recipe = next(iter(evidence['contracts']))
            for mutation in ('missing-cell', 'bad-hash', 'wrong-family'):
                changed = deepcopy(evidence)
                if mutation == 'missing-cell':
                    changed['contracts'][recipe]['path_hashes_by_cell'].pop()
                elif mutation == 'bad-hash':
                    changed['contracts'][recipe]['path_hashes_by_cell'][0][1] = 'not a resource hash'
                else:
                    changed['contracts'][recipe.replace('_b_', '_')] = changed['contracts'].pop(recipe)
                path.write_text(jsonc.document(changed, title='Independent B contract mutation', summary='Reject an incomplete or malformed saved-resource contract.'))
                with self.subTest(mutation=mutation), self.assertRaisesRegex(ValueError, 'fingerprints|fifteen reusable'):
                    contracts.load_contracts(root)

    def test_saved_b_freeze_associates_all_ports_and_composes_only_complete_outer_journeys(self):
        freezer = tool('freeze_parallel_b_connectors')
        manifest, scene, resources = fixture()
        pieces, records = {}, {}
        ports = journeys = 0
        for spec in manifest['pieces']:
            identifier = spec['id']
            measured = piece_connectivity(spec, resources[identifier], contract=b.reviewed_contract(spec),
                                          service_classifier=connections.service_classifier)
            mapping, components, channels, sources = freezer._channel_associations(spec, resources[identifier], measured)
            self.assertEqual(set(mapping), {port['id'] for port in measured['ports']})
            self.assertEqual({name for channel in channels for name in channel['ports']}, set(mapping))
            self.assertEqual({source['channel_id'] for source in sources}, {channel['id'] for channel in channels})
            self.assertTrue(components)
            self.assertTrue(freezer._full_saved_chord_check(spec, resources[identifier], measured)['passed'])
            pieces[identifier], records[identifier] = spec, measured
            ports += len(measured['ports'])
            journeys += len(measured['journeys'])
        composed = assembly_connectivity(b.SUBJECT, scene, records, pieces)
        self.assertEqual((ports, journeys, len(composed['ports']), len(composed['journeys']),
                          len(composed['encoded_route_joins'])), (200, 104, 20, 14, 90))
        self.assertEqual({port['variant'] for port in composed['ports']},
                         {'dd-rhw-l1', 'dd-rhw-l2', 'avenue-ground', 'avenue-sidewalk'})
        self.assertEqual(freezer.REVIEWED_COUNTS[a.HIGHWAY_SLIP_PROFILE], (200, 104, 20, 14, 90))

    def test_native_avenue_channel_coordinates_subtract_b_phase_without_moving_dd(self):
        freezer = tool('freeze_parallel_b_connectors')
        old_freezer = tool('freeze_parallel_connectors')
        for points, height, engine in ((((-8., 3.2), (3.2, -8.)), 0., 1),
                                       (((-8., -7.3), (-7.3, -8.)), 0., 2)):
            old = {'transport': engine, 'points': [(x, y, height) for x, y in points]}
            shifted = {'transport': engine, 'points': [(x + 8., y + 8., height) for x, y in points]}
            self.assertEqual(freezer._native_channel(shifted), old_freezer._native_channel(old))
        highway = {'transport': 1, 'points': [(-3.2, -8., 15.), (8., 3.2, 15.)]}
        self.assertEqual(freezer._native_channel(highway), old_freezer._native_channel(highway))

    def test_b_model_report_supplies_actual_visible_texture_references_to_the_framework(self):
        from scp.models import pack_s3d, parse_s3d
        from scp.recipes import combine_meshes
        from scp.track_paths import S3D
        from scp_highway import shadow_verify, ramp_verify
        import test_adaptive_ground as models
        spec = deepcopy(fixture()[0]['pieces'][0])
        spec['preview_id'] = '5ffff000'
        raw = models.model(models.model_mesh(b'Ground\0', 0x0400380E),
                           models.model_mesh(b'Deck\0', 0x5713000E, 15.))
        resources, preview = {}, []
        for cell, tile in zip(spec['cells'], spec['tile_ids']):
            for zoom in range(5):
                resources[*S3D, int(tile, 16) + zoom] = raw
            model = parse_s3d(raw)
            preview.append((model, model['meshes'], (16. * cell[0], 0., 16. * cell[1])))
        resources[*S3D, int(spec['preview_id'], 16)] = pack_s3d(combine_meshes(preview))
        # Synthetic model buffers exercise decoding, all zooms, the complete
        # preview, and the framework result contract. Native appearance and
        # carrier validation have their separate actual-native probes.
        with patch.object(a, 'check_wheeltrack_vertices', return_value={'passed': True}), \
             patch.object(ramp_verify, '_native_appearance', return_value={'checked': True}), \
             patch.object(shadow_verify, 'check_resources', return_value={'model_shadows_enabled': False}):
            report = b.check_models(resources, spec)
        self.assertEqual(report['texture_ids'], [0x0400380E, 0x5713000E])
        self.assertTrue(report['all_five_zooms_exact'])
        self.assertTrue(report['preview_matches_all_saved_cells'])

    def test_four_millimetre_saved_chord_keeps_the_real_grade_and_the_legacy_diagnostic(self):
        from scp.connectivity import PLACED_ROUTE_GRADE_TOLERANCE
        scene, pieces, records = tiny_grade_seam()
        left = next(port for port in records['left']['ports'] if port['direction'] == 'out')
        right = next(port for port in records['right']['ports'] if port['direction'] == 'in')
        self.assertGreater(abs(left['grade'] - right['grade']), PLACED_ROUTE_GRADE_TOLERANCE)
        self.assertLess(abs(left['actual_saved_grade'] - right['actual_saved_grade']), 1e-6)
        self.assertEqual(left['grade'], left['sampled_grade'])
        self.assertEqual(right['grade'], right['sampled_grade'])
        self.assertEqual(right['id'], '1-W-in-1')
        self.assertEqual(right['endpoint_m'], [-8., -.970563, 13.253148])
        self.assertLess(math.dist(right['sampled_tangent'], [1. / math.sqrt(2.), 1. / math.sqrt(2.)]), 1e-12)
        self.assertGreater(math.dist(right['actual_saved_tangent'], right['sampled_tangent']), 1e-8)
        composed = assembly_connectivity('saved-grade-precision', scene, records, pieces)
        self.assertEqual((len(composed['ports']), len(composed['journeys']), len(composed['encoded_route_joins'])),
                         (2, 1, 1))
        _scene, _pieces, precise = tiny_grade_seam(precise_contract=True)
        precise_right = next(port for port in precise['right']['ports'] if port['direction'] == 'in')
        self.assertEqual(precise_right['grade'], right['actual_saved_grade'])
        self.assertEqual(precise_right['sampled_tangent'], right['sampled_tangent'])
        self.assertEqual(precise_right['id'], right['id'])
        self.assertEqual(precise_right['endpoint_m'], right['endpoint_m'])

    def test_a_real_saved_grade_discontinuity_is_still_rejected_at_the_same_bound(self):
        from scp.connectivity import PLACED_ROUTE_GRADE_TOLERANCE
        scene, pieces, records = tiny_grade_seam(discontinuity=True)
        left = next(port for port in records['left']['ports'] if port['direction'] == 'out')
        right = next(port for port in records['right']['ports'] if port['direction'] == 'in')
        self.assertGreater(abs(left['actual_saved_grade'] - right['actual_saved_grade']), PLACED_ROUTE_GRADE_TOLERANCE)
        composed = assembly_connectivity('real-grade-discontinuity', scene, records, pieces)
        self.assertEqual(len(composed['encoded_route_joins']), 0)
        self.assertEqual(len(composed['ports']), 4)

    def test_invalid_saved_precision_witness_cannot_bypass_join_validation(self):
        for field, value in (('actual_saved_grade', float('nan')),
                             ('actual_saved_tangent', [0., 0.]), ('actual_saved_tangent', 'invalid')):
            scene, pieces, records = tiny_grade_seam()
            records['right']['ports'][0][field] = value
            with self.subTest(field=field, value=value), self.assertRaisesRegex(ValueError, 'exact saved'):
                assembly_connectivity('invalid-precision-witness', scene, records, pieces)

    def test_export_route_occurrences_match_the_declared_grade_basis_at_full_precision(self):
        from scp.connector_metadata import _route_matches_member
        route = {'engine_transport': 1, 'points': [(-8., -.970562748, 13.253147845),
            (-7.996935385, -.967498134, 13.251925525), (.970562748, 8., 10.)]}
        for precise in (False, True):
            _scene, _pieces, records = tiny_grade_seam(precise_contract=precise)
            port = next(port for port in records['right']['ports'] if port['direction'] == 'in')
            self.assertTrue(_route_matches_member(route, port))
            changed = deepcopy(port)
            changed['actual_saved_grade'] += .001
            self.assertFalse(_route_matches_member(route, changed))
        historical = deepcopy(port)
        _scene, _pieces, records = tiny_grade_seam()
        historical = next(port for port in records['right']['ports'] if port['direction'] == 'in')
        for field in ('grade_basis', 'actual_saved_grade', 'actual_saved_tangent', 'sampled_grade'):
            historical.pop(field)
        self.assertTrue(_route_matches_member(route, historical))


if __name__ == '__main__':
    unittest.main()
