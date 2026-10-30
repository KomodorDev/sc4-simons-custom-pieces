"""Measure saved slip-lane paint independently of its authoring helpers."""
from __future__ import annotations

import math
import struct

from scp.models import parse_s3d
from scp.track_paths import S3D

ROOT_TWO = math.sqrt(2.)
WHITE_CORE_WIDTH_M = .25
WIDTH_TOLERANCE_M = .001
POSITION_TOLERANCE_M = 2e-5
# Measured native join stations and accepted auxiliary-lane lengths. Each
# local frame looks from the highway towards its ramp, including entrances.
MOUTHS = (("lower-off", 75.80184694319789, -1, 1, 7.5, 12., 4.),
          ("lower-on", -75.80184694319789, 1, 1, 7.5, 12., 4.),
          ("upper-off", -109.74297244015216, 1, -1, 15., 16., 8.),
          ("upper-on", 109.74297244015214, -1, -1, 15., 16., 8.))

# Reviewed paint-only design controls. Native seam positions/tangents were
# independently decoded from accepted saved MIS faces, not writer helpers.
CONTRACTS = {'lower-off': {'nose': [18.876620416142387, 4.5],
               'outer_controls': [[12.128963600783806, 7.0],
                                  [13.46229693411714, 7.0],
                                  [15.809008612572992, 7.5],
                                  [16.128963600783806, 8.0]],
               'inner_controls': [[22.56731395684775, 7.0],
                                  [23.123572942306367, 7.313191102980563],
                                  [23.67983192776498, 7.670474206442252],
                                  [24.236090913223595, 8.0]],
               'inner_pre_ease_sections': [{'q': 5.0,
                                            'point': [19.54059030967961, 5.0],
                                            'outward_unit_tangent_sq': [0.7827471137312129,
                                                                        0.622339903867216]},
                                           {'q': 5.75,
                                            'point': [20.475356042760286, 5.75],
                                            'outward_unit_tangent_sq': [0.7928868570067732,
                                                                        0.6093688800602807]},
                                           {'q': 6.5,
                                            'point': [21.668398647572005, 6.5],
                                            'outward_unit_tangent_sq': [0.8764633475505484,
                                                                        0.4814685871378178]}],
               'hatches': [[[21.876620416142387, 4.875], [21.045419641831916, 5.706200774310471]],
                           [[23.376620416142387, 4.875], [21.99824738512015, 6.253373031022236]]]},
 'lower-on': {'nose': [18.876620416142412, 4.5],
              'outer_controls': [[12.129513418533207, 7.0],
                                 [13.462846751866541, 7.0],
                                 [15.81435982775504, 7.5],
                                 [16.129513418533207, 8.0]],
              'inner_controls': [[22.56731395684776, 7.0],
                                 [23.12357295422148, 7.313191109689172],
                                 [23.679831951595204, 7.670469663864008],
                                 [24.236090948968926, 8.0]],
              'inner_pre_ease_sections': [{'q': 5.0,
                                           'point': [19.54059030967963, 5.0],
                                           'outward_unit_tangent_sq': [0.782747113731237,
                                                                       0.6223399038671857]},
                                          {'q': 5.75,
                                           'point': [20.475356042760303, 5.75],
                                           'outward_unit_tangent_sq': [0.7928868570067706,
                                                                       0.6093688800602839]},
                                          {'q': 6.5,
                                           'point': [21.668398647572, 6.5],
                                           'outward_unit_tangent_sq': [0.8764633475505632,
                                                                       0.48146858713779106]}],
              'hatches': [[[21.876620416142412, 4.875], [21.04541964183194, 5.706200774310471]],
                          [[23.376620416142412, 4.875], [21.99824738512017, 6.253373031022242]]]},
 'upper-off': {'nose': [28.127472184198716, 4.5],
               'outer_controls': [[20.8458384371377, 7.0],
                                  [22.179171770471033, 7.0],
                                  [23.87788966004066, 7.5],
                                  [24.8458384371377, 8.0]],
               'inner_controls': [[34.10911955612607, 7.0],
                                  [34.957862480077914, 7.314833589369416],
                                  [35.80660540402976, 7.670576856776505],
                                  [36.655348327981606, 8.0]],
               'inner_pre_ease_sections': [{'q': 5.0,
                                            'point': [29.183682828907735, 5.0],
                                            'outward_unit_tangent_sq': [0.8987657034983982,
                                                                        0.43842925337507893]},
                                           {'q': 5.75,
                                            'point': [30.755052025849604, 5.75],
                                            'outward_unit_tangent_sq': [0.9131030147045766,
                                                                        0.4077289351240771]},
                                           {'q': 6.5,
                                            'point': [32.742534947055724, 6.5],
                                            'outward_unit_tangent_sq': [0.9407647167042353,
                                                                        0.3390600946799843]}],
               'hatches': [[[31.127472184198716, 4.875], [30.692350181074218, 5.310122003124498]],
                           [[32.627472184198716, 4.875], [31.754140767895926, 5.74833141630279]],
                           [[34.127472184198716, 4.875], [32.85908013478987, 6.143392049408848]],
                           [[35.627472184198716, 4.875], [33.958149537137786, 6.544322647060929]]]},
 'upper-on': {'nose': [28.127472184198616, 4.5],
              'outer_controls': [[20.847385462731395, 7.0],
                                 [22.180718796064728, 7.0],
                                 [23.839133582359214, 7.5],
                                 [24.847385462731395, 8.0]],
              'inner_controls': [[34.10911955612608, 7.0],
                                 [34.95786207208959, 7.314833438029755],
                                 [35.80660458805309, 7.670580205852454],
                                 [36.6553471040166, 8.0]],
              'inner_pre_ease_sections': [{'q': 5.0,
                                           'point': [29.183682828907628, 5.0],
                                           'outward_unit_tangent_sq': [0.8987657034984253,
                                                                       0.43842925337502336]},
                                          {'q': 5.75,
                                           'point': [30.75505202584953, 5.75],
                                           'outward_unit_tangent_sq': [0.9131030147046509,
                                                                       0.4077289351239104]},
                                          {'q': 6.5,
                                           'point': [32.74253494705571, 6.5],
                                           'outward_unit_tangent_sq': [0.9407647167042562,
                                                                       0.33906009467992626]}],
              'hatches': [[[31.127472184198616, 4.875], [30.692350181074126, 5.310122003124493]],
                          [[32.627472184198616, 4.875], [31.754140767895848, 5.748331416302769]],
                          [[34.127472184198616, 4.875], [32.85908013478979, 6.143392049408826]],
                          [[35.627472184198616, 4.875], [33.958149537137714, 6.544322647060902]]]}}


