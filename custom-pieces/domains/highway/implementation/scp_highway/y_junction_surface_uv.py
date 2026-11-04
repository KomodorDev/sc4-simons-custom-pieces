"""Texture-only partitions for the Y junction's existing flat asphalt.

The caller supplies the actual parent fan polygons and the already masked
asphalt. This module neither rebuilds physical road unions nor touches copied
native faces. Each returned domain has one material, one route owner, and one
fixed texture field; a triangle never chooses a different route per vertex.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
import math

import numpy as np
import shapely
from shapely.geometry import MultiPoint, Polygon
from shapely.ops import unary_union
from shapely.strtree import STRtree


NATIVE_FAN_END_M = 13.0
EDGE_MARKING_BLEND_M = 6.0
EDGE_MARKING_INSET_M = 0.21875
# Centres of the visible paint bands in the pinned 128-pixel NAM textures.
MIS_WHITE_U, MIS_YELLOW_U = 45.0 / 128.0, 80.5 / 128.0
DD_WHITE_U, DD_YELLOW_U = 28.0 / 128.0, 97.5 / 128.0


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def _parts(geometry):
    if geometry.is_empty:
        return []
    if geometry.geom_type == 'Polygon':
        return [geometry]
    return [part for child in geometry.geoms for part in _parts(child)] if hasattr(geometry, 'geoms') else []


@dataclass(frozen=True)
class AffineUV:
    """Map east/north coordinates to one fixed U/V texture frame."""
    coefficients: tuple

    def __call__(self, point):
        east, north = float(point[0]), float(point[1])
        return tuple(east * self.coefficients[0][i] + north * self.coefficients[1][i]
                     + self.coefficients[2][i] for i in (0, 1))


def _field(coefficients):
    matrix = np.asarray(coefficients, dtype=float)
    _require(matrix.shape == (3, 2) and np.isfinite(matrix).all(), 'Flat asphalt UV field must be finite and affine')
    return AffineUV(tuple(tuple(float(value) for value in row) for row in matrix))


@dataclass(frozen=True)
class NativePaintJoin:
    origin: tuple
    inward: tuple
    native_u: tuple
    ribbon_stripe_u: float
    native_stripe_u: float


@dataclass(frozen=True)
class RibbonMarkings:
    stations: np.ndarray
    left_stripe_m: np.ndarray
    right_stripe_m: np.ndarray
    joins: tuple
    reverse_traffic: bool

    def __call__(self, point, uv):
        """Keep V and adjust the two edge lines within the exposed asphalt."""
        u, v = uv
        station = 16.0 * v
        if self.reverse_traffic:
            station = self.stations[-1] - station
        lateral = 16.0 * (u - 0.5)
        left = np.interp(station, self.stations, self.left_stripe_m)
        right = np.interp(station, self.stations, self.right_stripe_m)
        ribbon_u = MIS_WHITE_U + (MIS_YELLOW_U - MIS_WHITE_U) * (lateral + right) / (left + right)
        east, north = point
        for join in self.joins:
            ox, oy = join.origin
            nx, ny = join.inward
            inward_m = (east - ox) * nx + (north - oy) * ny
            if inward_m >= NATIVE_FAN_END_M + EDGE_MARKING_BLEND_M:
                continue
            fraction = max(0.0, (inward_m - NATIVE_FAN_END_M) / EDGE_MARKING_BLEND_M)
            blend = fraction * fraction * (3.0 - 2.0 * fraction)
            a, b, c = join.native_u
            native_u = a * east + b * north + c
            # The native outer line keeps its world position at the cut. A
            # shallower U gradient keeps the other stripe outside the lane
            # there, so the native centre divider ends in its existing gap.
            aligned_u = join.ribbon_stripe_u + 0.8 * (native_u - join.native_stripe_u)
            return (1.0 - blend) * aligned_u + blend * ribbon_u, v
        return ribbon_u, v


def ribbon_markings(roads, profiles, sockets, barrier_inset, *, reverse_traffic=False):
    """Bind one exterior paint line to each lane at each native DD mouth."""
    lanes = defaultdict(list)
    joins = defaultdict(list)
    for road in roads:
        for arm, index in zip(road['id'].split('-'), (0, -1)):
            east, north, height = road['points'][index]
            deck = 'upper' if height == 15.0 else 'lower'
            a, b, c = profiles[arm, deck]['coefficients'][:, 0]
            lanes[arm, deck].append((float(a * east + b * north + c), road['id']))
    for (arm, deck), members in lanes.items():
        _require(len(members) == 2 and members[0][0] != members[1][0],
                 'Y native paint join requires two distinct same-deck lanes')
        right, left = sorted(members)
        socket = sockets[arm]
        native_u = tuple(profiles[arm, deck]['coefficients'][:, 0])
        for (_, route), ribbon_u, dd_u in ((right, MIS_WHITE_U, DD_WHITE_U),
                                          (left, MIS_YELLOW_U, DD_YELLOW_U)):
            joins[route].append(NativePaintJoin(socket['point'], socket['inward'], native_u, ribbon_u, dd_u))

    fields = {}
    for road in roads:
        normals = road['normals']
        normal_squared = np.sum(normals * normals, axis=1)
        right_clear = (-road['low_offsets']
                       - barrier_inset * np.sum(normals * road['inward_low'], axis=1) / normal_squared)
        left_clear = (road['high_offsets']
                      + barrier_inset * np.sum(normals * road['inward_high'], axis=1) / normal_squared)
        if reverse_traffic:
            right_clear, left_clear = left_clear, right_clear
        right = np.minimum(2.375, right_clear - EDGE_MARKING_INSET_M)
        left = np.minimum(2.0625, left_clear - EDGE_MARKING_INSET_M)
        _require(np.all(right > 0.0) and np.all(left > 0.0) and len(joins[road['id']]) == 2,
                 'Y paint field requires exposed asphalt and two native joins')
        fields[road['id']] = RibbonMarkings(road['station'], left, right, tuple(joins[road['id']]), reverse_traffic)
    return fields


class RibbonUV:
    """Evaluate only one fixed route's continuous, finite ribbon frames."""

    def __init__(self, frames):
        self.frames = frames
        self.tree = STRtree([frame['geometry'] for frame in frames])

    def __call__(self, point):
        from shapely.geometry import Point
        query = Point(float(point[0]), float(point[1]))
        candidates = [int(index) for index in self.tree.query(query)
                      if self.frames[int(index)]['geometry'].covers(query)]
        if candidates:
            index = min(candidates)
        else:
            index = int(self.tree.nearest(query))
            _require(self.frames[index]['geometry'].distance(query) <= 1e-7,
                     'Flat texture query left its fixed route ribbon')
        return self.frames[index]['uv'](point)


