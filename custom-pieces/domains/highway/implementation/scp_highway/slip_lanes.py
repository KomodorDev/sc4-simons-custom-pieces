"""Flat shoulder auxiliary lanes and native-material merge/diverge markings.

All coordinates use the existing highway u/v frame. Retained outer ramp
points and meshes remain authoritative beyond the original 8 m deck edge.
"""
from copy import deepcopy
import math

ASPHALT = 1.125
WHITE = 1.375
AUXILIARY_V = 5.5
SEPARATOR_V = (3.2 / math.sqrt(2.0) + AUXILIARY_V) / 2.0
SHOULDER_OUTER_V = 8.0 - .828125
# Native DD pavement uses U=0.5-q/16 on the served shoulder. Columns 26–28
# contain the old white edge; centres 25 and 29 bound its filtered footprint.
NATIVE_EDGE_ERASE_V = (4.3125, 4.8125)
NATIVE_EDGE_ASPHALT_U = 29.5 / 128.0
PAINT_HEIGHT = .01
SEAM_STEP = 2.**-20


def canonical_seam_vertex(point, cell):
    """Give both saved sides of the diagonal deck edge one binary line.

    Independent float32 clipping can place the native edge and authored edge
    on opposite sides of their mathematical line. One shared dyadic constant
    preserves encoded collinearity through later native face subdivision.
    PATH samples and every vertex away from this boundary remain unchanged.
    """
    if point[1] < 6.4:
        return point
    x,z = point[0]+16.*cell[0],point[2]+16.*cell[1]
    v = (-z-x+8.)/math.sqrt(2.)
    if abs(abs(v)-8.) > 2e-5:
        return point
    side = 1 if v>0 else -1
    constant = 8.-side*8.*math.sqrt(2.)-16.*sum(cell)
    # A transverse native diagonal meets this edge at half the sum/difference
    # constants. Use a two-ULP constant so that intersection is also exactly
    # representable in every local float32 buffer.
    constant = round(constant/(2.*SEAM_STEP))*(2.*SEAM_STEP)
    local_x = round(point[0]/SEAM_STEP)*SEAM_STEP
    transverse = x-z
    native_transverse = round(transverse/16.)*16.
    if abs(abs(point[2])-8.) < 1e-7:
        local_z = math.copysign(8.,point[2])
        local_x = constant-local_z
    elif abs(transverse-native_transverse)<2e-5:
        difference = native_transverse-16.*(cell[0]-cell[1])
        local_x = (constant+difference)/2.
        local_z = (constant-difference)/2.
    else:
        local_z = constant-local_x
    return local_x,point[1],local_z,*point[3:]


def native_seam_services(ramps):
    """Bound seam repair to the actual deck and side served by each ramp."""
    from .ramp_geometry import _branch_footprints
    services = []
    for ramp in ramps:
        data = profile(ramp)
        stations = [data['u0'], data['u0']+data['direction']*data['join_s']]
        stations.extend((x-z)/math.sqrt(2.)
                        for footprint in _branch_footprints(ramp) for x,z in footprint)
        services.append((ramp['height_m'], ramp['side'], min(stations), max(stations)))
    return services


def canonical_native_seam_vertex(point, cell, services):
    """Repair only a requested ramp's native seam, leaving other decks exact."""
    x = point[0]+16.*cell[0]
    z = point[2]+16.*cell[1]
    u,v = (x-z)/math.sqrt(2.),(-z-x+8.)/math.sqrt(2.)
    for height,side,first,last in services:
        if (height-1.0001 <= point[1] <= height+1.390635
                and abs(side*v-8.) <= 2e-5 and first-2e-5 <= u <= last+2e-5):
            return canonical_seam_vertex(point, cell)
    return point


def profile(ramp):
    """Describe one native-anchored flat auxiliary lane, looking outwards."""
    from .ramp_geometry import highway_coordinates
    points = ramp.get('mesh_points', ramp['points'])
    outward = points if ramp['direction'] == 'off' else list(reversed(points))
    u0, v0 = highway_coordinates(outward[0])
    direction = 1 if highway_coordinates(outward[1])[0] > u0 else -1
    join = next(index for index, point in enumerate(outward)
                if ramp['side'] * highway_coordinates(point)[1] >= 8.)
    uj, vj = highway_coordinates(outward[join])
    lower = ramp['deck'] == 'lower'
    taper, parallel = (12., 4.) if lower else (16., 8.)
    return {'outward': outward, 'u0': u0, 'v0': v0, 'direction': direction,
            'join_index': join, 'join_s': (uj-u0)*direction, 'join_v': ramp['side']*vj,
            'taper_m': taper, 'parallel_m': parallel, 'departure_s': taper+parallel,
            'side': ramp['side'], 'height': ramp['height_m']}


