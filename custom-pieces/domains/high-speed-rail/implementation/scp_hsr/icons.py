"""Draw original SCP menu icons in SimCity 4's four-frame PNG format.

The artwork is procedural, using only Pillow drawing primitives and a tiny
embedded bitmap alphabet.  No downloaded icon or ImageGen output is used.
Native frame order: locked/greyscale, normal, selected, highlighted.
"""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import struct
import zlib
from functools import lru_cache

FRAME_SIZE = 44
STATES = ('locked', 'normal', 'selected', 'highlighted')
STYLES = ('diagonal-hsr', 'tram-hsr', 'cross-oo', 'cross-do', 'cross-dd',
          'rail-hsr-s-left', 'rail-hsr-s-right', 'rail-ghsr-s-left', 'rail-ghsr-s-right',
          'rail-hsr-crossover-right', 'rail-hsr-crossover-left',
          'rail-ghsr-crossover-right', 'rail-ghsr-crossover-left', 'rail-transition', 'rail-hsr-road-stack')
PNG_SIGNATURE = b'\x89PNG\r\n\x1a\n'
REVISED_STYLES = {
    'rail-hsr-scissors-revised': 'rail-hsr-scissors',
    'rail-ghsr-scissors-revised': 'rail-ghsr-scissors',
}
# A recipe being a single construction does not make it a complete junction.
# In particular the historical ``interchange-*`` family contains individual
# branches, crossings and ramps, and must keep the PART label.
PNP_STYLES = frozenset({
    'directional-hsr-t-smooth-at-grade',
    'directional-hsr-t-smooth-diagonal-at-grade',
})
# These exact new styles need explicit kinds because their names describe
# extracted modules rather than the historical recipe naming conventions.
# Keep this scoped to these original styles so existing pixels remain stable.
_MODULAR_KIND = {
    'hsr-component-blind-rise-quarter-turn': 'RMP',
    'hsr-component-modular-south-junction': 'JCT',
    'hsr-component-modular-paired-climb': 'RMP',
    'hsr-component-modular-crossing-core': 'XNG',
    'hsr-component-l2-paired-fan-compact-core': 'JCT',
}
# Each piece declares one of these stable procedural keys in menu.style.
# Selection IDs and folder names do not select or rename artwork styles.
_FOOTER_LETTER = {
    'A': ('010', '101', '101', '111', '101', '101', '101'),
    'C': ('111', '100', '100', '100', '100', '100', '111'),
    'D': ('110', '101', '101', '101', '101', '101', '110'),
    'G': ('111', '100', '100', '101', '101', '101', '111'),
    'H': ('101', '101', '101', '111', '101', '101', '101'),
    'I': ('111', '010', '010', '010', '010', '010', '111'),
    'J': ('001', '001', '001', '001', '101', '101', '111'),
    'L': ('100', '100', '100', '100', '100', '100', '111'),
    'M': ('101', '111', '111', '101', '101', '101', '101'),
    'N': ('101', '111', '111', '111', '111', '111', '101'),
    'O': ('111', '101', '101', '101', '101', '101', '111'),
    'P': ('110', '101', '101', '110', '100', '100', '100'),
    'R': ('110', '101', '101', '110', '101', '101', '101'),
    'S': ('111', '100', '100', '111', '001', '001', '111'),
    'T': ('111', '010', '010', '010', '010', '010', '010'),
    'V': ('101', '101', '101', '101', '101', '101', '010'),
    'W': ('101', '101', '101', '101', '111', '111', '101'),
    'X': ('101', '101', '101', '010', '101', '101', '101'),
}


