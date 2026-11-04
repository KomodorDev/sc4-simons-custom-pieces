"""Mutation controls for actual saved Y-junction resources."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT/'framework'), str(ROOT/'domains/highway/implementation')]
from scp.dbpf import entries, decompress, pack_dbpf
from scp import jsonc
from scp.track_paths import PATH
from scp.verify import parse_paths
from scp_highway import ramp_paths as path_writer
from scp_highway import y_junction_verify as independent
from scp_highway import y_junction_layout as layout_writer
from scp_highway import y_junction_models_verify as models


def saved_path_fixture():
    """Use the existing generic PATH writer, independently of the Y checker."""
    source = independent._source()
    records = path_writer.slice_routes([
        {'id': name, 'points': source['routes'][name],
         'lane': source['route_metadata'][name]['from_lane']} for name in independent.NAMES])
    specifications, resources = [], {}
    for index, declaration in enumerate(layout_writer.module_catalog()['types']):
        key = declaration['geometry_key']
        world = list(map(tuple, declaration['world_cells']))
        origin = [min(cell[k] for cell in world) for k in range(2)]
        cells = [[cell[0]-origin[0], cell[1]-origin[1]] for cell in world]
        base = 0x5F900000+index*0x1000
        tiles = [f'{base+x*0x100+y*0x10:08x}' for x, y in cells]
        piece = {'id': 'ddrhw-'+key, 'domain': 'highway',
                 'recipe': 'highway_ddrhw_'+key.replace('-', '_'), 'geometry_key': key,
                 'cells': cells, 'tile_ids': tiles,
                 'footprint': [max(c[0] for c in cells)+1, max(c[1] for c in cells)+1],
                 'engineering': {'world_origin_cell': origin,
                                 'model_only_cells': [cell for cell, full in zip(cells, world) if full not in records],
                                 'max_grade_percent': 30., 'car_corridor_half_width_m': 1.25,
                                 'car_corridor_height_m': 3.8},
                 'shadow_mappings': [], 'model_shadows': {'enabled': False}}
        assets = {}
        for cell, tile in zip(world, tiles):
            raw = path_writer.encode_paths(records.get(cell, []), allow_empty=True)
            lines = raw.decode('ascii').splitlines()
            lines[4] = '1'
            assets[*PATH, int(tile, 16)] = ('\r\n'.join(lines)+'\r\n').encode('ascii')
        specifications.append(piece)
        resources[piece['id']] = {key: decompress(value) for key, value in entries(pack_dbpf(assets)).items()}
    return specifications, resources


class YJunctionSavedPathTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pieces, cls.resources = saved_path_fixture()

    def test_actual_encoded_paths_match_independent_cuts_and_four_rotations(self):
        for piece in self.pieces:
            with self.subTest(piece=piece['id']):
                result = independent.check_paths(self.resources[piece['id']], piece)
                self.assertTrue(result['passed'])
                self.assertEqual(len(result['proper_rotations']), 4)
                self.assertTrue(result['use_path_elevation'])
                self.assertFalse(result['game_operation_tested'])

    def test_saved_height_retention_cannot_be_disabled(self):
        piece = self.pieces[0]
        resources = dict(self.resources[piece['id']])
        key = next(iter(resources))
        lines = resources[key].decode('ascii').splitlines()
        lines[4] = '0'
        resources[key] = ('\r\n'.join(lines)+'\r\n').encode('ascii')
        with self.assertRaisesRegex(ValueError, 'retain authored elevated traffic heights'):
            independent.check_paths(resources, piece)

    def test_saved_interior_lane_displacement_is_rejected(self):
        piece = self.pieces[0]
        resources = dict(self.resources[piece['id']])
        key = next(key for key, raw in resources.items() if b'-- SCP ' in raw)
        raw = resources[key].decode('ascii')
        lines = raw.splitlines()
        coordinate = next(index for index, line in enumerate(lines) if ',' in line)
        point = list(map(float, lines[coordinate+1].split(',')))
        point[0] += .01
        lines[coordinate+1] = ','.join(map(str, point))
        resources[key] = ('\r\n'.join(lines)+'\r\n').encode('ascii')
        with self.assertRaisesRegex(ValueError, 'independently cut source route'):
            independent.check_paths(resources, piece)

    def test_each_component_exports_only_its_intrinsic_journeys(self):
        for piece in self.pieces:
            facts = independent.reviewed_facts(piece)
            self.assertEqual(len(facts['ports']), 2*len(facts['movements']))
            self.assertTrue(facts['forbidden_transfers'])
            self.assertEqual(facts['path_hashes_by_cell'], [])
            for entry, exit_ in facts['movements']:
                self.assertTrue(entry.endswith('-in'))
                self.assertTrue(exit_.endswith('-out'))

    def test_missing_real_route_cannot_be_replaced_by_capacity_metadata(self):
        piece = self.pieces[0]
        resources = dict(self.resources[piece['id']])
        key = next(key for key, raw in resources.items() if b'-- SCP ' in raw)
        lines = resources[key].decode('ascii').splitlines()
        first_route = next(index for index, line in enumerate(lines) if line.startswith('-- SCP '))
        lines[first_route+1] = '2'
        resources[key] = ('\r\n'.join(lines)+'\r\n').encode('ascii')
        with self.assertRaisesRegex(ValueError, 'independently cut source route'):
            independent.check_paths(resources, piece)

    def test_model_only_declaration_cannot_hide_a_routed_cell(self):
        piece = deepcopy(self.pieces[0])
        piece['engineering']['model_only_cells'] = [piece['cells'][0]]
        with self.assertRaisesRegex(ValueError, 'model-only cells'):
            independent.check_paths(self.resources[piece['id']], piece)

    def test_warm_expectations_recheck_revoked_review_and_changed_source_bytes(self):
        piece = next(piece for piece in self.pieces if piece['geometry_key'] == independent.KEYS[2])
        original_geometry = (independent.SUBJECT/'evidence/design-geometry.jsonc').read_bytes()
        original_review = (independent.SUBJECT/'evidence/source-verification.jsonc').read_bytes()
        with TemporaryDirectory() as folder:
            subject = Path(folder)
            evidence = subject/'evidence'
            evidence.mkdir()
            geometry_path = evidence/'design-geometry.jsonc'
            review_path = evidence/'source-verification.jsonc'
            geometry_path.write_bytes(original_geometry)
            review_path.write_bytes(original_review)
            with patch.object(independent, 'SUBJECT', subject):
                before = independent._expected_world()
                self.assertTrue(independent.check_paths(self.resources[piece['id']], piece)['passed'])
                review = jsonc.loads(original_review.decode('utf-8'))
                review['passed'] = False
                review_path.write_text(json.dumps(review))
                for read in (independent._source, independent._expected_world):
                    with self.subTest(reader=read.__name__):
                        with self.assertRaisesRegex(ValueError, 'matching independent source review'):
                            read()
                with self.assertRaisesRegex(ValueError, 'matching independent source review'):
                    independent.check_paths(self.resources[piece['id']], piece)

                geometry = jsonc.loads(original_geometry.decode('utf-8'))
                route = geometry['routes']['A-B']
                route[len(route)//2][0] += .01
                changed = json.dumps(geometry).encode('utf-8')
                geometry_path.write_bytes(changed)
                review['passed'] = True
                review['source']['design_geometry_sha256'] = hashlib.sha256(changed).hexdigest()
                review_path.write_text(json.dumps(review))
                self.assertEqual(set(independent._source()['routes']), set(independent.NAMES))
                self.assertNotEqual(independent._expected_world(), before)
                with self.assertRaisesRegex(ValueError, 'independently cut source route'):
                    independent.check_paths(self.resources[piece['id']], piece)

    def test_cached_source_and_cuts_are_defensive_copies(self):
        original_source = independent._source()
        original_world = independent._expected_world()
        source = independent._source()
        source['routes']['A-B'][0][0] += 10.
        world = independent._expected_world()
        row = next(row for rows in world.values() for row in rows if row['id'] == 'A-B')
        row['points'][0] = (1000., 1000., 1000.)
        row['lane'] = 1000
        self.assertEqual(independent._source(), original_source)
        self.assertEqual(independent._expected_world(), original_world)

    def test_three_actual_saved_owners_make_exactly_six_complete_journeys(self):
        scene = {'placements': [{'piece_id': piece['id'], 'rotation_degrees_ccw': 0,
                 'origin_m': [16.*piece['engineering']['world_origin_cell'][0],
                              -16.*piece['engineering']['world_origin_cell'][1]]} for piece in self.pieces]}
        result = independent.check_assembly(self.pieces, self.resources, scene)
        self.assertEqual(result['complete_directed_journeys'], 6)
        self.assertEqual(result['complete_native_members'], 12)
        self.assertEqual(len(result['proper_rotations']), 4)
        scene['placements'][1]['origin_m'][0] += 16.
        with self.assertRaisesRegex(ValueError, 'moved a component'):
            independent.check_assembly(self.pieces, self.resources, scene)


def rectangle_faces(west, east, south, north, height):
    points = [(west, south, height), (east, south, height),
              (east, north, height), (west, north, height)]
    return [{'points': tuple(points[i] for i in indices), 'kind': 'pavement', 'role': 'pavement',
             'upward': True, 'downward': False} for indices in ((0, 1, 2), (0, 2, 3))]


def prism_faces(record):
    corners, bottom, top = record['corners_en_m'], record['bottom_m'], record['top_m']
    vertices = [(*point, h) for h in (bottom, top) for point in corners]
    faces = []
    for quad in ((0, 3, 2, 1), (4, 5, 6, 7), (0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7)):
        for indices in ((quad[0], quad[1], quad[2]), (quad[0], quad[2], quad[3])):
            points = tuple(vertices[i] for i in indices)
            normal = np.cross(np.subtract(points[1], points[0]), np.subtract(points[2], points[0]))
            faces.append({'points': points, 'kind': 'support', 'role': record['id'],
                          'upward': normal[2] > 0., 'downward': normal[2] < 0.})
    return faces


class YJunctionPhysicalRejectionTests(unittest.TestCase):
    def test_both_raised_rail_sides_face_upward(self):
        from scp_highway import y_junction_geometry as writer
        for north, inward in ((-3., (0., 1.)), (3., (0., -1.))):
            with self.subTest(rail_north=north):
                triangles = writer._barrier_segment((0., north), (1., north), (15.001, 15.001), 2,
                                                     inward, inward, (0., 1.))
                self.assertTrue(triangles)
                self.assertTrue(all(np.cross(np.subtract(t[1][:3], t[0][:3]),
                                             np.subtract(t[2][:3], t[0][:3]))[1] > 0. for t in triangles))

    def test_missing_pavement_triangle_cannot_be_hidden_by_supported_nodes(self):
        faces = rectangle_faces(-1., 1., -1., 1., 7.501)
        first, last = (-.8, .25, 7.501), (.8, .25, 7.501)
        self.assertTrue(models.covered(first, last, faces))
        self.assertFalse(models.covered(first, last, faces[:1]))

    def test_native_phase_is_not_a_blanket_millimetre_support_tolerance(self):
        faces = rectangle_faces(-1., 1., -1., 1., 7.501)
        self.assertFalse(models.covered((-.8, .25, 7.502), (.8, .25, 7.502), faces))

    def test_finite_capsules_bound_only_small_encoding_gaps(self):
        first, last = (-.8, 0., 7.501), (.8, 0., 7.501)
        small = [*rectangle_faces(-1., -1e-6, -1., 1., 7.501),
                 *rectangle_faces(1e-6, 1., -1., 1., 7.501)]
        precision = {'admitted_spans': 0, 'maximum_admitted_span_m': 0.}
        self.assertTrue(models.covered(first, last, small, precision=precision))
        self.assertGreater(precision['admitted_spans'], 0)
        large = [*rectangle_faces(-1., -.0005, -1., 1., 7.501),
                 *rectangle_faces(.0005, 1., -1., 1., 7.501)]
        self.assertFalse(models.covered(first, last, large))

    def test_closed_road_shell_rejects_a_missing_actual_wall_triangle(self):
        record = {'id': 'support-A-B-16-1-pier', 'corners_en_m': [[1., 1.], [2., 1.], [2., 2.], [1., 2.]],
                  'bottom_m': 6.5, 'top_m': 7.5}
        faces = prism_faces(record)
        for face in faces:
            face['kind'] = 'pavement' if face['upward'] else 'body'
            face['role'] = face['kind']
        self.assertTrue(models.check_shell(faces, kind='road', component=False)['passed'])
        with self.assertRaisesRegex(ValueError, 'open or reversed edge'):
            models.check_shell(faces[:-1], kind='road', component=False)

    def test_barrier_face_entering_a_vehicle_corridor_is_rejected(self):
        first, last = (0., 0., 7.501), (1., 0., 7.501)
        obstacle = {'points': ((.2, .1, 7.501), (.8, .1, 7.501), (.8, .1, 8.8)),
                    'kind': 'barrier', 'role': 'barrier'}
        self.assertTrue(models._intrudes(first, last, obstacle))
        obstacle['points'] = tuple((p[0], p[1]+2., p[2]) for p in obstacle['points'])
        self.assertFalse(models._intrudes(first, last, obstacle))

    def test_a_barrier_clear_of_cars_cannot_enter_another_deck_slab(self):
        roof = rectangle_faces(-2., 2., -2., 2., 15.)
        underside = rectangle_faces(-2., 2., -2., 2., 14.)
        for face in underside:
            face['kind'] = face['role'] = 'body'
            face['points'] = (face['points'][0], face['points'][2], face['points'][1])
            face['upward'], face['downward'] = False, True
        rail = {'points': ((-.5, 1.5, 14.5), (.5, 1.5, 14.5), (0., 1.8, 14.5)),
                'kind': 'barrier', 'role': 'barrier'}
        with self.assertRaisesRegex(ValueError, 'barrier surface enters an actual road slab'):
            models.check_barrier_deck_clearance([*roof, *underside, rail])
        rail['points'] = tuple((*p[:2], 13.5) for p in rail['points'])
        lower_floor = deepcopy(underside)
        for face in lower_floor:
            face['points'] = tuple((*p[:2], 6.5) for p in face['points'])
        self.assertTrue(models.check_barrier_deck_clearance([*roof, *underside, *lower_floor, rail])['passed'])

    def test_barriers_on_distinct_links_cannot_cross_triangle_interiors(self):
        first = {'points': ((-1., -1., 10.), (1., -1., 10.), (0., 1., 10.)), 'kind': 'barrier', 'role': 'barrier'}
        second = {'points': ((0., -.5, 9.), (0., -.5, 11.), (0., .5, 10.)), 'kind': 'barrier', 'role': 'barrier'}
        with self.assertRaisesRegex(ValueError, 'cross through a finite triangle interior'):
            models.check_barrier_intersections([first, second])
        second['points'] = ((1., -1., 10.), (-1., -1., 10.), (0., -2., 11.))
        self.assertTrue(models.check_barrier_intersections([first, second])['passed'])
        with self.assertRaisesRegex(ValueError, 'duplicate a finite coplanar area'):
            models.check_barrier_intersections([first, first])

    def test_vertical_barrier_faces_inside_a_slab_cannot_hide_in_zero_plan_area(self):
        roof = {'points': ((0., 0., 10.), (4., 0., 10.), (0., 4., 10.)),
                'kind': 'pavement', 'role': 'pavement', 'upward': True, 'downward': False}
        underside = {'points': ((0., 0., 9.), (0., 4., 9.), (4., 0., 9.)),
                     'kind': 'body', 'role': 'body', 'upward': False, 'downward': True}
        rail = {'points': ((1., 1., 9.2), (1., 2., 9.2), (1., 1., 9.8)),
                'kind': 'barrier', 'role': 'barrier'}
        with self.assertRaisesRegex(ValueError, 'barrier surface enters an actual road slab'):
            models.check_barrier_deck_clearance([roof, underside, rail])
        rail['points'] = tuple((p[0], p[1], p[2]-2.) for p in rail['points'])
        result = models.check_barrier_deck_clearance([roof, underside, rail])
        self.assertEqual(result['vertical_barrier_triangles_checked'], 1)

    def test_a_thin_interior_duplicate_is_not_a_finite_edge_contact(self):
        first = {'points': ((0., 0., 10.), (10., 0., 10.), (0., 10., 10.)),
                 'kind': 'barrier', 'role': 'barrier'}
        second = {'points': ((1., 1., 10.), (2., 1., 10.), (1., 1.000003, 10.)),
                  'kind': 'barrier', 'role': 'barrier'}
        with self.assertRaisesRegex(ValueError, 'duplicate a finite coplanar area'):
            models.check_barrier_intersections([first, second])
        for face in (first, second):
            face['kind'] = face['role'] = 'pavement'
            face['upward'], face['downward'] = True, False
        with self.assertRaisesRegex(ValueError, 'deck bodies overlap'):
            models.check_deck_overlaps([first, second])

    def test_near_coplanar_sections_do_not_invent_segments_outside_native_faces(self):
        authored = {'points': ((-25.501174926757812, -22.498825073242188, 15.32912540435791),
                               (-24., -20.76151132583618, 15.07866096496582),
                               (-24., -20.688292503356934, 15.00100040435791)),
                    'kind': 'barrier', 'role': 'barrier-native-A-upper-helper'}
        native = {'points': ((-41.50117492675781, -38.49882507324219, 15.32912540435791),
                             (-25.501174926757812, -22.498825073242188, 15.32912540435791),
                             (-25.65585422515869, -22.344146728515625, 15.00100040435791)),
                  'kind': 'barrier', 'role': 'native-reference-barrier', 'native_reference': True}
        self.assertTrue(models.check_barrier_intersections([authored, native])['passed'])

    def test_original_c_overhang_skin_scope_requires_the_literal_parent_certificate(self):
        face = {'points': ((55.5, 7.5, 15.001), (56.001, 7.5, 15.001), (55.5, 8.001, 15.001)),
                'uv': ((0., 0.), (1., 0.), (0., 1.)), 'material': {'raw': b'fixture', 'textures': []},
                'role': 'pavement-native-C-upper-retained-core-collar', 'kind': 'pavement',
                'upward': True, 'downward': False, 'owner_cell': (3, 0)}
        original = deepcopy(face)
        certificate = {'certified_face_indices': [0], 'internal_pavement_masks': {},
                       'source_model_sha256': ['3d94bcce2ff84c9bd06d3bbbc7a089b8eaa28cfe921c3d31e87a27300cffd3dd']}
        with patch('scp_highway.y_junction_native_models.certify_native_collars', return_value=certificate):
            skin, report = models.external_skin([face], {'dd_rhw': {'fixture': b'fixture'}})
            self.assertTrue(all(p[0] <= 56. and p[1] <= 8. for f in skin for p in f['points']))
            self.assertGreater(report['finite_original_c_overhang_skin_scope']['removed_original_surface_area_m2'], 0.)
            self.assertEqual(face, original)
            certificate['certified_face_indices'] = []
            with self.assertRaisesRegex(ValueError, 'pinned original face'):
                models.external_skin([face], {'dd_rhw': {'fixture': b'fixture'}})
            face['role'] = 'pavement-native-C-upper'
            skin, _report = models.external_skin([face], {'dd_rhw': {'fixture': b'fixture'}})
            self.assertEqual(skin[0]['points'], original['points'])

    def test_buried_peer_body_trim_still_requires_the_real_new_outer_wall(self):
        high = 15.+models.DATUM_UPPER
        bottom, inner = high-1., 2.-.0014158
        main = prism_faces({'id': 'main', 'corners_en_m': [[1., 1.], [inner, 1.], [inner, 2.], [1., 2.]],
                            'bottom_m': bottom, 'top_m': high})
        ledge = prism_faces({'id': 'ledge', 'corners_en_m': [[inner, 1.], [2., 1.], [2., 2.], [inner, 2.]],
                             'bottom_m': bottom, 'top_m': 15.})[:10]
        faces = main+ledge
        for face in faces:
            face['kind'] = face['role'] = 'pavement' if face['upward'] else 'body'
            face.update(uv=((0., 0.), (1., 0.), (0., 1.)), material={'raw': b'fixture', 'textures': []})
        for face in main[6:8]:
            face['role'] = 'body-native-A-upper-peer'
        excess = high-15.
        rows = [{'face_index': index, 'role': 'body-native-A-upper-peer', 'analysis_below_height_m': 15.,
                 'underside_height_m': bottom, 'source_model_sha256': 'peer-source-fixture',
                 'source_extrusion_length_m': 3., 'finite_source_footprint_and_height_containment_proved': True,
                 'requires_independent_complete_shell_and_outer_wall_proof': True,
                 'source_body_surface_area_below_floor_m2': area}
                for index, area in ((6, .5-.5*excess**2), (7, .5-excess+.5*excess**2))]
        certificate = {'certified_face_indices': [6, 7], 'internal_pavement_masks': {},
                       'source_model_sha256': ['peer-source-fixture'], 'buried_peer_body_regions': rows}
        original = deepcopy(faces)
        with patch('scp_highway.y_junction_native_models.certify_native_collars', return_value=certificate):
            skin, report = models.external_skin(faces, {'dd_rhw': {'fixture': b'fixture'}})
        self.assertEqual(faces, original)
        raised_strip = [face for face in skin if face['role'] == 'body-native-A-upper-peer']
        self.assertTrue(raised_strip)
        self.assertTrue(all(p[2] >= 15. for face in raised_strip for p in face['points']))
        self.assertAlmostEqual(max(p[2] for face in raised_strip for p in face['points']), high)
        self.assertEqual(report['finite_original_peer_body_skin_scope']['source_faces_trimmed'], 2)
        self.assertTrue(models.check_shell(skin, kind='road', component=False)['passed'])
        without_wall = [face for face in skin if not all(abs(p[0]-2.) < 1e-12 for p in face['points'])]
        with self.assertRaisesRegex(ValueError, 'open or reversed edge'):
            models.check_shell(without_wall, kind='road', component=False)

    def test_missing_prism_surface_is_rejected_independently_of_its_name(self):
        record = {'id': 'support-A-B-16-1-pier', 'corners_en_m': [[1., 1.], [2., 1.], [2., 2.], [1., 2.]],
                  'bottom_m': 0., 'top_m': 6.5}
        faces = prism_faces(record)
        with patch.object(models, '_support_records', return_value=[record]):
            self.assertTrue(models.check_support_solids(faces, [])['passed'])
            with self.assertRaisesRegex(ValueError, 'complete surface'):
                models.check_support_solids(faces[:-1], [])

    def test_a_vehicle_wholly_inside_a_bad_closed_support_is_rejected(self):
        record = {'id': 'support-A-B-16-1-pier', 'corners_en_m': [[0., 0.], [10., 0.], [10., 10.], [0., 10.]],
                  'bottom_m': 0., 'top_m': 15.}
        faces = prism_faces(record)
        route = {'points': [(4., 5., 7.5), (5., 5., 7.5)]}
        with patch.object(models, '_support_records', return_value=[record]):
            with self.assertRaisesRegex(ValueError, 'contains part of the actual vehicle corridor'):
                models.check_support_solids(faces, [route])

    def test_a_pier_clear_of_cars_still_cannot_pierce_the_paved_shoulder(self):
        record = {'id': 'support-A-B-16-1-pier', 'corners_en_m': [[2., -.4], [2.8, -.4], [2.8, .4], [2., .4]],
                  'bottom_m': 0., 'top_m': 14.}
        faces = [*prism_faces(record), *rectangle_faces(-4., 4., -2., 2., 7.501)]
        route = {'points': [(-1., 0., 7.5), (1., 0., 7.5)]}
        with patch.object(models, '_support_records', return_value=[record]):
            with self.assertRaisesRegex(ValueError, 'pierces an actual pavement surface'):
                models.check_support_solids(faces, [route])

    def test_authored_faces_must_clear_unchanged_native_approach_cars(self):
        route = {'points': [(0., 0., 7.5), (1., 0., 7.5)]}
        face = {'points': ((.2, .1, 7.501), (.8, .1, 7.501), (.8, .1, 8.8)),
                'kind': 'barrier', 'role': 'barrier'}
        with self.assertRaisesRegex(ValueError, 'unchanged native approach vehicle corridor'):
            models.check_native_vehicle_clearance([face], [route])
        face['points'] = tuple((p[0], p[1]+2., p[2]) for p in face['points'])
        self.assertEqual(models.check_native_vehicle_clearance([face], [route])['native_real_car_segments_checked'], 1)

    def test_a_cap_touching_the_road_must_also_touch_its_ground_pier(self):
        corners = [[1., 1.], [2., 1.], [2., 2.], [1., 2.]]
        records = [{'id': 'support-B-C-16-1-pier', 'corners_en_m': corners, 'bottom_m': 0., 'top_m': 6.1},
                   {'id': 'support-B-C-16-1-cap', 'corners_en_m': corners, 'bottom_m': 6.1, 'top_m': 6.5}]
        self.assertEqual(models.check_support_frames(records, require_plan=False)['connected_ground_frames'], 1)
        records[0]['top_m'] -= .1
        with self.assertRaisesRegex(ValueError, 'pier contact'):
            models.check_support_frames(records, require_plan=False)

    def test_floating_cap_is_rejected_against_an_actual_served_underside(self):
        points = np.asarray(independent._source()['routes']['A-B'])
        station = np.r_[0., np.linalg.norm(np.diff(points[:, :2], axis=0), axis=1).cumsum()]
        p = points[int(np.argmin(abs(station-16.)))]
        floor = p[2]+models.datum(p[2])-1.
        faces = rectangle_faces(p[0]-2., p[0]+2., p[1]-2., p[1]+2., floor)
        for face in faces:
            face['kind'] = face['role'] = 'body'
            face['points'] = (face['points'][0], face['points'][2], face['points'][1])
            face['downward'], face['upward'] = True, False
        record = {'id': 'support-A-B-16-1-cap', 'corners_en_m': [[p[0]-1., p[1]-1.], [p[0]+1., p[1]-1.],
                    [p[0]+1., p[1]+1.], [p[0]-1., p[1]+1.]], 'bottom_m': floor-.4, 'top_m': floor}
        self.assertAlmostEqual(models._support_contact(record, faces, models.FaceIndex(faces))['intentional_contact_station_embed_m'], 0.)
        record['top_m'] -= .1
        with self.assertRaisesRegex(ValueError, 'floats below its slab'):
            models._support_contact(record, faces, models.FaceIndex(faces))
        record['top_m'] = floor
        for face in faces:
            face['points'] = tuple((*q[:2], floor+.4*(q[0]-p[0])) for q in face['points'])
        with self.assertRaisesRegex(ValueError, 'bounded embed over the actual served-slab footprint'):
            models._support_contact(record, faces, models.FaceIndex(faces))


if __name__ == '__main__':
    unittest.main()
