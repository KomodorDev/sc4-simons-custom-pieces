#!/usr/bin/env python3
"""Measure finite first-A native crops without importing a resource writer.

Original game archives stay private. The portable output contains only finite
joining lines, cropped numeric regions, affine fields, and parent identities.
It neither includes complete donor meshes nor approves a saved custom model.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT/'framework'))
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0, SourcePackages(ROOT))
from scp import jsonc
from scp.dbpf import decompress, entries, require
from scp_highway import diagonal_transition_native as native
from scp_highway import diagonal_transition_verify as design
from shapely.geometry import Polygon, box, mapping
from shapely.ops import unary_union

HEADER = ('// title: "Measured finite Alignment A native collar inputs"\n'
    '// summary: "Bind independently cropped source interfaces and affine fields to original native resource hashes."\n'
    '// Used when: Reconstructing finite native collar, bridge, and texture expectations before or after allocation.\n'
    '// Read by: The independent diagonal PATH and model verifiers.\n'
    '// Updated by: domains/highway/tools/measure_diagonal_transition_collars.py with audited original inputs.\n'
    '// Affects: Source-only finite expectations; no saved-model, installation, or game approval.\n')


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def identity(value):
    return sha(json.dumps(value, separators=(',', ':')).encode())


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def positive(shape):
    if shape.geom_type == 'Polygon':
        return [shape] if shape.area > 0. else []
    return [p for member in getattr(shape, 'geoms', ()) for p in positive(member)]


def clip(points, coefficients, constant):
    """Exact-sign finite half-space clipping, carrying the original UV field."""
    if not points:
        return []
    result = []
    previous = points[-1]
    before = dot(previous[:3], coefficients)-constant
    for current in points:
        after = dot(current[:3], coefficients)-constant
        if (before >= 0.) != (after >= 0.):
            t = before/(before-after)
            result.append(tuple(a+t*(b-a) for a,b in zip(previous, current)))
        if after >= 0.:
            result.append(tuple(current))
        previous, before = current, after
    return result


def cross(a, b):
    return a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]


def area(points):
    if len(points) < 3:
        return 0.
    return sum(math.sqrt(dot(n, n))/2. for i in range(1, len(points)-1)
        for n in [cross(tuple(points[i][j]-points[0][j] for j in range(3)),
                       tuple(points[i+1][j]-points[0][j] for j in range(3)))])


def parent_record(group, index, parent, owner):
    return {'native_owner_kind': owner, 'native_tile_id': group['native_tile_id'],
        'pose': group['pose'], 'source_world_cell': group['world_cell'],
        'mesh_index': group['mesh_index'], 'face_index': index,
        'role': group['role'], 'deck': group['deck'],
        'source_model_sha256': group['source_model_sha256'],
        'source_parent_ENHUV_sha256': identity(parent),
        'source_material_sha256': sha(group['material']['raw']),
        'source_texture_ids': group['material']['textures'], **native.surface_fields(parent)}


def source_direction(parent, inward):
    """Measure the actual same-height longitudinal source edge, if one exists."""
    candidates = []
    for a,b in zip(parent, (*parent[1:], parent[0])):
        if a[2] != b[2]:
            continue
        vector = tuple(b[i]-a[i] for i in range(3))
        length = math.sqrt(dot(vector, vector))
        if not length:
            continue
        vector = tuple(v/length for v in vector)
        if dot(vector, inward) < 0.:
            vector = tuple(-v for v in vector)
        candidates.append((dot(vector, inward), vector))
    if candidates:
        alignment, vector = max(candidates, key=lambda item: item[0])
        if alignment > .999999:
            return vector, 'same-height-original-edge'
    normal = native.surface_fields(parent)['source_surface_plane_ENH']['normal']
    vector = tuple(inward[i]-dot(inward, normal)*normal[i] for i in range(3))
    length = math.sqrt(dot(vector, vector))
    require(length > 0., 'Native face has no longitudinal in-plane direction')
    return tuple(value/length for value in vector), 'inward-projected-into-parent-plane'


def field_point(fields, east, north):
    plane = fields['source_surface_plane_ENH']
    n = plane['normal']
    require(n[2] != 0., 'Ground source crop must have a nonvertical finite parent')
    height = (plane['constant']-n[0]*east-n[1]*north)/n[2]
    p = east, north, height
    return (*p, *(dot(fields['source_affine_UV_ENH'][name]['gradient_ENH'], p)
        +fields['source_affine_UV_ENH'][name]['offset'] for name in ('U', 'V')))


def ground_crop(parent, socket):
    points = clip(parent, (0., 1., 0.), socket.joining_coordinate)
    inward = (*socket.inward_en, 0.)
    return clip(points, tuple(-v for v in inward),
        -design.FLAT_ENVELOPE-dot((*socket.mouth_en, 0.), inward))


def inner_segments(shape, socket, fields):
    rows = []
    inward = socket.inward_en
    for polygon in positive(shape):
        for ring in (polygon.exterior, *polygon.interiors):
            vertices = list(ring.coords)[:-1]
            for a,b in zip(vertices, (*vertices[1:], vertices[0])):
                values = [dot((p[0]-socket.mouth_en[0], p[1]-socket.mouth_en[1]), inward)
                    -design.FLAT_ENVELOPE for p in (a,b)]
                if max(map(abs, values)) <= 5e-12 and math.dist(a,b) > 0.:
                    rows.append([field_point(fields,*a), field_point(fields,*b)])
    return rows


def vehicle_strip(first,last):
    dx,dy=last[0]-first[0],last[1]-first[1]
    run=math.hypot(dx,dy)
    require(run>0.,'Native vehicle chord is stationary')
    normal=(-dy/run,dx/run)
    return Polygon([(p[0]+sign*1.25*normal[0],p[1]+sign*1.25*normal[1])
        for p,sign in ((first,-1),(last,-1),(last,1),(first,1))])


def vehicle_roof_crops(context,socket,variant):
    """Finite original roof witnesses for native strips and custom end wedges."""
    strips=[]
    for route in native.source_paths(context,*socket.helper):
        strips.extend(vehicle_strip(a,b) for a,b in zip(route['points'],route['points'][1:]))
    native_cells=unary_union([box(16*c-8,-16*r-8,16*c+8,-16*r+8)
        for c,r in (socket.helper[2],socket.outward_peer[2])])
    components=('upper','lower') if socket.arm=='dd' else (socket.arm,)
    for deck in components:
        for lane in (0,1):
            stations=design.lane_stations(deck,lane,variant=variant)
            points=[design.lane_point(deck,lane,s,variant=variant) for s in stations]
            for a,b in zip(points,points[1:]):
                region=vehicle_strip(a,b).intersection(native_cells)
                if region.area>0.:
                    strips.append(region)
    roi=unary_union(strips)
    result=[]
    for owner,placement in (('helper',socket.helper),('outward-peer',socket.outward_peer)):
        for group in native.source_faces(context,*placement):
            if group['role']!='pavement':
                continue
            for index,parent in enumerate(group['triangles']):
                region=Polygon([p[:2] for p in parent]).intersection(roi)
                if region.area==0.:
                    continue
                result.append({**parent_record(group,index,parent,owner),
                    'component':group['deck'] if socket.arm=='dd' else socket.arm,
                    'arm':socket.arm,'finite_roi_EN':mapping(region),
                    'reference_usage':'vehicle-only; excluded from authored floor and closed-skin substitution'})
    return result


def measure(context):
    result = {'schema_version': 1, 'stage': 'frozen-measured-finite-native-crops',
        'alignment': 'a', 'complete_physical_acceptance': False,
        'scope': 'Finite source-only crops and affine fields, independently reconstructed from pinned original parents; no complete donor meshes.',
        'native_inputs_sha256': native.MEASURED_CONTRACT_SHA256,
        'source_resource_sha256': {'-'.join(f'{part:08x}' for part in key): value
            for key,value in native.RESOURCE_SHA256.items()},
        'laws': {'dd_reference': 'Original helper and outward-peer parents intersected with each independently declared custom city cell.',
            'dd_profile': 'Finite original forward edge continued in its actual same-height longitudinal edge direction, or the inward projection in its parent plane, to inward station C.',
            'ground_roi': 'Original finite parent intersect north >= socket cut and native inward station <= C; no station lower bound.',
            'ground_source_order': 'Coreward source, then opposite source tile with pose+2 in source cell+(1,0); subtract outside-helper/outward-peer crops, followed by all earlier retained finite parent regions.',
            'hosting': 'Each literal fragment is recut into every free owned city cell. Only a portion projecting into an explicit reserved helper may retain its original source host.',
            'source_bound': 'Finite original-parent shape, source plane, UV field, winding, material, pose, resource hash, and crop ROI remain mandatory.'},
        'variants': {}}
    for variant in design.PHASES:
        layout = design.candidate_layout_for_measurement(variant)
        cells = layout['world_cells']
        owned = unary_union([box(16*c-8, -16*r-8, 16*c+8, -16*r+8) for c,r in cells])
        sockets = native.socket_specs(variant)
        entry = {'world_cells': cells, 'world_origin_cell': layout['world_origin_cell'],
            'footprint': layout['footprint'], 'DD_profiles': [], 'DD_references': [], 'ground': {}}
        dd = sockets[0]
        inward = (*dd.inward_en, 0.)
        for group in native.socket_faces(context, 'dd', variant):
            for index,parent in enumerate(group['triangles']):
                record = parent_record(group,index,parent,group['native_owner_kind'])
                crops = []
                for c,r in cells:
                    points = list(parent)
                    for coefficients, constant in (((1.,0.,0.),16*c-8),((-1.,0.,0.),-16*c-8),
                            ((0.,1.,0.),-16*r-8),((0.,-1.,0.),16*r-8)):
                        points = clip(points,coefficients,constant)
                    if area(points) > 0.:
                        crops.append({'city_cell': (c,r), 'polygon_ENH': [p[:3] for p in points]})
                if crops:
                    entry['DD_references'].append({**record, 'finite_city_crops': crops})
        for profile in native.forward_profiles(context, 'dd', variant):
            parent = profile['parent_triangle']
            vector, method = source_direction(parent,inward)
            record = parent_record(profile,profile['face_index'],parent,profile['native_owner_kind'])
            edge = profile['points']
            phases = [dot(tuple(p[i]-(dd.mouth_en[i] if i<2 else 0.) for i in range(3)), inward) for p in edge]
            extension = [(design.FLAT_ENVELOPE-station)/dot(vector,inward) for station in phases]
            require(min(extension) >= 3.-1e-12, 'Measured DD continuation is shorter than three metres')
            finish = [tuple(p[i]+length*vector[i] for i in range(3)) for p,length in zip(edge,extension)]
            entry['DD_profiles'].append({**record, 'source_edge_ENHUV': edge,
                'source_longitudinal_unit_ENH': vector, 'source_longitudinal_method': method,
                'extension_by_endpoint_m': extension, 'inner_edge_ENH': finish,
                'inner_station_m': design.FLAT_ENVELOPE})
        for socket in sockets[1:]:
            references, literal, covered = [], [], []
            for owner,placement in (('helper',socket.helper),('outward-peer',socket.outward_peer)):
                for group in native.source_faces(context,*placement):
                    for index,parent in enumerate(group['triangles']):
                        points = ground_crop(parent,socket)
                        if len(points)<3:
                            continue
                        shape = Polygon([p[:2] for p in points])
                        if not shape.area:
                            continue
                        covered.append(shape)
                        references.append({**parent_record(group,index,parent,owner),
                            'finite_roi_EN': mapping(shape)})
            unavailable = unary_union(covered)
            target,pose,cell = socket.coreward_source
            opposite = 0x57030900 if target==0x57030200 else 0x57030200
            placements = (socket.coreward_source, (opposite,(pose+2)%4,(cell[0]+1,cell[1])))
            for placement in placements:
                for group in native.source_faces(context,*placement):
                    for index,parent in enumerate(group['triangles']):
                        points = ground_crop(parent,socket)
                        if len(points)<3:
                            continue
                        shape = Polygon([p[:2] for p in points]).difference(unavailable)
                        if not shape.area:
                            continue
                        record = parent_record(group,index,parent,'literal-coreward')
                        crops = []
                        for c,r in cells:
                            fragment = shape.intersection(box(16*c-8,-16*r-8,16*c+8,-16*r+8))
                            if fragment.area:
                                crops.append({'host_city_cell':(c,r),'finite_roi_EN':mapping(fragment)})
                        outside = shape.difference(owned)
                        literal.append({**record, 'finite_roi_EN': mapping(shape), 'owned_city_crops': crops,
                            'outside_owned_roi_EN':mapping(outside),
                            'inner_profile_ENHUV':inner_segments(shape,socket,record)})
                        unavailable = unary_union([unavailable,shape])
            entry['ground'][socket.arm] = {'socket': {'helper':socket.helper,'outward_peer':socket.outward_peer,
                'coreward_sources':placements,'mouth_EN':socket.mouth_en,'inward_EN':socket.inward_en,
                'north_cut_m':socket.joining_coordinate,'inner_station_m':design.FLAT_ENVELOPE},
                'references':references,'literal_source_fragments':literal,
                'inner_profile_segment_count':sum(len(row['inner_profile_ENHUV']) for row in literal)}
        entry['native_vehicle_roof_crops']=[row for socket in sockets
            for row in vehicle_roof_crops(context,socket,variant)]
        result['variants'][variant] = entry
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-audit', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    audit = jsonc.loads(args.input_audit.read_text())
    context = {}
    archives = []
    for label,filename in (('dd_rhw','RealHighway_DD_RHW-4.dat'),('rhw4','RealHighway_RHW-4.dat')):
        row = next(row for row in audit['donors'] if row['filename']==filename)
        raw = Path(row['path']).read_bytes()
        require(sha(raw)==row['sha256'],'Original native archive changed after its input audit')
        context[label] = {key:decompress(value) for key,value in entries(raw).items()}
        archives.append({'filename':filename,'sha256':sha(raw)})
    value = measure(context)
    value['source_archives'] = archives
    value['measurement_tool_sha256'] = sha(Path(__file__).read_bytes())
    value['independent_equations_sha256'] = sha(Path(design.__file__).read_bytes())
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(HEADER+json.dumps(value,indent=2)+'\n')
    print(json.dumps({'output':str(args.output),'sha256':sha(args.output.read_bytes()),
        'variants':len(value['variants']),'complete_physical_acceptance':False}))


if __name__ == '__main__':
    main()
