#!/usr/bin/env python3
"""Render explicitly schematic surfaces from the diagonal-diamond route model.

This renderer reads the maintained JSONC design through the geometry module.
Every camera projects the same sampled road ribbons; a depth buffer resolves
their height order. The output is not a render of compiled SimCity resources.
Road-edge strokes and lane markings are illustrative, and are not native PATHs
or engineered barriers. No support columns or structural deck are invented.

Run from the repository root, for example::

    python3 -B custom-pieces/domains/highway/tools/render_diagonal_diamond.py \
        --design custom-pieces/domains/highway/01_assemblies/\
ddrhw-l1-and-l2-diagonal-avenue-diamond/design.jsonc \
        --output-dir custom-pieces/domains/highway/01_assemblies/\
ddrhw-l1-and-l2-diagonal-avenue-diamond/previews
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.dont_write_bytecode = True
TOOLS = Path(__file__).resolve().parent
LIBRARY = next(parent for parent in TOOLS.parents if (parent / 'project.jsonc').is_file())
REPOSITORY = LIBRARY.parent
sys.path.insert(0, str(TOOLS))

from diagonal_diamond_geometry import build_geometry, load_design


WIDTH, HEIGHT, SUPERSAMPLE = 2400, 1900, 2
INK = '#213745'
SECONDARY = '#5b6e76'
PAPER = '#f7f7f2'
ACCENTS = {'upper': '#138f93', 'lower': '#5269ae', 'avenue': '#687b69', 'ramp': '#bc812d'}
ASPHALT = {'upper': (67, 83, 92), 'lower': (77, 84, 105), 'avenue': (89, 98, 99), 'ramp': (96, 96, 90)}
VIEWS = (('top', -90., 90., 'Top view, north up'),
         ('southeast', -45., 22., 'Southeast view, looking northwest'),
         ('northwest', 135., 22., 'Northwest view, looking southeast'))


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def public_path(path):
    """Use portable paths, rejecting provenance outside the checkout."""
    return Path(path).resolve().relative_to(REPOSITORY).as_posix()


def font(size, bold=False):
    names = (('DejaVuSans-Bold.ttf', '/System/Library/Fonts/Supplemental/Arial Bold.ttf')
             if bold else ('DejaVuSans.ttf', '/System/Library/Fonts/Supplemental/Arial.ttf'))
    for name in names:
        try:
            return ImageFont.truetype(name, round(size * SUPERSAMPLE))
        except OSError:
            continue
    return ImageFont.load_default(size=round(size * SUPERSAMPLE))


def draw_text(draw, xy, text, size=22, fill=INK, bold=False, anchor=None):
    draw.text(tuple(round(v * SUPERSAMPLE) for v in xy), text, font=font(size, bold),
              fill=fill, anchor=anchor)


def line(draw, xy, fill, width=1):
    draw.line([tuple(round(v * SUPERSAMPLE) for v in point) for point in xy],
              fill=fill, width=max(1, round(width * SUPERSAMPLE)))


def box(draw, bounds, fill, outline=None, radius=12, width=1):
    draw.rounded_rectangle(tuple(round(v * SUPERSAMPLE) for v in bounds),
                           radius=round(radius * SUPERSAMPLE), fill=fill,
                           outline=outline, width=round(width * SUPERSAMPLE))


def wrap_text(draw, text, width, size):
    words, rows, row = text.split(), [], ''
    for word in words:
        candidate = (row + ' ' + word).strip()
        if row and draw.textlength(candidate, font=font(size)) > width * SUPERSAMPLE:
            rows.append(row)
            row = word
        else:
            row = candidate
    if row:
        rows.append(row)
    return rows


def classify(road):
    tag = (str(road.get('id', '')) + ' ' + str(road.get('kind', ''))).lower()
    if 'ramp' in tag or road['width_m'] < 8:
        return 'ramp'
    if 'avenue' in tag:
        return 'avenue'
    if road.get('deck') in ('upper', 'lower'):
        return road['deck']
    raise ValueError(f'Cannot classify road {road["id"]}')


def ribbon(points, width, offset=0.):
    """Offset the exact sampled centre line in the horizontal world plane."""
    points = np.asarray(points, dtype=float)
    difference = np.gradient(points[:, :2], axis=0)
    lengths = np.linalg.norm(difference, axis=1)
    if np.any(lengths < 1e-10):
        raise ValueError('A road ribbon contains a repeated horizontal sample')
    normal = np.column_stack((-difference[:, 1] / lengths, difference[:, 0] / lengths,
                              np.zeros(len(points))))
    return points + normal * (offset - width / 2), points + normal * (offset + width / 2)


class Camera:
    def __init__(self, extent, azimuth, elevation):
        az, el = math.radians(azimuth), math.radians(elevation)
        self.toward = np.array([math.cos(az) * math.cos(el), math.sin(az) * math.cos(el), math.sin(el)])
        self.right = np.array([-math.sin(az), math.cos(az), 0.])
        self.up = np.cross(self.toward, self.right)
        corners = np.array([[x, y, z] for x in extent[0:2] for y in extent[2:4]
                            for z in (0., extent[4])])
        xx, yy = corners @ self.right, corners @ self.up
        self.scale = min(1640 / np.ptp(xx), 1190 / np.ptp(yy))
        self.center = np.array([(xx.max() + xx.min()) / 2, (yy.max() + yy.min()) / 2])
        self.screen_center = np.array([936., 906.])
        self.azimuth, self.elevation = azimuth, elevation

    def project(self, points):
        points = np.asarray(points, dtype=float)
        px = (points @ self.right - self.center[0]) * self.scale + self.screen_center[0]
        py = -(points @ self.up - self.center[1]) * self.scale + self.screen_center[1]
        return np.column_stack((px, py, points @ self.toward))

    def evidence(self):
        return {'projection': 'orthographic', 'azimuth_degrees_from_east_ccw': self.azimuth,
                'elevation_degrees': self.elevation, 'towards_camera_unit_enh': self.toward.tolist(),
                'screen_right_unit_enh': self.right.tolist(), 'screen_up_unit_enh': self.up.tolist(),
                'pixels_per_metre_in_projection': self.scale,
                'look_at_world_enh_m': [0., 0., 0.]}


class Surface:
    """Small deterministic triangle depth renderer; larger depth is nearer."""
    def __init__(self, image, camera):
        self.pixels = np.asarray(image).copy()
        self.depth = np.full((image.height, image.width), -np.inf, dtype=np.float32)
        self.camera = camera

    def triangle(self, world, colour):
        projected = self.camera.project(world)
        projected[:, :2] *= SUPERSAMPLE
        xmin, ymin = np.maximum(np.floor(projected[:, :2].min(axis=0)).astype(int), (0, 0))
        xmax, ymax = np.minimum(np.ceil(projected[:, :2].max(axis=0)).astype(int),
                                (self.pixels.shape[1] - 1, self.pixels.shape[0] - 1))
        if xmax < xmin or ymax < ymin:
            return
        (x1, y1, d1), (x2, y2, d2), (x3, y3, d3) = projected
        denominator = (y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3)
        if abs(denominator) < 1e-8:
            return
        yy, xx = np.mgrid[ymin:ymax + 1, xmin:xmax + 1]
        xx, yy = xx + .5, yy + .5
        first = ((y2 - y3) * (xx - x3) + (x3 - x2) * (yy - y3)) / denominator
        second = ((y3 - y1) * (xx - x3) + (x1 - x3) * (yy - y3)) / denominator
        third = 1. - first - second
        depth = first * d1 + second * d2 + third * d3
        block = self.depth[ymin:ymax + 1, xmin:xmax + 1]
        visible = ((first >= -1e-7) & (second >= -1e-7) & (third >= -1e-7)
                   & (depth >= block - 1e-6))
        block[visible] = depth[visible]
        self.pixels[ymin:ymax + 1, xmin:xmax + 1][visible] = colour

    def strip(self, points, width, colour, offset=0., lift=0., dash=None):
        points = np.asarray(points, dtype=float).copy()
        points[:, 2] += lift
        left, right = ribbon(points, width, offset)
        distances = np.r_[0., np.cumsum(np.linalg.norm(np.diff(points[:, :2], axis=0), axis=1))]
        for index in range(len(points) - 1):
            if dash and ((distances[index] + distances[index + 1]) / 2) % sum(dash) >= dash[0]:
                continue
            self.triangle([left[index], right[index], right[index + 1]], colour)
            self.triangle([left[index], right[index + 1], left[index + 1]], colour)

    def arrow(self, points, index, colour=(235, 239, 232)):
        points = np.asarray(points, dtype=float)
        start, end = max(index - 2, 0), min(index + 2, len(points) - 1)
        delta = points[end, :2] - points[start, :2]
        length = np.linalg.norm(delta)
        if length < 1e-9:
            return
        tangent = np.r_[delta / length, 0.]
        normal = np.array([-tangent[1], tangent[0], 0.])
        center = points[index].copy()
        center[2] += .095
        tip, tail = center + tangent * 4.8, center - tangent * 2.8
        self.triangle([tip, tail + normal * 1.45, tail - normal * 1.45], colour)

    def image(self):
        return Image.fromarray(self.pixels, 'RGB')


def extent_and_grid(roads, tile_size):
    surfaces = [np.vstack(ribbon(road['points'], road['width_m'])) for road in roads]
    points = np.vstack(surfaces)
    # The same southwest TILE CENTRE is used in all three camera views.
    minimum = np.floor((points[:, :2].min(axis=0) - tile_size) / tile_size) * tile_size
    maximum = np.ceil((points[:, :2].max(axis=0) + tile_size) / tile_size) * tile_size
    return (minimum[0] - tile_size / 2, maximum[0] + tile_size / 2,
            minimum[1] - tile_size / 2, maximum[1] + tile_size / 2,
            float(points[:, 2].max()) + 4), minimum, maximum


def ground(image, camera, extent, minimum, maximum, tile_size):
    draw = ImageDraw.Draw(image)
    xmin, xmax, ymin, ymax = extent[:4]
    corners = [[xmin, ymin, 0.], [xmax, ymin, 0.], [xmax, ymax, 0.], [xmin, ymax, 0.]]
    draw.polygon([tuple(p[:2] * SUPERSAMPLE) for p in camera.project(corners)], fill='#eeefe7')
    nx, ny = np.rint((maximum - minimum) / tile_size).astype(int)
    for number in range(nx + 2):
        x = minimum[0] - tile_size / 2 + number * tile_size
        projected = camera.project([[x, ymin, 0.], [x, ymax, 0.]])
        line(draw, projected[:, :2], '#d8ddd5', .7)
    for number in range(ny + 2):
        y = minimum[1] - tile_size / 2 + number * tile_size
        projected = camera.project([[xmin, y, 0.], [xmax, y, 0.]])
        line(draw, projected[:, :2], '#d8ddd5', .7)
    for axis, count in ((0, nx), (1, ny)):
        for number in range(0, count + 1, 4):
            point = [minimum[0], minimum[1], 0.]
            point[axis] += number * tile_size
            if axis == 0:
                point[1] = ymin - 7
            else:
                point[0] = xmin - 7
            x, y = camera.project([point])[0, :2]
            draw_text(draw, (x, y), f'{"X" if axis == 0 else "Y"}{number}', 15,
                      fill='#708075', anchor='mm')
    origin = camera.project([[minimum[0], minimum[1], 0.]])[0, :2]
    x, y = origin
    draw.ellipse(((x - 3) * SUPERSAMPLE, (y - 3) * SUPERSAMPLE,
                  (x + 3) * SUPERSAMPLE, (y + 3) * SUPERSAMPLE), fill='#638573')
    return image


def shadows(image, roads, camera):
    mask = Image.new('L', image.size)
    draw = ImageDraw.Draw(mask)
    for road in roads:
        if max(point[2] for point in road['points']) < .1:
            continue
        left, right = ribbon(road['points'], road['width_m'])
        for index in range(len(left) - 1):
            quad = np.array([left[index], right[index], right[index + 1], left[index + 1]])
            # Illustrative sunlight only: the shadow is not clearance evidence.
            quad[:, 0] += .3 * quad[:, 2]
            quad[:, 1] -= .3 * quad[:, 2]
            quad[:, 2] = 0.
            draw.polygon([tuple(point[:2] * SUPERSAMPLE) for point in camera.project(quad)], fill=54)
    mask = mask.filter(ImageFilter.GaussianBlur(3 * SUPERSAMPLE))
    shade = Image.new('RGB', image.size, '#47564e')
    return Image.composite(shade, image, mask)


def render_roads(image, camera, roads, routes):
    surface = Surface(image, camera)
    for road in roads:
        kind, points = classify(road), road['points']
        surface.strip(points, road['width_m'], ASPHALT[kind])
    for road in roads:
        kind, points, width = classify(road), road['points'], road['width_m']
        edge_colour = tuple(int(ACCENTS[kind][i:i + 2], 16) for i in (1, 3, 5))
        for side in (-1, 1):
            surface.strip(points, .42, edge_colour, side * (width / 2 - .25), lift=.025)
            surface.strip(points, .17, (224, 228, 220), side * (width / 2 - .9), lift=.045)
        if kind in ('upper', 'lower'):
            surface.strip(points, .2, (226, 230, 222), lift=.055, dash=(5., 8.))
        elif kind == 'avenue':
            for side in (-1, 1):
                surface.strip(points, .18, (226, 196, 105), offset=side * .3, lift=.055)
                surface.strip(points, .18, (224, 228, 220), offset=side * 6., lift=.055, dash=(5., 8.))
    for route in routes:
        points = route['points']
        tag = str(route.get('kind', '')).lower()
        if 'turn' in tag or len(points) < 5:
            continue
        length = np.linalg.norm(np.diff(np.asarray(points)[:, :2], axis=0), axis=1).sum()
        if length < 50:
            continue
        # Arrows follow route direction as authored; there is no inferred reversal.
        fractions = (.28, .7) if length > 450 else (.38, .72)
        for fraction in fractions:
            surface.arrow(points, round((len(points) - 1) * fraction))
    return surface.image()


def callout(draw, camera, world, label, colour, offset=(0., -22.)):
    point = camera.project([world])[0, :2]
    target = point + np.asarray(offset)
    textwidth = draw.textlength(label, font=font(19, True)) / SUPERSAMPLE
    bounds = (target[0] - textwidth / 2 - 12, target[1] - 16,
              target[0] + textwidth / 2 + 12, target[1] + 16)
    line(draw, [point, target], colour, 1.3)
    box(draw, bounds, '#f9faf6', colour, radius=8, width=1)
    draw_text(draw, target, label, 19, colour, True, anchor='mm')


def annotations(draw, camera, roads, design):
    highway_half = design['geometry']['highway_half_length_m']
    avenue = next(road for road in roads if classify(road) == 'avenue')
    avenue_points = np.asarray(avenue['points'])
    northwest = avenue_points[np.argmax(avenue_points[:, 1] - avenue_points[:, 0])]
    southeast = avenue_points[np.argmin(avenue_points[:, 1] - avenue_points[:, 0])]
    q = math.sqrt(2.)
    upper_height = design['geometry']['upper_height_m']
    arms = [('SW', [-highway_half / q, -highway_half / q, upper_height]),
            ('NE', [highway_half / q, highway_half / q, upper_height]),
            ('NW', northwest), ('SE', southeast)]
    for label, world in arms:
        offset = (0., -28.) if label in ('NW', 'NE') else (0., 28.)
        callout(draw, camera, world, label, INK, offset)
    ramps = [road for road in roads if classify(road) == 'ramp']
    for number, road in enumerate(ramps, 1):
        points = np.asarray(road['points'])
        point = points[round((len(points) - 1) * .54)]
        # Move the label towards the outside of its highway/avenue quadrant.
        offset = (34 if point[0] > 0 else -34, -32 if point[1] > 0 else 32)
        callout(draw, camera, point, f'R{number}', ACCENTS['ramp'], offset)


def compass(draw, camera):
    origin = np.array([1595., 1438.])
    for label, vector, colour in [('N', [0., 32., 0.], INK), ('E', [32., 0., 0.], SECONDARY)]:
        projected = camera.project([[0., 0., 0.], vector])[:, :2]
        delta = projected[1] - projected[0]
        delta *= 62 / max(1e-6, np.linalg.norm(delta))
        end = origin + delta
        line(draw, [origin, end], colour, 2.5)
        direction = delta / np.linalg.norm(delta)
        normal = np.array([-direction[1], direction[0]])
        arrow = [end, end - direction * 12 + normal * 5, end - direction * 12 - normal * 5]
        draw.polygon([tuple(point * SUPERSAMPLE) for point in arrow], fill=colour)
        draw_text(draw, end + direction * 18, label, 23, colour, True, anchor='mm')


def panel(draw, design, roads, camera, minimum, maximum):
    x, right = 1836, 2342
    box(draw, (x, 272, right, 1550), '#ffffff', '#d8dfd9', 20)
    draw_text(draw, (x + 30, 301), 'SCHEMATIC', 30, '#127b80', True)
    draw_text(draw, (x + 30, 349), 'Parametric surface model', 24, INK, True)
    draw_text(draw, (x + 30, 391), 'Shared geometry in all 3 views', 21, SECONDARY)
    line(draw, [(x + 30, 440), (right - 30, 440)], '#d8dfd9')
    legend = [('upper', 'UPPER HIGHWAY', 'SW → NE', f'{design["geometry"]["upper_height_m"]:g} m'),
              ('lower', 'LOWER HIGHWAY', 'NE → SW', f'{design["geometry"]["lower_height_m"]:g} m'),
              ('avenue', 'DIAGONAL AVENUE', 'NW ↔ SE', '0 m')]
    y = 474
    for kind, title, direction, height in legend:
        box(draw, (x + 30, y + 5, x + 40, y + 63), ACCENTS[kind], radius=3)
        draw_text(draw, (x + 58, y), title, 20, ACCENTS[kind], True)
        draw_text(draw, (x + 58, y + 31), f'{direction}  |  {height}', 25, INK, True)
        y += 104
    line(draw, [(x + 30, 797), (right - 30, 797)], '#d8dfd9')
    draw_text(draw, (x + 30, 831), 'FOUR ONE-WAY RAMPS', 22, ACCENTS['ramp'], True)
    ramps = [road for road in roads if classify(road) == 'ramp']
    y = 877
    ramp_records = []
    for number, road in enumerate(ramps, 1):
        identifier = str(road['id'])
        tag = identifier.lower()
        upper = 'upper' in tag
        off = road.get('direction') == 'off'
        label = f'{"Upper" if upper else "Lower"} {"off-ramp" if off else "on-ramp"}'
        draw_text(draw, (x + 30, y), f'R{number}', 22, ACCENTS['ramp'], True)
        draw_text(draw, (x + 85, y), label, 22, INK)
        ramp_records.append({'label': f'R{number}', 'road_id': identifier, 'text': label})
        y += 47
    line(draw, [(x + 30, 1094), (right - 30, 1094)], '#d8dfd9')
    draw_text(draw, (x + 30, 1127), 'WIDTHS · PROVISIONAL', 20, SECONDARY, True)
    widths = design['geometry']
    for text, y in [(f'Each highway deck: {widths["highway_width_m"]:g} m', 1172),
                    (f'Avenue: {widths["avenue_width_m"]:g} m', 1211),
                    (f'Each ramp: {widths["ramp_width_m"]:g} m', 1250)]:
        draw_text(draw, (x + 30, y), text, 23, INK)
    line(draw, [(x + 30, 1310), (right - 30, 1310)], '#d8dfd9')
    note = ('Road-edge strokes, markings, and shadows are illustrative. Supports, structural details, and native joining seams are pending.')
    for number, row in enumerate(wrap_text(draw, note, right - x - 60, 21)):
        draw_text(draw, (x + 30, 1345 + number * 31), row, 21, SECONDARY)
    # The bar is in the ground plane, so an oblique view also has an honest scale.
    scale_start = np.array([137., 1598.])
    ground_delta = camera.project([[0., 0., 0.], [32., 0., 0.]])[:, :2]
    delta = ground_delta[1] - ground_delta[0]
    if delta[0] < 0:
        delta *= -1
    scale_end = scale_start + delta
    line(draw, [scale_start, scale_end], INK, 4)
    for point in (scale_start, scale_end):
        line(draw, [point + [0., -6.], point + [0., 6.]], INK, 2)
    draw_text(draw, (137., 1670.), '32 m = 2 tiles along the east–west axis', 19, SECONDARY)
    return ramp_records


def crossing_detail(image, camera, roads, routes, design):
    """Enlarge the same surfaces with a second orthographic camera."""
    width, height = 740, 360
    detail = Image.new('RGB', (width * SUPERSAMPLE, height * SUPERSAMPLE), '#eef1e9')
    zoom = Camera((-80., 80., -80., 80., 20.), camera.azimuth, camera.elevation)
    zoom.scale = max(5.6, camera.scale * 1.4)
    zoom.center = np.array([0., 0.])
    zoom.screen_center = np.array([width / 2, 255.])
    detail = render_roads(detail, zoom, roads, routes)
    draw = ImageDraw.Draw(detail)
    draw_text(draw, (18, 15), 'CROSSING DETAIL', 19, INK, True)
    draw_text(draw, (18, 46), f'{zoom.scale / camera.scale:.2f}× enlargement · same surfaces', 17, SECONDARY)
    for deck in ('upper', 'lower'):
        height_m = design['geometry'][f'{deck}_height_m']
        point = zoom.project([[0., 0., height_m]])[0, :2]
        # The lead points at a real sample's deck centre height.
        label = np.array([570., point[1] - (19. if deck == 'upper' else -20.)])
        line(draw, [point, label], ACCENTS[deck], 1.2)
        draw_text(draw, label, f'{height_m:g} m', 20, ACCENTS[deck], True, anchor='lm')
    box(draw, (10, 313, 602, 351), '#f7f8f2', radius=4)
    draw_text(draw, (18, 323), 'Avenue: 0 m · Surface geometry; supports pending', 17, SECONDARY)
    location = (128, 292)
    image.paste(detail, tuple(value * SUPERSAMPLE for value in location))
    draw = ImageDraw.Draw(image)
    box(draw, (location[0], location[1], location[0] + width, location[1] + height),
        None, '#cbd4cd', radius=0)
    return {'screen_bounds_pixels': [location[0], location[1], location[0] + width, location[1] + height],
            'enlargement_factor': zoom.scale / camera.scale, 'camera': zoom.evidence(),
            'source': 'Same unmodified sampled road points and widths as main view'}


def render_view(design, geometry, view):
    name, azimuth, elevation, caption = view
    roads = geometry['roads']
    extent, minimum, maximum = extent_and_grid(roads, design['coordinates']['tile_size_m'])
    camera = Camera(extent, azimuth, elevation)
    image = Image.new('RGB', (WIDTH * SUPERSAMPLE, HEIGHT * SUPERSAMPLE), PAPER)
    image = ground(image, camera, extent, minimum, maximum, design['coordinates']['tile_size_m'])
    image = shadows(image, roads, camera)
    image = render_roads(image, camera, roads, geometry.get('routes', []))
    inset = None
    if name != 'top':
        inset = crossing_detail(image, camera, roads, geometry.get('routes', []), design)
    draw = ImageDraw.Draw(image)
    draw_text(draw, (56, 37), 'Assembly - ' + design['title'], 45, INK, True)
    draw_text(draw, (56, 107), f'Clean view | {caption} | Schematic', 30, '#127b80')
    parameters = design['geometry']
    heights = (f'L2: {parameters["upper_height_m"]:g} m  ·  '
               f'L1: {parameters["lower_height_m"]:g} m  ·  '
               'Avenue: ground level  ·  Right-hand traffic')
    draw_text(draw, (56, 162), heights, 25, SECONDARY)
    line(draw, [(56, 224), (2342, 224)], '#cbd4cd', 1.5)
    annotations(draw, camera, roads, design)
    compass(draw, camera)
    ramps = panel(draw, design, roads, camera, minimum, maximum)
    line(draw, [(56, 1730), (2342, 1730)], '#cbd4cd', 1.5)
    draw_text(draw, (56, 1762), 'Independent X/Y grid · 1 tile = 16 m · Labels mark tile centres', 23, INK, True)
    draw_text(draw, (56, 1808), 'X increases east · Y increases north · X0/Y0 is the southwest display reference, not a construction anchor', 21, SECONDARY)
    if name == 'top':
        draw_text(draw, (850, 1634), 'The upper deck conceals the lower through deck in this view.', 20, SECONDARY)
    result = image.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
    return result, {'camera': camera.evidence(), 'display_grid': {
        'unit': 'tile centre', 'tile_size_m': design['coordinates']['tile_size_m'],
        'southwest_tile_centre_world_en_m': minimum.tolist(),
        'northeast_tile_centre_world_en_m': maximum.tolist(),
        'axis_x': 'east', 'axis_y': 'north', 'construction_anchor': False},
        'ramp_labels': ramps, 'crossing_detail': inset,
        'caption': f'Clean view | {caption} | Schematic'}


def render_profiles(design, geometry):
    """Draw actual u/z ramp samples with a declared, common vertical exaggeration."""
    image = Image.new('RGB', (WIDTH * SUPERSAMPLE, HEIGHT * SUPERSAMPLE), PAPER)
    draw = ImageDraw.Draw(image)
    draw_text(draw, (56, 37), 'Assembly - ' + design['title'], 45, INK, True)
    draw_text(draw, (56, 107), 'Clean view | Ramp elevation profiles | Schematic', 30, '#127b80')
    vertical_exaggeration = 1.5
    draw_text(draw, (56, 162), f'Four separate slip lanes · Actual sampled heights · Vertical scale exaggerated {vertical_exaggeration:g}×', 25, SECONDARY)
    line(draw, [(56, 224), (2342, 224)], '#cbd4cd', 1.5)
    ramps = [road for road in geometry['roads'] if classify(road) == 'ramp']
    maximum_u_span = max(np.ptp(np.asarray(road['points_uvz'])[:, 0]) for road in ramps)
    common_scale = 958. / maximum_u_span
    panels = []
    for number, road in enumerate(ramps, 1):
        column, row = (number - 1) % 2, (number - 1) // 2
        left, top = 56 + column * 1170, 270 + row * 674
        right, bottom = left + 1118, top + 622
        box(draw, (left, top, right, bottom), '#ffffff', '#d8dfd9', 16)
        uvz = np.asarray(road['points_uvz'])
        u, height = uvz[:, 0], uvz[:, 2]
        upper = 'upper' in road['id']
        off = road['direction'] == 'off'
        deck = 'upper' if upper else 'lower'
        title = f'R{number} · {"Upper" if upper else "Lower"} {"off-ramp" if off else "on-ramp"}'
        draw_text(draw, (left + 28, top + 22), title, 29, ACCENTS[deck], True)
        draw_text(draw, (left + 28, top + 67), f'{height[0]:g} m → {height[-1]:g} m  |  Arrows show vehicle travel', 23, INK)
        plan_length = float(np.linalg.norm(np.diff(np.asarray(road['points'])[:, :2], axis=0), axis=1).sum())
        tile_lengths = plan_length / design['coordinates']['tile_size_m']
        length_text = f'Full curved plan length: {round(plan_length, 3):g} m = {round(tile_lengths, 3):g} tile lengths'
        draw_text(draw, (left + 28, top + 105), length_text, 22, ACCENTS[deck], True)
        xmin, xmax = float(u.min()), float(u.max())
        plotleft = left + 110 + (maximum_u_span - (xmax - xmin)) * common_scale / 2
        plotright = plotleft + (xmax - xmin) * common_scale
        baseline = top + 457
        scale = common_scale
        def project_profile(x, z):
            return np.column_stack((plotleft + (np.asarray(x) - xmin) * scale,
                                    baseline - np.asarray(z) * scale * vertical_exaggeration))
        upper_height = design['geometry']['upper_height_m']
        lower_height = design['geometry']['lower_height_m']
        for value in (0., lower_height, upper_height):
            y = baseline - value * scale * vertical_exaggeration
            line(draw, [(plotleft, y), (plotright, y)], '#b7c5bc', 1)
            draw_text(draw, (plotleft - 17, y), f'{value:g} m', 19, SECONDARY, anchor='rm')
        for value in np.linspace(xmin, xmax, 5):
            x = plotleft + (value - xmin) * scale
            line(draw, [(x, baseline + 5), (x, baseline + 12)], '#9aaca2', 1)
            draw_text(draw, (x, baseline + 27), f'{value:.1f}', 17, SECONDARY, anchor='mm')
        points = project_profile(u, height)
        # Fill down to the ground plane to make the vertical drop visible.
        fill = [(points[0, 0], baseline), *map(tuple, points), (points[-1, 0], baseline)]
        draw.polygon([tuple(value * SUPERSAMPLE for value in point) for point in fill], fill='#edf2ee')
        # Restore the guide lines above the fill.
        for value in (lower_height, upper_height):
            y = baseline - value * scale * vertical_exaggeration
            line(draw, [(plotleft, y), (plotright, y)], '#c8d3cb', 1)
        line(draw, [(plotleft, baseline), (plotright, baseline)], '#7e9382', 3)
        line(draw, points, ACCENTS[deck], 7)
        line(draw, points, '#fff8df', 1.3)
        for fraction in (.28, .66):
            index = round(fraction * (len(points) - 1))
            delta = points[min(index + 2, len(points) - 1)] - points[max(index - 2, 0)]
            direction = delta / np.linalg.norm(delta)
            normal = np.array([-direction[1], direction[0]])
            tip = points[index] + direction * 12
            tail = points[index] - direction * 9
            triangle = [tip, tail + normal * 7, tail - normal * 7]
            draw.polygon([tuple(point * SUPERSAMPLE) for point in triangle], fill=ACCENTS[deck])
        ground_index = -1 if off else 0
        groundpoint = points[ground_index]
        draw.ellipse(tuple(value * SUPERSAMPLE for value in
                          (groundpoint[0] - 6, groundpoint[1] - 6, groundpoint[0] + 6, groundpoint[1] + 6)),
                     fill=ACCENTS['avenue'])
        labelx = min(max(groundpoint[0], left + 230), right - 230)
        draw_text(draw, (labelx, baseline + 70), 'AVENUE CONNECTION · GROUND LEVEL', 18, ACCENTS['avenue'], True, anchor='mm')
        draw_text(draw, (left + 28, bottom - 50), f'Maximum sampled grade: {road["grade_max_percent"]:.2f}%  ·  Road width: {road["width_m"]:g} m', 21, INK)
        panels.append({'road_id': road['id'], 'label': f'R{number}', 'source': 'roads.points_uvz',
                       'horizontal_axis': 'u, metres along highway towards northeast',
                       'u_range_m': [xmin, xmax], 'vertical_axis': 'height above flat ground, metres',
                       'vertical_exaggeration': vertical_exaggeration,
                       'common_horizontal_pixels_per_metre': common_scale,
                       'full_horizontal_curved_length_m': plan_length,
                       'full_horizontal_curved_length_in_16m_tiles': tile_lengths,
                       'start_height_m': float(height[0]), 'end_height_m': float(height[-1]),
                       'maximum_grade_percent': road['grade_max_percent']})
    line(draw, [(56, 1651), (2342, 1651)], '#cbd4cd', 1.5)
    draw_text(draw, (56, 1680), 'Horizontal axis: u in metres, increasing towards northeast · Vertical axis: height above ground in metres', 23, INK, True)
    note = ('All panels share the same scales. Each line uses the same ramp samples as the top and oblique views. The horizontal axis projects the curved route along the highway; '
            'it is not the full distance travelled. Grade values use actual horizontal route length.')
    for index, row in enumerate(wrap_text(draw, note, 2280, 22)):
        draw_text(draw, (56, 1725 + index * 34), row, 22, SECONDARY)
    draw_text(draw, (56, 1820), 'Schematic source geometry · Native joining seams, structural details, and game traffic paths remain pending', 22, SECONDARY)
    return image.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS), {
        'view': 'profiles', 'caption': 'Clean view | Ramp elevation profiles | Schematic',
        'panels': panels, 'compiled_model': False}


def render(design_path, output_dir):
    design_path, output_dir = Path(design_path).resolve(), Path(output_dir).resolve()
    # Resolve every provenance path before writing any output.
    public_path(design_path)
    public_path(output_dir)
    design = load_design(design_path)
    geometry = build_geometry(design)
    output_dir.mkdir(parents=True, exist_ok=True)
    images = []
    for view in VIEWS:
        image, record = render_view(design, geometry, view)
        output = output_dir / f'schematic-{view[0]}.png'
        image.save(output, optimize=True)
        record.update({'path': public_path(output), 'sha256': sha256(output),
                       'view': view[0], 'size_pixels': [WIDTH, HEIGHT]})
        images.append(record)
        print(f'Rendered {public_path(output)}', flush=True)
    image, record = render_profiles(design, geometry)
    output = output_dir / 'schematic-profiles.png'
    image.save(output, optimize=True)
    record.update({'path': public_path(output), 'sha256': sha256(output), 'size_pixels': [WIDTH, HEIGHT]})
    images.append(record)
    print(f'Rendered {public_path(output)}', flush=True)
    module_path = TOOLS / 'diagonal_diamond_geometry.py'
    report = {'schema_version': 1, 'generated': True, 'schematic': True, 'compiled_model': False,
              'source_design': {'path': public_path(design_path), 'sha256': sha256(design_path)},
              'renderer': {'path': public_path(__file__), 'sha256': sha256(__file__)},
              'geometry_module': {'path': public_path(module_path), 'sha256': sha256(module_path)},
              'sampled_geometry_sha256': hashlib.sha256(json.dumps(geometry, sort_keys=True,
                  separators=(',', ':'), allow_nan=False).encode()).hexdigest(),
              'method': 'Pillow and NumPy; orthographic projection with triangle depth buffer',
              'surface_source': 'Exact road points and widths returned by build_geometry(design)',
              'route_arrow_source': 'Directed sampled routes returned by build_geometry(design)',
              'decorative_only': ['road-edge strokes', 'lane markings', 'route arrow glyphs', 'sunlight shadows'],
              'not_modelled': ['support columns', 'structural decks', 'native tiles', 'native joining seams', 'traffic signals'],
              'supersampling_factor': SUPERSAMPLE,
              'images': images}
    evidence_dir = output_dir.parent / 'evidence'
    evidence_dir.mkdir(parents=True, exist_ok=True)
    evidence_path = evidence_dir / 'render.json'
    evidence_path.write_text(json.dumps(report, indent=2, allow_nan=False) + '\n', encoding='utf-8')
    print(f'Evidence {public_path(evidence_path)}', flush=True)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--design', type=Path, required=True)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    render(args.design, args.output_dir)


if __name__ == '__main__':
    main()
