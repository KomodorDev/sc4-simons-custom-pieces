"""Map authored ramp faces to measured NAM materials and continuous UVs.

Only native resource identities, fingerprints, and measurements live here.
The private audited NAM archives provide actual material bytes at build time;
their texture images stay in the installed NAM texture packs.
"""
from __future__ import annotations

from collections import defaultdict
from copy import deepcopy
import hashlib
import math

from scp.models import parse_s3d
from scp.track_paths import S3D

MIS_DONOR = 0x57722000
MIS_DONOR_SHA256 = "6736e259a2aeaeaf2f02f60b7b34c1782b4f8069957e31530260c072610bb1a5"
DD_DONOR = 0x5753A380
TEXTURES = {"highway": 0x5713000E, "ramp": 0x5712000E,
            "barrier": 0x5EB4BEE9, "concrete": 0x5EB4BEEE}
MATERIAL_SHA256 = {
    "highway": "307aba7786d4b4f11dbc499eb54f7d05d01a114001919b8a5f7d55970fbb64ca",
    "ramp": "ed1b4a35ab986ff74a56ac79a1a33f579c31bf9630e7bb2b79ad4a4d9b6739ca",
    "barrier": "d81e8d70e3ab9182adb393f2bc6a61608c70f8129cdb06631409a4b19c73e306",
    "concrete": "cf4e393b8ca3a2b3d0edba0f86bb197ddf82b65e85cf73cfa13ebd4d2a8c6f6e",
}


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def native_materials(context):
    """Read the pinned real slope's three materials and the DD deck material."""
    _require("mis" in context, "Native ramp appearance requires the audited MIS dependency")
    raw = context["mis"][*S3D, MIS_DONOR]
    _require(hashlib.sha256(raw).hexdigest() == MIS_DONOR_SHA256,
             "Native MIS slope donor changed; re-audit its materials and UVs")
    slope = parse_s3d(raw)
    dd = parse_s3d(context["dd_rhw"][*S3D, DD_DONOR])
    result = {}
    for role, model in (("highway", dd), ("ramp", slope),
                        ("barrier", slope), ("concrete", slope)):
        matches = [material for material in model["materials"]
                   if material["textures"] == [TEXTURES[role]]
                   and hashlib.sha256(material["raw"]).hexdigest() == MATERIAL_SHA256[role]]
        _require(matches, f"Native {role} material differs from the measured NAM donor")
        result[role] = deepcopy(matches[0])
    return result


def _connected_roads(roads):
    """Join directed touching fragments before assigning a texture coordinate.

    A ramp and its ground turn are one pavement corridor. Their exact shared
    mouth must not restart the longitudinal coordinate or choose a different
    transverse frame independently at each vertex of a face.
    """
    chains, seen = [], set()
    for road in roads:
        points = [tuple(point) for point in road['points']]
        identity = tuple(tuple(round(value,7) for value in point) for point in points)
        if identity not in seen:
            chains.append(points)
            seen.add(identity)
    while True:
        joins = [(a,b) for a,first in enumerate(chains) for b,last in enumerate(chains)
                 if a != b and math.dist(first[-1],last[0]) < 1e-6]
        if not joins:
            return chains
        # Branching paths require an explicit authored pavement owner. The
        # compact's four directed ramp/turn pairs each have one successor.
        _require(all(sum(first == a for first,_last in joins) == 1 for a,_b in joins)
                 and all(sum(last == b for _first,last in joins) == 1 for _a,b in joins),
                 'Ambiguous directed pavement fragments at a texture join')
        a,b = joins[0]
        combined = chains[a]+chains[b][1:]
        chains = [chain for index,chain in enumerate(chains) if index not in (a,b)]+[combined]


