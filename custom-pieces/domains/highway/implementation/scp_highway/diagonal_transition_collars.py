"""Finite first-A DD native profiles and the collar aggregation boundary.

All coordinates in this module are ENHUV. Source-parent continuations are
explicitly distinguished from literal parent fragments and already-rendered
native references. Returned topology gates are evidence, not acceptance.
"""
from __future__ import annotations

from collections import defaultdict
from copy import deepcopy
import math

import numpy as np
from shapely import constrained_delaunay_triangles
from shapely.geometry import Polygon, LineString, Point, box
from shapely.ops import unary_union

from scp.dbpf import require
from . import diagonal_transition_geometry as geometry
from . import diagonal_transition_layout as layout
from . import diagonal_transition_native as native


def _normal(triangle):
    return np.cross(np.subtract(triangle[1][:3], triangle[0][:3]),
                    np.subtract(triangle[2][:3], triangle[0][:3]))


def _clip_plane(points, normal, station, sign=1.):
    """Exact signs and bounded intersections; no fuzzy extrapolation."""
    if not points:
        return []
    result = []
    previous = points[-1]
    before = sign * (np.dot(previous[:3], normal) - station)
    for current in points:
        after = sign * (np.dot(current[:3], normal) - station)
        if (before >= 0.) != (after >= 0.):
            fraction = before / (before - after)
            require(0. <= fraction <= 1., 'Collar clipping extrapolated a source edge')
            point = tuple(a + fraction * (b-a) for a,b in zip(previous,current))
            result.append(point)
        if after >= 0.:
            result.append(current)
        previous, before = current, after
    return result


def _fan(points, desired=None):
    result = []
    for index in range(1, len(points)-1):
        face = (points[0],points[index],points[index+1])
        normal = _normal(face)
        if np.dot(normal,normal) == 0.:
            continue
        if desired is not None and np.dot(normal,desired) < 0.:
            face = (face[0],face[2],face[1])
        result.append(face)
    return result


def _polygons(value):
    if value.geom_type == 'Polygon':
        return [value] if value.area > 0. else []
    if hasattr(value,'geoms'):
        return [p for part in value.geoms for p in _polygons(part)]
    return []


def _plan(group):
    return unary_union([Polygon([p[:2] for p in triangle]) for triangle in group['triangles_ENHUV']
                        if Polygon([p[:2] for p in triangle]).area > 0.])


def _roof_attribute(triangle, east, north):
    matrix=np.array([[p[0],p[1],1.] for p in triangle])
    attributes=np.linalg.solve(matrix,np.array([p[2:] for p in triangle]))
    return (east,north,*(np.array([east,north,1.])@attributes))


def _clip_roof(group, allowed):
    faces=[]
    for triangle in group['triangles_ENHUV']:
        polygon=Polygon([p[:2] for p in triangle])
        if polygon.area==0.:
            continue
        for part in _polygons(polygon.intersection(allowed)):
            for child in constrained_delaunay_triangles(part).geoms:
                points=tuple(_roof_attribute(triangle,*point) for point in list(child.exterior.coords)[:3])
                faces.extend(_fan(points,_normal(triangle)))
    return {**group,'triangles_ENHUV':faces}


def _candidate_hosts(variant):
    # This extra free shoulder host is measured by the source-plane probe.
    # It is still a candidate until the independent layout proof is accepted.
    return tuple(sorted(set(layout.world_cells(variant=variant))|{(1,1)}))


def _owner_mask(variant):
    return unary_union([box(16*c-8,-16*r-8,16*c+8,-16*r+8) for c,r in _candidate_hosts(variant)])


def _clip_group_to_hosts(group, variant):
    faces=[]
    for triangle in group['triangles_ENHUV']:
        for cell in _candidate_hosts(variant):
            faces.extend(_clip_to_cell(triangle,cell))
    return {**group,'triangles_ENHUV':faces}


def _body_material(context, deck, variant):
    return next(group['material'] for group in native.socket_faces(context,'dd',variant)
                if group['role']=='body' and group['deck']==deck)


def _body_uv(point):
    return (point[0]/8.,point[1]/8.)


def _make_body_group(deck, material, kind):
    return {'role':'body','deck':deck,'material':material,'kind':kind,'triangles_ENHUV':[]}