def _need(value, message):
    if not value:
        raise ValueError(message)


def _cross(a, b):
    return a[0]*b[1] - a[1]*b[0]


def _section(triangle, centre, normal):
    """Intersect a transverse measurement line with one saved paint face."""
    signed = _cross((triangle[1][0]-triangle[0][0], triangle[1][1]-triangle[0][1]),
                    (triangle[2][0]-triangle[0][0], triangle[2][1]-triangle[0][1]))
    if abs(signed) < 1e-12:
        return None
    sense = 1. if signed > 0. else -1.
    low, high = -.4, .4
    for first, last in zip(triangle, triangle[1:]+triangle[:1]):
        edge = last[0]-first[0], last[1]-first[1]
        offset = sense*_cross(edge, (centre[0]-first[0], centre[1]-first[1]))
        rate = sense*_cross(edge, normal)
        if abs(rate) < 1e-12:
            if offset < -1e-9:
                return None
            continue
        boundary = -offset/rate
        if rate > 0.:
            low = max(low, boundary)
        else:
            high = min(high, boundary)
        if high < low - 1e-9:
            return None
    return low, high


def _span(triangles, centre, tangent):
    length = math.hypot(*tangent)
    normal = -tangent[1]/length, tangent[0]/length
    intervals = sorted(part for triangle in triangles
                       if (part := _section(triangle, centre, normal)) is not None)
    merged = []
    for low, high in intervals:
        if merged and low <= merged[-1][1] + 2e-5:
            merged[-1] = merged[-1][0], max(high, merged[-1][1])
        else:
            merged.append((low, high))
    matches = [(low, high) for low, high in merged if low <= 1e-5 and high >= -1e-5]
    _need(len(matches) == 1, 'Saved slip-lane marking is missing or disconnected at its width section')
    low, high = matches[0]
    _need(low > -.399 and high < .399, 'Saved slip-lane marking exceeds the width measurement window')
    return low, high


