"""Mutation checks for saved full-assembly traffic and physical seam evidence."""
from copy import deepcopy
import math
from pathlib import Path
import struct
import sys
from tempfile import TemporaryDirectory
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp import jsonc
from scp.models import pack_s3d
from scp.test_support import plane
from scp.verify import PATH, S3D
from scp_highway import assembly_verify as audit, ramp_paths, ramp_geometry

ASSEMBLY = ROOT / 'domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/assembly.jsonc'


def saved_path_fixture(include_transfers=True):
    scene = jsonc.load(ASSEMBLY)
    pieces = {placement['piece_id']: jsonc.load(ROOT / 'domains/highway/00_pieces' / placement['piece_id'] / 'piece.jsonc')
              for placement in scene['placements']}
    owners, _poses = audit.check_owned_cells(pieces, scene)
    lines = []
    root = math.sqrt(2.)
    # Analytic native straight lane continuations are fixture INPUTS. The
    # verifier's expected ports are literal native tile-half measurements.
    for v in (-3.2 / root, 3.2 / root):
        lines.append({'id': 'upper', 'points': [ramp_geometry.world_coordinates(-200., v, 15.), ramp_geometry.world_coordinates(200., v, 15.)]})
        lines.append({'id': 'lower', 'points': [ramp_geometry.world_coordinates(200., v, 7.5), ramp_geometry.world_coordinates(-200., v, 7.5)]})
    for u, transport in ((4.8 / root, 1), (11.2 / root, 1), (15.3 / root, 2)):
        lines.append({'id': 'avenue-nw', 'transport': transport, 'points': [ramp_geometry.world_coordinates(u, -200.), ramp_geometry.world_coordinates(u, 200.)]})
        lines.append({'id': 'avenue-se', 'transport': transport, 'points': [ramp_geometry.world_coordinates(-u, 200.), ramp_geometry.world_coordinates(-u, -200.)]})
    if include_transfers:
        lines.extend(ramp_paths.compact_access_routes())
    for line in lines:
        # The fixture's analytic native lines deliberately start far beyond
        # the selected city footprint. Their terminal cells are discarded.
        line['allow_interior_ends'] = True
    sliced = ramp_paths.deduplicate_routes(ramp_paths.slice_routes(lines))
    resources = {piece_id: {} for piece_id in pieces}
    for cell, owner in owners.items():
        routes = sliced.get((cell[0] - 3, cell[1] - 3), [])
        raw = ramp_paths.encode_paths(routes, allow_empty=True)
        key = (*PATH, owner['tile'])
        previous = resources[owner['piece_id']].get(key)
        if previous is not None and previous != raw:
            raise AssertionError('A repeated source tile has different fixture traffic')
        resources[owner['piece_id']][key] = raw
    return pieces, scene, owners, resources


