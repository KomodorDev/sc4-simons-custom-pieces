"""Shared native HSR mesh compiler for independently placeable rail modules.

Keep overlapping decks at their authored elevations, preserve native texture
priority and coordinate slope-seated supports across each supplied layout.
"""
from __future__ import annotations

from functools import lru_cache
import json
import math

from scp.dbpf import require
from .directional_t import _floor_clip, _floor_subtract, _plan_area, _partition_strict
from .directional_diagonal_t import _floor_bucket_keys

SURFACE_TOLERANCE = 1e-4
FOUNDATION_HALF_WIDTH = .65
SUPPORT_MIN_SPACING = 16.


def _plane(triangle):
    """Return the actual triangle's height plane h = gx*x + gz*z + c."""
    a, b, c = triangle
    ux, uz, uy = b[0]-a[0], b[2]-a[2], b[1]-a[1]
    vx, vz, vy = c[0]-a[0], c[2]-a[2], c[1]-a[1]
    determinant = ux*vz-uz*vx
    require(abs(determinant) > 1e-12, 'HSR floor has no map area')
    gx, gz = (uy*vz-uz*vy)/determinant, (ux*vy-uy*vx)/determinant
    return gx, gz, a[1]-gx*a[0]-gz*a[2]



def _coplanar(first, second):
    """Test the actual overlap against both actual surface planes.

    Long nearly parallel triangles can agree over their small intersection
    while their remote ends diverge. Only shared area matters for joining.
    """
    one, two = _plane(first), _plane(second)
    if (all(abs(p[1]-(one[0]*p[0]+one[1]*p[2]+one[2])) <= SURFACE_TOLERANCE for p in second) and
            all(abs(p[1]-(two[0]*p[0]+two[1]*p[2]+two[2])) <= SURFACE_TOLERANCE for p in first)):
        return True
    boundary = list(second)
    if sum(a[0]*b[2]-b[0]*a[2] for a, b in zip(boundary, boundary[1:]+boundary[:1])) < 0.:
        boundary.reverse()
    overlap = list(first)
    for a, b in zip(boundary, boundary[1:]+boundary[:1]):
        overlap = _floor_clip(overlap, a, b, True)
        if len(overlap) < 3:
            return False
    return (_plan_area(overlap) > 1e-10 and
            all(abs((one[0]-two[0])*p[0]+(one[1]-two[1])*p[2]+one[2]-two[2]) <= SURFACE_TOLERANCE
                for p in overlap))



def _height_aware_union(triangles, *, single_sheet=False, tagged=False):
    """Union exact 4 m patches separately for every actual surface plane.

    Input order establishes UV priority: rail ribbons precede ballast. Exact
    clipping preserves coverage, slopes and interpolated native texture UVs.
    Native bed noise below 0.0001 m has the same definition as its donor
    classification; the 15 m separation of the bridge is never collapsed.

    ``single_sheet`` is used only within one of the reviewed,
    non-self-crossing deck sweeps. Its separately triangulated rail ribbons
    and ballast approximate one slightly warped slab, rather than two floors.
    Their projected texture overlap is therefore removed once. ``tagged``
    retains each fragment's rail/ballast identity for global rail priority.
    """
    accepted, buckets = [], {}
    for item in triangles:
        kind, triangle = item if tagged else (None, item)
        if _plan_area(list(triangle)) <= 1e-10:
            continue
        for cell in _floor_bucket_keys(triangle):
            left, right = 4.*cell[0], 4.*(cell[0]+1)
            lower, upper = 4.*cell[1], 4.*(cell[1]+1)
            polygon = list(triangle)
            for a, b in (((left, 0., 1.), (left, 0., 0.)),
                         ((right, 0., 0.), (right, 0., 1.)),
                         ((0., 0., lower), (1., 0., lower)),
                         ((1., 0., upper), (0., 0., upper))):
                polygon = _floor_clip(polygon, a, b, True)
            if len(polygon) < 3 or _plan_area(polygon) <= 1e-10:
                continue
            pieces = [polygon]
            previous = buckets.setdefault(cell, [])
            for other in previous:
                xmin, xmax = min(p[0] for p in other), max(p[0] for p in other)
                zmin, zmax = min(p[2] for p in other), max(p[2] for p in other)
                # Exact four-metre cells can contain many disjoint fragments
                # after a graded rail/ballast join. Reject those cheaply before
                # fitting planes and clipping their potential intersection.
                # This is precisely the same strict bounding-box predicate as
                # the fragment loop below; no kept face changes.
                if not single_sheet:
                    if not any(min(p[0] for p in piece) < xmax and max(p[0] for p in piece) > xmin and
                               min(p[2] for p in piece) < zmax and max(p[2] for p in piece) > zmin
                               for piece in pieces):
                        continue
                    if not _coplanar(triangle, other):
                        continue
                remaining = []
                for piece in pieces:
                    if (min(p[0] for p in piece) >= xmax or max(p[0] for p in piece) <= xmin or
                            min(p[2] for p in piece) >= zmax or max(p[2] for p in piece) <= zmin):
                        remaining.append(piece)
                    else:
                        remaining.extend(_floor_subtract(piece, list(other)))
                pieces = remaining
                if not pieces:
                    break
            for piece in pieces:
                for number in range(1, len(piece)-1):
                    part = (piece[0], piece[number], piece[number+1])
                    if _plan_area(list(part)) > 1e-10:
                        previous.append(part)
                        accepted.append((kind, part) if tagged else part)
    return accepted



