"""Read saved diagonal transition geometry against independent finite inputs.

The source writer is not imported. Exact native parent faces and the separately
reviewed mathematical surface contract must be present before an actual model
can be accepted. Native/source data do not establish a game observation.
"""
from __future__ import annotations

from collections import defaultdict
from functools import lru_cache
import hashlib
import math
from pathlib import Path
import struct
from types import MappingProxyType

from scp.dbpf import decompress, require
from scp.models import parse_s3d, validate_s3d
from scp.track_paths import PATH, S3D
from scp.verify import parse_paths
from scp import jsonc
from . import diagonal_transition_verify as contract

# Quantization bounds are explicit, and no source-specific shoulder/body
# exemption is inherited from the orthogonal transitions or the Y junction.
POSITION_EPS = 4e-6
UV_EPS = 3e-6
PREFIX = 'SCP diagonal DD transition '
REVIEWED_SURFACES = MappingProxyType({key:MappingProxyType({
    'accepted_encoded_source_snapshot_sha256':'43f0c7a936ad07b227768d21e7f1ceb183f96a728f38a50d0c9fed169cf703a6',
    'accepted_source_physical_report_sha256':'cfdb0b02add5f59c7084e42d895252de26e8da076b1e79bfd94b2c10beb38f27',
    'normal_DAT_five_zooms_preview_and_originals_still_required':True,
    'game_tested':False}) for key in contract.PHASES})
NATIVE_SKIN_SCOPE_REVIEWED = True
COLLAR_INPUTS_FILE = 'diagonal-transition-collar-inputs.jsonc'
COLLAR_INPUTS_SHA256 = '6228bc9b0221cc53a3f03d84755ec02cd09a3b74d7ffa218699223267ddd5d1b'
NATIVE_OBSTACLE_INPUTS_FILE='diagonal-transition-native-obstacle-inputs.jsonc'
NATIVE_OBSTACLE_INPUTS_SHA256='59d58dcced070032c987777b7cea72865a52127ab142286a086faa42a79cb097'
BODY_MATERIAL_SHA256 = 'cf4e393b8ca3a2b3d0edba0f86bb197ddf82b65e85cf73cfa13ebd4d2a8c6f6e'
BARRIER_MATERIAL_SHA256 = 'd81e8d70e3ab9182adb393f2bc6a61608c70f8129cdb06631409a4b19c73e306'
GROUND_MATERIAL_SHA256 = '6222075ddc668c03c58ce8c66cbd82c633bf82d4b9eacb78d5da0a05e7589219'
DATUM = {'upper': .0010004043579101562, 'lower': .0009999275207519531}
TEXTURE = (0x7AB50E44, 0x1ABE787D)
NATIVE_TEXTURE_SHA256 = {
    0x5713000E: '25a91179a26a82ba6307777b1957c5862bee61daf55c7638c4487d64b275c7b8',
    0x5703000E: 'c2b9ac53cc080ca8146f1345e13d43e91c883d9559ec3ec3293e7ff88a259e88',
}
# Filled only by the independently reconstructed pinned source pixels, never
# by trusting the resource writer's generated atlas as its own expectation.
ATLAS_RGBA_SHA256 = MappingProxyType({
    'original': 'bd40fcc4325f385934e71eb1071aa58b6a25b4a6c6591f7009449e52ad6b6621',
    'opposite-side': 'f2dff6aaa6fc99b42b23fc88bfceb2ea0e921ccc028025b04fc30128b3849d81',
    'mirrored': 'c5bf9440efbc0ddbb01ed37282a00f6dd3ca2d13172ed1375474cd879ea099ff',
    'opposite-side-mirrored': '2420f758602112f2d611e1b49b2f3654ed98cd3ac1fb33ae9c35a6795c5f9979',
})


def _sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def collar_source_inputs():
    """Read independent finite original-parent crops, without donor meshes."""
    raw = Path(__file__).with_name(COLLAR_INPUTS_FILE).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == COLLAR_INPUTS_SHA256,
            'Reviewed finite diagonal native crops changed')
    value = jsonc.loads(raw.decode('utf-8'))
    from . import diagonal_transition_native as native
    require(value['stage'] == 'frozen-measured-finite-native-crops'
            and value['alignment'] == 'a' and value['complete_physical_acceptance'] is False
            and value['native_inputs_sha256'] == native.MEASURED_CONTRACT_SHA256,
            'Diagonal source crop scope, alignment, or native resource binding differs')
    require(value['source_resource_sha256'] == {
        '-'.join(f'{part:08x}' for part in key): pin for key,pin in native.RESOURCE_SHA256.items()},
        'Diagonal source crops disagree with original native resource hashes')
    return value


def check_native_obstacle_completeness(resources,piece,donors=None):
    """Bind a complete-original-source clearance proof to exact saved PATHs."""
    from . import diagonal_transition_native as native
    import json
    raw=Path(__file__).with_name(NATIVE_OBSTACLE_INPUTS_FILE).read_bytes()
    require(hashlib.sha256(raw).hexdigest()==NATIVE_OBSTACLE_INPUTS_SHA256,
        'Finite original-native obstacle certificate changed')
    value=jsonc.loads(raw.decode('utf-8'))
    require(value.get('schema_version')==1 and value.get('alignment')=='a'
        and value.get('stage')=='frozen-measured-native-obstacle-completeness',
        'Unreviewed original-native obstacle certificate scope')
    pins={tuple(int(v,16) for v in item['tgi']):item['sha256'] for item in value['native_resource_pins']}
    require(pins==native.RESOURCE_SHA256,'Original-native obstacle source resource pins differ')
    phase=contract.phase_for_piece(piece);row=value['variants'][phase.key]
    by_cell={tuple(cell):contract._number(tile) for cell,tile in zip(piece['cells'],piece['tile_ids'])}
    require(len(row['source05_PATH_sha256_by_local_cell'])==len(by_cell)==24,
        'Native obstacle certificate does not cover every actual saved PATH cell')
    for binding in row['source05_PATH_sha256_by_local_cell']:
        cell=tuple(binding['local_cell'])
        require(cell in by_cell and (*PATH,by_cell[cell]) in resources,
            'Native obstacle certificate PATH cell is missing')
        payload=decompress(resources[*PATH,by_cell[cell]])
        require(len(payload)==binding['bytes'] and hashlib.sha256(payload).hexdigest()==binding['sha256'],
            'Saved PATH changed its certified original-native obstacle window')
    routes,_cells=contract.native_vehicle_routes(donors,variant=phase.key)
    measured={r['id']:r for r in row['helper_vehicle_routes']}
    require(len(routes)==len(measured)==8,'Native obstacle window changes the eight helper lanes')
    for route in routes:
        source=measured.get(route['id'],{})
        require(source.get('component')==route['component'] and source.get('arm')==route['arm']
            and source.get('native_tile_id')==f'{route["native_tile_id"]:08x}'
            and source.get('pose_clockwise_quarter_turns')==route['native_pose_clockwise']
            and tuple(source.get('source_world_cell',()))==tuple(route['native_world_cell'])
            and source.get('points_ENH_m')==[list(p) for p in route['points']],
            'Native obstacle certificate changes an original finite helper route')
    parents=row['original_non_pavement_parents']
    require(len(parents)==row['original_non_pavement_parent_count']==48
        and row['conservative_plan_distance_lower_bound_m']==3.65
        and all(parent['conservative_plan_distance_lower_bound_m']>=3.65 for parent in parents),
        'Original native body/barrier obstacle clearance lacks its full finite inventory')
    if donors is not None:
        expected={(p['native_tile_id'],p['pose_clockwise_quarter_turns'],tuple(p['source_world_cell']),
            p['source_mesh_index'],p['source_face_index'],p['source_parent_ENHUV_sha256']) for p in parents}
        actual=set()
        for placement in row['native_source_model_placements']:
            tile=contract._number(placement['native_tile_id'])
            for group in native.source_faces(donors,tile,placement['pose_clockwise_quarter_turns'],placement['source_world_cell']):
                if group['role']=='pavement':
                    continue
                for index,parent in enumerate(group['triangles']):
                    digest=hashlib.sha256(json.dumps(parent,separators=(',',':')).encode()).hexdigest()
                    actual.add((group['native_tile_id'],group['pose'],tuple(group['world_cell']),group['mesh_index'],index,digest))
        require(actual==expected,'Actual indexed original native obstacle parents differ from their finite clearance proof')
    return {'passed':True,'exact_saved_PATH_bindings_checked':24,'actual_helper_vehicle_rows_checked':8,
        'all_original_non_pavement_parent_identities_checked':48,
        'conservative_finite_plan_clearance_m':3.65,'fresh_original_parent_check_performed':donors is not None,
        'opposing_original_pavement_clearance':row['opposing_native_pavement_clearance'],
        'peer_routes_recursively_claimed':False,'omitted_original_obstacles_inferred_from_roof_crops':False}


def _source_attributes(record, point):
    return tuple(_dot(record['source_affine_UV_ENH'][name]['gradient_ENH'],point)
        +record['source_affine_UV_ENH'][name]['offset'] for name in ('U','V'))


def _source_height(record, east, north):
    plane = record['source_surface_plane_ENH']
    n = plane['normal']
    require(n[2] != 0., 'Finite pavement field must have a nonvertical source plane')
    return (plane['constant']-n[0]*east-n[1]*north)/n[2]


@lru_cache(maxsize=4)
def native_collar_regions(variant='original'):
    """Reconstruct DD ownership and intrinsic top partition from source facts.

    No runtime collar groups or writer booleans are used. Every raw forward
    panel is clipped to the independently declared city ownership; original
    rendered pavement has priority, followed by helper, and then peer. Native
    rail footprints form the integral raised part of the same exterior roof.
    """
    from shapely.geometry import Polygon,box
    from shapely.ops import unary_union
    contract.phase_for_options(variant)
    data = collar_source_inputs()['variants'][variant]
    owned = unary_union([box(16*c-8,-16*r-8,16*c+8,-16*r+8) for c,r in data['world_cells']])
    raw = []
    for index,record in enumerate(data['DD_profiles']):
        a,b = record['source_edge_ENHUV']
        x,y = record['inner_edge_ENH']
        polygon = Polygon([a[:2],b[:2],y[:2],x[:2]])
        raw.append({'index':index,'source':record,'geometry':polygon.intersection(owned)})
    result = {}
    for deck in ('upper','lower'):
        references = []
        for record in data['DD_references']:
            if record['deck']==deck and record['role']=='pavement':
                references.extend(Polygon([p[:2] for p in crop['polygon_ENH']])
                    for crop in record['finite_city_crops'])
        original = unary_union(references)
        rail = unary_union([row['geometry'] for row in raw
            if row['source']['deck']==deck and row['source']['role']=='barrier'])
        taken = original
        floors,visible = [],[]
        for row in sorted((r for r in raw if r['source']['deck']==deck
                and r['source']['role']=='pavement'),
                key=lambda r:r['source']['native_owner_kind']!='helper'):
            region = row['geometry'].difference(taken)
            floors.append({**row,'geometry':region})
            visible.append({**row,'geometry':region.difference(rail)})
            taken = unary_union([taken,region])
        result[deck] = {'phase_roofs':floors,'visible_pavement':visible,
            'original_pavement':original,'base_geometry':taken,'raw_profile_panels':[
                row for row in raw if row['source']['deck']==deck], 'owned_geometry':owned}
    return result


def _inner_boundary_intervals(shape,centre,normal):
    """Measure actual finite polygon edges on C without a rebuilt GEOS line."""
    rows=[]
    for polygon in _positive_polygons(shape):
        for ring in (polygon.exterior,*polygon.interiors):
            points=list(ring.coords)[:-1]
            for a,b in zip(points,(*points[1:],points[0])):
                if max(abs(_dot(_sub(p[:2],centre),contract.LONGITUDINAL)) for p in (a,b))<=1e-11:
                    low,high=sorted(_dot(_sub(p[:2],centre),normal) for p in (a,b))
                    if high>low:
                        rows.append((low,high))
    return rows


def dd_inner_profiles(*,variant='original'):
    """Independent complete finite pavement/rail sections at the native C ring."""
    raw=[]
    for deck,regions in native_collar_regions(variant).items():
        centre,normal=contract.frame(deck,contract.FLAT_ENVELOPE,variant=variant)
        rows=[*regions['visible_pavement'],*(row for row in regions['raw_profile_panels']
            if row['source']['role']=='barrier')]
        for row in rows:
            source=row['source']
            for low,high in _inner_boundary_intervals(row['geometry'],centre,normal):
                points=[]
                for u in (low,high):
                    x,y=(centre[i]+u*normal[i] for i in range(2))
                    height=_source_height(source,x,y)
                    p=x,y,height
                    points.append((*p,*_source_attributes(source,p)))
                raw.append({'deck':deck,'kind':source['role'],'source':source,'points':points,
                    'lateral_interval_m':(low,high)})
    # The integral exterior is the upper envelope. A nominal asphalt line
    # below its own raised rail is an internal native surface, including at
    # the common C cut, and cannot become a second exterior profile merely
    # because two arithmetic cut coordinates differ by a few picometres.
    result=[]
    for deck in ('upper','lower'):
        rows=[row for row in raw if row['deck']==deck]
        cuts=sorted({u for row in rows for u in row['lateral_interval_m']})
        for low,high in zip(cuts,cuts[1:]):
            if high-low<=1e-12:
                continue
            mid=(low+high)/2.
            def at(row,u):
                a,b=row['lateral_interval_m'];t=(u-a)/(b-a)
                return tuple(row['points'][0][i]+t*(row['points'][1][i]-row['points'][0][i]) for i in range(5))
            candidates=[row for row in rows if row['lateral_interval_m'][0]<=mid<=row['lateral_interval_m'][1]]
            if not candidates:
                continue
            source=max(candidates,key=lambda row:at(row,mid)[2])
            result.append({**source,'lateral_interval_m':(low,high),'points':(at(source,low),at(source,high))})
    return result


def _quadratic_interval(vector,slope,radius,low,high):
    """Intersect a finite parameter interval with ||vector+t*slope||<=r."""
    aa=_dot(slope,slope);bb=2.*_dot(vector,slope);cc=_dot(vector,vector)-radius*radius
    if aa==0.:
        if bb==0.:
            return (low,high) if cc<=0. else None
        root=-cc/bb
        low,high=(low,min(high,root)) if bb>0. else (max(low,root),high)
    else:
        closest=-bb/(2.*aa)
        residual=tuple(a+closest*b for a,b in zip(vector,slope))
        remaining=radius*radius-_dot(residual,residual)
        if remaining<0.:
            return None
        half=math.sqrt(remaining/aa)
        low,high=max(low,closest-half),min(high,closest+half)
    return (low,high) if high>=low else None


def _segment_capsule_intervals(target,actual):
    """Exact finite3D-segment capsules, intersected with their affine UV bound."""
    a,b=target;p,q=actual
    d=_sub(b[:3],a[:3]);v=_sub(q[:3],p[:3]);vv=_dot(v,v)
    if vv==0.:
        return []
    offset=_sub(a[:3],p[:3]);alpha,beta=_dot(offset,v)/vv,_dot(d,v)/vv
    cuts=sorted({0.,1.,*((bound-alpha)/beta for bound in (0.,1.)
        if beta and 0.<(bound-alpha)/beta<1.)})
    result=[]
    for low,high in zip(cuts,cuts[1:]):
        sample=alpha+beta*(low+high)/2.
        ua,ub=(0.,0.) if sample<0. else (1.,0.) if sample>1. else (alpha,beta)
        delta=tuple(offset[i]-ua*v[i] for i in range(3))
        slope=tuple(d[i]-ub*v[i] for i in range(3))
        region=_quadratic_interval(delta,slope,POSITION_EPS,low,high)
        if region is None:
            continue
        uv_offset=tuple(a[i]-p[i]-ua*(q[i]-p[i]) for i in (3,4))
        uv_slope=tuple(b[i]-a[i]-ub*(q[i]-p[i]) for i in (3,4))
        region=_quadratic_interval(uv_offset,uv_slope,UV_EPS,*region)
        if region is not None:
            result.append(region)
    return result


def check_dd_inner_profiles(faces,*,variant='original'):
    """Prove complete native-derived width, XYZ, material, UV, and winding at C."""
    actual=[]
    for face in faces:
        if not face['role'].startswith('dd-') or face.get('kind') not in ('pavement','barrier'):
            continue
        values=[_dot(_sub(p[:2],contract.J),contract.LONGITUDINAL)-contract.FLAT_ENVELOPE
            for p in face['points']]
        if min(values)>POSITION_EPS or max(values)<-POSITION_EPS:
            continue
        vertices=[(*p,*uv) for p,uv in zip(face['points'],face['uv'])]
        for a,b,x,y in zip(vertices,(*vertices[1:],vertices[0]),values,(*values[1:],values[0])):
            if max(abs(x),abs(y))<=POSITION_EPS and math.dist(a[:3],b[:3])>0.:
                actual.append((face,(a,b)))
        points=[]
        for a,b,x,y in zip(vertices,(*vertices[1:],vertices[0]),values,(*values[1:],values[0])):
            if x==0.:
                points.append(a)
            if x*y<0.:
                t=x/(x-y);points.append(tuple(u+t*(v-u) for u,v in zip(a,b)))
        if len(points)>=2:
            first,last=max(((a,b) for i,a in enumerate(points) for b in points[i+1:]),
                key=lambda pair:math.dist(pair[0][:3],pair[1][:3]))
            if math.dist(first[:3],last[:3])>0.:
                actual.append((face,(first,last)))
    checked=0
    for profile in dd_inner_profiles(variant=variant):
        source=profile['source'];segments=[]
        for face,segment in actual:
            if face['deck']!=profile['deck'] or face['kind']!=profile['kind']:
                continue
            if _material_fingerprint(face,source)!=source['source_material_sha256']:
                continue
            if _dot(_normal(face['points']),source['source_surface_plane_ENH']['normal'])<=0.:
                continue
            segments.extend(_segment_capsule_intervals(profile['points'],segment))
        end=0.
        for a,b in sorted(segments):
            if a>end+1e-12:
                break
            end=max(end,b)
        require(end>=1.-1e-12,
            'Saved DD inner ring omits a finite original profile interval; '
            f'deck={profile["deck"]}, kind={profile["kind"]}, '
            f'lateral_interval_m={profile["lateral_interval_m"]}, covered_parameter={end}')
        checked+=1
    return {'passed':True,'complete_finite_source_inner_sections_checked':checked,
        'position_euclidean_bound_m':POSITION_EPS,'UV_euclidean_bound':UV_EPS,
        'full_native_shoulder_width_retained':True,'rebuilt_infinite_section_line':False}


