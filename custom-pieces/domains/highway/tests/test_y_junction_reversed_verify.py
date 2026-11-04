"""Independent reversed routes, saved PATHs, and finite native policy controls."""
from copy import deepcopy
import hashlib
import json
import math
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

import shapely
from shapely.geometry import box, Polygon
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT/'framework'), str(ROOT/'domains/highway/implementation')]
from scp import jsonc
from scp.connectivity import assembly_connectivity, piece_connectivity
from scp.track_paths import PATH
from scp_highway import connections, ramp_paths
from scp_highway import y_junction_verify as shared
from scp_highway import y_junction_reversed_verify as independent
from scp_highway import y_junction_reversed_models_verify as models
from scp_highway import y_junction_reversed_native_models as native
import test_y_junction_approaches as original_native_fixture


def path_fixture():
    """Traffic-only21-cell fixture; it makes no physical ownership claim."""
    source = independent.independent_source()
    cells = tuple(shared.OWNED_WORLD_CELLS[key] for key in shared.KEYS)
    config = shared.RouteVariantConfig(independent.KEYS, independent.PIECE_IDS,
                                      independent.RECIPES, cells, independent.independent_source)
    cut = ramp_paths.slice_routes([{'id': name, 'points': points,
                                    'lane': source['route_metadata'][name]['from_lane']}
                                   for name, points in source['routes'].items()])
    specs, resources = [], {}
    for index, world in enumerate(cells):
        origin = [min(c[k] for c in world) for k in (0, 1)]
        local = [[c[0]-origin[0], c[1]-origin[1]] for c in world]
        tiles = [f'{0x5FA00000+index*0x10000+i*0x100:08x}' for i in range(len(local))]
        piece = {'id': independent.PIECE_IDS[index], 'domain': 'highway',
            'recipe': independent.RECIPES[index], 'geometry_key': independent.KEYS[index],
            'y_junction_variant': 'reversed', 'cells': local, 'tile_ids': tiles,
            'footprint': [max(c[k] for c in local)+1 for k in (0, 1)],
            'engineering': {'world_origin_cell': origin, 'max_grade_percent': 30.,
                'car_corridor_half_width_m': 1.25, 'car_corridor_height_m': 3.8,
                'model_only_cells': [cell for cell, actual in zip(local, world) if actual not in cut]},
            'shadow_mappings': [], 'model_shadows': {'enabled': False}}
        assets = {}
        for actual, tile in zip(world, tiles):
            raw = ramp_paths.encode_paths(cut.get(actual, []), allow_empty=True)
            lines = raw.decode('ascii').splitlines(); lines[4] = '1'
            assets[*PATH, int(tile, 16)] = ('\r\n'.join(lines)+'\r\n').encode('ascii')
        specs.append(piece); resources[piece['id']] = assets
    scene = {'placements': [{'piece_id': p['id'], 'origin_m': [16.*p['engineering']['world_origin_cell'][0],
                -16.*p['engineering']['world_origin_cell'][1]], 'rotation_degrees_ccw': 0} for p in specs]}
    return config, specs, resources, scene