def icon_identity(style: str) -> dict:
    """Give menu labels and artwork one deterministic category vocabulary.

    GSR is the compact icon abbreviation for GHSR. MIX identifies elevated
    HSR together with ground GHSR; TRAM identifies the rail/tram crossing.
    Layout assembly blueprints never become PNP merely by sharing a name.
    """
    category = 'pnp' if style in PNP_STYLES else 'part'
    if 'tram' in style:
        network = 'TRAM'
    elif style.startswith(('cross-', 'diagonal-hsr')) or style == 'rail-transition':
        network = 'MIX'
    elif 'ghsr' in style and ('-hsr-' in style or 'mixed' in style):
        network = 'MIX'
    elif 'ground' in style and any(word in style for word in ('over-', 'under-', 'grade-')):
        network = 'MIX'
    elif 'ghsr' in style or 'ground' in style:
        network = 'GSR'
    else:
        network = 'HSR'
    if style in _MODULAR_KIND:
        kind = _MODULAR_KIND[style]
    elif category == 'pnp':
        kind = 'T'
    elif style.startswith(('cross-', 'diagonal-hsr', 'tram-')) or '-over-' in style or '-under-' in style:
        kind = 'XNG'
    elif 'scissors' in style or 'crossover' in style:
        kind = 'SWI'
    elif 'adapter' in style:
        kind = 'ADP'
    elif 'ramp' in style or 'grade-' in style or style == 'rail-transition':
        kind = 'RMP'
    elif ('split' in style and 'merge' in style) or 'y-merge' in style or 'graded-y' in style:
        kind = 'JCT'
    elif 'split' in style or 'turnout' in style or 'diverge' in style:
        kind = 'SPL'
    elif 'merge' in style:
        kind = 'MRG'
    elif 'curve' in style or 'turn90' in style or '-s-' in style:
        kind = 'CRV'
    elif 'diagonal' in style:
        kind = 'DIA'
    else:
        kind = 'STR'
    return {'category': category, 'badge': 'PNP' if category == 'pnp' else 'PART',
            'network': network, 'palette': 'purple' if category == 'pnp' else 'teal',
            'kind': kind,
            'meaning': ('Complete one-click junction' if category == 'pnp'
                        else 'Individual building piece')}
_LETTER = {
    'S': ('11111', '10000', '10000', '11111', '00001', '00001', '11111'),
    'C': ('11111', '10000', '10000', '10000', '10000', '10000', '11111'),
    'P': ('11110', '10001', '10001', '11110', '10000', '10000', '10000'),
}


def assembly_icon_network(assembly_id):
    """Declare an assembly's network explicitly, including future mixed layouts."""
    networks = {'hsr-trumpet-straight-stem': 'HSR'}
    _require(assembly_id in networks, f'No declared assembly icon network: {assembly_id}')
    return networks[assembly_id]


def assembly_icon_routes(scene, pieces):
    """Place the authored reusable HSR routes for the complete menu silhouette.

    This is a source-derived menu illustration, rather than compiled-resource
    verification or an observed game result. The same complete routes feed the
    piece builder; the assembly supplies their actual translations and turns.
    """
    from .hsr_components_layout import component_routes

    by_id = {piece['id']: piece for piece in pieces}
    placements = scene.get('placements', scene.get('instances'))
    _require(isinstance(placements, list) and placements, 'Assembly icon needs placements')
    routes = []
    for instance in placements:
        piece = by_id[instance['piece_id']]
        degrees = instance.get('rotation_ccw_degrees', instance.get(
            'rotation_degrees_ccw', instance.get('rotation_degrees', 0)))
        _require(degrees in (0, 90, 180, 270), 'Assembly icon requires cardinal rotations')
        east, north = instance['origin_m']
        for points in component_routes(piece['recipe']).values():
            placed = []
            for x, y, height in points:
                for _ in range(degrees // 90):
                    x, y = -y, x
                placed.append((x + east, y + north, height))
            routes.append(placed)
    return routes


def _require(condition: bool, message: str):
    if not condition:
        raise ValueError(message)


def _chunk(kind: bytes, data: bytes) -> bytes:
    return struct.pack('>I', len(data)) + kind + data + struct.pack('>I', zlib.crc32(kind + data))


def _encode_rgba(width: int, height: int, pixels: bytes) -> bytes:
    _require(len(pixels) == width * height * 4, 'RGBA pixel count mismatch')
    rows = b''.join(b'\0' + pixels[y * width * 4:(y + 1) * width * 4] for y in range(height))
    return (PNG_SIGNATURE + _chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0)) +
            _chunk(b'IDAT', zlib.compress(rows, 9)) + _chunk(b'IEND', b''))


def _paeth(a: int, b: int, c: int) -> int:
    p = a + b - c
    pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
    return a if pa <= pb and pa <= pc else (b if pb <= pc else c)