class CompactAssemblyVerifierTests(unittest.TestCase):
    def test_evidence_output_cannot_mutate_verified_build_file_closure(self):
        with TemporaryDirectory() as directory:
            build = Path(directory) / 'build'
            for target in (build / 'proof.json', build / 'docs/proof.json'):
                with self.assertRaisesRegex(ValueError, 'must stay outside the verified build directory'):
                    audit.verify_assembly(build, {}, evidence_path=target, verify_package=False)
                self.assertFalse(build.exists())

    def test_literal_boundary_keeps_all_four_dd_lanes_and_both_avenue_sidewalks(self):
        ports = audit.native_external_contract()
        self.assertEqual(len(ports), 20)
        self.assertEqual(sum(p['transport'] == 2 for p in ports), 4)
        self.assertIn({'transport': 1, 'direction': 'in', 'point': (-8., -115.2, 15.),
            'tangent': (math.sqrt(.5), math.sqrt(.5)), 'grade': 0., 'arm': 'HW_SW'}, ports)
        self.assertTrue(any(p['point'] == (115.2, 8., 7.5) and p['direction'] == 'in' for p in ports))
        self.assertTrue(any(p['point'] == (8., -23.3, 0.) and p['transport'] == 2 for p in ports))

    def test_current_saved_path_fixture_proves_twelve_distinct_arm_movements(self):
        pieces, scene, owners, resources = saved_path_fixture()
        routes = audit.decode_placed_routes(owners, resources)
        report, seams = audit.check_saved_routes(routes, owners)
        self.assertEqual(report['required_arm_movements'], 12)
        self.assertEqual(report['highway_avenue_transfers'], 8)
        self.assertEqual(report['through_arm_movements'], 4)
        self.assertTrue(report['all_cross_deck_journeys_require_intentional_ground_junctions'])
        self.assertTrue(seams)

    def test_missing_ramps_cannot_pass_from_native_through_routes_alone(self):
        pieces, scene, owners, resources = saved_path_fixture(include_transfers=False)
        with self.assertRaisesRegex(ValueError, 'missing required highway/Avenue transfer'):
            audit.check_saved_routes(audit.decode_placed_routes(owners, resources), owners)

    def test_changed_placement_is_rejected_by_the_independent_construction_contract(self):
        pieces, scene, owners, resources = saved_path_fixture(False)
        scene['placements'][0]['origin_m'][0] += 16.
        with self.assertRaisesRegex(ValueError, 'more than one owner|41-cell'):
            audit.check_owned_cells(pieces, scene)

    def test_displaced_external_lane_fails_even_when_arm_names_are_unchanged(self):
        pieces, scene, owners, resources = saved_path_fixture()
        routes = audit.decode_placed_routes(owners, resources)
        target = next(route for route in routes if route['points'][0] == (-8., -115.2, 15.))
        x, y, h = target['points'][0]; target['points'][0] = (x, y + .1, h)
        with self.assertRaisesRegex(ValueError, 'native boundary channel'):
            audit.check_saved_routes(routes, owners)

    def test_missing_pedestrian_route_cannot_be_hidden_by_complete_car_routes(self):
        pieces, scene, owners, resources = saved_path_fixture()
        routes = audit.decode_placed_routes(owners, resources)
        target = next(route for route in routes if route['transport'] == 2 and route['points'][0] == (8., -23.3, 0.))
        target['transport'] = 3
        with self.assertRaisesRegex(ValueError, 'native boundary channel'):
            audit.check_saved_routes(routes, owners)

    def test_inserted_cross_deck_shortcut_cannot_hide_behind_valid_ground_transfers(self):
        pieces, scene, owners, resources = saved_path_fixture()
        routes = audit.decode_placed_routes(owners, resources)
        # This extra saved route shares real directed native endpoints but
        # changes decks above ground. Existing valid ground routes remain.
        routes.append({'id': len(routes), 'transport': 1, 'cell': (3, 3), 'placement': 0,
                       'entry': 3, 'exit': 3, 'compatibility': 1,
                       'points': [(51.2, -56., 15.), (54.2, -53., 15.),
                                  (55., -52.2, 11.), (54.2, -53., 7.5), (51.2, -56., 7.5)]})
        with self.assertRaisesRegex(ValueError, 'deck transfer that bypasses'):
            audit.check_saved_routes(routes, owners)

    def test_surface_seam_support_uses_actual_triangles_and_rejects_missing_pavement(self):
        def pavement(height):
            model = plane(height=height)
            model['indices'][0]['values'] = (0, 2, 1, 0, 3, 2)
            return pack_s3d(model)
        owner = {'placement': 0, 'piece_id': 'a', 'tile': 0x7F700000, 'local_cell': (0, 0), 'angle': 0, 'origin': (0., 0.)}
        owners = {(0, 0): owner, (0, 1): {**owner, 'placement': 1, 'piece_id': 'b', 'tile': 0x7F700010, 'origin': (0., -16.)}}
        resources = {'a': {(*S3D, owner['tile'] + 4): pavement(7.5)},
                     'b': {(*S3D, 0x7F700014): pavement(7.5)}}
        routes = [{'transport': 1, 'points': [(0., 0., 7.5), (0., -8., 7.5)]},
                  {'transport': 1, 'points': [(0., -8., 7.5), (0., -16., 7.5)]}]
        seams = [(0, 1, (0., -8., 7.5))]
        # This deliberately small physical fixture exercises the seam reader,
        # without claiming the full diamond's construction or movement proof.
        old_contract = audit.CONSTRUCTION_CELLS
        try:
            audit.CONSTRUCTION_CELLS = frozenset(owners)
            report = audit.check_model_seams(owners, resources, routes, seams)
            self.assertEqual(report['car_lane_collar_samples'], 5)
            resources['b'][*S3D, 0x7F700014] = pavement(7.7)
            with self.assertRaisesRegex(ValueError, 'pavement seam has a gap'):
                audit.check_model_seams(owners, resources, routes, seams)
        finally:
            audit.CONSTRUCTION_CELLS = old_contract

    def test_actual_support_faces_require_all_six_columns_both_contacts_and_clear_car_paths(self):
        def saved_model(*, upper_plane=15., column=True):
            # Independent rectangular planes and four vertical column sides
            # exercise the saved S3D reader without compiler helper geometry.
            points, indices = [], []
            for height in (7.5, upper_plane):
                start = len(points)
                points.extend([(-2., height, -2.), (2., height, -2.),
                               (2., height, 2.), (-2., height, 2.)])
                indices.extend(start + n for n in (0, 2, 1, 0, 3, 2))
            if column:
                start = len(points)
                points.extend((x, height, z) for height in (0., 15.)
                              for x, z in ((-.4, -.4), (.4, -.4), (.4, .4), (-.4, .4)))
                for a, b in ((0, 1), (1, 2), (2, 3), (3, 0)):
                    indices.extend(start + n for n in (a, b, b + 4, a, b + 4, a + 4))
            model = plane()
            model['vertices'][0]['data'] = b''.join(struct.pack('<5f', *p, 0., 0.) for p in points)
            model['indices'][0]['values'] = tuple(indices)
            model['primitives'][0] = [(0, 0, len(indices))]
            return pack_s3d(model)

        owners = {cell: {'placement': n, 'piece_id': str(n), 'tile': 0x7F700000 + n * 16,
                         'local_cell': (0, 0), 'angle': 0,
                         'origin': (cell[0] * 16., -cell[1] * 16.)}
                  for n, cell in enumerate(sorted(audit.SUPPORT_CELLS))}
        resources = {owner['piece_id']: {(*S3D, owner['tile'] + 4): saved_model()}
                     for owner in owners.values()}
        routes = [{'transport': 1, 'points': [(-200., 200., 0.), (200., 200., 0.)]}]
        report = audit.check_saved_supports(owners, resources, routes)
        self.assertEqual(report['actual_columns'], 6)
        self.assertEqual(report['actual_vertical_triangles'], 48)
        self.assertEqual(report['actual_deck_contact_corner_samples'], 48)
        self.assertLess(max(p['height_difference_m'] for p in report['deck_contact_samples']), 1e-8)
        owner = next(iter(owners.values())); key = (*S3D, owner['tile'] + 4)
        resources[owner['piece_id']][key] = saved_model(upper_plane=15.1)
        with self.assertRaisesRegex(ValueError, 'does not intersect the actual lower or upper road plane'):
            audit.check_saved_supports(owners, resources, routes)
        resources[owner['piece_id']][key] = saved_model()
        east, north = owner['origin']
        collision = [{'transport': 1, 'points': [(east - 2., north, 7.5), (east + 2., north, 7.5)]}]
        with self.assertRaisesRegex(ValueError, 'intersects the declared 1.25-metre car corridor'):
            audit.check_saved_supports(owners, resources, collision)
        resources[owner['piece_id']][key] = saved_model(column=False)
        with self.assertRaisesRegex(ValueError, 'missing a measured centre support column'):
            audit.check_saved_supports(owners, resources, routes)


if __name__ == '__main__':
    unittest.main()
