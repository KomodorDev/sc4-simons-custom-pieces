"""A shared orthographic camera and the real 16 m SimCity construction grid.

World positions are (east, north, height), in metres. S3D model positions are
(east, height, -north). Bounds always mean (west, south, east, north), metres.
The grid is artwork behind a model, never additional track or game geometry.
"""
from __future__ import annotations

from dataclasses import dataclass
import math

import numpy as np
from PIL import Image, ImageDraw, ImageFont

TILE_METRES = 16.0
BACKGROUND = '#f7f9fb'


def _bounds(value):
    result = tuple(float(number) for number in value)
    if (len(result) != 4 or not all(math.isfinite(number) for number in result)
            or result[0] >= result[2] or result[1] >= result[3]):
        raise ValueError('Grid bounds must be finite (west, south, east, north) with positive area')
    return result


def world_to_s3d(east, north, height=0.0):
    """Broadcast world coordinates and return their exact S3D axis mapping."""
    east, north, height = np.broadcast_arrays(east, north, height)
    return np.stack((east, height, -north), axis=-1).astype(float)


@dataclass(frozen=True)
class OrthographicCamera:
    width: int
    height: int
    azimuth: float
    elevation: float
    right: np.ndarray
    up: np.ndarray
    towards: np.ndarray
    center: np.ndarray
    scale: float
    padding: float
    bounds_world_m: tuple

    def project_s3d(self, positions):
        """Project an array ending in XYZ to an array ending in screen XY."""
        positions = np.asarray(positions, dtype=float)
        if positions.shape[-1] != 3:
            raise ValueError('S3D positions must end in three coordinates')
        projected = np.stack((positions @ self.right, positions @ self.up), axis=-1)
        return (projected - self.center) * [self.scale, -self.scale] + [self.width / 2, self.height / 2]

    def project_world(self, east, north, height=0.0):
        return self.project_s3d(world_to_s3d(east, north, height))

    def metadata(self):
        """JSON-safe values sufficient to reproduce the pixel projection."""
        return {'projection': 'orthographic', 'image_size': [self.width, self.height],
                'azimuth_degrees': self.azimuth, 'elevation_degrees': self.elevation,
                'right_s3d': self.right.tolist(), 'up_s3d': self.up.tolist(),
                'towards_s3d': self.towards.tolist(),
                'projected_center_m': self.center.tolist(), 'pixels_per_metre': self.scale,
                'padding_pixels': self.padding, 'bounds_world_m': list(self.bounds_world_m),
                'world_coordinates': '(east, north, height)',
                's3d_coordinates': '(east, height, -north)'}


def make_camera(vertices_s3d, azimuth, elevation, width, height, *, bounds_world_m, padding=90):
    """Frame the actual model and ground-grid corners with one exact camera.

    The basis is identical to preview.render_fast_view's original camera.
    Padding is reserved on every side, not subtracted once from the width.
    """
    bounds = _bounds(bounds_world_m)
    if (width <= 0 or height <= 0 or padding < 0
            or min(width, height) <= 2 * padding):
        raise ValueError('Camera image size must exceed twice its nonnegative padding')
    vertices = np.asarray(vertices_s3d, dtype=float).reshape(-1, 3)
    if not len(vertices) or not np.isfinite(vertices).all():
        raise ValueError('Camera requires finite model vertices')
    if not math.isfinite(azimuth) or not math.isfinite(elevation) or not 0 < elevation <= 90:
        raise ValueError('Camera requires finite angles with elevation above 0 and at most 90 degrees')
    az, el = map(math.radians, (azimuth, elevation))
    right = np.array([math.cos(az), 0., -math.sin(az)])
    up = np.array([-math.sin(az) * math.sin(el), math.cos(el), -math.cos(az) * math.sin(el)])
    towards = np.array([math.sin(az) * math.cos(el), math.sin(el), math.cos(az) * math.cos(el)])
    west, south, east, north = bounds
    corners = world_to_s3d([west, west, east, east], [south, north, south, north])
    points = np.concatenate((vertices, corners))
    projected = np.column_stack((points @ right, points @ up))
    low, high = projected.min(axis=0), projected.max(axis=0)
    span = np.maximum(high - low, 1e-12)
    scale = min((width - 2 * padding) / span[0], (height - 2 * padding) / span[1])
    return OrthographicCamera(int(width), int(height), float(azimuth), float(elevation),
                              right, up, towards, (low + high) / 2, float(scale),
                              float(padding), bounds)


