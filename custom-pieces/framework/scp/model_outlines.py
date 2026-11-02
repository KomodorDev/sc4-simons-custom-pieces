"""Project actual indexed component triangles separately from construction cells."""
from __future__ import annotations

from PIL import Image, ImageChops, ImageDraw, ImageFilter
from .models import positions, validate_s3d


def projected_component_masks(model, sources, camera, size):
    """Return first-frame triangle unions; never substitute a tile rectangle."""
    validate_s3d(model)
    used=set();result=[]
    for source in sources:
        indices=source.get('render_mesh_indices')
        if not isinstance(indices,list) or not indices or any(type(i) is not int or i<0 or i>=len(model['meshes']) for i in indices):
            raise ValueError('Actual model outlines require an exact placed-component mesh mapping')
        if len(set(indices))!=len(indices) or used.intersection(indices):
            raise ValueError('A placed model mesh belongs to more than one component outline')
        used.update(indices)
        mask=Image.new('L',size,0);draw=ImageDraw.Draw(mask);count=0;projected={}
        for index in indices:
            mesh=model['meshes'][index];vi,ii,pi,_mi=mesh['frames'][0]
            if vi not in projected:
                vertices=positions(model['vertices'][vi])
                projected[vi]=camera.project_world([p[0] for p in vertices],[-p[2] for p in vertices])
            elements=model['indices'][ii]['values']
            for kind,first,number in model['primitives'][pi]:
                if kind!=0 or number%3:raise ValueError('Actual component outline requires indexed triangle primitives')
                for offset in range(first,first+number,3):
                    polygon=[tuple(projected[vi][i]) for i in elements[offset:offset+3]]
                    draw.polygon(polygon,fill=255);count+=1
        owned=Image.new('L',size,0);od=ImageDraw.Draw(owned)
        for east,north in source.get('occupied_world_cells',[]):
            points=camera.project_world([east-8,east+8,east+8,east-8],[north-8,north-8,north+8,north+8])
            od.polygon([tuple(p) for p in points],fill=255)
        overhang=ImageChops.subtract(mask,owned)
        result.append((source,mask,{'label':source['label'],'render_mesh_indices':indices,
            'indexed_triangles_projected':count,'projection_pixels':mask.histogram()[255],
            'projection_pixels_outside_owned_tiles':overhang.histogram()[255]}))
    if used!=set(range(len(model['meshes']))):
        raise ValueError('A placed model mesh is missing from the actual component outlines')
    return result


def draw_component_outlines(view, model, sources, camera, colours):
    """Draw a solid coloured silhouette above the independent tile boundaries."""
    result=view.convert('RGB');records=[]
    for source,mask,record in projected_component_masks(model,sources,camera,result.size):
        halo=ImageChops.subtract(mask.filter(ImageFilter.MaxFilter(7)),mask.filter(ImageFilter.MinFilter(7)))
        edge=ImageChops.subtract(mask.filter(ImageFilter.MaxFilter(3)),mask.filter(ImageFilter.MinFilter(3)))
        result.paste('white',(0,0),halo)
        result.paste(colours['palette'][source['label']],(0,0),edge)
        records.append(record)
    return result,{'enabled':True,'geometry_basis':'Union of actual placed first-frame indexed model triangles; independent of construction ownership and texture transparency.',
        'shared_ownership_camera':True,'line_width_pixels':2,'white_halo_width_pixels':6,
        'drawn_above_ownership_fills_and_boundaries':True,'components':records}
