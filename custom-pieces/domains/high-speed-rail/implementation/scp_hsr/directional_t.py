"""A deliberately simple, smooth, same-height six-movement HSR T.

The earlier catalog is immutable. This new recipe has three physical dual-track
decks and six directed train journeys. Its rail crossings are explicitly at
grade: it is a review prototype, not a flying junction or a signalling model.
"""
from __future__ import annotations

import math
import json
from functools import lru_cache

from scp.dbpf import require
from .interchange_layouts import _add_route, _normalize
from .interchange_models import construction_symbols, EFFECT_DONOR
from scp.track_paths import S3D, PATH, EXEMPLAR, EFFECT, LTEXT, encode_paths
from .rail_features import _construction_flags

RECIPE = 'directional_hsr_t_smooth_at_grade'
RECIPES = (RECIPE,)
HEIGHT = 15.5


def _quarter():
    """Integrate a smooth heading at constant arclength, then scale to87.5m.

    Heading is a quintic smoothstep. Its first and second derivatives vanish
    at either end, so curvature joins the straight approaches continuously.
    The half-metre native tangent collars themselves are exact straight lines.
    """
    count = 256
    headings = [-math.pi / 2 + math.pi / 2 * (10*t**3 - 15*t**4 + 6*t**5)
                for t in (n/count for n in range(count+1))]
    xy = [(0., 0.)]
    for a, b in zip(headings, headings[1:]):
        x, y = xy[-1]
        xy.append((x + (math.cos(a)+math.cos(b))/2/count,
                   y + (math.sin(a)+math.sin(b))/2/count))
    scale = 87.5 / xy[-1][0]
    states = [(x*scale, 87.5+y*scale, angle) for (x,y),angle in zip(xy,headings)]
    states[0] = (0., 87.5, -math.pi/2)
    states[-1] = (87.5, 0., 0.)
    return [(0.,88.,-math.pi/2), *states, (104.,0.,0.)]


def _pair(states, reflected=False):
    """Keep native rail offsets analytically normal to the actual deck.

    North-to-east uses the outer(-2m) lane. Reflecting a curve flips its
    handedness, so south-to-east uses the opposite normal to keep right-hand
    running at the unchanged native ports.
    """
    center, first, second = [], [], []
    for x,y,angle in states:
        if reflected:
            y, angle = -y, -angle
        normal = (-math.sin(angle), math.cos(angle))
        lane = -2.
        center.append((x,y-80.,HEIGHT))
        first.append((x+lane*normal[0],y+lane*normal[1]-80.,HEIGHT))
        second.append((x-lane*normal[0],y-lane*normal[1]-80.,HEIGHT))
    return center, first, list(reversed(second))


def directional_routes(recipe=RECIPE):
    """Return fresh complete paths, in normalized city coordinates."""
    require(recipe == RECIPE, 'Unknown directional rail recipe')
    north, ne, en = _pair(_quarter())
    south, se, es = _pair(_quarter(), reflected=True)
    return {
        'S>N': [(2.,-168.,HEIGHT),(2.,8.,HEIGHT)],
        'N>S': [(-2.,8.,HEIGHT),(-2.,-168.,HEIGHT)],
        'N>E': ne, 'E>N': en, 'S>E': se, 'E>S': es,
    }


def _physical_centers():
    north, _, _ = _pair(_quarter())
    south, _, _ = _pair(_quarter(), reflected=True)
    return {'main': [(0.,-168.,HEIGHT),(0.,8.,HEIGHT)],
            'north_curve': north, 'south_curve': south}