def tile_boundaries(low, high, origin=0.0):
    """Actual boundaries: origin + 8 + 16*k. Tile centres are origin + 16*k."""
    first = math.ceil((low - origin - TILE_METRES / 2) / TILE_METRES)
    last = math.floor((high - origin - TILE_METRES / 2) / TILE_METRES)
    return [origin + TILE_METRES / 2 + TILE_METRES * k for k in range(first, last + 1)]


def _tile_centres(low, high, origin):
    first, last = math.ceil((low - origin) / TILE_METRES), math.floor((high - origin) / TILE_METRES)
    return [(k, origin + TILE_METRES * k) for k in range(first, last + 1)]


def _coordinate(axis, value):
    return f'{axis}{value:d}'


def _arrow(draw, start, end, fill, width=2):
    draw.line((tuple(start), tuple(end)), fill=fill, width=width)
    direction = np.asarray(end) - start
    direction /= max(float(np.linalg.norm(direction)), 1e-12)
    normal = np.array([-direction[1], direction[0]])
    tip = np.asarray(end)
    draw.polygon([tuple(tip), tuple(tip - 9 * direction + 4 * normal),
                  tuple(tip - 9 * direction - 4 * normal)], fill=fill)


def make_city_grid(camera, bounds_world_m, *, origin_world_m=(0., 0.), font=None, bold_font=None,
                   scale_caption_visible=True):
    """Return (RGB background, metadata) for this camera's true ground grid.

    Draw the compiled model onto this background with the same camera. All
    grid lines then stay behind opaque track surfaces. Labels describe tile
    centres; lines mark tile boundaries half a tile away from those centres.
    Displayed tile indices are relative to origin_world_m; moving this label
    origin never translates model geometry or changes the camera projection.
    An origin at the southwest tile centre makes the enclosed indices start
    at X0 and Y0 without displaying unnecessary plus signs. X increases east;
    Y increases north. The origin stays internal and has no extra artwork.
    """
    west, south, east, north = bounds = _bounds(bounds_world_m)
    origin_e, origin_n = map(float, origin_world_m)
    if not all(math.isfinite(number) for number in (origin_e, origin_n)):
        raise ValueError('Grid origin must contain finite east and north metres')
    font = font or ImageFont.load_default()
    bold_font = bold_font or font
    image = Image.new('RGB', (camera.width, camera.height), BACKGROUND)
    draw = ImageDraw.Draw(image)
    corners = camera.project_world([west, east, east, west], [south, south, north, north])
    draw.polygon([tuple(point) for point in corners], fill='#f0f5f1')
    e_boundaries = tile_boundaries(west, east, origin_e)
    n_boundaries = tile_boundaries(south, north, origin_n)
    lines = []
    for axis, boundaries in (('east', e_boundaries), ('north', n_boundaries)):
        for coordinate in boundaries:
            if axis == 'east':
                ends = camera.project_world([coordinate, coordinate], [south, north])
                index = round((coordinate - origin_e - 8) / 16)
            else:
                ends = camera.project_world([west, east], [coordinate, coordinate])
                index = round((coordinate - origin_n - 8) / 16)
            major = index % 5 == 0
            draw.line([tuple(point) for point in ends], fill='#aebeb4' if major else '#cdd8cf',
                      width=2 if major else 1)
            lines.append({'axis': axis, 'coordinate_m': coordinate, 'pixels': ends.tolist(), 'major': major})
    labels = []
    # Labels are outside the ground rectangle, at the projected tile centres.
    # An outward vector is used instead of a fixed screen direction in oblique views.
    mid_e, mid_n = (west + east) / 2, (south + north) / 2
    e_centres = _tile_centres(west, east, origin_e)
    n_centres = _tile_centres(south, north, origin_n)
    for axis, centres in (('X', e_centres), ('Y', n_centres)):
        for index, coordinate in centres:
            world = (coordinate, south) if axis == 'X' else (west, coordinate)
            interior = camera.project_world(coordinate, mid_n) if axis == 'X' else camera.project_world(mid_e, coordinate)
            edge = camera.project_world(*world)
            outward = edge - interior
            outward /= max(float(np.linalg.norm(outward)), 1e-12)
            point = edge + outward * 17
            text = _coordinate(axis, index)
            draw.text(tuple(point), text, font=font, fill='#52685b', anchor='mm', stroke_width=2, stroke_fill=BACKGROUND)
            labels.append({'text': text, 'axis': axis, 'tile_index': index,
                           'world_m': list(world), 'pixel': point.tolist()})
    origin_pixel = camera.project_world(origin_e, origin_n)
    # A fixed corner key uses the projected ground directions, so north/east
    # remain correct even when the camera is viewing the opposite side.
    compass_origin = np.array([camera.width - 100., 100.])
    projected_origin = camera.project_world(origin_e, origin_n)
    arrows = []
    for label, vector in (('E', camera.project_world(origin_e + 16, origin_n) - projected_origin),
                          ('N', camera.project_world(origin_e, origin_n + 16) - projected_origin)):
        vector /= max(float(np.linalg.norm(vector)), 1e-12)
        tip = compass_origin + 48 * vector
        _arrow(draw, compass_origin, tip, '#234e66')
        draw.text(tuple(tip + 14 * vector), label, font=bold_font, fill='#234e66', anchor='mm')
        arrows.append({'direction': label, 'start_pixel': compass_origin.tolist(), 'end_pixel': tip.tolist()})
    if scale_caption_visible:
        draw.text((18, camera.height - 27), '1 tile = 16 m | labels mark tile centres', font=font, fill='#52685b')
    metadata = {'tile_metres': TILE_METRES, 'ground_height_m': 0,
                'bounds_world_m': list(bounds), 'origin_world_m': [origin_e, origin_n],
                'display_axis_labels': {'east': 'X', 'north': 'Y'},
                'origin_marker_visible': False,
                'display_coordinate_basis': {
                    'reference': 'tile-centre offsets relative to origin_world_m',
                    'units': 'tiles', 'east_increases': 'east', 'north_increases': 'north',
                    'east_index_formula': '(world_east_m - origin_world_m[0]) / 16',
                    'north_index_formula': '(world_north_m - origin_world_m[1]) / 16',
                    'east_index_range': [e_centres[0][0], e_centres[-1][0]] if e_centres else [],
                    'north_index_range': [n_centres[0][0], n_centres[-1][0]] if n_centres else [],
                    'nonnegative_labels_omit_plus_sign': True,
                    'authoring_world_coordinates_changed': False,
                },
                'origin_pixel': origin_pixel.tolist(), 'boundary_offset_from_centre_m': 8,
                'east_boundaries_m': e_boundaries, 'north_boundaries_m': n_boundaries,
                'grid_lines': lines, 'tile_labels': labels, 'direction_arrows': arrows,
                'tile_scale': {'metres': 16, 'east_pixels': float(np.linalg.norm(
                    camera.project_world(origin_e + 16, origin_n) - projected_origin)),
                    'north_pixels': float(np.linalg.norm(
                    camera.project_world(origin_e, origin_n + 16) - projected_origin)),
                    'caption': '1 tile = 16 m', 'caption_visible': bool(scale_caption_visible)},
                'camera': camera.metadata()}
    return image, metadata
