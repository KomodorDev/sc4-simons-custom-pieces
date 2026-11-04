"""Physical, native-textured first-phase DD RHW Y road and support solids.

Planar unions remove duplicate pavement and inside walls before constrained
triangulation. Graded ribbons retain an explicit driving-centreline seam.
The exact-plane transition clipper owns every final city-tile cut.
"""
from __future__ import annotations

from collections import defaultdict,Counter
from copy import deepcopy
from functools import lru_cache
import hashlib
import math
from pathlib import Path
import struct

import numpy as np
import shapely
from shapely.geometry import Polygon, LineString, Point, box
from shapely.geometry.polygon import orient

from scp import jsonc
from scp.models import parse_s3d
from scp.track_paths import S3D
from . import native, ramp_geometry, ramp_paths, orthogonal_transition
from .ramp_materials import native_materials
from . import y_junction_native_models as native_models
from .y_junction_surface_uv import NATIVE_FAN_END_M, flat_surface_domains, ribbon_markings

SUBJECT = Path(__file__).resolve().parents[2]/"01_assemblies/ddrhw-compact-diagonal-y-junction"
DATUM_LOWER = 0.0009999275207519531
DATUM_UPPER = 0.0010004043579101562
DEPTH = 1.0
WIDTH = 6.0
INNER_GRADE_HALF_WIDTH=2.25
FLAT_SHOULDER_TAPER_M=2.0
GRADE_END_NARROW_HOLD_M=5.0
GRADE_INTERIOR_RECOVERY_M=5.0
SOCKETS = {"A": {"outside": (-2,2), "donor": 0x57530900, "pose": 0, "point": (-24.,-32.), "inward": (math.sqrt(.5),math.sqrt(.5))},
           "B": {"outside": (-2,-2), "donor": 0x57530900, "pose": 3, "point": (-24.,32.), "inward": (math.sqrt(.5),-math.sqrt(.5))},
           "C": {"outside": (4,0), "donor": 0x57530000, "pose": 3, "point": (56.,0.), "inward": (-1.,0.)}}
_WORLD_CACHE = {}


def _require(test, message):
    if not test:
        raise ValueError(message)


def pavement_datum(height):
    return DATUM_LOWER+(float(height)-7.5)/7.5*(DATUM_UPPER-DATUM_LOWER)


@lru_cache(maxsize=1)
def _parsed_source_report(raw):
    return jsonc.loads(raw.decode("utf-8"))


def source_report():
    """Read current source bytes; callers cannot mutate the cached parsed value."""
    return deepcopy(_parsed_source_report((SUBJECT/"evidence/design-geometry.jsonc").read_bytes()))


def source_routes():
    report = source_report()
    return [{"id": name, "points": deepcopy(points), "transport": 1,
             "lane": report["route_metadata"][name]["from_lane"], "junction": False}
            for name,points in report["routes"].items()]


def _mesh_vertices(model, mesh):
    vi,ii,_pi,mi = mesh["frames"][0]
    vb = model["vertices"][vi]
    points = [struct.unpack_from("<5f",vb["data"],offset) for offset in range(0,len(vb["data"]),vb["stride"])]
    return points,model["indices"][ii]["values"],model["materials"][mi]


def _native_profiles(context,*,native_source=native_models,sockets=SOCKETS):
    profiles = {}
    for arm,record in sockets.items():
        model = native.rotate_model(parse_s3d(context["dd_rhw"][*S3D,record["donor"]]),record["pose"])
        origin = np.array([16*record["outside"][0],-16*record["outside"][1]])
        for deck,label in (("upper",b"Top Deck"),("lower",b"Bottom Deck")):
            mesh = next(m for m in model["meshes"] if m["name"].rstrip(b"\0")==label)
            vertices,indices,material = _mesh_vertices(model,mesh)
            triangle = [vertices[i] for i in indices[:3]]
            matrix = np.array([[p[0]+origin[0],-p[2]+origin[1],1.] for p in triangle])
            coefficients = np.linalg.solve(matrix,np.array([[p[3],p[4]] for p in triangle]))
            # UV decimals are rounded authoring values, not a dimensional
            # measurement. Derive both physical sides from actual native
            # helper/peer vertices, retaining their asymmetric millimetre phase.
            inward=np.asarray(record["inward"]);normal=np.array([-inward[1],inward[0]])
            axis=np.asarray(record["point"])
            native_points=[np.array([p[0],-p[2]])for group in native_source.posed_native_faces(context,arm,arm!="C")
                           if group["role"]=="pavement"and group["deck"]==deck
                           for triangle in group["triangles"]for p in triangle]
            lateral=[float((p-axis)@normal)for p in native_points]
            low,high=min(lateral),max(lateral)
            width=high-low;centre=axis+normal*((high+low)/2)
            profiles[arm,deck] = {"coefficients":coefficients,"width":float(width),"centre":centre,
                                  "material":deepcopy(material),"model":model,
                                  "height":vertices[0][1]}
    return profiles


def _frame(route):
    stations,normals = ramp_geometry.route_frames(route)
    return np.asarray(stations),np.asarray(normals)


def _route_skin(route,points,station,normals):
    """Move only the ramp's inner shoulder near its two height transitions.

    External flat runs keep the full 6 m profile. A two-metre cubic taper
    reaches the 5.25 m section at the grade boundary, holds it for five
    metres, and recovers over five metres towards the wide interior.
    """
    low=np.full(len(points),-3.);high=np.full(len(points),3.)
    if route["id"]in("B-C","C-B"):
        start=int(np.flatnonzero(points[:,2]>points[0,2])[0])-1
        end=int(np.flatnonzero(points[:,2]==points[-1,2])[0])
        a,b=station[start],station[end]
        def smooth(value):
            q=np.clip(value,0.,1.);return q*q*(3.-2.*q)
        entry=smooth((station-(a-FLAT_SHOULDER_TAPER_M))/FLAT_SHOULDER_TAPER_M)
        entry*=1.-smooth((station-(a+GRADE_END_NARROW_HOLD_M))/GRADE_INTERIOR_RECOVERY_M)
        exit=smooth((station-(b-GRADE_END_NARROW_HOLD_M-GRADE_INTERIOR_RECOVERY_M))/GRADE_INTERIOR_RECOVERY_M)
        exit*=1.-smooth((station-b)/FLAT_SHOULDER_TAPER_M)
        reduction=(3.-INNER_GRADE_HALF_WIDTH)*np.maximum(entry,exit)
        if route["id"]=="B-C":low+=reduction
        else:high-=reduction
    rail_low=points[:,:2]+low[:,None]*normals
    rail_high=points[:,:2]+high[:,None]*normals
    _,normal_low=_frame(np.column_stack([rail_low,np.zeros(len(points))]))
    _,normal_high=_frame(np.column_stack([rail_high,np.zeros(len(points))]))
    return {"low_offsets":low,"high_offsets":high,"rail_low":rail_low,"rail_high":rail_high,
            "inward_low":normal_low,"inward_high":-normal_high}


def _road_polygon(road,index):
    return Polygon([road["rail_low"][index],road["rail_low"][index+1],
                    road["rail_high"][index+1],road["rail_high"][index]])


