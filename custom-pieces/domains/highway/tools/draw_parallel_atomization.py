#!/usr/bin/env python3
"""Draw the implemented parallel split from actual saved S3D and PATH resources.

The figure supplements the canonical six assembly views. It reads no route
writer or proposed model geometry. Every route, model projection, obstacle,
and grade-cut location is measured from the selected saved resources.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import json
import math
from pathlib import Path
import re
import sys

from PIL import Image, ImageChops, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'framework'))
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0, SourcePackages(ROOT))
from scp import jsonc
from scp.dbpf import decompress, entries, require
from scp.models import parse_s3d, positions
from scp.preview import font
from scp_highway.native import parse_paths
from scp_highway.parallel_verify import check_owned_cells, verify_assembly
from scp_hsr_tools.assembly_annotations import colour_assignment_for_sources

from draw_parallel_ramp_review import Canvas as ReviewCanvas, arrow_on

SUBJECT = 'ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond'
WIDTH, HEIGHT = 3600, 3020
PLOT_LEFT, PLOT_TOP, SCALE = 130, 230, 10.5
ROOT_TWO = math.sqrt(2.0)


class Canvas(ReviewCanvas):
    def __init__(self):
        self.image = Image.new('RGB', (WIDTH, HEIGHT), '#f7f9fb')
        self.draw = ImageDraw.Draw(self.image)
        self.svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">',
                    f'<rect width="{WIDTH}" height="{HEIGHT}" fill="#f7f9fb"/>']


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def point(east, north):
    # Fixed old 10×10 frame: X=east/16+4, Y=north/16+5.
    return PLOT_LEFT + (east + 72.) * SCALE, PLOT_TOP + (72. - north) * SCALE


def source_triangles(raw, cell):
    """Decode only actual referenced triangle indices in their true world pose."""
    model = parse_s3d(raw)
    for mesh in model['meshes']:
        require(len(mesh['frames']) == 1, 'Implemented drawing requires actual static model frames')
        vi, ii, pi, mi = mesh['frames'][0]
        vertices = positions(model['vertices'][vi])
        indices = model['indices'][ii]['values']
        material = model['materials'][mi]
        for kind, first, count in model['primitives'][pi]:
            require(kind == 0 and count % 3 == 0, 'Implemented drawing requires indexed triangle lists')
            for index in range(first, first + count, 3):
                tri = [(vertices[k][0] + 16 * cell[0], -vertices[k][2] - 16 * cell[1], vertices[k][1])
                       for k in indices[index:index + 3]]
                yield {'points': tri, 'textures': material['textures'],
                       'mesh': mesh['name'].rstrip(b'\0').decode('ascii', 'replace')}


def source_routes(raw, cell, placement):
    records = parse_paths(raw)
    comments = re.findall(rb'^-- SCP (.*?) source_lane=', raw, re.M)
    require(len(comments) == len(records), 'Saved PATH comments do not match its actual route records')
    for row, comment in zip(records, comments):
        yield {**row, 'role': comment.decode('ascii'), 'placement': placement,
               'source_cell': list(cell),
               'points': [(p[0] + 16 * cell[0], p[1] - 16 * cell[1], p[2]) for p in row['points']]}


def stitch(routes, identifier):
    selected = [row for row in routes if row['role'] == identifier]
    key = lambda p: tuple(round(v, 6) for v in p)
    starts = {key(row['points'][0]): row for row in selected}
    ends = {key(row['points'][-1]) for row in selected}
    initial = set(starts) - ends
    require(len(starts) == len(selected) and len(initial) == 1, 'Saved ramp is not one unambiguous car chain')
    current, result, seen = starts[next(iter(initial))], [], set()
    while current is not None:
        marker = key(current['points'][0])
        require(marker not in seen, 'Saved ramp contains a cycle')
        seen.add(marker)
        result += current['points'] if not result else current['points'][1:]
        current = starts.get(key(result[-1]))
    require(len(seen) == len(selected), 'Saved ramp has disconnected fragments')
    if result[0][2] < result[-1][2]:
        result.reverse()
    lengths = [0.]
    for a, b in zip(result, result[1:]):
        lengths.append(lengths[-1] + math.dist(a[:2], b[:2]))
    # Independently measure the longest exact diagonal straight from saved
    # samples. Tile-edge interpolation can insert more collinear points.
    runs, first = [], None
    for index, (a, b) in enumerate(zip(result, result[1:])):
        dx, dy = b[0] - a[0], b[1] - a[1]
        run = math.hypot(dx, dy)
        aligned = abs(dx - dy) <= 3e-9  # Four saved decimal-rounding residuals, in metres.
        if aligned and first is None:
            first = index
        if first is not None and (not aligned or index == len(result) - 2):
            last = index if not aligned else index + 1
            runs.append((lengths[last] - lengths[first], first, last))
            first = None
    length, first, last = max(runs)
    require(length > 40. and result[first][2] > 7. and result[last][2] == 0.,
            'Saved ramp lacks its approved complete straight grade')
    return {'id': identifier, 'points': result, 'run_m': lengths, 'straight_indices': [first, last],
            'straight_length_m': length,
            'maximum_grade_percent': max(100 * abs(b[2] - a[2]) / math.dist(a[:2], b[:2])
                                         for a, b in zip(result, result[1:])),
            'traffic_direction': 'high to ground' if identifier.endswith('off') else 'ground to high'}


def border_edges(cells):
    for col, row in cells:
        e, n = 16 * col, -16 * row
        for neighbour, edge in (((col - 1, row), ((e - 8, n - 8), (e - 8, n + 8))),
                                ((col + 1, row), ((e + 8, n - 8), (e + 8, n + 8))),
                                ((col, row - 1), ((e - 8, n + 8), (e + 8, n + 8))),
                                ((col, row + 1), ((e - 8, n - 8), (e + 8, n - 8)))):
            if neighbour not in cells:
                yield edge


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build', required=True, type=Path)
    parser.add_argument('--destination', type=Path)
    args = parser.parse_args()
    subject = ROOT / 'domains/highway/01_assemblies' / SUBJECT
    destination = args.destination or subject
    scene = jsonc.load(subject / 'assembly.jsonc')
    # Fail before creating artwork if the actual selected assembly fails.
    verification = verify_assembly(args.build, scene, evidence_path=destination / 'evidence/saved-assembly.json')
    manifest_raw = (args.build / 'manifest.json').read_bytes()
    manifest = json.loads(manifest_raw)
    pieces = {p['id']: p for p in manifest['pieces']}
    owners, shift = check_owned_cells(pieces, scene)
    selected = {row['piece_id'] for row in scene['placements']}
    resources, asset_provenance = {}, []
    for pid in sorted(selected):
        data = (args.build / pieces[pid]['asset_file']).read_bytes()
        resources[pid] = {key: decompress(value) for key, value in entries(data).items()}
        asset_provenance.append({'piece_id': pid, 'asset_file': pieces[pid]['asset_file'], 'sha256': digest(data)})
    sources = [{'label': f'P{i + 1:02d}', 'occupied_world_cells':
                [[16 * c[0] + shift[0], -16 * c[1] + shift[1]]
                 for c, owner in owners.items() if owner['placement'] == i]}
               for i in range(15)]
    colours = colour_assignment_for_sources(sources)['palette']
    triangles, routes, snapshots = defaultdict(list), [], []
    for cell, owner in sorted(owners.items()):
        rs = resources[owner['piece_id']]
        model, path = rs[0x5AD0E817, 0xBADB57F1, owner['tile']], rs[0x296678F7, 0xA966883F, owner['tile']]
        label = f'P{owner["placement"] + 1:02d}'
        triangles[label].extend(source_triangles(model, cell))
        routes.extend(source_routes(path, cell, label))
        snapshots.append({'placement': label, 'source_city_cell': list(cell),
                          'tile_id': f'{owner["tile"]:08X}', 'model_sha256': digest(model), 'path_sha256': digest(path)})
    ramps = [stitch(routes, key) for key in ('lower-off', 'lower-on', 'upper-off', 'upper-on')]
    canvas = Canvas()
    canvas.text(65, 30, 'Assembly - ' + scene['title'], 37, bold=True)
    canvas.text(65, 86, 'Component guide | Implemented atomization | Actual saved routes, model outlines, and selected cuts', 28)
    canvas.text(65, 133, '15 independently placed modules | 31 occupied city tiles | 8 × 8 core inside the retained X0–X9 / Y0–Y9 frame', 25)
    # Grey actual indexed model union lies below the translucent ownership.
    physical = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    pd = ImageDraw.Draw(physical)
    masks, obstacle_faces = {}, []
    for label, faces in triangles.items():
        mask = Image.new('L', (WIDTH, HEIGHT), 0)
        md = ImageDraw.Draw(mask)
        for face in faces:
            xy = [point(*p[:2]) for p in face['points']]
            md.polygon(xy, fill=255)
            textures = set(face['textures'])
            pavement = bool(textures & {0x5713000E, 0x5712000E, 0x0400020E, 0x0400380E})
            pd.polygon(xy, fill='#d5dce2' if pavement else '#aab4bf')
            ps = face['points']
            plan = {(round(p[0], 5), round(p[1], 5)) for p in ps}
            extent = [max(p[a] for p in ps) - min(p[a] for p in ps) for a in (0, 1)]
            if (0x5EB4BEEE in textures and len(plan) == 2 and min(p[2] for p in ps) <= 1e-6
                    and max(p[2] for p in ps) > 1.
                    and abs(max(extent) - .8) < 2e-5):
                obstacle_faces.append({'placement': label, 'points': ps})
        masks[label] = mask
    canvas.raster(physical)
    overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    for cell, owner in owners.items():
        label = f'P{owner["placement"] + 1:02d}'
        colour = colours[label]
        rgb = tuple(int(colour[i:i + 2], 16) for i in (1, 3, 5))
        a, b = point(16 * cell[0] - 8, -16 * cell[1] + 8), point(16 * cell[0] + 8, -16 * cell[1] - 8)
        od.rectangle((*a, *b), fill=(*rgb, 76))
    canvas.raster(overlay)
    for index in range(11):
        value = -72 + index * 16
        canvas.line([point(value, -88), point(value, 72)], '#bcc8d4', 1)
        north = -88 + index * 16
        canvas.line([point(-72, north), point(88, north)], '#bcc8d4', 1)
    # A distinct opaque outline follows each actual model, including overhang.
    for label, mask in masks.items():
        edge = ImageChops.subtract(mask.filter(ImageFilter.MaxFilter(5)), mask.filter(ImageFilter.MinFilter(3)))
        tint = Image.new('RGBA', (WIDTH, HEIGHT), colours[label])
        tint.putalpha(edge)
        canvas.raster(tint)
    for index in range(15):
        label = f'P{index + 1:02d}'
        cells = {c for c, owner in owners.items() if owner['placement'] == index}
        for edge in border_edges(cells):
            canvas.line([point(*p) for p in edge], '#25384b', 4)
        for col, row in cells:
            x, y = point(16 * col - 7.4, -16 * row + 7.4)
            canvas.text(x, y, label, 22, colours[label], True)
    for face in obstacle_faces:
        canvas.line([point(*p[:2]) for p in face['points']], '#172737', 6)
    for index in range(10):
        x, y = point(-64 + 16 * index, -88)
        canvas.text(x - 8, y + 16, str(index), 24)
        x, y = point(-72, -80 + 16 * index)
        canvas.text(x - 45, y - 13, str(index), 24)
    canvas.text(865, 1995, 'X (east) — 16 m per tile', 25)
    canvas.text(48, 230, 'Y', 26, bold=True)
    canvas.arrow((65, 350), (65, 280), '#25384b', 4)
    canvas.text(52, 365, 'N', 24, bold=True)
    for route in sorted(routes, key=lambda r: max(p[2] for p in r['points'])):
        h = max(p[2] for p in route['points'])
        colour = '#397b51' if route['transport'] == 2 else '#be6a21' if h > 10. else '#1e77a2' if h > 1. else '#596a76'
        xy = [point(*p[:2]) for p in route['points']]
        canvas.line(xy, colour, 2 if route['transport'] == 2 else 3,
                    dash=route['role'] == 'native-highway' and h > 10.)
        if sum(math.dist(a, b) for a, b in zip(xy, xy[1:])) > 35:
            arrow_on(canvas, xy, colour, .6, 14, 3)
    cuts = []
    for ri, ramp in enumerate(ramps):
        for kind, at in zip(('departure / grade', 'grade / terminal'), ramp['straight_indices']):
            centre = ramp['points'][at]
            first, last = ramp['points'][max(0, at - 1)], ramp['points'][min(len(ramp['points']) - 1, at + 1)]
            dx, dy = last[0] - first[0], last[1] - first[1]
            length = math.hypot(dx, dy)
            normal = -dy / length, dx / length
            a = centre[0] - 4.2 * normal[0], centre[1] - 4.2 * normal[1]
            b = centre[0] + 4.2 * normal[0], centre[1] + 4.2 * normal[1]
            label = f'K{len(cuts) + 1}'
            canvas.line([point(*a), point(*b)], '#9c3279', 5)
            x, y = point(*b)
            canvas.circle((x + 15, y - 10), 17, '#9c3279', width=3)
            canvas.text(x + 4, y - 23, label, 18, '#9c3279', True)
            cuts.append({'id': label, 'ramp': ramp['id'], 'function': kind, 'point_enh_m': centre,
                         'display_XY': [centre[0] / 16 + 4, centre[1] / 16 + 5]})
    # Full exact names and stable placement IDs match the canonical side legend.
    canvas.text(1930, 212, 'Components — exact menu names', 30, bold=True)
    y = 265
    for pose in scene['placements']:
        label = pose['instance_id']
        colour = colours[label]
        canvas.rect((1930, y + 5, 1980, y + 42), colour)
        canvas.text(1934, y + 10, label, 19, '#ffffff', True)
        y2 = canvas.wrapped(2000, y, pose['menu_name'], 1500, 25, bold=True, leading=32)
        piece = pieces[pose['piece_id']]
        x, yy = pose['display_origin_tiles_en']
        canvas.text(2000, y2 + 2, f'Position X{x}, Y{yy} | {len(piece["cells"])} owned tiles | 0°', 21, '#526478')
        y = max(y + 98, y2 + 39)
    canvas.text(1930, 1815, 'Read the two boundaries separately', 27, bold=True)
    canvas.line([(1935, 1870), (2015, 1870)], '#25384b', 5)
    canvas.text(2035, 1853, 'Thick dark line: actual occupied tile boundary', 23)
    canvas.line([(1935, 1915), (2015, 1915)], '#a35e2c', 4)
    canvas.text(2035, 1898, 'Coloured outline: actual indexed model, including overhang', 23)
    canvas.text(1930, 1950, 'K1–K8: physical cuts; city-edge PATH ports remain whole-tile.', 23, '#9c3279')
    canvas.text(1930, 1990, 'Black squares: real grounded pier walls. Arrows follow saved travel.', 23)
    canvas.text(1930, 2030, 'Blue: L1 | Orange: L2 (dashed when stacked) | Grey: Avenue | Green: pedestrians', 22)
    # Four saved profiles retain the real direction and fixed end heights.
    for index, ramp in enumerate(ramps):
        x0 = 130 + (index % 2) * 1770
        y0 = 2145 + (index // 2) * 360
        colour = '#1e77a2' if ramp['id'].startswith('lower') else '#be6a21'
        title = ramp['id'].replace('-', ' ').title()
        canvas.text(x0, y0, title + ' — actual saved vertical profile', 27, colour, True)
        canvas.text(x0, y0 + 43, f'Travel: {ramp["traffic_direction"]} | straight grade {ramp["straight_length_m"]:.3f} m | peak {ramp["maximum_grade_percent"]:.3f}%', 23)
        xbase, ybase, length = x0 + 55, y0 + 245, ramp['run_m'][-1]
        sx, sy = 1400 / length, 9.0
        canvas.line([(xbase, ybase - 150), (xbase, ybase), (xbase + 1420, ybase)], '#536577', 2)
        for h in (0., 7.5, 15.):
            canvas.text(x0, ybase - sy * h - 10, f'{h:g}', 18)
        curve = [(xbase + d * sx, ybase - p[2] * sy) for p, d in zip(ramp['points'], ramp['run_m'])]
        canvas.line(curve, colour, 4)
        for at in ramp['straight_indices']:
            x, yy = curve[at]
            canvas.line([(x, ybase + 8), (x, yy - 14)], '#9c3279', 2, True)
        canvas.text(xbase + 520, ybase + 18, 'Horizontal distance from highway (m)', 20)
    canvas.wrapped(75, 2890, 'The crossing and slip-lane models form the straight highway stem. Complete curved departures, straight graded ramps, and ground terminals remain separate physical models. Whole-cell traffic ownership is independent of those physical cuts; model overhang adds no second plot owner.', 3430, 24, leading=32)
    destination.joinpath('previews').mkdir(parents=True, exist_ok=True)
    destination.joinpath('evidence').mkdir(parents=True, exist_ok=True)
    png = destination / 'previews/parallel-atomization.png'
    svg = destination / 'previews/parallel-atomization.svg'
    canvas.image.save(png)
    svg.write_text('\n'.join(canvas.svg + ['</svg>']) + '\n')
    report = {'schema_version': 1, 'purpose': 'Implemented saved-resource atomization drawing',
              'assembly': SUBJECT, 'manifest_sha256': digest(manifest_raw),
              'assembly_definition_sha256': digest((subject / 'assembly.jsonc').read_bytes()),
              'generator_sha256': digest(Path(__file__).read_bytes()), 'asset_inputs': asset_provenance,
              'cells': snapshots, 'owned_cell_count': len(owners), 'placements': len(scene['placements']),
              'display_grid': {'X': [0, 9], 'Y': [0, 9], 'occupied_X': [1, 8], 'occupied_Y': [1, 8]},
              'actual_saved_routes': len(routes), 'actual_indexed_triangles': sum(map(len, triangles.values())),
              'grounded_pier_wall_triangles': len(obstacle_faces), 'physical_cuts': cuts,
              'ramp_profiles': [{k: v for k, v in r.items() if k not in ('points', 'run_m')} for r in ramps],
              'palette': colours, 'saved_assembly_verification_passed': (verification.get('saved_resource_checks_passed') is True
                  and verification.get('saved_path_checks_passed') is True
                  and verification.get('saved_ownership_checks_passed') is True
                  and verification.get('saved_path_and_construction_checks_passed') is True
                  and verification.get('package_construction_checks') == 'passed-actual-saved-controller-rules'),
              'artwork': {'png_sha256': digest(png.read_bytes()), 'svg_sha256': digest(svg.read_bytes())},
              'manual_observations_changed': False,
              'scope': 'Actual selected DAT models and PATHs, nonoverlapping traffic owners, selected physical cuts, and real structural footprints. No structural capacity or game observation is established.'}
    (destination / 'evidence/parallel-atomization.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'owned_cells': len(owners), 'placements': 15, 'routes': len(routes),
                      'triangles': report['actual_indexed_triangles'], 'physical_cuts': len(cuts)}))


if __name__ == '__main__':
    main()