class _Undersides:
    """Exact map-space triangle index used to seat every support head."""
    def __init__(self, triangles):
        self.buckets = {}
        for triangle in triangles:
            if _plan_area(list(triangle)) <= 1e-10:
                continue
            plane = _plane(triangle)
            for cell in _floor_bucket_keys(triangle):
                self.buckets.setdefault(cell, []).append((triangle, plane))

    def height(self, x, z):
        heights = []
        for triangle, plane in self.buckets.get((math.floor(x/4.), math.floor(z/4.)), []):
            sides = [(b[0]-a[0])*(z-a[2])-(b[2]-a[2])*(x-a[0])
                     for a, b in zip(triangle, (*triangle[1:], triangle[0]))]
            if min(sides) >= -1e-8 or max(sides) <= 1e-8:
                heights.append(plane[0]*x+plane[1]*z+plane[2])
        return min(heights) if heights else None

    def head(self, x, z):
        heights = [self.height(x+dx, z+dz)
                   for dz in (-FOUNDATION_HALF_WIDTH, 0., FOUNDATION_HALF_WIDTH)
                   for dx in (-FOUNDATION_HALF_WIDTH, 0., FOUNDATION_HALF_WIDTH)]
        if any(value is None or value <= .05 for value in heights):
            return None
        # A nine-point head is allowed to follow a bend or grade break. It may
        # not bridge the 15 m jump from a low deck to a separate upper deck.
        if max(heights)-min(heights) > .5:
            return None
        return heights



def _underside_geometry(decks, bottom=14.01067):
    """Build the same swept underside triangles without loading an atlas."""
    from .rail_geometry import _route
    from .single_track_models import _quad
    triangles = []
    for deck in decks:
        points, lengths, miters = _route(deck['points'], deck.get('start_tangent'), deck.get('end_tangent'))
        half = float(deck.get('width', 15.))/2.
        for index, (a, b) in enumerate(zip(points, points[1:])):
            na, nb = miters[index:index+2]
            polygon = [(point[0]+cross*normal[0], bottom+point[1]-15.5,
                        point[2]+cross*normal[1], .07, 0.)
                       for point, normal, cross in ((a, na, -half), (a, na, half),
                                                     (b, nb, half), (b, nb, -half))]
            triangles.extend(_quad(polygon, (0., -1., 0.)))
    return triangles