def _line_parts(a,b,cutters):
    line=LineString((a,b));delta=np.subtract(b,a);length2=float(delta@delta)
    cuts={0.,1.}
    def collect(value):
        if value.geom_type=='Point':
            cuts.add(max(0.,min(1.,float((np.array(value.coords[0])-a)@delta/length2))))
        elif value.geom_type in ('LineString','LinearRing'):
            for p in value.coords:
                cuts.add(max(0.,min(1.,float((np.array(p)-a)@delta/length2))))
        elif hasattr(value,'geoms'):
            for part in value.geoms:collect(part)
    for shape in cutters:
        collect(line.intersection(shape))
    ordered=sorted(cuts)
    return [(tuple(np.array(a)+x*delta),tuple(np.array(a)+y*delta))
            for x,y in zip(ordered,ordered[1:]) if y>x]


def _rail_fields(groups,deck):
    fields=[]
    for group in groups:
        if group['role']!='barrier' or group['deck']!=deck:continue
        for triangle in group['triangles_ENHUV']:
            shape=Polygon([p[:2] for p in triangle])
            if shape.area>0.:fields.append((shape,triangle))
    return fields


def _phase_floor_sections(patches, deck, centre, normal, direction, station):
    """Cut actual finite phase triangles at C, retaining on-plane vertices.

    A GEOS line/polygon intersection can miss a complete end shoulder when
    two independently evaluated C coordinates differ by an arithmetic ULP.
    Reuse the finite source sectioner's 1e-11 m signed-distance classification
    instead. This is not the separate 4 micrometre saved-model tolerance, a
    polygon buffer, or an extrapolation of the source profile.
    """
    intervals=[]
    for patch in patches:
        if patch['deck']!=deck:
            continue
        triangles=[]
        for polygon in _polygons(patch['geometry']):
            for child in constrained_delaunay_triangles(polygon).geoms:
                triangles.append(tuple((e,n,patch['height_m'],0.,0.)
                    for e,n in list(child.exterior.coords)[:3]))
        group={'role':'pavement','deck':deck,'material':{},'triangles_ENHUV':triangles}
        for section in _section(group,direction,station):
            values=[sum((point[i]-centre[i])*normal[i] for i in range(2))
                    for point in (section['a'],section['b'])]
            intervals.append((min(values),max(values),patch['height_m']))
    return intervals


def _inner_rail_foot_shims(groups, patches, deck, material, variant, *,
                          kind='authored-DD-inner-rail-foot-phase-shim'):
    """Close actual authored inner rail feet above nominal 302 pavement.

    Native 302 asphalt is nominal while its raised rail starts at the 309
    datum. Actual incident inner-foot edges supply these finite new vertical
    panels. The caller selects authored continuations or the explicitly
    owned original302 reference crops. Original native faces stay unchanged;
    crowns, outer body strips, and already level309 roofs add no panels.
    """
    output=_make_body_group(deck,material,kind)
    output['construction_records']=[]
    centre,normal=geometry.frame(deck,geometry.COLLAR,variant=variant)
    lateral=lambda point:sum((point[i]-centre[i])*normal[i] for i in range(2))
    foot_height=(15. if deck=='upper' else 7.5)+geometry.pavement_datum(deck,0.)
    phase_patches=[patch for patch in patches if patch['deck']==deck]
    seen=set()
    for group in groups:
        if group['role']!='barrier' or group['deck']!=deck:
            continue
        for triangle_index,triangle in enumerate(group['triangles_ENHUV']):
            for index,a in enumerate(triangle):
                b=triangle[(index+1)%3];raised=triangle[(index+2)%3]
                if max(abs(point[2]-foot_height) for point in (a,b))>1e-10:
                    continue
                if raised[2]<=foot_height or math.dist(a[:3],b[:3])==0.:
                    continue
                # Moving from an inner foot towards its crest goes away
                # from the carriageway centre. The outer foot does not.
                if abs(lateral(raised))<=abs((lateral(a)+lateral(b))/2.):
                    continue
                key=tuple(sorted((tuple(a[:3]),tuple(b[:3]))))
                if key in seen:
                    continue
                seen.add(key)
                for first,last in _line_parts(a[:2],b[:2],
                        [patch['geometry'].boundary for patch in phase_patches]):
                    middle=LineString((first,last)).interpolate(.5,normalized=True)
                    floors=[patch['height_m'] for patch in phase_patches
                            if patch['geometry'].distance(middle)<=1e-9]
                    require(floors,'An authored DD inner rail foot has no finite roof phase')
                    floor=max(floors)
                    if floor>=foot_height:
                        continue
                    delta=np.subtract(b[:2],a[:2]);length2=float(delta@delta)
                    points=[]
                    for point in (first,last):
                        t=float((np.asarray(point)-a[:2])@delta/length2)
                        require(-1e-12<=t<=1.+1e-12,'Rail foot shim extrapolated its finite incident edge')
                        height=a[2]+t*(b[2]-a[2])
                        points.append((point[0],point[1],height,*_body_uv(point)))
                    low=[(point[0],point[1],floor,*point[3:]) for point in points]
                    desired=tuple((-1. if lateral(raised)>0. else 1.)*value
                                  for value in (*normal,0.))
                    output['triangles_ENHUV'].extend(_fan(
                        (low[0],low[1],points[1],points[0]),desired))
                    provenance=group.get('source_provenance',{})
                    if isinstance(provenance,list):
                        require(len(provenance)==len(group['triangles_ENHUV']),
                                'Native reference foot lost its exact source-parent association')
                        provenance=provenance[triangle_index]
                    output['construction_records'].append({
                        'incident_actual_rail_foot_edge_ENH':[list(a[:3]),list(b[:3])],
                        'finite_closed_interval_ENH':[[list(p[:3]) for p in low],
                                                     [list(p[:3]) for p in points]],
                        'floor_phase_height_m':floor,
                        'native_tile_id':group.get('native_tile_id',provenance.get('native_tile_id')),
                        'native_owner_kind':group.get('native_owner_kind'),
                        'pose':group.get('pose',provenance.get('pose')),
                        'source_world_cell':list(group.get('world_cell',provenance.get('world_cell',()))),
                        'original_native_reference':bool(group.get('analysis_only',False)),
                        'source_provenance':deepcopy(provenance),
                        'scope':'New finite authored inner-foot closure only; no original native face is removed'})
    return output