def _width(triangles, centre, tangent):
    low, high = _span(triangles, centre, tangent)
    return high-low


def _bezier(controls, t):
    a,b,c,d = controls
    point = tuple((1-t)**3*a[i]+3*(1-t)**2*t*b[i]+3*(1-t)*t*t*c[i]+t**3*d[i] for i in (0,1))
    tangent = tuple(3*((1-t)**2*(b[i]-a[i])+2*(1-t)*t*(c[i]-b[i])+t*t*(d[i]-c[i])) for i in (0,1))
    return point,tangent


def _present(triangles, point):
    # Saved float32 positions can place the exact q=8 boundary a few
    # micrometres from its reviewed double-precision endpoint. Keep this
    # bounded tolerance separate from the unchanged width measurement.
    for triangle in triangles:
        signed = _cross((triangle[1][0]-triangle[0][0], triangle[1][1]-triangle[0][1]),
                        (triangle[2][0]-triangle[0][0], triangle[2][1]-triangle[0][1]))
        if abs(signed) < 1e-12:
            continue
        sense = 1. if signed > 0. else -1.
        if all(sense*_cross((b[0]-a[0],b[1]-a[1]), (point[0]-a[0],point[1]-a[1]))
               >= -POSITION_TOLERANCE_M*math.hypot(b[0]-a[0],b[1]-a[1])
               for a,b in zip(triangle,triangle[1:]+triangle[:1])):
            return True
    return False