def _taper_engineering(roads):
    result={}
    for road in roads:
        if road["id"]not in("B-C","C-B"):continue
        points,station=road["points"],road["station"]
        start=int(np.flatnonzero(points[:,2]>points[0,2])[0])-1
        end=int(np.flatnonzero(points[:,2]==points[-1,2])[0])
        a,b=float(station[start]),float(station[end])
        result[road["id"]]={
            "station_frame":"cumulative horizontal source-route metres from the external incoming endpoint",
            "inner_side":"right"if road["id"]=="B-C"else"left",
            "interpolation":"cubic smoothstep q*q*(3-2*q), sampled at the unchanged source polyline stations",
            "grade_start_station_m":a,"grade_end_station_m":b,
            "inner_half_width_station_m":[[a-FLAT_SHOULDER_TAPER_M,3.],[a,INNER_GRADE_HALF_WIDTH],
                [a+GRADE_END_NARROW_HOLD_M,INNER_GRADE_HALF_WIDTH],
                [a+GRADE_END_NARROW_HOLD_M+GRADE_INTERIOR_RECOVERY_M,3.],
                [b-GRADE_END_NARROW_HOLD_M-GRADE_INTERIOR_RECOVERY_M,3.],
                [b-GRADE_END_NARROW_HOLD_M,INNER_GRADE_HALF_WIDTH],
                [b,INNER_GRADE_HALF_WIDTH],[b+FLAT_SHOULDER_TAPER_M,3.]],
            "outer_half_width_m":3.,"minimum_inner_half_width_m":INNER_GRADE_HALF_WIDTH,
            "minimum_deck_width_m":3.+INNER_GRADE_HALF_WIDTH,
            "minimum_asphalt_width_m":3.+INNER_GRADE_HALF_WIDTH-2*BARRIER[-1][0],
            "nominal_inner_barrier_clearance_m":INNER_GRADE_HALF_WIDTH-BARRIER[-1][0],
            "nominal_vehicle_half_width_margin_m":INNER_GRADE_HALF_WIDTH-BARRIER[-1][0]-1.25}
    return result


def _components(geometry):
    if geometry.is_empty:
        return []
    return [geometry] if geometry.geom_type=="Polygon" else [p for p in geometry.geoms if p.geom_type=="Polygon"]


def _unions(profiles,*,construction_routes=None,sockets=SOCKETS,native_source=native_models,full_width_stations=None):
    """Return flat carriageway unions and two joining graded strips."""
    polygons = {"upper":[],"lower":[]}
    graded,all_roads,mouths = [],[],[]
    reference_extra={"upper":[],"lower":[]}
    for route in source_routes()if construction_routes is None else construction_routes:
        points = np.asarray(route["points"])
        station,normals = _frame(points)
        skin=_route_skin(route,points,station,normals)
        full_road={**route,"points":points,"station":station,"normals":normals,**skin}
        all_roads.append(full_road)
        low,high = points[:,2].min(),points[:,2].max()
        if low==high:
            selected = [("upper" if high>10 else "lower",0,len(points)-1)]
        else:
            start = int(np.flatnonzero(points[:,2]>low)[0])-1
            end = int(np.flatnonzero(points[:,2]==high)[0])
            selected = [("lower",0,start),("upper",end,len(points)-1)]
            graded.append({**route,"points":points[start:end+1],"station":station[start:end+1],
                           "normals":normals[start:end+1],"full_length":float(station[-1]),
                           "first_index":start,"last_index":end,
                           **{key:values[start:end+1]for key,values in skin.items()}})
            for deck,indices in (("lower",range(start,min(end,len(points)-1))),
                                  ("upper",range(max(start,0),end))):
                for i in indices:
                    distance=(station[i]-station[start])if deck=="lower"else(station[end]-station[i+1])
                    if distance<=6.:
                        reference_extra[deck].append(_road_polygon(full_road,i))
        for deck,first,last in selected:
            polygons[deck].extend(_road_polygon(full_road,i)for i in range(first,last))
    # Full measured DD cross-sections at each external end taper only after
    # the retained native joining collar, before either active height change.
    for (arm,deck),profile in profiles.items():
        direction = np.array(sockets[arm]["inward"])
        normal = np.array([-direction[1],direction[0]])
        centre = profile["centre"]
        rings=[]
        full_station=11. if arm in("A","B")else 3.
        if full_width_stations is not None:full_station=full_width_stations.get(arm,full_station)
        for station,half in ((-9.,profile["width"]/2),(full_station,profile["width"]/2),(NATIVE_FAN_END_M,5.0)):
            rings.append((centre+station*direction,normal,half))
        parent_parts=[]
        for (p,n,half),(q,m,last_half) in zip(rings,rings[1:]):
            polygon = Polygon([p+n*half,q+m*last_half,q-m*last_half,p-n*half])
            reference_extra[deck].append(polygon)
            # The outside PATH socket remains native. Physical shoulders may
            # occupy neighbouring model-only cells to retain the full profile.
            if arm=="C":
                polygon = polygon.intersection(box(-200.,-200.,56.,200.))
            polygons[deck].append(polygon)
            parent_parts.append(polygon)
        mouths.append({"arm":arm,"deck":deck,"geometry":shapely.union_all(parent_parts)})
    reference={deck:shapely.union_all([*parts,*reference_extra[deck]],grid_size=1e-9) for deck,parts in polygons.items()}
    reserved=[]
    for arm,cells in native_source.reserved_native_cells(2).items():
        if arm=="C":continue
        reserved.extend(box(16*c-8,-16*r-8,16*c+8,-16*r+8)for c,r in cells)
    forbidden=shapely.union_all(reserved)
    flat = {deck:shapely.union_all(parts,grid_size=1e-9).difference(forbidden).intersection(box(-200.,-200.,56.,200.)) for deck,parts in polygons.items()}
    for deck,geometry in flat.items():
        _require(geometry.is_valid,f"Invalid {deck} pavement union")
    return flat,graded,all_roads,reference,mouths


def _clip_triangle_plan(triangle,geometry):
    """Trim a nonvertical native roof face with its own affine UV field."""
    original=Polygon([(p[0],-p[2])for p in triangle])
    if original.area<1e-14:return [triangle]
    clipped=original.intersection(geometry)
    if clipped.is_empty:return []
    matrix=np.array([[p[0],-p[2],1.]for p in triangle])
    fields=np.linalg.solve(matrix,np.array([[p[1],p[3],p[4]]for p in triangle]))
    result=[]
    for part in _components(clipped):
        for poly in shapely.constrained_delaunay_triangles(part).geoms:
            face=[]
            for e,n in list(poly.exterior.coords)[:3]:
                h,u,v=np.array([e,n,1.])@fields
                face.append((e,h,-n,u,v))
            result.extend(_quad(face,(0.,1.,0.)))
    return result