def _flat_body(context, groups, references, variant, *, foot_groups=()):
    """Construct real flat undersides and exposed walls, not native waivers."""
    output=[];patch_records=[]
    mask=_owner_mask(variant)
    for deck in ('upper','lower'):
        material=_body_material(context,deck,variant)
        rail_fields=_rail_fields([*groups,*references],deck)
        candidates=[g for g in references if g['role']=='pavement' and g['deck']==deck]
        candidates += [g for g in groups if g['role']=='pavement' and g['deck']==deck]
        candidates.sort(key=lambda g:(g.get('native_owner_kind')!='helper',not g.get('analysis_only',False)))
        used=Polygon();patches=[]
        for group in candidates:
            shape=_plan(group).intersection(mask).difference(used)
            if shape.is_empty:
                continue
            height=float(group['triangles_ENHUV'][0][0][2])
            patches.append({'geometry':shape,'height':height,'source_group':group})
            used=unary_union([used,shape])
        by_height=defaultdict(list)
        for patch in patches:
            by_height[patch['height']].append(patch['geometry'])
        patches=[{'geometry':unary_union(parts),'height':height} for height,parts in by_height.items()]
        floor=_make_body_group(deck,material,'authored-DD-underside')
        walls=_make_body_group(deck,material,'authored-DD-exposed-wall')
        phase=_make_body_group(deck,material,'authored-DD-floor-phase-step')
        top_steps=[]
        socket=native.socket_specs(variant)[0];direction=np.array([*socket.inward_en,0.])
        target=float(np.dot((*socket.mouth_en,0.),direction)+geometry.COLLAR)
        for patch in patches:
            height=patch['height'];bottom=14. if deck=='upper' else 6.5
            for part in _polygons(patch['geometry']):
                for child in constrained_delaunay_triangles(part).geoms:
                    points=tuple((e,n,bottom,e/8.,n/8.) for e,n in list(child.exterior.coords)[:3])
                    floor['triangles_ENHUV'].extend(_fan(points,(0.,0.,-1.)))
                for ring in (part.exterior,*part.interiors):
                    vertices=list(ring.coords)
                    signed=sum(a[0]*b[1]-b[0]*a[1] for a,b in zip(vertices,vertices[1:]))
                    edges=[part for a,b in zip(vertices,vertices[1:]) if math.dist(a,b)>0.
                           for part in _line_parts(a,b,[p['geometry'].boundary for p in patches]
                                                  +[shape for shape,_ in rail_fields])]
                    for a,b in edges:
                        if math.dist(a,b)==0.:
                            continue
                        if max(abs(np.dot((*p,0.),direction)-target) for p in (a,b))<2e-9:
                            continue
                        middle=LineString((a,b)).interpolate(.5,normalized=True)
                        covering=[tri for shape,tri in rail_fields if shape.distance(middle)<=1e-9]
                        rail=max(covering,key=lambda tri:_roof_attribute(tri,*middle.coords[0])[2]) if covering else None
                        top_a=max(height,_roof_attribute(rail,*a)[2]) if rail is not None else height
                        top_b=max(height,_roof_attribute(rail,*b)[2]) if rail is not None else height
                        neighbors=[p for p in patches if p is not patch and p['geometry'].distance(middle)<1e-8]
                        delta=np.subtract(b,a);desired=np.array([delta[1],-delta[0],0.])*(1. if signed>0 else -1.)
                        if neighbors:
                            other=min(neighbors,key=lambda p:abs(p['height']-height))['height']
                            if height>other and max(top_a,top_b)<=height+1e-10:
                                top_steps.append({'a':a,'b':b,'low':other,'high':height,'desired':desired.tolist()})
                            continue
                        points=((a[0],a[1],bottom,*_body_uv(a)),(b[0],b[1],bottom,*_body_uv(b)),
                                (b[0],b[1],top_b,*_body_uv(b)),(a[0],a[1],top_a,*_body_uv(a)))
                        walls['triangles_ENHUV'].extend(_fan(points,desired))
        for group in (floor,walls,phase):
            if group['triangles_ENHUV']:output.append(group)
        for step in top_steps:
            # This is an authored vertical closure at an actual phase boundary.
            # Its final material/UV/native-edge matching is separately audited.
            a,b=step['a'],step['b'];low,high=step['low'],step['high']
            q=((a[0],a[1],low,*_body_uv(a)),(b[0],b[1],low,*_body_uv(b)),
               (b[0],b[1],high,*_body_uv(b)),(a[0],a[1],high,*_body_uv(a)))
            g=_make_body_group(deck,material,'authored-DD-roof-phase-step')
            g['triangles_ENHUV']=_fan(q,step['desired']);output.append(g)
        patch_records.extend({'deck':deck,'height_m':p['height'],'underside_height_m':14. if deck=='upper' else 6.5,
                              'geometry':p['geometry']} for p in patches)
        shim=_inner_rail_foot_shims(foot_groups,patch_records,deck,material,variant)
        if shim['triangles_ENHUV']:
            output.append(shim)
        # These are new closing panels underneath the exact original302 rail
        # projection INSIDE owned cells. They do not copy, remove, or waive
        # any original native face, and cannot enter its reserved host cell.
        reference_feet=[group for group in references if group['role']=='barrier'
                        and group.get('native_tile_id')=='57530200']
        lip=_inner_rail_foot_shims(reference_feet,patch_records,deck,material,variant,
                                 kind='authored-DD-native-reference-inner-foot-lip')
        if lip['triangles_ENHUV']:
            output.append(lip)
    return output,patch_records


