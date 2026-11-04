"""Reversed source, coexisting native markers, and finite source-phase controls."""
from copy import deepcopy
import hashlib
import json
import math
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT/'framework'))
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0, SourcePackages(ROOT))
from scp import jsonc, native_approaches as framework
from scp_highway import y_junction_approaches as original_approaches
from scp_highway import y_junction_native_models as original_native
from scp_highway import y_junction_reversed_approaches as approaches
from scp_highway import y_junction_reversed_native_models as native
from scp_highway import y_junction_reversed_source as source
import test_y_junction_approaches as original_fixture


def specification(slug):
    from scp_highway.y_junction_reversed_layout import module_catalog
    row = next(row for row in module_catalog()['types'] if row['id'] == slug)
    return {'id': slug, 'domain': 'highway', 'recipe': row['recipe'],
        'geometry_key': row['geometry_key'], 'y_junction_variant': 'reversed',
        'cells': row['cells'], 'footprint': row['footprint'],
        'tile_ids': [f'{0x7F700000+i*0x100:08x}' for i in range(len(row['cells']))],
        'native_y_junction_approaches': True}


def saved_socket(piece):
    old_id = piece['id'].replace('y-reversed-', 'y-', 1)
    old = original_fixture.specification(old_id)
    _resources, _key, routes = original_fixture.socket_fixture(old)
    for route in routes:
        route['points'].reverse()
        route['entry'], route['exit'] = route['exit'], route['entry']
        route['lane'] = 1-route['lane']
    declared = approaches.approaches(piece)[0]
    key = (*original_approaches.PATH, int(declared['end_tile_id'], 16))
    return {key: original_fixture.encoded_routes(routes)}, routes, key


class ReversedSourceControls(unittest.TestCase):
    def test_every_whole_journey_reverses_the_opposite_frozen_route(self):
        actual = source.source_report()
        original = jsonc.load(source.ORIGINAL/'evidence/design-geometry.jsonc')
        self.assertEqual(actual['state'], 'author-derived-source-candidate')
        for name in source.NAMES:
            opposite = '-'.join(reversed(name.split('-')))
            self.assertEqual(actual['routes'][name], list(reversed(original['routes'][opposite])))
            before, after = original['route_metadata'][opposite], actual['route_metadata'][name]
            self.assertEqual((after['from_deck'], after['to_deck']), (before['to_deck'], before['from_deck']))
            self.assertEqual((after['from_lane'], after['to_lane']), (1-before['to_lane'], 1-before['from_lane']))
            points = actual['routes'][name]
            if name in ('B-C', 'C-B'):
                self.assertEqual((points[0][2], points[-1][2]), (15., 7.5))
                self.assertTrue(all(a[2] >= b[2] for a, b in zip(points, points[1:])))
            else:
                self.assertTrue(all(point[2] == points[0][2] for point in points))

    def test_changed_or_revoked_original_input_is_rejected(self):
        geometry = (source.ORIGINAL/'evidence/design-geometry.jsonc').read_bytes()
        review = (source.ORIGINAL/'evidence/source-verification.jsonc').read_bytes()
        for inputs in ((geometry+b' ', review), (geometry, review+b' '),
                       (geometry, review.replace(b'"passed": true', b'"passed": false', 1))):
            with self.assertRaisesRegex(ValueError, 'exact frozen original source and review'):
                source.derive_report(*inputs)

    def test_warm_source_cache_rejects_changed_candidate_and_returns_copies(self):
        original = source.source_report()
        altered = source.source_report()
        altered['routes']['A-B'][0][0] += .01
        self.assertEqual(source.source_report(), original)
        with TemporaryDirectory() as folder:
            subject = Path(folder)
            (subject/'evidence').mkdir()
            path = subject/'evidence/design-geometry.jsonc'
            path.write_text(json.dumps(original))
            with patch.object(source, 'SUBJECT', subject):
                self.assertEqual(source.source_report(), original)
                path.write_text(json.dumps(altered))
                with self.assertRaisesRegex(ValueError, 'frozen directed derivation'):
                    source.source_report()