def _native_collars(context,painter,*,native_source=native_models,sockets=SOCKETS,profiles=None,
                    low_floor_kind="peer",roof_priority_kind="helper",visible_priority_mask=False):
    loft=native_source.extrude_native_collars(context,3.,arms=("A","B"))
    original={deck:[]for deck in("upper","lower")}
    for arm in sockets:
        for group in native_source.posed_native_faces(context,arm,arm!="C"):
            if group["role"]=="pavement":
                original[group["deck"]].extend(Polygon([(p[0],-p[2])for p in face])for face in group["triangles"])
    original={deck:shapely.union_all(parts)for deck,parts in original.items()}
    helper={deck:shapely.union_all([p["geometry"]for p in loft["pavement_polygons"]if p["deck"]==deck and p["kind"]==roof_priority_kind])
            for deck in("upper","lower")}
    if visible_priority_mask:
        helper={deck:geometry.difference(original[deck])for deck,geometry in helper.items()}
    faces,patches=[],[]
    barrier_masks={deck:[]for deck in("upper","lower")}
    for arm in sockets:
        for group in native_source.posed_native_faces(context,arm,arm!="C"):
            if group["role"]=="barrier":
                barrier_masks[group["deck"]].extend(Polygon([(p[0],-p[2])for p in face])for face in group["triangles"])
    for group in loft["groups"]:
        role=f"{group['role']}-native-{group['arm']}-{group['deck']}-{group['kind']}"
        if role not in painter.materials:
            painter.materials[role]=deepcopy(group["material"]);painter.roles.append(role)
        selected=group["triangles"]
        if group["arm"]=="C":
            selected=[face for triangle in selected for face in _clip_triangle_plan(triangle,box(-200.,-200.,56.,200.))]if group["role"]=="pavement"else[
                face for triangle in selected for face in _clip_any_triangle_east(triangle,56.,-1)]
        if group["role"]=="pavement":
            permitted=box(-200.,-200.,200.,200.).difference(original[group["deck"]])
            if group["kind"]!=roof_priority_kind:permitted=permitted.difference(helper[group["deck"]])
            selected=[face for triangle in selected for face in _clip_triangle_plan(triangle,permitted)]
            geometry=shapely.union_all([Polygon([(p[0],-p[2])for p in face])for face in selected])
            patches.append({"geometry":geometry,"height":group["triangles"][0][0][1],"deck":group["deck"],"kind":group["kind"]})
        code=painter.role(role)
        faces.extend(tuple((*p,float(code))for p in triangle)for triangle in selected)
        if group["role"]=="barrier":
            barrier_masks[group["deck"]].extend(Polygon([(p[0],-p[2])for p in face])for face in selected)
        if group["role"]=="barrier"and group["kind"]==low_floor_kind:
            # The original 302 asphalt is nominal-height, while its barrier
            # foot is +1 mm. Close that inherited inner-foot slit explicitly
            # inside the authored collar, without lowering either native face.
            edges=Counter(tuple(sorted((a[:3],b[:3])))for triangle in selected
                          for a,b in zip(triangle,(*triangle[1:],triangle[0])))
            base=min(p[1]for triangle in selected for p in triangle)
            floor=15. if group["deck"]=="upper"else 7.5
            shim_role=f"barrier-{low_floor_kind}-foot-shim"
            if shim_role not in painter.materials:
                painter.materials[shim_role]=deepcopy(group["material"]);painter.roles.append(shim_role)
            shim_code=painter.role(shim_role)
            measured=_native_profiles(context,native_source=native_source,sockets=sockets)if profiles is None else profiles
            coefficients=measured[group["arm"],group["deck"]]["coefficients"][:,0]
            for triangle in selected:
                for a,b in zip(triangle,(*triangle[1:],triangle[0])):
                    if edges[tuple(sorted((a[:3],b[:3])))]!=1 or math.dist(a[:3],b[:3])<2.9:continue
                    if max(abs(a[1]-base),abs(b[1]-base))>2e-6:continue
                    across=float(np.array([(a[0]+b[0])/2,-(a[2]+b[2])/2,1.])@coefficients)
                    if not .01<across<.99:continue
                    inward=(-1. if across>.5 else 1.)*coefficients[:2]
                    outward=(float(inward[0]),0.,float(-inward[1]))
                    points=[(*p,float(shim_code))for p in(a,b,(b[0],floor,b[2],b[3],b[4]),(a[0],floor,a[2],a[3],a[4]))]
                    faces+=_quad(points,outward)
    for group in native_source.retained_core_collar_faces(context,"C",3.):
        role=f"{group['role']}-native-C-{group['deck']}-retained-core-collar"
        if role not in painter.materials:
            painter.materials[role]=deepcopy(group["material"]);painter.roles.append(role)
        code=painter.role(role)
        faces.extend(tuple((*p,float(code))for p in fragment["triangle"])for fragment in group["fragments"])
        projected=[Polygon([(p[0],-p[2])for p in fragment["triangle"]])for fragment in group["fragments"]]
        if group["role"]=="pavement":
            geometry=shapely.union_all(projected).intersection(box(-200.,-200.,56.,200.))
            patches.append({"geometry":geometry,"height":group["fragments"][0]["triangle"][0][1],"deck":group["deck"],"kind":"retained-core-collar"})
        elif group["role"]=="barrier":barrier_masks[group["deck"]].extend(projected)
    barrier_masks={deck:shapely.union_all([p for p in parts if p.area>1e-15])for deck,parts in barrier_masks.items()}
    return faces,patches,original,loft,barrier_masks


def _clip_any_triangle_east(triangle,boundary,direction):
    polygon=orthogonal_transition._clip_plane(list(triangle),0,boundary,direction)
    return _quad(polygon)


class _Painter:
    def __init__(self,context,profiles):
        native_set = native_materials(context)
        self.materials={"pavement":native_set["ramp"],"body":native_set["concrete"],"barrier":native_set["barrier"]}
        for (arm,deck),profile in profiles.items():
            self.materials[f"pavement-native-{arm}-{deck}"]=profile["material"]
        self.roles=list(self.materials)
        self.graded_end_windows={}
        self.flat_texture_domains=[]
        self.marking_fields={}

    def role(self,name):
        if name not in self.materials:
            self.materials[name]=deepcopy(self.materials["body"])
            self.roles.append(name)
        return self.roles.index(name)


def _vertex(e,n,h,uv,code):
    return (float(e),float(h),float(-n),float(uv[0]),float(uv[1]),float(code))


def _quad(points,normal=None):
    return ramp_geometry._triangulate(points,normal,minimum_normal_squared=1e-22)


def _closest_frame(point,roads,deck):
    cache=roads[0].setdefault("uv_frame_cache",{})
    key=round(float(point[0]),9),round(float(point[1]),9),deck
    if key in cache:return cache[key]
    best=None
    for road in roads:
        pts=np.asarray(road["points"])
        mask=np.abs(pts[:,2]-(15. if deck=="upper" else 7.5))<1e-7
        candidates=np.flatnonzero(mask)
        if not len(candidates):continue
        distances=np.sum((pts[candidates,:2]-point)**2,axis=1)
        index=int(candidates[int(distances.argmin())])
        if best is None or distances.min()<best[0]:
            normal=road["normals"][index]
            lateral=float((point-pts[index,:2])@normal)/(float(normal@normal))
            best=float(distances.min()),lateral,float(road["station"][index])
    result=(.5,0.) if best is None else (.5+best[1]/16.,best[2]/16.)
    cache[key]=result
    return result


def _triangulate_surface(polygon,height,code,uv,maximum_edge_m=None):
    faces=[]
    for part in _components(polygon):
        triangles=shapely.constrained_delaunay_triangles(part)
        _require(abs(sum(p.area for p in triangles.geoms)-part.area)<max(1e-8,part.area*1e-10),
                 "Constrained roof triangulation changed polygon area")
        for triangle in triangles.geoms:
            pending=[list(triangle.exterior.coords)[:3]]
            while pending:
                face=pending.pop()
                lengths=[math.dist(face[a],face[b])for a,b in((0,1),(1,2),(2,0))]
                longest=max(range(3),key=lengths.__getitem__)
                if maximum_edge_m is not None and lengths[longest]>maximum_edge_m+1e-10:
                    a,b=((0,1),(1,2),(2,0))[longest];c=3-a-b
                    middle=tuple((face[a][k]+face[b][k])/2 for k in range(2))
                    pending.extend([[face[a],middle,face[c]],[middle,face[b],face[c]]]);continue
                points=[_vertex(e,n,height(np.array([e,n]))if callable(height)else height,uv(np.array([e,n])),code)for e,n in face]
                faces+=_quad(points,(0.,1.,0.))
    return faces