def _partition_dd_lofts(context, groups, references, variant):
    """Remove original rendered coverage and internal authored panels."""
    output=[];raw_pavement=[];trim_records=[]
    owner=_owner_mask(variant)
    for deck in ('upper','lower'):
        originals=[g for g in references if g['deck']==deck and g['role']=='pavement']
        original_mask=unary_union([_plan(g) for g in originals])
        barriers=[g for g in groups if g['deck']==deck and g['role']=='barrier']
        barrier_mask=unary_union([_plan(g) for g in barriers])
        taken=original_mask
        source_pavements=sorted([g for g in groups if g['deck']==deck and g['role']=='pavement'],
                                key=lambda g:g['native_owner_kind']!='helper')
        roof_by_kind={}
        for group in native.socket_faces(context,'dd',variant):
            if group['deck']==deck and group['role']=='pavement':
                roof_by_kind[group['native_owner_kind']]=group['triangles'][0][0][2]
        for group in source_pavements:
            allowed=_plan(group).intersection(owner).difference(taken)
            kept=_clip_roof(group,allowed)
            if kept['triangles_ENHUV']:
                raw_pavement.append(kept)
                visible=_clip_roof(kept,allowed.difference(barrier_mask))
                if visible['triangles_ENHUV']:output.append(visible)
            taken=unary_union([taken,allowed])
        for group in groups:
            if group['deck']!=deck or group['role']=='pavement':continue
            clipped=_clip_group_to_hosts(group,variant)
            if group['role']=='body':
                level=float(roof_by_kind[group['native_owner_kind']])
                faces=[]
                for face in clipped['triangles_ENHUV']:
                    faces.extend(_fan(_clip_plane(face,(0.,0.,1.),level),_normal(face)))
                trim_records.append({'deck':deck,'native_owner_kind':group['native_owner_kind'],
                    'source_provenance':group['source_provenance'],
                    'raw_triangle_count':len(clipped['triangles_ENHUV']),'exterior_triangle_count':len(faces),
                    'trim_below_actual_pavement_height_m':level,
                    'scope':'Authored profile continuation inside the new slab is omitted directly, not waived in analysis'})
                clipped={**clipped,'triangles_ENHUV':faces}
            if clipped['triangles_ENHUV']:output.append(clipped)
    body,patches=_flat_body(context,raw_pavement,references,variant,
                           foot_groups=[group for group in output if group['role']=='barrier'])
    return output+body,patches,trim_records