def directional_layout(recipe=RECIPE):
    """Separate traffic slicing from the three complete physical deck sweeps."""
    routes = directional_routes(recipe)
    layout = {}
    for movement, points in routes.items():
        _add_route(layout, points, movement,
                   role='main' if movement in ('S>N','N>S') else 'branch', deck=False)
    # A global physical route need not be truncated at every traffic seam.
    # The geometry engine joins and partitions its finished union afterward.
    anchor = min(layout, key=lambda cell:(cell[1],cell[0]))
    for name, points in _physical_centers().items():
        local = [(p[0]-16*anchor[0],p[1]+16*anchor[1],p[2]) for p in points]
        layout[anchor]['decks'].append({
            'points':local, 'width':15., 'geometry_id':'directional_'+name,
            'profile':'hsr', 'precise_union':True, 'simplify_collinear':True,
            'extend_endpoints':'ports', 'clearance_half_width':2.6,
            'support':False,
            'start_tangent': (0.,1.) if name=='main' else (0.,1. if name=='south_curve' else -1.),
            'end_tangent': (0.,1.) if name=='main' else (1.,0.),
        })
    result, shift = _normalize(layout)
    require(shift == (0.,0.), 'Directional T normalization unexpectedly changed')
    return result


def _distance(point, a, b):
    dx,dy=b[0]-a[0],b[1]-a[1]
    fraction=max(0.,min(1.,((point[0]-a[0])*dx+(point[1]-a[1])*dy)/(dx*dx+dy*dy)))
    return math.hypot(point[0]-a[0]-fraction*dx,point[1]-a[1]-fraction*dy)


def _support_centers(cells):
    """One reserved grid foundation wherever its entire top is under a slab.

    This deliberately uses one global grid, rather than one support sequence
    per curve. Distinct centres therefore remain at least16m apart even in the
    broad junction openings. Nine underside-contact samples are also audited
    independently on the encoded physical models.
    """
    segments=[(a,b) for points in _physical_centers().values() for a,b in zip(points,points[1:])]
    result=[]
    for x,row in cells:
        center=(16.*x,-16.*row)
        if all(any(_distance((center[0]+dx,center[1]+dy),a,b)<7.49 for a,b in segments)
               for dx in (-.65,0.,.65) for dy in (-.65,0.,.65)):
            result.append(center)
    return result


_LAYOUT = directional_layout()
_CELLS = list(_LAYOUT)
INFO = {RECIPE: {
    'recipe':RECIPE, 'name':'HSR Level 2 (15.5 m) — Two-Track Smooth T Junction — At Grade',
    'kind':'smooth_at_grade_t', 'category':'directional-review-prototype',
    'height':HEIGHT, 'footprint':(7,11), 'cells':_CELLS,
    'cost':100*len(_CELLS), 'effect_donor':EFFECT_DONOR,
    'ports':{'N':{'in':(-2.,8.,HEIGHT),'out':(2.,8.,HEIGHT)},
             'S':{'in':(2.,-168.,HEIGHT),'out':(-2.,-168.,HEIGHT)},
             'E':{'in':(104.,-78.,HEIGHT),'out':(104.,-82.,HEIGHT)}},
    'movements':[(a,b) for a in 'NSE' for b in 'NSE' if a!=b],
    'construction_flags':{cell:_construction_flags(data['routes']) for cell,data in _LAYOUT.items()},
    'support_centers':_support_centers(_CELLS),
    'support_foundation_width':1.3, 'support_min_spacing':16.,
    'clearance_width':5., 'clearance_height':5.,
    'minimum_radius_m':24., 'maximum_turn_directness':1.55,
    'at_grade_conflicts':True,
    'provenance':'New smooth-heading dual-track junction; native HSR ports/profile; intentional at-grade conflicts; no game tests',
}}


def _number(value):
    return int(value,16) if isinstance(value,str) else int(value)


def _spec(spec):
    require(spec['recipe'] in INFO, 'Unknown directional T recipe')
    info=INFO[spec['recipe']]
    cells=[tuple(cell) for cell in spec.get('cells',info['cells'])]
    require(cells==info['cells'] and tuple(spec['footprint'])==info['footprint'],
            'Directional T cells/footprint differ from its implementation')
    tiles=list(map(_number,spec['tile_ids']))
    require(len(tiles)==len(cells), 'Directional T allocation differs from its cell count')
    base=tiles[0]-0x100*cells[0][0]-0x10*cells[0][1]
    require(tiles==[base+0x100*x+0x10*row for x,row in cells],
            'Directional T allocation differs from its AutoTileBase grid')
    return info,dict(zip(cells,tiles)),base


