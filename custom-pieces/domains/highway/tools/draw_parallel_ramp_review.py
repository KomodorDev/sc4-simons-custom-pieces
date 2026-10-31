#!/usr/bin/env python3
"""Draw the source-only tight, parallel-ramp design review.

The geometry provider owns the candidate routes and geometric measurements.
This supplementary figure does not change game definitions, recipes, native
resources, assembly placements, installed files, or manual observations.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import html
import json
import math
from pathlib import Path
import sys

from PIL import Image, ImageChops, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'framework'))
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0, SourcePackages(ROOT))
from scp.preview import font

from draw_further_atomization_review import Canvas as BaseCanvas, saved_inputs, support_measurements

SUBJECT = 'ddrhw-l1-and-l2-diagonal-avenue-modular-diamond'
COLORS = {'lower-off': '#197ba4', 'lower-on': '#255aa7',
          'upper-off': '#c77720', 'upper-on': '#ab4b71',
          'highway': '#7e8993', 'avenue': '#516473'}
WIDTH, HEIGHT = 3360, 2800


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def stable(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':')).encode()


class Canvas(BaseCanvas):
    """Raster and vector text, dimensions, traffic arrows, and editable lines."""

    def __init__(self):
        self.image = Image.new('RGB', (WIDTH, HEIGHT), '#f7f9fb')
        self.draw = ImageDraw.Draw(self.image)
        self.svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">',
                    f'<rect width="{WIDTH}" height="{HEIGHT}" fill="#f7f9fb"/>']

    def polygon(self, points, color, outline=None, width=1):
        self.draw.polygon(points, fill=color)
        if outline:
            self.draw.line(points + points[:1], fill=outline, width=width)
        self.svg.append('<polygon points="' + ' '.join(f'{x:.3f},{y:.3f}' for x, y in points)
                        + f'" fill="{color or "none"}" stroke="{outline or "none"}" stroke-width="{width}"/>')

    def wrapped(self, x, y, value, max_width, size=24, colour='#25384b', bold=False, leading=None):
        words = value.split()
        lines, line = [], ''
        for word in words:
            candidate = (line + ' ' + word).strip()
            if line and self.draw.textlength(candidate, font=font(size, bold)) > max_width:
                lines.append(line)
                line = word
            else:
                line = candidate
        if line:
            lines.append(line)
        for index, line in enumerate(lines):
            self.text(x, y + index * (leading or size + 10), line, size, colour, bold)
        return y + len(lines) * (leading or size + 10)


def arrow_on(canvas, points, colour, fraction=.56, size=18, width=3):
    segments = [(a, b, math.dist(a, b)) for a, b in zip(points, points[1:])]
    remaining = sum(row[2] for row in segments) * fraction
    for a, b, length in segments:
        if not length:
            continue
        if remaining <= length:
            amount = remaining / length
            end = (a[0] + amount * (b[0] - a[0]), a[1] + amount * (b[1] - a[1]))
            start = (end[0] - size * (b[0] - a[0]) / length,
                     end[1] - size * (b[1] - a[1]) / length)
            canvas.arrow(start, end, colour, width)
            return
        remaining -= length


def boundary_edges(cells):
    """Return whole-tile ownership borders, without internal cell diagonals."""
    owned = {tuple(cell) for cell in cells}
    for col, row in owned:
        east, north = 16. * col, -16. * row
        for neighbour, edge in (
                ((col - 1, row), ((east - 8, north - 8), (east - 8, north + 8))),
                ((col + 1, row), ((east + 8, north - 8), (east + 8, north + 8))),
                ((col, row - 1), ((east - 8, north + 8), (east + 8, north + 8))),
                ((col, row + 1), ((east - 8, north - 8), (east + 8, north - 8)))):
            if neighbour not in owned:
                yield edge


def pastel(colour, amount=.13):
    rgb = [int(colour[i:i+2], 16) for i in (1, 3, 5)]
    return '#' + ''.join(f'{round(amount * value + (1 - amount) * 255):02x}' for value in rgb)


def ninety_marker(canvas, point, along, across, colour='#263c4f', arm=2.2):
    """Draw a true right-angle square using the provider's unit directions."""
    origin = point
    a = (origin[0] + arm * along[0], origin[1] + arm * along[1])
    b = (a[0] + arm * across[0], a[1] + arm * across[1])
    c = (origin[0] + arm * across[0], origin[1] + arm * across[1])
    return [a, b, c]