def _bridge_dd(context, groups, patches, variant, middle_section):
    """Sample the named1m bridge on the source PATH grid, with coherent floors."""
    output=[]
    start,finish=geometry.COLLAR,geometry.COLLAR+1.
    stations=sorted({start,finish,*(s for s in geometry.STATIONS if start<s<finish)})
    socket=native.socket_specs(variant)[0];axis=np.array([*socket.inward_en,0.])
    plane=float(np.dot((*socket.mouth_en,0.),axis)+start)
    for deck in ('upper','lower'):
        centre,normal=geometry.frame(deck,start,variant=variant)
        lateral=lambda p:sum((p[i]-centre[i])*normal[i] for i in range(2))
        segments=[]
        for group in groups:
            if group['deck']==deck and group['role'] in ('pavement','barrier'):
                for segment in _section(group,axis,plane):
                    a,b=segment['a'],segment['b'];lo,hi=lateral(a),lateral(b)
                    if lo>hi:a,b,lo,hi=b,a,hi,lo
                    if hi-lo>1e-10:segments.append((lo,hi,a,b,segment))
        require(segments,'Native DD collar has no finite inner roof profile')
        floor_intervals=_phase_floor_sections(patches,deck,centre,normal,axis,plane)
        require(floor_intervals,'DD collar underside has no finite common-plane section')
        low=min(p[0] for p in floor_intervals);high=max(p[1] for p in floor_intervals)
        anchors=[(low,-8.),(-geometry.LANE_OFFSET,-geometry.LANE_OFFSET),(0.,0.),
                 (geometry.LANE_OFFSET,geometry.LANE_OFFSET),(high,8.)]
        def mapped(u):
            for (a,x),(b,y) in zip(anchors,anchors[1:]):
                if a-1e-8<=u<=b+1e-8:return x+(u-a)*(y-x)/(b-a)
            raise ValueError('A native DD lateral point escapes the complete collar profile')
        def inverse(u):
            for (a,x),(b,y) in zip(anchors,anchors[1:]):
                if x-1e-8<=u<=y+1e-8:return a+(u-x)*(b-a)/(y-x)
            raise ValueError('A middle DD lateral point escapes its complete section')
        target=middle_section(deck,finish)
        end_centre,end_normal=geometry.frame(deck,finish,variant=variant)
        target_u=lambda p:sum((p[i]-end_centre[i])*end_normal[i] for i in range(2))
        target_roofs=[(i,row,target_u(row['a']),target_u(row['b']))
                      for i,row in enumerate(target) if row.get('surface_kind')=='roof']
        cuts={low,high,-geometry.LANE_OFFSET,0.,geometry.LANE_OFFSET}
        for a,b,*_ in segments:cuts.update((max(low,a),min(high,b)))
        for a,b,_ in floor_intervals:cuts.update((a,b))
        for _i,row,a,b in target_roofs:cuts.update((inverse(a),inverse(b)))
        cuts=sorted(u for u in cuts if low-1e-9<=u<=high+1e-9)
        unique=[]
        for u in cuts:
            if not unique or abs(u-unique[-1])>1e-10:unique.append(u)
        made={};strips=[]
        body_material=_body_material(context,deck,variant)
        def add(role,material,triangles):
            item=made.setdefault(role,{'role':role,'deck':deck,'material':material,
                                      'kind':'authored-DD-bridge','triangles_ENHUV':[]})
            item['triangles_ENHUV'].extend(triangles)
        native_PATH_height=15. if deck=='upper' else 7.5
        for low_u,high_u in zip(unique,unique[1:]):
            if high_u-low_u<=1e-12:continue
            middle=(low_u+high_u)/2.
            possible=[row for row in segments if row[0]-1e-8<=middle<=row[1]+1e-8]
            require(possible,'The measured DD top profile contains an uncovered lateral interval')
            def native_at(row,u):
                a,b,x,y,_record=row;t=(u-a)/(b-a)
                return tuple(x[i]+t*(y[i]-x[i]) for i in range(5))
            source=max(possible,key=lambda row:native_at(row,middle)[2])
            base_candidates=[h for a,b,h in floor_intervals if a-1e-8<=middle<=b+1e-8]
            require(base_candidates,'DD bridge has no supported native floor phase')
            native_base=min(base_candidates)
            nominal=mapped(middle)
            target_index,target_row,ta,tb=next(row for row in target_roofs if row[2]-1e-8<=nominal<=row[3]+1e-8)
            rings=[];floors=[]
            for station in stations:
                t=station-start;callback=middle_section(deck,station)[target_index]
                local_centre,local_normal=geometry.frame(deck,station,variant=variant)
                ua=sum((callback['a'][i]-local_centre[i])*local_normal[i] for i in range(2))
                ub=sum((callback['b'][i]-local_centre[i])*local_normal[i] for i in range(2))
                top=[];bottom=[]
                for u in (low_u,high_u):
                    nominal=mapped(u);f=(nominal-ua)/(ub-ua)
                    target_point=tuple(callback['a'][i]+f*(callback['b'][i]-callback['a'][i]) for i in range(5))
                    native_point=native_at(source,u)
                    base=geometry.height(deck,station)+(1-t)*(native_base-native_PATH_height)+t*geometry.pavement_datum(deck,station)
                    target_base=geometry.height(deck,station)+geometry.pavement_datum(deck,station)
                    height=base+(1-t)*(native_point[2]-native_base)+t*(target_point[2]-target_base)
                    physical_u=(1-t)*u+t*nominal
                    en=tuple(local_centre[i]+physical_u*local_normal[i] for i in range(2))
                    parent=source[4]['source_group'].get('source_provenance',{}).get('parent_triangle')
                    uv=_parent_uv(parent,(*en,height)) if parent is not None else native_point[3:]
                    floor=geometry.height(deck,station)-1.+t*geometry.pavement_datum(deck,station)
                    top.append((*en,height,*uv));bottom.append((*en,max(0.,floor),en[0]/8.,en[1]/8.))
                rings.append(top);floors.append(bottom)
            source_role=source[4]['role'];surface_role='barrier' if 'barrier' in target_row['role'] else 'pavement'
            role=f'dd-{deck}-{surface_role}-bridge-{len(strips):02d}'
            for first,last,a,b in zip(rings,rings[1:],floors,floors[1:]):
                add(role,source[4]['material'],_fan((first[0],first[1],last[1],last[0]),(0.,0.,1.)))
                # Keep the identical A_low-to-B_high diagonal, then flip winding.
                add(f'dd-{deck}-body-bridge-underside',body_material,
                    _fan((a[0],a[1],b[1],b[0]),(0.,0.,-1.)))
            strips.append((rings,floors))
        for index,(rings,floors) in enumerate(strips):
            for side in (0,1):
                adjacent=index-1 if side==0 else index+1
                if 0<=adjacent<len(strips):
                    other_rings,other_floors=strips[adjacent]
                    other_side=1-side
                    for a,b,c,d in zip(rings,rings[1:],other_rings,other_rings[1:]):
                        if max(abs(a[side][2]-c[other_side][2]),abs(b[side][2]-d[other_side][2]))<1e-11:continue
                        if (a[side][2]+b[side][2])<(c[other_side][2]+d[other_side][2]):continue
                        desired=tuple((1. if side else -1.)*x for x in (*normal,0.))
                        add(f'dd-{deck}-body-bridge-roof-step',body_material,
                            _fan((a[side],b[side],d[other_side],c[other_side]),desired))
                    for a,b,c,d in zip(floors,floors[1:],other_floors,other_floors[1:]):
                        if max(abs(a[side][2]-c[other_side][2]),abs(b[side][2]-d[other_side][2]))<1e-11:continue
                        if (a[side][2]+b[side][2])>(c[other_side][2]+d[other_side][2]):continue
                        desired=tuple((1. if side else -1.)*x for x in (*normal,0.))
                        add(f'dd-{deck}-body-bridge-floor-step',body_material,
                            _fan((a[side],b[side],d[other_side],c[other_side]),desired))
                else:
                    desired=tuple((1. if side else -1.)*x for x in (*normal,0.))
                    for a,b,c,d in zip(rings,rings[1:],floors,floors[1:]):
                        add(f'dd-{deck}-body-bridge-outer-wall',body_material,
                            _fan((a[side],b[side],d[side],c[side]),desired))
        output.extend(made.values())
    return output