def _route_frames(road, deck):
    """Use finite source chords and the exact end UVs used by graded ribbons."""
    points = np.asarray(road['points'], dtype=float)
    normals = np.asarray(road['normals'], dtype=float)
    stations = np.asarray(road['station'], dtype=float)
    low, high = np.asarray(road['rail_low']), np.asarray(road['rail_high'])
    _require(points.ndim == 2 and points.shape[1] == 3 and len(points) >= 2
             and normals.shape == (len(points), 2) and stations.shape == (len(points),)
             and low.shape == high.shape == (len(points), 2), 'Flat asphalt requires complete actual route frames and rails')
    _require(all(np.isfinite(array).all() for array in (points, normals, stations, low, high)),
             'Flat asphalt route frames contain a nonfinite value')
    altitude = 15. if deck == 'upper' else 7.5
    frames, sites = [], []
    for index, (first, last) in enumerate(zip(points, points[1:])):
        if max(abs(first[2] - altitude), abs(last[2] - altitude)) > 1e-7:
            continue
        length = math.dist(first[:2], last[:2])
        _require(length > 1e-10 and stations[index + 1] > stations[index], 'Flat asphalt has a stationary route chord')
        for sample in range(math.ceil(length) + 1):
            fraction = sample / math.ceil(length)
            sites.append(tuple(float(value) for value in first[:2] + fraction * (last[:2] - first[:2])))
        for side, outer in ((-1, low), (1, high)):
            vertices, uvs = [], []
            for endpoint, xy in ((0, outer[index]), (1, outer[index + 1]),
                                 (1, last[:2]), (0, first[:2])):
                at = index + endpoint
                normal = normals[at]
                denominator = float(normal @ normal)
                _require(denominator > 1e-12, 'Flat asphalt route has a zero lateral frame')
                offset = float((xy - points[at, :2]) @ normal) / denominator
                vertices.append(tuple(float(value) for value in xy))
                uvs.append((.5 + offset / 16., float(stations[at]) / 16.))
            for triangle_number, indices in enumerate(((0, 1, 2), (0, 2, 3))):
                coordinates = np.array([[*vertices[i], 1.] for i in indices])
                if abs(float(np.linalg.det(coordinates))) <= 1e-15:
                    continue
                geometry = Polygon([vertices[i] for i in indices])
                coefficients = np.linalg.solve(coordinates, np.array([uvs[i] for i in indices]))
                frames.append({'geometry': geometry, 'uv': _field(coefficients),
                               'frame': {'route': road['id'], 'chord': index, 'side': side, 'triangle': triangle_number}})
    return frames, sites


