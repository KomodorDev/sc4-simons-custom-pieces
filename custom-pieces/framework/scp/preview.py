"""Render the staged S3D triangles with their installed NAM material textures.

This is an orthographic software rendering of the actual DAT model, not a
SimCity 4 screenshot. No geometry is invented and no AI image generation is
used. Writes requested preview PNGs and, in catalogue mode, their portable
coverage index and per-view evidence. Requires Pillow and NumPy.
"""
from __future__ import annotations

import json
import hashlib
import inspect
import math
import os
from pathlib import Path
import struct
import sys
import time

sys.dont_write_bytecode = True
import numpy as np
from PIL import Image, ImageDraw, ImageFont

from . import dbpf as read_dbpf
from .models import parse_s3d

S3D = (0x5ad0e817, 0xbadb57f1)
TEXTURE = (0x7ab50e44, 0x1abe787d)


def _sha(raw):
    return hashlib.sha256(raw).hexdigest()


def _json_hash(value):
    return _sha(json.dumps(value,sort_keys=True,separators=(',',':')).encode())


def piece_spec(piece):
    """The portable registered definition; asset_file is build-local metadata."""
    return {key:value for key,value in piece.items() if key!='asset_file'}


def select_pieces(manifest,piece_ids=None):
    pieces=manifest['pieces']
    if piece_ids is None:return pieces
    known={piece['id']:piece for piece in pieces}
    if len(piece_ids)!=len(set(piece_ids)) or not set(piece_ids)<=known.keys():
        raise ValueError('Preview selection contains duplicate or unknown piece identifiers')
    return [known[piece_id] for piece_id in piece_ids]


def read_resource(path,key):
    """Seek one indexed resource, without loading the rest of its DAT archive."""
    records=[(start,length) for kind,group,iid,start,length in read_dbpf.read_index(path)
             if (kind,group,iid)==key]
    if len(records)!=1:
        raise ValueError(f'Expected one preview resource {read_dbpf.tgi_string(key)} in {Path(path).name}')
    start,length=records[0]
    with Path(path).open('rb') as stream:
        stream.seek(start);raw=stream.read(length)
    if len(raw)!=length:raise ValueError('Truncated preview resource')
    return read_dbpf.decompress(raw)


def read_piece_preview(output,piece):
    from .autotile import validate_auto_tile_addresses
    validate_auto_tile_addresses(piece)
    output=Path(output).resolve()
    relative=Path(piece['asset_file'])
    path=(output/relative).resolve()
    if relative.is_absolute() or not path.is_relative_to(output) or path.suffix.lower()!='.dat':
        raise ValueError('Preview asset_file must identify a DAT inside the selected build')
    raw = read_resource(path,(*S3D,int(piece['preview_id'],16)))
    # Software rasterization accepts meshes that the game may fail to draw.
    # Reject oversized authored groups before producing reassuring artwork.
    from .render_meshes import assert_render_budget
    assert_render_budget(parse_s3d(raw))
    return raw


def model_texture_ids(model):
    required=set()
    for mesh in model['meshes']:
        material=model['materials'][mesh['frames'][0][3]]
        if not material['textures']:raise ValueError('Preview model has an untextured material')
        required.add(material['textures'][0])
    return required


class TextureLibrary:
    """Index NAM once, then decode each referenced atlas once per render run."""
    def __init__(self,plugins):
        self.plugins=Path(plugins)
        self.index=None
        self.textures={}
        self.provenance={}

    def for_model(self,model):
        required=model_texture_ids(model)
        if self.index is None:self.index=read_dbpf.index_plugins(self.plugins)
        for texture in sorted(required-self.textures.keys()):
            key=(*TEXTURE,texture)
            if key not in self.index:raise ValueError(f'Missing installed NAM texture {texture:08x}')
            path=sorted(self.index[key],key=lambda p:(p.name=='High Speed Rail_Textures.dat',str(p)))[-1]
            raw=read_resource(path,key)
            atlas=decode_fsh(raw)
            pixels=np.asarray(atlas,dtype=float)/255
            pixels.setflags(write=False)
            self.textures[texture]=pixels
            self.provenance[texture]={'instance':f'{texture:08x}','fsh_sha256':_sha(raw),
                                     'size':list(atlas.size)}
        return ({iid:self.textures[iid] for iid in required},
                [self.provenance[iid] for iid in sorted(required)])


