"""Saved-byte negative controls for the independently placed modular kit."""
from copy import deepcopy
import hashlib
import math
from pathlib import Path
import struct
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT/'framework'), str(ROOT/'domains/highway/implementation')]

from scp.models import parse_s3d, pack_s3d
from scp.recipes import combine_meshes
from scp.track_paths import PATH, S3D
from scp_highway import modular_verify as piece_audit
from scp_highway import modular_assembly_verify as assembly_audit
from scp_highway import modular_ramps as fixture_writer
from scp_highway import ramp_geometry, ramp_paths


def fixture(*, compact=False):
    """Encode actual writer curves plus independent analytic native spines.

    No native game input is needed. These fixture models are not offered as
    visual/native evidence; actual native models receive the separate build.
    """
    rows = ([row for row in fixture_writer.module_catalog()['types'] if row['key'].endswith('-compact')]
            +[row for row in ramp_paths.module_catalog()['types'] if row['key'] in ('northwest-junction', 'southeast-junction')]
            if compact else [fixture_writer.module_catalog()['types'][i] for i in range(6)])
    stamp_reference = piece_audit.reference()
    stamp = {'geometry_key': piece_audit.STAMP, 'recipe': 'highway_ddrhw_modular_stamp',
             'cells': [r['cell'] for r in piece_audit.stamp_reference_cells()], 'footprint': [10, 10],
             'engineering': {'max_grade_percent': 30., 'pavement_path_offset_m': 0.,
                 'car_corridor_half_width_m': 1.25, 'car_corridor_height_m': 3.8,
                 'model_only_cells': []}}
    rows = [stamp]+rows
    pieces, scene, resources = {}, {'placements': []}, {}
    for index, row in enumerate(rows):
        key = row['geometry_key']
        identifier = 'fixture-'+key
        piece = {**deepcopy(row), 'id': identifier, 'domain': 'highway',
                 'tile_ids': [f'{0x7F000000+index*0x10000+n*0x100:08x}' for n in range(len(row['cells']))]}
        pieces[identifier] = piece
        origin = piece_audit.ORIGINS[key] if key == piece_audit.STAMP else row['world_origin_cell']
        scene['placements'].append({'piece_id': identifier, 'origin_m': [16*(origin[0]+4), -16*(origin[1]+4)],
                                    'rotation_degrees_ccw': 0})
        resources[identifier] = {}
    root = math.sqrt(2.)
    lines = []
    for v in (-3.2/root, 3.2/root):
        lines.extend([{'points': [ramp_geometry.world_coordinates(-200., v, 15.), ramp_geometry.world_coordinates(200., v, 15.)]},
                      {'points': [ramp_geometry.world_coordinates(200., v, 7.5), ramp_geometry.world_coordinates(-200., v, 7.5)]}])
    for u, transport in ((4.8/root, 1), (11.2/root, 1), (15.3/root, 2)):
        lines.extend([{'transport': transport, 'points': [ramp_geometry.world_coordinates(u, -200.), ramp_geometry.world_coordinates(u, 200.)]},
                      {'transport': transport, 'points': [ramp_geometry.world_coordinates(-u, 200.), ramp_geometry.world_coordinates(-u, -200.)]}])
    lines.extend(ramp_paths.compact_access_routes() if compact else fixture_writer.access_routes())
    for line in lines:
        line['allow_interior_ends'] = True
    sliced = ramp_paths.deduplicate_routes(ramp_paths.slice_routes(lines))
    owners = (assembly_audit.check_compact_owned_cells(pieces, scene) if compact else
              assembly_audit.check_owned_cells(pieces, scene)[0])
    for cell, owner in owners.items():
        resources[owner['piece_id']][*PATH, owner['tile']] = ramp_paths.encode_paths(
            sliced.get((cell[0]-4, cell[1]-4), []), allow_empty=True)
    return pieces, scene, owners, resources


class ModularSavedContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pieces, cls.scene, cls.owners, cls.resources = fixture()

    def test_seven_owners_keep_every_cell_unique_and_twenty_native_channels(self):
        self.assertEqual(len(self.owners), 62)
        self.assertEqual(len(assembly_audit.native_external_contract()), 20)
        self.assertEqual(sum(p['transport'] == 2 for p in assembly_audit.native_external_contract()), 4)

    def test_all_new_saved_paths_have_literal_ports_and_r40_profiles(self):
        for identifier, piece in self.pieces.items():
            if piece['geometry_key'] == piece_audit.STAMP:
                continue
            with self.subTest(key=piece['geometry_key']):
                report = piece_audit.check_paths(self.resources[identifier], piece)
                self.assertTrue(report['r40_profile']['passed'])
                self.assertLess(report['maximum_grade_percent'], 30.)

    def test_whole_saved_layout_has_eight_movements_and_both_walkways_in_four_rotations(self):
        routes = assembly_audit.shared.decode_placed_routes(self.owners, self.resources)
        for q in range(4):
            transformed = assembly_audit._rotate_routes(routes, q)
            report, seams = assembly_audit.check_saved_routes(transformed, turns=q)
            self.assertTrue(report['passed'])
            self.assertEqual(report['required_arm_movements'], 8)
            self.assertEqual(report['native_through_lane_and_sidewalk_journeys'], 10)
            self.assertTrue(seams)

    def test_same_saved_stamp_accepts_the_independent_compact_counterparts(self):
        pieces, scene, owners, resources = fixture(compact=True)
        self.assertEqual(len(owners), 53)
        self.assertEqual(resources['fixture-modular-stamp'], self.resources['fixture-modular-stamp'])
        report = assembly_audit.verify_compact_alternative_resources(
            {'pieces': list(pieces.values())}, scene, resources, inspect_models=False)
        self.assertTrue(report['saved_path_and_construction_checks_passed'])
        self.assertFalse(report['saved_resource_checks_passed'])
        self.assertEqual(len(report['proper_rotation_paths']), 4)
        self.assertEqual(report['paths']['required_arm_movements'], 8)
        self.assertEqual(report['paths']['native_through_lane_and_sidewalk_journeys'], 10)
        wrong = deepcopy(scene)
        wrong['placements'][1]['origin_m'][1] += 16
        with self.assertRaisesRegex(ValueError, 'pose'):
            assembly_audit.check_compact_owned_cells(pieces, wrong)

    def test_moving_a_component_or_repeating_a_type_is_rejected(self):
        for mutation in ('move', 'repeat'):
            scene = deepcopy(self.scene)
            if mutation == 'move':
                scene['placements'][1]['origin_m'][0] += 16
            else:
                scene['placements'][1] = deepcopy(scene['placements'][0])
            with self.assertRaises(ValueError):
                assembly_audit.check_owned_cells(self.pieces, scene)

    def test_removing_a_saved_transfer_fails_the_assembled_route_graph(self):
        routes = assembly_audit.shared.decode_placed_routes(self.owners, self.resources)
        # Removing an actual ramp-only cell's records cannot be hidden by
        # native mainline/Avenue through routes, which remain in the fixture.
        bad = [r for r in routes if r['piece_id'] != 'fixture-lower-exit-r40']
        bad = [{**route, 'id': i} for i, route in enumerate(bad)]
        with self.assertRaisesRegex(ValueError, 'disconnected|missing'):
            assembly_audit.check_saved_routes(bad)

    def test_wrong_height_grade_limit_or_empty_shoulder_declaration_fails(self):
        source = self.pieces['fixture-lower-exit-r40']
        for change in ({'max_grade_percent': 40.}, {'model_only_cells': []},
                       {'pavement_path_offset_m': .5}):
            piece = deepcopy(source)
            piece['engineering'].update(change)
            with self.assertRaises(ValueError):
                piece_audit.check_paths(self.resources[source['id']], piece)

    def test_changed_new_arc_and_easing_height_fail_positive_measurements(self):
        piece = self.pieces['fixture-upper-exit-r40']
        rows = piece_audit._source_routes(self.resources[piece['id']], piece)
        for axis in (0, 2):
            changed = deepcopy(rows)
            candidates = [(r, i, p) for r in changed for i, p in enumerate(r['points'])
                          if -19. < p[0] < -10. and 2 <= i < len(r['points'])-2]
            self.assertTrue(candidates)
            route, index, point = candidates[len(candidates)//2]
            point = list(point)
            point[axis] += .1
            route['points'][index] = tuple(point)
            with self.assertRaisesRegex(ValueError, 'length|profile|circle'):
                piece_audit.check_profile_routes(changed, 'upper-exit-r40')

    def test_terminal_curve_cannot_be_replaced_with_a_chord(self):
        piece = self.pieces['fixture-northwest-terminal-r40']
        rows = piece_audit._source_routes(self.resources[piece['id']], piece)
        changed = [{**r, 'points': [r['points'][0], r['points'][-1]]} for r in rows]
        with self.assertRaisesRegex(ValueError, 'R40'):
            piece_audit.check_profile_routes(changed, 'northwest-terminal-r40')

    def test_removing_walkways_and_adding_a_forbidden_external_shortcut_fail(self):
        original = assembly_audit.shared.decode_placed_routes(self.owners, self.resources)
        no_walks = [{**r, 'id': i} for i, r in enumerate(r for r in original if r['transport'] == 1)]
        with self.assertRaisesRegex(ValueError, 'sidewalk|missing'):
            assembly_audit.check_saved_routes(no_walks)
        ports = assembly_audit.native_external_contract()
        first = next(p for p in ports if p['transport'] == 1 and p['direction'] == 'in' and p['arm'] == 'HW_NE')
        last = next(p for p in ports if p['transport'] == 1 and p['direction'] == 'out' and p['arm'] == 'AVE_SE')
        template = next(r for r in original if math.dist(r['points'][0], first['point']) < 1e-5)
        tail = next(r for r in original if math.dist(r['points'][-1], last['point']) < 1e-5)
        # This deliberately illegal cross-network witness preserves the real
        # boundary tangents, so the forbidden-turn rule must reject it.
        start, finish = first['point'], last['point']
        shortcut = {**template, 'id': len(original), 'exit': tail['exit'],
                    'points': [start, tuple(start[i]+.01*first['tangent'][i] if i < 2 else start[i] for i in range(3)),
                               tuple(finish[i]-.01*last['tangent'][i] if i < 2 else finish[i] for i in range(3)), finish]}
        with self.assertRaisesRegex(ValueError, 'forbidden'):
            assembly_audit.check_saved_routes(original+[shortcut])

    def test_actual_saved_pier_has_six_complete_outward_sides(self):
        ramp = next(r for r in fixture_writer.variant_ramps() if r['id'] == 'lower-off')
        raw = ramp_geometry.pack_road_model(fixture_writer._pier_faces(ramp), 0x5EB4BEEE)
        owners = {(0, 0): {'piece_id': 'pier', 'tile': 0x100, 'local_cell': (0, 0), 'angle': 0, 'origin': (0., 0.)}}
        triangles = [p for _cell, p, _textures in assembly_audit._indexed_faces(owners, {'pier': {(*S3D, 0x104): raw}})]
        x, y, top, gx, gy = assembly_audit.PIERS[0]
        corners = [(x+dx, y+dy, top+gx*dx+gy*dy) for dx in (-.4, .4) for dy in (-.4, .4)]
        self.assertTrue(assembly_audit.check_pier_shell(triangles, corners)['passed'])
        for mutation in ('remove', 'duplicate', 'reverse', 'raise'):
            changed = deepcopy(triangles)
            if mutation == 'remove':
                changed.pop()
            elif mutation == 'duplicate':
                changed[-1] = changed[0]
            elif mutation == 'reverse':
                changed[0] = list(reversed(changed[0]))
            else:
                changed[0][0] = (*changed[0][0][:2], changed[0][0][2]+.1)
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                assembly_audit.check_pier_shell(changed, corners)

    def test_construction_uses_saved_curved_approaches_and_rejects_changed_flags(self):
        piece = self.pieces['fixture-lower-exit-r40']
        data = self.resources[piece['id']]
        compiled = [(tuple(cell), b'unused-model', data[*PATH, int(iid, 16)])
                    for cell, iid in zip(piece['cells'], piece['tile_ids'])]
        rows, checks, cons = fixture_writer.construction_fields(piece, compiled)
        fields = {'CellLayout': rows, 'ConsLayout': cons, 'CheckType': checks, 'Costs': ['1000']}
        self.assertTrue(piece_audit.check_construction_fields(fields, piece, data)['actual_saved_route_flags_checked'])
        fields['CheckType'][-1] = checks[-1].split('0x')[0]+'0x00000000'
        with self.assertRaisesRegex(ValueError, 'construction'):
            piece_audit.check_construction_fields(fields, piece, data)

    def test_stamp_hashes_bind_all_five_zooms_and_preview_composition(self):
        raw = ramp_geometry.pack_road_model([((0., 0., 0., .1, .1), (1., 0., 0., .1, .1),
                                             (0., 0., -1., .1, .1))], 0x5713000E)
        model = parse_s3d(raw)
        path = b'SC4PATHS\r\n1.2\r\n0\r\n0\r\n0\r\n'
        piece = {'cells': [[0, 0], [1, 0]], 'tile_ids': ['70000000', '70000100'], 'preview_id': '70000ff5'}
        rows = [{'model_sha256': hashlib.sha256(raw).hexdigest(), 'path_sha256': hashlib.sha256(path).hexdigest()} for _ in range(2)]
        resources = {(*PATH, int(iid, 16)): path for iid in piece['tile_ids']}
        for iid in piece['tile_ids']:
            for q in range(5):
                resources[*S3D, int(iid, 16)+q] = raw
        resources[*S3D, int(piece['preview_id'], 16)] = pack_s3d(combine_meshes([
            (model, model['meshes'], (0., 0., 0.)), (model, model['meshes'], (16., 0., 0.))]))
        with patch.object(piece_audit, 'reference', return_value={'cells': rows}):
            self.assertTrue(piece_audit._stamp_models(resources, piece)['preview_matches_all_cells'])
            bad = dict(resources)
            bad[*S3D, 0x70000104] = raw+b'extra'
            with self.assertRaisesRegex(ValueError, 'frozen'):
                piece_audit._stamp_models(bad, piece)
            bad = {**resources, (*PATH, 0x70000100): path+b'-- changed\r\n'}
            with self.assertRaisesRegex(ValueError, 'PATH'):
                piece_audit._stamp_models(bad, piece)
            preview = parse_s3d(resources[*S3D, int(piece['preview_id'], 16)])
            data = bytearray(preview['vertices'][0]['data'])
            struct.pack_into('<f', data, 0, .125)
            preview['vertices'][0]['data'] = bytes(data)
            bad = {**resources, (*S3D, int(piece['preview_id'], 16)): pack_s3d(preview)}
            with self.assertRaisesRegex(ValueError, 'preview differs'):
                piece_audit._stamp_models(bad, piece)

    def test_stamp_projection_requires_the_frozen_actual_model_hash(self):
        raw = ramp_geometry.pack_road_model([((0., 0., 0., .1, .1), (1., 0., 0., .1, .1),
                                             (0., 0., -1., .1, .1))], 0x5713000E)
        owner = {'piece_id': 'stamp', 'geometry_key': piece_audit.STAMP, 'tile': 0x100,
                 'local_cell': (0, 0), 'angle': 0, 'origin': (0., 0.)}
        expected = {'pieces': {'stamp': {'cell_resources': [{'cell': [0, 0], 'model_sha256': hashlib.sha256(raw).hexdigest()}]}}}
        with patch('scp_highway.modular_partition_verify.reviewed_models', return_value=expected):
            records = assembly_audit._frozen_stamp_provenance({(0, 0): owner}, {'stamp': {(*S3D, 0x104): raw}})
            self.assertEqual(len(records), 1)
            changed = parse_s3d(raw)
            data = bytearray(changed['vertices'][0]['data'])
            struct.pack_into('<f', data, 0, 1.)
            changed['vertices'][0]['data'] = bytes(data)
            with self.assertRaisesRegex(ValueError, 'frozen native model provenance'):
                assembly_audit._frozen_stamp_provenance(
                    {(0, 0): owner}, {'stamp': {(*S3D, 0x104): pack_s3d(changed)}})

    def test_authored_attachment_cannot_use_the_stamp_overhang_allowance(self):
        owner = {'piece_id': 'ramp', 'geometry_key': 'lower-exit-r40', 'tile': 0x100,
                 'local_cell': (0, 0), 'angle': 0, 'origin': (0., 0.)}
        def saved_triangle(xs):
            return ramp_geometry.pack_road_model([
                tuple((x, 0., z, .1, .1) for x, z in xs)], 0x5713000E)
        inside = saved_triangle(((0., 0.), (1., 0.), (0., -1.)))
        self.assertEqual(len(assembly_audit._new_component_projection(
            {(0, 0): owner}, {'ramp': {(*S3D, 0x104): inside}})), 1)
        outside = saved_triangle(((7., 0.), (9., 0.), (7., -1.)))
        with self.assertRaisesRegex(ValueError, 'beyond its own construction cells'):
            assembly_audit._new_component_projection({(0, 0): owner}, {'ramp': {(*S3D, 0x104): outside}})


if __name__ == '__main__':
    unittest.main()