def apply(ramp):
    """Replace only the level high prefix; retain every original outer point."""
    from .ramp_geometry import highway_coordinates, world_coordinates
    result = deepcopy(ramp)
    data = profile(ramp)
    points, side, direction = data['outward'], data['side'], data['direction']
    u0, height = data['u0'], data['height']
    taper, departure, join_s = data['taper_m'], data['departure_s'], data['join_s']
    if join_s <= departure:
        raise ValueError('Auxiliary lane has no room to rejoin its retained ramp')
    following = highway_coordinates(points[data['join_index']+1])
    current = highway_coordinates(points[data['join_index']])
    slope = side * (following[1]-current[1]) / ((following[0]-current[0])*direction)
    prefix = [points[0], points[1]]  # Keep the exact native 1 cm collar.
    lane = abs(data['v0'])
    for index in range(1, int(taper*8)+1):
        s = index/8.
        t = s/taper
        smooth = t*t*t*(10.+t*(-15.+6.*t))
        v = lane+(AUXILIARY_V-lane)*smooth
        prefix.append(world_coordinates(u0+direction*s, side*v, height))
    for index in range(1, int(data['parallel_m']*8)+1):
        s = taper+index/8.
        prefix.append(world_coordinates(u0+direction*s, side*AUXILIARY_V, height))
    count = max(8, math.ceil((join_s-departure)*8))
    span = join_s-departure
    for index in range(1, count):
        t = index/count
        v = ((2*t**3-3*t*t+1)*AUXILIARY_V
             +(-2*t**3+3*t*t)*data['join_v']+(t**3-t*t)*span*slope)
        # Only original samples may occupy or exceed the retained 8 m cut.
        v = min(v, 8.-1e-8)
        prefix.append(world_coordinates(u0+direction*(departure+t*span), side*v, height))
    revised = prefix+points[data['join_index']:]
    old_length = sum(math.dist(a[:2], b[:2]) for a,b in zip(points,points[1:]))
    new_length = sum(math.dist(a[:2], b[:2]) for a,b in zip(revised,revised[1:]))
    result['mesh_points'] = deepcopy(ramp['points'])
    result['points'] = revised if ramp['direction'] == 'off' else list(reversed(revised))
    result['length_plan_m'] = new_length
    result['flat_start_m'] += new_length-old_length
    result['auxiliary_lane'] = {key:value for key,value in data.items() if key != 'outward'}
    return result


def _polygon(ramp, coordinates, semantic=ASPHALT, height_offset=0.):
    from .ramp_geometry import world_coordinates, _triangulate
    data = profile(ramp)
    vertices = []
    for s,v,*across in coordinates:
        x,y,z = world_coordinates(data['u0']+data['direction']*s,
                                   data['side']*v, data['height']+height_offset)
        vertices.append((x,z,-y,semantic,across[0] if across else .5))
    return _triangulate(vertices,(0.,1.,0.))


def shoulder_footprint(ramp):
    """Return only the old white edge's half-metre top-face footprint."""
    inner, outer = NATIVE_EDGE_ERASE_V
    faces = _polygon(ramp, ((0.,inner),(profile(ramp)['join_s'],inner),
                           (profile(ramp)['join_s'],outer),(0.,outer)))
    return [[(p[0],p[2]) for p in triangle] for triangle in faces]


def native_shoulder_cuts(cell, ramps):
    """Clip repainting to this native source tile; preserve its overhangs."""
    from .ramp_geometry import _clip
    output = []
    for ramp in ramps:
        for footprint in shoulder_footprint(ramp):
            polygon = [(x,0.,z) for x,z in footprint]
            for distance in (lambda p:p[0]-(16.*cell[0]-8.),
                             lambda p:16.*cell[0]+8.-p[0],
                             lambda p:p[2]-(16.*cell[1]-8.),
                             lambda p:16.*cell[1]+8.-p[2]):
                polygon = _clip(polygon,distance)
            if len(polygon) >= 3:
                output.append((ramp['height_m'],ramp['side'],[(p[0],p[2]) for p in polygon]))
    return output


