"""Three functional whole-cell owners for the first physical DD RHW Y.

Rows run south. Every actual route, road surface, barrier, and support fragment
in a city tile is compiled into that tile's one owner. Model-only shoulders and
support cells carry an explicitly empty elevated PATH, never artificial lanes.
"""
from copy import deepcopy

GROUPS = {
    "diagonal-stem-split": {
        "id":"ddrhw-y-diagonal-stem-split",
        "name":"DD RHW-4 — Diagonal Two-Branch Stem — L1/L2",
        "recipe":"highway_ddrhw_y_diagonal_stem_split",
        "function":"Native diagonal two-lane split and reverse merge, with the south paired flat approaches",
        "world_cells":((-2,1),(-1,1),(0,1),(1,1),(2,1),(-1,2),(0,2),(-1,3)),
    },
    "diagonal-branch": {
        "id":"ddrhw-y-diagonal-branch",
        "name":"DD RHW-4 — Diagonal Branch and Paired Graded Links — L1/L2",
        "recipe":"highway_ddrhw_y_diagonal_branch",
        "function":"Native diagonal branch and the two separate lower-to-upper connections",
        "world_cells":((-1,-3),(-1,-2),(0,-2),(-2,-1),(-1,-1),(0,-1),(1,-1),(2,-1)),
    },
    "orthogonal-core": {
        "id":"ddrhw-y-orthogonal-core",
        "name":"DD RHW-4 — Orthogonal Y Connection Core — L1/L2",
        "recipe":"highway_ddrhw_y_orthogonal_core",
        "function":"Native orthogonal branch and the coordinated middle-band services",
        "world_cells":((-1,0),(0,0),(1,0),(2,0),(3,0)),
    },
}
PATH_CELLS={(-1,-2),(-1,-1),(0,-1),(1,-1),(2,-1),(-1,0),(0,0),(1,0),(2,0),(3,0),
            (-1,1),(0,1),(1,1),(-1,2)}


def owner(cell):
    matches=[key for key,row in GROUPS.items()if tuple(cell)in row["world_cells"]]
    if len(matches)!=1:
        raise ValueError(f"Y construction cell has no unique owner: {cell}")
    return matches[0]


def module_catalog():
    records=[]
    for key,row in GROUPS.items():
        cells=sorted(row["world_cells"],key=lambda c:(c[1],c[0]))
        origin=min(c[0]for c in cells),min(c[1]for c in cells)
        local=[[c[0]-origin[0],c[1]-origin[1]]for c in cells]
        records.append({**deepcopy(row),"key":key,"geometry_key":"y-"+key,
                        "world_cells":[list(c)for c in cells],"world_origin_cell":list(origin),"cells":local,
                        "footprint":[max(c[0]for c in local)+1,max(c[1]for c in local)+1],
                        "authors_surface_atlas":False,"engineering":{
                            "world_origin_cell":list(origin),"physical_model_function":row["function"],
                            "max_grade_percent":30.,"car_corridor_half_width_m":1.25,"car_corridor_height_m":3.8,
                            "pavement_path_offset_m":.001,"native_pavement_datums_m":[.0009999275207519531,.0010004043579101562],
                            "standard_deck_depth_m":1.,
                            "native_peer_shoulder_body_depth_m":{"upper":.9989995956420898,"lower":.999000072479248},
                            "single_lane_deck_width_m":6.,
                            "minimum_single_lane_deck_width_m":5.25,
                            "single_lane_asphalt_width_m":4.34375,
                            "minimum_single_lane_asphalt_width_m":3.59375,
                            "graded_inner_barrier_clearance_m":1.421875,
                            "model_only_cells":[[c[0]-origin[0],c[1]-origin[1]]for c in cells if c not in PATH_CELLS],
                            "model_overhang":True,"authored_model_overhang":False,
                            "path_ownership":"Every source route fragment in each owned city cell",
                            "native_phase":"first measured phase with common axis intersection (8,0) m",
                            "shadows_enabled":False}})
    occupied=sorted({tuple(c)for r in records for c in r["world_cells"]},key=lambda c:(c[1],c[0]))
    return {"types":records,"occupied_cells":[list(c)for c in occupied],"placement_count":3}


def declaration(spec):
    rows=[row for row in module_catalog()["types"]if row["recipe"]==spec["recipe"]]
    if len(rows)!=1:
        raise ValueError("Unknown or ambiguous Y recipe")
    row=rows[0]
    if spec.get("id")!=row["id"]or spec["cells"]!=row["cells"]or spec["footprint"]!=row["footprint"]:
        raise ValueError("Y type identity or allocated cells differ from its physical owner")
    return row
