"""Draw standalone Highway button strips from registered component routes."""
from __future__ import annotations

import argparse
from io import BytesIO
from math import ceil, dist, floor
from pathlib import Path
import struct

from PIL import Image, ImageChops, ImageDraw, ImageOps

from scp.dbpf import require
from scp.menu_experiment_resources import _assembly_label as bitmap_label

ARTWORK = 'highway-piece-v1'
FRAME = 44
STATES = ('locked', 'normal', 'selected', 'highlighted')
FOOTER = 'PART HWY'
STYLES = {
    'ddrhw-crossing': 'XNG',
    'ddrhw-ghsr-crossing': 'XNG',
    'ddrhw-transition': 'RMP',
    'ddrhw-diagonal-transition': 'RMP',
    'ddrhw-y-stem': 'JCT',
    'ddrhw-y-branch': 'JCT',
    'ddrhw-y-core': 'JCT',
}


def icon_identity(piece):
    """Use registered roles for the readable category, network, and kind labels."""
    require(piece.get('domain') == 'highway', 'Standalone Highway icon requires a Highway piece')
    style = piece['menu']['style']
    if style in STYLES:
        kind = STYLES[style]
    else:
        require(style == 'ddrhw-ramp', 'Unsupported standalone Highway icon style')
        key = piece['geometry_key']
        if key.endswith(('crossing', 'access-core')):
            kind = 'XNG'
        elif key.startswith('diagonal-half-'):
            kind = 'DIA'
        elif key.endswith(('junction', 'terminal', 'terminal-r40', 'stamp')):
            kind = 'JCT'
        elif key.endswith('departure'):
            kind = 'CRV'
        elif key.endswith(('branch', 'slip')):
            kind = 'SPL' if 'exit-' in key else 'MRG'
        else:
            kind = 'RMP'
    return {'category': 'part', 'badge': 'PART', 'network': 'HWY', 'kind': kind}


def _cell_routes(cells, routes_by_cell, *, transports):
    return [[(x + 16 * column, y - 16 * row, height) for x, y, height in route['points']]
            for (column, row), routes in zip(cells, routes_by_cell, strict=True)
            for route in routes if route['transport'] in transports]


def _icon_routes(piece):
    style = piece['menu']['style']
    if style == 'ddrhw-crossing':
        from .verify import expected_paths
        return _cell_routes(piece['cells'], expected_paths(), transports=(1,))
    if style == 'ddrhw-ghsr-crossing':
        from .ghsr_crossing_verify import expected_paths
        return _cell_routes(piece['cells'], expected_paths(piece), transports=(1, 7))
    if style == 'ddrhw-transition':
        from .orthogonal_transition_geometry import traffic_routes
        from .orthogonal_transition_variants import variant_of
        return [route['points'] for route in traffic_routes(variant=variant_of(piece))]
    if style == 'ddrhw-diagonal-transition':
        from .diagonal_transition_geometry import traffic_routes
        from .diagonal_transition_variants import variant_of
        return [route['points'] for route in traffic_routes(variant=variant_of(piece))]
    from .icons import component_icon_routes
    routes = component_icon_routes(piece)
    return list(routes.values()) if isinstance(routes, dict) else routes


def _direction_line(routes):
    """Pick a stable high, long route and derive its direction from point order."""
    def length(route):
        return sum(dist(a[:2], b[:2]) for a, b in zip(route, route[1:]))

    route = max(routes, key=lambda points: (
        max(p[2] for p in points), length(points), tuple(sorted((points[0], points[-1])))))
    length_m = length(route)
    if length_m == 0:
        return None
    target = length_m * .5
    for first, second in zip(route, route[1:]):
        span = dist(first[:2], second[:2])
        if span and target <= span:
            fraction = target / span
            centre = tuple(a + (b-a)*fraction for a, b in zip(first[:2], second[:2]))
            return centre, ((second[0]-first[0])/span, (second[1]-first[1])/span)
        target -= span
    return None


