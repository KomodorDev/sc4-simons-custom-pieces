"""Independent external socket, construction, and original-rule controls."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'framework'))
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0, SourcePackages(ROOT))

from scp import jsonc, native_approaches as shared
from scp.dbpf import entries, decompress
from scp.paths import local_settings
from scp_highway import y_junction_approaches as approaches


def specification(slug):
    from scp_highway.y_junction_layout import module_catalog
    types = module_catalog()['types']
    records = types.values() if isinstance(types, dict) else types
    record = next(record for record in records if record['id'] == slug)
    cells = [list(cell) for cell in record['cells']]
    return {'id': slug, 'domain': 'highway', 'recipe': record['recipe'],
            'cells': cells, 'footprint': list(record['footprint']),
            'tile_ids': [f'{0x7F600000 + cell[0] * 0x100 + cell[1] * 0x10:08x}' for cell in cells],
            'native_y_junction_approaches': True}


def core_fields(piece):
    width, depth = piece['footprint']
    rows = [['.'] * (width + 2) for _ in range(depth + 1)]
    cons = deepcopy(rows)
    checks = []
    for symbol, cell in zip('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', piece['cells']):
        x, y = cell
        rows[y][x], cons[y][x] = symbol, '+'
        checks.append(f'{symbol} - dirtroad: 0x02000200')
    rows[depth][0] = cons[depth][0] = '^'
    rows[0][width + 1] = cons[0][width + 1] = '<'
    return {'CellLayout': [''.join(row) for row in rows], 'ConsLayout': [''.join(row) for row in cons],
            'CheckType': checks, 'AutoTileBase': ['0x7F600000'], 'Piece': ['unchanged preview']}


def encoded_routes(routes):
    lines = ['SC4PATHS', '1.2', str(len(routes)), '0', '1']
    for route in routes:
        lines.extend(str(route[field]) for field in ('transport', 'lane', 'entry', 'exit', 'compatibility'))
        lines.append(str(len(route['points'])))
        lines.extend(','.join(str(value) for value in point) for point in route['points'])
    return ('\n'.join(lines) + '\n').encode('ascii')


def socket_fixture(piece):
    """Independent four-metre outer collars; no full-route claim is made."""
    rows = {
        'ddrhw-y-diagonal-stem-split': ((-1, 2), 0, [
            (0, True, (-24., -35.2, 15.), (1., 1.)),
            (1, True, (-24., -28.8, 15.), (1., 1.)),
            (0, False, (-24., -28.8, 7.5), (-1., -1.)),
            (1, False, (-24., -35.2, 7.5), (-1., -1.))]),
        'ddrhw-y-diagonal-branch': ((-1, -2), 0, [
            (0, False, (-24., 35.2, 15.), (-1., 1.)),
            (1, False, (-24., 28.8, 15.), (-1., 1.)),
            (0, True, (-24., 28.8, 7.5), (1., -1.)),
            (1, True, (-24., 35.2, 7.5), (1., -1.))]),
        'ddrhw-y-orthogonal-core': ((3, 0), 2, [
            (0, False, (56., -2.5, 15.), (1., 0.)),
            (1, False, (56., 2.5, 15.), (1., 0.)),
            (0, True, (56., 2.5, 7.5), (-1., 0.)),
            (1, True, (56., -2.5, 7.5), (-1., 0.))]),
    }
    owner, edge, values = rows[piece['id']]
    routes = []
    for lane, incoming, point, tangent in values:
        length = (tangent[0] ** 2 + tangent[1] ** 2) ** .5
        point = (point[0] - 16 * owner[0], point[1] + 16 * owner[1], point[2])
        sign = 1 if incoming else -1
        inner = (point[0] + sign * 4 * tangent[0] / length,
                 point[1] + sign * 4 * tangent[1] / length, point[2])
        routes.append({'transport': 1, 'lane': lane, 'compatibility': 0,
                       'entry': edge if incoming else (edge + 2) % 4,
                       'exit': (edge + 2) % 4 if incoming else edge,
                       'points': [point, inner] if incoming else [inner, point]})
    declaration = approaches.approaches(piece)[0]
    key = (0x296678F7, 0xA966883F, int(declaration['end_tile_id'], 16))
    return {key: encoded_routes(routes)}, key, routes


class YJunctionApproachTests(unittest.TestCase):
    def test_absent_and_false_are_inert_and_non_boolean_values_fail(self):
        for piece in ({}, {'native_y_junction_approaches': False}):
            self.assertEqual(approaches.approaches(piece), [])
            self.assertEqual(shared.approaches(piece), [])
        for value in (0, 1, None, 'true', [], {}):
            with self.subTest(value=value), self.assertRaises(ValueError):
                approaches.approaches({'native_y_junction_approaches': value})

    def test_owner_identity_cells_and_modes_fail_closed(self):
        piece = specification('ddrhw-y-diagonal-stem-split')
        changes = [('id', 'ddrhw-another'), ('recipe', 'highway_another'),
                   ('domain', 'high-speed-rail'), ('cells', piece['cells'][:-1]),
                   ('cells', list(reversed(piece['cells']))), ('footprint', [99, 99]),
                   ('tile_ids', ['bad'] * len(piece['cells'])), ('native_dd_approaches', True),
                   ('native_orthogonal_approaches', True), ('native_ghsr_approaches', True),
                   ('adaptive_ground', {'network': 'avenue'})]
        for name, value in changes:
            with self.subTest(field=name), self.assertRaises(ValueError):
                approaches.approaches({**piece, name: value})

    def test_three_independent_owners_have_exact_native_poses_and_resource_sets(self):
        rows = [approaches.approaches(specification(slug))[0] for slug in approaches.OWNERS]
        self.assertEqual([(row['native_tile_id'], row['native_rotation'], row['outward_edge']) for row in rows],
                         [('57530900', 0, 0), ('57530900', 3, 0), ('57530000', 3, 2)])
        self.assertEqual([row['networks'] for row in rows], [
            [{'name': 'monorail', 'flags': '01000400'}, {'name': 'dirtroad', 'flags': '03010000'}],
            [{'name': 'monorail', 'flags': '00010004'}, {'name': 'dirtroad', 'flags': '00030100'}],
            [{'name': 'monorail', 'flags': '00010004'}, {'name': 'dirtroad', 'flags': '00020002'}]])
        pieces = [specification(slug) for slug in approaches.OWNERS]
        self.assertEqual([len(shared.dependency_keys([piece])) for piece in pieces], [6, 6, 3])
        self.assertEqual(len(shared.dependency_keys(pieces)), 9)
        self.assertEqual([len(approaches.dependency_sha256(piece)) for piece in pieces], [6, 6, 3])
        sections = shared.expected_solution_sections(pieces)
        self.assertEqual(len(sections[approaches.SECTION]), 8)
        self.assertEqual(len(shared._existing_solution_sections(pieces)[approaches.SECTION]), 4)
        self.assertEqual({row[0] for row in sections[approaches.SECTION].values()}, {0x57530900, 0x57530000})

    def test_padding_roundtrip_and_helper_mutations(self):
        for slug in approaches.OWNERS:
            piece = specification(slug)
            old = core_fields(piece)
            rows, checks, cons = approaches.add_approaches(piece, old['CellLayout'], old['CheckType'], old['ConsLayout'])
            padded = {**old, 'CellLayout': rows, 'CheckType': checks, 'ConsLayout': cons}
            self.assertEqual(approaches.check_construction_approaches(padded, piece), old)
            self.assertEqual(sum(row.count('+') for row in cons), len(piece['cells']))
            declaration = approaches.approaches(piece)[0]
            left, top, _columns, _rows = approaches._extent(piece, declaration)
            x, y = declaration['cell'][0] + left, declaration['cell'][1] + top
            mutations = []
            for before, after in [(' optional', ''), ('0xFFFFFFFF', '0x00000000'), ('monorail:', 'road:')]:
                changed = deepcopy(padded)
                changed['CheckType'][-1] = changed['CheckType'][-1].replace(before, after)
                mutations.append(changed)
            changed = deepcopy(padded); line = list(changed['ConsLayout'][y]); line[x] = '+'; changed['ConsLayout'][y] = ''.join(line); mutations.append(changed)
            changed = deepcopy(padded); line = list(changed['CellLayout'][y]); line[x] = '.'; changed['CellLayout'][y] = ''.join(line); mutations.append(changed)
            changed = deepcopy(padded); changed['CheckType'].append(changed['CheckType'][-1]); mutations.append(changed)
            for index, changed in enumerate(mutations):
                with self.subTest(slug=slug, mutation=index), self.assertRaises(ValueError):
                    approaches.check_construction_approaches(changed, piece)

    def test_independent_saved_collars_and_bidirectional_native_propagation(self):
        for slug in approaches.OWNERS:
            piece = specification(slug)
            resources, _key, _routes = socket_fixture(piece)
            report = approaches.check_native_boundary_paths(None, piece, resources)
            self.assertEqual(report['boundary_members_checked'], 4)
            self.assertEqual(report['rotated_boundary_member_checks'], 16)
            self.assertEqual(report['native_continuation_member_checks'], 16)
            orders = {row['construction_order'] for row in report['oriented_propagation']}
            self.assertEqual(orders, {'inward', 'outward'})
            self.assertEqual({row['piece_rotation'] for row in report['oriented_propagation']}, {0, 1, 2, 3})
            self.assertFalse(report['in_game_dragging_tested'] or report['in_game_travel_tested'])

    def test_wrong_lane_height_direction_compatibility_and_short_collar_are_rejected(self):
        for slug in approaches.OWNERS:
            piece = specification(slug)
            resources, key, routes = socket_fixture(piece)
            mutations = []
            changed = deepcopy(routes); changed[0]['lane'] += 9; mutations.append(changed)
            changed = deepcopy(routes); changed[0]['compatibility'] = 1; mutations.append(changed)
            changed = deepcopy(routes); changed.pop(); mutations.append(changed)
            changed = deepcopy(routes); changed.append(deepcopy(changed[0])); mutations.append(changed)
            changed = deepcopy(routes); changed[0]['entry'], changed[0]['exit'] = changed[0]['exit'], changed[0]['entry']; mutations.append(changed)
            changed = deepcopy(routes); changed[0]['points'] = [(p[0], p[1], p[2] + .1) for p in changed[0]['points']]; mutations.append(changed)
            changed = deepcopy(routes)
            p, q = changed[0]['points']
            changed[0]['points'] = [p, tuple(p[i] + (q[i] - p[i]) / 4 for i in range(3))]
            mutations.append(changed)
            for index, changed in enumerate(mutations):
                with self.subTest(slug=slug, mutation=index), self.assertRaises(ValueError):
                    approaches.check_native_boundary_paths(None, piece, {**resources, key: encoded_routes(changed)})


class YNativePhysicalUtilityTests(unittest.TestCase):
    def test_entire_native_staircase_is_reserved_but_adjacent_shoulder_cells_are_available(self):
        from scp_highway.y_junction_native_models import check_reserved_native_corridor
        self.assertEqual(check_reserved_native_corridor([(-2, 1), (-2, -1), (-1, 2), (-1, -2), (3, 0)])[
            'native_outward_runs_checked'], 3)
        for cell in [(-2, 2), (-2, 3), (-102, 102), (-102, 103),
                     (-2, -2), (-2, -3), (-102, -102), (-102, -103), (4, 0), (100, 0)]:
            with self.subTest(cell=cell), self.assertRaisesRegex(ValueError, 'blocks a native outward continuation'):
                check_reserved_native_corridor([cell])

    def test_finite_plane_cut_interpolates_geometry_and_uv_without_extrapolation(self):
        from scp_highway.y_junction_native_models import _plane_segments
        triangle = ((-1., 0., 0., 0., 0.), (1., 0., 0., 2., 0.), (1., 2., 2., 2., 2.))
        segment = _plane_segments(triangle, 0.)[0]
        self.assertEqual(set(segment), {(0., 0., 0., 1., 0.), (0., 1., 1., 1., 1.)})
        self.assertEqual(_plane_segments(triangle, 2.), [])


class ActualNativeYJunctionApproaches(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        settings_path = local_settings(ROOT)
        if not settings_path.is_file():
            raise unittest.SkipTest('Original NAM 50 inputs are unavailable in this checkout')
        settings = jsonc.load(settings_path)
        roots = [Path(settings['plugins']).expanduser(), *(Path(value).expanduser() for value in settings.get('extra_plugins', []))]
        cls.donors = {}
        for label, name in (('controller', 'NetworkAddonMod_Controller.dat'), ('dd_rhw', 'RealHighway_DD_RHW-4.dat')):
            matches = {path for root in roots if root.is_dir() for path in root.rglob(name)}
            if len(matches) != 1:
                raise unittest.SkipTest('Exactly one original ' + name + ' is required')
            raw = next(iter(matches)).read_bytes()
            cls.donors[label] = {key: decompress(value) for key, value in entries(raw).items()}
        cls.flat = {key: value for resources in cls.donors.values() for key, value in resources.items()}

    def test_actual_resources_rules_dependencies_and_reversible_composition(self):
        report = approaches.check_native_continuation(self.donors['controller'])
        self.assertEqual(report['existing_native_rul1_solutions_checked'], 4)
        self.assertEqual(report['native_continuation_rows_checked'], 8)
        pieces = [specification(slug) for slug in approaches.OWNERS]
        self.assertEqual(len(shared.dependency_records(pieces, self.flat)), 9)
        original = self.flat[approaches.RUL1]
        result, proof = shared.compose_rul1(original, pieces, self.flat)
        self.assertEqual(proof['schema_version'], 3)
        self.assertEqual(sum(len(row['native_solutions']) for row in proof['sections']), 4)
        self.assertEqual(sum(len(row['native_solutions']) for row in proof['existing_native_solutions']), 4)
        report = shared.verify_rul1({approaches.RUL1: result}, pieces,
                                   {'native_dd_approaches': proof}, self.flat)
        self.assertEqual(report['native_dd_approach_cells_checked'], 3)
        self.assertEqual(report['native_dd_dependencies_checked'], 9)
        self.assertEqual(report['existing_native_rul1_solutions_reused'], 4)
        c_only, proof = shared.compose_rul1(original, [pieces[2]], self.flat)
        self.assertEqual(c_only, original)
        self.assertEqual(proof['sections'], [])

    def test_actual_native_boundary_and_inward_outward_rows_cover_each_owner(self):
        for slug in approaches.OWNERS:
            piece = specification(slug)
            resources, _key, _routes = socket_fixture(piece)
            report = approaches.check_native_boundary_paths(self.donors, piece, resources)
            self.assertTrue(report['native_controller_reread'])
            self.assertEqual(report['native_input_scope'], 'reread-pinned-native-resources')

    def test_foreign_continuation_model_path_or_exemplar_is_rejected(self):
        piece = specification('ddrhw-y-diagonal-stem-split')
        paths = {'controller': Path('original-controller.dat'), 'dd_rhw': Path('original-dd.dat')}
        installed = {key: [paths[label]] for label, resources in self.donors.items() for key in resources}
        for key in approaches.additional_dependency_keys(piece):
            changed = deepcopy(installed)
            changed[key] = [*changed[key], Path('foreign-override.dat')]
            with self.subTest(tgi=key), self.assertRaisesRegex(ValueError, 'Foreign or missing'):
                shared.audit_dependencies([piece], self.donors, changed, paths)

    def test_exact_finite_native_lofts_preserve_uvs_and_report_original_phase_overlap(self):
        from scp_highway import y_junction_native_models as native_models
        result = native_models.extrude_native_collars(self.donors)
        overlaps = result['projected_overlaps_requiring_partition']
        self.assertEqual({(row['arm'], row['deck']) for row in overlaps},
                         {('A', 'upper'), ('A', 'lower'), ('B', 'upper'), ('B', 'lower')})
        self.assertTrue(all(.0042 < row['area_m2'] < .0043 for row in overlaps))
        roles, materials, faces = ['pavement', 'body', 'barrier'], {}, []
        for group in result['groups']:
            role = group['role']
            materials.setdefault(role, group['material'])
            self.assertEqual(materials[role]['raw'], group['material']['raw'])
            faces.extend(tuple((*point, float(roles.index(role))) for point in triangle)
                         for triangle in group['triangles'])
        report = native_models.native_join_audit(faces, roles, materials, self.donors)
        self.assertEqual(report['native_finite_segments_checked'], 86)
        self.assertGreater(report['original_native_occluded_profile_length_m'], 0.)
        # A uniform wrong U offset changes lane markings and barrier appearance.
        altered = [tuple((*point[:3], point[3] + .1, *point[4:]) for point in face) for face in faces]
        with self.assertRaisesRegex(ValueError, 'geometry, material, or UV'):
            native_models.native_join_audit(altered, roles, materials, self.donors)
        repeated = []
        for group in result['groups']:
            if group['arm'] != 'C':
                continue
            uv_axis = 4 if group['role'] == 'pavement' else 3
            for triangle in group['triangles']:
                repeated.append(tuple(tuple(value + (1. if index == uv_axis else 0.)
                                            for index, value in enumerate(point))
                                      + (float(roles.index(group['role'])),) for point in triangle))
        phase = native_models.native_join_audit(repeated, roles, materials, self.donors, arms=['C'])
        self.assertTrue(phase['native_C_longitudinal_texture_repeat_offsets'])
        transverse = [tuple((point[0], point[1], point[2], point[3] + 1., point[4], point[5])
                            if round(point[5]) == 0 else point for point in face) for face in repeated]
        with self.assertRaisesRegex(ValueError, 'geometry, material, or UV'):
            native_models.native_join_audit(transverse, roles, materials, self.donors, arms=['C'])
        contact = native_models.retained_core_contact_faces(self.donors)
        self.assertEqual({(row['donor'], row['pose'], tuple(row['cell'])) for row in contact},
                         {('57530000', 3, (3, 0))})
        self.assertTrue(all(56. - 1e-12 <= point[0] <= 56.00100040435791 + 1e-12
                            for row in contact for fragment in row['fragments'] for point in fragment['triangle']))
        contact_faces = [tuple((*point, float(roles.index(group['role']))) for point in fragment['triangle'])
                         for group in contact for fragment in group['fragments']]
        # The retained outer edge is only 0.477 micrometres from the native
        # neighbour's plane. A raw-sign crossing after on-plane classification
        # would create spurious intersections 7.6 mm along this thin face.
        contact_report = native_models.native_join_audit(contact_faces, roles, materials, self.donors, arms=['C'])
        self.assertEqual(contact_report['native_finite_segments_checked'], 26)
        self.assertTrue(contact_report['native_C_longitudinal_texture_repeat_offsets'])

    def test_reader_certifies_only_finite_native_roles_and_supplies_exact_barrier_masks(self):
        from scp_highway import y_junction_native_models as native_models
        source = native_models.extrude_native_collars(self.donors)
        roles, materials, faces = [], {}, []
        for group in source['groups']:
            role = f"{group['role']}-native-{group['arm']}-{group['deck']}-{group['kind']}"
            if role not in materials:
                materials[role] = group['material']; roles.append(role)
            faces.extend(tuple((*point, float(roles.index(role))) for point in triangle) for triangle in group['triangles'])
        for group in native_models.retained_core_contact_faces(self.donors):
            role = f"{group['role']}-native-C-{group['deck']}-retained-contact"
            materials[role] = group['material']; roles.append(role)
            faces.extend(tuple((*point, float(roles.index(role))) for point in row['triangle']) for row in group['fragments'])
        report = native_models.certify_native_collars(faces, roles, materials, self.donors)
        self.assertEqual(report['native_faces_checked'], len(faces))
        self.assertEqual(len(report['internal_pavement_masks']), 12)
        self.assertTrue(all(value.area > 0 for value in report['internal_pavement_masks'].values()))
        mutations = []
        changed = deepcopy(faces)
        changed[0] = tuple((point[0], point[1] + .001, *point[2:]) for point in changed[0]); mutations.append(changed)
        changed = deepcopy(faces)
        changed[0] = tuple((*point[:3], point[3] + .1, *point[4:]) for point in changed[0]); mutations.append(changed)
        changed = deepcopy(faces); changed[0] = (changed[0][0], changed[0][2], changed[0][1]); mutations.append(changed)
        for index, changed in enumerate(mutations):
            with self.subTest(mutation=index), self.assertRaisesRegex(ValueError, 'pinned finite native'):
                native_models.certify_native_collars(changed, roles, materials, self.donors)
        generic = 'pavement-native-A-upper'
        roles.append(generic); materials[generic] = materials[roles[0]]
        extra = tuple((*point[:5], float(roles.index(generic))) for point in faces[0])
        report = native_models.certify_native_collars([*faces, extra], roles, materials, self.donors)
        self.assertEqual(report['generic_native_texture_face_indices_without_geometry_exception'], [len(faces)])
        literal = []
        for group in native_models.retained_core_collar_faces(self.donors):
            role = f"{group['role']}-native-C-{group['deck']}-retained-core-collar"
            materials[role] = group['material']; roles.append(role)
            literal.extend(tuple((*point, float(roles.index(role))) for point in row['triangle']) for row in group['fragments'])
        literal_report = native_models.certify_native_collars(literal, roles, materials, self.donors)
        self.assertEqual(literal_report['native_faces_checked'], len(literal))
        self.assertEqual(set(literal_report['internal_pavement_masks']),
                         {'pavement-native-C-upper-retained-core-collar', 'pavement-native-C-lower-retained-core-collar'})
        literal_seam = native_models.native_join_audit(literal, roles, materials, self.donors, arms=['C'])
        self.assertEqual(literal_seam['native_finite_segments_checked'], 26)
        self.assertTrue(literal_seam['native_C_longitudinal_texture_repeat_offsets'])

    def test_buried_peer_body_scope_is_finite_source_only_and_preserves_the_raised_strip(self):
        from scp_highway import y_junction_native_models as native_models
        source = native_models.extrude_native_collars(self.donors, arms=['A', 'B'])
        roles, materials, faces = [], {}, []
        for group in source['groups']:
            role = f"{group['role']}-native-{group['arm']}-{group['deck']}-{group['kind']}"
            materials[role] = group['material']; roles.append(role)
            faces.extend(tuple((*point, float(roles.index(role))) for point in triangle)
                         for triangle in group['triangles'])
        before = deepcopy(faces)
        report = native_models.certify_native_collars(faces, roles, materials, self.donors)
        regions = report['buried_peer_body_regions']
        self.assertEqual({(row['arm'], row['deck']) for row in regions},
                         {('A', 'upper'), ('A', 'lower'), ('B', 'upper'), ('B', 'lower')})
        pin = approaches.NATIVE_DEPENDENCY_SHA256[0x5ad0e817, 0xbadb57f1, 0x57530200]
        for row in regions:
            self.assertEqual(row['source_model_sha256'], pin)
            self.assertEqual(row['role'], f"body-native-{row['arm']}-{row['deck']}-peer")
            self.assertEqual(row['source_extrusion_length_m'], 3.)
            self.assertTrue(row['finite_source_footprint_and_height_containment_proved'])
            self.assertTrue(row['requires_independent_complete_shell_and_outer_wall_proof'])
            self.assertFalse(row['raised_native_strip_and_actual_saved_faces_changed'])
            nominal = 15. if row['deck'] == 'upper' else 7.5
            underside = 14.00100040435791 if row['deck'] == 'upper' else 6.500999927520752
            self.assertEqual(row['analysis_below_height_m'], nominal)
            self.assertEqual(row['underside_height_m'], underside)
            self.assertGreater(row['source_body_surface_area_below_floor_m2'], 0.)
            self.assertGreater(max(p[1] for p in faces[row['face_index']]), nominal)
        self.assertEqual(faces, before)
        # A generic body with identical material and vertices receives no
        # inherited-source scope, and neither do helper-body native roles.
        index = regions[0]['face_index']
        roles.append('body'); materials['body'] = materials[regions[0]['role']]
        generic = tuple((*point[:5], float(roles.index('body'))) for point in faces[index])
        extra = native_models.certify_native_collars([*faces, generic], roles, materials, self.donors)
        self.assertEqual(extra['buried_peer_body_regions'], regions)
        self.assertTrue(all('-peer' in row['role'] for row in extra['buried_peer_body_regions']))


if __name__ == '__main__':
    unittest.main()