class NativeRoadPainter:
    """Keep a route's texture phase across tile cuts and component boundaries.

    MIS donor 57722000 maps 16 m of plan length to one texture repeat and its
    12 m-wide roadway to U=0.125..0.875. The compact authored road uses the
    central U=0.3125..0.6875 strip, preserving the native marking scale on
    its explicitly narrower 6 m width.
    Native barrier and underside materials retain their independent flags.
    """

    def __init__(self, context, roads):
        self.materials = native_materials(context)
        self.buckets, self.cache = defaultdict(list), {}
        self.segments, self.road_segments = [], defaultdict(list)
        for road_id,points in enumerate(_connected_roads(roads)):
            distance = 0.0
            for first, last in zip(points, points[1:]):
                dx, dy = last[0]-first[0], last[1]-first[1]
                length = math.hypot(dx, dy)
                if length < 1e-9:
                    continue
                segment = (first, last, distance, length, dx/length, dy/length, road_id)
                index = len(self.segments)
                self.segments.append(segment)
                self.road_segments[road_id].append(index)
                for column in range(math.floor((min(first[0], last[0])-8)/16),
                                    math.floor((max(first[0], last[0])+8)/16)+1):
                    for row in range(math.floor((min(first[1], last[1])-8)/16),
                                     math.floor((max(first[1], last[1])+8)/16)+1):
                        self.buckets[column, row].append(index)
                distance += length
        _require(self.segments, "Native ramp UVs require actual road polylines")

    def _frame(self, point, road_id=None):
        identity = tuple(round(v, 7) for v in point),road_id
        if identity in self.cache:
            return self.cache[identity]
        candidates = self.buckets.get((math.floor(point[0]/16), math.floor(point[1]/16)), ())
        if road_id is not None:
            candidates = [index for index in candidates if self.segments[index][-1] == road_id]
        candidates = candidates or (range(len(self.segments)) if road_id is None else self.road_segments[road_id])
        nearest = None
        for index in candidates:
            first, last, distance, length, tx, ty,owner = self.segments[index]
            along = min(length, max(0.0, (point[0]-first[0])*tx+(point[1]-first[1])*ty))
            fraction = along/length
            east, north = first[0]+along*tx, first[1]+along*ty
            height = first[2]+fraction*(last[2]-first[2])
            score = (point[0]-east)**2+(point[1]-north)**2+4*(point[2]-height)**2
            if nearest is None or score < nearest[0]:
                lateral = -(point[0]-east)*ty+(point[1]-north)*tx
                nearest = score, distance+along, lateral, height,owner
        self.cache[identity] = nearest[1:]
        return nearest[1:]

    def texture_triangles(self, triangles):
        """Sample curved UV fields inside long, flat ground-apron faces.

        Long rectangles are a compact physical pavement representation, but
        corner-only UVs cannot represent a turning wheel track inside them.
        Exact edge midpoints subdivide only ground asphalt until every edge
        is at most one metre. Every new point lies on the original triangle;
        its plane, area, boundary, winding, and city ownership stay unchanged.
        Binary source coordinates remain exactly representable in float32.
        """
        for original in triangles:
            ground = all(abs(p[1]) < 1e-8 and abs(p[3]-.125) < 1e-8 for p in original)
            if not ground:
                yield original
                continue
            pending = [original]
            while pending:
                face = pending.pop()
                lengths = [sum((face[a][axis]-face[b][axis])**2 for axis in (0,2))
                           for a,b in ((0,1),(1,2),(2,0))]
                longest = max(range(3),key=lengths.__getitem__)
                if lengths[longest] <= 1.0+1e-12:
                    yield face
                    continue
                a,b = ((0,1),(1,2),(2,0))[longest]
                c = 3-a-b
                midpoint = tuple((first+last)/2 for first,last in zip(face[a],face[b]))
                pending.append((face[a],midpoint,face[c]))
                pending.append((midpoint,face[b],face[c]))

    def paint(self, triangle, cell=(0, 0)):
        """Return (material role, XYZUV triangle), omitting old paint overlays."""
        semantic = triangle[0][3]
        _require(all(abs(p[3]-semantic) < 1e-7 for p in triangle),
                 "Road face lost its semantic material before native texturing")
        if abs(semantic-0.625) < 1e-7 or abs(semantic-0.875) < 1e-7:
            # The native MIS texture already paints its yellow and white edges.
            return None
        world = [(p[0]+16*cell[0], -p[2]-16*cell[1], p[1]) for p in triangle]
        from .slip_lanes import WHITE
        if abs(semantic-WHITE) < 1e-7:
            # The measured continuous white DD edge is safely inside texel
            # centres 27..28; preserve a spatial longitudinal coordinate.
            painted = []
            for point,global_point in zip(triangle,world):
                u = .21484375+.0078125*min(1.,max(0.,point[4]))
                v = (global_point[0]+global_point[1])/(16.*math.sqrt(2.))
                painted.append((*point[:3],u,v))
            return 'highway',tuple(painted)
        centroid = tuple(sum(p[axis] for p in world)/3 for axis in range(3))
        owner = self._frame(centroid)[3]
        frames = [self._frame(p,owner)[:3] for p in world]
        if abs(semantic-0.125) < 1e-7:
            # Keep one authentic MIS pavement strip over the complete authored
            # road. Retained native mainline faces keep their original DD
            # material; arbitrary per-triangle DD crops make dark rectangles.
            role = "ramp"
            painted = []
            for point, world_point, (distance, lateral, _height) in zip(triangle, world, frames):
                across = min(1.0, max(0.0, lateral/6+0.5))
                # Ground aprons join a narrower turn into native Avenue
                # pavement. Sampling the MIS edge lines there stretches
                # yellow/white paint across the joined carriageway. Preserve
                # spatial native asphalt UVs, while smoothly ending markings
                # over the same 1.5 m height range as the concrete barriers.
                marking = min(1.0,max(0.0,world_point[2]/1.5))
                raised_u = .3125+.375*across
                ground_across = min(1.0,max(0.0,lateral/3.5+.5))
                ground_u = .375+.21875*ground_across
                u = ground_u+(raised_u-ground_u)*marking
                painted.append((*point[:3], u, distance/16))
            return role, tuple(painted)
        _require(abs(semantic-0.375) < 1e-7, "Unknown semantic road material")
        relative_heights = [p[2]-frame[2] for p, frame in zip(world, frames)]
        barrier = (any(height > 0.02 for height in relative_heights)
                   and max(relative_heights)-min(relative_heights) <= 1.5
                   and max(relative_heights) <= 1.5)
        role = "barrier" if barrier else "concrete"
        barrier_top = barrier and all(abs(relative/max(1e-7,min(1.0,frame[2]/1.5))-1.390625) < .03
                                      for relative,frame in zip(relative_heights,frames))
        painted = []
        for point, world_point, (distance, lateral, height) in zip(triangle, world, frames):
            relative = world_point[2]-height
            if barrier:
                if barrier_top:
                    inset = 3.0-abs(lateral)
                    v = .325+.3*min(1.0,max(0.0,(inset-.265625)/.296875))
                else:
                    normal_height = relative/max(1e-7,min(1.0,height/1.5))
                    if normal_height <= .328125:
                        v = 1-.2880359888076782*max(0.0,normal_height)/.328125
                    else:
                        v = .7119640111923218*max(0.0,(1.390625-normal_height)/1.0625)
                u = distance/16
            else:
                u, v = (world_point[0]-world_point[1])/16, world_point[2]/8
            painted.append((*point[:3], u, v))
        return role, tuple(painted)


def provenance():
    """Portable measured identities; native image payloads are never returned."""
    return {"mis_archive_filename": "RealHighway_MIS.dat", "mis_s3d_instance": f"{MIS_DONOR:08X}",
            "mis_s3d_sha256": MIS_DONOR_SHA256, "dd_s3d_instance": f"{DD_DONOR:08X}",
            "textures": {role: f"{iid:08X}" for role, iid in TEXTURES.items()},
            "material_sha256": dict(MATERIAL_SHA256), "native_texture_repeat_plan_m": 16.0,
            "native_mis_road_width_m": 12.0, "authored_compact_road_width_m": 6.0,
            "native_pavement_u_range": [0.125, 0.875],
            "authored_pavement_u_range": [0.3125, 0.6875],
            "ground_unmarked_pavement_u_range": [.375,.59375],
            "ground_unmarked_pavement_width_m": 3.5,
            "edge_marking_taper_height_m": 1.5,
            "ground_texture_triangle_maximum_edge_m": 1.0,
            "native_images_copied_into_piece": False}