def native_atlas_fields(variant='original'):
    """Derive finite UV owners at each native-to-owned-asphalt interface."""
    data = collar_source_inputs()['variants'][variant]
    regions = native_collar_regions(variant)
    result = {}
    for deck in ('upper','lower'):
        centre,normal = contract.frame(deck,contract.FLAT_ENVELOPE,variant=variant)
        def lateral(point):
            return _dot(_sub(point[:2],centre),normal)
        def intervals(shape):
            # These are original finite polygons whose inner boundary was
            # explicitly constructed at C. A separately constructed GEOS
            # line can lie one arithmetic ULP outside that boundary. Classify
            # the actual polygon vertices in the measured section plane;
            # this 10-picometre arithmetic zero does not extend a source ROI.
            result=[]
            for polygon in _positive_polygons(shape):
                for ring in (polygon.exterior,*polygon.interiors):
                    points=list(ring.coords)[:-1]
                    for a,b in zip(points,(*points[1:],points[0])):
                        phase=[_dot(_sub(p[:2],centre),contract.LONGITUDINAL) for p in (a,b)]
                        if max(map(abs,phase))<=1e-11 and math.dist(a,b)>0.:
                            result.append(tuple(sorted((lateral(a),lateral(b)))))
            return result
        bounds = intervals(regions[deck]['base_geometry'])
        require(bounds, 'Finite native DD field has no complete inner cross-section')
        low,high = min(a for a,b in bounds),max(b for a,b in bounds)
        anchors = ((low,-8.),(-contract.LANE_OFFSET,-contract.LANE_OFFSET),(0.,0.),
            (contract.LANE_OFFSET,contract.LANE_OFFSET),(high,8.))
        def mapped(value):
            for (a,x),(b,y) in zip(anchors,anchors[1:]):
                if a-1e-10<=value<=b+1e-10:
                    return x+(value-a)*(y-x)/(b-a)
            raise ValueError('Finite native DD UV interval escapes the measured inner roof')
        rows = []
        reference = contract.FLAT_ENVELOPE+1.
        refcentre,refnormal = contract.frame(deck,reference,variant=variant)
        for region in regions[deck]['visible_pavement']:
            source = region['source']
            for a,b in intervals(region['geometry']):
                a,b=max(low,a),min(high,b)
                cuts=sorted({a,b,*(u for u,v in anchors if a<u<b)})
                for first,last in zip(cuts,cuts[1:]):
                    if last-first<=1e-10:
                        continue
                    x,y=mapped(first),mapped(last)
                    point=(*tuple(refcentre[i]+x*refnormal[i] for i in range(2)),
                        source['source_edge_ENHUV'][0][2])
                    rows.append({'lateral_interval_m':(x,y),'reference_station_m':reference,
                        'UV_at_first_lateral':_source_attributes(source,point),
                        'dUV_d_lateral_m':tuple(_dot(source['source_affine_UV_ENH'][name]['gradient_ENH'],
                            (*refnormal,0.)) for name in ('U','V')),
                        'dUV_d_station_m':tuple(_dot(source['source_affine_UV_ENH'][name]['gradient_ENH'],
                            (*contract.LONGITUDINAL,0.)) for name in ('U','V')),
                        'source_parent_ENHUV_sha256':source['source_parent_ENHUV_sha256']})
        require(rows,'Finite native DD UV field omits every visible source owner')
        ground=data['ground'][deck]
        gcentre,gnormal=contract.frame(deck,contract.LENGTH-contract.FLAT_ENVELOPE,variant=variant)
        local=lambda p:_dot(_sub(p[:2],gcentre),gnormal)
        profiles=[(record,segment) for record in ground['literal_source_fragments']
            for segment in record['inner_profile_ENHUV']]
        require(profiles,'Finite ground UV fields have no independently measured inner profile')
        low=min(local(p) for record,segment in profiles for p in segment)
        high=max(local(p) for record,segment in profiles for p in segment)
        grows=[]
        for source,segment in profiles:
            a,b=sorted(segment,key=local)
            x,y=(-8.+16.*(local(p)-low)/(high-low) for p in (a,b))
            if y-x<=1e-10:
                continue
            grows.append({'lateral_interval_m':(x,y),'reference_station_m':contract.LENGTH-contract.FLAT_ENVELOPE,
                'UV_at_first_lateral':a[3:],
                'dUV_d_lateral_m':tuple((b[i]-a[i])/(y-x) for i in (3,4)),
                'dUV_d_station_m':tuple(_dot(source['source_affine_UV_ENH'][name]['gradient_ENH'],
                    (*contract.LONGITUDINAL,0.)) for name in ('U','V')),
                'source_parent_ENHUV_sha256':source['source_parent_ENHUV_sha256']})
        result[deck]={'dd':sorted(rows,key=lambda r:r['lateral_interval_m']),
            'ground':sorted(grows,key=lambda r:r['lateral_interval_m'])}
    return result


def _dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def _cross(a, b):
    return a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]


def _normal(points):
    return _cross(_sub(points[1], points[0]), _sub(points[2], points[0]))


def _area(points):
    return sum(math.sqrt(_dot(n,n))/2. for i in range(1,len(points)-1)
        for n in [_cross(_sub(points[i],points[0]),_sub(points[i+1],points[0]))])


def _positive_polygons(geometry):
    """Keep every actual positive polygon, excluding only lower dimensions."""
    if geometry.geom_type == 'Polygon':
        return [geometry] if geometry.area > 0. else []
    return [part for member in getattr(geometry, 'geoms', ()) for part in _positive_polygons(member)]


def _point_triangle_distance(point, triangle):
    """True three-dimensional distance to a finite triangle, not its plane."""
    a, b, c = triangle
    u, v, w = _sub(b, a), _sub(c, a), _sub(point, a)
    normal = _cross(u, v)
    norm2 = _dot(normal, normal)
    if norm2 > 0.:
        phase = _dot(w, normal)/norm2
        projected = tuple(point[i]-phase*normal[i] for i in range(3))
        q = _sub(projected, a)
        uu, uv, vv = _dot(u, u), _dot(u, v), _dot(v, v)
        denominator = uu*vv-uv*uv
        if denominator > 0.:
            second = (vv*_dot(q, u)-uv*_dot(q, v))/denominator
            third = (uu*_dot(q, v)-uv*_dot(q, u))/denominator
            if second >= 0. and third >= 0. and second+third <= 1.:
                return math.dist(point, projected)
    best = math.inf
    for first, last in ((a, b), (b, c), (c, a)):
        edge = _sub(last, first)
        length2 = _dot(edge, edge)
        t = min(1., max(0., _dot(_sub(point, first), edge)/length2)) if length2 else 0.
        best = min(best, math.dist(point, tuple(first[i]+t*edge[i] for i in range(3))))
    return best


def _point_segment_distance(point, first, last):
    edge=_sub(last,first)
    length2=_dot(edge,edge)
    t=min(1.,max(0.,_dot(_sub(point,first),edge)/length2)) if length2 else 0.
    return math.dist(point,tuple(first[i]+t*edge[i] for i in range(3)))


def finite_edge_contact(region,first,second):
    """Bound a whole convex contact by ONE finite edge per actual triangle.

    A three-dimensional capsule around a finite segment is convex. If every
    convex-region vertex is in that SAME capsule, its entire interior is too.
    Endpoint caps remain valid even when the edge's far end leaves the first
    surface plane. No infinite line, per-corner edge switching, or area limit
    is used, and the radius is the unchanged4µm Euclidean bound.
    """
    for triangle in (first,second):
        if not any(all(_point_segment_distance(p,a,b)<=POSITION_EPS for p in region)
                for a,b in zip(triangle,(*triangle[1:],triangle[0]))):
            return False
    return True


def check_surface_contacts(faces,*,underside=False,variant=None):
    """Reject finite duplicate/crossing roofs or floors, including tiny areas."""
    from shapely.geometry import Polygon
    from shapely.strtree import STRtree
    selected=[f for f in faces if (f.get('kind')=='body' and _normal(f['points'])[2]<0.
        if underside else f.get('kind')=='pavement' and _normal(f['points'])[2]>0.)]
    polygons=[Polygon([p[:2] for p in f['points']]) for f in selected]
    tree=STRtree(polygons)
    def height(point,triangle):
        a,b,c=triangle
        determinant=(b[1]-c[1])*(a[0]-c[0])+(c[0]-b[0])*(a[1]-c[1])
        u=((b[1]-c[1])*(point[0]-c[0])+(c[0]-b[0])*(point[1]-c[1]))/determinant
        v=((c[1]-a[1])*(point[0]-c[0])+(a[0]-c[0])*(point[1]-c[1]))/determinant
        return u*a[2]+v*b[2]+(1.-u-v)*c[2]
    tested=0;phase_contacts=0
    maximum=0.
    for i,polygon in enumerate(polygons):
        for j in tree.query(polygon,predicate='intersects'):
            j=int(j)
            if j<=i:
                continue
            if selected[i].get('native_reference') and selected[j].get('native_reference'):
                continue
            overlap=polygon.intersection(polygons[j])
            if overlap.area==0.:
                continue
            for region in _positive_polygons(overlap):
                vertices=list(region.convex_hull.exterior.coords)[:-1]
                first=[(*p,height(p,selected[i]['points'])) for p in vertices]
                second=[(*p,height(p,selected[j]['points'])) for p in vertices]
                differences=[a[2]-b[2] for a,b in zip(first,second)]
                if min(differences)>=1.-POSITION_EPS or max(differences)<=-1.+POSITION_EPS:
                    continue
                if (not underside and variant is not None
                        and _incident_native_phase_cap(first,second,selected[i],selected[j],faces,variant)):
                    phase_contacts+=1
                    continue
                require(max(map(abs,differences))<=POSITION_EPS
                        and finite_edge_contact(first,selected[i]['points'],selected[j]['points']),
                    'Diagonal saved road surfaces duplicate or cross beyond finite edge contact; '
                    f'roles={selected[i]["role"]}/{selected[j]["role"]}, '
                    f'area_m2={region.area}, bounds_EN={region.bounds}')
                maximum=max(maximum,*(min(max(_point_segment_distance(p,a,b) for p in first)
                    for a,b in zip(triangle,(*triangle[1:],triangle[0])))
                    for triangle in (selected[i]['points'],selected[j]['points'])))
                tested+=1
    return {'passed':True,'actual_triangles_checked':len(selected),'finite_edge_contacts_checked':tested,
        'source_paired_finite_phase_cap_contacts':phase_contacts,
        'maximum_finite_edge_distance_m':maximum,'combined_euclidean_bound_m':POSITION_EPS,
        'positive_area_exemption':False,'infinite_edge_extension':False}


def _incident_native_phase_cap(first_points,second_points,first,second,faces,variant):
    """One actual finite source-paired1mm cap joins two native roof phases.

    This changes no face and accepts no XY-only fringe. Every overlap point
    stays within4µm of its OWN finite roof edge and the SAME finite cap
    triangle. The complete cap is bound to those same two original source
    boundary edges at their actual respective heights, shader, and UV field.
    """
    if first.get('deck')!=second.get('deck') or first.get('deck') not in ('upper','lower'):
        return False
    deck=first['deck'];nominal=15. if deck=='upper' else 7.5;upper=nominal+DATUM[deck]
    if max(p[2] for p in first_points)<min(p[2] for p in second_points):
        low,high=first,second;low_points,high_points=first_points,second_points
    else:
        low,high=second,first;low_points,high_points=second_points,first_points
    source=high.get('source',{})
    if (low.get('native_reference') or not high.get('native_reference')
            or source.get('native_tile_id')!='57530900'
            or '-pavement-native-profile-loft-' not in low['role']
            or max(abs(p[2]-nominal) for p in low['points'])>POSITION_EPS
            or max(abs(p[2]-upper) for p in high['points'])>POSITION_EPS):
        return False
    # The actual lower face must itself belong to a pinned finite302
    # continuation. A role string or the nominal height alone is not proof.
    native302=[parent for parent in native_dd_profile_surfaces(variant=variant,visible=False)
        if parent['source_record']['native_tile_id']=='57530200'
        and parent['source_record']['deck']==deck and parent['source_record']['role']=='pavement'
        and _material_fingerprint(low,parent)==parent['material_sha256']]
    if not any(all(_field_weights(p,uv,parent) is not None for p,uv in zip(low['points'],low['uv']))
            for parent in native302):
        return False
    low_edges=[(a,b) for a,b in zip(low['points'],(*low['points'][1:],low['points'][0]))
        if all(_point_segment_distance(p,a,b)<=POSITION_EPS for p in low_points)]
    high_edges=[(a,b) for a,b in zip(high['points'],(*high['points'][1:],high['points'][0]))
        if all(_point_segment_distance(p,a,b)<=POSITION_EPS for p in high_points)]
    if not low_edges or not high_edges:
        return False
    prefix=f'dd-{deck}-body-authored-DD-roof-phase-step-'
    for cap in faces:
        if not cap['role'].startswith(prefix) or cap.get('native_reference'):
            continue
        if (cap.get('kind')!='body' or cap.get('deck')!=deck or cap['texture']!=0x5EB4BEEE
                or _material_fingerprint(cap,{})!=BODY_MATERIAL_SHA256
                or any(p[2]<nominal-POSITION_EPS or p[2]>upper+POSITION_EPS for p in cap['points'])
                or any(math.dist(uv,(p[0]/8.,p[1]/8.))>UV_EPS for p,uv in zip(cap['points'],cap['uv']))):
            continue
        if not any(all(_point_segment_distance((p[0],p[1],nominal),a,b)<=POSITION_EPS
                for p in cap['points']) for a,b in low_edges):
            continue
        if not any(all(_point_segment_distance((p[0],p[1],upper),a,b)<=POSITION_EPS
                for p in cap['points']) for a,b in high_edges):
            continue
        # A roof-phase step closes the lower roof with the opposite directed
        # lower boundary incidence. Choose the geometrically incident edge,
        # rather than a different tiny corner edge merely within4µm.
        incident=min(low_edges,key=lambda edge:max(_point_segment_distance((p[0],p[1],nominal),*edge)
            for p in cap['points']))
        outward=_cross(_sub(incident[1],incident[0]),_normal(low['points']))
        if _dot(_normal(cap['points']),outward)>=0.:
            continue
        if all(_point_triangle_distance(p,cap['points'])<=POSITION_EPS for p in (*low_points,*high_points)):
            return True
    return False


def decode_faces(raw, cell=(0, 0)):
    """Decode actual referenced finite triangles in east/north/height metres."""
    model = parse_s3d(decompress(raw))
    validate_s3d(model)
    require(struct.unpack_from('<H', model['anim_header'])[0] == 1,
            'Diagonal transition models must be static')
    require(all(len(chunk) == 12 and chunk[8:] == b'\0'*4 for _name, chunk in model['trailing']),
            'Diagonal transition contains an unreviewed model transform')
    result = []
    for mesh in model['meshes']:
        require(len(mesh['frames']) == 1, 'Diagonal transition mesh has multiple frames')
        vi, ii, pi, mi = mesh['frames'][0]
        block = model['vertices'][vi]
        require(block['stride'] >= 20 and len(block['data'])//block['stride'] <= 512,
                'Diagonal transition render group exceeds its vertex budget')
        vertices = [struct.unpack_from('<5f', block['data'], at)
                    for at in range(0, len(block['data']), block['stride'])]
        require(all(all(math.isfinite(v) for v in p) for p in vertices),
                'Diagonal transition contains nonfinite XYZ/UV')
        material = model['materials'][mi]
        require(len(material['textures']) == 1, 'Diagonal material must have one texture')
        indices = model['indices'][ii]['values']
        require(len(indices) <= 1536, 'Diagonal transition render group exceeds its index budget')
        name = mesh['name'].rstrip(b'\0').decode('ascii')
        require(name.startswith(PREFIX), 'Diagonal model contains an unreviewed mesh namespace')
        role = name[len(PREFIX):]
        for kind, start, count in model['primitives'][pi]:
            require(kind == 0 and count % 3 == 0, 'Diagonal model primitive is not a finite triangle list')
            for at in range(start, start+count, 3):
                selected = [vertices[indices[at+i]] for i in range(3)]
                points = tuple((p[0]+16.*cell[0], -p[2]-16.*cell[1], p[1]) for p in selected)
                uv = tuple((p[3], p[4]) for p in selected)
                result.append({'role': role, 'points': points, 'uv': uv,
                    'texture': material['textures'][0], 'material': material,
                    'area': _area(points), 'cell': tuple(cell), 'upward': _normal(points)[2] > 0.})
    return result


def _field_weights(point, uv, parent):
    """Find one finite parent witness for all three XYZ and both UV fields."""
    scales = (POSITION_EPS,)*3+(UV_EPS,)*2
    rows = [tuple(v/s for v, s in zip((*p, *t), scales))
            for p, t in zip(parent['points'], parent['uv'])]
    target = tuple(v/s for v, s in zip((*point, *uv), scales))
    a, b, c = rows
    u, v, w = _sub(b, a), _sub(c, a), _sub(target, a)
    determinant, first, second = max((abs(u[i]*v[j]-u[j]*v[i]), i, j)
        for i in range(5) for j in range(i+1, 5))
    if determinant <= 1e-20:
        return None
    denominator = u[first]*v[second]-u[second]*v[first]
    q = (w[first]*v[second]-w[second]*v[first])/denominator
    r = (u[first]*w[second]-u[second]*w[first])/denominator
    weights = (1.-q-r, q, r)
    reconstructed_xyz = tuple(sum(weights[k]*parent['points'][k][i] for k in range(3)) for i in range(3))
    reconstructed_uv = tuple(sum(weights[k]*parent['uv'][k][i] for k in range(3)) for i in range(2))
    if math.dist(point, reconstructed_xyz) > POSITION_EPS or math.dist(uv, reconstructed_uv) > UV_EPS:
        return None
    # This is a finite witness, rather than permission to extend a parent
    # plane. Parent-domain excursions are tested in physical XYZ below.
    if min(weights) < 0.:
        if _point_triangle_distance(point, parent['points']) > POSITION_EPS:
            return None
    return weights


def _material_fingerprint(actual, parent):
    raw = actual.get('material', {}).get('raw')
    if not isinstance(raw, bytes):
        return None
    if 'source_material_texture' in parent:
        word = struct.pack('<I', actual['texture'])
        if raw.count(word) != 1:
            return None
        raw = raw.replace(word, struct.pack('<I', parent['source_material_texture']), 1)
    return hashlib.sha256(raw).hexdigest()


