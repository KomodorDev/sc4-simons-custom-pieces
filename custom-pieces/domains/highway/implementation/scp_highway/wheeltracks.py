"""Continue native tyre wear through the flat auxiliary-lane pavement.

The existing DD asphalt atlas contains the MIS ramp's native tyre trough.
Only original DD top faces within the accepted ramp's swept six-metre strip
and the 4.5..8 m auxiliary shoulder are subdivided and remapped. All output
UVs stay inside the unmarked second-lane asphalt; no image is copied or made.
"""
from __future__ import annotations

from bisect import bisect_right
from collections import defaultdict
import math

from .ramp_geometry import _clip, _normal, _subtract_convex, _triangulate, route_frames

INNER_Q = 4.5
OUTER_Q = 8.0
HALF_WIDTH = 3.0
MAXIMUM_TEXTURE_EDGE = 0.125
SAFE_DD_COLUMNS = (65.0, 95.0)


def _ease(value):
    t = min(1.0, max(0.0, value))
    return t * t * (3.0 - 2.0 * t)


def _inside(polygon, boundary):
    for first, last in zip(boundary, boundary[1:] + boundary[:1]):
        length = math.dist(first, last)
        if length <= 1e-10:
            continue
        polygon = _clip(polygon, lambda p, a=first, b=last, length=length:
                        ((b[0] - a[0]) * (p[2] - a[1])
                         - (b[1] - a[1]) * (p[0] - a[0])) / length)
        if len(polygon) < 3:
            return []
    return polygon


def _split_crossing_sweep(polygon):
    """Return the exact two lobes of a folded four-corner sweep.

    A tight offset can cross itself even though the accepted PATH does not.
    Convex half-plane clipping cannot represent that bowtie. Split at its
    actual nonadjacent-edge intersection, preserving the even-odd footprint
    rather than filling its convex hull. Uncrossed sweeps remain unchanged.
    """
    for shift in (0, 1):
        a, b, c, d = polygon[shift:] + polygon[:shift]
        rx, rz = b[0] - a[0], b[2] - a[2]
        sx, sz = d[0] - c[0], d[2] - c[2]
        determinant = rx * sz - rz * sx
        if abs(determinant) <= 1e-14:
            continue
        dx, dz = c[0] - a[0], c[2] - a[2]
        first = (dx * sz - dz * sx) / determinant
        second = (dx * rz - dz * rx) / determinant
        if 1e-10 < first < 1.0 - 1e-10 and 1e-10 < second < 1.0 - 1e-10:
            intersection = tuple(x + first * (y - x) for x, y in zip(a, b))
            return [[intersection, b, c], [intersection, d, a]]
    return [polygon]


