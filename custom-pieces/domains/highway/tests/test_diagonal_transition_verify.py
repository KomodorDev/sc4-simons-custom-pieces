"""Portable corruption controls for independent first-A diagonal readers.

The small fixture mask is synthetic, and is supplied only inside each test.
It cannot approve the unresolved production ownership or physical surfaces.
"""
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

from scp.connectivity import piece_connectivity
from scp.models import pack_s3d, parse_s3d
from scp.preview import decode_fsh
from scp.track_paths import PATH
from scp.verify import parse_paths
from scp_highway import diagonal_transition_verify as check
from scp_highway import diagonal_transition_models_verify as models


def encode(routes, *, elevation=1):
    lines = ['SC4PATHS', '1.2', str(len(routes)), '0', str(elevation)]
    for route in routes:
        lines.extend(str(route[k]) for k in ('transport', 'lane', 'entry', 'exit', 'compatibility'))
        lines.append(str(len(route['points'])))
        lines.extend(','.join(f'{v:.9f}'.rstrip('0').rstrip('.') if v else '0' for v in p)
                     for p in route['points'])
    return ('\n'.join(lines)+'\n').encode('ascii')


def fixture(variant='original'):
    world = check.expected_cell_routes(variant=variant, world=True)
    cells = set(world)
    extra = next((c[0]+dx, c[1]+dy) for c in sorted(cells) for dx, dy in ((1, 0), (0, 1))
                 if (c[0]+dx, c[1]+dy) not in cells)
    cells.add(extra)
    origin = min(x for x, y in cells), min(y for x, y in cells)
    local = sorted(((x-origin[0], y-origin[1]) for x, y in cells), key=lambda c: (c[1], c[0]))
    width, depth = max(x for x, y in local)+1, max(y for x, y in local)+1
    layout_grid = [['.']*(width+2) for _ in range(depth+1)]
    cons_grid = deepcopy(layout_grid)
    for i, (x, y) in enumerate(local):
        layout_grid[y][x] = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'[i]
        cons_grid[y][x] = '#'
    for grid in (layout_grid, cons_grid):
        grid[0][width+1] = '<'
        grid[depth][0] = '^'
    layout = {'world_origin_cell': origin, 'cells': local, 'footprint': (width, depth),
        'cell_layout': [''.join(r) for r in layout_grid],
        'cons_layout': [''.join(r) for r in cons_grid]}
    phase = check.PHASES[variant]
    piece = {'id': phase.piece_id, 'domain': 'highway', 'recipe': phase.recipe,
        'diagonal_transition_variant': variant, 'diagonal_transition_alignment': 'a',
        'cells': [list(c) for c in local], 'footprint': [width, depth],
        'tile_ids': [f'{0x7f600000+x*0x100+y*0x10:08x}' for x, y in local],
        'shadow_mappings': [], 'model_shadows': {'enabled': False},
        'engineering': {'model_only_cells': [[extra[0]-origin[0], extra[1]-origin[1]]],
            'max_grade_percent': 20., 'car_corridor_half_width_m': 1.25, 'car_corridor_height_m': 3.8}}
    with patch.object(check, 'REVIEWED_LAYOUTS', {variant: layout}):
        routes = check.expected_cell_routes(variant=variant)
        resources = {(*PATH, int(tile, 16)): encode(routes[tuple(cell)])
                     for cell, tile in zip(piece['cells'], piece['tile_ids'])}
        fields = {'CellLayout': layout['cell_layout'], 'ConsLayout': layout['cons_layout'],
            'Costs': ['1000'], 'CheckType': [layout['cell_layout'][y][x]+f' - dirtroad: 0x{check._construction_word(routes[x,y]):08x}'
                                           for x, y in local]}
    return piece, resources, fields, layout