def check_faces(faces):
    """Measure bounded indexed-paint widths, alignment, hatches, and handoffs.

    Expected positions are literal reviewed geometry contracts. Triangle
    unions supply measured widths and centres after decoding; no authoring
    helper supplies expected or measured geometry. Native filtered fringes,
    complete polygon clearance, and game rendering remain separate checks.
    """
    results, hatch_results, continuity = [], [], 0
    for name, station, direction, side, height, taper, parallel in MOUTHS:
        triangles = []
        for face in faces:
            if face['texture'] != 0x5713000E or any(abs(p[2]-height-.01) > 1e-5 for p in face['points']):
                continue
            triangles.append(tuple((direction*((p[0]+p[1])/ROOT_TWO-station),
                                    side*(p[1]-p[0]+136.)/ROOT_TWO) for p in face['points']))
        _need(triangles, f'Saved slip-lane marking geometry is absent at {name}')
        contract = CONTRACTS[name]
        outer,inner = contract['outer_controls'],contract['inner_controls']
        join = 20.197995366891178 if name.startswith('lower') else 30.94286762967826
        cases = [('dash',(9. if name.startswith('lower') else 13.,4.5),(1.,0.)),
                 ('taper',(taper/2.,5.75),(1.,4.6875/taper)),
                 ('parallel',((taper+outer[0][0])/2.,7.),(1.,0.)),
                 ('gore-mainline',((contract['nose'][0]+join)/2.,4.5),(1.,0.))]
        cases += [('gore-rail',row['point'],row['outward_unit_tangent_sq'])
                  for row in contract['inner_pre_ease_sections']]
        for kind,controls in (('outer-connector',outer),('inner-connector',inner)):
            for fraction in (.25,.5,.75):
                point,tangent = _bezier(controls,fraction)
                cases.append((kind,point,tangent))
            # Near-seam point coverage includes the exact independently
            # measured handoff, without claiming full width at the q=8 clip.
            for fraction in (.9,.97,.995,1.):
                point,_tangent = _bezier(controls,fraction)
                _need(_present(triangles,point),f'Saved {name} {kind} handoff is disconnected')
                continuity += 1
        # The reviewed split point must belong to the joined V stroke.
        nose = contract['nose']
        _need(_present(triangles,nose),f'Saved {name} gore nose is misplaced or missing')
        continuity += 1
        for fraction in (.05,.95):
            point = (nose[0]+fraction*(join-nose[0]),4.5)
            _need(_present(triangles,point),f'Saved {name} native mainline handoff is disconnected')
            continuity += 1
        for index,(first,last) in enumerate(contract['hatches']):
            tangent = last[0]-first[0],last[1]-first[1]
            length = math.hypot(*tangent)
            normal = -tangent[1]/length,tangent[0]/length
            measured=[]
            for fraction in (.35,.65):
                point=tuple(a+fraction*(b-a) for a,b in zip(first,last))
                low,high=_span(triangles,point,tangent)
                measured.append(tuple(point[i]+(low+high)/2.*normal[i] for i in (0,1)))
            actual = measured[1][0]-measured[0][0],measured[1][1]-measured[0][1]
            angle = (math.degrees(math.atan2(actual[1],actual[0]))+90.)%180.-90.
            _need(abs(angle+45.) <= .5,f'Saved {name} hatch is not aligned at -45 degrees')
            hatch_results.append({'mouth':name,'hatch':index,'angle_degrees':angle})
            cases += [('hatch',point,actual) for point in measured]
        for kind,centre,tangent in cases:
            low,high = _span(triangles,centre,tangent)
            width = high-low
            _need(abs(width-WHITE_CORE_WIDTH_M) <= WIDTH_TOLERANCE_M,
                  f'Saved {name} {kind} white-stripe width differs from the native 0.25 m core')
            _need(abs((low+high)/2.) <= .003,f'Saved {name} {kind} marking is offset from its reviewed centre')
            results.append({'mouth':name,'kind':kind,'width_m':width})
    return {'passed':True,'ramp_mouths_checked':len(MOUTHS),
            'perpendicular_width_sections_checked':len(results),
            'native_white_core_width_m':WHITE_CORE_WIDTH_M,'width_tolerance_m':WIDTH_TOLERANCE_M,
            'reviewed_centre_tolerance_m':.003,'hatches_checked':len(hatch_results),
            'hatch_angle_tolerance_degrees':.5,'nose_and_handoff_points_checked':continuity,
            'point_position_tolerance_m':POSITION_TOLERANCE_M,
            'sections':results,'hatches':hatch_results,'game_rendering_tested':False,
            'coverage_limit':'Bounded saved triangle-union widths, reviewed gore/mainline centres, hatch angles, acute noses, and near-seam point continuity at four mouths; this does not certify every stroke point, full polygon/barrier clearance, native filtered fringes, or game appearance.'}


def check_saved_markings(owners, piece_resources):
    faces = []
    for owner in owners.values():
        model = parse_s3d(piece_resources[owner['piece_id']][*S3D, owner['tile']+4])
        for mesh in model['meshes']:
            _need(len(mesh['frames']) == 1, 'Marking check requires a static saved model')
            vi, ii, pi, mi = mesh['frames'][0]
            textures = model['materials'][mi]['textures']
            if textures != [0x5713000E]:
                continue
            block = model['vertices'][vi]
            vertices = [struct.unpack_from('<5f', block['data'], offset)
                        for offset in range(0, len(block['data']), block['stride'])]
            indices = model['indices'][ii]['values']
            for kind, first, count in model['primitives'][pi]:
                _need(kind == 0 and count % 3 == 0, 'Marking check requires indexed triangle lists')
                for offset in range(first, first+count, 3):
                    points = []
                    for index in indices[offset:offset+3]:
                        point = vertices[index]
                        east = point[0]+16.*owner['local_cell'][0]
                        north = -point[2]-16.*owner['local_cell'][1]
                        for _ in range(owner['angle']//90):
                            east, north = -north, east
                        points.append((east+owner['origin'][0], north+owner['origin'][1], point[1]))
                    faces.append({'texture': textures[0], 'points': tuple(points)})
    return check_faces(faces)