def support_centers(layout):
    """Select one coordinated support plan with at least 16 m spacing.

    Cell-centred candidates make the regular spans predictable. Additional
    centreline candidates cover curved narrow decks where the square city
    grid falls outside the slab. Every full head must touch a real underside.
    """
    from .rail_geometry import _global_decks
    decks = _global_decks(layout)
    undersides = _Undersides(_underside_geometry(decks))
    cells = set(layout)
    candidates = [(16.*x, 16.*row) for x, row in layout]
    for deck in decks:
        points = deck['points']
        distance, next_distance = 0., 0.
        for a, b in zip(points, points[1:]):
            length = math.hypot(b[0]-a[0], b[1]-a[1])
            while next_distance <= distance+length:
                fraction = max(0., min(1., (next_distance-distance)/length))
                candidates.append((a[0]+fraction*(b[0]-a[0]),
                                   -a[1]-fraction*(b[1]-a[1])))
                next_distance += 4.
            distance += length
    selected = []
    for x, z in candidates:
        if any((math.floor((x+dx+8.)/16.), math.floor((z+dz+8.)/16.)) not in cells
               for dx in (-FOUNDATION_HALF_WIDTH, 0., FOUNDATION_HALF_WIDTH)
               for dz in (-FOUNDATION_HALF_WIDTH, 0., FOUNDATION_HALF_WIDTH)):
            continue
        if any(math.hypot(x-a, z-b) < SUPPORT_MIN_SPACING-1e-8 for a, b in selected):
            continue
        if undersides.head(x, z) is None:
            continue
        selected.append((round(x, 9), round(z, 9)))
    return [(x, -z) for x, z in selected]



def _support(center, heights):
    """Construct a 1.3 m square pier with nine true underside contacts."""
    from .single_track_models import _quad
    x, z = center
    half = FOUNDATION_HALF_WIDTH
    top = [(x+dx, height, z+dz, .07+.035*dx/half, height/16.)
           for height, (dx, dz) in zip(heights,
                [(dx, dz) for dz in (-half, 0., half) for dx in (-half, 0., half)])]
    triangles = []
    for row in range(2):
        for col in range(2):
            index = row*3+col
            triangles.extend(_quad([top[index], top[index+1], top[index+4], top[index+3]], (0., 1., 0.)))
    base = [(x-half, 0., z-half, .035, 0.), (x+half, 0., z-half, .105, 0.),
            (x+half, 0., z+half, .105, 0.), (x-half, 0., z+half, .035, 0.)]
    triangles.extend(_quad(base, (0., -1., 0.)))
    for indices, normal in (((0, 1, 2), (0., 0., -1.)), ((2, 5, 8), (1., 0., 0.)),
                             ((8, 7, 6), (0., 0., 1.)), ((6, 3, 0), (-1., 0., 0.))):
        for first, last in zip(indices, indices[1:]):
            a, b = top[first], top[last]
            triangles.extend(_quad([(a[0], 0., a[2], a[3], 0.),
                                    (b[0], 0., b[2], b[3], 0.), b, a], normal))
    return triangles



def _expand_convex(polygon, margin):
    """Expand a convex wall-opening polygon by an exact outward margin."""
    if margin <= 0.:
        return polygon
    points = list(polygon)
    area = sum(a[0]*b[1]-b[0]*a[1] for a, b in zip(points, points[1:]+points[:1]))
    if area < 0.:
        points.reverse()
    lines = []
    for a, b in zip(points, points[1:]+points[:1]):
        dx, dz = b[0]-a[0], b[1]-a[1]
        length = math.hypot(dx, dz)
        if length < 1e-12:
            continue
        nx, nz = dz/length, -dx/length
        lines.append((nx, nz, nx*a[0]+nz*a[1]+margin))
    result = []
    for before, after in zip(lines[-1:]+lines[:-1], lines):
        nx, nz, value = before
        mx, mz, following = after
        determinant = nx*mz-nz*mx
        if abs(determinant) < 1e-12:
            continue
        result.append(((value*mz-nz*following)/determinant,
                       (nx*following-value*mx)/determinant))
    require(len(result) >= 3, 'HSR wall-opening polygon collapsed')
    return result