class DiagonalIndependentPathTests(unittest.TestCase):
    def test_literal_native_endpoints_and_lane_classes_in_all_four_phases(self):
        expected_ground_zero = {'original': (-83.2, -56.), 'mirrored': (-44.8, -88.),
            'opposite-side': (-51.2, -88.), 'opposite-side-mirrored': (-76.8, -56.)}
        for key, (ground_e, ground_n) in expected_ground_zero.items():
            ports = check.external_ports(variant=key, world=True)
            self.assertEqual(len(ports), 8)
            upper = [p for p in ports if p['component'] == 'upper' and p['source_class'] == 0]
            dd = next(p for p in upper if p['point_m'][2] == 15.)
            ground = next(p for p in upper if p['point_m'][2] == 0.)
            self.assertAlmostEqual(dd['point_m'][0], 8.)
            self.assertAlmostEqual(dd['point_m'][1], -3.2 if check.PHASES[key].traffic_reversed else 3.2)
            self.assertAlmostEqual(ground['point_m'][0], ground_e)
            self.assertAlmostEqual(ground['point_m'][1], ground_n)
            self.assertEqual(dd['native_class'], 0)
            self.assertEqual(ground['native_class'], 1)
            self.assertEqual(dd['direction'], 'out' if check.PHASES[key].traffic_reversed else 'in')

    def test_four_encoded_journeys_and_all_proper_rotations(self):
        for key in check.PHASES:
            piece, resources, fields, layout = fixture(key)
            with patch.object(check, 'REVIEWED_LAYOUTS', {key: layout}):
                report = check.check_paths(resources, piece)
                self.assertEqual(report['complete_directed_journeys'], 4)
                self.assertEqual(report['complete_native_boundary_members_checked'], 8)
                self.assertEqual(report['route_fragments_checked'], 36)
                self.assertEqual(report['proper_rotations_checked'], 4)
                self.assertLess(report['maximum_grade_percent'], 20.)
                self.assertGreater(report['maximum_grade_percent'], 18.9)
                self.assertEqual(report['model_only_cells'], piece['engineering']['model_only_cells'])
                self.assertFalse(report['game_operation_tested'])

    def test_saved_connection_fields_match_shared_consumer_precision(self):
        for key in check.PHASES:
            piece, resources, _fields, layout = fixture(key)
            with patch.object(check, 'REVIEWED_LAYOUTS', {key: layout}):
                actual = piece_connectivity(piece, resources, contract=check.reviewed_contract(piece))
                expected = check.reviewed_facts(piece)
                self.assertEqual(len(actual['ports']), 8)
                by_id = {p['id']: p for p in actual['ports']}
                for wanted in expected['ports']:
                    measured = by_id[wanted['id']]
                    for field in ('direction', 'edge', 'endpoint_m', 'sampled_tangent', 'tangent', 'grade'):
                        self.assertEqual(measured[field], wanted[field], (key, field, wanted['id']))

    def test_changed_native_half_classes_missing_lane_and_bad_elevation_reject(self):
        for kind in ('class', 'missing', 'elevation', 'endpoint', 'reverse', 'extra'):
            piece, resources, _fields, layout = fixture()
            address = next(k for k, raw in resources.items() if parse_paths(raw)['routes'])
            parsed = parse_paths(resources[address])
            if kind == 'class':
                parsed['routes'][0]['lane'] += 10
            elif kind == 'missing':
                parsed['routes'].pop()
            elif kind == 'elevation':
                parsed['terrain'] = 0
            elif kind == 'endpoint':
                p = parsed['routes'][0]['points'][0]
                parsed['routes'][0]['points'][0] = (p[0]+.001, p[1], p[2])
            elif kind == 'reverse':
                parsed['routes'][0]['points'].reverse()
                row = parsed['routes'][0]
                row['entry'], row['exit'] = row['exit'], row['entry']
            else:
                parsed['routes'].append(deepcopy(parsed['routes'][0]))
            resources[address] = encode(parsed['routes'], elevation=parsed['terrain'])
            with self.subTest(kind=kind), patch.object(check, 'REVIEWED_LAYOUTS', {'original': layout}):
                with self.assertRaises(ValueError):
                    check.check_paths(resources, piece)

    def test_phase_identity_and_alignment_are_strict(self):
        piece, _resources, _fields, _layout = fixture()
        for field, value in (('diagonal_transition_variant', None), ('diagonal_transition_alignment', 'b'),
                             ('id', check.PHASES['mirrored'].piece_id), ('recipe', 'old-orthogonal-recipe')):
            bad = {**piece, field: value}
            with self.subTest(field=field), self.assertRaises(ValueError):
                check.phase_for_piece(bad)

    def test_grade_ceiling_cannot_be_relaxed(self):
        piece, resources, _fields, layout = fixture()
        piece['engineering']['max_grade_percent'] = 30.
        with patch.object(check, 'REVIEWED_LAYOUTS', {'original': layout}), self.assertRaisesRegex(ValueError, 'twenty-percent'):
            check.check_paths(resources, piece)

    def test_construction_checks_actual_routes_and_preserves_flat_sparse_core(self):
        piece, resources, fields, layout = fixture()
        with patch.object(check, 'REVIEWED_LAYOUTS', {'original': layout}):
            proof = check.check_construction_fields(fields, piece, resources)
            self.assertEqual(proof['inserted_equality_pairs'], 3*len(piece['cells']))
            self.assertEqual(proof['proper_rotations_checked'], 4)
            self.assertFalse(proof['absolute_world_height_fixed'])
            bad = deepcopy(fields)
            bad['CheckType'][0] = bad['CheckType'][0].split(':')[0]+': 0x00000000'
            with self.assertRaises(ValueError):
                check.check_construction_fields(bad, piece, resources)
            for symbol in ('+', '|', '.'):
                bad = deepcopy(fields)
                x, y = piece['cells'][0]
                row = list(bad['ConsLayout'][y]); row[x] = symbol
                bad['ConsLayout'][y] = ''.join(row)
                with self.assertRaises(ValueError):
                    check.check_construction_fields(bad, piece, resources)

    def test_registered_construction_dispatch_checks_helpers_before_the_owned_core(self):
        from scp import jsonc
        from scp.verify import check_emitted_runtime_addresses, parse_rules
        from scp_highway import diagonal_transition as writer
        from scp_highway import diagonal_transition_approaches as helpers
        from scp_highway import recipes, verify as domain_verify

        for key, phase in check.PHASES.items():
            with self.subTest(variant=key):
                piece = jsonc.load(ROOT/'domains/highway/00_pieces'/phase.piece_id/'piece.jsonc')
                expected = check.expected_cell_routes(variant=key)
                compiled = [(tuple(cell), b'', encode(expected[tuple(cell)])) for cell in piece['cells']]
                resources = {(*PATH, int(tile, 16)): raw
                             for tile, (_cell, _model, raw) in zip(piece['tile_ids'], compiled)}
                core = writer.construction_fields(piece, compiled)
                rows, palette, constraints = helpers.add_approaches(piece, *core)
                rings, sections = parse_rules(recipes.construction(piece, rows, palette, constraints))
                root = int(piece['puzzle_id'], 16)
                self.assertEqual(rings, [[root+turn*0x10000 for turn in range(8)]])
                self.assertEqual(set(sections), set(rings[0]))
                fields = {}
                for name, value in sections[root]:
                    fields.setdefault(name, []).append(value)

                addresses = check_emitted_runtime_addresses(fields, piece)
                self.assertEqual((addresses['cells_checked'], addresses['wrong_model_selections']), (24, 0))
                restored = helpers.check_construction_approaches(fields, piece)
                self.assertEqual(restored['CellLayout'], list(check.reviewed_layout(key)['cell_layout']))
                self.assertEqual(restored['ConsLayout'], list(check.reviewed_layout(key)['cons_layout']))
                self.assertEqual(len(restored['CheckType']), 24)
                # This direct call must still reject the full helper-bearing
                # fields: only the dispatch adapter may restore the core.
                with self.assertRaisesRegex(ValueError, 'accepted owners'):
                    check.check_construction_fields(fields, piece, resources)
                report = domain_verify.check_construction_fields(fields, piece, resources)
                expected_handle = [6, 1] if key in ('original', 'opposite-side-mirrored') else [5, 1]
                self.assertEqual(report['placement_handle_cell'], expected_handle)
                legacy = {name: value for name, value in fields.items() if name != 'HandleOffset'}
                self.assertNotIn('placement_handle_cell', domain_verify.check_construction_fields(legacy, piece, resources))
                self.assertEqual(report['native_diagonal_transition_outside_approaches_checked'], 3)
                self.assertEqual(report['occupied_cells_checked'], 24)
                self.assertEqual(report['inserted_equality_pairs'], 72)
                self.assertEqual([row['constrained_vertices'] for row in report['proper_rotations']], [39]*4)
                self.assertFalse(report['absolute_world_height_fixed'])

                for corruption in ('helper-mask', 'helper-owned', 'helper-constraint', 'padding', 'core-flat',
                                   'native-socket-handle', 'duplicate-handle'):
                    broken = deepcopy(fields)
                    if corruption == 'helper-mask':
                        broken['CheckType'][-1] = broken['CheckType'][-1].replace('0xFFFFFFFF', '0xFFFFFFFE')
                    elif corruption == 'helper-owned':
                        broken['CheckType'][-1] = broken['CheckType'][-1].replace(' optional', '')
                        with self.assertRaises(ValueError):
                            check_emitted_runtime_addresses(broken, piece)
                    elif corruption == 'helper-constraint':
                        symbol = broken['CheckType'][-1].split('-', 1)[0].strip()
                        y, x = next((y, line.index(symbol)) for y, line in enumerate(broken['CellLayout'])
                                    if symbol in line)
                        line = list(broken['ConsLayout'][y]); line[x] = '#'
                        broken['ConsLayout'][y] = ''.join(line)
                    elif corruption == 'padding':
                        for name in ('CellLayout', 'ConsLayout'):
                            broken[name].append('.'*len(broken[name][0]))
                    elif corruption == 'core-flat':
                        x, y = piece['cells'][0]
                        line = list(broken['ConsLayout'][y]); line[x] = '+'
                        broken['ConsLayout'][y] = ''.join(line)
                    elif corruption == 'native-socket-handle':
                        broken['HandleOffset'] = [f'{expected_handle[0] + 1}, 1']
                    else:
                        broken['HandleOffset'] *= 2
                    with self.subTest(corruption=corruption), self.assertRaises(ValueError):
                        domain_verify.check_construction_fields(broken, piece, resources)

    def test_all_corner_equality_graph_is_recomputed_for_the_actual_mask(self):
        cells = ((0, 0), (1, 0), (0, 1))
        for rotation in range(4):
            groups = check.terrain_vertex_components(cells, ('##', '#.'), rotation)
            self.assertEqual(len(groups), 1)
            self.assertEqual(len(groups[0]), 8)
        with self.assertRaises(ValueError):
            check.terrain_vertex_components(cells, ('#+', '#.'))

    def test_preallocation_guard_uses_independent_mask_not_author_flags(self):
        piece, _resources, _fields, layout = fixture()
        row = {**piece, 'world_origin_cell': layout['world_origin_cell']}
        with patch.object(check, 'REVIEWED_LAYOUTS', {'original': layout}):
            self.assertTrue(check.validate_layout_metadata(row)['accepted_for_allocation'])
            bad = deepcopy(row)
            bad['engineering']['physical_layout_reviewed'] = True
            bad['cells'].pop()
            with self.assertRaisesRegex(ValueError, 'finite ownership'):
                check.validate_layout_metadata(bad)
        with patch.object(check, 'REVIEWED_LAYOUTS', {}), self.assertRaisesRegex(ValueError, 'review is pending'):
            check.validate_layout_metadata(row)

    def test_all_eight_saved_native_members_and_wrong_phase_controls(self):
        from scp_highway import diagonal_transition_native as native
        def source(_context, tile, pose, cell):
            self.assertEqual(pose, 2)
            rows = []
            if tile >> 16 == 0x5753:
                incoming = tile == 0x57530900
                for height, upper in ((15., True), (7.5, False)):
                    for lane in (0, 1):
                        ends = ((8., 3.2, height), (8., -3.2, height)) if upper == incoming else (
                            (8., -3.2, height), (8., 3.2, height))
                        endpoint = ends[lane]
                        far = (endpoint[0]+8.-endpoint[1], 8., height)
                        points = [far, endpoint] if upper == incoming else [endpoint, far]
                        rows.append({'transport': 1, 'lane': lane, 'compatibility': 0,
                            'entry': 1 if upper == incoming else 0,
                            'exit': 0 if upper == incoming else 1, 'points': points})
            else:
                cx, cy = 16.*cell[0], -16.*cell[1]+8.
                sw = tile == 0x57030900
                for lane in (1, 2):
                    endpoint = (cx+(-3.2 if lane == 1 else 3.2)*(1. if sw else -1.), cy, 0.)
                    far = (cx-8., cy-(cx-8.-endpoint[0])*-1., 0.)
                    points = [endpoint, far] if sw else [far, endpoint]
                    rows.append({'transport': 1, 'lane': lane, 'compatibility': 0,
                        'entry': 1 if sw else 0, 'exit': 0 if sw else 1, 'points': points})
            return rows
        for key in check.PHASES:
            piece, resources, _fields, layout = fixture(key)
            with patch.object(check, 'REVIEWED_LAYOUTS', {key: layout}), patch.object(native, 'source_paths', side_effect=source):
                proof = check.check_native_boundaries({}, piece, resources)
                self.assertEqual(proof['directed_native_comparisons'], 32)
                self.assertFalse(proof['native_dragging_game_tested'])
            def wrong(*args):
                rows = source(*args)
                p = rows[0]['points'][0]
                rows[0]['points'][0] = (p[0]+.1, p[1], p[2])
                return rows
            with patch.object(check, 'REVIEWED_LAYOUTS', {key: layout}), patch.object(native, 'source_paths', side_effect=wrong):
                with self.assertRaises(ValueError):
                    check.check_native_boundaries({}, piece, resources)

    def test_actual_pinned_native_path_facts_work_without_private_archives(self):
        for key in check.PHASES:
            piece, resources, _fields, layout = fixture(key)
            with patch.object(check, 'REVIEWED_LAYOUTS', {key: layout}):
                proof = check.check_native_boundaries(None, piece, resources)
                self.assertTrue(proof['native_source_pins_enforced'])
                self.assertEqual(proof['directed_native_comparisons'], 32)