class ReversedIndependentSourceControls(unittest.TestCase):
    def test_source_review_matches_twelve_fresh_members_and_descending_links(self):
        report = independent.check_source_candidate()
        self.assertEqual(report['fresh_native_members_checked'], 12)
        self.assertEqual(report['complete_directed_journeys'], 6)
        self.assertFalse(report['physical_model_mask_accepted'])
        grades = {r['journey']: r for r in report['routes']}
        for name in ('B-C', 'C-B'):
            self.assertLess(grades[name]['minimum_signed_grade_percent'], -20.)
            self.assertEqual(grades[name]['maximum_signed_grade_percent'], 0.)

    def test_changed_route_lane_or_native_pose_fails_independent_source_review(self):
        original = jsonc.load(independent.SUBJECT/'evidence/design-geometry.jsonc')
        measurements = jsonc.load(independent.SUBJECT/'evidence/native-design-inputs.jsonc')
        for field in ('point', 'lane', 'native-pose'):
            source, native_report = deepcopy(original), deepcopy(measurements)
            if field == 'point': source['routes']['B-C'][4][0] += .01
            if field == 'lane': source['route_metadata']['B-C']['from_lane'] ^= 1
            if field == 'native-pose': native_report['arms'][0]['helper'][1] = 2
            with TemporaryDirectory() as folder:
                subject = Path(folder); (subject/'evidence').mkdir()
                (subject/'evidence/design-geometry.jsonc').write_text(json.dumps(source))
                (subject/'evidence/native-design-inputs.jsonc').write_text(json.dumps(native_report))
                with patch.object(independent, 'SUBJECT', subject), self.subTest(field=field), self.assertRaises(ValueError):
                    independent.check_source_candidate()

    def test_original_dat_byte_invariance_requires_every_file_and_rejects_change(self):
        before = {key: key.encode() for key in independent.ORIGINAL_DAT_SHA256}
        self.assertEqual(independent.check_dat_byte_invariance(before, dict(before))['original_DATs_byte_identical'], 3)
        after = dict(before); after[next(iter(after))] += b'changed'
        with self.assertRaisesRegex(ValueError, 'original Y DAT changed'):
            independent.check_dat_byte_invariance(before, after)
        with self.assertRaisesRegex(ValueError, 'all three'):
            independent.check_dat_byte_invariance({}, {})
        with self.assertRaisesRegex(ValueError, 'baseline differs'):
            independent.check_original_dat_invariance(before, before)


class ReversedSavedPathControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config, cls.pieces, cls.resources, cls.scene = path_fixture()

    def test_all_three_encoded_path_sets_and_all_four_complete_rotations(self):
        with patch.object(independent, '_configuration', return_value=self.config):
            for piece in self.pieces:
                result = independent.check_paths(self.resources[piece['id']], piece)
                self.assertTrue(result['passed'])
                self.assertEqual(len(result['proper_rotations']), 4)
                self.assertLessEqual(result['maximum_signed_grade_percent'], 1e-6)
            report = independent.check_assembly(self.pieces, self.resources, self.scene)
        self.assertEqual(report['complete_directed_journeys'], 6)
        self.assertEqual(report['complete_native_members'], 12)
        self.assertTrue(report['no_uturn_or_unintended_lane_transfer'])
        self.assertEqual(len(report['proper_rotations']), 4)

    def test_shared_consumer_keeps_six_journeys_twelve_ports_and_signed_sloped_joins(self):
        with patch.object(independent, '_configuration', return_value=self.config):
            records = {piece['id']: piece_connectivity(piece, self.resources[piece['id']],
                contract=independent.reviewed_contract(piece), service_classifier=connections.service_classifier)
                for piece in self.pieces}
            result = assembly_connectivity('ddrhw-compact-diagonal-y-junction-reversed', self.scene,
                                           records, {p['id']: p for p in self.pieces})
        self.assertEqual(len(result['journeys']), 6)
        self.assertEqual(len(result['ports']), 12)
        self.assertEqual(len(result['encoded_route_joins']), 8)
        graded = []
        for join in result['encoded_route_joins']:
            first = next(p for p in records[join['from_piece']]['ports'] if p['id'] == join['from_port'])
            second = next(p for p in records[join['to_piece']]['ports'] if p['id'] == join['to_port'])
            self.assertEqual(first['grade'], first['actual_saved_grade'])
            self.assertAlmostEqual(first['actual_saved_grade'], second['actual_saved_grade'], places=6)
            if abs(first['grade']) > 1e-4:
                graded.append(first['grade'])
        self.assertEqual(len(graded), 2)
        self.assertTrue(all(g < 0. for g in graded))

    def test_saved_new_endpoint_lane_class_cannot_revert_to_original(self):
        piece = self.pieces[0]; assets = dict(self.resources[piece['id']])
        origin = piece['engineering']['world_origin_cell']
        local = [-1-origin[0], 2-origin[1]]
        tile = int(piece['tile_ids'][piece['cells'].index(local)], 16)
        key = (*PATH, tile)
        lines = assets[key].decode().splitlines()
        marker = next(i for i, line in enumerate(lines) if line.startswith('-- SCP '))
        lines[marker+2] = str(int(lines[marker+2])+4)
        assets[key] = ('\r\n'.join(lines)+'\r\n').encode()
        with patch.object(independent, '_configuration', return_value=self.config), self.assertRaises(ValueError):
            independent.check_paths(assets, piece)


class ReversedFiniteNativePhysicalControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        original_native_fixture.ActualNativeYJunctionApproaches.setUpClass.__func__(cls)

    def test_fresh_source302_floor_transitions_at_exact_finite_three_metres(self):
        split = models.source_floor_segments(self.donors)
        values = list(split((-24., -28.8, 15.), (-20., -24.8, 15.)))
        self.assertEqual(len(values), 2)
        self.assertEqual(values[0][2][2], 15.)
        self.assertAlmostEqual(math.dist(values[0][0][:2], values[0][1][:2]), 3., places=10)
        self.assertEqual(values[1][2][2], 15.+models.physical.DATUM_UPPER)
        graded = list(split((0., 0., 15.), (1., 0., 14.9)))
        self.assertEqual(len(graded), 1)
        self.assertAlmostEqual(graded[0][2][2], 15.+models.physical.DATUM_UPPER)

    def test_actual_two_dimensional_datum_riser_clears_but_body_above_local_roof_rejects(self):
        floors = models.source_floor_segments(self.donors)
        first = (-22.799479141, -27.599479141, 7.5)
        last = (-22.728860267, -27.528860267, 7.5)
        points = ((-21.87867975235, -24., 7.50013256073),
                  (-21.87867975235, -24., 7.5), (-21.87867975235, -37.87867975235, 7.5))
        face = models._face(points, [(0., 0.)]*3, 'body', {})
        self.assertTrue(models.physical._intrudes(first, last, face), 'Exercise the old centreline-height false positive')
        self.assertFalse(floors.intrudes(first, last, face))
        raised = {**face, 'points': tuple((p[0], p[1], p[2]+.002) for p in points)}
        self.assertTrue(floors.intrudes(first, last, raised))

    def test_full_underfloor_checks_the_vehicle_width_beyond_the_centreline(self):
        def square(ymin, ymax, height, role, downward=False):
            points = [(0., ymin, height), (2., ymin, height), (2., ymax, height), (0., ymax, height)]
            faces = []
            for indices in ((0, 1, 2), (0, 2, 3)):
                if downward: indices = tuple(reversed(indices))
                faces.append(models._face([points[i] for i in indices], [(0., 0.)]*3, role, {}))
            return faces
        height = 15.+models.physical.DATUM_UPPER
        roof = square(-2., 2., height, 'pavement')
        floor = square(-2., 2., height-1., 'body', True)
        routes = [{'points': [(.1, 0., 15.), (1.9, 0., 15.)]}]
        self.assertTrue(models.check_full_underfloor(floor, roof, routes)['passed'])
        narrow = square(-.5, .5, height-1., 'body', True)
        with self.assertRaisesRegex(ValueError, 'full authored one-metre body'):
            models.check_full_underfloor(narrow, roof, routes)
        with self.assertRaisesRegex(ValueError, 'full authored one-metre body'):
            models.check_full_underfloor(square(-2., 2., 6.5, 'body', True), roof, routes)

        # This hole is entirely inside the owned width and4.5µm from the
        # nearest real floor at its centre. An area-only1e-10m² guard would
        # incorrectly hide the remaining finite hole after4µm edge capsules.
        region = box(0., -2., 2., 2.).difference(box(.9-4.5e-6, 1.-4.5e-6, .9+4.5e-6, 1.+4.5e-6))
        punctured = []
        for triangle in shapely.constrained_delaunay_triangles(region).geoms:
            points = [(x, y, height-1.) for x, y in list(triangle.exterior.coords)[:3]]
            if models.physical._normal(points)[2] > 0.: points.reverse()
            punctured.append(models._face(points, [(0., 0.)]*3, 'body', {}))
        with self.assertRaisesRegex(ValueError, 'full authored one-metre body'):
            models.check_full_underfloor(punctured, roof, routes)

    def test_actual_old_graded_plane_pair_rejects_and_coherent_pair_passes(self):
        roof_points = ((-8., 24.971564292907715, 7.5039801597595215),
                       (-8.390762329101562, 24., 7.504121780395508),
                       (-8., 24.80594539642334, 7.504329204559326))
        floor_points = ((-8.399335384368896, 24., 6.504082202911377),
                        (-8., 24.850939750671387, 6.504239559173584),
                        (-8., 24.728355884552002, 6.504483222961426))
        roof = models._face(roof_points, [(0., 0.)]*3, 'pavement', {})
        old_floor = models._face(floor_points, [(0., 0.)]*3, 'body', {})
        patch = Polygon([p[:2] for p in roof_points]).intersection(Polygon([p[:2] for p in floor_points]))
        q = np.array([-8.1429, 24.5459, 1.])
        actual_depth = float((models._plane_field(roof)-models._plane_field(old_floor))@q)
        self.assertAlmostEqual(actual_depth, .9999959362232755, places=12)
        self.assertGreater(patch.difference(models.body_depth_coverage(roof, patch, [old_floor])).area, 1e-4)
        field = models._plane_field(roof)
        coherent = models._face([(p[0], p[1], float(field@np.array([p[0], p[1], 1.]))-1.)
                                for p in floor_points], [(0., 0.)]*3, 'body', {})
        self.assertLessEqual(patch.difference(models.body_depth_coverage(roof, patch, [coherent])).area, 1e-18)

    def test_actual_edge_only_floor_contact_uses_one_finite_triangle_within4um(self):
        roof_points = ((-10.500677108764648, 24., 7.500999927520752),
                       (-10.381772518157959, 24.24247646331787, 7.500999927520752),
                       (-10.505190372467041, 24., 7.500999927520752))
        floor_points = ((-10.400605201721191, 24., 6.500999927520752),
                        (-10.500677108764648, 24., 6.500999927520752),
                        (-10.381772518157959, 24.24247646331787, 6.500999927520752))
        roof = models._face(roof_points, [(0., 0.)]*3, 'pavement', {})
        floor = models._face(floor_points, [(0., 0.)]*3, 'body', {})
        patch = Polygon([p[:2] for p in roof_points]).intersection(
            box(-10.3817745, 24.2424725, -10.381772518157959, 24.24247646331787))
        self.assertEqual(patch.intersection(Polygon([p[:2] for p in floor_points])).area, 0.)
        proof = {'exact_convex_patch_admissions': 0, 'maximum_admitted_euclidean_distance_m': 0.}
        self.assertLessEqual(patch.difference(models.body_depth_coverage(roof, patch, [floor], precision=proof)).area, 1e-18)
        self.assertEqual(proof['exact_convex_patch_admissions'], 1)
        self.assertLess(proof['maximum_admitted_euclidean_distance_m'], .1e-6)
        raised = {**floor, 'points': tuple((p[0], p[1], p[2]+5e-6) for p in floor_points)}
        remote = {**floor, 'points': tuple((p[0]+100., p[1], p[2]) for p in floor_points)}
        for wrong in (raised, remote, {**floor, 'native_reference': True}):
            self.assertGreater(patch.difference(models.body_depth_coverage(roof, patch, [wrong])).area, 0.)

    def test_floor_contact_has_one_combined3d_budget(self):
        roof = models._face([(-1., 0., 15.), (1., 0., 15.), (-1., 2., 15.)], [(0., 0.)]*3, 'pavement', {})
        patch = box(-3e-6, .4, .1, .6)
        def floor(error):
            return models._face([(0., 0., 14.+error), (0., 1., 14.+error), (1., 0., 14.+error)],
                                [(0., 0.)]*3, 'body', {})
        #3µm laterally plus3µm vertically is4.243µm in3D and must fail.
        self.assertGreater(patch.difference(models.body_depth_coverage(roof, patch, [floor(3e-6)])).area, 0.)
        #3µm laterally plus2µm vertically remains within the same4µm radius.
        self.assertLessEqual(patch.difference(models.body_depth_coverage(roof, patch, [floor(2e-6)])).area, 1e-18)

    def test_nonzero_tiny_seam_across_two_floors_is_proved_without_area_exemption(self):
        roof = models._face([(-3., -3., 15.), (3., -3., 15.), (0., 6., 15.)], [(0., 0.)]*3, 'pavement', {})
        left = models._face([(-2., -2., 14.), (-2., 0., 14.), (0., 0., 14.)], [(0., 0.)]*3, 'body', {})
        right = models._face([(0., 0., 14.), (2., 2., 14.), (2., 0., 14.)], [(0., 0.)]*3, 'body', {})
        patch = Polygon([(-1., -1.), (1., 1.), (0., 3e-16)])
        self.assertGreater(patch.area, 0.)
        self.assertLess(patch.area, 1e-15)
        self.assertLessEqual(patch.difference(models.body_depth_coverage(roof, patch, [left, right])).area, 1e-18)
        self.assertTrue(models.body_depth_coverage(roof, patch, [left]).is_empty)

    def test_removed_helper_wall_requires_real_slab_outside_every_car_strip(self):
        q = np.array([-25.65585422515869, -22.34414577484131])
        direction = np.array([math.sqrt(.5), math.sqrt(.5)])
        end = q+3.*direction; normal = np.array([-direction[1], direction[0]])*.05
        wall = models._face([(*q, 14.00100040435791), (*end, 14.00100040435791),
                             (*end, 15.00100040435791)], [(0., 0.)]*3,
                            'body-native-A-upper-helper', {})
        ring = [q-normal, end-normal, end+normal, q+normal]
        polygon = Polygon(ring)
        def faces(region, height, kind, downward=False):
            result = []
            for triangle in shapely.constrained_delaunay_triangles(region).geoms:
                points = [(x, y, height) for x, y in list(triangle.exterior.coords)[:3]]
                if (models.physical._normal(points)[2] < 0.) != downward: points.reverse()
                result.append(models._face(points, [(0., 0.)]*3, kind, {}))
            return result
        roof, floor = faces(polygon, 15., 'pavement'), faces(polygon, 14., 'body', True)
        row = {'face_index': 0, 'role': wall['role'], 'analysis_below_height_m': 15., 'underside_height_m': 14.}
        actual = [wall, *roof, *floor]
        self.assertTrue(models.check_actual_helper_slab_containment(actual, [row])['passed'])
        middle = (q+end)/2.
        hole = box(middle[0]-.01, middle[1]-.01, middle[0]+.01, middle[1]+.01)
        car = models._vehicle_polygon((-24., -28.8, 15.), (-21.8786796564, -26.6786796564, 15.))
        self.assertTrue(hole.disjoint(car), 'The removed floor interval must lie outside the vehicle strip')
        punctured = faces(polygon.difference(hole), 14., 'body', True)
        with self.assertRaisesRegex(ValueError, 'entire removed footprint'):
            models.check_actual_helper_slab_containment([wall, *roof, *punctured], [row])
        with self.assertRaisesRegex(ValueError, 'entire removed footprint'):
            models.check_actual_helper_slab_containment([wall, *roof, *[{**f, 'native_reference': True} for f in floor]], [row])
        with self.assertRaisesRegex(ValueError, 'entire removed footprint'):
            models.check_actual_helper_slab_containment([wall, *roof, *faces(polygon, 14.5, 'body', True)], [row])

    def test_owned_native_c_roof_is_source_pinned_and_has_no_underside_waiver(self):
        faces = models.owned_native_roof_references(self.donors)
        self.assertEqual(len(faces), 8)
        self.assertTrue(all(models.C_JOIN_EAST-1e-12 <= p[0] <= 56. for f in faces for p in f['points']))
        original = native.native_owned_interface_faces(self.donors)
        for kind in ('missing', 'wrong-pose', 'enlarged-roi', 'changed-uv'):
            actual = deepcopy(original)
            if kind == 'missing': actual = []
            if kind == 'wrong-pose': actual[0]['pose'] = 3
            if kind == 'enlarged-roi': actual[0]['owned_analysis_bounds_en_m'][1][0] += .001
            if kind == 'changed-uv':
                p = list(actual[0]['fragments'][0]['triangle'][0]); p[3] += .01
                actual[0]['fragments'][0]['triangle'] = (tuple(p), *actual[0]['fragments'][0]['triangle'][1:])
            with patch.object(native, 'native_owned_interface_faces', return_value=actual), self.subTest(kind=kind), self.assertRaises(ValueError):
                models.owned_native_roof_references(self.donors)

    def test_source_c_helper_absence_cannot_supply_a_reference(self):
        context = deepcopy(self.donors)
        del context['dd_rhw'][0x5ad0e817, 0xbadb57f1, 0x57530000]
        with self.assertRaisesRegex(ValueError, 'all exact pinned'):
            models.owned_native_roof_references(context)

    def test_full_native_interface_has_exact_source_roles_and_rejects_barrier_deletion(self):
        parts = models.owned_native_roof_references(self.donors, kinds=('pavement', 'body', 'barrier'))
        self.assertEqual({kind: sum(p['kind'] == kind for p in parts) for kind in ('pavement', 'body', 'barrier')},
                         {'pavement': 8, 'body': 6, 'barrier': 62})
        original = native.native_owned_interface_faces(self.donors)
        for mutation in ('deleted-fragment', 'barrier-uv', 'source-pose', 'enlarged-roi'):
            actual = deepcopy(original)
            group = next(row for row in actual if row['role'] == 'barrier')
            if mutation == 'deleted-fragment': group['fragments'].pop(0)
            if mutation == 'source-pose': group['pose'] = 3
            if mutation == 'enlarged-roi': group['owned_analysis_bounds_en_m'][1][0] += .001
            if mutation == 'barrier-uv':
                triangle = list(group['fragments'][0]['triangle']); point = list(triangle[0]); point[3] += .01
                triangle[0] = tuple(point); group['fragments'][0]['triangle'] = tuple(triangle)
            with patch.object(native, 'native_owned_interface_faces', return_value=actual), self.subTest(mutation=mutation), self.assertRaises(ValueError):
                models.owned_native_roof_references(self.donors, kinds=('pavement', 'body', 'barrier'))

    def test_intrinsic_native_reference_roof_mask_uses_only_its_same_source_pose_and_deck(self):
        faces, proof = models.native_interface_skin(self.donors)
        self.assertEqual(proof['reference_source_counts'], {'pavement': 8, 'barrier': 62})
        self.assertEqual(proof['analysis_reference_faces'], 74)
        self.assertEqual(proof['source_body_reference_faces_used'], 0)
        union = proof['intrinsic_source_roof_union']
        self.assertEqual(union['source_roof_fragments_trimmed'], 8)
        self.assertAlmostEqual(union['removed_source_roof_plan_area_m2'], .0033118387718786843, places=14)
        self.assertEqual(union['new_authored_faces_trimmed'], 0)
        source = models.owned_native_roof_references(self.donors, kinds=('pavement', 'barrier'))
        for field in ('model_sha256', 'pose', 'deck'):
            actual = deepcopy(source)
            item = next(face for face in actual if face['kind'] == 'barrier')
            item['native_source'][field] = {'model_sha256': '0'*64, 'pose': 3, 'deck': 'lower'}[field]
            with patch.object(models, 'owned_native_roof_references', return_value=actual), self.subTest(field=field), self.assertRaisesRegex(ValueError, 'same actual pinned model and pose'):
                models.native_interface_skin(self.donors)

    def test_reversed_roles_and_bounds_are_explicit_and_old_defaults_stay_strict(self):
        self.assertEqual(models.physical._kind('barrier-helper-foot-shim', variant='reversed'), 'barrier')
        with self.assertRaises(ValueError): models.physical._kind('barrier-helper-foot-shim')
        bounds = models.native_cell_bounds(self.donors)
        self.assertEqual(len(bounds), 6)
        self.assertTrue(all(b[:3] == (-8., 8., -8.) and b[3] == 8.00100040435791 for b in bounds.values()))
        self.assertEqual(models.check_support_source()['unchanged_physical_prisms'], 66)

    def test_c_hybrid_roof_requires_authored_floor_and_owned_boundary_cap(self):
        height = 15.+models.physical.DATUM_UPPER
        points = [(x, y, z) for z in (height-1., height) for x, y in ((55., -2.), (56., -2.), (56., 2.), (55., 2.))]
        body = []
        for indices in ((0, 3, 2), (0, 2, 1), (0, 1, 5), (0, 5, 4),
                        (1, 2, 6), (1, 6, 5), (2, 3, 7), (2, 7, 6), (3, 0, 4), (3, 4, 7)):
            body.append(models._face([points[i] for i in indices], [(0., 0.)]*3, 'body', {}))
        roof = [models._face([(55., -2., height), (models.C_JOIN_EAST, -2., height),
                             (models.C_JOIN_EAST, 2., height)], [(0., 0.)]*3, 'pavement', {}),
                models._face([(55., -2., height), (models.C_JOIN_EAST, 2., height),
                             (55., 2., height)], [(0., 0.)]*3, 'pavement', {})]
        references = []
        for face in models.owned_native_roof_references(self.donors):
            if face['points'][0][2] < 10.:
                continue
            vertices = [(*p, *uv) for p, uv in zip(face['points'], face['uv'])]
            clipped = models._clip(vertices, (0., 1., 0., 2.), (0., -1., 0., 2.))
            references.extend(models._triangulated(face, clipped))
        skin = [*body, *roof, *references]
        self.assertTrue(models.physical.check_shell(skin, kind='road', component=False)['passed'])
        with self.assertRaisesRegex(ValueError, 'open or reversed edge'):
            models.physical.check_shell([*body[2:], *roof, *references], kind='road', component=False)
        without_east_cap = [f for f in body if not all(abs(p[0]-56.) < 1e-12 for p in f['points'])]
        with self.assertRaisesRegex(ValueError, 'open or reversed edge'):
            models.physical.check_shell([*without_east_cap, *roof, *references], kind='road', component=False)
        routes = [{'points': [(55.9988, 0., 15.), (56., 0., 15.)]}]
        floors = models.source_floor_segments(self.donors)
        result = models.physical.check_corridors(skin, routes, floor_segments=floors, allow_original_prefix=False)
        self.assertEqual(result['original_native_endpoint_prefixes'], 0)
        with self.assertRaisesRegex(ValueError, 'complete one-metre underside'):
            models.physical.check_corridors([*body[2:], *roof, *references], routes,
                                            floor_segments=floors, allow_original_prefix=False)


if __name__ == '__main__':
    unittest.main()
