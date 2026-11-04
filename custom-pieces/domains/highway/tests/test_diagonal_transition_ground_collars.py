"""Finite actual-native ground shoulder, hosting, and sampled bridge controls."""
from pathlib import Path
import hashlib
import json
import math
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'framework'))
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0, SourcePackages(ROOT))
from scp import jsonc
from scp.dbpf import entries, decompress
from scp.paths import local_settings
from scp_highway import diagonal_transition as writer
from scp_highway import diagonal_transition_geometry as geometry
from scp_highway import diagonal_transition_layout as layout
from scp_highway import diagonal_transition_native as native
from scp_highway import diagonal_transition_ground_collars as collars
from shapely.geometry import Polygon, box
from shapely.ops import unary_union


def surface_height(triangle, east, north):
    a, b, c = triangle
    det = (b[1]-c[1])*(a[0]-c[0]) + (c[0]-b[0])*(a[1]-c[1])
    if not det:
        return None
    u = ((b[1]-c[1])*(east-c[0]) + (c[0]-b[0])*(north-c[1]))/det
    v = ((c[1]-a[1])*(east-c[0]) + (a[0]-c[0])*(north-c[1]))/det
    if min(u, v, 1-u-v) < -1e-10:
        return None
    return u*a[2] + v*b[2] + (1-u-v)*c[2]


class ActualDiagonalGroundCollarTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = local_settings(ROOT)
        if not path.is_file():
            raise unittest.SkipTest('Audited original NAM sources are not supplied in a portable clone')
        settings = jsonc.load(path)
        roots = [Path(settings['plugins']).expanduser(),
                 *(Path(p).expanduser() for p in settings.get('extra_plugins', []))]
        cls.context = {}
        for label, filename in [('dd_rhw', 'RealHighway_DD_RHW-4.dat'), ('rhw4', 'RealHighway_RHW-4.dat')]:
            found = {p for root in roots if root.is_dir() for p in root.rglob(filename)}
            if len(found) != 1:
                raise unittest.SkipTest('Exactly one original '+filename+' is required')
            cls.context[label] = {key: decompress(raw) for key, raw in entries(found.pop().read_bytes()).items()}
        cls.results = {}
        for variant in ('original', 'mirrored', 'opposite-side', 'opposite-side-mirrored'):
            section = writer.section_factory(cls.context, 0x7fdf0000, variant=variant)
            cls.results[variant] = collars.build_ground_collars(cls.context, variant=variant, middle_section=section)

    def test_real_negative_station_shoulder_is_kept_and_the_free_city_host_is_recut(self):
        for variant, result in self.results.items():
            literal = [group for group in result['groups'] if group['kind'] == 'literal-native']
            self.assertTrue(literal)
            # This finite native shoulder lies behind the nominal perpendicular
            # mouth. A station>=0 crop incorrectly deletes real source pavement.
            socket = next(row for row in native.socket_specs(variant) if row.arm == 'lower')
            negative = [Polygon([point[:2] for point in tri])
                for group in literal if group['deck'] == 'lower'
                for tri in group['triangles_ENHUV']
                if all(sum((point[i]-socket.mouth_en[i])*socket.inward_en[i] for i in range(2)) < 0.
                       for point in tri)]
            self.assertGreater(unary_union(negative).area, 2.)
            # The retained source has genuine positive area in the free leaf
            # cell; that area must be hosted there, rather than inventing a
            # dummy face or retaining an avoidable free-cell overhang.
            leaf = (-5, 4) if variant in ('mirrored', 'opposite-side') else (-6, 3)
            self.assertIn(leaf, layout.world_cells(variant=variant))
            hosted = [Polygon([point[:2] for point in tri])
                for group in literal if tuple(group['host_world_cell']) == leaf
                for tri in group['triangles_ENHUV']]
            self.assertTrue(hosted)
            self.assertGreater(unary_union(hosted).area, 1e-6)

    def test_every_literal_vertex_keeps_its_pinned_parent_fields_and_only_reserved_overhang(self):
        for variant, result in self.results.items():
            owned = set(layout.world_cells(variant=variant))
            for group in result['groups']:
                if group['kind'] != 'literal-native':
                    continue
                p = group['source_provenance']
                sources = native.source_faces(self.context, int(p['native_tile_id'], 16), p['pose'], p['world_cell'])
                source = next(row for row in sources if row['mesh_index'] == p['source_mesh_index'])
                parent = source['triangles'][p['source_parent_face_index']]
                a, b, c = parent
                det = (b[1]-c[1])*(a[0]-c[0]) + (c[0]-b[0])*(a[1]-c[1])
                for tri in group['triangles_ENHUV']:
                    for x in tri:
                        u = ((b[1]-c[1])*(x[0]-c[0])+(c[0]-b[0])*(x[1]-c[1]))/det
                        v = ((c[1]-a[1])*(x[0]-c[0])+(a[0]-c[0])*(x[1]-c[1]))/det
                        self.assertGreaterEqual(min(u, v, 1-u-v), -2e-12)
                        for axis in (2, 3, 4):
                            self.assertAlmostEqual(x[axis], u*a[axis]+v*b[axis]+(1-u-v)*c[axis], places=11)
                host = tuple(group['host_world_cell'])
                self.assertIn(host, owned)
                shape = unary_union([Polygon([point[:2] for point in tri]) for tri in group['triangles_ENHUV']])
                outside = shape.difference(box(16*host[0]-8, -16*host[1]-8, 16*host[0]+8, -16*host[1]+8))
                declared = p['retained_overhang_only_into_reserved_cells']
                reserved = [box(16*c-8, -16*r-8, 16*c+8, -16*r+8) for c, r in declared]
                self.assertTrue(all(layout.is_reserved_native_cell(tuple(cell), variant=variant) for cell in declared))
                self.assertLess(outside.difference(unary_union(reserved)).area, 1e-20)

    def test_one_metre_ground_bridge_samples_cubic_height_and_retains_ground_clamped_floor(self):
        start = geometry.LENGTH-geometry.COLLAR-1.
        end = geometry.LENGTH-geometry.COLLAR
        middle = next(s for s in geometry.STATIONS if start+.45 < s < start+.55)
        expected = geometry.height('upper', middle)+geometry.pavement_datum('upper', middle)
        first = geometry.height('upper', start)+geometry.pavement_datum('upper', start)
        last = geometry.height('upper', end)+geometry.pavement_datum('upper', end)
        chord = first+(last-first)*(middle-start)/(end-start)
        self.assertGreater(abs(expected-chord), 1e-5)
        for variant, result in self.results.items():
            centre, _normal = geometry.frame('upper', middle, variant=variant)
            surfaces = [height for group in result['groups']
                if group['kind'] == 'authored-ground-bridge' and group['role'] == 'upper-pavement-atlas'
                for tri in group['triangles_ENHUV']
                if (height := surface_height(tri, *centre)) is not None]
            self.assertTrue(surfaces)
            self.assertTrue(all(abs(h-expected) < 1e-11 for h in surfaces))
            floors = [height for group in result['groups']
                if group['kind'] == 'authored-ground-bridge' and group['role'] == 'upper-body'
                for tri in group['triangles_ENHUV']
                if (height := surface_height(tri, *centre)) is not None]
            self.assertTrue(floors)
            self.assertTrue(all(abs(h) < 1e-12 for h in floors))

    def test_owned_texture_phase_retains_measured_offsets_lateral_skew_and_both_ground_half_signs(self):
        direction = (-math.sqrt(.5), -math.sqrt(.5))
        for variant in self.results:
            fields = writer._atlas_native_fields(self.context, 0x7fdf0000, variant=variant)
            for deck in ('upper', 'lower'):
                for kind, rows in fields[deck].items():
                    if kind == 'ground':
                        # A global +s/16 or -s/16 rule necessarily loses one
                        # real alternating half, regardless of traffic phase.
                        self.assertEqual({math.copysign(1., row['dUV_d_station_m'][1]) for row in rows}, {-1., 1.})
                        self.assertTrue(any(abs(row['dUV_d_station_m'][0]) > 1e-6 for row in rows))
                    for row in rows:
                        sources = native.source_faces(self.context, int(row['native_tile_id'], 16),
                                                      row['pose'], row['source_world_cell'])
                        parents = [tri for group in sources for tri in group['triangles']
                            if hashlib.sha256(json.dumps(tri, separators=(',', ':')).encode()).hexdigest()
                            == row['source_parent_ENHUV_sha256']]
                        self.assertEqual(len(parents), 1)
                        a, b, c = parents[0]
                        dx, dy, ex, ey = b[0]-a[0], b[1]-a[1], c[0]-a[0], c[1]-a[1]
                        det = dx*ey-dy*ex
                        for index, axis in enumerate((3, 4)):
                            first, second = b[axis]-a[axis], c[axis]-a[axis]
                            ge, gn = (first*ey-second*dy)/det, (dx*second-ex*first)/det
                            expected_slope = ge*direction[0]+gn*direction[1]
                            self.assertAlmostEqual(row['dUV_d_station_m'][index], expected_slope, places=12)
                        if kind == 'dd':
                            self.assertLess(row['dUV_d_station_m'][1], -.0624)
                            u = row['lateral_interval_m'][0]
                            centre, normal = geometry.frame(deck, row['reference_station_m'], variant=variant)
                            east, north = (centre[i]+u*normal[i] for i in range(2))
                            det = (b[1]-c[1])*(a[0]-c[0])+(c[0]-b[0])*(a[1]-c[1])
                            x = ((b[1]-c[1])*(east-c[0])+(c[0]-b[0])*(north-c[1]))/det
                            y = ((c[1]-a[1])*(east-c[0])+(a[0]-c[0])*(north-c[1]))/det
                            for index, axis in enumerate((3, 4)):
                                expected_uv = x*a[axis]+y*b[axis]+(1-x-y)*c[axis]
                                self.assertAlmostEqual(row['UV_at_first_lateral'][index], expected_uv, places=11)


if __name__ == '__main__':
    unittest.main()