def _decode_rgba(raw: bytes) -> tuple[int, int, bytes]:
    """Validate PNG structure/CRCs and decode noninterlaced 8-bit RGBA PNG."""
    _require(raw.startswith(PNG_SIGNATURE), 'Missing PNG signature')
    cursor, chunks, compressed = len(PNG_SIGNATURE), [], bytearray()
    width = height = None
    while cursor < len(raw):
        _require(cursor + 12 <= len(raw), 'Truncated PNG chunk')
        length = struct.unpack_from('>I', raw, cursor)[0]
        kind = raw[cursor + 4:cursor + 8]
        end = cursor + length + 12
        _require(end <= len(raw), 'PNG chunk extends past EOF')
        payload = raw[cursor + 8:end - 4]
        crc = struct.unpack_from('>I', raw, end - 4)[0]
        _require(zlib.crc32(kind + payload) == crc, f'Invalid {kind!r} PNG CRC')
        chunks.append(kind)
        if kind == b'IHDR':
            _require(len(chunks) == 1 and length == 13, 'Invalid PNG IHDR')
            width, height, depth, color, method, filtering, interlace = struct.unpack('>IIBBBBB', payload)
            _require((width, height) == (176, 44), 'SC4 menu icon must be 176 by 44 pixels')
            _require((depth, color, method, filtering, interlace) == (8, 6, 0, 0, 0),
                     'Expected noninterlaced 8-bit RGBA PNG')
        elif kind == b'IDAT':
            compressed.extend(payload)
        elif kind == b'IEND':
            _require(length == 0 and end == len(raw), 'Invalid PNG IEND or trailing bytes')
        else:
            _require(kind[0] & 0x20, 'Unsupported critical PNG chunk')
        cursor = end
    _require(chunks and chunks[0] == b'IHDR' and chunks[-1] == b'IEND' and b'IDAT' in chunks,
             'Incomplete PNG')
    stride = width * 4
    expected_size = (stride + 1) * height
    decoder = zlib.decompressobj()
    data = decoder.decompress(bytes(compressed), expected_size + 1)
    _require(len(data) == expected_size and decoder.eof and not decoder.unused_data,
             'Invalid PNG decompression length')
    previous, pixels = bytearray(stride), bytearray()
    for y in range(height):
        offset = y * (stride + 1)
        filtering = data[offset]
        _require(filtering in range(5), 'Unknown PNG row filter')
        row = bytearray(data[offset + 1:offset + 1 + stride])
        for x in range(stride):
            left, up, corner = (row[x - 4] if x >= 4 else 0), previous[x], (previous[x - 4] if x >= 4 else 0)
            prediction = (0, left, up, (left + up) // 2, _paeth(left, up, corner))[filtering]
            row[x] = (row[x] + prediction) & 255
        pixels.extend(row)
        previous = row
    return width, height, bytes(pixels)


def _frame(style: str, state: str):
    from PIL import Image, ImageDraw, ImageOps

    identity = icon_identity(style)
    badge_colour = ((169, 127, 226, 255) if identity['category'] == 'pnp'
                    else (52, 193, 181, 255))
    background = ((43, 30, 63, 255) if identity['category'] == 'pnp'
                  else (21, 42, 52, 255))
    revised = style in REVISED_STYLES
    style = REVISED_STYLES.get(style, style)

    scale = 4
    image = Image.new('RGBA', (FRAME_SIZE * scale, FRAME_SIZE * scale))
    draw = ImageDraw.Draw(image)

    def box(coords, fill, radius=0, outline=None, width=1):
        coords = tuple(round(v * scale) for v in coords)
        if radius:
            draw.rounded_rectangle(coords, radius=round(radius * scale), fill=fill,
                                   outline=outline, width=round(width * scale))
        else:
            draw.rectangle(coords, fill=fill, outline=outline, width=round(width * scale))

    def line(coords, fill, width):
        draw.line([tuple(round(v * scale) for v in p) for p in coords], fill=fill,
                  width=round(width * scale), joint='curve')

    def track(start, end, color):
        x0, y0 = start
        x1, y1 = end
        dx, dy = x1 - x0, y1 - y0
        length = (dx * dx + dy * dy) ** 0.5
        nx, ny = -dy / length, dx / length
        line([start, end], (10, 24, 32, 255), 7)
        for number in range(11):
            t = number / 10
            x, y = x0 + dx * t, y0 + dy * t
            line([(x - nx * 3., y - ny * 3.), (x + nx * 3., y + ny * 3.)], color, 1)
        for displacement in (-1.6, 1.6):
            line([(x0 + nx * displacement, y0 + ny * displacement),
                  (x1 + nx * displacement, y1 + ny * displacement)], (236, 240, 238, 255), .8)

    box((.5, .5, 43.5, 43.5), background, radius=5.5)
    for y in range(16, 43, 4):
        line([(3, y), (41, y)], (31, 55, 64, 255), .5)
    if style == 'rail-hsr-road-stack':
        # Side elevation communicates that the two straight services are stacked.
        line([(6, 39), (38, 39)], (139, 112, 86, 255), 5)
        line([(8, 38.5), (36, 38.5)], (245, 207, 103, 255), .65)
        line([(11, 27), (11, 36)], (151, 169, 174, 255), 2)
        line([(33, 27), (33, 36)], (151, 169, 174, 255), 2)
        track((6, 26), (38, 26), (151, 169, 174, 255))
    elif style == 'diagonal-hsr':
        track((5, 38), (37, 17), (236, 181, 76, 255))
        # An elevated deck runs vertically in front of the diagonal ground line.
        box((20, 16, 29, 42), (4, 14, 20, 170))
        box((17, 15, 25, 43), (151, 169, 174, 255))
        line([(17, 15), (17, 43)], (227, 236, 237, 255), .8)
        for x in (19.2, 22.8):
            line([(x, 15), (x, 43)], (39, 61, 70, 255), .8)
    elif style == 'tram-hsr':
        track((21, 16), (21, 43), (72, 208, 198, 255))
        box((2, 28, 43, 37), (4, 14, 20, 180))
        box((1, 25, 43, 33), (151, 169, 174, 255))
        line([(1, 25), (43, 25)], (227, 236, 237, 255), .8)
        for y in (27.2, 30.8):
            line([(1, y), (43, y)], (39, 61, 70, 255), .8)
    elif style.startswith('cross-'):
        lower = ((4, 29), (40, 29)) if style != 'cross-dd' else ((5, 39), (39, 17))
        track(*lower, (236, 181, 76, 255))
        upper = [(21, 17), (21, 43)] if style == 'cross-oo' else [(5, 18), (39, 42)]
        line([(x + 2, y + 2) for x, y in upper], (4, 14, 20, 180), 10)
        line(upper, (151, 169, 174, 255), 8)
        # Two bright rails distinguish the elevated line from the ground track.
        dx, dy = upper[1][0] - upper[0][0], upper[1][1] - upper[0][1]
        length = (dx * dx + dy * dy) ** .5
        for d in (-1.8, 1.8):
            line([(x - dy / length * d, y + dx / length * d) for x, y in upper],
                 (39, 61, 70, 255), .8)
    elif style.startswith(('interchange-', 'directional-', 'hsr-component-')):
        # Draw the registered piece's real track layout. Every menu item gets
        # its own silhouette, direction arrows and height colours, rather than
        # reusing a generic T icon for a differently shaped junction.
        recipe = style.replace('-', '_')
        if style.startswith('hsr-component-'):
            from .hsr_components_layout import component_layout
            layout = component_layout(recipe)
        elif style.startswith('directional-'):
            if recipe == 'directional_hsr_t_smooth_diagonal_at_grade':
                from .directional_diagonal_t import directional_layout
            else:
                from .directional_t import directional_layout
            layout = directional_layout(recipe)
        else:
            from .interchange_layouts import interchange_layout
            layout = interchange_layout(recipe)
        routes = []
        for (x, row), data in layout.items():
            for route in data['routes']:
                routes.append([(point[0] + 16*x, point[1] - 16*row, point[2])
                               for point in route['points']])
        xmin = min(p[0] for route in routes for p in route)
        xmax = max(p[0] for route in routes for p in route)
        ymin = min(p[1] for route in routes for p in route)
        ymax = max(p[1] for route in routes for p in route)
        factor = min(35/max(1, xmax-xmin), 23/max(1, ymax-ymin))
        def screen(point):
            return (22 + (point[0]-(xmin+xmax)/2)*factor,
                    29 - (point[1]-(ymin+ymax)/2)*factor)
        starts = {tuple(round(v, 5) for v in route[0]) for route in routes}
        for route in sorted(routes, key=lambda points: sum(p[2] for p in points)/len(points)):
            points = [screen(point) for point in route]
            height = sum(p[2] for p in route)/len(route)
            colour = ((221, 172, 88, 255) if height < 4 else
                      (147, 178, 190, 255) if height < 20 else
                      (164, 141, 228, 255) if height < 27 else (104, 219, 195, 255))
            line(points, (3, 16, 22, 255), 4)
            line(points, colour, 2.1)
            if tuple(round(v, 5) for v in route[-1]) not in starts:
                a, b = points[-2:]
                dx, dy = b[0]-a[0], b[1]-a[1]
                length = max(.0001, (dx*dx+dy*dy)**.5)
                dx, dy = dx/length, dy/length
                line([(b[0]-dx*3-dy*1.8, b[1]-dy*3+dx*1.8), b,
                      (b[0]-dx*3+dy*1.8, b[1]-dy*3-dx*1.8)],
                     (255, 239, 177, 255), 1)
        if 'wide' in style:
            line([(5, 39), (12, 39)], (255, 239, 177, 255), 1)
            line([(5, 37.5), (5, 40.5)], (255, 239, 177, 255), 1)
            line([(12, 37.5), (12, 40.5)], (255, 239, 177, 255), 1)
    elif style.startswith('rail-'):
        ground = style.startswith('rail-ghsr')
        base = (210, 171, 100, 255) if ground else (151, 169, 174, 255)

        def railway(points, color=base):
            line([(x + 1.5, y + 1.5) for x, y in points], (4, 14, 20, 180), 8)
            line(points, color, 6)
            for shift in (-1.5, 1.5):
                offset = []
                for i, (x, y) in enumerate(points):
                    a, b = points[max(0, i-1)], points[min(len(points)-1, i+1)]
                    dx, dy = b[0]-a[0], b[1]-a[1]
                    length = (dx*dx + dy*dy)**.5
                    offset.append((x-dy/length*shift, y+dx/length*shift))
                line(offset, (39, 61, 70, 255), .65)

        if '-s-' in style:
            points = [(5, 41), (10, 36), (15, 32), (23, 31), (30, 27), (38, 18)]
            if style.endswith('-right'):
                points = [(44-x, y) for x, y in points]
            railway(points)
        elif style == 'rail-transition':
            railway([(16, 18), (16, 25)], (151, 169, 174, 255))
            railway([(16, 25), (22, 34)], (177, 170, 143, 255))
            railway([(22, 34), (22, 43)], (210, 171, 100, 255))
            line([(29, 20), (29, 40)], (52, 193, 181, 255), 1.2)
            line([(26, 36), (29, 40), (32, 36)], (52, 193, 181, 255), 1.2)
        else:
            railway([(11, 18), (11, 43)])
            railway([(32, 18), (32, 43)])
            if style.endswith(('-right', '-scissors')):
                railway([(11, 40), (13, 35), (29, 26), (32, 20)])
            if style.endswith(('-left', '-scissors')):
                railway([(11, 20), (13, 26), (29, 35), (32, 40)])
    # Fit the existing route illustration into its own band without changing
    # its aspect ratio. Labels stay outside it, so neither long modules nor a
    # complete junction can obscure the PART/PNP distinction.
    illustration = image.crop((scale, 16 * scale, 43 * scale, 43 * scale))
    illustration = illustration.resize((round(42 * scale * 17 / 27), 17 * scale),
                                      Image.Resampling.LANCZOS)
    box((1, 14, 43, 43), background)
    image.alpha_composite(illustration, (round(22 * scale - illustration.width / 2), 14 * scale))
    if style == 'hsr-component-l2-paired-straight-recessed-web':
        # A schematic inset structural web distinguishes this profile while
        # retaining the exact paired track silhouette and STR classification.
        profile = [(31.5, 17.5), (39., 17.5), (39., 19.5), (37., 19.5),
                   (37., 25.5), (39., 25.5), (39., 27.5), (31.5, 27.5),
                   (31.5, 25.5), (33.5, 25.5), (33.5, 19.5), (31.5, 19.5),
                   (31.5, 17.5)]
        line(profile, (147, 178, 190, 255), .8)
    box((4, 3, 40, 13), badge_colour, radius=2)
    for number, letter in enumerate('SCP'):
        for y, row in enumerate(_LETTER[letter]):
            for x, pixel in enumerate(row):
                if pixel == '1':
                    box((6 + number * 6 + x, 5 + y, 6.95 + number * 6 + x, 5.95 + y),
                        (8, 38, 46, 255))
    if revised:
        box((33, 21, 40, 28), (8, 38, 46, 255), radius=2)
        line([(34, 24), (36, 26), (39, 22)], (133, 242, 186, 255), 1.1)
    box((3, 31, 41, 41), (9, 17, 26, 255), radius=1)
    line([(4, 31), (40, 31)], badge_colour, 1)
    # Reapply a rounded alpha mask after drawing clipped track ends.
    mask = Image.new('L', image.size)
    ImageDraw.Draw(mask).rounded_rectangle((scale // 2, scale // 2, 43.5 * scale, 43.5 * scale),
                                          radius=5.5 * scale, fill=255)
    image.putalpha(mask)
    border = ImageDraw.Draw(image)
    if state == 'selected':
        border.rounded_rectangle((1.5 * scale, 1.5 * scale, 42.5 * scale, 42.5 * scale),
                                 radius=4.5 * scale, outline=(178, 221, 218, 255), width=2 * scale)
    elif state == 'highlighted':
        border.rounded_rectangle((1.5 * scale, 1.5 * scale, 42.5 * scale, 42.5 * scale),
                                 radius=4.5 * scale, outline=(255, 255, 255, 255), width=3 * scale)
    else:
        border.rounded_rectangle((.5 * scale, .5 * scale, 43.5 * scale, 43.5 * scale),
                                 radius=5.5 * scale, outline=(5, 12, 15, 255), width=scale)
    image = image.resize((FRAME_SIZE, FRAME_SIZE), Image.Resampling.LANCZOS)
    # Draw these small glyphs on the FINAL 44 px frame. One-pixel strokes
    # must remain crisp rather than being blurred by the supersampling pass.
    label_draw = ImageDraw.Draw(image)
    # The highlighted outline is three pixels thick. Reserve an opaque text
    # rectangle inside it so its antialiased bottom edge cannot add strokes
    # to a category letter in the selected/highlighted states.
    label_draw.rectangle((5, 33, 38, 39), fill=(9, 17, 26, 255))

    def label(value, x, y, colour):
        for index, letter in enumerate(value):
            for row, pixels in enumerate(_FOOTER_LETTER[letter]):
                for column, on in enumerate(pixels):
                    if on == '1':
                        label_draw.point((x + index * 4 + column, y + row), fill=colour)

    label(identity['kind'], 38 - (len(identity['kind']) * 4 - 1), 5,
          (8, 28, 38, 255))
    text = identity['badge'] + ' ' + identity['network']
    text_width = sum(4 if letter != ' ' else 3 for letter in text) - 1
    x = (FRAME_SIZE - text_width) // 2
    for word in (identity['badge'], identity['network']):
        label(word, x, 33, (244, 249, 250, 255))
        x += len(word) * 4 + 3
    if state == 'locked':
        alpha = image.getchannel('A')
        image = ImageOps.grayscale(image).convert('RGBA')
        image.putalpha(alpha)
    return image


@lru_cache(maxsize=512)
def make_icon(style: str) -> bytes:
    """Return one deterministic native-format strip, with an SCP badge."""
    from PIL import Image
    if style.startswith('hsr-component-'):
        from .hsr_components_layout import RECIPES
        known = style.replace('-', '_') in RECIPES
    elif style.startswith('directional-'):
        if style == 'directional-hsr-t-smooth-diagonal-at-grade':
            from .directional_diagonal_t import RECIPES
        else:
            from .directional_t import RECIPES
        known = style.replace('-', '_') in RECIPES
    elif style.startswith('interchange-'):
        from .interchange_layouts import RECIPES
        known = style.replace('-', '_') in RECIPES
    else:
        known = style in STYLES or style in REVISED_STYLES
    _require(known, f'Unknown SCP icon style: {style}')
    strip = Image.new('RGBA', (FRAME_SIZE * len(STATES), FRAME_SIZE))
    for number, state in enumerate(STATES):
        strip.paste(_frame(style, state), (FRAME_SIZE * number, 0))
    raw = _encode_rgba(strip.width, strip.height, strip.tobytes())
    validate_icon(raw)
    return raw


def validate_icon(raw: bytes) -> dict:
    """Validate actual PNG pixels, state differences, and transparent corners."""
    width, height, pixels = _decode_rgba(raw)
    frames = []
    for number, _ in enumerate(STATES):
        frame = b''.join(pixels[(y * width + number * FRAME_SIZE) * 4:
                                (y * width + (number + 1) * FRAME_SIZE) * 4] for y in range(height))
        frames.append(frame)
        _require(frame[3] == 0 and frame[(FRAME_SIZE - 1) * 4 + 3] == 0,
                 'Icon corners must remain transparent')
        _require(sum(frame[offset + 3] == 255 for offset in range(0, len(frame), 4)) > 1200,
                 'Missing opaque icon artwork')
    _require(len(set(frames)) == 4, 'The four icon states must differ')
    _require(all(frames[0][i] == frames[0][i + 1] == frames[0][i + 2]
                 for i in range(0, len(frames[0]), 4)), 'First native icon frame must be greyscale')
    _require(any(frames[1][i] != frames[1][i + 1] for i in range(0, len(frames[1]), 4)),
             'Normal icon state unexpectedly has no color')
    return {'width': width, 'height': height, 'pixel_format': 'RGBA8', 'interlaced': False,
            'states': list(STATES), 'state_dimensions': [FRAME_SIZE, FRAME_SIZE],
            'transparent_corners': True, 'crc_valid': True,
            'sha256': hashlib.sha256(raw).hexdigest()}


def write_contact_sheet(path: Path, styles=None):
    from PIL import Image, ImageDraw
    from io import BytesIO
    styles = STYLES if styles is None else tuple(styles)
    sheet = Image.new('RGB', (632, 64 + len(styles) * 216), (239, 244, 244))
    draw = ImageDraw.Draw(sheet)
    draw.text((16, 12), "Simon's Custom Pieces | native menu icons", fill=(24, 43, 50))
    draw.text((16, 32), 'Actual 44 px frames', fill=(57, 76, 82))
    draw.text((224, 32), 'Normal: 4x nearest-neighbour', fill=(57, 76, 82))
    draw.text((432, 32), 'Locked: 4x', fill=(57, 76, 82))
    for index, style in enumerate(styles):
        y, name = 64 + index * 216, style.replace('-', ' ').title()
        draw.text((16, y), name, fill=(24, 43, 50))
        strip = Image.open(BytesIO(make_icon(style))).convert('RGBA')
        sheet.paste(strip, (16, y + 24), strip)
        for number, state in enumerate(STATES):
            short = ('lock', 'normal', 'select', 'hover')[number]
            draw.text((16 + number * FRAME_SIZE, y + 74), short, fill=(57, 76, 82))
        identity = icon_identity(style)
        draw.text((16, y + 100), identity['badge'] + ' / ' + identity['network'] +
                  ' / ' + identity['kind'], fill=(24, 43, 50))
        for frame_number, x in ((1, 224), (0, 432)):
            frame = strip.crop((frame_number * FRAME_SIZE, 0,
                                (frame_number + 1) * FRAME_SIZE, FRAME_SIZE))
            frame = frame.resize((176, 176), Image.Resampling.NEAREST)
            sheet.paste(frame, (x, y + 24), frame)
    path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(path)


def main():
    from scp.catalog import load_catalog
    from scp.paths import project_root
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=project_root())
    parser.add_argument('--output', type=Path, help='Optional isolated output directory for icon experiments')
    args = parser.parse_args()
    catalog = load_catalog(args.root)
    domain = Path(args.root)/catalog['domains']['high-speed-rail']['path']
    for piece in catalog['pieces']:
        if piece['domain'] != 'high-speed-rail':
            continue
        target = ((args.output/piece['id']/'icon.png') if args.output else
                  domain/'00_pieces'/piece['id']/'icon.png')
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(make_icon(piece['menu']['style']))
        print(target)
    sheet = (args.output/'icon-contact-sheet.png' if args.output else
             domain/'assets/figures/menu/icon-contact-sheet.png')
    write_contact_sheet(sheet)


if __name__ == '__main__':
    main()