def decode_fsh(blob: bytes) -> Image.Image:
    """Decode the first image of the NAM FSH texture resource."""
    data = read_dbpf.decompress(blob)
    if data[:4] != b'SHPI':
        raise ValueError('Texture is not an FSH resource')
    count, = struct.unpack_from('<I', data, 8)
    if count < 1:
        raise ValueError('FSH resource has no images')
    offset, = struct.unpack_from('<I', data, 20)
    code, width, height = struct.unpack_from('<IHH', data, offset)
    kind = code & 0xff
    pixels = data[offset + 16:]
    if kind == 0x60:
        length = ((width + 3) // 4) * ((height + 3) // 4) * 8
        return Image.frombytes('RGBA', (width, height), pixels[:length], 'bcn', (1, 'DXT1'))
    if kind == 0x61:
        length = ((width + 3) // 4) * ((height + 3) // 4) * 16
        return Image.frombytes('RGBA', (width, height), pixels[:length], 'bcn', (2, 'DXT3'))
    if kind == 0x7d:
        return Image.frombytes('RGBA', (width, height), pixels[:width * height * 4], 'raw', 'BGRA')
    if kind == 0x7f:
        return Image.frombytes('RGB', (width, height), pixels[:width * height * 3], 'raw', 'BGR').convert('RGBA')
    raise ValueError(f'Unsupported FSH image encoding {kind:02x}')


def model_triangles(model: dict):
    for mesh in model['meshes']:
        vi, ii, pi, mi = mesh['frames'][0]
        vb = model['vertices'][vi]
        vertices = np.array([struct.unpack_from('<5f', vb['data'], offset)
                             for offset in range(0, len(vb['data']), vb['stride'])])
        indices = np.array(model['indices'][ii]['values'])
        texture = model['materials'][mi]['textures'][0]
        for kind, first, length in model['primitives'][pi]:
            if kind != 0:
                raise ValueError('Preview supports triangle lists only')
            for tri in indices[first:first + length].reshape(-1, 3):
                yield vertices[tri, :3], vertices[tri, 3:], texture


def render_view(model: dict, textures: dict, azimuth: float, elevation: float,
                width: int, height: int) -> Image.Image:
    az, el = map(math.radians, (azimuth, elevation))
    right = np.array([math.cos(az), 0, -math.sin(az)])
    up = np.array([-math.sin(az) * math.sin(el), math.cos(el), -math.cos(az) * math.sin(el)])
    towards = np.array([math.sin(az) * math.cos(el), math.sin(el), math.cos(az) * math.cos(el)])
    triangles = list(model_triangles(model))
    all_positions = np.concatenate([position for position, uv, tex in triangles])
    projected = np.column_stack((all_positions @ right, all_positions @ up))
    low, high = projected.min(axis=0), projected.max(axis=0)
    scale = min((width - 80) / (high[0] - low[0]), (height - 80) / (high[1] - low[1]))
    center = (low + high) / 2
    background = np.array([247, 249, 251], float) / 255
    rgb = np.broadcast_to(background, (height, width, 3)).copy()
    depth = np.full((height, width), -np.inf)
    light = np.array([-0.4, 0.9, 0.2]); light /= np.linalg.norm(light)

    for position, uv, texture_id in triangles:
        projected = np.column_stack((position @ right, position @ up))
        screen = (projected - center) * [scale, -scale] + [width / 2, height / 2]
        z = position @ towards
        x0, y0 = np.maximum(np.floor(screen.min(axis=0)).astype(int), [0, 0])
        x1, y1 = np.minimum(np.ceil(screen.max(axis=0)).astype(int), [width - 1, height - 1])
        if x1 < x0 or y1 < y0:
            continue
        yy, xx = np.mgrid[y0:y1 + 1, x0:x1 + 1]
        xx, yy = xx + .5, yy + .5
        a, b, c = screen
        denominator = (b[1] - c[1]) * (a[0] - c[0]) + (c[0] - b[0]) * (a[1] - c[1])
        if abs(denominator) < 1e-8:
            continue
        w0 = ((b[1] - c[1]) * (xx - c[0]) + (c[0] - b[0]) * (yy - c[1])) / denominator
        w1 = ((c[1] - a[1]) * (xx - c[0]) + (a[0] - c[0]) * (yy - c[1])) / denominator
        w2 = 1 - w0 - w1
        inside = (w0 >= -1e-8) & (w1 >= -1e-8) & (w2 >= -1e-8)
        pixel_depth = w0 * z[0] + w1 * z[1] + w2 * z[2]
        local_depth = depth[y0:y1 + 1, x0:x1 + 1]
        visible = inside & (pixel_depth > local_depth)
        coords = w0[..., None] * uv[0] + w1[..., None] * uv[1] + w2[..., None] * uv[2]
        texture = textures[texture_id]
        # S3D's repeat wrapping handles the HSR donor's V range of -1 to 0.
        tu = np.mod(coords[..., 0], 1) * texture.shape[1] - .5
        tv = np.mod(coords[..., 1], 1) * texture.shape[0] - .5
        u0, v0 = np.floor(tu).astype(int), np.floor(tv).astype(int)
        fu, fv = (tu - u0)[..., None], (tv - v0)[..., None]
        t00 = texture[v0 % texture.shape[0], u0 % texture.shape[1]]
        t10 = texture[v0 % texture.shape[0], (u0 + 1) % texture.shape[1]]
        t01 = texture[(v0 + 1) % texture.shape[0], u0 % texture.shape[1]]
        t11 = texture[(v0 + 1) % texture.shape[0], (u0 + 1) % texture.shape[1]]
        sampled = (t00 * (1 - fu) + t10 * fu) * (1 - fv) + (t01 * (1 - fu) + t11 * fu) * fv
        visible &= sampled[..., 3] > .5
        normal = np.cross(position[1] - position[0], position[2] - position[0])
        normal /= np.linalg.norm(normal)
        shade = .78 + .22 * abs(normal @ light)
        color = np.clip(sampled[..., :3] * shade, 0, 1)
        local_rgb = rgb[y0:y1 + 1, x0:x1 + 1]
        local_rgb[visible] = color[visible]
        local_depth[visible] = pixel_depth[visible]
    return Image.fromarray(np.uint8(np.clip(rgb * 255, 0, 255)), 'RGB')


def render_fast_view(model,textures,azimuth,elevation,width,height,*,camera=None,
                     background_image=None,return_depth=False):
    """Render the same indexed triangles in bounded vectorized pixel batches.

    The depth test still chooses the first triangle at exactly equal depth,
    and texture alpha is evaluated before accepting a surface. No geometry
    is simplified or replaced by a diagram. An optional shared camera aligns
    world-grid artwork exactly with the model. Existing callers retain their
    original framing and pixels. return_depth also returns the surface depths;
    untouched background pixels have depth negative infinity.
    """
    triangles=list(model_triangles(model))
    positions=np.stack([item[0] for item in triangles])
    uvs=np.stack([item[1] for item in triangles])
    texture_ids=np.array([item[2] for item in triangles],dtype=np.uint32)
    if camera is None:
        az,el=map(math.radians,(azimuth,elevation))
        right=np.array([math.cos(az),0,-math.sin(az)])
        up=np.array([-math.sin(az)*math.sin(el),math.cos(el),-math.cos(az)*math.sin(el)])
        towards=np.array([math.sin(az)*math.cos(el),math.sin(el),math.cos(az)*math.cos(el)])
        projected=np.stack((positions@right,positions@up),axis=-1)
        low,high=projected.min(axis=(0,1)),projected.max(axis=(0,1))
        scale=min((width-80)/(high[0]-low[0]),(height-80)/(high[1]-low[1]))
        screen=(projected-(low+high)/2)*[scale,-scale]+[width/2,height/2]
    else:
        if (camera.width,camera.height)!=(width,height):
            raise ValueError('Shared camera image size must match the requested raster')
        if abs(camera.azimuth-azimuth)>1e-9 or abs(camera.elevation-elevation)>1e-9:
            raise ValueError('Shared camera angles must match the requested view')
        screen=camera.project_s3d(positions)
        towards=camera.towards
    z=positions@towards
    a,b,c=screen[:,0],screen[:,1],screen[:,2]
    denominator=(b[:,1]-c[:,1])*(a[:,0]-c[:,0])+(c[:,0]-b[:,0])*(a[:,1]-c[:,1])
    first=np.maximum(np.floor(screen.min(axis=1)).astype(int),[0,0])
    last=np.minimum(np.ceil(screen.max(axis=1)).astype(int),[width-1,height-1])
    valid=np.flatnonzero((np.abs(denominator)>=1e-8)&np.all(last>=first,axis=1))
    normals=np.cross(positions[:,1]-positions[:,0],positions[:,2]-positions[:,0])
    lengths=np.linalg.norm(normals,axis=1)
    light=np.array([-.4,.9,.2]);light/=np.linalg.norm(light)
    shade=.78+.22*np.abs((normals/np.maximum(lengths[:,None],1e-30))@light)
    if background_image is None:
        background=np.array([247,249,251],float)/255
        rgb=np.broadcast_to(background,(width*height,3)).copy()
    else:
        if background_image.size!=(width,height):
            raise ValueError('Background image size must match the requested raster')
        rgb=np.asarray(background_image.convert('RGB'),dtype=float).reshape(width*height,3).copy()/255
    depth=np.full(width*height,-np.inf)
    cursor=0
    while cursor<len(valid):
        batch=valid[cursor:cursor+512]
        sizes=last[batch]-first[batch]+1
        counts=sizes[:,0]*sizes[:,1]
        # A large simple triangle may itself cover most of the image. Keep
        # other batches below 400k candidate pixels to bound temporary arrays.
        stop=max(1,int(np.searchsorted(np.cumsum(counts),400000,side='right')))
        batch=batch[:stop];sizes=sizes[:stop];counts=counts[:stop]
        local=np.repeat(np.arange(len(batch)),counts)
        offsets=np.arange(int(counts.sum()))-np.repeat(np.cumsum(counts)-counts,counts)
        tri=batch[local]
        xx=first[tri,0]+offsets%sizes[local,0]
        yy=first[tri,1]+offsets//sizes[local,0]
        px,py=xx+.5,yy+.5
        w0=((b[tri,1]-c[tri,1])*(px-c[tri,0])+(c[tri,0]-b[tri,0])*(py-c[tri,1]))/denominator[tri]
        w1=((c[tri,1]-a[tri,1])*(px-c[tri,0])+(a[tri,0]-c[tri,0])*(py-c[tri,1]))/denominator[tri]
        w2=1-w0-w1
        inside=(w0>=-1e-8)&(w1>=-1e-8)&(w2>=-1e-8)
        tri,xx,yy,w0,w1,w2=(value[inside] for value in (tri,xx,yy,w0,w1,w2))
        pixel=yy*width+xx
        pixel_depth=w0*z[tri,0]+w1*z[tri,1]+w2*z[tri,2]
        closer=pixel_depth>depth[pixel]
        tri,pixel,pixel_depth,w0,w1,w2=(value[closer] for value in (tri,pixel,pixel_depth,w0,w1,w2))
        coords=w0[:,None]*uvs[tri,0]+w1[:,None]*uvs[tri,1]+w2[:,None]*uvs[tri,2]
        sampled=np.empty((len(tri),4),float)
        for iid in np.unique(texture_ids[tri]):
            selected=texture_ids[tri]==iid
            texture=textures[int(iid)]
            tu=np.mod(coords[selected,0],1)*texture.shape[1]-.5
            tv=np.mod(coords[selected,1],1)*texture.shape[0]-.5
            u0,v0=np.floor(tu).astype(int),np.floor(tv).astype(int)
            fu,fv=(tu-u0)[:,None],(tv-v0)[:,None]
            t00=texture[v0%texture.shape[0],u0%texture.shape[1]]
            t10=texture[v0%texture.shape[0],(u0+1)%texture.shape[1]]
            t01=texture[(v0+1)%texture.shape[0],u0%texture.shape[1]]
            t11=texture[(v0+1)%texture.shape[0],(u0+1)%texture.shape[1]]
            sampled[selected]=(t00*(1-fu)+t10*fu)*(1-fv)+(t01*(1-fu)+t11*fu)*fv
        opaque=sampled[:,3]>.5
        tri,pixel,pixel_depth,sampled=(value[opaque] for value in (tri,pixel,pixel_depth,sampled))
        np.maximum.at(depth,pixel,pixel_depth)
        winning=pixel_depth==depth[pixel]
        candidate=np.flatnonzero(winning)
        winners=np.full(width*height,len(tri),np.int64)
        np.minimum.at(winners,pixel[candidate],candidate)
        used=np.unique(pixel[candidate])
        chosen=winners[used]
        rgb[used]=np.clip(sampled[chosen,:3]*shade[tri[chosen],None],0,1)
        cursor+=len(batch)
    image=Image.fromarray(np.uint8(np.clip(rgb.reshape(height,width,3)*255,0,255)),'RGB')
    return (image,depth.reshape(height,width)) if return_depth else image


def font(size: int, bold: bool = False):
    candidates = ([Path('/System/Library/Fonts/Supplemental/Arial Bold.ttf')] if bold else
                  [Path('/System/Library/Fonts/Supplemental/Arial.ttf')])
    for path in candidates:
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def textures_for_models(models: list[dict], plugins: Path) -> dict:
    """Load actual installed model atlases by TGI, preferring the HSR archive."""
    library=TextureLibrary(plugins)
    for model in models:library.for_model(model)
    return library.textures


def render_contact_sheet(items: list[tuple[str, dict]], textures: dict,
                         destination: Path, *, title='One-way HSR branch kit') -> dict:
    """Render real indexed geometry; labels are the only graphical overlays."""
    columns = 2 if len(items) == 4 else min(3, len(items))
    if not columns:
        raise ValueError('No models selected for preview')
    rows = math.ceil(len(items) / columns)
    panel_width, panel_height = 640, 565
    canvas = Image.new('RGB', (columns * panel_width, 150 + rows * panel_height + 78), '#f7f9fb')
    draw = ImageDraw.Draw(canvas)
    dark, muted, blue = '#172b42', '#586a7e', '#176eaf'
    draw.text((42, 32), title, fill=dark, font=font(37, True))
    draw.text((44, 88), 'Actual S3D geometry and installed NAM texture · experimental fixed pieces',
              fill=muted, font=font(21))
    for number, (label, model) in enumerate(items):
        x, y = (number % columns) * panel_width, 150 + (number // columns) * panel_height
        draw.text((x + 32, y + 8), label, fill=blue, font=font(23, True))
        view = render_view(model, textures, 45, 36, 1200, 1000)
        canvas.paste(view.resize((600, 500), Image.Resampling.LANCZOS), (x + 20, y + 47))
    draw.text((44, canvas.height - 50), 'Software model preview, not a game screenshot. Placement, routing and shadows need game tests.',
              fill=muted, font=font(20))
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(destination)
    return {'output': str(destination.resolve()), 'models': len(items), 'size': list(canvas.size)}


def render_package(output: Path, plugins: Path, destination: Path, *, piece_ids=None) -> dict:
    """Read complete preview S3Ds from a built package's DATs."""
    output = Path(output)
    manifest = json.loads((output / 'manifest.json').read_text())
    pieces=select_pieces(manifest,piece_ids)
    items = []
    for piece in pieces:
        model=parse_s3d(read_piece_preview(output,piece))
        items.append((piece['name'], model))
    textures = textures_for_models([model for label, model in items], plugins)
    return render_contact_sheet(items, textures, destination, title="Simon's Custom Pieces · actual models")


def font_fingerprint(face):
    """Hash file-backed or Pillow-cached font bytes without consuming streams."""
    source=getattr(face,'path',None)
    if isinstance(source,(str,bytes,os.PathLike)):
        path=Path(os.fsdecode(source))
        raw=path.read_bytes() if path.is_file() else None
    else:
        # Pillow's built-in TrueType font has a BytesIO path. FreeTypeFont
        # caches the exact bytes it loaded, independent of stream position.
        raw=getattr(face,'font_bytes',None)
    return {'name':list(face.getname()),
            'file_sha256':_sha(raw) if raw is not None else None}


def renderer_settings():
    fonts=[font_fingerprint(font(24,bold)) for bold in (False,True)]
    # Documentation/selection changes do not change rendered pixels. Include
    # every rendering helper here; newly factored render helpers must join
    # this list so a changed algorithm can never reuse stale artwork.
    rendering_source='\n'.join(inspect.getsource(function) for function in _RENDER_HELPERS)
    return {'renderer':'indexed S3D triangles with bilinear NAM FSH textures',
            'renderer_sha256':_sha(rendering_source.encode()),'pillow_version':Image.__version__,
            'numpy_version':np.__version__,
            'background':'#f7f9fb','fonts':fonts,'geometry_simplified':False}


_RENDER_HELPERS=(decode_fsh,model_triangles,render_fast_view,font)


def _save_index(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_suffix('.tmp.json')
    temporary.write_text(json.dumps(value,indent=2)+'\n')
    temporary.replace(path)


def _selected_views(view_roles):
    if (isinstance(view_roles, str) or not isinstance(view_roles, (list, tuple)) or not view_roles
            or len(set(view_roles)) != len(view_roles) or not set(view_roles) <= {'angled', 'top'}):
        raise ValueError('Preview views must be a nonempty collection of unique angled/top roles')
    return tuple(view_roles)


def _view_files(role):
    return ('preview-top.png', 'evidence/preview-top.json') if role == 'top' else ('preview.png', 'evidence/preview.json')


def _valid_view_record(record, role, base):
    relative = Path(record.get('image', ''))
    image = (base/relative).resolve()
    safe = (not relative.is_absolute() and '..' not in relative.parts and image.is_relative_to(base)
            and image.name == _view_files(role)[0] and image.parent.parent.name == '00_pieces')
    if not safe or not image.is_file() or record.get('image_sha256') != _sha(image.read_bytes()):
        return False
    if role == 'angled':
        thumb = (base/record.get('thumbnail', '')).resolve()
        if (thumb != image.with_name('preview-thumb.png') or not thumb.is_file()
                or record.get('thumbnail_sha256') != _sha(thumb.read_bytes())):
            return False
    evidence = image.parent/_view_files(role)[1]
    if not evidence.is_file():
        return False
    if record.get('evidence_sha256') and record['evidence_sha256'] != _sha(evidence.read_bytes()):
        return False
    try:
        saved = json.loads(evidence.read_text())
    except (ValueError, OSError):
        return False
    return (saved.get('sha256') == record['image_sha256']
            and saved.get('source', {}).get('model_sha256') == record.get('preview_sha256')
            and saved.get('view_role', 'angled') == ('top-down' if role == 'top' else 'angled'))


def validate_preview_coverage(index, pieces, destination, *, settings=None, view_roles=('angled',)):
    """Check requested view coverage without imposing new artwork on old types."""
    view_roles = _selected_views(view_roles)
    missing, stale = [], []; base = Path(destination).resolve(); per_view = {}
    for role in view_roles:
        per_view[role] = {'missing': [], 'stale': []}
    for piece in pieces:
        entry = index.get('pieces', {}).get(piece['id'])
        if entry is None:
            missing.append(piece['id'])
            for role in view_roles: per_view[role]['missing'].append(piece['id'])
            continue
        invalid = False
        for role in view_roles:
            record = entry.get('views', {}).get(role)
            if record is None and role == 'angled' and entry.get('image'):
                record = entry
            if record is None:
                per_view[role]['missing'].append(piece['id']); invalid = True; continue
            expected = settings.get(role) if settings and ('angled' in settings or 'top' in settings) else settings
            valid = (_valid_view_record(record, role, base)
                     and Path(record.get('image', '')).parent.name == piece['id']
                     and entry.get('catalog_spec_sha256') == _json_hash(piece_spec(piece))
                     and entry.get('built_spec_sha256') == _json_hash(entry.get('built_spec'))
                     and entry.get('catalog_spec_sha256') == _json_hash(entry.get('catalog_spec'))
                     and record.get('preview_sha256') and record.get('textures')
                     and (not entry.get('current_model_sha256') or record['preview_sha256'] == entry['current_model_sha256'])
                     and (not entry.get('current_textures') or record['textures'] == entry['current_textures'])
                     and entry.get('actual_model_triangles', 0) > 0
                     and entry.get('preview_tgi') == read_dbpf.tgi_string((*S3D, int(piece['preview_id'], 16)))
                     and (expected is None or record.get('settings_sha256') == _json_hash(expected)))
            # Preserve strict checking of the established angled index fields.
            if role == 'angled' and entry.get('image'):
                valid = valid and all(entry.get(key) == record.get(key) for key in
                                      ('image', 'image_sha256', 'thumbnail', 'thumbnail_sha256'))
            if not valid:
                per_view[role]['stale'].append(piece['id']); invalid = True
        if invalid: stale.append(piece['id'])
    return {'registered': len(pieces), 'covered': len(pieces)-len(missing)-len(stale),
            'missing': missing, 'stale': stale, 'complete': not missing and not stale,
            'requested_views': list(view_roles), 'views': per_view}


def _canonical_title(root, catalog, piece):
    from .render_headers import piece_title, title_records
    domain = catalog.get('domains', {}).get(piece.get('domain'), {})
    relative = domain.get('path')
    if relative is None:
        return piece['name'], {}
    directory = root/relative/'00_pieces'/piece['id']
    declaration = directory/'connector-groups.jsonc'
    if not declaration.is_file():
        return piece['name'], {}
    from .connector_metadata import load_library
    resolved = load_library(root, [piece['id']], domain_id=piece['domain'])['pieces'][piece['id']]
    title = piece_title(piece['id'], title_records(resolved), piece['name'])
    paths = [directory/name for name in ('piece.json', 'connections.json', 'connector-groups.jsonc')]
    registry = root/relative/'domain.json'; paths.append(registry)
    domain_data = json.loads(registry.read_text())
    profiles = root/relative/domain_data.get('connector_profiles', 'connector-profiles.json')
    if profiles.is_file(): paths.append(profiles)
    return title, {path.relative_to(root).as_posix(): _sha(path.read_bytes()) for path in paths}


def render_catalog(outputs, plugins, destination=None, *, root, index_path=None,
                   piece_ids=None, force=False, progress=None, view_roles=('angled',)):
    """Render explicitly requested canonical views; never create a flat catalogue."""
    from .catalog import load_catalog
    from .piece_previews import render_piece, preview_settings
    view_roles = _selected_views(view_roles)
    root = Path(root).resolve(); catalog = load_catalog(root); pieces = catalog['pieces']; known = {p['id']: p for p in pieces}
    sources = {}
    for output in outputs:
        output = Path(output); manifest_raw = (output/'manifest.json').read_bytes(); manifest = json.loads(manifest_raw)
        files = {item['path']: item for item in manifest.get('files', [])}
        for piece in manifest['pieces']:
            sources[piece['id']] = (output, piece, files.get(piece['asset_file'], {}), manifest.get('version'), _sha(manifest_raw))
    if piece_ids is None: piece_ids = [p['id'] for p in pieces if p['id'] in sources]
    if isinstance(piece_ids, str) or len(piece_ids) != len(set(piece_ids)) or not set(piece_ids) <= sources.keys() & known.keys():
        raise ValueError('Preview selection contains duplicate, unknown or unbuilt piece identifiers')
    if destination is not None and Path(destination).name != '00_pieces':
        raise ValueError('Canonical catalog destinations must be a domain pieces directory; omit --destination to use registered domains')
    base = Path(destination).resolve() if destination is not None else root
    index_path = Path(index_path) if index_path is not None else root/'local/cache/preview-index.json'
    index = json.loads(index_path.read_text()) if index_path.is_file() else {'schema_version': 3, 'pieces': {}}
    index = {**index, 'schema_version': 3, 'purpose': 'Portable actual-source coverage for canonical per-piece previews; not manual or in-game evidence.'}
    index['pieces'] = {key: value for key, value in index['pieces'].items() if key in known}
    settings = {role: preview_settings(view_role=role) for role in view_roles}
    index['settings'] = preview_settings(); index['view_settings'] = {**index.get('view_settings', {}), **settings}
    library = TextureLibrary(plugins); rendered = skipped = 0; rendered_views = skipped_views = 0; start = time.monotonic()
    for number, slug in enumerate(piece_ids, 1):
        output, built, file_record, version, manifest_hash = sources[slug]; current = known[slug]
        comparable = lambda p: {key: value for key, value in piece_spec(p).items() if key not in ('design_review', 'purpose')}
        if comparable(built) != comparable(current):
            raise ValueError(f'{slug}: built definition differs from the current registered piece; rebuild it first')
        dat_hash = _sha((output/built['asset_file']).read_bytes())
        if file_record.get('sha256') and dat_hash != file_record['sha256']:
            raise ValueError(f'{slug}: actual DAT hash differs from the build manifest')
        raw = read_piece_preview(output, built); model = parse_s3d(raw)
        textures, atlases = library.for_model(model)
        target = (base/slug) if destination is not None else root/catalog['domains'][current['domain']]['path']/'00_pieces'/slug
        title, title_sources = _canonical_title(root, catalog, current)
        old = index['pieces'].get(slug, {})
        views = dict(old.get('views', {})); any_rendered = False
        drawing = {key: current.get(key) for key in ('id', 'name', 'footprint', 'cells', 'tile_ids')}
        for role in view_roles:
            image_name, evidence_name = _view_files(role)
            image, evidence_path = target/image_name, target/evidence_name
            inputs = {'drawing': drawing, 'preview_sha256': _sha(raw), 'source_dat_sha256': dat_hash,
                      'textures': atlases, 'settings_sha256': _json_hash(settings[role]),
                      'display_title': title, 'title_source_inputs': title_sources}
            fingerprint = _json_hash(inputs); previous = views.get(role, {})
            unchanged = (not force and previous.get('input_fingerprint') == fingerprint
                         and _valid_view_record(previous, role, base))
            if unchanged:
                skipped_views += 1
            else:
                evidence = render_piece({**current, 'asset_file': built['asset_file']}, raw, library, target,
                                        dat_hash=dat_hash, view_role=role, title=title)
                evidence['title_source_inputs'] = title_sources
                evidence['input_fingerprint'] = fingerprint
                evidence_path.write_text(json.dumps(evidence, indent=2)+'\n')
                rendered_views += 1; any_rendered = True
            evidence = json.loads(evidence_path.read_text())
            if evidence['sha256'] != _sha(image.read_bytes()) or evidence['source']['model_sha256'] != _sha(raw):
                raise ValueError(f'{slug}: saved per-piece evidence differs from actual image/model')
            record = {key: inputs[key] for key in ('preview_sha256', 'source_dat_sha256', 'textures', 'settings_sha256', 'display_title')}
            record.update(input_fingerprint=fingerprint, image=image.relative_to(base).as_posix(),
                          image_sha256=_sha(image.read_bytes()), image_size=evidence['size'],
                          evidence_sha256=_sha(evidence_path.read_bytes()))
            if role == 'angled':
                thumb = target/'preview-thumb.png'
                record.update(thumbnail=thumb.relative_to(base).as_posix(), thumbnail_sha256=_sha(thumb.read_bytes()))
            views[role] = record
        rendered += int(any_rendered); skipped += int(not any_rendered)
        entry = {**old, 'id': slug, 'menu_name': current['name'], 'views': views,
                 'built_spec_sha256': _json_hash(piece_spec(built)), 'catalog_spec_sha256': _json_hash(piece_spec(current)),
                 'built_spec': piece_spec(built), 'catalog_spec': piece_spec(current),
                 'preview_tgi': read_dbpf.tgi_string((*S3D, int(built['preview_id'], 16))),
                 'preview_bytes': len(raw), 'source_asset': built['asset_file'], 'source_build_version': version,
                 'source_manifest_sha256': manifest_hash, 'source_dat_sha256': dat_hash,
                 'current_model_sha256': _sha(raw), 'current_textures': atlases,
                 'actual_model_triangles': evidence['model']['triangles'], 'in_game_evidence': False}
        if 'angled' in views:
            entry.update(views['angled'])
        index['pieces'][slug] = entry
        _save_index(index_path, index)
        if progress:
            progress({'piece': slug, 'number': number, 'selected': len(piece_ids),
                      'views': list(view_roles), 'action': 'rendered' if any_rendered else 'unchanged',
                      'elapsed_seconds': round(time.monotonic()-start, 2)})
    selected_pieces = [known[identifier] for identifier in piece_ids]
    index['coverage'] = {
        **validate_preview_coverage(index, selected_pieces, base, settings=settings, view_roles=view_roles),
        'scope': 'selected_piece_ids_and_requested_views',
        'selected_piece_ids': list(piece_ids), 'selected_count': len(piece_ids),
    }
    index['catalogue_coverage'] = {
        **validate_preview_coverage(index, pieces, base, settings=settings, view_roles=view_roles),
        'scope': 'all_registered_piece_ids_and_requested_views',
    }
    _save_index(index_path, index)
    return {'rendered': rendered, 'skipped_unchanged': skipped, 'rendered_views': rendered_views,
            'skipped_unchanged_views': skipped_views, 'requested_views': list(view_roles),
            'selected_piece_ids': list(piece_ids), 'selected_count': len(piece_ids),
            'coverage': index['coverage'], 'catalogue_coverage': index['catalogue_coverage'],
            'index': str(index_path), 'elapsed_seconds': round(time.monotonic()-start, 2)}


def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path,action='append')
    parser.add_argument('--plugins', required=True, type=Path)
    parser.add_argument('--destination', type=Path,help='Contact-sheet file, or optional canonical domain pieces directory for --catalog')
    parser.add_argument('--include', action='append')
    parser.add_argument('--catalog',action='store_true',help='Write selected canonical reusable-piece views in their piece folders (default: angled view and thumbnail)')
    parser.add_argument('--views', nargs='+', choices=('angled', 'top'), default=['angled'],
                        help='Canonical --catalog views: angled, top, or both; top writes preview-top.png without changing an existing angle')
    parser.add_argument('--root',type=Path,default=next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file()))
    parser.add_argument('--index',type=Path,help='Portable JSON coverage index for --catalog')
    parser.add_argument('--force',action='store_true',help='Render even when all input and image hashes match')
    parser.add_argument('--progress',action='store_true')
    args = parser.parse_args()
    if args.catalog:
        result=render_catalog(args.output,args.plugins,args.destination,root=args.root,
            index_path=args.index,
            piece_ids=args.include,force=args.force,view_roles=args.views,
            progress=(lambda event:print(json.dumps(event),flush=True)) if args.progress else None)
    else:
        if len(args.output)!=1:parser.error('Repeated --output requires --catalog')
        if args.destination is None:parser.error('Contact-sheet rendering requires --destination FILE')
        result=render_package(args.output[0],args.plugins,args.destination,piece_ids=args.include)
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()

