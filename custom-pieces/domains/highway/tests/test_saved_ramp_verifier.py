"""Independent saved-triangle checks reject missing road and traffic defects."""
from copy import deepcopy
from pathlib import Path
import struct
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT/'framework'),str(ROOT/'domains/highway/implementation')]

from scp.dbpf import pack_dbpf
from scp.models import pack_s3d,parse_s3d
from scp.track_paths import PATH,S3D,_parse_paths
from scp.verify import strict_dbpf
from scp_highway import ramp_geometry as geometry
from scp_highway import ramp_paths as paths
from scp_highway.ramp_verify import check_pavement

TEXTURE = (0x7AB50E44,0x1ABE787D)
EMPTY_PATH = b'SC4PATHS\r\n1.2\r\n0\r\n0\r\n0\r\n'


def fixture(road_points,traffic_points=None):
    models = geometry.compile_road_tiles([{'points':road_points}],0x5F900000)
    routes = paths.slice_routes([{'id':'lower-off','points':traffic_points or road_points}])
    cells = sorted(models)
    piece = {'id':'saved-lower-ramp-fixture','cells':[list(cell) for cell in cells],
             'tile_ids':[f'{0x5F900000+16*index:08x}' for index in range(len(cells))],
             'authored_texture_ids':['5f900000'],
             'engineering':{'max_grade_percent':40.0,'pavement_path_offset_m':0.0,
                 'car_corridor_half_width_m':1.25,'car_corridor_height_m':3.8,
                 'model_only_cells':[list(cell) for cell in cells if cell not in routes]}}
    resources = {(*TEXTURE,0x5F900000):geometry.create_surface_atlas()}
    for cell,identifier in zip(cells,piece['tile_ids']):
        iid = int(identifier,16)
        resources[*S3D,iid] = models[cell]
        resources[*PATH,iid] = paths.encode_paths(routes[cell]) if cell in routes else EMPTY_PATH
    # Re-open an actual encoded DAT, so checks see saved resources rather than
    # an in-memory mesh or an author's unsaved point sequence.
    return strict_dbpf(pack_dbpf(resources)),piece


def saved_routes(raw):
    return [] if raw.splitlines()[2] == b'0' else _parse_paths(raw)


def edit_vertices(raw,edit):
    model = parse_s3d(raw)
    for block in model['vertices']:
        data = bytearray(block['data'])
        for offset in range(0,len(data),block['stride']):
            values = struct.unpack_from('<5f',data,offset)
            struct.pack_into('<5f',data,offset,*edit(values))
        block['data'] = bytes(data)
    return pack_s3d(model)


def remove_faces(raw,predicate):
    model = parse_s3d(raw)
    for mesh in model['meshes']:
        vi,ii,pi,_mi = mesh['frames'][0]
        block = model['vertices'][vi]
        vertices = [struct.unpack_from('<5f',block['data'],offset)
                    for offset in range(0,len(block['data']),block['stride'])]
        current = model['indices'][ii]['values']
        indices = []
        for offset in range(0,len(current),3):
            ids = current[offset:offset+3]
            if not predicate([vertices[index] for index in ids]):
                indices.extend(ids)
        model['indices'][ii]['values'] = tuple(indices)
        model['primitives'][pi] = [(0,0,len(indices))]
    return pack_s3d(model)


class SavedRampVerifierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.profile = geometry.sample_grade_curve(
            [(8.,3.2),(18.,13.2),(30.,9.2),(40.,19.2)],
            start_height=7.5,flat_start=5.,flat_end=4.,max_grade=0.4,count=81)
        cls.saved,cls.definition = fixture(cls.profile['points'])

    def setUp(self):
        self.resources,self.piece = dict(self.saved),deepcopy(self.definition)

    def test_actual_saved_lower_ramp_passes_in_all_four_proper_rotations(self):
        ports = [{'direction':'in','point_m':[8.,3.2,7.5],'tangent':[1.,1.],'grade':0.0},
                 {'direction':'out','point_m':[40.,19.2,0.0],'tangent':[1.,1.],'grade':0.0}]
        report = check_pavement(self.resources,self.piece,ports=ports)
        self.assertTrue(report['passed'])
        self.assertTrue(report['continuous_segment_support'])
        self.assertTrue(report['native_external_ports_checked'])
        self.assertTrue(report['atlas']['checked'])
        self.assertGreater(report['maximum_grade_percent'],29.0)
        self.assertLess(report['maximum_grade_percent'],30.0)
        self.assertEqual(report['pavement_path_offset_m'],0.0)
        self.assertEqual([row['quarter_turns_clockwise'] for row in report['rotations']],[0,1,2,3])
        self.assertTrue(all(row['car_segments_checked'] == report['car_segments'] for row in report['rotations']))
        self.assertIn('no closed-solid containment',report['coverage_limit'])

    def test_missing_asphalt_cannot_pass_using_the_concrete_underside(self):
        iid = next(int(identifier,16) for identifier in self.piece['tile_ids']
                   if saved_routes(self.resources[*PATH,int(identifier,16)]))
        self.resources[*S3D,iid] = remove_faces(self.resources[*S3D,iid],
            lambda triangle:all(abs(point[3]-0.125) < 1e-6 for point in triangle))
        with self.assertRaisesRegex(ValueError,'does not continuously support'):
            check_pavement(self.resources,self.piece)

    def test_pavement_hole_between_two_path_nodes_is_rejected(self):
        points = [(0.,north,7.5) for north in (-8.,-2.,2.,8.)]
        resources,piece = fixture(points,[points[0],points[-1]])
        iid = int(piece['tile_ids'][0],16)
        resources[*S3D,iid] = remove_faces(resources[*S3D,iid],lambda triangle:
            all(abs(point[3]-0.125) < 1e-6 and abs(point[2]) <= 2.01 for point in triangle))
        self.assertEqual(len(_parse_paths(resources[*PATH,iid])[0]['points']),2)
        with self.assertRaisesRegex(ValueError,'does not continuously support'):
            check_pavement(resources,piece)

    def test_visually_displaced_pavement_cannot_claim_a_nonzero_wheel_offset(self):
        resources,piece = fixture([(0.,-8.,7.5),(0.,8.,7.5)])
        iid = int(piece['tile_ids'][0],16)
        resources[*S3D,iid] = edit_vertices(resources[*S3D,iid],lambda point:
            (point[0],point[1]+0.2,*point[2:]))
        with self.assertRaisesRegex(ValueError,'does not continuously support'):
            check_pavement(resources,piece)
        piece['engineering']['pavement_path_offset_m'] = 0.2
        with self.assertRaisesRegex(ValueError,'datum offset must be exactly zero'):
            check_pavement(resources,piece)

    def test_barrier_face_moved_inside_the_car_corridor_is_rejected(self):
        resources,piece = fixture([(0.,-8.,7.5),(0.,8.,7.5)])
        iid = int(piece['tile_ids'][0],16)
        resources[*S3D,iid] = edit_vertices(resources[*S3D,iid],lambda point:
            (0.4,*point[1:]) if point[0] > 2.5 and point[1] > 7.55 else point)
        with self.assertRaisesRegex(ValueError,'solid triangle intrudes'):
            check_pavement(resources,piece)

    def test_saved_path_grade_is_measured_from_encoded_points(self):
        for key,raw in self.resources.items():
            if key[:2] != PATH:
                continue
            routes = saved_routes(raw)
            if routes and len(routes[0]['points']) > 6:
                point = routes[0]['points'][3]
                routes[0]['points'][3] = (*point[:2],point[2]+2.0)
                self.resources[key] = paths.encode_paths(routes)
                break
        with self.assertRaisesRegex(ValueError,'exceeds its declared maximum grade'):
            check_pavement(self.resources,self.piece)

    def test_unexpected_transport_flags_and_nonfinite_path_points_are_rejected(self):
        key = next(key for key,raw in self.resources.items() if key[:2] == PATH and saved_routes(raw))
        lines = [line for line in self.resources[key].decode('ascii').splitlines() if not line.startswith('--')]
        for index,value,message in ((5,'7','Unexpected highway PATH transport'),
                                    (7,'255','entry or exit flag'),
                                    (9,'9','junction flag'),
                                    (11,'nan,0,7.5','three finite')):
            changed = list(lines)
            changed[index] = value
            resources = dict(self.resources)
            resources[key] = ('\r\n'.join(changed)+'\r\n').encode('ascii')
            with self.subTest(value=value),self.assertRaisesRegex(ValueError,message):
                check_pavement(resources,self.piece)

    def test_only_exactly_declared_model_only_cells_may_have_zero_car_paths(self):
        self.assertTrue(self.piece['engineering']['model_only_cells'])
        self.piece['engineering']['model_only_cells'] = []
        with self.assertRaisesRegex(ValueError,'model-only cell contract'):
            check_pavement(self.resources,self.piece)
        piece = deepcopy(self.definition)
        key = next(key for key,raw in self.resources.items() if key[:2] == PATH and saved_routes(raw))
        self.resources[key] = EMPTY_PATH
        with self.assertRaisesRegex(ValueError,'model-only cell contract'):
            check_pavement(self.resources,piece)

    def test_measured_native_port_point_and_tangent_are_checked(self):
        ports = [{'direction':'in','point_m':[8.,3.2,7.6]},
                 {'direction':'out','point_m':[40.,19.2,0.0]}]
        with self.assertRaisesRegex(ValueError,'measured external port contract'):
            check_pavement(self.resources,self.piece,ports=ports)
        ports[0]['point_m'][2] = 7.5
        ports[0]['tangent'] = [-1.,1.]
        with self.assertRaisesRegex(ValueError,'tangent differs'):
            check_pavement(self.resources,self.piece,ports=ports)

    def test_actual_authored_atlas_colors_are_checked_separately_from_support(self):
        key = (*TEXTURE,int(self.piece['tile_ids'][0],16))
        raw = bytearray(self.resources[key])
        raw[40] ^= 0x10
        self.resources[key] = bytes(raw)
        with self.assertRaisesRegex(ValueError,'atlas color or opacity changed'):
            check_pavement(self.resources,self.piece)


if __name__ == '__main__':
    unittest.main()