def _attachment_lines(graded,deck):
    lines=[]
    for road in graded:
        index=-1 if deck=="upper" else 0
        lines.append(LineString([road["rail_low"][index],road["rail_high"][index]]))
    return lines


# Native DD/MIS cross-section: outer base, outer shoulder, outer crest,
# inner crest, inner shoulder, and inner base. Heights are native measurements.
BARRIER=((0.,0.),(.21875,.328125),(.265625,1.390625),(.5625,1.390625),(.625,.328125),(.828125,0.))
BARRIER_UV=((1.,.7119640111923218),(.7119640111923218,0.),(.32499998807907104,.625),
            (0.,.7119640111923218),(.7119640111923218,1.))


def _barrier_segment(first,last,height,code,normal_first=None,normal_last=None,stations=None,source_station_by_vertex=None):
    a,b=np.asarray(first),np.asarray(last)
    direction=(b-a)/np.linalg.norm(b-a)
    # Oriented polygons have road interior left of every boundary edge.
    inward=np.array([-direction[1],direction[0]])
    nfirst=inward if normal_first is None else np.asarray(normal_first)
    nlast=inward if normal_last is None else np.asarray(normal_last)
    faces=[]
    for band,((inset_a,rise_a),(inset_b,rise_b)) in enumerate(zip(BARRIER,BARRIER[1:])):
        points=[]
        for endpoint,point,normal,inset,rise,v in ((0,a,nfirst,inset_a,rise_a,BARRIER_UV[band][0]),(1,b,nlast,inset_a,rise_a,BARRIER_UV[band][0]),
                                                (1,b,nlast,inset_b,rise_b,BARRIER_UV[band][1]),(0,a,nfirst,inset_b,rise_b,BARRIER_UV[band][1])):
            altitude=height[0] if np.array_equal(point,a) else height[1]
            p=point+inset*normal
            u=float(point@direction)/16. if stations is None else stations[endpoint]/16.
            vertex=_vertex(*p,altitude+rise,(u,v),code)
            points.append(vertex)
            if source_station_by_vertex is not None:source_station_by_vertex[id(vertex)]=stations[endpoint]
        # Each band is the top of a raised solid and a height graph over
        # the horizontal plane, on either side of the driving lane.
        faces+=_quad(points,(0.,1.,0.))
    return faces


def _flat_faces(flat,graded,roads,profiles,painter,reference,patches=(),barrier_masks=None,step_profiles=(),parent_mouths=(),*,surface_domains=flat_surface_domains,bottom_builder=None):
    faces=[]
    for deck,polygon in flat.items():
        altitude=15. if deck=="upper" else 7.5
        roof=altitude+pavement_datum(altitude)
        ref=reference[deck]
        boundary_layers=[ref.buffer(-inset,join_style="mitre",mitre_limit=2.).boundary for inset,_height in BARRIER[1:]]
        inside=ref.buffer(-BARRIER[-1][0],join_style="mitre",mitre_limit=2.)
        deck_patches=[p for p in patches if p["deck"]==deck]
        patch_mask=shapely.union_all([p["geometry"]for p in deck_patches])
        if barrier_masks is not None:patch_mask=patch_mask.union(barrier_masks[deck])
        pending=polygon.intersection(inside).difference(patch_mask)
        for domain in surface_domains(pending,roads,deck,profiles,parent_mouths):
            uv = domain["uv"]
            paint = painter.marking_fields.get(domain["owner"])
            if paint is not None:
                uv = lambda point, base=uv, field=paint: field(point, base(point))
            faces+=_triangulate_surface(domain["geometry"],roof,painter.role(domain["material_role"]),uv,
                                         domain.get("maximum_edge_m"))
            painter.flat_texture_domains.append({"deck":deck,"owner":domain["owner"],
                "material_role":domain["material_role"],"area_m2":float(domain["geometry"].area),"frame":domain["frame"]})
        outer=ref
        height_fields=[]
        for index,((a,h),(b,k))in enumerate(zip(BARRIER,BARRIER[1:])):
            inner=ref.buffer(-b,join_style="mitre",mitre_limit=2.)
            full_band=outer.difference(inner)
            band=full_band.intersection(polygon).difference(patch_mask)
            outer_boundary,inner_boundary=outer.boundary,inner.boundary
            def fraction(point,outside=outer_boundary,inside=inner_boundary,cache={}):
                key=round(float(point[0]),9),round(float(point[1]),9)
                if key in cache:return cache[key]
                first=outside.distance(Point(point));last=inside.distance(Point(point))
                value=0. if first<1e-8 else 1. if last<1e-8 else first/(first+last)
                cache[key]=value
                return value
            height_field=lambda p,f=fraction,ha=h,hb=k:roof+ha+(hb-ha)*f(p)
            height_fields.append((full_band,height_field))
            faces+=_triangulate_surface(band,height_field,
                                         painter.role("barrier"),lambda p,f=fraction,i=index:
                                         (_closest_frame(p,roads,deck)[1],BARRIER_UV[i][0]+(BARRIER_UV[i][1]-BARRIER_UV[i][0])*f(p)))
            outer=inner
        def flat_height(point):
            p=Point(point)
            return next((field(np.asarray(point))for region,field in height_fields if region.distance(p)<1e-8),roof)
        if bottom_builder is None:
            bottom=_triangulate_surface(polygon,roof-DEPTH,painter.role("body"),lambda p:(p[0]/8.,p[1]/8.))
            faces+=[(t[0],t[2],t[1])for t in bottom]
        else:faces+=bottom_builder(polygon,deck_patches,roof,painter)
        attachments=_attachment_lines(graded,deck)
        for part in _components(polygon):
            part=orient(part,sign=1.)
            for ring in [part.exterior,*part.interiors]:
                coords=list(ring.coords)
                for initial,final in zip(coords,coords[1:]):
                    line=LineString([initial,final])
                    cuts=[0.,1.]
                    for boundary in [*boundary_layers,patch_mask.boundary]:
                        intersections=line.intersection(boundary)
                        items=list(intersections.geoms)if hasattr(intersections,"geoms")else[intersections]
                        for item in items:
                            if item.geom_type=="Point":cuts.append(line.project(item,normalized=True))
                    ordered=sorted(set(round(value,13)for value in cuts))
                    for t0,t1 in zip(ordered,ordered[1:]):
                        first=tuple(initial[k]+t0*(final[k]-initial[k])for k in range(2))
                        last=tuple(initial[k]+t1*(final[k]-initial[k])for k in range(2))
                        if math.dist(first,last)<1e-8:continue
                        midpoint=Point((first[0]+last[0])/2,(first[1]+last[1])/2)
                        if patch_mask.buffer(1e-8).covers(midpoint):continue
                        if any(part.distance(Point((first[0]+last[0])/2,(first[1]+last[1])/2))<1e-7 for part in attachments):continue
                        first_height=flat_height(first)
                        last_height=flat_height(last)
                        points=[_vertex(*p,h,(p[0]/8.,h/8.),painter.role("body"))
                                for p,h in ((first,first_height),(last,last_height),(last,roof-DEPTH),(first,roof-DEPTH))]
                        outward=(last[1]-first[1],0.,last[0]-first[0])
                        faces+=_quad(points,outward)
        for patch in deck_patches:
            if abs(patch["height"]-roof)<1e-7:continue
            for part in _components(patch["geometry"]):
                for first,last in zip(part.exterior.coords,list(part.exterior.coords)[1:]):
                    midpoint=Point((first[0]+last[0])/2,(first[1]+last[1])/2)
                    if polygon.boundary.distance(midpoint)<1e-7:continue
                    # A floor datum step is external only on exposed
                    # asphalt. Beneath a raised rail, the preserved native
                    # faces and the raised-profile join already own the skin.
                    # Keep the low wall on the exposed native pavement
                    # ledge even where the coreward generic rail is wider.
                    masks=[]if barrier_masks is None else[barrier_masks[deck]]
                    visible=LineString([first,last]).difference(shapely.union_all(masks))
                    parts=[visible]if visible.geom_type=="LineString"else list(getattr(visible,"geoms",()))
                    for line in parts:
                        if line.geom_type!="LineString"or line.length<1e-8:continue
                        for a,b in _exposed_step_intervals(line,deck,step_profiles):
                            faces+=_quad([_vertex(*p,h,(p[0]/8.,h/8.),painter.role("body"))
                                          for p,h in((a,patch["height"]),(b,patch["height"]),(b,roof),(a,roof))])
    return faces