class ReversedNativeConstructionControls(unittest.TestCase):
    def test_exact_marker_families_coexist_with_every_original_rotation(self):
        old = [original_fixture.specification(slug) for slug in original_approaches.OWNERS]
        new = [specification(slug) for slug in approaches.OWNERS]
        combined = framework.expected_solution_sections([*old, *new])[original_approaches.SECTION]
        self.assertEqual(len(combined), 12)
        self.assertEqual({value[0] for value in combined.values()}, {0x57530000, 0x57530200, 0x57530900})
        row = approaches.approaches(new[0])[0]
        self.assertEqual(row['networks'], [{'name': 'monorail', 'flags': '04000100'},
                                           {'name': 'dirtroad', 'flags': '03010000'}])
        bad = {original_approaches.SECTION: tuple((*r[:2], 0x57530200, *r[3:])
            for r in original_approaches.rul1_sections(old[0])[original_approaches.SECTION])}
        with patch.object(approaches, 'rul1_sections', return_value=bad):
            with self.assertRaisesRegex(ValueError, 'Conflicting native DD RUL1'):
                framework.expected_solution_sections([old[0], new[0]])

    def test_wrong_explicit_variant_or_identity_cannot_select_new_helpers(self):
        piece = specification(next(iter(approaches.OWNERS)))
        for changes in ({'y_junction_variant': 'original'}, {'y_junction_variant': 'other'},
                        {'id': piece['id'].replace('y-reversed-', 'y-')},
                        {'recipe': 'highway_ddrhw_y_diagonal_stem_split'}):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                original_approaches.approaches({**piece, **changes})

    def test_saved_reversed_lanes_cover_each_socket_and_both_propagation_orders(self):
        for slug in approaches.OWNERS:
            piece = specification(slug)
            resources, routes, key = saved_socket(piece)
            result = approaches.check_native_boundary_paths(None, piece, resources)
            self.assertEqual(result['boundary_members_checked'], 4)
            self.assertEqual(result['proper_rotations_checked'], 4)
            self.assertEqual({row['construction_order'] for row in result['oriented_propagation']}, {'inward', 'outward'})
            self.assertEqual(result['native_helper_tile'], '57530000' if slug.endswith('core') else '57530200')
            routes[0]['lane'] = 1-routes[0]['lane']
            with self.assertRaises(ValueError):
                approaches.check_native_boundary_paths(None, piece, {key: original_fixture.encoded_routes(routes)})

    def test_helper_padding_remains_reversible_and_optional(self):
        for slug in approaches.OWNERS:
            piece = specification(slug)
            before = original_fixture.core_fields(piece)
            layout, checks, cons = approaches.add_approaches(piece, before['CellLayout'], before['CheckType'], before['ConsLayout'])
            after = {**before, 'CellLayout': layout, 'CheckType': checks, 'ConsLayout': cons}
            self.assertEqual(approaches.check_construction_approaches(after, piece), before)
            after['CheckType'][-1] = after['CheckType'][-1].replace(' optional', '')
            with self.assertRaisesRegex(ValueError, 'optional network flags'):
                approaches.check_construction_approaches(after, piece)


class ActualReversedNativeControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        original_fixture.ActualNativeYJunctionApproaches.setUpClass.__func__(cls)

    def test_fresh_twelve_native_members_match_the_bound_reversed_source(self):
        measured = native.native_profiles_report(self.donors)
        expected = {row['arm']: row for row in source.source_report()['native_socket_members']}
        for arm in measured['arms']:
            for member in arm['members']:
                row = next(row for row in expected[arm['arm']]['members']
                    if (row['lane'], row['direction']) == (member['lane'], member['direction']))
                self.assertLess(math.dist(row['endpoint_enh_m'], member['point_enh_m']), 2e-8)
                self.assertLess(math.dist(row['unit_travel_tangent_enh'], member['travel_tangent_enh']), 2e-8)
        self.assertEqual(sum(len(arm['members']) for arm in measured['arms']), 12)

    def test_native_floor_phase_and_south_contact_are_fresh_not_original_assumptions(self):
        for arm in ('A', 'B'):
            helper = [row for row in native.posed_native_faces(self.donors, arm)
                      if row['kind'] == 'helper' and row['role'] == 'pavement']
            self.assertEqual({p[1] for row in helper for face in row['triangles'] for p in face}, {7.5, 15.})
        self.assertEqual(native.native_join_plane(self.donors, 'C'), 55.99899959564209)
        contacts = native.native_owned_interface_faces(self.donors)
        self.assertTrue(contacts)
        for row in contacts:
            self.assertTrue(row['reference_only_already_rendered_native'])
            self.assertFalse(row['copy_into_custom_DAT_permitted'])
            self.assertFalse(row['underside_or_car_corridor_waiver'])
            for fragment in row['fragments']:
                for point in fragment['triangle']:
                    self.assertTrue(55.99899959564209-1e-12 <= point[0] <= 56.+1e-12)
                    self.assertTrue(-8.-1e-12 <= point[2] <= 8.+1e-12)

    def test_finite_reversed_native_lofts_certify_and_reject_wrong_phase_uv_or_winding(self):
        compiled = native.extrude_native_collars(self.donors)
        roles, materials, faces = [], {}, []
        for row in compiled['groups']:
            role = f"{row['role']}-native-{row['arm']}-{row['deck']}-{row['kind']}"
            if role not in materials:
                roles.append(role); materials[role] = row['material']
            faces.extend(tuple((*p, float(roles.index(role))) for p in face) for face in row['triangles'])
        proof = native.certify_native_collars(faces, roles, materials, self.donors)
        self.assertEqual(proof['native_faces_checked'], len(faces))
        self.assertEqual(proof['buried_peer_body_regions'], [])
        buried = proof['buried_helper_body_regions']
        # Uncut source quads have two triangles per arm/deck. The measured
        # saved city-cell partition splits these eight into24 actual faces.
        self.assertEqual(len(buried), 8)
        self.assertAlmostEqual(sum(row['source_body_surface_area_below_floor_m2'] for row in buried),
                               6.*((15.-14.00100040435791)+(7.5-6.500999927520752)), places=8)
        for row in buried:
            self.assertEqual(row['role'], f"body-native-{row['arm']}-{row['deck']}-helper")
            self.assertEqual(row['source_native_tile_id'], '57530200')
            self.assertEqual(row['source_native_pose'], 0 if row['arm'] == 'A' else 3)
            self.assertEqual(row['analysis_below_height_m'], 15. if row['deck'] == 'upper' else 7.5)
            self.assertEqual(row['underside_height_m'], 14. if row['deck'] == 'upper' else 6.5)
            self.assertTrue(row['requires_independent_complete_shell_and_outer_wall_proof'])
            self.assertTrue(row['requires_independent_actual_slab_containment_proof'])
            self.assertFalse(row['generic_authored_phase_wall_covered'])
            self.assertFalse(row['raised_native_strip_and_actual_saved_faces_changed'])
        # A coincident ordinary phase wall remains an authored shell face.
        generic = 'body'
        roles.append(generic)
        source_index = buried[0]['face_index']
        materials[generic] = materials[buried[0]['role']]
        phase_wall = tuple((*point[:5], float(roles.index(generic))) for point in faces[source_index])
        with_phase_wall = native.certify_native_collars([*faces, phase_wall], roles, materials, self.donors)
        self.assertEqual(len(with_phase_wall['buried_helper_body_regions']), len(buried))
        self.assertNotIn(len(faces), with_phase_wall['certified_face_indices'])
        # Rotate the actual helper body to the wrong native half-cell pose,
        # retaining its role/material/UVs. The source envelope must reject it.
        wrong_pose = deepcopy(faces)
        target = next(row for row in buried if row['arm'] == 'A' and row['deck'] == 'upper')
        index = target['face_index']
        wrong_pose[index] = tuple((-64.-p[0], p[1], 64.-p[2], *p[3:]) for p in wrong_pose[index])
        with self.assertRaisesRegex(ValueError, 'pinned finite native'):
            native.certify_native_collars(wrong_pose, roles, materials, self.donors)
        self.assertEqual(native.native_join_audit(faces, roles, materials, self.donors)['native_finite_segments_checked'], 86)
        for transform in (lambda p: (p[0], p[1]+.001, *p[2:]),
                          lambda p: (*p[:3], p[3]+.1, *p[4:])):
            changed = deepcopy(faces)
            changed[0] = tuple(transform(p) for p in changed[0])
            with self.assertRaisesRegex(ValueError, 'pinned finite native'):
                native.certify_native_collars(changed, roles, materials, self.donors)
        changed = deepcopy(faces); changed[0] = tuple(reversed(changed[0]))
        with self.assertRaisesRegex(ValueError, 'pinned finite native'):
            native.certify_native_collars(changed, roles, materials, self.donors)

    def test_original_reader_outputs_survive_interleaved_reversed_calls(self):
        before = original_native.posed_native_faces(self.donors, 'A')
        native.posed_native_faces(self.donors, 'A')
        native.retained_core_collar_faces(self.donors)
        self.assertEqual(original_native.posed_native_faces(self.donors, 'A'), before)
        self.assertEqual(original_native.posed_native_faces(self.donors, 'A', variant='original'), before)
        with self.assertRaisesRegex(ValueError, 'cannot select another variant'):
            native.posed_native_faces(self.donors, 'A', variant='original')

    def test_only_four_approved_caps_clip_by_exact_owned_cells_and_keep_raw_profiles(self):
        report = native.ownership_join_trace_report(self.donors, native.APPROVED_INTERFACE_CELLS)
        self.assertFalse(report['occlusion_floor_or_underside_waiver'])
        self.assertEqual(len(report['traces']), 4)
        for row in report['traces']:
            self.assertAlmostEqual(row['full_source_length_m'], 2.343146625118034, places=12)
            self.assertAlmostEqual(row['inside_owned_length_m'], 2.3417325134463294, places=12)
            self.assertAlmostEqual(row['outside_owned_length_m'], .0014141116717046691, places=12)
            self.assertEqual(row['positive_length_outside_intersection_with_custom_mask_m'], 0.)
            self.assertTrue(row['raw_source_segments'])
            self.assertTrue(row['inside_owned_segments'])
            self.assertTrue(row['outside_owned_segments'])
        for arm in ('A', 'B', 'C'):
            for deck in ('upper', 'lower'):
                raw = native.visible_native_end_sections(self.donors, arm, deck)
                owned = native.owned_native_join_sections(self.donors, arm, deck, native.APPROVED_INTERFACE_CELLS)
                self.assertEqual(len(raw), len(owned))
                for first, last in zip(raw, owned):
                    if 'source_interface_ownership_trace' not in last:
                        self.assertEqual(first, last)
        with self.assertRaisesRegex(ValueError, 'exact approved 21-cell mask'):
            native.ownership_join_trace_report(self.donors, native.APPROVED_INTERFACE_CELLS-{(-2, 1)})

    def test_removing_one_millimetre_inside_owned_peer_cap_still_fails(self):
        compiled = native.extrude_native_collars(self.donors)
        roles, materials = [], {}
        for row in compiled['groups']:
            role = f"{row['role']}-native-{row['arm']}-{row['deck']}-{row['kind']}"
            if role not in materials:
                roles.append(role); materials[role] = row['material']
        def faces(inside_deletion=False):
            result = []
            for row in compiled['groups']:
                role = f"{row['role']}-native-{row['arm']}-{row['deck']}-{row['kind']}"
                triangles = row['triangles']
                if row['arm'] in ('A', 'B') and row['kind'] == 'peer' and row['role'] == 'pavement':
                    boundary = -23.999 if inside_deletion and row['arm'] == 'A' and row['deck'] == 'upper' else -24.
                    triangles = [part for triangle in triangles
                                 for part in original_native._clip_coreward(triangle, boundary, 1)]
                result.extend(tuple((*p, float(roles.index(role))) for p in face) for face in triangles)
            return result
        exact = faces()
        report = native.native_join_audit(exact, roles, materials, self.donors,
                                         owned_cells=native.APPROVED_INTERFACE_CELLS)
        self.assertEqual(report['native_finite_segments_checked'], 86)
        self.assertEqual(len(report['source_interface_ownership']['traces']), 4)
        with self.assertRaisesRegex(ValueError, 'seam loses finite geometry, material, or UV'):
            native.native_join_audit(exact, roles, materials, self.donors)
        with self.assertRaisesRegex(ValueError, 'seam loses finite geometry, material, or UV'):
            native.native_join_audit(faces(inside_deletion=True), roles, materials, self.donors,
                                     owned_cells=native.APPROVED_INTERFACE_CELLS)


if __name__ == '__main__':
    unittest.main()
