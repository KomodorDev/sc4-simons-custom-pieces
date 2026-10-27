"""Independent literal contracts for the one-piece paired L2/L4 turn.

No geometry writer or layout INFO is imported here. These are the accepted
external ports, construction mask, native collar sections, and support plan.
"""
import math
from scp.dbpf import require

RECIPE = 'hsr_component_blind_rise_quarter_turn'
QUALITY = {'max_length_ratio': 1.55, 'min_total_turn_degrees': 89.,
    'max_total_turn_degrees': 91., 'max_sample_turn_degrees': 8.,
    'max_raw_turn_degrees': 3., 'min_radius_m': 50.,
    'max_curvature_change_per_m2': .0015,
    'max_endpoint_curvature_per_m': .0005, 'max_grade_change_per_m': .011,
    'min_length_m': 175., 'max_length_m': 184.}
CONTRACTS = {RECIPE: {
    'kind': 'paired_curved_grade', 'footprint': (7, 7), 'cost': 2000,
    'cells': [(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(0,1),(1,1),(2,1),(3,1),(4,1),
              (0,2),(1,2),(2,2),(0,3),(1,3),(0,4),(1,4),(0,5),(0,6)],
    'structural_cells': [(1,0),(0,1),(3,1),(4,1),(2,2),(1,3),(1,4)],
    'ports': {'Sin': (2.,-104.,15.5), 'Sout': (-2.,-104.,15.5),
              'Ein': (104.,2.,30.5), 'Eout': (104.,-2.,30.5)},
    'port_vectors': {'Sin': (0.,1.), 'Sout': (0.,-1.), 'Ein': (-1.,0.), 'Eout': (1.,0.)},
    'movements': [('Sin','Eout'),('Ein','Sout')],
    'min_height': 15.5, 'max_height': 30.5, 'max_grade': .12, 'flat_collar_m': 8.,
    'clearance_width_m': 5., 'minimum_clearance': 5.,
    'foundation_width_m': 1.3, 'minimum_support_spacing_m': 16.,
    'allow_same_edge': False, 'required_grade_separated_crossings': 0,
    'support_centres_xz': [(48.,0.),(64.,0.),(80.,0.),(96.,0.),(16.,16.),(32.,16.),
                           (16.,32.),(0.,48.),(0.,64.),(0.,80.),(0.,96.)],
    'quality_limits': {('Sin','Eout'): {**QUALITY,'signed_turn_degrees': -90.},
                       ('Ein','Sout'): {**QUALITY,'signed_turn_degrees': 90.}},
}}


def audit_shared_sheet(journeys):
    # Matching original station vertices proves equal height and 4 m spacing.
    # Tile-plane cuts are independently checked by the graph and bed audits.
    a, b = journeys['Sin','Eout'], list(reversed(journeys['Ein','Sout']))
    count, max_spacing_error, max_height_error = 0, 0., 0.
    for first, other in ((a,b),(b,a)):
        for p in first:
            if any(abs(v-(16.*round((v+8.)/16.)-8.)) <= 2e-6 for v in p[:2]):
                continue
            candidates = [(abs(math.dist(p[:2],q[:2])-4.),abs(p[2]-q[2]))
                          for q in other if abs(p[2]-q[2]) <= 2e-6]
            require(candidates, 'Paired rise tracks lost their shared-height sheet')
            spacing, height = min(candidates)
            require(spacing <= 3e-6 and height <= 2e-6,
                    'Paired rise tracks lost their four-metre shared-height sheet')
            max_spacing_error = max(max_spacing_error,spacing)
            max_height_error = max(max_height_error,height)
            count += 1
    require(count >= 700, 'Paired rise lacks its complete shared-sheet station proof')
    return {'paired_shared_sheet_points_checked':count,
            'maximum_paired_spacing_error_m':max_spacing_error,
            'maximum_paired_height_error_m':max_height_error,
            'physical_channels':2,'intermediate_exposed_custom_height_ports':0}


def audit_native_collars(triangles):
    # Inspect real compiled triangles at three stations in both flat collars.
    from .hsr_components_verify import _section_intervals
    triangles = list(triangles)
    swapped = [tuple((p[2],p[1],p[0],p[3],p[4]) for p in tri) for tri in triangles]
    count = 0
    for surfaces, height in ((triangles,15.5),(swapped,30.5)):
        for distance in (.5,4.,7.5):
            plane = 104.-distance
            for absolute, floor in ((height+.689326,True),(height-1.48933,False)):
                actual = _section_intervals(surfaces,plane,absolute,floor=floor)
                require(len(actual)==1 and abs(actual[0][0]+7.5)<.00005
                        and abs(actual[0][1]-7.5)<.00005,
                        'Paired rise native collar slab width, continuity, or thickness differs')
                count += 1
            caps = _section_intervals(surfaces,plane,height+1.48933)
            expected = [(-7.5,-5.9965477),(5.9965477,7.5)]
            require(len(caps)==2 and all(abs(a-c)<.00005 and abs(b-d)<.00005
                    for (a,b),(c,d) in zip(caps,expected)),
                    'Paired rise native collar parapet differs')
            for tri in surfaces:
                intersections=[]
                for a,b in zip(tri,tri[1:]+tri[:1]):
                    if abs(a[2]-plane)<=2e-6:
                        intersections.append(a)
                    if a[2]<plane<b[2] or b[2]<plane<a[2]:
                        t=(plane-a[2])/(b[2]-a[2])
                        intersections.append(tuple(a[k]+t*(b[k]-a[k]) for k in range(5)))
                require(not any(-5.9964<p[0]<5.9964 and height+.889326<p[1]<height+1.4894
                                for p in intersections),
                        'Paired rise collar has an internal wall')
    return {'native_collar_slab_sections_checked':count,'native_paired_slab_width_m':15.,
            'flat_collar_length_m':8.,'physical_connection_heights_m':[15.5,30.5]}
