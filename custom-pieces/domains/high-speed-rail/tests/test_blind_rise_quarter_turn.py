"""Focused paired-rise controls: encoding, heights, directions, and collars."""
from copy import deepcopy
from pathlib import Path
import json
import unittest
from scp.catalog import load_catalog
from scp.track_paths import PATH, encode_paths
from scp.verify import parse_paths
from scp_hsr.hsr_components_layout import component_layout
from scp_hsr.hsr_components_verify import check_paths
from scp_hsr.hsr_blind_rise_verify import audit_shared_sheet, audit_native_collars, CONTRACTS, RECIPE
from scp_hsr.directional_t_verify import _journeys
from scp_hsr.interchange_verify import _encoded_routes
from scp_hsr.interchange_models import EMPTY_STRUCTURAL_PATH
from scp_hsr.test_support import floor

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'project.jsonc').is_file())

def fixture():
    spec = next(p for p in load_catalog(ROOT)['pieces'] if p['id']=='hsr-l2-and-l4-two-track-curve-ramp-90deg-right')
    layout = component_layout(RECIPE)
    resources = {(*PATH,int(t,16)):encode_paths(layout[tuple(c)]['routes'])
        if layout[tuple(c)]['routes'] else EMPTY_STRUCTURAL_PATH
        for c,t in zip(spec['cells'],spec['tile_ids'])}
    return spec,resources

def reencode(routes):
    lines=['SC4PATHS','1.2',str(len(routes)),'0','0']
    for r in routes:
        lines += [str(r[k]) for k in ('transport','lane','entry','exit','compatibility')]
        lines += [str(len(r['points']))]
        lines += [','.join(format(v,'.12g') for v in p) for p in r['points']]
    return ('\r\n'.join(lines)+'\r\n').encode('ascii')

def collars():
    result=[]
    for h in (15.5+.689326,15.5-1.48933):
        result += floor(-7.5,7.5,96.,104.,absolute_y=h)
    for a,b in ((-7.5,-5.9965477),(5.9965477,7.5)):
        result += floor(a,b,96.,104.,absolute_y=15.5+1.48933)
    for h in (30.5+.689326,30.5-1.48933):
        result += floor(96.,104.,-7.5,7.5,absolute_y=h)
    for a,b in ((-7.5,-5.9965477),(5.9965477,7.5)):
        result += floor(96.,104.,a,b,absolute_y=30.5+1.48933)
    return result

class PairedRiseTests(unittest.TestCase):
    def test_complete_two_direction_routes_and_four_rotations(self):
        spec,resources=fixture()
        r=check_paths(resources,spec)
        self.assertEqual(r['rotations_checked'],4)
        self.assertEqual(r['unique_complete_journeys_checked'],2)
        self.assertEqual(r['native_port_heights_m'],[15.5,30.5])
        self.assertLess(r['maximum_encoded_grade'],.12)
        self.assertEqual(r['physical_channels'],2)
        self.assertEqual(r['intermediate_exposed_custom_height_ports'],0)
        self.assertGreaterEqual(r['paired_shared_sheet_points_checked'],700)

    def test_changed_interior_height_and_lateral_position_are_rejected(self):
        spec,resources=fixture()
        journeys=_journeys(_encoded_routes(resources,spec,CONTRACTS[RECIPE]),CONTRACTS[RECIPE])
        for axis in (0,2):
            changed=deepcopy(journeys)
            p=list(changed['Ein','Sout'][200]);p[axis]+=.01
            changed['Ein','Sout'][200]=tuple(p)
            with self.assertRaisesRegex(ValueError,'shared-height sheet'):
                audit_shared_sheet(changed)

    def test_reversed_encoded_channel_is_rejected(self):
        spec,resources=fixture()
        for key,raw in resources.items():
            try:
                routes=parse_paths(raw)['routes']
            except ValueError:
                continue
            if routes:
                routes[0]['points'].reverse()
                routes[0]['entry'],routes[0]['exit']=routes[0]['exit'],routes[0]['entry']
                with self.assertRaises(ValueError):
                    check_paths({**resources,key:reencode(routes)},spec)
                break

    def test_removed_encoded_cell_creates_a_rejected_seam(self):
        spec,resources=fixture()
        key=(*PATH,int(spec['tile_ids'][-1],16))
        with self.assertRaises(ValueError):
            check_paths({**resources,key:EMPTY_STRUCTURAL_PATH},spec)

    def test_native_collar_thickness_and_internal_wall_controls(self):
        triangles=collars()
        self.assertEqual(audit_native_collars(triangles)['native_collar_slab_sections_checked'],12)
        missing=[t for t in triangles if not all(abs(p[1]-29.01067)<1e-5 for p in t)]
        with self.assertRaisesRegex(ValueError,'thickness'):
            audit_native_collars(missing)
        wall=((0.,16.5,96.,.1,0.),(0.,16.8,104.,.1,0.),(0.,16.5,104.,.1,0.))
        with self.assertRaisesRegex(ValueError,'internal wall'):
            audit_native_collars(triangles+[wall])

if __name__=='__main__':
    unittest.main()
