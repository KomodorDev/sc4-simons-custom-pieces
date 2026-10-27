"""One native-width HSR/Road parallel module; no traffic transfers are added."""
from copy import deepcopy
import struct
from scp.dbpf import require
from scp.models import parse_s3d, pack_s3d, valid_frame
from scp.recipes import combine_meshes, effect_clone, tile_exemplar
from scp.shadows import build_shadows
from scp.track_paths import S3D, PATH, EXEMPLAR, EFFECT

RECIPE = 'rail_hsr_road_stack'
INFO = {'effect_donor': ((*EFFECT,0x5DDF0100),'preview_hsr_ofillerpiece000',0x5DD31500)}


def _box(native, half, bottom, top):
    """Create a median column or its transverse cap, below the native deck."""
    from .single_track_models import _quad, _pack
    x, depth = 0., .65
    points = [(x+a*half,y,b*depth,.07+.035*a,y/16)
              for y in (bottom,top) for a,b in ((-1,-1),(1,-1),(1,1),(-1,1))]
    faces=[]
    for ids, normal in (((0,1,2,3),(0,-1,0)),((4,5,6,7),(0,1,0)),
                        ((0,1,5,4),(0,0,-1)),((1,2,6,5),(1,0,0)),
                        ((2,3,7,6),(0,0,1)),((3,0,4,7),(-1,0,0))):
        faces.extend(_quad([points[i] for i in ids],normal))
    return parse_s3d(_pack(native,faces))


def _road(native):
    from .single_track_models import _quad, _pack
    material=deepcopy(native)
    material['material']=deepcopy(native['material'])
    old=material['material']['textures'][0]
    material['material']['raw']=material['material']['raw'].replace(struct.pack('<I',old),struct.pack('<I',0x00004B0E))
    material['material']['textures']=[0x00004B0E]
    # Full tile UV range retains the actual ordinary Road texture's lane widths.
    vertices=[(-8.,0.,-8.,0.,0.),(8.,0.,-8.,1.,0.),(8.,0.,8.,1.,1.),(-8.,0.,8.,0.,1.)]
    return parse_s3d(_pack(material,_quad(vertices,(0,1,0))))


def _paths(hsr, road):
    from .crossings import _read_paths
    upper=_read_paths(hsr)[2]; lower=_read_paths(road)[2]
    require(len(upper)==2 and len(lower)==8,'Audited native route count changed')
    lines=['SC4PATHS','1.2','10','0','0']
    for r in upper+lower:
        lines += [f"-- Native_{r['transport']}_{r['entry']}_{r['exit']}",str(r['transport']),str(r['lane']),str(r['entry']),str(r['exit']),str(r['compatibility'] or 0),str(len(r['points']))]
        lines += [','.join(f'{v:g}' for v in p) for p in r['points']]
    return ('\r\n'.join(lines)+'\r\n').encode('ascii')


def build(spec,context):
    from .single_track_models import _native
    tile=int(spec['tile_ids'][0],16); preview=int(spec['preview_id'],16)
    require(spec['footprint']==[1,1] and len(spec['tile_ids'])==1,'Parallel stack is exactly one owned tile')
    hsr=context['hsr']; source=parse_s3d(hsr[*S3D,0x5DD31500])
    meshes=[m for m in source['meshes'] if all(valid_frame(source,f) for f in m['frames'])]
    native=_native(hsr[*S3D,0x5DD31500])
    road=_road(native); column=_box(native,.65,0.,13.5);cap=_box(native,7.5,13.5,native['bottom'])
    parts=[(source,meshes,(0.,0.,0.))]+[(m,m['meshes'],(0.,0.,0.)) for m in (road,column,cap)]
    raw=pack_s3d(combine_meshes(parts))
    assets={(*S3D,tile+z):raw for z in range(5)}
    assets.update(build_shadows(raw,tile)); assets[*S3D,preview]=raw
    assets[*PATH,tile]=_paths(hsr[*PATH,0x5DD31500],context['ordinary_road'][0x296678F7,0x69668828,0x00004B00])
    assets[*EXEMPLAR,tile]=tile_exemplar(hsr[*EXEMPLAR,0x5DCF0A00],tile,'SCP | '+spec['name'])
    key,name,old_model=INFO['effect_donor']
    assets[*EFFECT,preview]=effect_clone(hsr[key],name,spec['effect_name'],old_model,preview)
    root=int(spec['puzzle_id'],16)
    lines=[f'[HighwayIntersectionInfo_0x{root:08X}]',f'Piece = 0.0, 0.0, 0, 0, 0x{preview:08X}',f"PreviewEffect = {spec['effect_name']}",
           'CellLayout = ....','CellLayout = .a.<','CellLayout = .^..',
           'CheckType = a - monorail: 0x02000200 road: 0x02000200',
           'ConsLayout = ....','ConsLayout = .+.<','ConsLayout = .^..',
           f'AutoTileBase = 0x{tile:08X}','ReplacementIntersection = 0, 0',f'PlaceQueryID = 0x{tile:08X}','Costs = 150']
    for slot in range(1,8):
        lines += ['',f'[HighwayIntersectionInfo_0x{root+slot*0x10000:08X}]',f'CopyFrom = 0x{root+(slot%4)*0x10000 if slot>=4 else root:08X}']
        if slot<4:lines.append(f'Rotate = {slot}')
    return assets,'\r\n'.join(lines)+'\r\n'