def _exposed_step_intervals(line,deck,profiles):
    a,b=np.asarray(line.coords[0]),np.asarray(line.coords[-1]);delta=b-a
    length2=float(delta@delta);intervals=[(0.,1.)]
    for record in profiles:
        if record["deck"]!=deck:continue
        normal=np.asarray(record["normal"])
        # Match the existing measured finite-native section bound; do not
        # widen a barrier footprint or permit a new opening in the skin.
        if max(abs(float(np.array([p[0],0.,-p[1]])@normal)-record["station"])for p in(a,b))>2e-6:continue
        values=[float((np.array([p[0],-p[2]])-a)@delta/length2)for p in record["points"]]
        lo,hi=max(0.,min(values)),min(1.,max(values))
        if hi<=lo:continue
        remaining=[]
        for first,last in intervals:
            if lo>first:remaining.append((first,min(last,lo)))
            if hi<last:remaining.append((max(first,hi),last))
        intervals=[(first,last)for first,last in remaining if last-first>1e-10]
    return [(a+first*delta,a+last*delta)for first,last in intervals]


def _mark_end_windows(triangles,source_stations,station,painter):
    for triangle in triangles:
        xy=[(p[0],-p[2])for p in triangle]
        field=np.linalg.solve(np.array([[*p,1.]for p in xy]),np.array([source_stations[id(p)]for p in triangle]))
        windows=[]
        for deck,lo,hi in(("lower",station[0],station[0]+5.),("upper",station[-1]-5.,station[-1])):
            window=_positive_polygon(xy,field-np.array([0.,0.,lo]))
            window=window.intersection(_positive_polygon(xy,np.array([0.,0.,hi])-field))
            windows.append((deck,window))
        painter.graded_end_windows[id(triangle)]=windows


def _graded_faces(graded,painter,*,reverse_traffic=False):
    faces=[]
    for road in graded:
        pts,normals,station=road["points"],road["normals"],road["station"]
        paint = painter.marking_fields.get(road["id"])
        for index,(first,last)in enumerate(zip(pts,pts[1:])):
            roof_first=first[2]+pavement_datum(first[2]);roof_last=last[2]+pavement_datum(last[2])
            outer_low=road["rail_low"][index:index+2]
            outer_high=road["rail_high"][index:index+2]
            inner_low=outer_low+BARRIER[-1][0]*road["inward_low"][index:index+2]
            inner_high=outer_high+BARRIER[-1][0]*road["inward_high"][index:index+2]
            for low,high in ((inner_low,pts[index:index+2,:2]),(pts[index:index+2,:2],inner_high)):
                polygon=[]
                source_stations={}
                for endpoint,xy in((0,low[0]),(1,low[1]),(1,high[1]),(0,high[0])):
                    p,n,s=pts[index+endpoint],normals[index+endpoint],station[index+endpoint]
                    offset=float((xy-p[:2])@n/(n@n))
                    uv=(.5-offset/16.,(road["full_length"]-s)/16.)if reverse_traffic else(.5+offset/16.,s/16.)
                    if paint is not None:
                        uv = paint(xy, uv)
                    vertex=_vertex(*xy,p[2]+pavement_datum(p[2]),uv,painter.role("pavement"))
                    polygon.append(vertex);source_stations[id(vertex)]=s
                triangles=_quad(polygon,(0.,1.,0.));_mark_end_windows(triangles,source_stations,station,painter)
                faces+=triangles
            for low,high in((outer_low,pts[index:index+2,:2]),(pts[index:index+2,:2],outer_high)):
                bottom=[]
                for endpoint,xy in((0,low[0]),(1,low[1]),(1,high[1]),(0,high[0])):
                    p,n,s=pts[index+endpoint],normals[index+endpoint],station[index+endpoint]
                    offset=float((xy-p[:2])@n/(n@n))
                    bottom.append(_vertex(*xy,p[2]+pavement_datum(p[2])-DEPTH,(s/8.,offset/3.),painter.role("body")))
                faces+=_quad(bottom,(0.,-1.,0.))
            for side in(-1,1):
                rails=road["rail_low"]if side==-1 else road["rail_high"]
                inward=road["inward_low"]if side==-1 else road["inward_high"]
                a,b=rails[index:index+2]
                outward=(side*normals[index][0],0.,-side*normals[index][1])
                faces+=_quad([_vertex(*p,h,(s/8.,h/8.),painter.role("body"))
                              for p,h,s in ((a,roof_first,station[index]),(b,roof_last,station[index+1]),
                                            (b,roof_last-DEPTH,station[index+1]),(a,roof_first-DEPTH,station[index]))],outward)
                inward_first,inward_last=inward[index:index+2]
                source_stations={}
                barrier_faces=_barrier_segment(a,b,(roof_first,roof_last),painter.role("barrier"),inward_first,inward_last,
                                                (station[index],station[index+1]),source_stations)
                _mark_end_windows(barrier_faces,source_stations,station,painter)
                faces+=barrier_faces
    return faces


def _affine_triangle(triangle):
    return np.linalg.solve(np.array([[p[0],-p[2],1.]for p in triangle]),
                           np.array([[p[1],p[3],p[4]]for p in triangle]))


def _positive_polygon(points,field):
    output=[]
    first=np.asarray(points[-1]);a=float(np.r_[first,1.]@field)
    for point in points:
        last=np.asarray(point);b=float(np.r_[last,1.]@field)
        if (a>=0.)!=(b>=0.):output.append(tuple(first+a/(a-b)*(last-first)))
        if b>=0.:output.append(tuple(last))
        first,a=last,b
    return Polygon(output)if len(output)>=3 else Polygon()