def _draw_arrow(image, vertices, outline_width):
    """Keep the established triangle tips stable across Pillow scanline changes."""
    corners = [(int(x), int(y)) for x, y in vertices]
    mask = Image.new('1', image.size)
    pen = ImageDraw.Draw(mask)
    pen.polygon(corners, fill=1)
    for boundary, step in ((min, 1), (max, -1)):
        y = boundary(point[1] for point in corners)
        tips = [x for x, row in corners if row == y]
        if len(tips) != 1:
            continue
        x = tips[0]
        slopes = [(other_x-x)/(other_y-y) for other_x, other_y in corners if other_y != y]
        adjacent = [x+step*slope for slope in slopes]
        extent = x
        if all(slope > 0 for slope in slopes):
            extent = min(adjacent) if step == 1 else max(adjacent)+1
        elif all(slope < 0 for slope in slopes):
            extent = max(adjacent)+1 if step == 1 else min(adjacent)-1
        pen.line((0, y, image.width-1, y), fill=0)
        pen.line((floor(min(x, extent)+.5), y, ceil(max(x, extent)-.5), y), fill=1)
    image.paste('#fff8df', mask=mask)
    outline = Image.new('1', image.size)
    ImageDraw.Draw(outline).line(corners+[corners[0]], fill=1, width=outline_width*2-1)
    image.paste('#132b34', mask=ImageChops.logical_and(mask, outline))