def source_measurements(route):
    points = route['points']
    lengths = [0.]
    grades = []
    for a, b in zip(points, points[1:]):
        length = math.dist(a[:2], b[:2])
        if length <= 1e-10:
            raise ValueError('Candidate drawing requires nonstationary plan samples')
        lengths.append(lengths[-1] + length)
        grades.append(100 * (b[2] - a[2]) / length)
    return {'length_m': lengths[-1], 'run_m': lengths,
            'maximum_grade_percent': max(map(abs, grades)),
            'start_height_m': points[0][2], 'end_height_m': points[-1][2]}


def occupied_bounds(cells):
    cells = [tuple(cell) for cell in cells]
    return (min(c[0] for c in cells), min(c[1] for c in cells),
            max(c[0] for c in cells), max(c[1] for c in cells))


def filtered_native_routes(routes, candidate):
    """Keep the retained stamp plus actual straight Avenue reference PATHs."""
    selected = []
    stamp = set(map(tuple, candidate['stamp_cells']))
    avenue_extent = candidate['avenue_extent_v_m']
    for route in routes:
        points = route['source_points']
        if route['placement'] == 0:
            if route['source_cell'] in stamp:
                selected.append(route)
            continue
        # The Avenue lies along v, with lateral u fixed at the measured
        # native lane/pedestrian position. Reject the old curved terminals.
        us = [(p[0] + p[1]) / math.sqrt(2.) for p in points]
        if max(abs(p[2]) for p in points) <= 1e-7 and max(us) - min(us) <= 1e-7:
            kept = []
            for a, b in zip(points, points[1:]):
                av = (a[1] - a[0] + 8.) / math.sqrt(2.)
                bv = (b[1] - b[0] + 8.) / math.sqrt(2.)
                if abs(bv - av) < 1e-10:
                    continue
                ts = sorted(((-avenue_extent - av) / (bv - av),
                             (avenue_extent - av) / (bv - av)))
                low, high = max(0., ts[0]), min(1., ts[1])
                if high - low <= 1e-10:
                    continue
                aa = tuple(x + (y - x) * low for x, y in zip(a, b))
                bb = tuple(x + (y - x) * high for x, y in zip(a, b))
                if not kept or math.dist(kept[-1], aa) > 1e-10:
                    kept.append(aa)
                kept.append(bb)
            if len(kept) >= 2:
                selected.append({**route, 'source_points': kept})
    return selected


def avenue_cover_measurements(payload, native_cells, routes):
    """Check the proposed Avenue union against measured pavement and feet."""
    from scp_highway import ramp_geometry as geometry, ramp_paths as paths
    template_cells = ((0, -1), (-1, 0))
    points = [p for cell in template_cells for triangle in native_cells[cell]['triangles']
              if triangle['mesh'] == 'Avenue' for p in triangle['points']]
    half_width = max(abs(geometry.highway_coordinates(p)[0]) for p in points)
    pedestrian_offsets = sorted({round(geometry.highway_coordinates(p)[0], 10)
                                 for route in routes if route['transport'] == 2
                                 and route['source_cell'] in template_cells
                                 for p in route['source_points']})
    results = []
    for candidate in payload['candidates']:
        extent = candidate['avenue_extent_v_m']
        source = [geometry.world_coordinates(u, v)
                  for u, v in ((-half_width, -extent), (half_width, -extent),
                               (half_width, extent), (-half_width, extent))]
        model = [(e, 0., -n, 0., 0.) for e, n, _h in source]
        faces = [(model[0], model[1], model[2]), (model[0], model[2], model[3])]
        projection = set(geometry.partition_triangles(faces))
        pedestrians = {cell for u in pedestrian_offsets
                       for cell, _part in paths.polyline_fragments(
                           [geometry.world_coordinates(u, -extent), geometry.world_coordinates(u, extent)])}
        declared = set(map(tuple, candidate['avenue_cells']))
        if projection - declared or pedestrians - declared:
            raise ValueError('Candidate Avenue cells miss measured-width pavement or pedestrian traces')
        results.append({'candidate': candidate['id'], 'extent_v_m': extent,
                        'declared_avenue_cells': sorted(map(list, declared)),
                        'full_width_projection_cells': sorted(map(list, projection)),
                        'pedestrian_trace_cells': sorted(map(list, pedestrians)),
                        'projection_missing_cells': [], 'pedestrian_missing_cells': []})
    return {'native_template_cells': list(map(list, template_cells)),
            'measured_native_ground_half_width_u_m': half_width,
            'measured_native_pedestrian_offsets_u_m': pedestrian_offsets,
            'projection_scope': 'Conservative full-width strip through selected Avenue extent, using measured native template width; not a newly compiled Avenue.',
            'candidates': results}


