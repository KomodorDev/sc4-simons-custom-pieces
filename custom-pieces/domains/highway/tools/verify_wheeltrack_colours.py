#!/usr/bin/env python3
"""Audit actual saved wheeltrack UVs and pinned native RGB; never install."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

LIBRARY=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(LIBRARY/'framework'))
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0,SourcePackages(LIBRARY))
from scp import jsonc
from scp.preview import TextureLibrary
from scp.verify import strict_dbpf
from scp_highway.assembly_verify import check_owned_cells,decode_placed_routes,check_saved_routes
from scp_highway.wheeltrack_verify import (DD,MIS,reviewed_paths,corridor_regions,saved_faces,
                                         check_uv,audit_native_rgb,export_corridors)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build',type=Path,required=True)
    parser.add_argument('--plugins',type=Path,required=True,help='Explicit installed NAM texture root; read only')
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--reference',type=Path,help='Frozen marking build, required with --corridor-output')
    parser.add_argument('--corridor-output',type=Path)
    args=parser.parse_args()
    if args.corridor_output and not args.reference:
        parser.error('--corridor-output requires --reference')
    raw=(args.build/'manifest.json').read_bytes();manifest=json.loads(raw)
    scene=jsonc.load(LIBRARY/'domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/assembly.jsonc')
    owners,_=check_owned_cells({p['id']:p for p in manifest['pieces']},scene)
    resources={p['id']:strict_dbpf((args.build/p['asset_file']).read_bytes()) for p in manifest['pieces']}
    routes=decode_placed_routes(owners,resources);path_report,_=check_saved_routes(routes,owners)
    paths=reviewed_paths(routes,path_report);regions=corridor_regions(paths);faces=saved_faces(owners,resources)
    uv=check_uv(faces,paths,regions)
    texture_library=TextureLibrary(args.plugins)
    dummy={'meshes':[{'frames':[(0,0,0,i)]} for i in (0,1)],
           'materials':[{'textures':[DD]},{'textures':[MIS]}]}
    textures,provenance=texture_library.for_model(dummy)
    rgb=audit_native_rgb(faces,paths,textures,provenance)
    result={'schema_version':1,'purpose':'Independent actual-saved pavement UV and explicit pinned-native RGB audit.',
            'build_manifest_sha256':hashlib.sha256(raw).hexdigest(),'uv':uv,'native_rgb':rgb,
            'native_inputs':'Explicit read-only NAM texture root; private paths omitted.',
            'installed':False,'in_game_tested':False,'native_pixels_included':False}
    if args.corridor_output:
        contract=export_corridors(owners,regions,hashlib.sha256((args.reference/'manifest.json').read_bytes()).hexdigest(),result['build_manifest_sha256'])
        args.corridor_output.parent.mkdir(parents=True,exist_ok=True)
        args.corridor_output.write_text(json.dumps(contract,indent=2,sort_keys=True)+'\n')
        result['independent_corridor_contract_sha256']=hashlib.sha256(args.corridor_output.read_bytes()).hexdigest()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'passed':True,'seam_uv_controls':uv['seam_controls_checked'],
                      **{k:v for k,v in rgb.items() if k.startswith('maximum_')},
                      'installed':False,'in_game_tested':False},sort_keys=True))


if __name__=='__main__':main()