def _finite_triangle_union_covers(region, parent, actual_triangles):
    """Cover a finite parent-plane region by finite 3D triangle capsules.

    A city boundary can divide a long thin encoding remainder among several
    actual triangles. Requiring one child to cover that entire remainder is
    too strong. Each projected capsule reserves its actual maximum normal
    displacement from the SAME four-micrometre Euclidean budget. Inscribed
    GEOS circles make this a conservative finite cover, not a plane extension.
    """
    from shapely.geometry import Polygon
    from shapely.ops import unary_union
    a = parent[0]
    normal = _normal(parent)
    length = math.sqrt(_dot(normal, normal))
    normal = tuple(v/length for v in normal)
    first = _sub(parent[1], a)
    length = math.sqrt(_dot(first, first))
    first = tuple(v/length for v in first)
    second = _cross(normal, first)
    def project(point):
        delta = _sub(point, a)
        return _dot(delta, first), _dot(delta, second)
    target = Polygon([project(p) for p in region])
    masks = []
    for points in actual_triangles:
        phase = max(abs(_dot(_sub(p,a),normal)) for p in points)
        if phase > POSITION_EPS:
            continue
        radius = math.sqrt(max(0.,POSITION_EPS**2-phase**2))
        mask = Polygon([project(p) for p in points])
        if radius:
            mask = mask.buffer(radius,quad_segs=32)
        masks.append(mask)
    return target.difference(unary_union(masks)).area == 0.


def _piecewise_source_faces(actual,parents,*,material_checked=False):
    """Certify an actual triangle split across several finite reviewed parents.

    City clipping and harmless transverse subdivisions need not keep the
    same triangulation on a planar surface. Every analysis patch retains one
    actual affine XYZUV field and one finite reviewed parent witness at all
    corners. Convexity then proves both distance bounds across that patch.
    """
    from shapely.geometry import Polygon
    from shapely.ops import unary_union
    from shapely import constrained_delaunay_triangles
    origin=actual['points'][0]
    normal=_normal(actual['points']);length=math.sqrt(_dot(normal,normal))
    if not length:
        return None
    normal=tuple(v/length for v in normal)
    edge=_sub(actual['points'][1],origin);length=math.sqrt(_dot(edge,edge))
    u=tuple(v/length for v in edge);v=_cross(normal,u)
    project=lambda p:(_dot(_sub(p,origin),u),_dot(_sub(p,origin),v))
    actual_xy=[project(p) for p in actual['points']]
    target=Polygon(actual_xy)
    a,b,c=actual_xy
    determinant=(b[1]-c[1])*(a[0]-c[0])+(c[0]-b[0])*(a[1]-c[1])
    def actual_at(point):
        first=((b[1]-c[1])*(point[0]-c[0])+(c[0]-b[0])*(point[1]-c[1]))/determinant
        second=((c[1]-a[1])*(point[0]-c[0])+(a[0]-c[0])*(point[1]-c[1]))/determinant
        weights=first,second,1.-first-second
        xyz=tuple(sum(w*p[i] for w,p in zip(weights,actual['points'])) for i in range(3))
        uv=tuple(sum(w*t[i] for w,t in zip(weights,actual['uv'])) for i in range(2))
        return xyz,uv
    usable=[]
    for index,parent in parents:
        if ((material_checked or _material_fingerprint(actual,parent)==parent['material_sha256'])
                and _dot(_normal(actual['points']),_normal(parent['points']))>0.):
            polygon=Polygon([project(p) for p in parent['points']])
            if polygon.area>0.:
                usable.append((index,parent,polygon))
    covered=[];pieces=[]
    def keep(region,index,parent):
        vertices=list(region.exterior.coords)[:-1]
        fields=[actual_at(p) for p in vertices]
        weights=[_field_weights(xyz,uv,parent) for xyz,uv in fields]
        if any(w is None for w in weights):
            return False
        # Each convex patch is certified against one finite5D affine parent.
        # Store true subtriangles of the actual saved face for the reverse
        # coverage and duplicate checks; the DAT itself is never modified.
        for at in range(1,len(vertices)-1):
            ids=(0,at,at+1)
            child={**actual,'points':tuple(fields[i][0] for i in ids),
                'uv':tuple(fields[i][1] for i in ids)}
            polygon=Polygon([(weights[i][1],weights[i][2]) for i in ids])
            if polygon.area>0.:
                pieces.append((index,polygon,child))
        covered.append(region)
        return True
    for index,parent,polygon in usable:
        for region in _positive_polygons(target.intersection(polygon)):
            keep(region,index,parent)
    missing=target.difference(unary_union(covered))
    if missing.area>0.:
        for index,parent,polygon in usable:
            for region in _positive_polygons(missing.intersection(polygon.buffer(POSITION_EPS,quad_segs=32))):
                if keep(region,index,parent):
                    continue
                for triangle in constrained_delaunay_triangles(region).geoms:
                    if triangle.area>0.:
                        keep(triangle,index,parent)
            missing=target.difference(unary_union(covered))
            if missing.area==0.:
                break
    if missing.area>0.:
        # Polygon overlay can leave a positive but arbitrarily thin residue
        # along an already proved finite boundary. Prove every such region
        # independently; never use its area as an admission threshold.
        def subdivided_proof(triangle,depth=0):
            vertices=list(triangle.exterior.coords)[:3]
            west,south,east,north=triangle.bounds
            nearby=[(index,parent,polygon) for index,parent,polygon in usable
                if polygon.bounds[2]>=west-POSITION_EPS and polygon.bounds[0]<=east+POSITION_EPS
                and polygon.bounds[3]>=south-POSITION_EPS and polygon.bounds[1]<=north+POSITION_EPS]
            if any(keep(triangle,index,parent) for index,parent,polygon in nearby):
                return True
            # Every recursive corner still needs a finite5D source witness.
            # This rejects a real hole or a wrong attribute before further
            # subdivision, regardless of the patch's area.
            if any(not any(_field_weights(*actual_at(p),parent) is not None
                    for index,parent,polygon in nearby) for p in vertices):
                return False
            if depth>=64:
                return False
            i,j=max(((0,1),(1,2),(2,0)),key=lambda pair:math.dist(vertices[pair[0]],vertices[pair[1]]))
            k=3-i-j;a,b,c=vertices[i],vertices[j],vertices[k]
            middle=tuple((x+y)/2. for x,y in zip(a,b))
            if middle==a or middle==b:
                return False
            first,second=Polygon((a,middle,c)),Polygon((middle,b,c))
            # A residual thinner than one arithmetic ULP can yield a
            # collinear ANALYSIS child when bisected. Its finite corners
            # still need the same source witness; no saved zero-area face is
            # admitted, and no area-based admission is used.
            return subdivided_proof(first,depth+1) and subdivided_proof(second,depth+1)
        for region in _positive_polygons(missing):
            if any(keep(region,index,parent) for index,parent,_polygon in usable):
                continue
            for triangle in constrained_delaunay_triangles(region).geoms:
                if triangle.area>0. and not subdivided_proof(triangle):
                    return None
    return pieces


def check_face_partition(actual_faces, expected_faces,*,additional_source_membership=()):
    """Require finite XYZ/UV/material/winding and complete parent coverage.

    The caller supplies separately reviewed parents. A writer-produced face
    list is not an acceptable expected contract for a production check.
    """
    from shapely.geometry import Polygon
    from shapely import constrained_delaunay_triangles
    from shapely.ops import unary_union
    expected_faces = tuple(expected_faces)
    require(expected_faces, 'Diagonal independent surface review is absent')
    children = defaultdict(list)
    parent_index = defaultdict(set)
    def keys(points):
        low = [math.floor((min(p[i] for p in points)-POSITION_EPS)/2.) for i in (0, 1)]
        high = [math.floor((max(p[i] for p in points)+POSITION_EPS)/2.) for i in (0, 1)]
        return ((x, y) for x in range(low[0], high[0]+1) for y in range(low[1], high[1]+1))
    for index, parent in enumerate(expected_faces):
        require(parent.get('material_sha256') is not None,
                'Diagonal surface contract omits an exact material fingerprint')
        for key in keys(parent['points']):
            parent_index[parent['role'], parent.get('texture'), key].add(index)
    maximum_uv_error = 0.
    contact_members=0
    for original_actual in actual_faces:
        # Several overlapping analysis witnesses can describe the SAME
        # saved triangle. They are not duplicate DAT faces; real distinct
        # indexed triangles receive different tokens and remain checked.
        actual={**original_actual,'_verification_saved_face_token':object(),
            '_verification_saved_points':original_actual['points']}
        require(_area(actual['points']) > 0., 'Saved diagonal model has a degenerate triangle')
        candidates = []
        possible = set()
        for key in keys(actual['points']):
            possible.update(parent_index.get((actual['role'], actual.get('texture'), key), ()))
        for index in possible:
            parent = expected_faces[index]
            wanted = parent.get('material_sha256')
            if _material_fingerprint(actual, parent) != wanted:
                continue
            if any(max(p[i] for p in actual['points']) < min(p[i] for p in parent['points'])-POSITION_EPS
                or min(p[i] for p in actual['points']) > max(p[i] for p in parent['points'])+POSITION_EPS
                for i in range(3)):
                continue
            if _dot(_normal(actual['points']), _normal(parent['points'])) <= 0.:
                continue
            weights = [_field_weights(p, t, parent) for p, t in zip(actual['points'], actual['uv'])]
            if any(w is None for w in weights):
                continue
            error = max(math.dist(t, tuple(sum(w[k]*parent['uv'][k][i] for k in range(3)) for i in range(2)))
                        for t, w in zip(actual['uv'], weights))
            candidates.append((error, index, weights))
        if not candidates:
            pieces=_piecewise_source_faces(actual,[(index,expected_faces[index]) for index in possible])
            if pieces:
                for index,polygon,child in pieces:
                    children[index].append((polygon,child))
                continue
        if not candidates and additional_source_membership:
            # Native source roof partition boundaries can encode a finite
            # contact strip whose exact source crop has zero plan area.
            # This certifies ONLY membership in the original finite source
            # continuation; the caller must still check every raw actual
            # overlap with the already-rendered source and the whole shell.
            members=[parent for parent in additional_source_membership
                if parent['role']==actual['role'] and parent['texture']==actual['texture']
                and _material_fingerprint(actual,parent)==parent['material_sha256']
                and _dot(_normal(actual['points']),_normal(parent['points']))>0.
                and all(_field_weights(p,t,parent) is not None
                    for p,t in zip(actual['points'],actual['uv']))]
            if members:
                contact_members+=1
                continue
        require(candidates, 'Saved diagonal face changes its finite source surface, material, UV, or winding; '
                f'role={actual["role"]}, points={actual["points"]}, UV={actual["uv"]}')
        error, parent, weights = min(candidates)
        maximum_uv_error = max(maximum_uv_error, error)
        polygon = Polygon([(w[1], w[2]) for w in weights])
        require(polygon.area > 0., 'Saved diagonal face collapses in its source field')
        children[parent].append((polygon, actual))
    for index, parent in enumerate(expected_faces):
        require(index in children, 'Diagonal model omits an entire reviewed surface')
        pieces = children[index]
        union = unary_union([p for p, _actual in pieces])
        target = Polygon(((0., 0.), (1., 0.), (0., 1.)))
        def world(p):
            weights = (1.-p[0]-p[1], p[0], p[1])
            return tuple(sum(weights[k]*parent['points'][k][i] for k in range(3)) for i in range(3))
        missing = target.difference(union)
        if not missing.is_empty and missing.area > 0.:
            for region in _positive_polygons(missing):
                vertices = [world(p) for p in list(region.exterior.coords)[:-1]]
                if any(all(_point_triangle_distance(p, actual['points']) <= POSITION_EPS for p in vertices)
                       for _poly, actual in pieces):
                    continue
                if _finite_triangle_union_covers(vertices,parent['points'],
                        [actual['points'] for _poly,actual in pieces]):
                    continue
                for patch in constrained_delaunay_triangles(region).geoms:
                    if patch.area <= 0.:
                        continue
                    vertices = [world(p) for p in list(patch.exterior.coords)[:-1]]
                    # Distance to a finite convex triangle is convex. One
                    # actual triangle bounding every lifted vertex bounds
                    # the entire patch under the SAME 3D Euclidean budget.
                    require(any(all(_point_triangle_distance(p, actual['points']) <= POSITION_EPS
                                    for p in vertices) for _poly, actual in pieces),
                            'Diagonal model has a missing finite pavement, body, barrier, or support patch; '
                            f'role={parent["role"]}, parent={parent["points"]}, missing_patch={vertices}')
        # A duplicate may only be an actual finite-edge encoding contact.
        # An interior thin sliver still rejects, regardless of its area.
        from .y_junction_models_verify import _finite_edge_contact_region
        for at, (first, first_actual) in enumerate(pieces):
            for second, second_actual in pieces[at+1:]:
                if first_actual.get('_verification_saved_face_token') is second_actual.get('_verification_saved_face_token'):
                    continue
                overlap = first.intersection(second)
                if overlap.area <= 0.:
                    continue
                for region in _positive_polygons(overlap):
                    vertices = [world(p) for p in list(region.exterior.coords)[:-1]]
                    first_points=first_actual.get('_verification_saved_points',first_actual['points'])
                    second_points=second_actual.get('_verification_saved_points',second_actual['points'])
                    require(finite_edge_contact(vertices,first_points,second_points)
                            or _finite_edge_contact_region(vertices,first_points,second_points),
                            'Diagonal duplicate faces conceal a missing finite surface')
    return {'passed': True, 'saved_indexed_faces_checked': len(actual_faces),
            'reviewed_source_faces_checked': len(expected_faces),
            'maximum_affine_uv_error': maximum_uv_error,
            'surface_distance_tolerance_m': POSITION_EPS, 'uv_distance_tolerance': UV_EPS,
            'source_specific_native_exceptions_inherited': False,
            'additional_finite_source_membership_faces':contact_members,
            'raw_contact_and_shell_checks_still_required':bool(additional_source_membership)}


def check_city_encoded_surfaces(actual_faces,expected_faces,*,variant='original'):
    """Fast exact encoding proof, with strict original-parent residual checks.

    Independently reconstructed world triangles are cut by the declared city
    rectangles, snapped only at the existing1nm city boundary, and encoded as
    local Float32 XYZUV. Exact indexed matches need no repeated plane solve.
    Any mismatch falls back to the ORIGINAL unencoded finite source parents,
    preserving one4µm budget rather than adding an encoding tolerance twice.
    """
    from collections import deque
    expected_faces=tuple(expected_faces)
    cells=set(contract.candidate_layout_for_measurement(variant)['world_cells'])
    encoded=[]
    maximum=0.
    collapsed=0
    for source_index,face in enumerate(expected_faces):
        vertices=[(*p,*uv) for p,uv in zip(face['points'],face['uv'])]
        east,north=[p[0] for p in vertices],[p[1] for p in vertices]
        c0,c1=math.floor((min(east)+8.)/16.),math.floor((max(east)+8.-1e-12)/16.)
        r0,r1=math.floor((8.-max(north))/16.),math.floor((8.-min(north)-1e-12)/16.)
        for c in range(c0,max(c0,c1)+1):
            for r in range(r0,max(r0,r1)+1):
                require((c,r) in cells,'Independent reviewed middle leaves the finite city mask')
                polygon=vertices
                for axis,bound,sign in ((0,16*c-8.,1.),(0,16*c+8.,-1.),
                        (1,-16*r-8.,1.),(1,-16*r+8.,-1.)):
                    polygon=_clip_source_polygon(polygon,axis,bound,sign)
                for at in range(1,len(polygon)-1):
                    original=(polygon[0],polygon[at],polygon[at+1])
                    if _area(original)==0.:
                        continue
                    values=[]
                    for p in original:
                        local=[p[0]-16*c,p[1]+16*r,p[2],p[3],p[4]]
                        for axis in (0,1):
                            for edge in (-8.,8.):
                                if abs(local[axis]-edge)<=1e-9:
                                    local[axis]=edge
                        q=struct.unpack('<5f',struct.pack('<5f',*local))
                        point=(q[0]+16*c,q[1]-16*r,q[2])
                        maximum=max(maximum,math.dist(point,p[:3]))
                        values.append((*point,*q[3:]))
                    if _area(values)==0.:
                        collapsed+=1
                        continue
                    if _dot(_normal(values),_normal(original))<0.:
                        values[1],values[2]=values[2],values[1]
                    encoded.append({**face,'points':tuple(p[:3] for p in values),
                        'uv':tuple(p[3:] for p in values),'cell':(c,r),'source_index':source_index})
    require(maximum<=POSITION_EPS,'Independent Float32 encoding itself exceeds the declared physical bound')
    material_templates={}
    for face in expected_faces:
        key=face['role'],face['texture']
        material_templates[key]=face
    def signature(face,actual=False):
        template=material_templates.get((face['role'],face['texture']))
        digest=_material_fingerprint(face,template) if actual and template else face.get('material_sha256')
        c,r=face['cell']
        points=[struct.pack('<5f',p[0]-16*c,p[1]+16*r,p[2],*uv)
            for p,uv in zip(face['points'],face['uv'])]
        cyclic=min(tuple(points[i:]+points[:i]) for i in range(3))
        return face['role'],face['texture'],digest,tuple(face['cell']),cyclic
    wanted=defaultdict(deque)
    for index,face in enumerate(encoded):
        wanted[signature(face)].append(index)
    unmatched=[];matched=defaultdict(list)
    for face in actual_faces:
        key=signature(face,True)
        if wanted.get(key):
            index=wanted[key].popleft()
            matched[encoded[index]['source_index']].append(face)
        else:
            unmatched.append(face)
    residual_ids={encoded[i]['source_index'] for indices in wanted.values() for i in indices}
    for actual in unmatched:
        for index,parent in enumerate(expected_faces):
            if parent['role']==actual['role'] and parent['texture']==actual['texture'] and all(
                max(p[axis] for p in actual['points'])>=min(p[axis] for p in parent['points'])-POSITION_EPS
                and min(p[axis] for p in actual['points'])<=max(p[axis] for p in parent['points'])+POSITION_EPS
                for axis in range(3)):
                residual_ids.add(index)
    residual=None
    if residual_ids or unmatched:
        residual=check_face_partition([*unmatched,*(face for index in residual_ids for face in matched[index])],
            [expected_faces[index] for index in sorted(residual_ids)])
    return {'passed':True,'actual_saved_triangles_checked':len(actual_faces),
        'independent_world_source_triangles':len(expected_faces),'independently_city_encoded_triangles':len(encoded),
        'exact_float32_matches':len(actual_faces)-len(unmatched),
        'maximum_independent_encoding_displacement_m':maximum,
        'exact_zero_encoded_source_fragments':collapsed,'original_parent_residual_check':residual,
        'combined_euclidean_bound_m':POSITION_EPS,'triangle_winding_preserved':True}


def _base_height(deck, station):
    height = contract.upper_height(station) if deck == 'upper' else contract.lower_height(station)
    return height+DATUM[deck]*height/(15. if deck == 'upper' else 7.5)


def _clamp_root(deck):
    low, high = contract.FLAT_ENVELOPE, contract.LENGTH-contract.FLAT_ENVELOPE
    for _ in range(64):
        middle = (low+high)/2.
        if _base_height(deck, middle) > 1.:
            low = middle
        else:
            high = middle
    return (low+high)/2.


