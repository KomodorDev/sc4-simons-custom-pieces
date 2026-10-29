"""Keep the paired southern parapets straight until their ballast-curve joins.

The existing native floor, outside faces, curved roofs, northern wedges, and
all original encoded buffers remain intact. Only uncovered roof and inside
wall faces are added to the explicitly scoped, flat southern stem.
"""
from __future__ import annotations

from scp.dbpf import require
from scp.models import parse_s3d, pack_s3d
from scp.recipes import combine_meshes
from .directional_t import _partition_strict
from .rail_geometry import _route, _trim_sweep
from .single_track_models import _native, _pack, _quad
from .hsr_symmetric_parapet import _world, _uncovered


def repair_stem_models(native_hsr, models, mapping, alignment):
    """Add continuous raised tops and inside walls along both stem borders."""
    from .hsr_partition_components import _source
    require(alignment['branch_inner_half_width_m'] == 2.6
            and alignment['paired_centre_east_m'] == 16.
            and alignment['stem_scope_local_south_m'] == [48., 88.],
            'Symmetric HSR stem alignment differs from its scoped contract')
    require({(16.*(s[0]-l[0]), 16.*(s[1]-l[1])) for l, s in mapping.items()}
            == {(0., 96.)}, 'Symmetric HSR stem has an unexpected surface frame')
    source = _native(native_hsr)
    existing = _world(models)
    decks = {deck['name']: deck for deck in
             _source('hsr_component_modular_south_junction')['surface_context']['surface_decks']}
    native = [p for triangle in source['triangles'] for p in triangle]
    roof_u = [p[3] for p in native if abs(p[1]-source['top']) < 1e-4]
    wall_u = [p[3] for p in native if abs(abs(p[0])-source['inner']) < 1e-3]
    require(roof_u and wall_u, 'Symmetric HSR stem lacks native concrete material')
    roof_u, wall_u = sum(roof_u)/len(roof_u), sum(wall_u)/len(wall_u)
    bed, top = source['bed_y'], source['top']
    desired = []
    for name, side in ((alignment['left_branch'], 1.), (alignment['right_branch'], -1.)):
        deck = decks[name]
        require(deck['width'] == 8. and all(abs(p[2]-15.5) < 1e-8 for p in deck['points']),
                'Symmetric HSR stem requires the original flat eight-metre branches')
        points, _, miters = _route(deck['points'], deck.get('start_tangent'), deck.get('end_tangent'))
        curve = [(p[0]+side*2.6*n[0], p[2]-96.+side*2.6*n[1])
                 for p, n in zip(points, miters)]
        outer, inner = 16.-side*7.5, 16.-side*source['inner']
        planes = [(0, outer, side), (0, inner, -side), (2, 48., 1.), (2, 88., -1.)]
        for a, b in zip(curve, curve[1:]):
            roof = _quad([(outer, top, a[1], roof_u, -a[1]/16.),
                          (a[0], top, a[1], roof_u, -a[1]/16.),
                          (b[0], top, b[1], roof_u, -b[1]/16.),
                          (outer, top, b[1], roof_u, -b[1]/16.)], (0., 1., 0.))
            clipped = [t for _, t in _trim_sweep([('roof', t) for t in roof], [], planes)[0]]
            desired.extend(clipped)
            wall = _quad([(a[0], bed, a[1], wall_u, -a[1]/16.),
                          (a[0], top, a[1], wall_u, -a[1]/16.),
                          (b[0], top, b[1], wall_u, -b[1]/16.),
                          (b[0], bed, b[1], wall_u, -b[1]/16.)], (side, 0., 0.))
            desired.extend(t for _, t in _trim_sweep([('wall', t) for t in wall], [], planes)[0])
            # The same clipped roof vertices locate the straight inside face;
            # this ends exactly where the sampled branch line reaches it.
            for triangle in clipped:
                line = sorted({p[2] for p in triangle if abs(p[0]-inner) < 1e-7})
                if len(line) < 2 or line[-1]-line[0] < 1e-8:
                    continue
                lo, hi = line[0], line[-1]
                desired.extend(_quad([(inner, bed, lo, wall_u, -lo/16.),
                                      (inner, top, lo, wall_u, -lo/16.),
                                      (inner, top, hi, wall_u, -hi/16.),
                                      (inner, bed, hi, wall_u, -hi/16.)], (side, 0., 0.)))
    additions = []
    for triangle in desired:
        additions.extend(_uncovered(triangle, [*existing, *additions]))
    local = _partition_strict(additions, list(models))
    result = dict(models)
    for cell, triangles in local.items():
        if not triangles:
            continue
        original = parse_s3d(models[cell])
        added = parse_s3d(_pack(source, triangles))
        added['meshes'][0]['name'] = b'SCP HSR symmetric straight-to-ballast stem parapets\0'
        result[cell] = pack_s3d(combine_meshes([
            (original, original['meshes'], (0., 0., 0.)),
            (added, added['meshes'], (0., 0., 0.))]))
    return result