def _diagram(routes, *, show_direction):
    scale = 6
    points = [point for route in routes for point in route]
    west, east = min(p[0] for p in points), max(p[0] for p in points)
    south, north = min(p[1] for p in points), max(p[1] for p in points)
    factor = min(31 / max(east-west, 1), 21 / max(north-south, 1))

    def screen(point):
        return ((21.5 + (point[0]-(west+east)/2)*factor)*scale,
                (21.0 - (point[1]-(south+north)/2)*factor)*scale)

    image = Image.new('RGBA', (FRAME * scale, FRAME * scale))
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((scale, scale, 42 * scale, 42 * scale), radius=5*scale,
                           fill='#142b35', outline='#35bcb1', width=scale)
    # Render each route from low to high, so overpasses retain the visual break.
    for route in sorted(routes, key=lambda row: sum(p[2] for p in row)/len(row)):
        planar = [screen(p) for p in route]
        draw.line(planar, fill='#091a21', width=round(3.6*scale), joint='curve')
        for first, last, a, b in zip(route, route[1:], planar, planar[1:]):
            elevation = min(1, max(0, (first[2]+last[2])/30))
            colour = tuple(round(low+(high-low)*elevation)
                           for low, high in zip((245, 215, 159), (83, 225, 215)))
            draw.line((a, b), fill=colour, width=round(1.85*scale))
    arrow = _direction_line(routes) if show_direction else None
    if arrow is not None:
        centre, (eastward, northward) = arrow
        x, y = screen(centre)
        dx, dy = eastward, -northward
        size = 3.1*scale
        _draw_arrow(image, [(x+dx*size, y+dy*size),
                            (x-dx*size/2-dy*size/2, y-dy*size/2+dx*size/2),
                            (x-dx*size/2+dy*size/2, y-dy*size/2-dx*size/2)],
                    outline_width=scale//2)
    return image, scale


def make_piece_icon(piece):
    """Return the exact current native-size four-state strip for this spec."""
    identity = icon_identity(piece)
    routes = _icon_routes(piece)
    require(routes and all(len(route) >= 2 for route in routes), 'Standalone Highway icon needs complete route lines')
    diagram, scale = _diagram(routes, show_direction=piece['menu']['style'].startswith('ddrhw-y-') or
                              piece['menu']['style'].endswith('transition'))
    strip = Image.new('RGBA', (FRAME * len(STATES), FRAME))
    for number, state in enumerate(STATES):
        frame = diagram.copy()
        outline = {'selected': '#b2ddda', 'highlighted': '#ffffff'}.get(state)
        if outline:
            ImageDraw.Draw(frame).rounded_rectangle((scale, scale, 42*scale, 42*scale),
                radius=5*scale, outline=outline, width=2*scale)
        frame = frame.resize((FRAME, FRAME), Image.Resampling.LANCZOS)
        draw = ImageDraw.Draw(frame)
        if outline:
            draw.line((9, 2, 34, 2), fill=outline)
        bitmap_label(draw, 'SCP', 5, 5, '#b6ddd9')
        kind = identity['kind']
        bitmap_label(draw, kind, 39-(4*len(kind)-1), 5, '#86e2d8')
        bitmap_label(draw, FOOTER, 6, 35, '#e2f0f0')
        if state == 'locked':
            alpha = frame.getchannel('A')
            frame = ImageOps.grayscale(frame).convert('RGBA')
            frame.putalpha(alpha)
        strip.paste(frame, (FRAME*number, 0))
    output = BytesIO()
    strip.save(output, format='PNG', optimize=False)
    raw = output.getvalue()
    validate_piece_icon(raw)
    return raw


def validate_piece_icon(raw, *, expected=None):
    """Check native format and states, and optionally require exact artwork pixels."""
    require(isinstance(raw, bytes) and len(raw) >= 33 and
            raw.startswith(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR') and
            struct.unpack('>IIBBBBB', raw[16:29]) == (176, 44, 8, 6, 0, 0, 0),
            'Wrong Highway icon PNG format')
    with Image.open(BytesIO(raw)) as png:
        require(png.format == 'PNG' and png.mode == 'RGBA' and png.n_frames == 1
                and png.get_format_mimetype() == 'image/png', 'Highway icon must be a single RGBA PNG')
        png.verify()
    with Image.open(BytesIO(raw)) as png:
        pixels = png.tobytes()
        frames = [png.crop((index*FRAME, 0, (index+1)*FRAME, FRAME)) for index in range(len(STATES))]
    require(len({frame.tobytes() for frame in frames}) == len(STATES), 'Highway icon states must be distinct')
    require(all(frame.getpixel((x, y))[3] == 0 for frame in frames
                for x in (0, FRAME-1) for y in (0, FRAME-1)), 'Highway icon corners must remain transparent')
    locked, normal = (frame.tobytes() for frame in frames[:2])
    require(locked[0::4] == locked[1::4] == locked[2::4], 'Highway locked icon must be greyscale')
    require(any(a and (r != g or g != b) for r, g, b, a in zip(
        normal[0::4], normal[1::4], normal[2::4], normal[3::4])), 'Highway normal icon must retain colour')
    require(frames[2].getpixel((22, 2))[:3] == (178, 221, 218) and
            frames[3].getpixel((22, 2))[:3] == (255, 255, 255), 'Highway selection and highlight outlines differ')
    if expected is not None:
        with Image.open(BytesIO(expected)) as reference:
            require(reference.mode == 'RGBA' and reference.size == (176, 44)
                    and reference.tobytes() == pixels, 'Highway icon artwork pixels differ')


def write_piece_icons(root, *, output=None):
    """Render all registered Highway piece icons before replacing any target."""
    from scp.catalog import load_catalog
    root = Path(root).resolve()
    catalog = load_catalog(root)
    directory = Path(output) if output is not None else root/catalog['domains']['highway']['path']/'00_pieces'
    artwork = {piece['id']: make_piece_icon(piece) for piece in catalog['pieces']
               if piece['domain'] == 'highway' and piece['status'] != 'draft'}
    require(artwork, 'No registered Highway piece icons')
    for identifier, raw in artwork.items():
        target = directory/identifier/'icon.png'
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
    return tuple(artwork)


def main():
    from scp.paths import project_root
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=project_root())
    parser.add_argument('--output', type=Path, help='Isolated artwork output directory')
    args = parser.parse_args()
    print(f'Wrote {len(write_piece_icons(args.root, output=args.output))} standalone Highway icon strips')


if __name__ == '__main__':
    main()