def middle_stations():
    """Reviewed common rings, including both exact ground-clamp roots."""
    start, end = contract.FLAT_ENVELOPE+1., contract.LENGTH-contract.FLAT_ENVELOPE-1.
    return tuple(sorted({start, end, *(s for s in contract.BREAKS if start < s < end),
        *(i*contract.STATION_STEP for i in range(math.floor(contract.LENGTH/contract.STATION_STEP)+1)
          if start < i*contract.STATION_STEP < end),
        *(_clamp_root(deck) for deck in ('upper', 'lower'))}))


def _middle_roof_profile(deck,station,variant,atlas_id):
    """The declared numerical cross-section, independent of writer callbacks."""
    phase=contract.phase_for_options(variant)
    base=_base_height(deck,station)
    nominal=contract.upper_height(station) if deck=='upper' else contract.lower_height(station)
    inside=7.171875
    asphalt=sorted({-inside,inside,0.,*(sign*(contract.LANE_OFFSET+offset)
        for sign in (-1,1) for offset in (-1.25,0.,1.25))})
    rows=[]
    def asphalt_uv(u):
        t=(u+8.)/16.
        if phase.physical_reflection!=phase.traffic_reversed:
            t=1.-t
        if deck=='lower':
            t=1.-t
        return ((8. if deck=='upper' else 264.)+128.*t)/512.,(128.+8.*station)/1024.
    for low,high in zip(asphalt,asphalt[1:]):
        rows.append({'kind':'pavement','low':low,'high':high,'heights':(base,base),
            'uv':(asphalt_uv(low),asphalt_uv(high)),'texture':atlas_id,
            'material_sha256':GROUND_MATERIAL_SHA256,'source_material_texture':0x5703000E})
    insets=(0.,.21875,.265625,.5625,.625,.828125)
    crown=1.3906240463256836 if deck=='upper' else 1.3906254768371582
    rise=(0.,.328125,crown,crown,.328125,0.)
    bands=((1.,.7119640111923218),(.7119640111923218,0.),
        (.32499998807907104,.625),(0.,.7119640111923218),(.7119640111923218,1.))
    for side in (-1,1):
        for band in range(5):
            a=(side*(8.-insets[band]),base+rise[band]*contract._cubic(nominal/2.),(station/16.,bands[band][0]))
            b=(side*(8.-insets[band+1]),base+rise[band+1]*contract._cubic(nominal/2.),(station/16.,bands[band][1]))
            a,b=sorted((a,b))
            rows.append({'kind':'barrier','low':a[0],'high':b[0],'heights':(a[1],b[1]),
                'uv':(a[2],b[2]),'texture':0x5EB4BEE9,'material_sha256':BARRIER_MATERIAL_SHA256})
    return sorted(rows,key=lambda row:row['low'])


def _expected_quad(faces,role,points,normal,texture,material,**extra):
    for ids in ((0,1,2),(0,2,3)):
        vertices=[points[i] for i in ids]
        if _area(vertices)==0.:
            continue
        if _dot(_normal(vertices),normal)<0.:
            vertices[1],vertices[2]=vertices[2],vertices[1]
        faces.append({'role':role,'points':tuple(p[:3] for p in vertices),
            'uv':tuple(p[3:] for p in vertices),'texture':texture,'material_sha256':material,**extra})


def dd_bridge_surface_contract(atlas_id,*,variant='original'):
    """Rebuild the reviewed one-metre native-profile-to-middle bridge."""
    from shapely.geometry import Polygon
    from shapely.ops import unary_union
    sources=collar_source_inputs()['variants'][variant]
    regions=native_collar_regions(variant)
    # Sections come from independently reconstructed finite source panels,
    # including their city-cut vertices, never runtime writer groups.
    panels=native_dd_profile_surfaces(variant=variant)
    raw_profiles=sources['DD_profiles']
    faces=[];floor_faces=[]
    start=contract.FLAT_ENVELOPE;finish=start+1.
    stations=sorted({start,finish,*(s for s in contract.BREAKS if start<s<finish),
        *(i*.125 for i in range(math.floor(contract.LENGTH/.125)+1) if start<i*.125<finish)})
    for deck in ('upper','lower'):
        centre,normal=contract.frame(deck,start,variant=variant)
        local=lambda p:_dot(_sub(p[:2],centre),normal)
        segments=[]
        for panel in panels:
            if panel['role'] not in (f'raw-dd-{deck}-pavement',f'raw-dd-{deck}-barrier'):
                continue
            vertices=[(*p,*uv) for p,uv in zip(panel['points'],panel['uv'])]
            values=[_dot(_sub(p[:2],centre),contract.LONGITUDINAL) for p in vertices]
            values=[0. if abs(v)<1e-11 else v for v in values]
            points=[]
            for a,b,x,y in zip(vertices,(*vertices[1:],vertices[0]),values,(*values[1:],values[0])):
                if x==0.:
                    points.append(a)
                if x*y<0.:
                    t=x/(x-y);points.append(tuple(u+t*(v-u) for u,v in zip(a,b)))
            unique=[]
            for p in points:
                if not any(math.dist(p[:3],q[:3])<1e-10 for q in unique):
                    unique.append(p)
            if len(unique)!=2:
                continue
            a,b=sorted(unique,key=local)
            if local(b)-local(a)>1e-10:
                source=panel['source_record']
                segments.append((local(a),local(b),a,b,source))
        phase_regions=[]
        candidates=[]
        for record in sources['DD_references']:
            if record['deck']==deck and record['role']=='pavement':
                candidates.append((record,unary_union([Polygon([p[:2] for p in crop['polygon_ENH']])
                    for crop in record['finite_city_crops']]),True))
        candidates.extend((row['source'],row['geometry'],False) for row in regions[deck]['phase_roofs'])
        taken=Polygon()
        for source,shape,reference in sorted(candidates,key=lambda row:(row[0]['native_owner_kind']!='helper',not row[2])):
            shape=shape.difference(taken)
            phase_regions.extend((a,b,_source_height(source,*centre))
                for a,b in _inner_boundary_intervals(shape,centre,normal))
            taken=unary_union([taken,shape])
        require(segments and phase_regions,'Independent DD bridge omits a finite source roof/floor section')
        low=min(a for a,b,h in phase_regions);high=max(b for a,b,h in phase_regions)
        anchors=((low,-8.),(-contract.LANE_OFFSET,-contract.LANE_OFFSET),(0.,0.),
            (contract.LANE_OFFSET,contract.LANE_OFFSET),(high,8.))
        def mapped(u):
            for (a,x),(b,y) in zip(anchors,anchors[1:]):
                if a-1e-10<=u<=b+1e-10:
                    return x+(u-a)*(y-x)/(b-a)
            raise ValueError('Independent DD bridge source shoulder leaves its finite cross-section')
        def inverse(u):
            for (a,x),(b,y) in zip(anchors,anchors[1:]):
                if x-1e-10<=u<=y+1e-10:
                    return a+(u-x)*(b-a)/(y-x)
            raise ValueError('Independent DD middle profile leaves its declared width')
        target=_middle_roof_profile(deck,finish,variant,atlas_id)
        cuts={low,high,-contract.LANE_OFFSET,0.,contract.LANE_OFFSET}
        for a,b,*unused in segments:
            cuts.update((max(low,a),min(high,b)))
        for a,b,h in phase_regions:
            cuts.update((a,b))
        for row in target:
            cuts.update((inverse(row['low']),inverse(row['high'])))
        cuts=sorted(u for u in cuts if low-1e-9<=u<=high+1e-9)
        unique=[]
        for u in cuts:
            if not unique or abs(u-unique[-1])>1e-10:
                unique.append(u)
        strips=[]
        for low_u,high_u in zip(unique,unique[1:]):
            if high_u-low_u<=1e-12:
                continue
            mid=(low_u+high_u)/2.
            def native_at(row,u):
                a,b,x,y,source=row;t=(u-a)/(b-a)
                return tuple(x[i]+t*(y[i]-x[i]) for i in range(5))
            possible=[row for row in segments if row[0]-1e-8<=mid<=row[1]+1e-8]
            require(possible,'Independent DD bridge has a source-profile hole')
            source=max(possible,key=lambda row:native_at(row,mid)[2])
            phases=[h for a,b,h in phase_regions if a-1e-8<=mid<=b+1e-8]
            require(phases,'Independent DD bridge has no finite native floor phase')
            base=min(phases)
            index=next(i for i,row in enumerate(target) if row['low']-1e-8<=mapped(mid)<=row['high']+1e-8)
            kind=target[index]['kind'];native_source=source[4]
            rings=[];floors=[]
            for s in stations:
                t=s-start;row=_middle_roof_profile(deck,s,variant,atlas_id)[index]
                c,n=contract.frame(deck,s,variant=variant)
                tops=[];bottoms=[]
                nominal_height=contract.upper_height(s) if deck=='upper' else contract.lower_height(s)
                faded=DATUM[deck]*nominal_height/(15. if deck=='upper' else 7.5)
                for u in (low_u,high_u):
                    v=mapped(u);fraction=(v-row['low'])/(row['high']-row['low'])
                    target_height=row['heights'][0]+fraction*(row['heights'][1]-row['heights'][0])
                    np=native_at(source,u)
                    phase_base=nominal_height+(1.-t)*(base-(15. if deck=='upper' else 7.5))+t*faded
                    height=phase_base+(1.-t)*(np[2]-base)+t*(target_height-nominal_height-faded)
                    lateral=(1.-t)*u+t*v
                    en=tuple(c[i]+lateral*n[i] for i in range(2))
                    tops.append((*en,height,*_source_attributes(native_source,(*en,height))))
                    bottom=max(0.,nominal_height-1.+t*faded)
                    bottoms.append((*en,bottom,en[0]/8.,en[1]/8.))
                rings.append(tops);floors.append(bottoms)
            role=f'dd-bridge-{deck}-{kind}'
            for a,b,x,y in zip(rings,rings[1:],floors,floors[1:]):
                _expected_quad(faces,role,(a[0],a[1],b[1],b[0]),(0.,0.,1.),
                    native_source['source_texture_ids'][0],native_source['source_material_sha256'])
                _expected_quad(faces,f'dd-bridge-{deck}-body',(x[0],x[1],y[1],y[0]),(0.,0.,-1.),
                    0x5EB4BEEE,BODY_MATERIAL_SHA256)
                _expected_quad(floor_faces,f'dd-bridge-{deck}-body',(x[0],x[1],y[1],y[0]),(0.,0.,-1.),
                    0x5EB4BEEE,BODY_MATERIAL_SHA256)
            strips.append((rings,floors))
        for index,(rings,floors) in enumerate(strips):
            for side in (0,1):
                adjacent=index-1 if side==0 else index+1
                hint=tuple((1. if side else -1.)*v for v in (*normal,0.))
                if not 0<=adjacent<len(strips):
                    for a,b,x,y in zip(rings,rings[1:],floors,floors[1:]):
                        _expected_quad(faces,f'dd-bridge-{deck}-body',(a[side],b[side],y[side],x[side]),hint,
                            0x5EB4BEEE,BODY_MATERIAL_SHA256)
                else:
                    other_tops,other_floors=strips[adjacent]
                    for a,b,c,d in zip(rings,rings[1:],other_tops,other_tops[1:]):
                        if max(abs(a[side][2]-c[1-side][2]),abs(b[side][2]-d[1-side][2]))<1e-11:
                            continue
                        if a[side][2]+b[side][2]>=c[1-side][2]+d[1-side][2]:
                            _expected_quad(faces,f'dd-bridge-{deck}-body',
                                (a[side],b[side],d[1-side],c[1-side]),hint,0x5EB4BEEE,BODY_MATERIAL_SHA256)
    return faces,floor_faces


def ground_bridge_surface_contract(atlas_id,*,variant='original'):
    """Rebuild both finite native-ground-to-middle bridges from source crops."""
    data=collar_source_inputs()['variants'][variant]
    start=contract.LENGTH-contract.FLAT_ENVELOPE-1.;finish=start+1.
    stations=sorted({start,finish,*(s for s in contract.BREAKS if start<s<finish),
        *(i*.125 for i in range(math.floor(contract.LENGTH/.125)+1) if start<i*.125<finish)})
    faces=[]
    for deck in ('upper','lower'):
        c,n=contract.frame(deck,finish,variant=variant)
        local=lambda p:_dot(_sub(p[:2],c),n)
        profiles=[]
        for source in data['ground'][deck]['literal_source_fragments']:
            for segment in source['inner_profile_ENHUV']:
                a,b=sorted(segment,key=local)
                profiles.append((local(a),local(b),a,b))
        low=min(a for a,b,x,y in profiles);high=max(b for a,b,x,y in profiles)
        target=_middle_roof_profile(deck,start,variant,atlas_id)
        cuts={0.,1.}
        for a,b,x,y in profiles:
            cuts.update(((a-low)/(high-low),(b-low)/(high-low)))
        for row in target:
            cuts.update(((row['low']+8.)/16.,(row['high']+8.)/16.))
        cuts=sorted(min(1.,max(0.,u)) for u in cuts if -1e-10<=u<=1.+1e-10)
        unique=[]
        for u in cuts:
            if not unique or abs(u-unique[-1])>1e-12:
                unique.append(u)
        def native_at(t):
            u=low+(high-low)*t
            row=next((row for row in profiles if row[0]-2e-9<=u<=row[1]+2e-9),None)
            require(row is not None,'Independent ground bridge has a finite source-profile gap')
            a,b,x,y=row;v=(u-a)/(b-a)
            return tuple(x[i]+v*(y[i]-x[i]) for i in range(5))
        strips=[]
        for first,last in zip(unique,unique[1:]):
            if last==first:
                continue
            mid=-8.+8.*(first+last)
            index=next(i for i,row in enumerate(target) if row['low']-1e-8<=mid<=row['high']+1e-8)
            field=target[index];rings=[];floors=[]
            for s in stations:
                row=_middle_roof_profile(deck,s,variant,atlas_id)[index]
                c,n=contract.frame(deck,s,variant=variant);alpha=s-start
                top=[];bottom=[]
                for t in (first,last):
                    u=-8.+16.*t;fraction=(u-row['low'])/(row['high']-row['low'])
                    height=row['heights'][0]+fraction*(row['heights'][1]-row['heights'][0])
                    uv=tuple(row['uv'][0][i]+fraction*(row['uv'][1][i]-row['uv'][0][i]) for i in range(2))
                    lateral=(1.-alpha)*u+alpha*(low+(high-low)*t)
                    en=tuple(c[i]+lateral*n[i] for i in range(2))
                    if s==finish:
                        en=native_at(t)[:2]
                    top.append((*en,height,*uv))
                    bottom.append((*en,0.,lateral/8.,s/8.))
                rings.append(top);floors.append(bottom)
            role=deck+('-pavement-atlas' if field['kind']=='pavement' else '-barrier')
            extra={'source_material_texture':0x5703000E} if field['kind']=='pavement' else {}
            for a,b,x,y in zip(rings,rings[1:],floors,floors[1:]):
                _expected_quad(faces,role,(a[0],a[1],b[1],b[0]),(0.,0.,1.),
                    field['texture'],field['material_sha256'],**extra)
                if max(p[2] for p in (*a,*b))>0.:
                    _expected_quad(faces,deck+'-body',(x[0],x[1],y[1],y[0]),(0.,0.,-1.),
                        0x5EB4BEEE,BODY_MATERIAL_SHA256)
            strips.append((first,last,rings))
        for side in (0,1):
            t=float(side)
            for first,last,rings in strips:
                if abs((first if side==0 else last)-t)>=1e-10:
                    continue
                for a,b in zip(rings,rings[1:]):
                    x,y=a[side],b[side]
                    _expected_quad(faces,deck+'-body',(x,y,(y[0],y[1],0.,*y[3:]),(x[0],x[1],0.,*x[3:])),
                        tuple((1. if side else -1.)*v for v in (*n,0.)),0x5EB4BEEE,BODY_MATERIAL_SHA256)
    return faces


def check_ground_bridge_surfaces(faces,atlas_id,*,variant='original'):
    expected=ground_bridge_surface_contract(atlas_id,variant=variant)
    end=contract.LENGTH-contract.FLAT_ENVELOPE-1.
    roles={f['role'] for f in expected}
    actual=[]
    for face in faces:
        if face['role'] not in roles:
            continue
        deck=face['role'].split('-')[0]
        center=tuple(sum(p[i] for p in face['points'])/3. for i in range(3))
        if _station_for_point(center,deck,variant)>end+1e-9:
            actual.append(face)
    return check_face_partition(actual,expected)