def _parent_uv(triangle, point):
    a = np.array(triangle[0][:3]); x = np.array(triangle[1][:3])-a; y = np.array(triangle[2][:3])-a
    weights = np.linalg.solve(np.array([[x@x,x@y],[x@y,y@y]]),
                              np.array([x@(np.array(point)-a),y@(np.array(point)-a)]))
    return tuple(triangle[0][i]+weights[0]*(triangle[1][i]-triangle[0][i])
                 + weights[1]*(triangle[2][i]-triangle[0][i]) for i in (3,4))


def _source_plane_direction(triangle, desired):
    # A native rail's encoded longitudinal edge retains the exact foot/crown
    # height. Merely projecting the ideal45degree direction onto its sloped
    # face introduces a false vertical drift over the longer staggered loft.
    candidates=[]
    for a,b in zip(triangle,(*triangle[1:],triangle[0])):
        edge=np.subtract(b[:3],a[:3]);length=np.linalg.norm(edge)
        if length and abs(a[2]-b[2])<1e-12:
            unit=edge/length
            if unit@desired<0.:unit=-unit
            candidates.append((float(unit@desired),unit))
    if candidates:
        alignment,unit=max(candidates,key=lambda item:item[0])
        if alignment>.999999:
            return unit
    normal = _normal(triangle)
    unit = normal / np.linalg.norm(normal)
    projected = np.asarray(desired)-unit*np.dot(unit,desired)
    length = np.linalg.norm(projected)
    require(length > .999999, 'Native profile cannot continue longitudinally within its source plane')
    return projected/length