class DiagonalFiniteSurfaceTests(unittest.TestCase):
    @staticmethod
    def triangle(points=((0., 0., 5.), (1., 0., 5.), (0., 1., 5.))):
        raw = b'finite material test'
        return {'role': 'pavement', 'points': points, 'uv': ((0., 0.), (1., 0.), (0., 1.)),
            'texture': 1, 'material': {'raw': raw}, 'material_sha256': hashlib.sha256(raw).hexdigest()}

    def test_finite_distance_does_not_extrapolate_a_plane(self):
        parent = self.triangle()['points']
        self.assertAlmostEqual(models._point_triangle_distance((.2, .2, 5.000002), parent), .000002)
        self.assertGreater(models._point_triangle_distance((2., 2., 5.), parent), 2.)

    def test_missing_uv_material_winding_and_interior_duplicates_reject(self):
        parent = self.triangle()
        self.assertTrue(models.check_face_partition([parent], [parent])['passed'])
        for kind in ('missing', 'uv', 'material', 'winding', 'duplicate'):
            actual = deepcopy(parent)
            if kind == 'uv': actual['uv'] = ((0., 0.), (0., 1.), (1., 0.))
            if kind == 'material': actual['material']['raw'] = b'wrong material'
            if kind == 'winding':
                actual['points'] = tuple(reversed(actual['points']))
                actual['uv'] = tuple(reversed(actual['uv']))
            if kind == 'missing': actual = []
            elif kind == 'duplicate': actual = [actual, deepcopy(actual)]
            else: actual = [actual]
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                models.check_face_partition(actual, [parent])

    def test_nine_micrometre_finite_hole_rejects_without_area_exemption(self):
        parent = self.triangle()
        child = deepcopy(parent)
        child['points'] = ((.000009, 0., 5.), (1., 0., 5.), (.000009, .999991, 5.))
        child['uv'] = ((.000009, 0.), (1., 0.), (.000009, .999991))
        with self.assertRaisesRegex(ValueError, 'missing finite'):
            models.check_face_partition([child], [parent])

    def test_interior_thin_duplicate_is_not_a_finite_edge_contact(self):
        parent = self.triangle()
        sliver = deepcopy(parent)
        sliver['points'] = ((.2, .2, 5.), (.8, .2, 5.), (.2, .200003, 5.))
        sliver['uv'] = tuple(p[:2] for p in sliver['points'])
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            models.check_face_partition([parent, sliver], [parent])

    def test_distance_budget_is_one_euclidean_bound(self):
        triangle = self.triangle()['points']
        actual = models._point_triangle_distance((-.0000029, .2, 5.0000029), triangle)
        self.assertGreater(actual, models.POSITION_EPS)
        self.assertAlmostEqual(actual, math.sqrt(2.)*.0000029)

    def test_production_model_gate_cannot_accept_an_unreviewed_mask(self):
        piece, resources, _fields, layout = fixture()
        with patch.object(check, 'REVIEWED_LAYOUTS', {'original': layout}), patch.object(models,'REVIEWED_SURFACES',{}):
            with self.assertRaisesRegex(ValueError, 'review is pending'):
                models.check_models(resources, piece)

    def test_fourteen_whole_support_prisms_and_missing_face_control(self):
        raw = b'synthetic support material'
        fingerprint = hashlib.sha256(raw).hexdigest()
        with patch.object(models, 'BODY_MATERIAL_SHA256', fingerprint):
            faces = []
            for solid in models.support_contract():
                faces.extend({**face, 'material': {'raw': raw}}
                             for face in models._prism_faces(solid, solid['id']))
            proof = models.check_support_solids(faces)
            self.assertEqual(proof['complete_closed_support_solids'], 14)
            self.assertEqual(proof['actual_saved_support_triangles_checked'], 168)
            self.assertFalse(proof['structural_capacity_tested'])
            for kind in ('missing', 'winding', 'displaced'):
                bad = deepcopy(faces)
                if kind == 'missing': bad.pop(0)
                elif kind == 'winding': bad[0]['points'] = tuple(reversed(bad[0]['points']))
                else:
                    point = bad[0]['points'][0]
                    bad[0]['points'] = ((point[0]+.01, *point[1:]), *bad[0]['points'][1:])
                with self.subTest(kind=kind), self.assertRaises(ValueError):
                    models.check_support_solids(bad)

    def test_encoded_s3d_and_fsh_markings_stay_driver_left_in_four_rotations(self):
        from PIL import Image
        image = Image.new('RGBA', (128, 128), (50, 50, 50, 255))
        for x in range(13, 20):
            for y in range(128):
                image.putpixel((x, y), (240, 205, 0, 255))
        pixels = image.tobytes('raw', 'BGRA')
        size = 16+len(pixels)
        fsh = (struct.pack('<4sII4s4sI', b'SHPI', 24+size, 1, b'GIMX', b'0000', 24)
               +struct.pack('<I6H', (size << 8)|0x7d, 128, 128, 0, 0, 0, 0)+pixels)
        images = {1: decode_fsh(fsh)}
        material = (struct.pack('<IBBBBHIBB', 0, 0, 0, 0, 0, 0, 0, 0, 1)
                    +struct.pack('<IBBBBHHB', 1, 0, 0, 0, 0, 0, 0, 1)+b'\0')
        quad = ((-8., 0., 5., 0., 0.), (8., 0., 5., 1., 0.),
                (8., 10., 5., 1., 1.), (-8., 10., 5., 0., 1.))
        for rotation in range(4):
            posed = [(*check._rotate(p[:3], rotation), *p[3:]) for p in quad]
            model = {'version': (1, 5),
                'vertices': [{'flags': 0, 'format': 2, 'stride': 20,
                    'data': b''.join(struct.pack('<5f', p[0], p[2], -p[1], p[3], p[4]) for p in posed)}],
                'indices': [{'flags': 0, 'stride': 2, 'values': (0, 1, 2, 0, 2, 3)}],
                'primitives': [[(0, 0, 6)]], 'materials': [{'raw': material, 'textures': [1]}],
                'anim_header': struct.pack('<H', 1)+bytes(12),
                'meshes': [{'name': (models.PREFIX+'upper-pavement\0').encode('ascii'),
                            'flags': 0, 'frames': [(0, 0, 0, 0)]}],
                'trailing': []}
            journey = {'id': 'actual-upper', 'component': 'upper',
                'points': [check._rotate((0., 0., 5.), rotation), check._rotate((0., 10., 5.), rotation)]}
            raw = pack_s3d(model)
            proof = models.check_driver_left_markings(models.decode_faces(raw), [journey], images,
                                                      {'upper': {'upper-pavement'}})
            self.assertEqual(proof['actual_saved_pixel_samples_checked'], 5)
            bad = parse_s3d(raw)
            data = bytearray(bad['vertices'][0]['data'])
            for at in range(0, len(data), 20):
                u, = struct.unpack_from('<f', data, at+12)
                struct.pack_into('<f', data, at+12, 1.-u)
            bad['vertices'][0]['data'] = bytes(data)
            with self.assertRaisesRegex(ValueError, 'driver left'):
                models.check_driver_left_markings(models.decode_faces(pack_s3d(bad)), [journey], images,
                                                  {'upper': {'upper-pavement'}})

    def test_actual_opposite_bottom_diagonal_depth_regression(self):
        # Measured62.125..62.25m middle band. The wrong bottom diagonal
        # removes373.354331µm of real slab depth at their finite intersection.
        quad = ((-52.29825511949323, -26.803081002033405, 5.032905319483615),
                (-51.64844382560164, -27.870903685034165, 5.032905319483615),
                (-51.76121147413592, -27.93979854776997, 5.010037891873878),
                (-52.41476617924427, -26.87426288556493, 5.010037891873878))
        roofs = [{'points': tuple(quad[i] for i in indices)} for indices in ((0, 1, 2), (0, 2, 3))]
        for face in roofs:
            if models._normal(face['points'])[2] < 0.:
                face['points'] = tuple(reversed(face['points']))
        def floors(indices):
            result = []
            for selected in indices:
                points = tuple((*quad[i][:2], quad[i][2]-1.) for i in selected)
                if models._normal(points)[2] > 0.:
                    points = tuple(reversed(points))
                result.append({'role': 'upper-body', 'points': points})
            return result
        correct = floors(((0, 1, 2), (0, 2, 3)))
        self.assertTrue(models.check_slab_depth(roofs, correct)['passed'])
        for bad in (floors(((1, 0, 3), (1, 3, 2))), correct[:1],
                    [{**f, 'points': tuple((p[0], p[1], p[2]-.1) for p in f['points'])} for f in correct]):
            with self.assertRaisesRegex(ValueError, 'underside'):
                models.check_slab_depth(roofs, bad)

    def test_ground_clamp_has_real_floors_for_every_positive_depth(self):
        roofs = [{'points': ((0., 0., 1.), (1., 0., .5), (0., 1., .1))}]
        floor = {'role': 'lower-body', 'points': ((0., 1., 0.), (1., 0., 0.), (0., 0., 0.))}
        proof = models.check_slab_depth(roofs, [floor])
        self.assertEqual(proof['borrowed_native_floors'], 0)
        self.assertTrue(proof['passed'])
        for role in ('lower-pier-48-1', 'native-reference'):
            with self.assertRaisesRegex(ValueError, 'no actual authored'):
                models.check_slab_depth(roofs, [{**floor, 'role': role}])

    def test_atlas_material_substitution_preserves_every_other_source_byte(self):
        parent = self.triangle()
        source = b'fixed shader settings'+struct.pack('<I', 0x5703000E)+b'fixed wrapping'
        parent.update(texture=0x7f6ff300, material_sha256=hashlib.sha256(source).hexdigest(),
                      source_material_texture=0x5703000E)
        actual = deepcopy(parent)
        actual['material']['raw'] = source.replace(struct.pack('<I', 0x5703000E), struct.pack('<I', 0x7f6ff300))
        self.assertTrue(models.check_face_partition([actual], [parent])['passed'])
        actual['material']['raw'] += b'changed culling'
        with self.assertRaisesRegex(ValueError, 'material'):
            models.check_face_partition([actual], [parent])

    def test_middle_contract_has_matching_floors_and_no_zero_depth_underside(self):
        with patch.object(models, 'middle_stations', return_value=(62.125, 62.25)):
            faces, base = models.middle_surface_contract(0x7f6ff300)
        floors = [f for f in faces if f['role'].endswith('-body') and models._normal(f['points'])[2] < 0.]
        self.assertTrue(models.check_slab_depth(base, floors)['passed'])
        start = check.FLAT_ENVELOPE+check.CURVE_RUN+.25
        with patch.object(models, 'middle_stations', return_value=(start, start+.125)):
            faces, _base = models.middle_surface_contract(0x7f6ff300)
        self.assertFalse(any(f['role'] == 'lower-body' for f in faces))
        self.assertTrue(any(f['role'] == 'lower-pavement-atlas' for f in faces))
        extra = {'role': 'lower-body', 'points': ((-60., -70., 0.), (-60., -69., 0.), (-59., -70., 0.)),
                 'uv': ((0., 0.), (0., 1.), (1., 0.)), 'texture': 0x5EB4BEEE, 'material': {'raw': b''}}
        with patch.object(models, '_material_fingerprint', side_effect=lambda _a, p: p['material_sha256']):
            actual = [{**f, 'material': {'raw': b''}} for f in faces]
            with self.assertRaisesRegex(ValueError, 'finite source surface'):
                models.check_face_partition([*actual, extra], faces)

    def test_finite_edge_endpoint_caps_include_real_saved_dd_t_junction(self):
        first=((3.655456066131592,-9.312310695648193,7.495886325836182),
            (6.176990509033203,-11.965572357177734,7.494894981384277),
            (6.242854118347168,-11.89970874786377,7.495886325836182))
        second=((5.193669319152832,-10.805474758148193,7.4962053298950195),
            (6.242708683013916,-11.899563789367676,7.495886325836182),
            (6.265206336975098,-11.877011775970459,7.4962053298950195))
        faces=[{'role':name,'points':points,'kind':'pavement'}
            for name,points in (('middle',first),('dd-bridge',second))]
        proof=models.check_surface_contacts(faces)
        self.assertEqual(proof['finite_edge_contacts_checked'],1)
        self.assertLess(proof['maximum_finite_edge_distance_m'],.338e-6)
        # A thin interior duplicate cannot use a remote edge merely because
        # its area is small. A finite edge endpoint cannot act as an infinite
        # line either, and physical displacement still has one4µm budget.
        for triangle in (((0.,0.,0.),(10.,0.,0.),(0.,10.,0.)),):
            interior=((1.,1.,0.),(2.,1.,0.),(1.,1.+3e-6,0.))
            self.assertFalse(models.finite_edge_contact(interior,triangle,interior))
        segment_triangle=((0.,0.,0.),(1.,0.,0.),(0.,1.,0.))
        self.assertFalse(models.finite_edge_contact(((1.+9e-6,0.,0.),),segment_triangle,segment_triangle))
        self.assertFalse(models.finite_edge_contact(((.5,3e-6,3e-6),),segment_triangle,segment_triangle))

    def test_multi_child_finite_capsules_cover_city_cut_rounding_only(self):
        parent=((0.,0.,0.),(10.,0.,0.),(0.,1.,0.))
        region=((0.,0.,0.),(10.,0.,0.),(0.,.1e-6,0.))
        children=(((0.,.1e-6,0.),(5.,.1e-6,0.),(0.,1.,0.)),
            ((5.,.1e-6,0.),(10.,.1e-6,0.),(0.,1.,0.)))
        self.assertTrue(models._finite_triangle_union_covers(region,parent,children))
        for displacement in ((0.,9e-6,0.),(0.,3e-6,3e-6)):
            bad=[tuple(tuple(p[i]+displacement[i] for i in range(3)) for p in t) for t in children]
            self.assertFalse(models._finite_triangle_union_covers(region,parent,bad))

    def test_integral_barrier_height_uses_exact_finite_source_prism(self):
        roof=((0.,0.,15.),(1.,0.,16.),(0.,1.,15.))
        self.assertEqual(models._point_triangular_slab_distance((.3,.1,15.298),roof,14.),0.)
        self.assertGreater(models._point_triangular_slab_distance((.3,.1,15.31),roof,14.),.005)
        self.assertGreater(models._point_triangular_slab_distance((-3e-6,.2,15.+3e-6),roof,14.),4e-6)
        self.assertGreater(models._point_triangular_slab_distance((.3,.1,14.-9e-6),roof,14.),4e-6)

    def test_alternate_planar_triangulation_keeps_one_finite_attribute_proof(self):
        raw=b'finite planar grid fixture';pin=hashlib.sha256(raw).hexdigest()
        def face(points):
            return {'role':'pavement','points':tuple(points),'uv':tuple((p[0]/2.,p[1])for p in points),
                'texture':1,'material':{'raw':raw},'material_sha256':pin}
        expected=[]
        for a,b in ((0.,1.),(1.,2.)):
            expected.extend((face(((a,0.,5.),(b,0.,5.),(b,1.,5.))),
                face(((a,0.,5.),(b,1.,5.),(a,1.,5.)))))
        actual=[face(((0.,0.,5.),(2.,0.,5.),(0.,1.,5.))),face(((2.,0.,5.),(2.,1.,5.),(0.,1.,5.)))]
        self.assertTrue(models.check_face_partition(actual,expected)['passed'])
        self.assertTrue(models.check_symmetric_mesh_fields(actual,expected)['passed'])
        with self.assertRaisesRegex(ValueError,'duplicate'):
            models.check_symmetric_mesh_fields([*actual,actual[0]],expected)
        bad=deepcopy(actual);bad[0]['uv']=tuple((u+.01,v)for u,v in bad[0]['uv'])
        with self.assertRaisesRegex(ValueError,'finite source surface'):
            models.check_face_partition(bad,expected)

    def test_finite_diagonal_native_fields_retain_both_signed_halves(self):
        for variant in check.PHASES:
            fields=models.native_atlas_fields(variant)
            for deck in ('upper','lower'):
                slopes=[row['dUV_d_station_m'][1]for row in fields[deck]['dd']]
                self.assertTrue(any(abs(v-.0625)<1e-6 for v in slopes))
                self.assertTrue(any(abs(v+.0625)<1e-6 for v in slopes))
                self.assertTrue(any(abs(row['dUV_d_station_m'][0])>1e-4 for row in fields[deck]['ground']))
                # Source origins also differ: retaining a sign alone cannot
                # replace each finite original parent's measured UV phase.
                self.assertGreater(len({round(row['UV_at_first_lateral'][1],5)
                    for row in fields[deck]['dd']}),1)

    def test_real_source_phase_corner_requires_same_finite_oriented_cap(self):
        lower_points=((8.,7.999999523162842,15.),(8.,8.,15.),
            (-2.1213204860687256,-2.1213204860687256,15.))
        upper_height=15.+models.DATUM['upper']
        higher_points=((8.,8.,upper_height),(7.99999952402658,8.,upper_height),
            (8.,7.999999524026169,upper_height))
        low={'role':'dd-upper-pavement-native-profile-loft-00','points':lower_points,
            'uv':((.8535529971122742,1.5),(.8535529971122742,1.5),(.8535529971122742,.6053934693336487)),
            'texture':0x5713000E,'material':{'raw':b'synthetic phase shader'},'deck':'upper','kind':'pavement'}
        high={'role':'native-reference-dd-upper-pavement-fixture','points':higher_points,
            'uv':((0.,0.),)*3,'texture':0x5713000E,'deck':'upper','kind':'pavement',
            'native_reference':True,'source':{'native_tile_id':'57530900'}}
        cap_points=((8.,7.999999523162842,15.),(8.,8.,upper_height),(8.,8.,15.))
        cap={'role':'dd-upper-body-authored-DD-roof-phase-step-32','points':cap_points,
            'uv':tuple((p[0]/8.,p[1]/8.)for p in cap_points),'texture':0x5EB4BEEE,
            'material':{'raw':b'synthetic concrete shader'},'deck':'upper','kind':'body'}
        xy=((8.,7.999999524026169),(7.9999997620131875,7.9999997620131875),(8.,8.))
        a=tuple((*p,15.)for p in xy);b=tuple((*p,upper_height)for p in xy)
        # Source shader payloads remain private. This geometry unit supplies
        # explicit stand-ins; separate saved-material tests reject changes.
        with patch.object(models,'_material_fingerprint',side_effect=lambda face,parent:
                parent.get('material_sha256',models.BODY_MATERIAL_SHA256)):
            self.assertTrue(models._incident_native_phase_cap(a,b,low,high,[cap],'mirrored'))
            for wrong in ([],[{**cap,'role':'dd-upper-body-authored-DD-exposed-wall-32'}],
                    [{**cap,'points':tuple(reversed(cap['points'])),'uv':tuple(reversed(cap['uv']))}],
                    [{**cap,'points':tuple((p[0]+.002,p[1],p[2])for p in cap['points']),
                        'uv':tuple(((p[0]+.002)/8.,p[1]/8.)for p in cap['points'])}],
                    [{**cap,'points':tuple((p[0],p[1],p[2]+.002)for p in cap['points'])}]):
                self.assertFalse(models._incident_native_phase_cap(a,b,low,high,wrong,'mirrored'))
            wide=tuple((p[0]-.00001,p[1],p[2])for p in a)
            self.assertFalse(models._incident_native_phase_cap(wide,b,low,high,[cap],'mirrored'))


if __name__ == '__main__':
    unittest.main()