def middle_surface_contract(atlas_id, *, variant='original'):
    """Independent new-only base slab, asphalt, rails, and support fields.

    Each floor interval uses the SAME geometric diagonal as its base roof.
    This reconstructs the reviewed mathematical contract, not writer groups.
    Native collars and their finite bridge/source scopes are separate inputs.
    """
    phase = contract.phase_for_options(variant)
    inside = 7.171875
    asphalt = sorted({-inside, inside, 0., *(sign*(contract.LANE_OFFSET+offset)
                     for sign in (-1, 1) for offset in (-1.25, 0., 1.25))})
    insets = (0., .21875, .265625, .5625, .625, .828125)
    bottom = sorted({*asphalt, *(sign*(8.-inset) for sign in (-1, 1) for inset in insets)})
    faces, bases = [], []
    def point(deck, s, u, h, uv):
        center, normal = contract.frame(deck, s, variant=variant)
        return center[0]+u*normal[0], center[1]+u*normal[1], h, *uv
    def concrete_uv(s, u, h):
        return u/8., (s+h)/8.
    def asphalt_uv(deck, s, u):
        lateral = (u+8.)/16.
        if phase.physical_reflection != phase.traffic_reversed:
            lateral = 1.-lateral
        if deck == 'lower':
            lateral = 1.-lateral
        return ((8. if deck == 'upper' else 264.)+128.*lateral)/512., (128.+8.*s)/1024.
    def quad(role, vertices, hint, texture, material, *, base=False, atlas=False):
        for indices in ((0, 1, 2), (0, 2, 3)):
            points = tuple(vertices[i][:3] for i in indices)
            uv = tuple(vertices[i][3:] for i in indices)
            if _area(points) == 0.:
                continue
            if _dot(_normal(points), hint) < 0.:
                points, uv = (points[0], points[2], points[1]), (uv[0], uv[2], uv[1])
            record = {'role': role, 'points': points, 'uv': uv, 'texture': texture,
                      'material_sha256': material}
            if atlas:
                record['source_material_texture'] = 0x5703000E
            (bases if base else faces).append(record)
    stations = middle_stations()
    for deck in ('upper', 'lower'):
        crown = 1.3906240463256836 if deck == 'upper' else 1.3906254768371582
        rises = (0., .328125, crown, crown, .328125, 0.)
        bands = ((1., .7119640111923218), (.7119640111923218, 0.),
                 (.32499998807907104, .625), (0., .7119640111923218), (.7119640111923218, 1.))
        for first, last in zip(stations, stations[1:]):
            heights = [_base_height(deck, s) for s in (first, last)]
            floors = [max(0., h-1.) for h in heights]
            for low, high in zip(bottom, bottom[1:]):
                vertices = [point(deck, s, u, h, concrete_uv(s, u, h))
                    for s, u, h in ((first, low, heights[0]), (first, high, heights[0]),
                                    (last, high, heights[1]), (last, low, heights[1]))]
                quad(deck+'-base', vertices, (0., 0., 1.), 0, BODY_MATERIAL_SHA256, base=True)
                if heights != [0., 0.]:
                    vertices = [point(deck, s, u, h, concrete_uv(s, u, h))
                        for s, u, h in ((first, low, floors[0]), (first, high, floors[0]),
                                        (last, high, floors[1]), (last, low, floors[1]))]
                    quad(deck+'-body', vertices, (0., 0., -1.), 0x5EB4BEEE, BODY_MATERIAL_SHA256)
            for low, high in zip(asphalt, asphalt[1:]):
                vertices = [point(deck, s, u, h, asphalt_uv(deck, s, u))
                    for s, u, h in ((first, low, heights[0]), (first, high, heights[0]),
                                    (last, high, heights[1]), (last, low, heights[1]))]
                quad(deck+'-pavement-atlas', vertices, (0., 0., 1.), atlas_id,
                     GROUND_MATERIAL_SHA256, atlas=True)
            for side in (-1, 1):
                u = side*8.
                normal = contract.frame(deck, (first+last)/2., variant=variant)[1]
                vertices = [point(deck, s, u, h, concrete_uv(s, u, h))
                    for s, h in ((first, heights[0]), (first, floors[0]),
                                 (last, floors[1]), (last, heights[1]))]
                if side < 0:
                    vertices = [vertices[1], vertices[0], vertices[3], vertices[2]]
                quad(deck+'-body', vertices, (side*normal[0], side*normal[1], 0.),
                     0x5EB4BEEE, BODY_MATERIAL_SHA256)
                for band in range(5):
                    left = (side*(8.-insets[band]), rises[band], bands[band][0])
                    right = (side*(8.-insets[band+1]), rises[band+1], bands[band][1])
                    if side > 0:
                        left, right = right, left
                    vertices = []
                    for s, node in ((first, left), (first, right), (last, right), (last, left)):
                        nominal = contract.upper_height(s) if deck == 'upper' else contract.lower_height(s)
                        h = _base_height(deck, s)+node[1]*contract._cubic(nominal/2.)
                        vertices.append(point(deck, s, node[0], h, (s/16., node[2])))
                    delta_u, delta_h = right[0]-left[0], right[1]-left[1]
                    hint = (-delta_h*normal[0], -delta_h*normal[1], delta_u)
                    quad(deck+'-barrier', vertices, hint, 0x5EB4BEE9, BARRIER_MATERIAL_SHA256)
    for solid in support_contract(variant=variant):
        for face in _prism_faces(solid, solid['id']):
            face['uv'] = tuple((p[0]/8., (-p[1]+p[2])/8.) for p in face['points'])
            face.pop('auxiliary_axes')
            faces.append(face)
    return tuple(faces), tuple(bases)


def check_corridors(faces, routes, pavement_roles):
    """Inspect actual finite indexed geometry against every saved lane chord."""
    from .ramp_verify import _covered, _intrudes
    count, tests = 0, 0
    for route in routes:
        pavement = [f for f in faces if f['role'] in pavement_roles[route['component']]]
        for first, last in zip(route['points'], route['points'][1:]):
            require(_covered(first, last, pavement), 'Saved diagonal lane lacks continuous pavement')
            for face in faces:
                if max(p[2] for p in face['points']) <= min(first[2], last[2])+.00001:
                    continue
                if min(p[2] for p in face['points']) > max(first[2], last[2])+3.8:
                    continue
                if any(max(p[i] for p in face['points']) < min(first[i], last[i])-1.25
                       or min(p[i] for p in face['points']) > max(first[i], last[i])+1.25 for i in (0, 1)):
                    continue
                tests += 1
                require(not _intrudes(first, last, face['points'], 1.25, 3.8),
                        'Saved diagonal body, barrier, support, or opposing road enters a vehicle corridor')
            count += 1
    return {'passed': True, 'continuous_saved_segments_checked': count,
            'actual_face_prism_intersections_checked': tests, 'half_width_m': 1.25, 'height_m': 3.8}


def support_contract(*, variant='original'):
    """Independently positioned complete support prisms in the source frame."""
    contract.phase_for_options(variant)
    result = []
    def underside(deck, station):
        nominal = contract.upper_height(station) if deck == 'upper' else contract.lower_height(station)
        return max(0., nominal+DATUM[deck]*nominal/(15. if deck == 'upper' else 7.5)-1.)
    for reference in (12., 32., 52., 72.):
        station = reference*contract.LENGTH/96.
        top = underside('upper', station)
        outside = -9.2 if reference == 12. else -6.4
        result.extend(({'id': f'upper-pier-{int(reference)}', 'deck': 'upper', 'station_m': station,
            'lateral_range_m': (outside-.4, outside+.4), 'station_half_length_m': .4,
            'bottom_m': 0., 'top_m': top-.3},
            {'id': f'upper-cap-{int(reference)}', 'deck': 'upper', 'station_m': station,
            'lateral_range_m': (min(-7., outside-.4), 7.), 'station_half_length_m': .45,
            'bottom_m': top-.3, 'top_m': top}))
    for reference in (12., 32., 48.):
        station = reference*contract.LENGTH/96.
        for side in (-1, 1):
            result.append({'id': f'lower-pier-{int(reference)}-{side}', 'deck': 'lower',
                'station_m': station, 'lateral_range_m': (side*6.4-.4, side*6.4+.4),
                'station_half_length_m': .4, 'bottom_m': 0., 'top_m': underside('lower', station)})
    for row in result:
        station, half = row['station_m'], row['station_half_length_m']
        low, high = row['lateral_range_m']
        corners = []
        for s, lateral in ((station-half, low), (station+half, low),
                           (station+half, high), (station-half, high)):
            center, normal = contract.frame(row['deck'], s, variant=variant)
            corners.append(tuple(center[i]+lateral*normal[i] for i in range(2)))
        row['corners_EN_m'] = tuple(corners)
        require(row['top_m'] > row['bottom_m'], 'Independent diagonal support collapsed')
    return tuple(result)


def _prism_faces(solid, role):
    vertices = [(*p, height) for height in (solid['bottom_m'], solid['top_m'])
                for p in solid['corners_EN_m']]
    middle = tuple(sum(p[i] for p in vertices)/8. for i in range(3))
    result = []
    for indices in ((0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1),
                    (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 0)):
        quad = [vertices[i] for i in indices]
        outward = tuple(sum(p[i] for p in quad)/4.-middle[i] for i in range(3))
        for selected in ((0, 1, 2), (0, 2, 3)):
            points = tuple(quad[i] for i in selected)
            if _dot(_normal(points), outward) < 0.:
                points = points[0], points[2], points[1]
            # This auxiliary field is used only for solid XYZ completeness.
            # Saved authored texture fields are checked separately.
            normal = _normal(points)
            dropped = max(range(3), key=lambda i: abs(normal[i]))
            axes = [i for i in range(3) if i != dropped]
            uv = tuple(tuple(p[i]/16. for i in axes) for p in points)
            result.append({'role': role, 'points': points, 'uv': uv, 'texture': 0x5EB4BEEE,
                           'material_sha256': BODY_MATERIAL_SHA256, 'auxiliary_axes': axes})
    return result


def check_support_solids(faces, *, variant='original', role_prefix=''):
    """Prove every actual saved support retains its six complete finite sides."""
    count = 0
    total = 0
    for solid in support_contract(variant=variant):
        role = role_prefix+solid['id']
        actual = [face for face in faces if face['role'] == role]
        require(actual, 'Diagonal model omits an entire support solid')
        expected = _prism_faces(solid, role)
        # Choose the expected finite plane per saved triangle without using
        # writer labels to certify its geometry. Actual UVs are left intact
        # for the separate material/profile surface check.
        auxiliary = []
        for face in actual:
            candidates = [p for p in expected if all(_point_triangle_distance(v, p['points']) <= POSITION_EPS
                for v in face['points']) and _dot(_normal(face['points']), _normal(p['points'])) > 0.]
            require(candidates, 'Saved diagonal support leaves its complete independent finite prism')
            axes = candidates[0]['auxiliary_axes']
            auxiliary.append({**face, 'uv': tuple(tuple(p[i]/16. for i in axes) for p in face['points'])})
        check_face_partition(auxiliary, expected)
        count += 1
        total += len(actual)
    return {'passed': True, 'complete_closed_support_solids': count,
            'actual_saved_support_triangles_checked': total,
            'all_six_finite_faces_per_solid_checked': True, 'structural_capacity_tested': False}


def check_support_opposing_road_clearance(faces,*,variant='original'):
    """Clip actual opposing road faces against every complete support prism."""
    from shapely.geometry import Polygon,box
    from shapely.strtree import STRtree
    from .y_junction_models_verify import _clip_xy_prism,_clip_linear_polygon
    roads=[f for f in faces if f['kind'] in ('body','pavement','barrier')]
    boxes=[box(min(p[0] for p in f['points']),min(p[1] for p in f['points']),
        max(p[0] for p in f['points']),max(p[1] for p in f['points'])) for f in roads]
    tree=STRtree(boxes);checked=0
    for solid in support_contract(variant=variant):
        polygon=Polygon(solid['corners_EN_m'])
        require(polygon.is_valid and polygon.area>0.,'Independent support has no finite footprint')
        for index in tree.query(polygon,predicate='intersects'):
            face=roads[int(index)]
            if face['deck']==solid['deck']:
                continue
            if max(p[2] for p in face['points'])<solid['bottom_m']-POSITION_EPS or min(
                    p[2] for p in face['points'])>solid['top_m']+POSITION_EPS:
                continue
            fragment=_clip_xy_prism(list(face['points']),polygon)
            fragment=_clip_linear_polygon(fragment,(0.,0.,1.,-solid['bottom_m']),POSITION_EPS)
            fragment=_clip_linear_polygon(fragment,(0.,0.,-1.,solid['top_m']),POSITION_EPS)
            require(_area(fragment)==0.,
                'A saved opposing road surface enters the complete independent support volume; '
                f'support={solid["id"]}, role={face["role"]}, finite_points={fragment}')
            checked+=1
    return {'passed':True,'complete_prisms_checked':14,'opposing_finite_road_intersections_checked':checked,
        'served_slab_contact_not_mistaken_for_opposing_deck':True,
        'all_support_side_and_cap_volumes_checked':True,'position_euclidean_bound_m':POSITION_EPS}


def _station_for_point(point, deck, variant):
    """Invert the independently reviewed centre curve's normal coordinates."""
    phase=contract.phase_for_options(variant)
    # A diagonal projection is a bounded start even at the22.6m upper spread.
    station=_dot(_sub(point[:2],contract.J),contract.LONGITUDINAL)
    station=min(contract.LENGTH,max(0.,station))
    sign=-1. if phase.physical_reflection else 1.
    for _ in range(12):
        offset,derivative,curvature=contract.lateral(station) if deck=='upper' else (0.,0.,0.)
        second=curvature*(1.+derivative*derivative)**1.5
        center=tuple(contract.J[i]+station*contract.LONGITUDINAL[i]
            +sign*offset*contract.TRANSVERSE[i] for i in range(2))
        tangent=tuple(contract.LONGITUDINAL[i]+sign*derivative*contract.TRANSVERSE[i] for i in range(2))
        acceleration=tuple(sign*second*v for v in contract.TRANSVERSE)
        delta=_sub(point[:2],center)
        f=_dot(delta,tangent)
        slope=-_dot(tangent,tangent)+_dot(delta,acceleration)
        require(slope<0.,'Independent diagonal normal-coordinate inverse is ambiguous')
        change=f/slope
        station=min(contract.LENGTH,max(0.,station-change))
        if abs(change)<1e-12:
            break
    return station


def check_middle_surfaces(faces,atlas_id,*,variant='original'):
    """Check the complete declared middle, including every solid support."""
    start,end=contract.FLAT_ENVELOPE+1.,contract.LENGTH-contract.FLAT_ENVELOPE-1.
    expected,bases=middle_surface_contract(atlas_id,variant=variant)
    roles={face['role'] for face in expected}
    actual=[]
    for face in faces:
        if face['role'] not in roles:
            continue
        if face['role'].startswith(('upper-pier-','upper-cap-','lower-pier-')):
            actual.append(face)
            continue
        deck='upper' if face['role'].startswith('upper-') else 'lower'
        center=tuple(sum(p[i] for p in face['points'])/3. for i in range(3))
        station=_station_for_point(center,deck,variant)
        if start-1e-9<=station<=end+1e-9:
            actual.append(face)
    surface=check_city_encoded_surfaces(actual,expected,variant=variant)
    floor=check_slab_depth(bases,actual)
    return {'passed':True,'complete_finite_surface_fields':surface,
        'full_width_one_metre_or_ground_clamped_depth':floor,
        'source_writer_imported_as_expectation':False}


def classify_faces(faces,*,variant='original'):
    """Classify saved finite triangles by the exact reviewed role namespace."""
    supports={row['id']:row['deck'] for row in support_contract(variant=variant)}
    result=[]
    for face in faces:
        role=face['role']
        if role in supports:
            kind,deck='support',supports[role]
        elif role.startswith('native-ground-literal-'):
            deck=role.split('-')[3]
            kind='pavement'
        elif role.startswith(('upper-','lower-')):
            deck=role.split('-')[0]
            kind={'pavement-atlas':'pavement','body':'body','barrier':'barrier'}.get(role[len(deck)+1:])
        elif role.startswith(('dd-upper-','dd-lower-')):
            parts=role.split('-')
            deck,kind=parts[1:3]
        else:
            raise ValueError('Saved diagonal model has an unknown surface or support role: '+role)
        require(kind in ('pavement','body','barrier','support') and deck in ('upper','lower'),
            'Saved diagonal role is outside the reviewed finite surface inventory')
        normal=_normal(face['points'])
        result.append({**face,'kind':kind,'deck':deck,'upward':normal[2]>0.,'downward':normal[2]<0.})
    return result


def native_reference_faces(*,variant='original'):
    """Rebuild only already-rendered finite source crops for interface analysis.

    These original helper/peer faces are never copied into a custom model.
    Their parent hashes, fields, exact pose, finite crop, and resource pins
    were measured independently from audited originals. A source reference
    cannot supply an authored floor or excuse a missing custom support.
    """
    from shapely import constrained_delaunay_triangles
    from shapely.geometry import shape
    data=collar_source_inputs()['variants'][variant]
    result=[]
    def add(record,points,deck,tag):
        points=tuple(tuple(p) for p in points)
        if _area(points)==0.:
            return
        normal=record['source_surface_plane_ENH']['normal']
        if _dot(_normal(points),normal)<0.:
            points=points[0],points[2],points[1]
        result.append({'role':'native-reference-'+tag,'points':points,
            'uv':tuple(_source_attributes(record,p) for p in points),
            'texture':record['source_texture_ids'][0],
            'source_material_sha256':record['source_material_sha256'],
            'source_parent_ENHUV_sha256':record['source_parent_ENHUV_sha256'],
            'source_model_sha256':record['source_model_sha256'],
            'source':record,'native_reference':True,'kind':record['role'],
            'deck':deck,'upward':_normal(points)[2]>0.,'downward':_normal(points)[2]<0.,
            'area':_area(points)})
    for index,record in enumerate(data['DD_references']):
        for crop in record['finite_city_crops']:
            points=crop['polygon_ENH']
            for at in range(1,len(points)-1):
                add(record,(points[0],points[at],points[at+1]),record['deck'],
                    f'dd-{record["deck"]}-{record["role"]}-{index}')
    for deck,ground in data['ground'].items():
        for index,record in enumerate(ground['references']):
            for polygon in _positive_polygons(shape(record['finite_roi_EN'])):
                for triangle in constrained_delaunay_triangles(polygon).geoms:
                    points=[(x,y,_source_height(record,x,y)) for x,y in list(triangle.exterior.coords)[:3]]
                    add(record,points,deck,f'ground-{deck}-{index}')
    return result


def native_vehicle_reference_faces(*,variant='original'):
    """Original finite roofs for approach chords and endpoint-width wedges only.

    These faces cannot supply an authored floor or enter the custom road's
    closed-skin proof. Every patch remains bounded by an original finite
    indexed parent and an explicitly measured2.5m vehicle-strip ROI.
    """
    from shapely import constrained_delaunay_triangles
    from shapely.geometry import shape
    result=[]
    for index,source in enumerate(collar_source_inputs()['variants'][variant]['native_vehicle_roof_crops']):
        for polygon in _positive_polygons(shape(source['finite_roi_EN'])):
            for triangle in constrained_delaunay_triangles(polygon).geoms:
                points=tuple((e,n,_source_height(source,e,n)) for e,n in list(triangle.exterior.coords)[:3])
                if _area(points)==0.:
                    continue
                if _normal(points)[2]<0.:
                    points=points[0],points[2],points[1]
                result.append({'role':f'native-vehicle-roof-{source["component"]}-{index}',
                    'points':points,'uv':tuple(_source_attributes(source,p) for p in points),
                    'texture':source['source_texture_ids'][0],
                    'source_parent_ENHUV_sha256':source['source_parent_ENHUV_sha256'],
                    'source_model_sha256':source['source_model_sha256'],'source':source,
                    'native_reference':True,'native_vehicle_reference':True,'kind':'pavement',
                    'deck':source['component'],'upward':True,'downward':False,'area':_area(points)})
    return result