def _join_graded_barrier_tops(flat_faces,graded_faces,graded,painter):
    """Keep the finite upper envelope where a raised ramp meets its flat rail.

    Adjacent shoulders share a volume near a grade-end mouth. Their two
    independently triangulated raised tops must be united, rather than
    left crossing one another. Each retained fragment keeps its original
    affine height, material, and texture coordinates.
    """
    def records(faces):
        result=[]
        for index,triangle in enumerate(faces):
            if not painter.roles[round(triangle[0][5])].startswith(("barrier","pavement")):continue
            polygon=Polygon([(p[0],-p[2])for p in triangle])
            if polygon.area>1e-14:result.append((index,triangle,polygon,_affine_triangle(triangle)))
        return result
    first,second=records(flat_faces),records(graded_faces)
    tree=shapely.STRtree([row[2]for row in second])
    masks_flat=defaultdict(list);masks_graded=defaultdict(list)
    for i,triangle,polygon,field in first:
        for j in tree.query(polygon):
            k,other,footprint,coefficients=second[int(j)]
            # The two independent elevation decks remain separate solids.
            # Only the five-metre native-height end of this same graded
            # road is part of the corresponding flat rail union.
            deck="lower"if max(p[1]for p in triangle)<10. else"upper"
            window=next(region for label,region in painter.graded_end_windows[id(other)]if label==deck)
            overlap=polygon.intersection(footprint).intersection(window)
            if overlap.area<1e-13:continue
            delta=coefficients[:,0]-field[:,0]
            if np.max(np.abs(delta))<1e-12:
                masks_graded[k].append(overlap);continue
            above=_positive_polygon(list(footprint.exterior.coords)[:3],delta).intersection(polygon).intersection(window)
            below=_positive_polygon(list(polygon.exterior.coords)[:3],-delta).intersection(footprint).intersection(window)
            if above.area>1e-13:masks_flat[i].append(above)
            if below.area>1e-13:masks_graded[k].append(below)
    def trim(faces,masks):
        result=[]
        for i,triangle in enumerate(faces):
            if i not in masks:result.append(triangle);continue
            region=Polygon([(p[0],-p[2])for p in triangle]).difference(shapely.union_all(masks[i]))
            field=_affine_triangle(triangle);code=triangle[0][5]
            for part in _components(region):
                for shape in shapely.constrained_delaunay_triangles(part).geoms:
                    points=[]
                    for e,n in list(shape.exterior.coords)[:3]:
                        h,u,v=np.array([e,n,1.])@field
                        points.append(_vertex(e,n,h,(u,v),code))
                    result+=_quad(points,(0.,1.,0.))
        return result
    return trim(flat_faces,masks_flat),trim(graded_faces,masks_graded)


def _native_mouth_caps(flat,context,painter,*,native_source=native_models,floor_matched_underside=False):
    """Close the authored underside at finite diagonal native roof mouths.

    Original NAM roads have open undersides. These new concrete end caps
    are authored faces below the roof, rather than altered native profiles.
    Every cap interval is shared by the measured finite native roof edge
    and the actual flat-deck perimeter; no whole-plane cap is introduced.
    """
    faces,records=[],[]
    for arm in("A","B"):
        for deck in("upper","lower"):
            nominal=15. if deck=="upper"else 7.5
            underside=nominal+pavement_datum(nominal)-DEPTH
            for group in native_source.visible_native_end_sections(context,arm,deck):
                if group["role"]!="pavement":continue
                desired=tuple(-value for value in group["plane_normal_xyz"])
                for segment in group["segments"]:
                    first,last=segment["points"]
                    if floor_matched_underside:underside=first[1]-DEPTH
                    a,b=np.array([first[0],-first[2]]),np.array([last[0],-last[2]])
                    delta=b-a;length2=float(delta@delta)
                    for part in _components(flat[deck]):
                        for ring in(part.exterior,*part.interiors):
                            for p,q in zip(ring.coords,list(ring.coords)[1:]):
                                p,q=np.asarray(p),np.asarray(q)
                                t,u=float((p-a)@delta/length2),float((q-a)@delta/length2)
                                if max(np.linalg.norm(p-a-t*delta),np.linalg.norm(q-a-u*delta))>1e-7:continue
                                lo,hi=max(0.,min(t,u)),min(1.,max(t,u))
                                if hi-lo<1e-8:continue
                                points=[]
                                for f,lower in((lo,False),(hi,False),(hi,True),(lo,True)):
                                    xy=a+f*delta
                                    h=underside if lower else first[1]+f*(last[1]-first[1])
                                    points.append(_vertex(*xy,h,(float(xy[0])/8.,h/8.),painter.role("body")))
                                faces+=_quad(points,desired)
                                records.append({"arm":arm,"deck":deck,"native_owner":group["kind"],
                                    "top_endpoints_enh_m":[[points[i][0],-points[i][2],points[i][1]]for i in(0,1)],
                                    "underside_height_m":underside,
                                    "plane_normal_xyz":list(group["plane_normal_xyz"]),
                                    "plane_station_m":group["plane_station_m"]})
    return faces,records


def _peer_step_profiles(context,*,native_source=native_models,sockets=SOCKETS,low_floor_kind="peer"):
    records=[]
    for arm in("A","B"):
        direction=np.array([sockets[arm]["inward"][0],0.,-sockets[arm]["inward"][1]])
        for deck in("upper","lower"):
            for group in native_source.native_end_sections(context,arm,deck):
                if group["role"]!="barrier"or group["kind"]!=low_floor_kind:continue
                normal=np.asarray(group["plane_normal_xyz"])
                records.append({"deck":deck,"normal":normal,
                    "station":group["plane_station_m"]+float(3.*direction@normal),
                    "points":[np.asarray(p[:3])+3.*direction for segment in group["segments"]for p in segment["points"]]})
    return records


def _peer_raised_mouth_caps(native_faces,context,painter,*,native_source=native_models,sockets=SOCKETS,low_floor_kind="peer"):
    """Close the source peer's under-rail floor slit at its finite mouth."""
    faces=[]
    for arm in("A","B"):
        direction=np.array(sockets[arm]["inward"]);axis=np.array([-direction[1],direction[0]])
        for deck in("upper","lower"):
            base=15. if deck=="upper"else 7.5
            for group in native_source.native_end_sections(context,arm,deck):
                if group["role"]!="barrier"or group["kind"]!=low_floor_kind:continue
                normal=group["plane_normal_xyz"];station=group["plane_station_m"]
                lateral=[float(np.array([p[0],-p[2]])@axis)for segment in group["segments"]for p in segment["points"]]
                segments=_section_top_segments(native_faces,normal,station,axis,base,2e-6)
                cuts=_section_cuts([segments],min(lateral),max(lateral))
                for a,b in zip(cuts,cuts[1:]):
                    if b-a<1e-8 or _section_height(segments,(a+b)/2)is None:continue
                    high=[_section_height(segments,t)for t in(a,b)]
                    if any(h is None for h in high):continue
                    phases=[_section_phase(segments,t)for t in(a,b,b,a)]
                    faces+=_section_wall(a,b,[base,base],high,normal,station,axis,painter,
                                         tuple(-value for value in normal),phases)
    return faces


def _section_top_segments(faces,normal,station,axis,base,tolerance=1e-8):
    result=[]
    for triangle in faces:
        if max(p[1]for p in triangle)<base-1e-5 or min(p[1]for p in triangle)>base+1.4:continue
        a,b,c=np.asarray(triangle)[:,:3]
        if np.cross(b-a,c-a)[1]<=1e-12:continue
        for first,last in native_models._oblique_segments(triangle,normal,station,tolerance):
            t,u=float(np.array([first[0],-first[2]])@axis),float(np.array([last[0],-last[2]])@axis)
            if abs(t-u)>1e-9:result.append((t,u,float(first[1]),float(last[1]),
                sum(first[i]*normal[i]for i in range(3)),sum(last[i]*normal[i]for i in range(3))))
    return result


def _section_cuts(groups,lo,hi):
    segments=[s for group in groups for s in group if max(s[:2])>=lo and min(s[:2])<=hi]
    cuts=[lo,hi,*[value for s in segments for value in s[:2]if lo<value<hi]]
    for i,segment in enumerate(segments):
        a,b,h,k=segment[:4]
        slope=(k-h)/(b-a);constant=h-a*slope
        for other_segment in segments[i+1:]:
            c,d,j,l=other_segment[:4]
            other=(l-j)/(d-c);offset=j-c*other
            if abs(slope-other)<1e-14:continue
            point=(offset-constant)/(slope-other)
            if max(lo,min(a,b),min(c,d))<point<min(hi,max(a,b),max(c,d)):cuts.append(point)
    return sorted(set(round(float(value),12)for value in cuts))