def repaint_native_shoulder(polygon, cuts):
    """Erase old edge paint; preserve surrounding native UVs and original V."""
    from .ramp_geometry import _clip, _normal, _subtract_convex
    if len(polygon)<3 or _normal(polygon[:3])[1] <= 1e-9:
        return [polygon]
    if max(p[1] for p in polygon)-min(p[1] for p in polygon)>1e-6:
        return [polygon]
    pieces = [polygon]
    for height,side,footprint in cuts:
        if abs(polygon[0][1]-height)>1e-6:
            continue
        area = sum(a[0]*b[1]-b[0]*a[1] for a,b in zip(footprint,footprint[1:]+footprint[:1]))
        if abs(area)<1e-10:
            continue
        boundary = footprint if area>0 else list(reversed(footprint))
        revised = []
        for part in pieces:
            inside = part
            for a,b in zip(boundary,boundary[1:]+boundary[:1]):
                length = math.dist(a,b)
                if length<=1e-10:
                    continue
                inside = _clip(inside,lambda p,a=a,b=b,length=length:
                               ((b[0]-a[0])*(p[2]-a[1])-(b[1]-a[1])*(p[0]-a[0]))/length)
            if len(inside)<3:
                revised.append(part)
                continue
            revised.extend(_subtract_convex(part,footprint))
            painted = []
            for p in inside:
                # Adjacent inner asphalt keeps its native longitudinal phase.
                # The outer border is the same grey shoulder tone; no wheel
                # track is stretched across the surrounding auxiliary lane.
                painted.append((*p[:3],NATIVE_EDGE_ASPHALT_U,p[4]))
            revised.append(painted)
        pieces = revised
    return pieces


def _stripe(ramp, a, b, width=.12):
    dx,dy = b[0]-a[0],b[1]-a[1]
    length = math.hypot(dx,dy)
    if length < 1e-8:
        return []
    nx,ny = -dy/length*width/2.,dx/length*width/2.
    return _polygon(ramp, ((a[0]+nx,a[1]+ny,0.),(b[0]+nx,b[1]+ny,0.),
                           (b[0]-nx,b[1]-ny,1.),(a[0]-nx,a[1]-ny,1.)), WHITE, PAINT_HEIGHT)


def surfaces(ramps):
    """Replace shoulder asphalt and paint a dashed separator and compact gore."""
    result = []
    for ramp in ramps:
        data = profile(ramp)
        end, departure, taper = data['join_s'],data['departure_s'],data['taper_m']
        result += _polygon(ramp, ((0.,SEPARATOR_V),(end,SEPARATOR_V),
                                  (end,SHOULDER_OUTER_V),(0.,SHOULDER_OUTER_V)))
        # Leave the actual lane-change crossing clear inside the dashed run.
        for start in range(0,math.ceil(departure),4):
            finish = min(start+2.,departure)
            intervals = [(float(start),finish)]
            low,high = .35*taper,.65*taper
            intervals = [(a,min(b,low)) for a,b in intervals if a < low]+[(max(a,high),b) for a,b in intervals if b > high]
            for a,b in intervals:
                if b-a > .05:
                    result += _stripe(ramp,(a,SEPARATOR_V),(b,SEPARATOR_V))
        # The measured native white edge is |v|=4.5 m. Open that edge
        # smoothly to the auxiliary lane's outer edge, rather than jumping
        # sideways at the external native seam.
        previous = (0.,4.5)
        for index in range(1,int(taper*2)+1):
            s = index/2.
            t = s/taper
            smooth = t*t*t*(10.+t*(-15.+6.*t))
            current = (s,4.5+2.5*smooth)
            result += _stripe(ramp,previous,current,.10)
            previous = current
        result += _stripe(ramp,(taper,7.),(departure,7.),.10)
        base_end = 4.5
        far = max(base_end+.2,data['join_v']-1.5)
        result += _stripe(ramp,(departure,SEPARATOR_V),(end,base_end),.10)
        result += _stripe(ramp,(departure,SEPARATOR_V),(end,far),.10)
        # Keep hatch ends inside the two gore boundaries.
        for offset in (1.5,3.,4.5):
            s = departure+offset
            if s >= end-.25:
                continue
            fraction = (s-departure)/(end-departure)
            low = SEPARATOR_V+(base_end-SEPARATOR_V)*fraction
            high = SEPARATOR_V+(far-SEPARATOR_V)*fraction
            if high-low > .25:
                result += _stripe(ramp,(s-.15,low+.1),(s+.15,high-.1),.10)
    return result