def check_literal_ground_sources(faces,*,variant='original'):
    """Certify every saved ground fragment against its finite original crop."""
    from shapely.geometry import shape,box,Polygon
    from shapely.ops import unary_union
    from . import diagonal_transition_native as native
    data=collar_source_inputs()['variants'][variant]
    reserved={tuple(socket.helper[2]) for socket in native.socket_specs(variant)}
    expected={}
    total_outside=0.
    for deck,ground in data['ground'].items():
        for record in ground['literal_source_fragments']:
            crops={tuple(crop['host_city_cell']):shape(crop['finite_roi_EN'])
                for crop in record['owned_city_crops']}
            outside=shape(record['outside_owned_roi_EN'])
            if outside.area:
                allowed=unary_union([box(16*c-8,-16*r-8,16*c+8,-16*r+8) for c,r in reserved])
                require(outside.difference(allowed).area==0.,
                    'Original ground fragment projects into an unowned free cell')
                host=tuple(record['source_world_cell'])
                require(host in {tuple(p) for p in data['world_cells']},
                    'Ground literal overhang has no actual owned original host')
                crops[host]=unary_union([crops.get(host,Polygon()),outside])
                total_outside+=outside.area
            for host,region in crops.items():
                role=(f'native-ground-literal-{deck}-{record["native_tile_id"]}-'
                    f'{record["mesh_index"]}-{record["face_index"]}-host-{host[0]}-{host[1]}')
                require(role not in expected,'Independent finite ground role is ambiguous')
                expected[role]=(record,region,host)
    children=defaultdict(list)
    count=0
    for face in faces:
        if not face['role'].startswith('native-ground-literal-'):
            continue
        require(face['role'] in expected,'Saved literal ground face changes its original parent or city host')
        source,region,host=expected[face['role']]
        require(tuple(face['cell'])==host,'Saved literal source fragment is stored in an unreviewed city host')
        require(_material_fingerprint(face,source)==source['source_material_sha256']
                and face['texture'] in source['source_texture_ids'],
            'Saved literal source fragment changes its native material or texture')
        plane=source['source_surface_plane_ENH']
        normal=plane['normal']
        phase=max(abs(_dot(p,normal)-plane['constant']) for p in face['points'])
        require(phase<=POSITION_EPS and _dot(_normal(face['points']),normal)>0.,
            'Saved literal source fragment changes its original finite plane or winding')
        require(all(math.dist(t,_source_attributes(source,p))<=UV_EPS
            for p,t in zip(face['points'],face['uv'])),
            'Saved literal ground source changes its original affine UV phase')
        # Ground originals are horizontal; reserve any actual vertical
        # displacement before testing a conservative finite plan capsule.
        require(abs(abs(normal[2])-1.)<1e-12,'Reviewed native ground parent is unexpectedly tilted')
        radius=math.sqrt(max(0.,POSITION_EPS**2-phase**2))
        polygon=Polygon([p[:2] for p in face['points']])
        require(polygon.area>0. and polygon.difference(region.buffer(radius,quad_segs=32)).area==0.,
            'Saved literal ground face leaves its finite original-parent crop')
        children[face['role']].append(face)
        count+=1
    for role,(source,region,host) in expected.items():
        require(role in children,'Saved ground collar omits an entire finite original source fragment')
        masks=[]
        normal=source['source_surface_plane_ENH']['normal']
        for face in children[role]:
            phase=max(abs(_dot(p,normal)-source['source_surface_plane_ENH']['constant'])
                for p in face['points'])
            radius=math.sqrt(max(0.,POSITION_EPS**2-phase**2))
            masks.append(Polygon([p[:2] for p in face['points']]).buffer(radius,quad_segs=32))
        require(region.difference(unary_union(masks)).area==0.,
            'Saved literal ground collar omits finite source-parent coverage')
    return {'passed':True,'saved_literal_source_triangles_checked':count,
        'independent_source_parent_host_regions_checked':len(expected),
        'literal_source_only_reserved_overhang_plan_area_m2':total_outside,
        'free_owned_cells_recut':True,'material_uv_winding_and_finite_roi_checked':True,
        'complete_donor_mesh_distributed':False,'authored_overhang_allowed':False}


def _clip_source_polygon(points,axis,bound,sign=1.):
    if not points:
        return []
    result=[];previous=points[-1];before=sign*(previous[axis]-bound)
    for current in points:
        after=sign*(current[axis]-bound)
        if (before>=0.)!=(after>=0.):
            t=before/(before-after)
            result.append(tuple(a+t*(b-a) for a,b in zip(previous,current)))
        if after>=0.:
            result.append(tuple(current))
        previous,before=current,after
    return result


def native_dd_profile_surfaces(*,variant='original',visible=True):
    """Reconstruct finite DD source-plane continuations and their visible union."""
    from shapely.geometry import Polygon
    from shapely import constrained_delaunay_triangles
    data=collar_source_inputs()['variants'][variant]
    regions=native_collar_regions(variant)
    result=[]
    roof={(row['deck'],row['native_owner_kind']):row['source_edge_ENHUV'][0][2]
        for row in data['DD_profiles'] if row['role']=='pavement'}
    def emit(points,source):
        points=tuple(tuple(p[:3]) for p in points)
        if _area(points)==0.:
            return
        if _dot(_normal(points),source['source_surface_plane_ENH']['normal'])<0.:
            points=points[0],points[2],points[1]
        result.append({'role':f'raw-dd-{source["deck"]}-{source["role"]}',
            'points':points,'uv':tuple(_source_attributes(source,p) for p in points),
            'texture':source['source_texture_ids'][0],
            'material_sha256':source['source_material_sha256'],'source_record':source})
    for index,source in enumerate(data['DD_profiles']):
        a,b=source['source_edge_ENHUV'];x,y=source['inner_edge_ENH']
        quad=(a[:3],b[:3],y,x)
        if source['role']=='pavement' and visible:
            shape=next(row['geometry'] for row in regions[source['deck']]['visible_pavement']
                if row['index']==index)
            for selected in ((0,1,2),(0,2,3)):
                triangle=[quad[i] for i in selected]
                allowed=shape.intersection(Polygon([p[:2] for p in triangle]))
                for polygon in _positive_polygons(allowed):
                    for child in constrained_delaunay_triangles(polygon).geoms:
                        emit([(e,n,_source_height(source,e,n))
                            for e,n in list(child.exterior.coords)[:3]],source)
        else:
            for selected in ((0,1,2),(0,2,3)):
                triangle=[quad[i] for i in selected]
                if source['role']=='body':
                    triangle=_clip_source_polygon(triangle,2,roof[source['deck'],source['native_owner_kind']])
                for c,r in data['world_cells']:
                    points=triangle
                    for axis,bound,sign in ((0,16*c-8,1.),(0,16*c+8,-1.),
                            (1,-16*r-8,1.),(1,-16*r+8,-1.)):
                        points=_clip_source_polygon(points,axis,bound,sign)
                    for at in range(1,len(points)-1):
                        emit((points[0],points[at],points[at+1]),source)
    return result


def check_dd_profile_surfaces(faces,*,variant='original',bridge_proof=None):
    from shapely.geometry import Polygon
    from shapely.ops import unary_union
    expected=native_dd_profile_surfaces(variant=variant)
    raw=native_dd_profile_surfaces(variant=variant,visible=False)
    grouped={}
    for face in raw:
        source=face['source_record'];key=source['source_parent_ENHUV_sha256']
        if key not in grouped:
            origin=face['points'][0]
            n=source['source_surface_plane_ENH']['normal']
            # An extremely short city-cut edge is not a stable plane basis.
            # Use the independently measured original longitudinal edge,
            # then make the numeric basis explicitly orthonormal.
            edge=source['source_longitudinal_unit_ENH']
            edge=tuple(edge[i]-_dot(edge,n)*n[i] for i in range(3))
            length=math.sqrt(_dot(edge,edge))
            u=tuple(value/length for value in edge);v=_cross(n,u)
            length=math.sqrt(_dot(v,v));v=tuple(value/length for value in v)
            grouped[key]={'source':source,'origin':origin,'u':u,'v':v,'raw':[],
                'expected':[],'actual':[],'maximum_uv_error':0.}
        group=grouped[key]
        project=lambda p:(_dot(_sub(p,group['origin']),group['u']),_dot(_sub(p,group['origin']),group['v']))
        group['raw'].append(Polygon([project(p) for p in face['points']]))
    for face in expected:
        key=face['source_record']['source_parent_ENHUV_sha256'];group=grouped[key]
        group['expected'].append(Polygon([(_dot(_sub(p,group['origin']),group['u']),
            _dot(_sub(p,group['origin']),group['v'])) for p in face['points']]))
    for group in grouped.values():
        group['raw']=unary_union(group['raw']);group['expected']=unary_union(group['expected'])
    count=0;outside_visible=0.
    for face in faces:
        if '-native-profile-loft-' not in face['role']:
            continue
        parts=face['role'].split('-')
        require(parts[0]=='dd' and parts[1] in ('upper','lower')
            and parts[2] in ('pavement','body','barrier'),
            'Saved DD source continuation uses an unreviewed surface role')
        choices=[]
        for key,group in grouped.items():
            source=group['source']
            if (source['deck']!=parts[1] or source['role']!=parts[2]
                    or _material_fingerprint(face,source)!=source['source_material_sha256']):
                continue
            n=source['source_surface_plane_ENH']['normal']
            if _dot(_normal(face['points']),n)<=0.:
                continue
            phase=max(abs(_dot(p,n)-source['source_surface_plane_ENH']['constant']) for p in face['points'])
            error=max(math.dist(t,_source_attributes(source,p)) for p,t in zip(face['points'],face['uv']))
            if phase>POSITION_EPS or error>UV_EPS:
                continue
            polygon=Polygon([(_dot(_sub(p,group['origin']),group['u']),
                _dot(_sub(p,group['origin']),group['v'])) for p in face['points']])
            radius=math.sqrt(max(0.,POSITION_EPS**2-phase**2))
            if polygon.area>0. and polygon.difference(group['raw'].buffer(radius,quad_segs=32)).area==0.:
                choices.append((phase+error,key,polygon,radius,error))
        require(choices,'Saved DD profile changes its finite original continuation, material, UV, or winding; '
            f'role={face["role"]}, points={face["points"]}')
        _error,key,polygon,radius,error=min(choices,key=lambda row:row[0])
        group=grouped[key]
        group['actual'].append(polygon.buffer(radius,quad_segs=32))
        group['maximum_uv_error']=max(group['maximum_uv_error'],error)
        outside_visible+=polygon.difference(group['expected']).area
        count+=1
    occluded=[]
    for group in grouped.values():
        missing=group['expected'].difference(unary_union(group['actual']))
        if missing.area>0. and group['source']['role']=='pavement':
            if bridge_proof is None:
                atlas_ids={f['texture'] for f in faces if f['role'] in ('upper-pavement-atlas','lower-pavement-atlas')}
                require(len(atlas_ids)==1,'Expected C-rail interior requires one actual certified bridge atlas')
                bridge_proof=check_dd_bridge_surfaces(faces,next(iter(atlas_ids)),variant=variant)
            require(bridge_proof.get('passed') is True,'Expected rail enclosure lacks independent complete bridge fields')
            proof=_expected_C_rail_enclosure(group,missing,faces)
            if proof is not None:
                occluded.append(proof)
                continue
        require(missing.area==0.,
            'Saved DD profile omits a finite visible native-source continuation; '
            f'source={group["source"]["native_tile_id"]}, deck={group["source"]["deck"]}, '
            f'kind={group["source"]["role"]}, face={group["source"]["face_index"]}, '
            f'missing_area_m2={missing.area}, plane_bounds={missing.bounds}, children={len(group["actual"])}')
    return {'passed':True,'saved_finite_profile_triangles_checked':count,
        'independent_native_parent_regions_checked':len(grouped),
        'maximum_source_affine_uv_error':max(group['maximum_uv_error'] for group in grouped.values()),
        'raw_source_membership_beyond_exact_partition_area_m2':outside_visible,
        'raw_contact_and_closed_shell_checks_still_required':True,
        'expected_only_integral_C_rail_interiors':occluded,
        'position_euclidean_bound_m':POSITION_EPS,'UV_euclidean_bound':UV_EPS,
        'original_parent_material_plane_uv_winding_and_roi_checked':True}


def _exact_convex_cover(vertices,candidates,base_height,*,above):
    """Exact rational finite triangular cover and affine height separation."""
    from fractions import Fraction as F
    def signed_area(points):
        return sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(points,(*points[1:],points[0])))
    def side(p,a,b):
        return (b[0]-a[0])*(p[1]-a[1])-(b[1]-a[1])*(p[0]-a[0])
    def clip(points,a,b,sign):
        result=[];previous=points[-1];before=sign*side(previous,a,b)
        for current in points:
            after=sign*side(current,a,b)
            if (before>=0)!=(after>=0):
                t=before/(before-after);result.append(tuple(x+t*(y-x) for x,y in zip(previous,current)))
            if after>=0:result.append(current)
            previous,before=current,after
        clean=[]
        for p in result:
            if not clean or p!=clean[-1]:clean.append(p)
        if len(clean)>1 and clean[0]==clean[-1]:clean.pop()
        return clean
    def height(face,p):
        a,b,c=[tuple(F(v) for v in q) for q in face['points']]
        n=_cross(_sub(b,a),_sub(c,a))
        require(n[2]!=0,'Finite source rail/floor proof requires an actual nonvertical triangle')
        return a[2]-(n[0]*(p[0]-a[0])+n[1]*(p[1]-a[1]))/n[2]
    west,east=min(p[0] for p in vertices),max(p[0] for p in vertices)
    south,north=min(p[1] for p in vertices),max(p[1] for p in vertices)
    selected=[]
    for index,face in enumerate(candidates):
        points=[tuple(F(v) for v in p[:2]) for p in face['points']]
        if (max(p[0] for p in points)<west or min(p[0] for p in points)>east
                or max(p[1] for p in points)<south or min(p[1] for p in points)>north):
            continue
        if signed_area(points)<0:points.reverse()
        selected.append((index,points))
    if not selected:
        return None
    # A convex hull is conservative for an imported polygon with redundant
    # or slightly nonconvex overlay vertices: prove the larger closed set.
    ordered=sorted(set(vertices))
    lower=[];upper=[]
    for p in ordered:
        while len(lower)>=2 and side(p,lower[-2],lower[-1])<=0:lower.pop()
        lower.append(p)
    for p in reversed(ordered):
        while len(upper)>=2 and side(p,upper[-2],upper[-1])<=0:upper.pop()
        upper.append(p)
    hull=lower[:-1]+upper[:-1]
    if len(hull)<3 or signed_area(hull)==0:
        return None
    cells=[hull]
    for index,triangle in selected:
        for a,b in zip(triangle,(*triangle[1:],triangle[0])):
            updated=[]
            for cell in cells:
                values=[side(p,a,b) for p in cell]
                if min(values)<0<max(values):
                    halves=[clip(cell,a,b,sign) for sign in (1,-1)]
                    updated.extend(p for p in halves if len(p)>=3 and signed_area(p)!=0)
                else:updated.append(cell)
            cells=updated
    minimum=None;chosen=set()
    for cell in cells:
        valid=[]
        for index,triangle in selected:
            if not all(side(p,a,b)>=0 for p in cell for a,b in zip(triangle,(*triangle[1:],triangle[0]))):
                continue
            gaps=[height(candidates[index],p)-base_height if above else base_height-height(candidates[index],p) for p in cell]
            if min(gaps)>F(POSITION_EPS):
                valid.append((min(gaps),index))
        if not valid:
            return None
        gap,index=max(valid)
        minimum=gap if minimum is None else min(minimum,gap);chosen.add(index)
    return {'exact_closed_convex_cells_checked':len(cells),'minimum_vertical_separation_m':float(minimum),
        'actual_saved_triangle_roles':sorted({candidates[i]['role'] for i in chosen}),
        'unbuffered_finite_plan_coverage':True,'arithmetic':'exact rational values of original binary floats'}


def _expected_C_rail_enclosure(group,missing,faces):
    """Only an expected exterior-pave terminal fringe may be interior to rails.

    The independently certified actual bridge roof and authored floor must
    enclose EVERY exact lifted point. No actual/source face is modified, and
    no missing asphalt elsewhere can use a barrier as a replacement surface.
    """
    from fractions import Fraction as F
    source=group['source'];deck=source['deck']
    require(abs(abs(source['source_surface_plane_ENH']['normal'][2])-1.)<1e-12,
        'Expected native pavement terminal plane is not horizontal')
    roofs=[f for f in faces if f['role'].startswith(f'dd-{deck}-barrier-bridge-') and _normal(f['points'])[2]>0.]
    floors=[f for f in faces if (f['role'].startswith(f'dd-{deck}-body-bridge-underside')
        or f['role'].startswith(f'dd-{deck}-body-authored-DD-underside-')) and _normal(f['points'])[2]<0.]
    records=[]
    for region in _positive_polygons(missing):
        points=[tuple(F(group['origin'][i])+F(x)*F(group['u'][i])+F(y)*F(group['v'][i])
            for i in range(3)) for x,y in list(region.exterior.coords)[:-1]]
        if not points or max(abs(_dot(_sub(tuple(float(v) for v in p[:2]),contract.J),contract.LONGITUDINAL)
                -contract.FLAT_ENVELOPE) for p in points)>1e-11:
            return None
        roof=_exact_convex_cover([p[:2] for p in points],roofs,F(source['source_surface_plane_ENH']['constant']),above=True)
        floor=_exact_convex_cover([p[:2] for p in points],floors,F(source['source_surface_plane_ENH']['constant']),above=False)
        if roof is None or floor is None:
            return None
        records.append({'expected_source_plane_region':region.__geo_interface__,'actual_integral_rail_roof':roof,
            'actual_authored_floor':floor,'expected_fragment_source_parent_sha256':source['source_parent_ENHUV_sha256']})
    return {'stage':'expected_exterior_partition_only','exact_terminal_regions':records,
        'actual_authored_faces_removed':0,'actual_source_faces_removed':0,'area_or_buffer_allowance':False,
        'independent_complete_bridge_fields_required':True,'closed_positive_depth_body_still_required':True}


def check_dd_bridge_surfaces(faces,atlas_id,*,variant='original'):
    expected,floors=dd_bridge_surface_contract(atlas_id,variant=variant)
    actual=[]
    for face in faces:
        if not face['role'].startswith('dd-') or '-bridge-' not in face['role']:
            continue
        parts=face['role'].split('-')
        actual.append({**face,'role':f'dd-bridge-{parts[1]}-{parts[2]}'})
    return {'passed':True,'complete_finite_bridge_fields':check_symmetric_mesh_fields(actual,expected),
        'independent_authored_floor_triangles':len(floors),
        'native_full_width_start_and_middle_finish_checked':True}