def _section_height(segments,point):
    candidates=[s[2]+(point-s[0])/(s[1]-s[0])*(s[3]-s[2])for s in segments if min(s[:2])-1e-8<=point<=max(s[:2])+1e-8]
    return max(candidates)if candidates else None


def _section_phase(segments,point):
    candidates=[(s[2]+(point-s[0])/(s[1]-s[0])*(s[3]-s[2]),
                 s[4]+(point-s[0])/(s[1]-s[0])*(s[5]-s[4]))for s in segments
                if min(s[:2])-1e-8<=point<=max(s[:2])+1e-8]
    return max(candidates,key=lambda row:row[0])[1]


def _section_wall(lo,hi,low,high,normal,station,axis,painter,outward,phases=None):
    # The vertical section's horizontal basis is orthonormal up to the
    # measured float phase of the native cap plane; solve it explicitly.
    frame=np.array([[normal[0],-normal[2]],[axis[0],axis[1]]])
    points=[]
    for index,(t,h)in enumerate(((lo,low[0]),(hi,low[1]),(hi,high[1]),(lo,high[0]))):
        xy=np.linalg.solve(frame,np.array([station if phases is None else phases[index],t]))
        points.append(_vertex(*xy,h,(t/8.,h/8.),painter.role("body")))
    return _quad(points,outward)


def _native_inner_profile_joins(native_faces,flat_faces,context,painter,*,native_source=native_models,sockets=SOCKETS,core_north_interval=(-7.999000072479248,8.)):
    """Close the measured millimetre phase step at each diagonal inner rail.

    The native 302 pavement and its body/barrier have different horizontal
    phases. This finite vertical section joins the two actual raised top
    profiles at the end of the exact three-metre collar; it does not move
    either profile or copy a native-material exception onto authored faces.
    """
    faces=[]
    sections=[]
    for arm in("A","B"):
        direction=np.array(sockets[arm]["inward"])
        axis=np.array([-direction[1],direction[0]])
        for deck in("upper","lower"):
            base=15. if deck=="upper"else 7.5
            for group in native_source.native_end_sections(context,arm,deck):
                if group["role"]!="barrier":continue
                normal=group["plane_normal_xyz"]
                station=group["plane_station_m"]+3.*sum(normal[i]*v for i,v in enumerate((direction[0],0.,-direction[1])))
                lateral=[float(np.array([p[0],-p[2]])@axis)for segment in group["segments"]for p in segment["points"]]
                lo,hi=min(lateral)-.003,max(lateral)+.003
                sections.append((base,normal,station,axis,lo,hi))
    minimum=min(group["bounded_east_interval_m"][0]for group in native_source.retained_core_collar_faces(context,"C",3.))
    for base in(7.5,15.):sections.append((base,(-1.,0.,0.),-minimum,np.array([0.,1.]),*core_north_interval))
    for base,normal,station,axis,lo,hi in sections:
        roof=base+pavement_datum(base)
        original=_section_top_segments(native_faces,normal,station,axis,base,2e-6)
        authored=_section_top_segments(flat_faces,normal,station,axis,base,2e-6)
        cuts=_section_cuts([original,authored,[(lo,hi,roof,roof,station,station)]],lo,hi)
        for a,b in zip(cuts,cuts[1:]):
            if b-a<1e-8:continue
            first=_section_height(original,(a+b)/2)
            last=_section_height(authored,(a+b)/2)
            if first is None or last is None or abs(first-last)<1e-8:continue
            # The existing flat-pavement datum-step wall already
            # closes the region below this roof. Add only the
            # genuinely raised rail-profile difference above it.
            if max(first,last)<=roof+1e-8:continue
            h=[_section_height(original,t)for t in(a,b)]
            k=[_section_height(authored,t)for t in(a,b)]
            if any(value is None for value in h+k):continue
            h=[max(roof,value)for value in h];k=[max(roof,value)for value in k]
            outward=normal if first>last else tuple(-v for v in normal)
            low_segments,high_segments=(authored,original)if first>last else(original,authored)
            phases=[_section_phase(low_segments,a),_section_phase(low_segments,b),
                    _section_phase(high_segments,b),_section_phase(high_segments,a)]
            faces+=_section_wall(a,b,k if first>last else h,h if first>last else k,
                                 normal,station,axis,painter,outward,phases)
    return faces


def _peer_outer_walls(context,painter,*,native_source=native_models,sockets=SOCKETS,low_floor_kind="peer",floor_matched_underside=False):
    """Close actual peer pavement perimeters while retaining native sidewalls.

    The original 302 sidewall lies approximately 1.415 mm inward of its
    pavement edge. These exact finite new walls close the full authored
    deck to its underside; the preserved source wall remains in the DAT.
    """
    faces=[]
    for arm in("A","B"):
        direction=np.array(sockets[arm]["inward"])
        normal=np.array([-direction[1],direction[0]])
        centre=np.array(sockets[arm]["point"])
        for deck in("upper","lower"):
            nominal=15. if deck=="upper"else 7.5
            bottom=nominal+pavement_datum(nominal)-DEPTH
            for group in native_source.native_end_sections(context,arm,deck):
                if group["role"]!="pavement"or group["kind"]!=low_floor_kind:continue
                vertices=[p for segment in group["segments"]for p in segment["points"]]
                p=max(vertices,key=lambda p:abs((np.array([p[0],-p[2]])-centre)@normal))
                if floor_matched_underside:bottom=p[1]-DEPTH
                first=np.array([p[0],-p[2]]);last=first+3.*direction
                side=np.sign((first-centre)@normal)
                outward=(side*normal[0],0.,-side*normal[1])
                faces+=_quad([_vertex(*xy,h,(float(xy@direction)/8.,h/8.),painter.role("body"))
                              for xy,h in((first,p[1]),(last,p[1]),(last,bottom),(first,bottom))],outward)
    return faces


def _core_owned_caps(native_faces,context,painter,*,native_source=native_models,east_boundary=56.,north_interval=(-7.999000072479248,8.),side_boundary=8.,side_sign=1.):
    """Close the authored C slab at E56/N8, below its literal native top."""
    groups=native_source.retained_core_collar_faces(context,"C",3.)
    minimum=min(group["bounded_east_interval_m"][0]for group in groups)
    faces=[]
    for deck in("upper","lower"):
        base=15. if deck=="upper"else 7.5
        bottom=base+pavement_datum(base)-DEPTH
        for normal,station,axis,lo,hi in(((1.,0.,0.),east_boundary,np.array([0.,1.]),*north_interval),
                                        ((0.,0.,-side_sign),side_sign*side_boundary,np.array([1.,0.]),minimum,east_boundary)):
            segments=_section_top_segments(native_faces,normal,station,axis,base)
            cuts=_section_cuts([segments],lo,hi)
            for a,b in zip(cuts,cuts[1:]):
                if b-a<1e-8 or _section_height(segments,(a+b)/2)is None:continue
                heights=[_section_height(segments,t)for t in(a,b)]
                if any(h is None for h in heights):continue
                faces+=_section_wall(a,b,[bottom,bottom],heights,normal,station,axis,painter,normal)
    return faces,minimum