class NativeWheeltrackField:
    """A phase-continuous native asphalt field on existing shoulder faces.

    Separate negative/positive lateral half-ribbons may have different UVs
    at the same centre vertex during the intensity ease. Cutting them first
    prevents interpolation between their opposite neutral atlas edges.
    The two solutions meet in the same native dark trough after the ease.
    """

    def __init__(self, ramps, painter, *, retain_nonzero_top_fragments=False):
        self.painter = painter
        self.retain_nonzero_top_fragments = retain_nonzero_top_fragments
        self.regions = []
        self.buckets = defaultdict(list)
        self.stations = {
            owner: [painter.segments[index][2] for index in indices]
            for owner, indices in painter.road_segments.items()}
        for ramp in ramps:
            points = ramp['points']
            _lengths, normals = route_frames(points)
            height, side = ramp['height_m'], ramp['side']
            owner = None
            for index, (first, last) in enumerate(zip(points, points[1:])):
                if max(abs(first[2] - height), abs(last[2] - height)) > 1e-5:
                    continue
                if owner is None:
                    middle = tuple((a + b) / 2 for a, b in zip(first, last))
                    owner = painter._frame(middle)[3]
                for low, high, flank in ((-HALF_WIDTH, 0.0, -1), (0.0, HALF_WIDTH, 1)):
                    polygon = [(point[0] + offset * normal[0], point[2],
                                -(point[1] + offset * normal[1]), 0.0, 0.0)
                               for point, normal, offset in (
                                   (first, normals[index], low), (first, normals[index], high),
                                   (last, normals[index + 1], high), (last, normals[index + 1], low))]
                    for part in _split_crossing_sweep(polygon):
                        part = _clip(part, lambda p, side=side:
                                     side * (-p[2] - p[0] + 8.0) / math.sqrt(2.0) - INNER_Q)
                        part = _clip(part, lambda p, side=side:
                                     OUTER_Q - side * (-p[2] - p[0] + 8.0) / math.sqrt(2.0))
                        if len(part) < 3:
                            continue
                        boundary = [(p[0], p[2]) for p in part]
                        area = sum(a[0] * b[1] - b[0] * a[1]
                                   for a, b in zip(boundary, boundary[1:] + boundary[:1]))
                        if abs(area) < 1e-12:
                            continue
                        if area < 0.0:
                            boundary.reverse()
                        bounds = (min(x for x, _z in boundary), max(x for x, _z in boundary),
                                  min(z for _x, z in boundary), max(z for _x, z in boundary))
                        record = {'height': height, 'side': side, 'owner': owner, 'flank': flank,
                                  'boundary': boundary, 'bounds': bounds, 'ramp_id': ramp['id']}
                        region = len(self.regions)
                        self.regions.append(record)
                        for column in range(math.floor(bounds[0] / 16.0), math.floor(bounds[1] / 16.0) + 1):
                            for row in range(math.floor(bounds[2] / 16.0), math.floor(bounds[3] / 16.0) + 1):
                                self.buckets[column, row].append(region)

    def map_point(self, point, region):
        """Return original XYZ plus bounded DD asphalt UV for one half-ribbon."""
        owner, side = region['owner'], region['side']
        distance, lateral, _height, actual_owner = self.painter._frame(
            (point[0], -point[2], point[1]), owner)
        if actual_owner != owner:
            raise ValueError('A wheeltrack field changed its connected road owner')
        indices = self.painter.road_segments[owner]
        index = max(0, bisect_right(self.stations[owner], distance) - 1)
        segment = self.painter.segments[indices[index]]
        tx, ty = segment[4:6]
        q = side * (-point[2] - point[0] + 8.0) / math.sqrt(2.0)
        centre_q = q - lateral * side * (tx + ty) / math.sqrt(2.0)
        amplitude = _ease(centre_q - INNER_Q) * _ease(q - INNER_Q)
        mis_column = 63.5 + 8.0 * lateral
        shift = 16.0 + min(1.0, max(0.0, (mis_column - 68.0) / 6.0))
        target = min(SAFE_DD_COLUMNS[1], max(SAFE_DD_COLUMNS[0], mis_column + shift))
        edge = SAFE_DD_COLUMNS[0] if region['flank'] < 0 else SAFE_DD_COLUMNS[1]
        column = edge + (target - edge) * amplitude
        return (*point[:3], (column + 0.5) / 128.0, distance / 16.0)

    def _sample(self, polygon, region):
        for face in _triangulate(polygon, minimum_normal_squared=(
                0.0 if self.retain_nonzero_top_fragments else 1e-16)):
            pending = [face]
            while pending:
                triangle = pending.pop()
                lengths = [math.dist(triangle[a][:3], triangle[b][:3])
                           for a, b in ((0, 1), (1, 2), (2, 0))]
                longest = max(range(3), key=lengths.__getitem__)
                if lengths[longest] <= MAXIMUM_TEXTURE_EDGE + 1e-9:
                    yield tuple(self.map_point(point, region) for point in triangle)
                    continue
                first, last = ((0, 1), (1, 2), (2, 0))[longest]
                third = 3 - first - last
                middle = tuple((a + b) / 2 for a, b in zip(triangle[first], triangle[last]))
                pending.extend(((triangle[first], middle, triangle[third]),
                                (middle, triangle[last], triangle[third])))

    def remap_polygon(self, polygon):
        """Split a native top in the road footprint, including its overhang.

        Nominal construction-tile bounds do not cut the physical road.
        Native overhang positions and coverage need their independent donor
        proof; UVs outside this route footprint remain unchanged.
        """
        upward_area = sum(_normal((polygon[0], polygon[index], polygon[index + 1]))[1]
                          for index in range(1, len(polygon) - 1))
        if (len(polygon) < 3 or upward_area <= 1e-8
                or max(p[1] for p in polygon) - min(p[1] for p in polygon) > 1e-5):
            return [polygon]
        x0, x1 = min(p[0] for p in polygon), max(p[0] for p in polygon)
        z0, z1 = min(p[2] for p in polygon), max(p[2] for p in polygon)
        candidates = set()
        for column in range(math.floor(x0 / 16.0), math.floor(x1 / 16.0) + 1):
            for row in range(math.floor(z0 / 16.0), math.floor(z1 / 16.0) + 1):
                candidates.update(self.buckets.get((column, row), ()))
        remaining, mapped = [polygon], []
        for index in sorted(candidates):
            region = self.regions[index]
            a, b, c, d = region['bounds']
            if (abs(polygon[0][1] - region['height']) > 1e-5
                    or x1 < a or x0 > b or z1 < c or z0 > d):
                continue
            outside = []
            for part in remaining:
                inside = _inside(part, region['boundary'])
                if len(inside) < 3:
                    outside.append(part)
                    continue
                outside.extend(_subtract_convex(part, region['boundary']))
                mapped.extend(self._sample(inside, region))
            remaining = outside
            if not remaining:
                break
        return remaining + mapped