def check_symmetric_mesh_fields(actual,expected):
    """Prove both finite XYZUV mesh directions without assigning one parent.

    Each saved face must be covered by reviewed finite source faces, and each
    complete reviewed source face must be covered by actual saved faces. A
    different legal transverse cut cannot steal coverage from its neighbour.
    The coupled3D and UV witnesses remain one finite triangle per convex
    analysis patch; all actual physical contact checks remain mandatory.
    """
    expected=tuple(expected);actual=tuple(actual)
    def keys(face):
        x0,x1=(math.floor((op(p[0] for p in face['points'])+sgn*POSITION_EPS)/2.)
            for op,sgn in ((min,-1),(max,1)))
        y0,y1=(math.floor((op(p[1] for p in face['points'])+sgn*POSITION_EPS)/2.)
            for op,sgn in ((min,-1),(max,1)))
        return [(face['role'],face['texture'],x,y) for x in range(x0,x1+1) for y in range(y0,y1+1)]
    expected_index=defaultdict(set);actual_index=defaultdict(set)
    for i,face in enumerate(expected):
        for key in keys(face):expected_index[key].add(i)
    for i,face in enumerate(actual):
        require(_area(face['points'])>0.,'Saved finite mesh contains a zero-area triangle')
        for key in keys(face):actual_index[key].add(i)
    def overlap_bbox(a,b):
        return all(min(p[axis] for p in a['points'])<=max(p[axis] for p in b['points'])+POSITION_EPS
            and max(p[axis] for p in a['points'])>=min(p[axis] for p in b['points'])-POSITION_EPS
            for axis in range(3))
    patch_counts={'forward':0,'reverse':0}
    for direction,targets,parents,index in (
            ('forward',actual,expected,expected_index),('reverse',expected,actual,actual_index)):
        for target in targets:
            ids=set()
            for key in keys(target):ids.update(index.get(key,()))
            candidates=[]
            for i in ids:
                parent=parents[i]
                if not overlap_bbox(target,parent) or _dot(_normal(target['points']),_normal(parent['points']))<=0.:
                    continue
                wanted=parent if direction=='forward' else target
                saved=target if direction=='forward' else parent
                if _material_fingerprint(saved,wanted)!=wanted['material_sha256']:
                    continue
                candidates.append((i,parent))
            require(candidates,'Finite diagonal bridge has no matching material, source, or winding')
            if any(all(_field_weights(p,t,parent) is not None for p,t in zip(target['points'],target['uv']))
                    for i,parent in candidates):
                continue
            pieces=_piecewise_source_faces(target,candidates,material_checked=True)
            require(pieces is not None,'Finite diagonal bridge mesh loses coupled source XYZ/UV coverage; '
                f'direction={direction}, role={target["role"]}, points={target["points"]}')
            patch_counts[direction]+=len(pieces)
    # Duplicate detection is performed on ORIGINAL SAVED finite triangles,
    # never overlaps of projected source-analysis witnesses.
    from shapely.geometry import Polygon
    from shapely.strtree import STRtree
    from .y_junction_models_verify import _finite_edge_contact_region
    boxes=[Polygon([p[:2] for p in f['points']]).envelope for f in actual]
    tree=STRtree(boxes);contacts=0
    for i,face in enumerate(actual):
        first=face['points'];n=_normal(first);length=math.sqrt(_dot(n,n));n=tuple(v/length for v in n)
        edge=max((_sub(b,a) for a,b in zip(first,(*first[1:],first[0]))),key=lambda e:_dot(e,e))
        length=math.sqrt(_dot(edge,edge));u=tuple(v/length for v in edge);v=_cross(n,u)
        project=lambda p:(_dot(_sub(p,first[0]),u),_dot(_sub(p,first[0]),v))
        for j in tree.query(boxes[i],predicate='intersects'):
            j=int(j)
            if j<=i or actual[j]['role']!=face['role'] or actual[j]['texture']!=face['texture']:
                continue
            second=actual[j]['points']
            if max(abs(_dot(_sub(p,first[0]),n)) for p in second)>POSITION_EPS:
                continue
            overlap=Polygon([project(p) for p in first]).intersection(Polygon([project(p) for p in second]))
            if overlap.area==0.:
                continue
            for region in _positive_polygons(overlap):
                vertices=[tuple(first[0][axis]+x*u[axis]+y*v[axis] for axis in range(3))
                    for x,y in list(region.convex_hull.exterior.coords)[:-1]]
                require(finite_edge_contact(vertices,first,second)
                    or _finite_edge_contact_region(vertices,first,second),
                    'Two original saved diagonal bridge triangles duplicate a finite interior region; '
                    f'first={first}, second={second}')
                contacts+=1
    return {'passed':True,'saved_original_triangles_checked':len(actual),
        'complete_reviewed_source_triangles_checked':len(expected),'finite_patch_counts':patch_counts,
        'original_saved_edge_contacts_checked':contacts,'position_euclidean_bound_m':POSITION_EPS,
        'UV_euclidean_bound':UV_EPS,'analysis_patch_overlap_not_treated_as_a_DAT_duplicate':True,
        'raw_full_physical_overlap_checks_still_required':True}


def check_dd_flat_floor(faces,*,variant='original'):
    """Prove the full real nominal collar floor, including every shoulder."""
    from shapely.geometry import Polygon
    from shapely.ops import unary_union
    results={}
    for deck,regions in native_collar_regions(variant).items():
        height=14. if deck=='upper' else 6.5
        selected=[f for f in faces if f['role'].startswith(f'dd-{deck}-body-authored-DD-underside-')]
        require(selected,'Saved DD collar omits its actual authored full-width floor')
        masks=[];actual_polygons=[]
        for face in selected:
            require(_normal(face['points'])[2]<0. and face['texture']==0x5EB4BEEE
                and _material_fingerprint(face,{})==BODY_MATERIAL_SHA256,
                'Saved DD collar floor changes its winding, material, or texture')
            phase=max(abs(p[2]-height) for p in face['points'])
            require(phase<=POSITION_EPS and all(math.dist(uv,(p[0]/8.,p[1]/8.))<=UV_EPS
                for p,uv in zip(face['points'],face['uv'])),
                'Saved DD collar floor changes its independently declared height or UV field')
            polygon=Polygon([p[:2] for p in face['points']])
            radius=math.sqrt(max(0.,POSITION_EPS**2-phase**2))
            require(polygon.area>0. and polygon.difference(regions['base_geometry'].buffer(radius,quad_segs=32)).area==0.,
                'Saved DD collar floor leaves its independently measured finite native roof union')
            masks.append(polygon.buffer(radius,quad_segs=32));actual_polygons.append(polygon)
        require(regions['base_geometry'].difference(unary_union(masks)).area==0.,
            'Saved DD collar floor has a finite missing shoulder or inner-ring patch')
        results[deck]={'saved_authored_floor_triangles':len(selected),'nominal_floor_height_m':height,
            'full_native_roof_plan_area_m2':regions['base_geometry'].area,
            'actual_authored_floor_plan_area_m2':unary_union(actual_polygons).area}
    return {'passed':True,'decks':results,'full_shoulders_checked':True,'borrowed_native_floor_faces':0,
        'position_euclidean_bound_m':POSITION_EPS}


def check_dd_authored_body_fields(faces,*,variant='original'):
    """Bind new flat closing faces to the declared concrete field and bounds."""
    from shapely.geometry import Polygon,LineString
    allowed=('underside','exposed-wall','floor-phase-step','roof-phase-step',
        'inner-rail-foot-phase-shim','native-reference-inner-foot-lip')
    roofs=defaultdict(list)
    for face in native_dd_profile_surfaces(variant=variant):
        if face['source_record']['role'] in ('pavement','barrier') and _normal(face['points'])[2]>0.:
            roofs[face['source_record']['deck']].append(face['points'])
    for face in native_reference_faces(variant=variant):
        if face['kind'] in ('pavement','barrier') and face['upward']:
            roofs[face['deck']].append(face['points'])
    count=0;maximum=0.
    for face in faces:
        if '-body-authored-DD-' not in face['role']:
            continue
        deck=face['role'].split('-')[1]
        kind=face['role'].split('-body-authored-DD-',1)[1].rsplit('-',1)[0]
        require(kind in allowed,'Saved DD collar contains an unreviewed authored closing role')
        require(face['texture']==0x5EB4BEEE and _material_fingerprint(face,{})==BODY_MATERIAL_SHA256
            and all(math.dist(uv,(p[0]/8.,p[1]/8.))<=UV_EPS
                for p,uv in zip(face['points'],face['uv'])),
            'Saved DD closing face changes its declared concrete material or affine UV')
        nominal=15. if deck=='upper' else 7.5
        floor=nominal-1.
        require(min(p[2] for p in face['points'])>=floor-POSITION_EPS,
            'Saved flat DD body falls below its independently declared nominal floor')
        if kind=='exposed-wall':
            region=native_collar_regions(variant)[deck]['base_geometry']
            polygon=Polygon([p[:2] for p in face['points']])
            if polygon.area==0.:
                polygon=LineString([p[:2] for p in face['points']]).convex_hull
            outside=polygon.difference(region.boundary.buffer(POSITION_EPS,quad_segs=32))
            require(outside.area==0. and outside.length==0.,
                'Saved DD outer wall leaves the finite measured pavement perimeter')
            for point in face['points']:
                possible=[tri for tri in roofs[deck] if all(min(p[i] for p in tri)-POSITION_EPS<=point[i]
                    <=max(p[i] for p in tri)+POSITION_EPS for i in (0,1))]
                distance=min((_point_triangular_slab_distance(point,tri,floor) for tri in possible),default=math.inf)
                require(distance<=POSITION_EPS,
                    'Saved DD outer wall exceeds the exact finite source integral roof/floor envelope')
                maximum=max(maximum,distance)
        elif kind!='underside':
            require(min(p[2] for p in face['points'])>=nominal-POSITION_EPS
                and max(p[2] for p in face['points'])<=nominal+DATUM[deck]+POSITION_EPS,
                'A DD phase or foot closure extends below its finite source roof interval')
        count+=1
    return {'passed':True,'saved_authored_closing_triangles_checked':count,
        'finite_nominal_floor_native_foot_heights_checked':True,
        'exposed_walls_bound_to_measured_exterior_perimeter':True,
        'outer_wall_maximum_finite_source_slab_distance_m':maximum,
        'arbitrary_crown_height_substituted':False,'authored_faces_removed_from_analysis':0}


def _point_triangular_slab_distance(point,roof,floor):
    """True finite Euclidean distance to a triangular sloped-roof solid.

    This is a source-measured roof, a nominal floor, and three finite vertical
    trapezoids. An exterior corner cannot spend4µm separately in XY and H.
    """
    a,b,c=roof
    determinant=(b[1]-c[1])*(a[0]-c[0])+(c[0]-b[0])*(a[1]-c[1])
    require(determinant!=0.,'Source roof prism requires a nonzero finite plan triangle')
    u=((b[1]-c[1])*(point[0]-c[0])+(c[0]-b[0])*(point[1]-c[1]))/determinant
    v=((c[1]-a[1])*(point[0]-c[0])+(a[0]-c[0])*(point[1]-c[1]))/determinant
    h=u*a[2]+v*b[2]+(1.-u-v)*c[2]
    if u>=0. and v>=0. and u+v<=1. and floor<=point[2]<=h:
        return 0.
    bottom=tuple((p[0],p[1],floor) for p in roof)
    triangles=[tuple(roof),bottom]
    for i in range(3):
        j=(i+1)%3
        triangles.extend(((bottom[i],bottom[j],roof[j]),(bottom[i],roof[j],roof[i])))
    return min(_point_triangle_distance(point,tri) for tri in triangles)


def native_union_skin(faces,*,variant='original',_diagnostic_proposal=False):
    """Compose a source-pinned intrinsic native union over actual new floors.

    Only independently certified original helper/peer references are trimmed
    by the native-union step. The separate positive-depth derivative omits
    exactly-H0 pavement/rail sheets; every actual DAT face remains in the raw
    interference, floor, and car inputs. Source facts alone do not approve it.
    """
    from shapely.geometry import Polygon,LineString
    from shapely.ops import unary_union
    from shapely import constrained_delaunay_triangles
    require(NATIVE_SKIN_SCOPE_REVIEWED or _diagnostic_proposal,
        'Fresh diagonal intrinsic native-union scope is not yet reviewed')
    floor_proof=check_dd_flat_floor(faces,variant=variant)
    references=native_reference_faces(variant=variant)
    floors={deck:unary_union([Polygon([p[:2] for p in f['points']]) for f in faces
        if f['role'].startswith(f'dd-{deck}-body-authored-DD-underside-')]) for deck in ('upper','lower')}
    roof_by_owner={}
    barriers_by_owner=defaultdict(list)
    for face in references:
        source=face['source']
        key=(face['deck'],source['native_tile_id'],source['pose'],tuple(source['source_world_cell']))
        if face['kind']=='pavement':
            roof_by_owner.setdefault(key,[]).append(Polygon([p[:2] for p in face['points']]))
        elif face['kind']=='barrier':
            polygon=Polygon([p[:2] for p in face['points']])
            if polygon.area>0.:
                barriers_by_owner[key].append(polygon)
    roof_by_owner={key:unary_union(values) for key,values in roof_by_owner.items()}
    trimmed_body=[];trimmed_roof=[];kept=[]
    body_area=0.;roof_area=0.
    for index,face in enumerate(references):
        source=face['source'];deck=face['deck']
        key=(deck,source['native_tile_id'],source['pose'],tuple(source['source_world_cell']))
        nominal=15. if deck=='upper' else 7.5
        level=nominal+(DATUM[deck] if source['native_tile_id']=='57530900' else 0.)
        if face['kind']=='body':
            vertices=[(*p,*uv) for p,uv in zip(face['points'],face['uv'])]
            below=_clip_source_polygon(vertices,2,level,-1.)
            if _area(below)>0.:
                footprint=Polygon([p[:2] for p in below])
                if footprint.area==0.:
                    footprint=LineString([p[:2] for p in below]).convex_hull
                require(min(p[2] for p in below)>(14. if deck=='upper' else 6.5)+POSITION_EPS,
                    'Original native wall falls below or touches the actual new floor')
                missing=footprint.difference(floors[deck].buffer(POSITION_EPS,quad_segs=32))
                require(missing.area==0. and missing.length==0.,
                    'A removed original native wall lacks actual authored floor under its entire footprint')
                missing=footprint.difference(roof_by_owner.get(key,Polygon()).buffer(POSITION_EPS,quad_segs=32))
                require(missing.area==0. and missing.length==0.,
                    'Original native wall lacks its own finite source roof coverage')
                body_area+=_area(below)
                trimmed_body.append({'reference_face_index':index,'source_parent_ENHUV_sha256':
                    source['source_parent_ENHUV_sha256'],'native_tile_id':source['native_tile_id'],
                    'pose':source['pose'],'source_world_cell':source['source_world_cell'],
                    'deck':deck,'finite_removed_polygon_ENH':[p[:3] for p in below],
                    'removed_area_m2':_area(below),'own_roof_height_m':level,
                    'actual_authored_floor_height_m':14. if deck=='upper' else 6.5})
            above=_clip_source_polygon(vertices,2,level,1.)
            for at in range(1,len(above)-1):
                child=(above[0],above[at],above[at+1])
                if _area(child)>0.:
                    kept.append({**face,'points':tuple(p[:3] for p in child),'uv':tuple(p[3:] for p in child)})
        elif face['kind']=='pavement' and face['role'].startswith('native-reference-dd-'):
            polygon=Polygon([p[:2] for p in face['points']])
            mask=unary_union(barriers_by_owner[key])
            # Intrinsic overlap of two already-rendered native halves uses
            # only the higher pinned original roof, never authored geometry.
            higher=[]
            for other in references:
                if (other['kind']=='pavement' and other['deck']==deck
                        and min(p[2] for p in other['points'])>max(p[2] for p in face['points'])):
                    higher.append(Polygon([p[:2] for p in other['points']]))
            mask=unary_union([mask,*higher])
            removed=polygon.intersection(mask)
            remaining=polygon.difference(mask)
            if removed.area>0.:
                roof_area+=removed.area
                trimmed_roof.append({'reference_face_index':index,'source_parent_ENHUV_sha256':source['source_parent_ENHUV_sha256'],
                    'deck':deck,'native_tile_id':source['native_tile_id'],'pose':source['pose'],
                    'finite_removed_roi_EN':removed.__geo_interface__,'removed_plan_area_m2':removed.area})
            for region in _positive_polygons(remaining):
                for triangle in constrained_delaunay_triangles(region).geoms:
                    points=tuple((e,n,_source_height(source,e,n)) for e,n in list(triangle.exterior.coords)[:3])
                    if _area(points)==0.:
                        continue
                    if _dot(_normal(points),source['source_surface_plane_ENH']['normal'])<0.:
                        points=points[0],points[2],points[1]
                    kept.append({**face,'points':points,'uv':tuple(_source_attributes(source,p) for p in points)})
        else:
            kept.append(face)
    skin,zero=positive_depth_skin([*faces,*kept])
    return skin,{'scope_reviewed':NATIVE_SKIN_SCOPE_REVIEWED,'diagnostic_proposal':_diagnostic_proposal,
        'actual_full_floor_proof':floor_proof,'source_only_body_faces_trimmed':len(trimmed_body),
        'source_only_body_surface_area_removed_m2':body_area,'body_records':trimmed_body,
        'source_only_roof_fragments_trimmed':len(trimmed_roof),'source_only_roof_plan_area_removed_m2':roof_area,
        'roof_records':trimmed_roof,'authored_faces_removed_by_native_union':0,'raw_DAT_faces_changed':0,
        'raised_302_body_strip_above_nominal_retained':True,'zero_ground_sheet_scope':zero,
        'native_vehicle_roof_references_used_in_skin':0}


def positive_depth_skin(faces):
    """Keep actual positive-depth solids; omit only declared zero-ground sheets.

    A downward concrete floor is never removed here. Its finite coverage and
    depth remain mandatory wherever an actual positive-height roof exists.
    """
    selected=[]
    omitted=0
    area=0.
    for face in faces:
        if face['kind'] in ('pavement','barrier') and all(p[2]==0. for p in face['points']):
            omitted+=1
            area+=face.get('area',_area(face['points']))
        else:
            selected.append(face)
    return selected,{'exact_zero_height_sheet_faces':omitted,
        'zero_height_sheet_surface_area_m2':area,'authored_body_floor_faces_removed':0}


def _yellow(pixel):
    red, green, blue, alpha = pixel
    return (red > 125 and green > 105 and blue < 80 and red-blue > 80
            and green-blue > 60 and alpha > 200)


def _sample_image(image, u, v):
    width, height = image.size
    x, y = u*width-.5, v*height-.5
    ix, iy = math.floor(x), math.floor(y)
    fx, fy = x-ix, y-iy
    return tuple(sum(image.getpixel(((ix+a)%width, (iy+b)%height))[channel]
                 *(fx if a else 1.-fx)*(fy if b else 1.-fy)
                 for a, b in ((0, 0), (1, 0), (0, 1), (1, 1))) for channel in range(4))


