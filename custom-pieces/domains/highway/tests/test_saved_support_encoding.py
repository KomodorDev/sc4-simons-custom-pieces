"""Reopen serialized pavement and bound the scoped float32 support precision."""
import hashlib
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[3]
sys.path[:0]=[str(ROOT/'framework'),str(ROOT/'domains/highway/implementation')]
from scp.models import parse_s3d,pack_s3d
from scp.recipes import combine_meshes
from scp_highway.ramp_geometry import pack_road_model,road_material
from scp_highway import ramp_verify as verify

DD=0x5713000E
FIELD={'geometry_key':'lower-exit-branch','field_controls':{'passed':True}}


def quad(low,high,height):
    points=((low,height,-1.,.6,0.),(low,height,1.,.6,.1),
            (high,height,1.,.7,.1),(high,height,-1.,.7,0.))
    return [tuple(points[i] for i in indices) for indices in ((0,1,2),(0,2,3))]


def saved_faces(gap=1e-6,*,right_height=7.5,right_texture=DD,absent=False,changed_flags=False):
    left=parse_s3d(pack_road_model(quad(0.,1.,7.5),DD))
    models=[left]
    if not absent:
        right=parse_s3d(pack_road_model(quad(1.+gap,2.,right_height),right_texture))
        if changed_flags:
            raw=bytearray(right['materials'][0]['raw']);raw[4]^=1
            right['materials'][0]['raw']=bytes(raw)
        models.append(right)
    model=combine_meshes([(m,m['meshes'],(0.,0.,0.))for m in models])
    # Geometry and material changes are serialized and decoded before checks.
    return verify._triangles(pack_s3d(model),(0,0))


class SavedSupportEncodingTests(unittest.TestCase):
    def setUp(self):
        # Portable materials exercise exact digest matching without embedding
        # native bytes. Production uses the independently pinned NAM digest.
        portable=hashlib.sha256(road_material(DD)['raw']).hexdigest()
        self.pin=patch.object(verify,'DD_MATERIAL_SHA256',portable)
        self.pin.start();self.addCleanup(self.pin.stop)
        self.first,self.last=(.1,0.,7.5),(1.9,0.,7.5)

    def test_default_stays_strict_and_scoped_report_records_the_actual_gap(self):
        faces=saved_faces()
        self.assertFalse(verify._covered(self.first,self.last,faces))
        report={'admitted_spans':0,'admitted_endpoint_spans':0,'maximum_admitted_along_path_span_m':0.,
                'distance_samples_checked':0,'maximum_sampled_distance_m':0.}
        self.assertTrue(verify._covered(self.first,self.last,faces,encoding=FIELD,precision_report=report))
        self.assertEqual(report['admitted_spans'],1)
        self.assertEqual(report['admitted_endpoint_spans'],0)
        self.assertGreater(report['maximum_admitted_along_path_span_m'],0.)
        self.assertLessEqual(report['maximum_sampled_distance_m'],2e-6)

    def test_serialized_holes_above_the_physical_cap_are_rejected(self):
        # A 5 micrometre hole has a centre more than 2 micrometres from
        # either actual pavement edge. The test checks distance, not length.
        for gap in (5e-6,1e-4,.01):
            with self.subTest(gap=gap):
                self.assertFalse(verify._covered(self.first,self.last,saved_faces(gap),encoding=FIELD))

    def test_raised_absent_or_different_material_cannot_bridge_a_gap(self):
        for options in ({'right_height':7.501},{'absent':True},
                        {'right_texture':0x5712000E},{'changed_flags':True}):
            with self.subTest(options=options):
                self.assertFalse(verify._covered(self.first,self.last,saved_faces(gap=3e-6,**options),encoding=FIELD))

    def test_unknown_branch_missing_field_proof_ground_and_grade_stay_strict(self):
        faces=saved_faces()
        for encoding in ({'geometry_key':'unrelated','field_controls':{'passed':True}},
                         {'geometry_key':'lower-exit-branch'},
                         {'geometry_key':'lower-exit-branch','field_controls':{'passed':False}}):
            with self.subTest(encoding=encoding):
                self.assertFalse(verify._covered(self.first,self.last,faces,encoding=encoding))
        ground=[{**f,'points':tuple((x,y,0.)for x,y,_h in f['points'])}for f in faces]
        self.assertFalse(verify._covered((.1,0.,0.),(1.9,0.,0.),ground,encoding=FIELD))
        self.assertFalse(verify._covered(self.first,(1.9,0.,7.50001),faces,encoding=FIELD))

    def test_leading_and_trailing_endpoint_allowances_are_also_capped(self):
        faces=saved_faces(gap=0.)
        for first,last in (((-1e-6,0.,7.5),self.last),(self.first,(2.+1e-6,0.,7.5))):
            with self.subTest(first=first,last=last):
                self.assertFalse(verify._covered(first,last,faces))
                self.assertTrue(verify._covered(first,last,faces,encoding=FIELD))
        self.assertFalse(verify._covered((-3e-6,0.,7.5),self.last,faces,encoding=FIELD))
        self.assertFalse(verify._covered(self.first,(2.+3e-6,0.,7.5),faces,encoding=FIELD))

    def test_long_parallel_rounding_sliver_uses_distance_and_rejects_larger_offset(self):
        raw=pack_road_model(quad(0.,2.,7.5),DD)
        faces=verify._triangles(raw,(0,0))
        first,last=(.1,1.+5e-7,7.5),(1.9,1.+5e-7,7.5)
        self.assertFalse(verify._covered(first,last,faces))
        self.assertTrue(verify._covered(first,last,faces,encoding=FIELD))
        self.assertFalse(verify._covered((.1,1.+2.1e-6,7.5),(1.9,1.+2.1e-6,7.5),faces,encoding=FIELD))

    def test_acute_corner_does_not_receive_an_unbounded_miter_extension(self):
        triangle=((-7.,7.5,.0001,.6,0.),(7.,7.5,0.,.7,.1),(-7.,7.5,-.0001,.6,.2))
        faces=verify._triangles(pack_road_model([triangle],DD),(0,0))
        self.assertFalse(verify._covered((7.0001,0.,7.5),(7.001,0.,7.5),faces,encoding=FIELD))
        self.assertFalse(verify._covered(self.first,self.last,[],encoding=FIELD))


if __name__=='__main__':unittest.main()