def flat_surface_domains(asphalt_polygon, roads, deck, profiles, parent_mouths):
    """Partition supplied asphalt into fixed native or route texture domains.

    ``parent_mouths`` contains ``{arm, deck, geometry}`` records copied from
    the caller's actual physical fan/taper construction. Native affine fields
    cover those complete mouths, including their taper. Other asphalt uses
    fixed route ownership from a deterministic, at-most-one-metre sampled
    Voronoi partition, restricted to each route's actual ribbon. Its field
    interpolates exact chord-end stations and lateral frames within that
    same owner. No additional triangle subdivision is requested: existing
    source curve boundaries already carry dense longitudinal samples.
    This changes texture ownership only; it cannot cross-fade two different
    native materials or establish their final pixel appearance.
    """
    _require(deck in ('upper', 'lower'), 'Unknown flat asphalt deck')
    _require(asphalt_polygon.is_valid, 'Flat asphalt input must retain its valid physical polygon')
    if asphalt_polygon.is_empty:
        return []
    domains, pending = [], asphalt_polygon
    mouths = defaultdict(list)
    for mouth in parent_mouths:
        if mouth['deck'] == deck:
            _require(mouth['arm'] in ('A', 'B', 'C'), 'Unknown native asphalt mouth')
            mouths[mouth['arm']].append(mouth['geometry'])
    for arm in sorted(mouths):
        geometry = pending.intersection(unary_union(mouths[arm]))
        if geometry.is_empty:
            continue
        uv = _field(profiles[arm, deck]['coefficients'])
        domains.extend({'geometry': part, 'owner': 'native-' + arm,
                        'material_role': f'pavement-native-{arm}-{deck}', 'uv': uv,
                        'frame': {'native_arm': arm, 'deck': deck}}
                       for part in _parts(geometry))
        pending = pending.difference(geometry)
    if pending.is_empty:
        return domains

    route_records, site_owners, site_bins = {}, {}, defaultdict(list)
    for road in sorted(roads, key=lambda row: row['id']):
        _require(road['id'] not in route_records, 'Flat asphalt route owners must be unique')
        frames, sites = _route_frames(road, deck)
        if not frames:
            continue
        route_records[road['id']] = {'frames': frames, 'geometry': unary_union([frame['geometry'] for frame in frames])}
        for site in sites:
            # Consecutive source chords can compute their shared endpoint
            # with different last-bit arithmetic. Deduplicate only these
            # owner sampling sites, including across a spatial bin border;
            # actual asphalt and ribbon vertices are never moved.
            grid = tuple(math.floor(value / 1e-6) for value in site)
            nearby = [point for x in (-1, 0, 1) for y in (-1, 0, 1)
                      for point in site_bins[grid[0] + x, grid[1] + y]
                      if math.dist(site, point) <= 1e-7]
            if not nearby:
                site_owners[site] = road['id']
                site_bins[grid].append(site)
    _require(route_records, 'Flat asphalt has no finite same-deck route owner')
    sites = sorted(site_owners)
    cells = shapely.voronoi_polygons(MultiPoint(sites), extend_to=pending.envelope, ordered=True)
    voronoi = defaultdict(list)
    for site, cell in zip(sites, cells.geoms):
        # Cocircular/collinear samples can give an auxiliary cell a zero-area
        # self-touch far outside the asphalt. Normalize that owner mask only;
        # it is subsequently clipped to the unchanged physical input.
        if not cell.is_valid:
            cell = shapely.make_valid(cell)
        voronoi[site_owners[site]].append(cell)
    assigned, rest = {}, pending
    for owner, record in route_records.items():
        # Adjacent Voronoi cells can differ in their last arithmetic bits.
        # Node this texture-owner mask on a 1 nm grid before clipping the
        # unchanged actual asphalt. Subtracting from ``rest`` makes owner
        # domains disjoint even across a mask's numerical grid boundary.
        mask = shapely.union_all(voronoi[owner], grid_size=1e-9)
        region = rest.intersection(mask).intersection(record['geometry'])
        assigned[owner] = region
        rest = rest.difference(region)
    # A narrower ribbon can make a nearer route ineligible. Assign only the
    # uncovered portions of actual source ribbons, without enlarging asphalt.
    for owner, record in route_records.items():
        extra = rest.intersection(record['geometry'])
        assigned[owner] = assigned[owner].union(extra)
        rest = rest.difference(extra)
    # The physical union uses a 1 nm input grid. Preserve its exact input
    # polygon while extending each fixed UV field only across that boundary.
    for owner, record in route_records.items():
        if rest.is_empty:
            break
        piece = rest.intersection(record['geometry'].buffer(1e-7))
        assigned[owner] = assigned[owner].union(piece)
        rest = rest.difference(piece)
    _require(not _parts(rest), 'Flat asphalt is outside the supplied actual route ribbons and native mouths')
    for owner, region in assigned.items():
        uv = RibbonUV(route_records[owner]['frames'])
        domains.extend({'geometry': part, 'owner': owner, 'material_role': 'pavement',
                        'uv': uv, 'frame': {'route': owner}, 'maximum_edge_m': None}
                       for part in _parts(region))
    # Boolean overlays can leave a last-bit seam between two owner polygons.
    # Attach only that existing input-asphalt sliver to an adjacent domain;
    # this neither expands the physical asphalt nor creates extra UV pieces.
    missing = asphalt_polygon.difference(unary_union([domain['geometry'] for domain in domains]))
    for domain in domains:
        if missing.is_empty:
            break
        seam = missing.intersection(domain['geometry'].buffer(1e-7))
        domain['geometry'] = domain['geometry'].union(seam)
        missing = missing.difference(seam)
    _require(not _parts(missing), 'Flat texture partition lost part of its unchanged input asphalt')
    return domains