def plan_map(canvas, candidate, native_cells, native_routes, origin=(120, 230), size=1610):
    """Draw equal-scale candidate geometry on the unchanged reference grid."""
    ox, oy = origin
    all_cells = set(map(tuple, candidate['owned_cells'])) | set(native_cells)
    # Include the complete accepted 10-by-10 plot so that land savings cannot
    # be exaggerated by changing the plot's coordinate system or cropping.
    cols = [cell[0] for cell in all_cells] + [-4, 5]
    rows = [cell[1] for cell in all_cells] + [-4, 5]
    min_c, max_c, min_r, max_r = min(cols), max(cols), min(rows), max(rows)
    edge_min_e, edge_max_e = 16 * min_c - 8., 16 * max_c + 8.
    edge_min_n, edge_max_n = -16 * max_r - 8., -16 * min_r + 8.
    scale = min(size / (edge_max_e - edge_min_e), size / (edge_max_n - edge_min_n))

    def point(e, n):
        return ox + (e - edge_min_e) * scale, oy + (edge_max_n - n) * scale

    route_cells = set(map(tuple, candidate['owned_cells']))
    stamp_cells = set(map(tuple, candidate['stamp_cells']))
    for col, row in sorted(route_cells):
        e, n = 16. * col, -16. * row
        a, b = point(e - 8, n + 8), point(e + 8, n - 8)
        canvas.rect((*a, *b), '#e2eaf1' if (col, row) in stamp_cells else '#edf2e6')
    for col in range(min_c, max_c + 2):
        e = 16. * col - 8.
        canvas.line([point(e, edge_min_n), point(e, edge_max_n)], '#c5cfd9', 1)
    for row in range(min_r, max_r + 2):
        n = -16. * row + 8.
        canvas.line([point(edge_min_e, n), point(edge_max_e, n)], '#c5cfd9', 1)

    # Native reference: all actual first-frame, indexed face projections of
    # the retained stamp. Its overhang is therefore visible independently
    # from the tile ownership border.
    native_mask = Image.new('L', canvas.image.size, 0)
    draw = ImageDraw.Draw(native_mask)
    for cell in candidate['stamp_cells']:
        record = native_cells.get(tuple(cell))
        if record is None:
            continue
        for triangle in record['triangles']:
            draw.polygon([point(*p[:2]) for p in triangle['points']], fill=255)
    layer = Image.new('RGBA', canvas.image.size, (0, 0, 0, 0))
    layer.paste('#d4dbe0', (0, 0), native_mask)
    edge = ImageChops.subtract(native_mask.filter(ImageFilter.MaxFilter(3)),
                              native_mask.filter(ImageFilter.MinFilter(3)))
    layer.paste('#7e8993', (0, 0), edge)
    canvas.raster(layer)

    for route in candidate['routes']:
        colour = COLORS[route['id']]
        for outline in route['ribbon_outlines_en']:
            canvas.polygon([point(*p[:2]) for p in outline], pastel(colour, .29), colour, 2)
    for route in native_routes:
        points = [point(*p[:2]) for p in route['source_points']]
        elevated = max(p[2] for p in route['source_points']) > .01
        colour = '#617587' if elevated else '#5a7a51' if route['transport'] == 2 else '#485e70'
        canvas.line(points, colour, 2)
        if sum(math.dist(a, b) for a, b in zip(points, points[1:])) > 35:
            arrow_on(canvas, points, colour, width=2, size=12)

    # Planned owner-union border and native stamp boundary are separate
    # from coloured model silhouettes. Shared-cell assignments remain a
    # source design constraint, rather than a saved-resource claim.
    for edge in boundary_edges(route_cells):
        canvas.line([point(*p) for p in edge], '#283d4f', 4)
    for edge in boundary_edges(stamp_cells):
        canvas.line([point(*p) for p in edge], '#708294', 2, True)

    route_stats = {}
    for route in candidate['routes']:
        colour = COLORS[route['id']]
        points = [point(*p[:2]) for p in route['points']]
        canvas.line(points, colour, 5)
        for fraction in (.2, .48, .8):
            arrow_on(canvas, points, colour, fraction, 23, 4)
        route_stats[route['id']] = source_measurements(route)
        approach = route['approach']
        if abs(approach['angle_to_avenue_degrees'] - 90.) > 1e-7:
            raise ValueError('A displayed 90-degree approach is not perpendicular')
        at = approach['point_enh']
        tangent = approach['unit_tangent_en']
        across = (-tangent[1], tangent[0])
        marker = ninety_marker(canvas, at, tangent, across)
        canvas.line([point(*p) for p in marker], '#263c4f', 3)
        px, py = point(*at[:2])
        dx = -42 if tangent[0] > 0 else 10
        canvas.rect((px + dx - 3, py - 37, px + dx + 52, py - 6), 'white')
        canvas.text(px + dx, py - 38, '90°', 22, '#263c4f', True)
        # Label the clear parallel middle, away from the crowded junction.
        parallels = [seg for seg in route['segments'] if 'parallel' in seg['kind']]
        at_index = ((parallels[0]['start_index'] + parallels[0]['end_index']) // 2
                    if parallels else len(route['points']) // 3)
        px, py = points[at_index]
        short = {'lower-off': 'L-out', 'lower-on': 'L-in',
                 'upper-off': 'U-out', 'upper-on': 'U-in'}[route['id']]
        canvas.rect((px + 8, py + 8, px + 108, py + 44), 'white')
        canvas.text(px + 12, py + 7, short, 23, colour, True)

    # Retained supports are measured indexed native faces. Proposed ramp
    # supports remain visibly distinct hollow squares.
    retained_supports = [support for support in support_measurements(native_cells)[:6]
                         if tuple(support['source_cell']) in stamp_cells]
    for support in retained_supports:
        low, high = support['bounds_ENH_m']
        a, b = point(low[0], high[1]), point(high[0], low[1])
        canvas.rect((a[0] - 2, a[1] - 2, b[0] + 2, b[1] + 2), 'white')
        canvas.rect((*a, *b), '#23374d')
    proposed_supports = []
    for route in candidate['routes']:
        for support in route['supports']:
            canvas.polygon([point(*p) for p in support['footprint_en']], 'white', COLORS[route['id']], 3)
            proposed_supports.append({'route': route['id'], **support})

    for col in range(min_c, max_c + 1):
        x, y = point(16. * col, edge_min_n)
        canvas.text(x - 9, y + 17, str(col + 4), 25)
    for row in range(min_r, max_r + 1):
        x, y = point(edge_min_e, -16. * row)
        canvas.text(x - 43, y - 17, str(5 - row), 25)
    bottom = point(edge_min_e, edge_min_n)[1]
    canvas.text(ox + 270, bottom + 65, 'X — east | fixed tile centres | 1 tile = 16 m', 27)
    canvas.text(ox - 67, oy, 'Y', 28, bold=True)
    canvas.arrow((ox - 54, oy + 117), (ox - 54, oy + 62), '#25384b', 3)
    canvas.text(ox - 66, oy + 130, 'N', 23, bold=True)
    # This dimension uses the exact map projection, not an independent
    # approximate scale bar.
    a = (ox + 17, bottom + 126)
    b = (a[0] + 16 * scale, a[1])
    canvas.line([a, b], '#25384b', 4)
    for x, y in (a, b):
        canvas.line([(x, y - 7), (x, y + 7)], '#25384b', 3)
    canvas.text(a[0], a[1] + 13, '16 m', 23)
    return {'pixel_per_m': scale, 'route_statistics': route_stats,
            'bounds_source_cells': [min_c, min_r, max_c, max_r],
            'planned_owned_union_count': len(route_cells),
            'retained_measured_supports': retained_supports,
            'proposed_source_supports': proposed_supports}


def info_panel(canvas, payload, candidate):
    x, width = 1845, 1420
    y = 230
    canvas.text(x, y, 'Tight parallel ramps; perpendicular Avenue approaches', 32, bold=True)
    y = canvas.wrapped(x, y + 61,
        'L-out / L-in = lower-deck exit / entry. U-out / U-in = upper-deck exit / entry. '
        'Each coloured arrow follows the proposed traffic direction.', width, 25)
    y += 26
    for rid, full in [('lower-off', 'Lower-deck exit ramp'), ('lower-on', 'Lower-deck entry ramp'),
                      ('upper-off', 'Upper-deck exit ramp'), ('upper-on', 'Upper-deck entry ramp')]:
        canvas.line([(x, y + 16), (x + 49, y + 16)], COLORS[rid], 6)
        canvas.text(x + 67, y, full, 27, COLORS[rid], True)
        y += 48
    y += 15
    canvas.text(x, y, 'Measured source routes', 31, bold=True)
    y += 57
    canvas.text(x, y, 'Ramp', 25, bold=True)
    canvas.text(x + 260, y, 'Travel length', 25, bold=True)
    canvas.text(x + 540, y, 'Height change', 25, bold=True)
    canvas.text(x + 900, y, 'Maximum grade', 25, bold=True)
    y += 43
    for route in candidate['routes']:
        metrics = source_measurements(route)
        rid = route['id']
        canvas.text(x, y, rid.replace('-', ' '), 25, COLORS[rid], True)
        canvas.text(x + 260, y, f'{metrics["length_m"]:.2f} m', 25)
        canvas.text(x + 540, y, f'{metrics["start_height_m"]:g} → {metrics["end_height_m"]:g} m', 25)
        canvas.text(x + 900, y, f'{metrics["maximum_grade_percent"]:.2f}%', 25)
        y += 43
    y += 24
    bounds = occupied_bounds(candidate['owned_cells'])
    rectangle = (bounds[2] - bounds[0] + 1, bounds[3] - bounds[1] + 1)
    canvas.text(x, y, 'Land use on the same 16 m grid', 31, bold=True)
    y += 55
    canvas.text(x, y, f'{len(candidate["owned_cells"])} conservative service/model cells; {rectangle[0]} × {rectangle[1]} tile bounds.', 27, bold=True)
    y += 47
    y = canvas.wrapped(x, y,
        'The faint reference grid retains the previous 10 × 10 coordinate frame. '
        f'The proposed {rectangle[0]} × {rectangle[1]} cell envelope is inset within that frame.', width, 25)
    y += 24
    baseline = payload['baselines']['r40']
    comparison = next(row for row in payload['candidates'] if row['id'] != candidate['id'])
    canvas.text(x, y, f'Current R40 layout: {baseline["cell_count"]} occupied cells, 10 × 10 bounds.', 25)
    y += 41
    canvas.text(x, y, f'Parallel layout retaining old sockets: {len(comparison["owned_cells"])} cells, {comparison["bounds"]["tiles"][0]} × {comparison["bounds"]["tiles"][1]} bounds.', 25)
    y += 55
    parallel_offsets = []
    for route in candidate['routes']:
        values = []
        for segment in route['segments']:
            if 'parallel' not in segment['kind']:
                continue
            samples = route['points_uvh'][segment['start_index']:segment['end_index'] + 1]
            values.extend(abs(p[1]) for p in samples)
        if values:
            parallel_offsets.append((route['id'], min(values), max(values)))
    if parallel_offsets:
        minimum = min(row[1] for row in parallel_offsets)
        maximum = max(row[2] for row in parallel_offsets)
        if abs(maximum - minimum) < .001:
            value = f'{minimum:.2f} m'
        else:
            value = f'{minimum:.2f}–{maximum:.2f} m'
        y = canvas.wrapped(x, y,
            f'Parallel ramp centre offset: {value} from the highway axis. '
            'The source road is 6.00 m wide; its entire width and barriers must fit beside the deck.', width, 25)
        y = canvas.wrapped(x, y + 12,
            f'Straight-run lateral edge gap: {minimum - 8. - 3.:.2f} m minimum '
            '(16.00 m native deck; 6.00 m ramp). Curved joins need separate clearance checks.', width, 25)
        y += 24
    canvas.text(x, y, 'Read the outlines separately', 30, bold=True)
    y += 53
    legend_rows = [('#283d4f', False, 'Dark solid borders: conservative service/model cell union.'),
                   ('#708294', True, 'Grey dashed borders: native highway-stamp cells.'),
                   ('#197ba4', False, 'Thin coloured outlines: new source model projection.'),
                   ('#485e70', False, 'Thin grey / green lines: saved Avenue cars / pedestrians.')]
    for colour, dashed, text in legend_rows:
        canvas.line([(x, y + 15), (x + 52, y + 15)], colour, 4 if colour == '#283d4f' else 2, dashed)
        canvas.text(x + 68, y, text, 24)
        y += 43
    canvas.text(x, y, 'Filled black squares: retained piers. Hollow squares: source ramp piers.', 23)
    y += 43
    y += 22
    canvas.text(x, y, '90° means the straight approach meets the Avenue squarely.', 26, bold=True)
    y += 45
    y = canvas.wrapped(x, y,
        f'The vehicle then follows a right turn of radius {candidate["ground_turn_radius_m"]:g} m into the adjacent carriageway. '
        'The terminal does not send traffic across the Avenue.', width, 25)
    y += 23
    if candidate['changed_native_high_sockets']:
        y = canvas.wrapped(x, y,
            f'Upper sockets move {candidate["upper_socket_shift_along_highway_m"]:.2f} m inward. '
            'The straight stamp shortens to 17 cells. Slip-lane markings, seams, and the separate-piece ownership plan need revision.', width, 25)
    return {'parallel_offsets_m': parallel_offsets, 'info_bottom_pixel': y}


def profile_panel(canvas, candidate, deck, x, y, width=1555, height=525):
    canvas.rect((x, y, x + width, y + height), 'white', '#c6d0d9', 2)
    title = 'Lower deck — 7.5 m to ground' if deck == 'lower' else 'Upper deck — 15 m to ground'
    canvas.text(x + 25, y + 18, title, 30, bold=True)
    canvas.text(x + 25, y + 63, 'Source side profiles | horizontal distance follows traffic direction', 24)
    routes = [route for route in candidate['routes'] if route['deck'] == deck]
    stats = {route['id']: source_measurements(route) for route in routes}
    maximum_length = math.ceil(max(row['length_m'] for row in stats.values()) / 10) * 10.
    maximum_height = 8. if deck == 'lower' else 16.
    gx, gy, gw, gh = x + 91, y + 132, width - 165, 265

    def point(s, h):
        return gx + s / maximum_length * gw, gy + gh - h / maximum_height * gh

    for step in range(5):
        h = maximum_height * step / 4
        canvas.line([point(0, h), point(maximum_length, h)], '#d8e0e6', 1)
        canvas.text(gx - 47, point(0, h)[1] - 13, f'{h:g}', 21)
    ticks = list(range(0, int(maximum_length) + 1, 20))
    for distance in ticks:
        canvas.line([point(distance, 0), point(distance, maximum_height)], '#e4e9ee', 1)
        canvas.text(point(distance, 0)[0] - 11, gy + gh + 13, str(distance), 21)
    for route in routes:
        stats_row = stats[route['id']]
        points = [point(s, p[2]) for s, p in zip(stats_row['run_m'], route['points'])]
        colour = COLORS[route['id']]
        canvas.line(points, colour, 4)
        for fraction in (.25, .72):
            arrow_on(canvas, points, colour, fraction, 19, 3)
    canvas.text(gx, y + 453, 'Run in metres; height axis in metres.', 22)
    canvas.text(gx + 570, y + 453, 'Exit descends; entry climbs.', 22, bold=True)
    canvas.text(gx, y + 489, 'Horizontal and vertical axes use different scales.', 20)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build', type=Path, required=True)
    parser.add_argument('--candidate', default='parallel-inward-upper')
    parser.add_argument('--destination', type=Path)
    args = parser.parse_args()
    from scp_highway.parallel_ramp_review import review
    payload = review()
    candidate = next(row for row in payload['candidates'] if row['id'] == args.candidate)
    build = args.build.resolve()
    dest = args.destination or ROOT / 'domains/highway/01_assemblies' / SUBJECT
    scene_path, scene, pieces, owners, resources, routes, cells, records = saved_inputs(build)
    native_routes = filtered_native_routes(routes, candidate)
    avenue_cover = avenue_cover_measurements(payload, cells, routes)
    canvas = Canvas()
    canvas.text(65, 28, 'Assembly - DD RHW-4 — Modular Diagonal Avenue Diamond', 44, bold=True)
    canvas.text(65, 91, 'Component guide | Close parallel ramps | Perpendicular Avenue approaches | Top view | North up', 30)
    canvas.text(65, 144, 'SOURCE-ONLY PROPOSAL: new ramp geometry | Saved native highway / Avenue reference | Fixed X/Y tile grid', 26, bold=True)
    map_report = plan_map(canvas, candidate, cells, native_routes)
    info_report = info_panel(canvas, payload, candidate)
    profile_panel(canvas, candidate, 'lower', 65, 2120)
    profile_panel(canvas, candidate, 'upper', 1735, 2120)
    canvas.text(75, 2690, 'Geometric cells and model projections are design measurements. New ownership, interfaces, clearance, construction, and four rotations need validation.', 24)
    canvas.text(75, 2734, 'Current game recipes, assembly placements, plugin files, and manual observations remain unchanged by this review.', 24)
    previews, evidence = dest / 'previews', dest / 'evidence'
    previews.mkdir(parents=True, exist_ok=True)
    evidence.mkdir(parents=True, exist_ok=True)
    png, svg = previews / 'parallel-ramp-review.png', previews / 'parallel-ramp-review.svg'
    canvas.image.save(png)
    svg.write_text('\n'.join(canvas.svg + ['</svg>']) + '\n')
    report = {'schema_version': 1,
              'purpose': 'Supplementary line drawing of the source-only close parallel ramp proposal.',
              'selected_candidate': candidate['id'],
              'source_geometry_review_sha256': digest(stable(payload)),
              'source_geometry_review': payload,
              'source_scene_sha256': digest(scene_path.read_bytes()),
              'source_saved_cells': records,
              'native_reference_route_count': len(native_routes),
              'native_reference_routes_sha256': digest(stable(native_routes)),
              'independent_native_avenue_coverage': avenue_cover,
              'generator_sha256': digest(Path(__file__).read_bytes()),
              'geometry_provider_sha256': digest((ROOT / 'domains/highway/implementation/scp_highway/parallel_ramp_review.py').read_bytes()),
              'drawing': {**map_report, **info_report, 'canvas_pixels': [WIDTH, HEIGHT],
                          'fixed_display_grid': 'X=source column+4; Y=5-source row; tile centres.',
                          'tile_size_m': 16,
                          'model_outline_scope': 'New six-metre source ribbon projections; saved native stamp indexed-face projection.',
                          'ownership_scope': 'Geometric planned occupied-cell union; saved-resource and game placement unverified.',
                          'profiles': 'Actual candidate sample heights against planar travel distance, with separate horizontal and vertical scales.'},
              'outputs': {'png': {'path': str(png.relative_to(dest)), 'sha256': digest(png.read_bytes())},
                          'svg': {'path': str(svg.relative_to(dest)), 'sha256': digest(svg.read_bytes())}},
              'game_resources_changed': False, 'manual_observations_changed': False, 'installed': False}
    (evidence / 'parallel-ramp-review.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'candidate': candidate['id'], 'cells': len(candidate['owned_cells']),
                      'outputs': [str(path.relative_to(dest)) for path in (png, svg)],
                      'geometry_review_sha256': report['source_geometry_review_sha256']}))


if __name__ == '__main__':
    main()