def _sweep_native_profile(source, deck):
    """Sweep an 8 m single slab, then open its authored 5.2 m train corridor.

    The shared native profile retains approximately 5 m inside this width and
    deliberately rejects a larger mask.  For this new recipe only, cutting
    a little over 0.1 m from each parapet's inside face supplies the stated
    clearance margin.  The outer slab, native rail ribbons and all existing
    piece generators remain unchanged.
    """
    from .rail_geometry import _sweep
    requested = float(deck.get('clearance_half_width', 2.6))
    copied = dict(deck)
    width = float(copied.get('width', 15.))
    actual = requested
    if width != 15.:
        require(abs(width-8.) < 1e-8, 'HSR single-track slabs must be exactly 8 m wide')
        native_inset = source['outer']-source['inner']
        actual = min(requested, width/2.-native_inset-.000001)
        copied['clearance_half_width'] = actual
    surfaces, corridors, points, lengths = _sweep(source, copied, False)
    if requested > actual:
        for corridor in corridors:
            corridor['clearance_polygons'] = [_expand_convex(polygon, requested-actual)
                for polygon in corridor.get('clearance_polygons', [])]
        surfaces.extend(_inner_wall_faces(source, deck, requested))
    return surfaces, corridors, points, lengths



def _inner_wall_faces(source, deck, half_width):
    """Close the inside of each trimmed parapet with its native concrete UVs."""
    from .rail_geometry import _route, _trim_sweep
    from .single_track_models import _quad
    points, lengths, miters = _route(deck['points'], deck.get('start_tangent'), deck.get('end_tangent'))
    native = [vertex for triangle in source['triangles'] for vertex in triangle
              if abs(abs(vertex[0])-source['inner']) < 1e-3]
    top = [v[3] for v in native if abs(v[1]-source['top']) < 1e-3]
    bed = [v[3] for v in native if abs(v[1]-source['bed_y']) < 1e-3]
    require(top and bed, 'HSR native inside-wall UV donor is missing')
    top_u, bed_u = sum(top)/len(top), sum(bed)/len(bed)
    scopes = []
    for axis, boundary, sign, endpoint in deck.get('scoped_clip_planes', []):
        selected = set()
        indices = range(len(lengths)) if endpoint == 0 else reversed(range(len(lengths)))
        for number in indices:
            selected.add(number)
            if min(sign*(point[axis]-boundary) for point in points[number:number+2]) >= float(deck.get('width', 8.)):
                break
        scopes.append(((axis, boundary, sign), selected))
    surfaces, distance = [], float(deck.get('uv_offset', 0.))
    for number, (a, b, length) in enumerate(zip(points, points[1:], lengths)):
        na, nb = miters[number:number+2]
        additions = []
        for sign in (-1., 1.):
            vertices = [(point[0]+sign*half_width*normal[0],
                         point[1]-15.5+height,
                         point[2]+sign*half_width*normal[1], u, -span/16.)
                        for point, normal, height, u, span in (
                            (a, na, source['bed_y'], bed_u, distance),
                            (a, na, source['top'], top_u, distance),
                            (b, nb, source['top'], top_u, distance+length),
                            (b, nb, source['bed_y'], bed_u, distance+length))]
            additions.extend(('inner_wall', triangle) for triangle in _quad(
                vertices, (-sign*na[0], 0., -sign*na[1])))
        planes = [*deck.get('clip_planes', []),
                  *(plane for plane, selected in scopes if number in selected)]
        if planes:
            additions = _trim_sweep(additions, [], planes)[0]
        surfaces.extend(additions)
        distance += length
    return surfaces