def reconstruct_atlas(native_images, *, variant='original'):
    """Independent finite-native-owner, repeat-wrapped pixel reconstruction.

    Diagonal native halves have distinct signed station derivatives and UV
    origins. A generic +/-station/16 rule is deliberately not an expectation.
    """
    phase = contract.phase_for_options(variant)
    fields = native_atlas_fields(variant)
    from PIL import Image
    result = Image.new('RGBA', (512, 1024), (0, 0, 0, 0))
    output = result.load()
    for deck, column in (('upper', 8), ('lower', 264)):
        native_height = 15. if deck == 'upper' else 7.5
        for row in range(1024):
            station = (row-127.5)/8.
            height = contract.upper_height(station) if deck == 'upper' else contract.lower_height(station)
            colour = 1.-height/native_height
            alpha = 1.-contract._cubic(height/.25)
            for x in range(-2, 130):
                t = ((x%128)+.5)/128.
                if phase.physical_reflection != phase.traffic_reversed:
                    t = 1.-t
                if deck=='lower':
                    t = 1.-t
                lateral = -8.+16.*t
                pixels=[]
                for kind,iid in (('dd',0x5713000E),('ground',0x5703000E)):
                    field=min(fields[deck][kind],key=lambda r:max(
                        r['lateral_interval_m'][0]-lateral,lateral-r['lateral_interval_m'][1],0.))
                    du=lateral-field['lateral_interval_m'][0]
                    ds=station-field['reference_station_m']
                    uv=tuple(field['UV_at_first_lateral'][i]+du*field['dUV_d_lateral_m'][i]
                        +ds*field['dUV_d_station_m'][i] for i in range(2))
                    pixels.append(_sample_image(native_images[iid],*uv))
                dd,ground=pixels
                output[column+x, row] = tuple(min(255, max(0, round(a+(alpha if i == 3 else colour)*(b-a))))
                                             for i, (a, b) in enumerate(zip(dd, ground)))
    return result.tobytes()


def check_atlas(resources, piece, donors=None):
    from scp.preview import decode_fsh
    phase = contract.phase_for_piece(piece)
    ids = piece.get('authored_texture_ids', ())
    require(len(ids) == 1, 'Diagonal transition needs exactly one owned asphalt atlas')
    key = (*TEXTURE, contract._number(ids[0]))
    require(key in resources, 'Saved diagonal asphalt atlas is absent')
    image = decode_fsh(resources[key]).convert('RGBA')
    require(image.size == (512, 1024), 'Diagonal atlas dimensions differ from the reviewed fields')
    digest = hashlib.sha256(image.tobytes()).hexdigest()
    if donors is None:
        require(phase.key in ATLAS_RGBA_SHA256, 'Independent diagonal atlas source-pixel acceptance is pending')
        expected = ATLAS_RGBA_SHA256[phase.key]
    else:
        source = donors.get('rhw4_textures', donors)
        images = {}
        for iid, pin in NATIVE_TEXTURE_SHA256.items():
            raw = source.get((*TEXTURE, iid))
            require(raw is not None and hashlib.sha256(decompress(raw)).hexdigest() == pin,
                    'Original diagonal asphalt texture source differs')
            images[iid] = decode_fsh(raw).convert('RGBA')
            require(images[iid].size == (128, 128), 'Native asphalt source dimensions differ')
        expected = hashlib.sha256(reconstruct_atlas(images, variant=phase.key)).hexdigest()
    require(digest == expected, 'Saved diagonal atlas differs from independent original source pixels')
    return {'passed': True, 'rgba_sha256': digest, 'pixels_checked': 512*1024,
            'independent_native_pixel_reconstruction': donors is not None,
            'portable_reviewed_pixel_identity': donors is None}


def check_driver_left_markings(faces, journeys, images, pavement_roles,
                               *, fractions=(.01, .25, .5, .75, .99)):
    """Measure yellow from actual saved XYZUV, directed PATHs, and pixels.

    Input images are decoded actual saved atlas/native FSH resources, with
    their source identities checked by the caller. Curve functions, material
    names alone, and an unencoded source texture cannot establish this fact.
    """
    import numpy as np
    from shapely.geometry import LineString, Point, Polygon
    from shapely.strtree import STRtree
    selected = []
    for face in faces:
        components = [c for c, roles in pavement_roles.items() if face['role'] in roles]
        if not components or _normal(face['points'])[2] <= 0.:
            continue
        require(len(components) == 1 and face['texture'] in images,
                'Saved diagonal pavement has ambiguous ownership or missing actual texture pixels')
        vertices = np.array(face['points'])
        fields = np.linalg.solve(np.c_[vertices[:, :2], np.ones(3)],
                                 np.c_[vertices[:, 2], np.array(face['uv'])])
        selected.append((face, fields, Polygon(vertices[:, :2]), components[0]))
    require(selected, 'Saved diagonal model has no measured asphalt texture field')
    tree = STRtree([row[2] for row in selected])
    columns = {}
    for texture, image in images.items():
        width, height = image.size
        columns[texture] = [x for x in range(width)
            if sum(_yellow(image.getpixel((x, y))) for y in range(height)) >= max(8, height//16)]
    checked = []
    for journey in journeys:
        points = np.array(journey['points'])
        runs = np.linalg.norm(np.diff(points[:, :2], axis=0), axis=1)
        require(len(runs) and min(runs) > 0., 'Saved marking journey contains a stationary chord')
        stations = np.r_[0., np.cumsum(runs)]
        for fraction in fractions:
            require(0. < fraction < 1., 'Marking sample must lie inside the actual journey')
            station = fraction*stations[-1]
            at = min(len(runs)-1, int(np.searchsorted(stations, station, side='right')-1))
            t = (station-stations[at])/runs[at]
            point = points[at]+t*(points[at+1]-points[at])
            direction = (points[at+1, :2]-points[at, :2])/runs[at]
            left = np.array((-direction[1], direction[0]))
            hits = []
            for index in tree.query(LineString((point[:2]-9.*left, point[:2]+9.*left))):
                face, field, polygon, component = selected[int(index)]
                if component != journey['component']:
                    continue
                u0 = float(np.array((*point[:2], 1.))@field[:, 1])
                du = float(left@field[:2, 1])
                if abs(du) < 1e-12:
                    continue
                image = images[face['texture']]
                width = image.size[0]
                low, high = sorted((u0-9.*du, u0+9.*du))
                for column in columns[face['texture']]:
                    for repeat in range(math.floor(low)-1, math.ceil(high)+1):
                        offset = ((column+.5)/width+repeat-u0)/du
                        if abs(offset) > 9.:
                            continue
                        xy = point[:2]+offset*left
                        if not polygon.covers(Point(*xy)):
                            continue
                        height, u, v = np.array((*xy, 1.))@field
                        if abs(height-point[2]) <= .03 and _yellow(_sample_image(image, u, v)):
                            hits.append(float(offset))
            require(hits and min(hits) > .05,
                    'Encoded diagonal yellow is absent or not on the driver left')
            checked.append({'journey': journey['id'], 'fraction': fraction,
                            'minimum_driver_left_offset_m': min(hits)})
    return {'passed': True, 'actual_saved_pixel_samples_checked': len(checked),
            'actual_saved_journeys_checked': len(journeys), 'samples': checked,
            'scope': 'Actual encoded XYZUV, directed saved PATH chords, and decoded FSH pixels; game appearance remains unverified.'}


def _clip_height(points, field, minimum):
    """Clip finite XY vertices by one affine field, with consistent signs."""
    if not points:
        return []
    def value(p):
        return field[0]*p[0]+field[1]*p[1]+field[2]-minimum
    result = []
    previous, a = points[-1], value(points[-1])
    for current in points:
        b = value(current)
        if (a >= 0.) != (b >= 0.):
            t = a/(a-b)
            result.append(tuple(previous[i]+t*(current[i]-previous[i]) for i in range(2)))
        if b >= 0.:
            result.append(tuple(current))
        previous, a = current, b
    return result


def check_slab_depth(base_roofs, actual_floors, *, floor_roles=('upper-body', 'lower-body')):
    """Prove full finite floor coverage at max(0,base roof−1m).

    Base roofs are independently reviewed slab planes, including the base
    below integral raised rails. Floors are actual saved authored body faces;
    native references and support soles may not replace a missing slab.
    """
    import numpy as np
    from shapely import constrained_delaunay_triangles
    from shapely.geometry import Polygon
    from shapely.ops import unary_union
    from shapely.strtree import STRtree
    floors = [f for f in actual_floors if _normal(f['points'])[2] < 0.
              and not f.get('native_reference') and f['role'] in floor_roles]
    require(floors, 'Diagonal slab has no actual authored underside faces')
    polygons = [Polygon([p[:2] for p in f['points']]) for f in floors]
    tree = STRtree(polygons)
    def plane(points):
        return np.linalg.solve(np.array([[p[0], p[1], 1.] for p in points]),
                               np.array([p[2] for p in points]))
    fields = [plane(f['points']) for f in floors]
    checked = 0
    maximum_distance = 0.
    for roof in base_roofs:
        require(_normal(roof['points'])[2] > 0., 'Independent slab base roof is not upward')
        if all(p[2] == 0. for p in roof['points']):
            continue
        source = plane(roof['points'])
        ring = [p[:2] for p in roof['points']]
        upper = _clip_height(ring, source, 1.)
        lower = _clip_height(ring, tuple(-v for v in source), -1.)
        for vertices, target in ((upper, (source[0], source[1], source[2]-1.)),
                                 (lower, (0., 0., 0.))):
            if len(vertices) < 3:
                continue
            polygon = Polygon(vertices)
            if polygon.area <= 0.:
                continue
            candidates = [int(i) for i in tree.query(polygon.buffer(POSITION_EPS), predicate='intersects')]
            cover = []
            for index in candidates:
                overlap = polygon.intersection(polygons[index])
                if overlap.area <= 0.:
                    continue
                field = tuple(fields[index][i]-target[i] for i in range(3))
                for region in _positive_polygons(overlap):
                    clipped = _clip_height(list(region.exterior.coords)[:-1], field, -POSITION_EPS)
                    clipped = _clip_height(clipped, tuple(-v for v in field), -POSITION_EPS)
                    if len(clipped) >= 3:
                        part = Polygon(clipped)
                        if part.area > 0.:
                            cover.append(part)
            missing = polygon.difference(unary_union(cover))
            if missing.area > 0.:
                for region in _positive_polygons(missing):
                    def finite_distance(polygon):
                        targets = [(x, y, target[0]*x+target[1]*y+target[2])
                                   for x, y in list(polygon.exterior.coords)[:-1]]
                        return min((max(_point_triangle_distance(p, floors[i]['points']) for p in targets)
                                    for i in candidates), default=math.inf)
                    distance = finite_distance(region)
                    if distance <= POSITION_EPS:
                        maximum_distance = max(maximum_distance, distance)
                        continue
                    targets=[(x,y,target[0]*x+target[1]*y+target[2])
                        for x,y in list(region.exterior.coords)[:-1]]
                    parent=tuple((p[0],p[1],target[0]*p[0]+target[1]*p[1]+target[2])
                        for p in roof['points'])
                    if _finite_triangle_union_covers(targets,parent,
                            [floors[i]['points'] for i in candidates]):
                        continue
                    for patch in constrained_delaunay_triangles(region).geoms:
                        if patch.area <= 0.:
                            continue
                        distance = finite_distance(patch)
                        require(distance <= POSITION_EPS,
                                'Diagonal actual underside does not cover its full one-metre or ground-clamped slab; '
                                f'target_patch={targets}, finite_distance_m={distance}')
                        maximum_distance = max(maximum_distance, distance)
            checked += 1
    return {'passed': True, 'finite_slab_patches_checked': checked,
            'actual_authored_floor_triangles_checked': len(floors),
            'elevated_depth_m': 1., 'ground_clamp_height_m': 0.,
            'maximum_finite_encoding_admission_m': maximum_distance,
            'combined_euclidean_bound_m': POSITION_EPS, 'borrowed_native_floors': 0,
            'unrelated_lower_deck_floor_substitution': False}


def _saved_physical_checks(resources,piece,donors=None,*,source_only=False):
    """One ordered saved-geometry proof for prototypes and normal containers."""
    from . import diagonal_transition_native as native
    from .diagonal_transition_corridors_verify import check_corridors as vehicle_check
    from .y_junction_models_verify import (check_shell,check_barrier_deck_clearance,
        check_barrier_intersections)
    tiles=contract._spec(piece,_source_only=source_only)
    phase=contract.phase_for_piece(piece)
    layout=contract.candidate_layout_for_measurement(phase.key) if source_only else contract.reviewed_layout(phase.key)
    origin=layout['world_origin_cell']
    if 'world_origin_cell' in piece:
        require(tuple(piece['world_origin_cell'])==tuple(origin),'Saved source world origin differs from the independent layout')
    faces=[]
    for cell,tile in zip(piece['cells'],tiles):
        require((*S3D,tile) in resources,'Saved diagonal source model is absent')
        world=tuple(cell[i]+origin[i] for i in range(2))
        faces.extend(decode_faces(resources[*S3D,tile],world))
    faces=classify_faces(faces,variant=phase.key)
    require(all(face['area']>0. for face in faces),'Saved diagonal model contains an exact zero-area indexed triangle')
    require(all(face['upward'] for face in faces if face['kind']=='pavement'),
        'Saved diagonal pavement winding reverses its source-facing direction')
    paths=(contract.check_source_paths if source_only else contract.check_paths)(resources,piece)
    boundaries=contract.check_native_boundaries(donors,piece,resources,_source_only=source_only)
    if donors is not None:
        for key in native.RESOURCE_SHA256:
            native.resource(donors,key)
    atlas=check_atlas(resources,piece,donors)
    atlas_id=contract._number(piece['authored_texture_ids'][0])
    dd_bridge=check_dd_bridge_surfaces(faces,atlas_id,variant=phase.key)
    source_profiles=check_dd_profile_surfaces(faces,variant=phase.key,bridge_proof=dd_bridge)
    inner_ring=check_dd_inner_profiles(faces,variant=phase.key)
    literal_ground=check_literal_ground_sources(faces,variant=phase.key)
    ground_bridge=check_ground_bridge_surfaces(faces,atlas_id,variant=phase.key)
    middle=check_middle_surfaces(faces,atlas_id,variant=phase.key)
    flat_floor=check_dd_flat_floor(faces,variant=phase.key)
    closing_fields=check_dd_authored_body_fields(faces,variant=phase.key)
    supports=check_support_solids(faces,variant=phase.key)
    references=native_reference_faces(variant=phase.key)
    raw=[*faces,*references]
    support_clearance=check_support_opposing_road_clearance(raw,variant=phase.key)
    roof_contacts=check_surface_contacts(raw,variant=phase.key)
    floor_contacts=check_surface_contacts(raw,underside=True)
    barrier_slabs=check_barrier_deck_clearance(raw)
    barrier_contacts=check_barrier_intersections(raw)
    skin,skin_scope=native_union_skin(faces,variant=phase.key)
    closed=check_shell(skin,kind='road',component=False)
    support_shell=check_shell(faces,kind='support',component=False)
    journeys=contract.decoded_journeys(resources,piece,_source_only=source_only)
    journeys=[{**row,'points':[(p[0]+16.*origin[0],p[1]-16.*origin[1],p[2])
        for p in row['points']]} for row in journeys]
    native_routes,native_cells=contract.native_vehicle_routes(donors,variant=phase.key)
    vehicle_references=native_vehicle_reference_faces(variant=phase.key)
    corridors=vehicle_check([*raw,*vehicle_references],journeys,
        owned_cells=layout['world_cells'],native_routes=native_routes,native_cells=native_cells)
    # Completeness of omitted original source obstacles is a separately
    # source-pinned finite clearance certificate, never an inference from
    # vehicle-only roof crops.
    native_obstacles=check_native_obstacle_completeness(resources,piece,donors)
    from scp.preview import decode_fsh
    images={atlas_id:decode_fsh(resources[*TEXTURE,atlas_id]).convert('RGBA')}
    if donors is not None:
        source=donors.get('rhw4_textures',donors)
        images.update({iid:decode_fsh(source[*TEXTURE,iid]).convert('RGBA') for iid in NATIVE_TEXTURE_SHA256})
    marking_roles={deck:{f['role'] for f in faces if f['deck']==deck and f['kind']=='pavement'}
        for deck in ('upper','lower')}
    # Atlas/source pixels were checked independently above; without original
    # images, portable operation samples only the actual owned atlas regions.
    marking_faces=[f for f in faces if f['kind']=='pavement' and f['texture'] in images]
    markings=check_driver_left_markings(marking_faces,journeys,images,marking_roles,
        fractions=(.1,.25,.5,.75,.9))
    return {'passed':True,'complete_physical_acceptance':True,'actual_indexed_triangles_checked':len(faces),
        'indexed_triangles_checked':len(faces),'texture_ids':sorted({face['texture'] for face in faces}),
        'position_euclidean_bound_m':POSITION_EPS,'UV_euclidean_bound':UV_EPS,
        'paths':paths,'native_boundaries':boundaries,'native_original_resources_checked':donors is not None,
        'native_source_profile_fields':source_profiles,'complete_DD_inner_ring':inner_ring,
        'native_to_middle_bridge_fields':dd_bridge,'literal_ground_source_fields':literal_ground,
        'ground_bridge_fields':ground_bridge,'complete_middle_and_full_width_floors':middle,
        'complete_flat_collar_floor':flat_floor,'authored_closing_fields':closing_fields,
        'complete_support_solids':supports,'opposing_road_support_clearance':support_clearance,
        'raw_roof_contacts':roof_contacts,'raw_floor_contacts':floor_contacts,
        'raw_barrier_to_slab_clearance':barrier_slabs,'raw_finite_barrier_contacts':barrier_contacts,
        'intrinsic_original_native_union_scope':skin_scope,'closed_positive_depth_road_skin':closed,
        'closed_support_shells':support_shell,'strict_full_width_vehicle_corridors':corridors,
        'original_native_obstacle_completeness':native_obstacles,'independent_native_atlas':atlas,
        'actual_saved_driver_left_markings':markings,'game_rendering_tested':False,
        'structural_capacity_tested':False}


def check_source_models(resources,piece,donors=None):
    """Actual unallocated prototypes; normal container checks are deferred."""
    result=_saved_physical_checks(resources,piece,donors,source_only=True)
    return {**result,'stage':'encoded-source-physical-verification',
        'normal_DAT_five_zooms_preview_or_shadow_checks_performed':False,
        'permanent_addresses_allocated':False,'installed':False}


def check_models(resources,piece,donors=None):
    """Normal saved DATs add five zooms, preview, shadows, and fresh originals."""
    contract._spec(piece)
    phase=contract.phase_for_piece(piece)
    require(phase.key in REVIEWED_SURFACES,
        'Diagonal finite native/profile/support surface review is pending; model acceptance is closed')
    require(donors is not None,'Normal diagonal native models require audited original source resources')
    for tile in map(contract._number,piece['tile_ids']):
        require(all((*S3D,tile+zoom) in resources for zoom in range(5)),
            'Diagonal saved model zoom is missing')
        raw=decompress(resources[*S3D,tile])
        require(all(decompress(resources[*S3D,tile+zoom])==raw for zoom in range(5)),
            'Diagonal saved zoom changes its complete source geometry')
    result=_saved_physical_checks(resources,piece,donors)
    from .modular_partition_verify import check_preview
    from .shadow_verify import check_resources
    check_preview(resources,piece)
    shadows=check_resources(resources,piece)
    return {**result,'stage':'normal-saved-DAT-physical-verification',
        'all_five_zooms_exact':True,'preview_matches_all_saved_cells':True,**shadows}