def _section(group, direction, station):
    """Finite triangle/plane sections retaining actual on-plane vertices."""
    result = []
    for triangle in group['triangles_ENHUV']:
        values = [np.dot(p[:3],direction)-station for p in triangle]
        # The encoded source plane can depart at sub-picometre arithmetic.
        values = [0. if abs(value)<1e-11 else value for value in values]
        points=[]
        for index,a in enumerate(triangle):
            b=triangle[(index+1)%3]; va,vb=values[index],values[(index+1)%3]
            if va==0.: points.append(a)
            if (va<0.<vb) or (vb<0.<va):
                t=va/(va-vb); points.append(tuple(x+t*(y-x) for x,y in zip(a,b)))
        unique=[]
        for p in points:
            if not any(math.dist(p[:3],q[:3])<1e-10 for q in unique): unique.append(p)
        if len(unique)==2 and math.dist(unique[0][:3],unique[1][:3])>1e-10:
            result.append({'role':group['role'],'deck':group['deck'],'material':group['material'],
                           'a':unique[0],'b':unique[1], 'source_group':group})
    return result


def _clip_to_cell(triangle, cell):
    c,r=cell; points=triangle
    for normal,plane,sign in (((1.,0.,0.),16*c-8.,1.),((1.,0.,0.),16*c+8.,-1.),
                               ((0.,1.,0.),-16*r-8.,1.),((0.,1.,0.),-16*r+8.,-1.)):
        points=_clip_plane(points,normal,plane,sign)
    return _fan(points,_normal(triangle))


def _reference_groups(context, variant):
    owned=_candidate_hosts(variant)
    result=[]
    for group in native.socket_faces(context,'dd',variant):
        fragments=[]; parents=[]
        for index,triangle in enumerate(group['triangles']):
            for cell in owned:
                children=_clip_to_cell(triangle,cell)
                fragments.extend(children)
                parents.extend({'face_index':index,'parent_triangle':triangle,'world_cell':cell}
                               for _ in children)
        if fragments:
            result.append({**{k:deepcopy(v) for k,v in group.items() if k!='triangles'},
                'triangles_ENHUV':fragments,'kind':'already-rendered-native','analysis_only':True,
                'source_provenance':parents})
    return result


def _profile_lofts(context, variant):
    socket=native.socket_specs(variant)[0]
    direction=np.array([*socket.inward_en,0.])
    target=np.dot((*socket.mouth_en,0.),direction)+geometry.COLLAR
    result=[]
    for profile in native.forward_profiles(context,'dd',variant):
        triangle=profile['parent_triangle']; a,b=profile['points']
        along=_source_plane_direction(triangle,direction)
        denominator=float(direction@along)
        lengths=[float((target-np.dot(point[:3],direction))/denominator) for point in (a,b)]
        require(min(lengths)>=geometry.NATIVE_COLLAR-1e-10,'The complete native profile lost its3m collar')
        shifted=[]
        for point,length in zip((a,b),lengths):
            position=tuple(point[i]+length*along[i] for i in range(3))
            shifted.append((*position,*_parent_uv(triangle,position)))
        faces=_fan((a,b,shifted[1],shifted[0]),_normal(triangle))
        result.append({'role':profile['role'],'deck':profile['deck'],'material':deepcopy(profile['material']),
            'triangles_ENHUV':faces,'kind':'native-profile-loft','socket_arm':'dd',
            'native_owner_kind':profile['native_owner_kind'],
            'source_provenance':{k:deepcopy(profile[k]) for k in ('native_tile_id','pose','world_cell',
                'mesh_index','face_index','source_model_sha256','parent_triangle','points')}
                | {'target_plane_normal_ENH':direction.tolist(),'target_plane_station_m':float(target),
                   'actual_parent_plane_longitudinal_unit_ENH':along.tolist(),
                   'minimum_extension_m':min(lengths),'maximum_extension_m':max(lengths)}})
    return result