def build_rules(spec):
    info,tiles,base=_spec(spec)
    flags=info['construction_flags']
    letters,by_flag=construction_symbols(list(tiles),flags)
    width,depth=info['footprint']
    def grid(construct=False):
        rows=['.'*(width+3)]
        for row in range(depth):
            rows.append('.'+''.join(('+' if construct else letters[x,row]) if (x,row) in letters else '.'
                                    for x in range(width))+'.'+('<' if row==0 else '.'))
        return rows+['.^'+'.'*(width+1)]
    puzzle,preview=_number(spec['puzzle_id']),_number(spec['preview_id'])
    lines=[f'[HighwayIntersectionInfo_0x{puzzle:08X}]',f'Piece = 0.0, 0.0, 0, 0, 0x{preview:08X}',
           f"PreviewEffect = {spec['effect_name']}",'']
    lines+=['CellLayout = '+row for row in grid()]
    lines+=['']+[f'CheckType = {symbol} - monorail: 0x{flag:08X}' for flag,symbol in by_flag.items()]
    lines+=['']+['ConsLayout = '+row for row in grid(True)]
    lines+=['',f'AutoTileBase = 0x{base:08X}','ReplacementIntersection = 0, 0',
            f'PlaceQueryID = 0x{next(iter(tiles.values())):08X}',f'Costs = {info["cost"]}']
    for slot in range(1,8):
        lines+=['',f'[HighwayIntersectionInfo_0x{puzzle+slot*0x10000:08X}]',
                f'CopyFrom = 0x{puzzle+(slot%4)*0x10000 if slot>=4 else puzzle:X}']
        if slot<4:lines.append(f'Rotate = {slot}')
    return '\r\n'.join(lines)+'\r\n'


def _plan_area(polygon):
    return abs(sum(a[0]*b[2]-b[0]*a[2] for a,b in zip(polygon,polygon[1:]+polygon[:1])))/2


def _floor_clip(polygon,a,b,inside):
    """Use one exact boundary for both classification and interpolation.

    An epsilon classification combined with a zero-plane intersection can
    extrapolate past a segment on almost parallel edges. That can produce
    self-crossing fans at an eased rail merge. This new recipe uses the same
    zero boundary throughout; previous recipe bytes are unaffected.
    """
    if not polygon:return []
    sign=1. if inside else -1.
    def side(point):
        return sign*((b[0]-a[0])*(point[2]-a[2])-(b[2]-a[2])*(point[0]-a[0]))
    previous=polygon[-1]
    before=side(previous)
    result=[]
    for current in polygon:
        after=side(current)
        if (after>=0.)!=(before>=0.):
            fraction=before/(before-after)
            require(0.<=fraction<=1.,'A new directional floor clip extrapolated beyond its segment')
            result.append(tuple(previous[n]+fraction*(current[n]-previous[n]) for n in range(5)))
        if after>=0.:result.append(current)
        previous,before=current,after
    return result


def _floor_subtract(polygon,triangle):
    """Subtract one convex floor triangle, retaining exact interpolated UVs."""
    orientation=sum(a[0]*b[2]-b[0]*a[2] for a,b in zip(triangle,triangle[1:]+triangle[:1]))
    if orientation<0:triangle=list(reversed(triangle))
    pending,outside=polygon,[]
    for a,b in zip(triangle,triangle[1:]+triangle[:1]):
        if not pending:break
        fragment=_floor_clip(pending,a,b,False)
        if len(fragment)>=3 and _plan_area(fragment)>1e-10:outside.append(fragment)
        pending=_floor_clip(pending,a,b,True)
    return outside


