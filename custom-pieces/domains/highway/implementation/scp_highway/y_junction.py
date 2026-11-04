"""Compile each whole-cell Y owner into actual S3D and elevated car PATHs."""
from collections import defaultdict
from copy import deepcopy

from scp.dbpf import require
from scp.models import parse_s3d,pack_s3d
from . import y_junction_geometry as geometry
from . import y_junction_layout as layout
from . import ramp_paths,orthogonal_transition
from .y_junction_variants import ORIGINAL, REVERSED, variant_of


def _native_contact(route,world,variant=ORIGINAL):
    point_a,point_b=route["points"][0],route["points"][-1]
    values=[(point_a[0]+16*world[0],point_a[1]-16*world[1],point_a[2]),
            (point_b[0]+16*world[0],point_b[1]-16*world[1],point_b[2])]
    if variant == REVERSED:
        from .y_junction_reversed_source import source_routes
    else:
        require(variant == ORIGINAL, "Unknown Y PATH encoding variant")
        source_routes = geometry.source_routes
    source={row["id"]:row for row in source_routes()}[route["id"]]
    return any(all(abs(point[k]-target[k])<1e-7 for k in range(3))
               for point in values for target in(source["points"][0],source["points"][-1]))


def encode_paths(routes,world,variant=ORIGINAL):
    """Reserve exterior native classes before allocating distinct inner classes."""
    ordered=sorted(deepcopy(routes),key=lambda r:(not _native_contact(r,world,variant),r["id"]))
    used=defaultdict(set)
    lines=["SC4PATHS","1.2",str(len(ordered)),"0","1"]
    for route in ordered:
        pair=route["transport"],route["entry"],route["exit"]
        lane=route["lane"]
        if _native_contact(route,world,variant):
            require(lane not in used[pair],"Two native Y contacts request one engine lane class")
        else:
            while lane in used[pair]:lane+=1
        used[pair].add(lane)
        lines += [f"-- SCP Y {route['id']} source_lane={route['lane']}",str(route["transport"]),str(lane),
                  str(route["entry"]),str(route["exit"]),"0",str(len(route["points"]))]
        lines += [",".join(format(float(value),".9f").rstrip("0").rstrip(".")if value else"0"for value in point)
                  for point in route["points"]]
    return ("\r\n".join(lines)+"\r\n").encode("ascii")


def compile_module(spec,context):
    variant = variant_of(spec)
    if variant == REVERSED:
        from . import y_junction_reversed_layout as selected_layout
        from .y_junction_reversed_geometry import world_geometry
    else:
        selected_layout, world_geometry = layout, geometry.world_geometry
    record=selected_layout.declaration(spec)
    world=world_geometry(context)
    declared={tuple(c)for c in selected_layout.module_catalog()["occupied_cells"]}
    require(declared==set(world["tiles"]),"Physical Y model mask differs from its frozen module catalogue")
    require(selected_layout.PATH_CELLS==set(world["paths"]),"Y route mask differs from its frozen model-only declaration")
    origin=record["world_origin_cell"]
    output=[]
    for local in map(tuple,spec["cells"]):
        cell=local[0]+origin[0],local[1]+origin[1]
        raw=orthogonal_transition._pack_model(world["tiles"][cell],world["painter"],world["template"])
        model=parse_s3d(raw)
        for mesh in model["meshes"]:
            mesh["name"]=mesh["name"].replace(b"SCP DD transition ",b"SCP DD Y ",1)
        output.append((local,pack_s3d(model),encode_paths(world["paths"].get(cell,[]),cell,variant)))
    return output


def construction_fields(spec,compiled):
    width,depth=spec["footprint"]
    rows=[["."]*(width+2)for _ in range(depth+1)]
    cons=deepcopy(rows)
    rows[0][-1]=cons[0][-1]="<"
    rows[-1][0]=cons[-1][0]="^"
    checks=[]
    from scp.verify import parse_paths
    for index,(cell,_model,raw)in enumerate(compiled):
        symbol=ramp_paths.construction_symbol(index)
        rows[cell[1]][cell[0]]=symbol
        cons[cell[1]][cell[0]]="+"
        routes=[ramp_paths._route_metadata(route,"saved-Y")for route in parse_paths(raw)["routes"]]
        checks.append(f"{symbol} - dirtroad: 0x{ramp_paths.construction_flags(routes):08X}")
    return ["".join(row)for row in rows],checks,["".join(row)for row in cons]


def build_piece(spec,context):
    from .recipes import finish_piece,construction
    from .y_junction_approaches import add_approaches
    from .model_shadows import add_shadows
    compiled=compile_module(spec,context)
    assets=finish_piece(spec,context,compiled)
    rows,checks,cons=add_approaches(spec,*construction_fields(spec,compiled))
    return add_shadows(spec,context,compiled,assets),construction(spec,rows,checks,cons)