def _support_solids(painter,*,subject=SUBJECT):
    """Compile the reviewed support contract, without selecting new placements."""
    source=subject/"checks/support-solids.jsonc"
    contract=jsonc.loads(source.read_text())
    design_sha=hashlib.sha256((subject/"evidence/design-geometry.jsonc").read_bytes()).hexdigest()
    _require(contract["source_design_sha256"]==design_sha,"Support contract belongs to another route design")
    records=deepcopy(contract["supports"])
    _require(len({record["id"]for record in records})==len(records),"Duplicate declared support identifier")
    faces=[]
    for record in records:
        corners=record["corners_en_m"]
        bottom,ceiling=record["bottom_m"],record["top_m"]
        _require(len(corners)==4 and Polygon(corners).is_valid and ceiling>bottom,
                 "Invalid declared support prism")
        code=painter.role(record["id"])
        vertices=[_vertex(*xy,h,(xy[0]/8.,(xy[1]+h)/8.),code)for h in(bottom,ceiling)for xy in corners]
        centre=np.mean(np.asarray([v[:3]for v in vertices]),axis=0)
        for ids in((0,1,2,3),(4,7,6,5),(0,4,5,1),(1,5,6,2),(2,6,7,3),(3,7,4,0)):
            quad=[vertices[i]for i in ids]
            outward=np.mean(np.asarray([v[:3]for v in quad]),axis=0)-centre
            faces+=_quad(quad,outward)
    _require(records,"Y junction requires declared supporting solids")
    return faces,records


def world_geometry(context):
    """Return the complete physical world before module selection or allocation."""
    native_inputs=(("dd_rhw",0x57530900),("dd_rhw",0x57530000),("dd_rhw",0x57530200),
                   ("dd_rhw",0x5753A380),("mis",0x57722000))
    fingerprints=[]
    for label,donor in native_inputs:
        raw=context.get(label,{}).get((*S3D,donor))
        fingerprints.append(None if raw is None else hashlib.sha256(raw).hexdigest())
    key=tuple(fingerprints)+tuple(hashlib.sha256((SUBJECT/path).read_bytes()).hexdigest()
                                  for path in("evidence/design-geometry.jsonc","checks/support-solids.jsonc"))
    if key in _WORLD_CACHE:return _WORLD_CACHE[key]
    profiles=_native_profiles(context);painter=_Painter(context,profiles)
    flat,graded,roads,reference,parent_mouths=_unions(profiles)
    painter.marking_fields = ribbon_markings(roads, profiles, SOCKETS, BARRIER[-1][0])
    native_faces,patches,native_original,collar_data,barrier_masks=_native_collars(context,painter)
    core_caps,core_minimum=_core_owned_caps(native_faces,context,painter)
    flat={deck:shapely.union_all([polygon.difference(native_original[deck]),
                                *[p["geometry"]for p in patches if p["deck"]==deck]],grid_size=1e-9)
          for deck,polygon in flat.items()}
    # Only literal original C faces retain the north/east millimetre
    # overhang. Newly authored slab geometry closes inside the city owner.
    flat={deck:polygon.difference(box(43.,8.,56.,100.))for deck,polygon in flat.items()}
    flat_faces=_flat_faces(flat,graded,roads,profiles,painter,reference,patches,barrier_masks,_peer_step_profiles(context),parent_mouths)
    graded_faces=_graded_faces(graded,painter)
    flat_faces,graded_faces=_join_graded_barrier_tops(flat_faces,graded_faces,graded,painter)
    profile_joins=_native_inner_profile_joins(native_faces,flat_faces,context,painter)
    peer_walls=_peer_outer_walls(context,painter)
    faces=flat_faces+graded_faces+native_faces+profile_joins+core_caps+peer_walls
    mouth_faces,mouth_records=_native_mouth_caps(flat,context,painter);faces+=mouth_faces
    raised_mouth_caps=_peer_raised_mouth_caps(native_faces,context,painter);faces+=raised_mouth_caps
    supports,records=_support_solids(painter);faces+=supports
    partition=orthogonal_transition.partition_triangles(faces)
    paths=ramp_paths.slice_routes(source_routes())
    # The measured +1mm native C datum projects into its unchanged native cell.
    for cell in list(partition):
        if cell==(3,0):continue
        keep=[]
        for triangle in partition[cell]:
            if painter.roles[round(triangle[0][5])].endswith(("-retained-contact","-retained-core-collar")):
                dx,dz=16*(cell[0]-3),16*cell[1]
                partition.setdefault((3,0),[]).append(tuple((p[0]+dx,p[1],p[2]+dz,*p[3:])for p in triangle))
            else:keep.append(triangle)
        if keep:partition[cell]=keep
        else:partition.pop(cell)
    reserved={tuple(c)for cells in native_models.reserved_native_cells(2).values()for c in cells}
    for cell in list(set(partition)&reserved):
        for triangle in partition.pop(cell):
            hosts=[]
            for axis,side,delta in((0,-8.,(-1,0)),(0,8.,(1,0)),(2,-8.,(0,-1)),(2,8.,(0,1))):
                host=cell[0]+delta[0],cell[1]+delta[1]
                if host not in reserved and host in partition and all(abs(p[axis]-side)<1e-9 for p in triangle):hosts.append(host)
            _require(hosts,"An authored Y face enters a reserved native traffic cell")
            host=hosts[0];dx,dz=16*(cell[0]-host[0]),16*(cell[1]-host[1])
            partition[host].append(tuple((p[0]+dx,p[1],p[2]+dz,*p[3:])for p in triangle))
    _require(not set(record["outside"]for record in SOCKETS.values())&set(partition),"Physical Y model overwrites an exterior native socket")
    _require(set(paths)<=set(partition),"A routed city cell has no pavement model")
    native_models.check_reserved_native_corridor(partition)
    result={"triangles":faces,"tiles":partition,"paths":paths,"roles":tuple(painter.roles),
            "materials":painter.materials,"painter":painter,"template":profiles["C","upper"]["model"],
            "supports":records,"flat_polygons":flat,"graded":graded,
            "native_collars":collar_data,
            "engineering":{"shapely_version":shapely.__version__,"geos_version":shapely.geos_version_string,
                           "pavement_datum_lower_m":DATUM_LOWER,"pavement_datum_upper_m":DATUM_UPPER,
                           "standard_deck_depth_m":DEPTH,
                           "native_peer_shoulder_body_depth_m":{"upper":1.-DATUM_UPPER,"lower":1.-DATUM_LOWER},
                           "single_lane_deck_width_m":WIDTH,
                           "single_lane_asphalt_width_m":WIDTH-2*BARRIER[-1][0],
                           "barrier_inner_base_inset_m":BARRIER[-1][0],
                           "barrier_cross_profile_inset_rise_m":[list(pair)for pair in BARRIER],
                           "graded_inner_shoulder_tapers":_taper_engineering(roads),
                           "native_physical_profile_measurement":"Width and centre bounds use posed pavement XYZ vertices; native UV coefficients supply textures and identify/orient peer foot shims.",
                           "flat_asphalt_texture_domains":painter.flat_texture_domains,
                           "flat_asphalt_uv_method":"Disjoint fixed-owner native fans and finite route-ribbon texture fields; copied native collar faces are unchanged.",
                           "support_contract_sha256":key[-1],
                           "authored_native_mouth_caps":mouth_records,
                           "authored_peer_raised_mouth_cap_triangles":len(raised_mouth_caps),
                           "authored_inner_profile_join_triangles":len(profile_joins),
                           "authored_peer_outer_wall_triangles":len(peer_walls),
                           "authored_core_cap_triangles":len(core_caps),
                           "authored_core_cap_planes_en_m":{"east":56.,"north":8.,"minimum_east":core_minimum},
                           "graded_surface_union_scope":"Finite affine pavement/barrier upper envelope against the same flat deck within five horizontal metres of each grade end.",
                           "native_profile_resources":["57530900","57530200","57530000"]}}
    _WORLD_CACHE.clear()
    _WORLD_CACHE[key]=result
    return result