def _flat_union(triangles):
    """Emit each point of a flat deck once, with earlier texture priority."""
    accepted,buckets=[],{}
    def keys(polygon):
        return [(x,z) for x in range(math.floor(min(p[0] for p in polygon)/4.),
                                    math.floor(max(p[0] for p in polygon)/4.)+1)
                for z in range(math.floor(min(p[2] for p in polygon)/4.),
                               math.floor(max(p[2] for p in polygon)/4.)+1)]
    for triangle in triangles:
        pieces=[list(triangle)]
        candidates={index for key in keys(triangle) for index in buckets.get(key,())}
        for index in sorted(candidates):
            other=accepted[index]
            xmin,xmax=min(p[0] for p in other),max(p[0] for p in other)
            zmin,zmax=min(p[2] for p in other),max(p[2] for p in other)
            remaining=[]
            for polygon in pieces:
                if (min(p[0] for p in polygon)>=xmax or max(p[0] for p in polygon)<=xmin or
                    min(p[2] for p in polygon)>=zmax or max(p[2] for p in polygon)<=zmin):
                    remaining.append(polygon)
                else:remaining.extend(_floor_subtract(polygon,list(other)))
            pieces=remaining
            if not pieces:break
        for polygon in pieces:
            for n in range(1,len(polygon)-1):
                part=(polygon[0],polygon[n],polygon[n+1])
                if _plan_area(list(part))<=1e-10:continue
                index=len(accepted)
                accepted.append(part)
                for key in keys(part):buckets.setdefault(key,[]).append(index)
    return accepted


def _partition_strict(triangles,occupied):
    """Partition with the same robust boundary rule, retaining overhangs.

    Empty neighbouring cells receive no new network occupancy. Their profile
    fragments remain attached to the nearest occupied cell, exactly as in
    the earlier partition policy, while each actual face is emitted once.
    """
    result={cell:[] for cell in occupied}
    for triangle in triangles:
        lx,hx=min(p[0] for p in triangle),max(p[0] for p in triangle)
        lz,hz=min(p[2] for p in triangle),max(p[2] for p in triangle)
        xs=([math.floor((lx+8-1e-7)/16)] if hx-lx<1e-7 else
            range(math.floor((lx+8)/16),math.floor((hx+8)/16)+1))
        rows=([math.floor((lz+8-1e-7)/16)] if hz-lz<1e-7 else
              range(math.floor((lz+8)/16),math.floor((hz+8)/16)+1))
        for x in xs:
            for row in rows:
                polygon=list(triangle)
                left,right,bottom,top=16*x-8,16*x+8,16*row-8,16*row+8
                for a,b in (((left,0.,1.),(left,0.,0.)),
                            ((right,0.,0.),(right,0.,1.)),
                            ((0.,0.,bottom),(1.,0.,bottom)),
                            ((1.,0.,top),(0.,0.,top))):
                    polygon=_floor_clip(polygon,a,b,True)
                if len(polygon)<3:continue
                cell=(x,row)
                if cell not in result:
                    cx=sum(p[0] for p in polygon)/len(polygon)
                    cz=sum(p[2] for p in polygon)/len(polygon)
                    def distance(candidate):
                        dx=max(0.,abs(cx-16*candidate[0])-8)
                        dz=max(0.,abs(cz-16*candidate[1])-8)
                        return dx*dx+dz*dz,candidate
                    cell=min(occupied,key=distance)
                local=[(p[0]-16*cell[0],p[1],p[2]-16*cell[1],p[3],p[4]) for p in polygon]
                for n in range(1,len(local)-1):
                    face=(local[0],local[n],local[n+1])
                    u=tuple(face[1][k]-face[0][k] for k in range(3))
                    v=tuple(face[2][k]-face[0][k] for k in range(3))
                    normal=(u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])
                    if sum(value*value for value in normal)>1e-14:result[cell].append(face)
    return result


def build_models(native_hsr,recipe=RECIPE):
    """Cache only immutable models under their complete physical inputs."""
    require(recipe in INFO,'Unknown directional rail recipe')
    layout=directional_layout(recipe)
    config={'layout':[[list(cell),data] for cell,data in layout.items()],
            'ground':False,
            'support_centers':INFO[recipe]['support_centers'],
            'support_foundation_width':INFO[recipe]['support_foundation_width'],
            'support_min_spacing':INFO[recipe]['support_min_spacing']}
    signature=json.dumps(config,sort_keys=True,separators=(',',':'),allow_nan=False)
    return dict(_cached_models(native_hsr,signature))