def _surface_triangles(source, decks, sweep):
    """Create ordered surfaces before module-specific cuts and supports."""
    from .rail_geometry import _index_corridors, _subtract_corridors
    swept = [sweep(source, deck) for deck in decks]
    triangles = []
    for index, (surfaces, corridors, _, _) in enumerate(swept):
        other_corridors = _index_corridors(
            [corridor for number, other in enumerate(swept) if number != index
             for corridor in other[1]], True)
        own_clearance = _index_corridors(
            [{**corridor, 'polygon': polygon} for corridor in corridors
             for polygon in corridor.get('clearance_polygons', [])], True)
        for kind, triangle in surfaces:
            if kind in ('bed', 'rail', 'underside'):
                continue
            for fragment in _subtract_corridors(triangle, other_corridors, wall=True):
                if kind == 'inner_wall':
                    triangles.append(fragment)
                else:
                    triangles.extend(_subtract_corridors(fragment, own_clearance, wall=True))
    # A graded, turning sweep makes a slightly warped quad. Its narrow rail
    # strip and wide ballast use different diagonals and therefore slightly
    # different planes. Join those texture layers within that single slab
    # first; comparing source planes alone leaves tiny ballast fragments over
    # a rail after later grid cuts. The supplied physical sweeps must be noncrossing
    # single sheets. Independent bridge tiers remain separate in the global
    # height-aware pass, and rail priority survives between all decks.
    own_floors = [_height_aware_union(
        [(kind, triangle) for kind in ('rail', 'bed')
         for actual, triangle in surfaces if actual == kind],
        single_sheet=True, tagged=True) for surfaces, _, _, _ in reversed(swept)]
    floors = [triangle for kind in ('rail', 'bed') for surfaces in own_floors
              for actual, triangle in surfaces if actual == kind]
    undersides = [triangle for surfaces, _, _, _ in reversed(swept)
                  for kind, triangle in surfaces if kind == 'underside']
    triangles.extend(_height_aware_union(floors))
    triangles.extend(_height_aware_union(undersides))
    return triangles, undersides


@lru_cache(maxsize=2)
def _cached_surface_triangles(native_hsr, deck_signature, sweep):
    """Share exact analytical surfaces, never selected tile models.

    Keys include the immutable native donor bytes, every serialized deck
    setting and the actual sweep callable. Cell ownership, output packing
    and supports stay outside this cache and are evaluated for each module.
    Two contexts bound memory while allowing adjacent modules to share work.
    Returned nested tuples cannot be mutated by a later module compiler.
    """
    from .single_track_models import _native
    triangles, undersides = _surface_triangles(_native(native_hsr), json.loads(deck_signature), sweep)
    freeze = lambda faces: tuple(tuple(tuple(vertex) for vertex in face) for face in faces)
    return freeze(triangles), freeze(undersides)


def _compile_models(native_hsr, layout, config, *, sweep_function=None):
    from scp.models import parse_s3d, pack_s3d
    from .rail_geometry import _global_decks, _pack_junction
    from .single_track_models import _native, _pack
    from scp.recipes import combine_meshes
    source = _native(native_hsr)
    decks = config['surface_decks'] if 'surface_decks' in config else _global_decks(layout)
    sweep = _sweep_native_profile if sweep_function is None else sweep_function
    if 'surface_decks' in config:
        signature = json.dumps(decks, sort_keys=True, separators=(',', ':'), allow_nan=False)
        triangles, undersides = _cached_surface_triangles(native_hsr, signature, sweep)
    else:
        triangles, undersides = _surface_triangles(source, decks, sweep)
    # A module may retain a larger sweep boundary mask solely to preserve
    # deterministic ownership of tiny overhangs. Pack only its emitted cells.
    partition_cells = [tuple(cell) for cell in config.get('surface_partition_cells', list(layout))]
    result = {cell: _pack_junction(source, parts)
              for cell, parts in _partition_strict(triangles, partition_cells).items()
              if cell in layout}
    underside_index = _Undersides(undersides)
    for x, north in config['support_centers']:
        z = -north
        heights = underside_index.head(x, z)
        require(heights is not None, 'HSR support does not seat on all nine underside points')
        cell = math.floor((x+8.)/16.), math.floor((z+8.)/16.)
        require(cell in result, 'HSR support foundation is outside the reserved cells')
        local = [(xv-16.*cell[0], h, zv-16.*cell[1], u, v)
                 for triangle in _support((x, z), heights) for xv, h, zv, u, v in triangle]
        support_triangles = [tuple(local[index:index+3]) for index in range(0, len(local), 3)]
        support = parse_s3d(_pack(source, support_triangles))
        support['meshes'][0]['name'] = b'SCP HSR component consolidated slope-seated support\0'
        model = parse_s3d(result[cell])
        result[cell] = pack_s3d(combine_meshes([
            (model, model['meshes'], (0., 0., 0.)),
            (support, support['meshes'], (0., 0., 0.))]))
    return result