def _ownership(groups, variant):
    owned=set(layout.world_cells(variant=variant)); required=set(); forbidden=set()
    for group in groups:
        for triangle in group['triangles_ENHUV']:
            es=[p[0] for p in triangle]; ns=[p[1] for p in triangle]
            for c in range(math.floor((min(es)+8)/16),math.floor((max(es)+8)/16)+1):
                for r in range(math.floor((8-max(ns))/16),math.floor((8-min(ns))/16)+1):
                    if _clip_to_cell(triangle,(c,r)):
                        required.add((c,r))
                        if layout.is_reserved_native_cell((c,r),variant=variant): forbidden.add((c,r))
    return {'declared_world_cells':[list(c) for c in sorted(owned)],
            'authored_profile_required_world_cells':[list(c) for c in sorted(required)],
            'additional_free_host_cells':[list(c) for c in sorted(required-owned-forbidden)],
            'reserved_native_intersections':[list(c) for c in sorted(forbidden)],
            'reviewed':False}


def build_dd_profiles(context, *, variant):
    """Concrete finite parent-plane lofts and strict native reference ROIs.

    This lower-level capture intentionally reports unresolved host/topology
    work; it is useful before a middle writer or permanent IDs exist.
    """
    groups=_profile_lofts(context,variant)
    references=_reference_groups(context,variant)
    socket=native.socket_specs(variant)[0]
    direction=(*socket.inward_en,0.)
    target=float(np.dot((*socket.mouth_en,0.),direction)+geometry.COLLAR)
    rings={deck:[segment for group in groups if group['deck']==deck
                for segment in _section(group,direction,target)] for deck in ('upper','lower')}
    return {'groups':groups,'references':references,'inner_profiles':rings,
            'ownership':_ownership(groups,variant),
            'source_scopes':{'DD_native_parent_planes':'Exact original edge vertices, UV fields, and parent-plane longitudinal directions',
                'native_reference_ROI':'Only actual helper/peer fragments inside the declared custom host union; never copied into the custom DAT',
                'native_minimum_continuation_m':geometry.NATIVE_COLLAR,
                'body_underside_and_phase_closure':'Not yet emitted by this lower-level profile capture',
                'accepted':False}}


def build_collars(context, *, variant, middle_section):
    """Emit a concrete first-A candidate; acceptance remains independent."""
    require(callable(middle_section),'A concrete closed middle-section callback is required')
    dd=build_dd_profiles(context,variant=variant)
    flat,patches,trimmed=_partition_dd_lofts(context,dd['groups'],dd['references'],variant)
    bridge=_bridge_dd(context,flat,patches,variant,middle_section)
    for index,group in enumerate(flat):
        group['surface_role']=group['role']
        group['role']=f"dd-{group['deck']}-{group['role']}-{group['kind']}-{index:02d}"
    from .diagonal_transition_ground_collars import build_ground_collars
    ground=build_ground_collars(context,variant=variant,middle_section=middle_section)
    return {'groups':flat+bridge+ground['groups'],
            'references':dd['references']+ground.get('references',[]),
            'inner_profiles':dd['inner_profiles'],
            'ground_inner_profiles':ground['inner_profiles'],
            'source_scopes':{'dd':dd['source_scopes'],'ground':ground.get('source_scopes',{}),
                'DD_authored_internal_body_panels_trimmed':trimmed,
                'DD_phase_floor_patches':[{'deck':p['deck'],'height_m':p['height_m'],
                    'underside_height_m':p['underside_height_m'],'plan_geometry':p['geometry'].__geo_interface__}for p in patches],
                'DD_floor_field':{'flat_upper_m':14.,'flat_lower_m':6.5,
                    'bridge':'PATHheight(s)-1+t*faded309Datum(s), t=s-C in the named1m bridge',
                    'actual_flat_depth_m':[1.,1.0010004043579102],
                    'minimum_depth_waiver':False},
                'DD_common_plane_section':{
                    'method':'Finite phase-polygon triangles and original source-profile breakpoints',
                    'on_plane_arithmetic_classification_m':1e-11,
                    'source_points_extrapolated':False,
                    'saved_model_physical_tolerance_unchanged_m':4e-6},
                'DD_authored_inner_rail_foot_closures':[
                    {'deck':g['deck'],'records':g['construction_records']}
                    for g in flat if g['kind'] in ('authored-DD-inner-rail-foot-phase-shim',
                                                   'authored-DD-native-reference-inner-foot-lip')],
                'closed_skin_and_actual_saved_checks':'Pending independent actual candidate checks','accepted':False},
            'middle_start_s':geometry.COLLAR+1.,'middle_end_s':geometry.LENGTH-geometry.COLLAR-1.,
            'ownership':{'dd':dd['ownership'],'ground':ground.get('ownership',{}),'reviewed':False}}