@lru_cache(maxsize=2)
def _cached_models(native_hsr,signature):
    config=json.loads(signature)
    layout={tuple(cell):data for cell,data in config['layout']}
    return tuple(_compile_models(native_hsr,layout,config).items())


def _compile_models(native_hsr,layout,config):
    """Compile the actual union, then add each globally selected pier once."""
    from scp.models import parse_s3d,pack_s3d
    from .rail_geometry import _global_decks,_build_triangles,_pack_junction,_sweep
    from .single_track_models import _native,_pack,_pillar
    from scp.recipes import combine_meshes
    source=_native(native_hsr)
    decks=_global_decks(layout)
    triangles=_build_triangles(source,decks,False,False)
    # The old compiler still opens the parapets. Flat upper/lower surfaces
    # use the robust new-only union, including real rail ribbons first so
    # ballast never paints over a used train track.
    # Native bed vertices differ by about0.000002m; their audited donor
    # classification already uses0.0001m coplanarity. A tighter replacement
    # filter would accidentally retain a few original floor faces.
    triangles=[tri for tri in triangles if not any(all(abs(p[1]-height)<1e-4 for p in tri)
                                                for height in (source['bed_y'],source['bottom']))]
    swept=[_sweep(source,deck,False)[0] for deck in reversed(decks)]
    floors=[tri for kind in ('rail','bed') for surfaces in swept
            for actual,tri in surfaces if actual==kind]
    undersides=[tri for surfaces in swept for kind,tri in surfaces if kind=='underside']
    triangles.extend(_flat_union(floors))
    triangles.extend(_flat_union(undersides))
    result={cell:_pack_junction(source,parts) for cell,parts in _partition_strict(triangles,list(layout)).items()}
    support=parse_s3d(_pack(source,_pillar((0.,0.),source['bottom'])))
    support['meshes'][0]['name']=b'SCP consolidated directional support\0'
    require(config['support_foundation_width']==1.3,'Directional support donor uses a1.3m foundation')
    for x,north in config['support_centers']:
        cell=round(x/16),round(-north/16)
        model=parse_s3d(result[cell])
        result[cell]=pack_s3d(combine_meshes([
            (model,model['meshes'],(0.,0.,0.)),(support,support['meshes'],(0.,0.,0.))]))
    return result


def build_directional(spec,context):
    """Compile all five zooms, actual paths, shadows and the model preview."""
    from scp.models import parse_s3d,pack_s3d
    from scp.recipes import combine_meshes,effect_clone,label,tile_exemplar
    from scp.shadows import build_shadows
    info,tiles,_=_spec(spec)
    layout=directional_layout(spec['recipe'])
    hsr=context['hsr']
    models=build_models(hsr[*S3D,0x5DD31500],spec['recipe'])
    assets,parts={},[]
    for cell,tile in tiles.items():
        raw=models[cell]
        for zoom in range(5):assets[*S3D,tile+zoom]=raw
        assets.update(build_shadows(raw,tile))
        assets[*PATH,tile]=encode_paths(layout[cell]['routes'])
        assets[*EXEMPLAR,tile]=tile_exemplar(hsr[*EXEMPLAR,0x5DCF0A00],tile,'SCP | '+spec['name'])
        assets[*LTEXT,tile]=label('SCP | '+spec['name']+' (Experimental)')
        model=parse_s3d(raw)
        parts.append((model,model['meshes'],(16.*cell[0],0.,16.*cell[1])))
    preview=_number(spec['preview_id'])
    assets[*S3D,preview]=pack_s3d(combine_meshes(parts))
    donor,name,model=info['effect_donor']
    assets[*EFFECT,preview]=effect_clone(hsr[donor],name,spec['effect_name'],model,preview)
    return assets,build_rules(spec)
