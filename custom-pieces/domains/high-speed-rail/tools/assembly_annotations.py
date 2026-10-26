"""Readable instance names for interchange model renders and placement plans.

These overlays never change the compiled model. An instance badge may move a
few pixels to remain legible; its small connector always ends at the exact
projected source-model anchor, and both points are recorded in the evidence.
"""
from __future__ import annotations

import hashlib
import colorsys
from collections import defaultdict
import math
import re

from PIL import ImageDraw

from scp.preview import font


# Fixed across camera views and independent of the order of the source list.
INSTANCE_COLOURS = (
    '#176b89', '#ad551d', '#7860ab', '#1b8061', '#ae3e6f',
    '#6a7223', '#2c67af', '#9a542b', '#80669b', '#007b7b',
)


def colour_for_label(label):
    """Legacy standalone fallback; layouts use colour_assignment_for_sources."""
    text = str(label)
    match = re.fullmatch(r'P(\d+)', text)
    number = int(match.group(1)) - 1 if match else int.from_bytes(
        hashlib.sha256(text.encode('utf-8')).digest()[:4], 'big')
    return INSTANCE_COLOURS[number % len(INSTANCE_COLOURS)]


MIN_ADJACENT_DELTA_E = 26.
MIN_OUTLINE_DELTA_E = 35.
MIN_TEXT_CONTRAST = 4.5
OWNERSHIP_TEXT = '#10212d'
OWNERSHIP_FILL_FRACTION = .60
INTERNAL_GRID_WIDTH = 1
OWNER_BOUNDARY_WIDTH = 6
OWNER_BOUNDARY_HALO_WIDTH = 10


def _rgb(colour):
    from PIL import ImageColor
    return ImageColor.getrgb(colour)


def _linear_rgb(colour):
    return tuple(value/12.92 if value <= .04045 else ((value+.055)/1.055)**2.4
                 for value in (component/255. for component in _rgb(colour)))


def _lab(colour):
    r, g, b = _linear_rgb(colour)
    xyz = ((.4124564*r+.3575761*g+.1804375*b)/.95047,
           .2126729*r+.7151522*g+.0721750*b,
           (.0193339*r+.1191920*g+.9503041*b)/1.08883)
    f = tuple(value**(1./3.) if value > (6./29.)**3
              else value/(3.*(6./29.)**2)+4./29. for value in xyz)
    return 116.*f[1]-16., 500.*(f[0]-f[1]), 200.*(f[1]-f[2])


def colour_distance(first, second):
    """CIELAB Delta E 1976 under the sRGB D65 white point."""
    return math.dist(_lab(first), _lab(second))


def contrast_ratio(first, second):
    def luminance(value):
        r, g, b = _linear_rgb(value)
        return .2126*r+.7152*g+.0722*b
    a, b = sorted((luminance(first), luminance(second)))
    return (b+.05)/(a+.05)


def ownership_fill(colour):
    components = [round(OWNERSHIP_FILL_FRACTION*value+
                        (1.-OWNERSHIP_FILL_FRACTION)*255) for value in _rgb(colour)]
    return '#'+''.join(f'{value:02x}' for value in components)


def _ownership(sources):
    labels, owners = set(), {}
    for source in sources:
        label = source.get('label')
        if not isinstance(label, str) or not label or label in labels:
            raise ValueError('Every colour source needs a unique nonempty label')
        labels.add(label)
        for cell in source.get('occupied_world_cells', []):
            if len(cell) != 2 or not all(math.isfinite(float(value)) for value in cell):
                raise ValueError(f'{label} needs finite occupied city cells')
            position = tuple(round(float(value)/16.) for value in cell)
            if any(abs(float(value)-16.*index) > 1e-6 for value, index in zip(cell, position)):
                raise ValueError(f'{label} occupied cells must follow the 16 m city grid')
            if position in owners:
                raise ValueError(f'Occupied city cell has more than one owner: {cell}')
            owners[position] = label
    return sorted(labels), owners


def ownership_adjacency(sources):
    """Return physical owner contacts, including shared city-grid corners."""
    _, owners = _ownership(sources)
    contacts = defaultdict(set)
    for (x, y), label in owners.items():
        for dx, dy in ((-1, -1), (-1, 0), (-1, 1), (0, -1),
                       (0, 1), (1, -1), (1, 0), (1, 1)):
            other = owners.get((x+dx, y+dy))
            if other is not None and other != label:
                contacts[tuple(sorted((label, other)))].add('side' if dx*dy == 0 else 'corner')
    return [{'labels': list(pair), 'contact': sorted(kinds)}
            for pair, kinds in sorted(contacts.items())]


def ownership_boundary_segments(sources):
    """Classify each real tile edge once, preserving thin intra-piece grids."""
    _, owners = _ownership(sources)
    edges = defaultdict(list)
    for (x, y), owner in owners.items():
        x, y = 16*x, 16*y
        corners = ((x-8, y-8), (x+8, y-8), (x+8, y+8), (x-8, y+8))
        for first, last in zip(corners, corners[1:]+corners[:1]):
            edges[tuple(sorted((first, last)))].append(owner)
    result = []
    for endpoints, labels in sorted(edges.items()):
        distinct = sorted(set(labels))
        kind = ('outer' if len(labels) == 1 else
                'internal-grid' if len(distinct) == 1 else 'between-owners')
        result.append({'world_endpoints_m': [list(point) for point in endpoints],
                       'owners': distinct, 'kind': kind,
                       'width_pixels': INTERNAL_GRID_WIDTH if kind == 'internal-grid'
                                       else OWNER_BOUNDARY_WIDTH})
    return result


def audit_colour_assignment(sources, palette):
    sources = list(sources)
    labels, _ = _ownership(sources)
    if set(palette) != set(labels):
        raise ValueError('Colour palette must cover every instance label exactly')
    fills = {label: ownership_fill(palette[label]) for label in labels}
    contacts = ownership_adjacency(sources)
    for contact in contacts:
        a, b = contact['labels']
        contact['fill_delta_e_76'] = colour_distance(fills[a], fills[b])
        contact['outline_delta_e_76'] = colour_distance(palette[a], palette[b])
        if contact['fill_delta_e_76'] < MIN_ADJACENT_DELTA_E or contact['outline_delta_e_76'] < MIN_OUTLINE_DELTA_E:
            raise ValueError(f'Adjacent owners {a} and {b} have insufficient colour separation')
    contrasts = {label: {'badge_white_text': contrast_ratio(palette[label], '#ffffff'),
                         'ownership_dark_text': contrast_ratio(fills[label], OWNERSHIP_TEXT)}
                 for label in labels}
    if any(min(values.values()) < MIN_TEXT_CONTRAST for values in contrasts.values()):
        raise ValueError('Instance colours have insufficient text contrast')
    return {'schema_version': 1,
            'algorithm': 'deterministic saturation-degree graph colouring; labels identify instances',
            'palette': {label: palette[label] for label in labels}, 'ownership_fill_palette': fills,
            'ownership_text_colour': OWNERSHIP_TEXT,
            'fill_fraction_of_source_colour': OWNERSHIP_FILL_FRACTION,
            'adjacency': contacts, 'adjacency_includes_corner_contacts': True,
            'minimum_required_fill_delta_e_76': MIN_ADJACENT_DELTA_E,
            'minimum_required_outline_delta_e_76': MIN_OUTLINE_DELTA_E,
            'minimum_measured_fill_delta_e_76': min((c['fill_delta_e_76'] for c in contacts), default=None),
            'minimum_measured_outline_delta_e_76': min((c['outline_delta_e_76'] for c in contacts), default=None),
            'minimum_text_contrast_ratio': MIN_TEXT_CONTRAST, 'text_contrasts': contrasts,
            'unique_colours_used': len(set(palette.values())),
            'nonadjacent_colour_reuse_permitted': True}


def colour_assignment_for_sources(sources):
    sources = list(sources)
    labels, _ = _ownership(sources)
    neighbours = {label: set() for label in labels}
    for contact in ownership_adjacency(sources):
        a, b = contact['labels']
        neighbours[a].add(b)
        neighbours[b].add(a)
    preferred = ('#0072b2', '#a33a00', '#6e3a8a', '#007b58', '#a52a61', '#667000')
    generated = []
    for lightness in (.31, .39, .47):
        for saturation in (.70, .95):
            for hue in range(0, 360, 10):
                values = colorsys.hls_to_rgb(hue/360., lightness, saturation)
                generated.append('#'+''.join(f'{round(value*255):02x}' for value in values))
    candidates = list(dict.fromkeys((*preferred, *generated)))
    candidates = [colour for colour in candidates
                  if contrast_ratio(colour, '#ffffff') >= MIN_TEXT_CONTRAST and
                  contrast_ratio(ownership_fill(colour), OWNERSHIP_TEXT) >= MIN_TEXT_CONTRAST]
    fills = {colour: ownership_fill(colour) for colour in candidates}
    palette, usage = {}, defaultdict(int)
    while len(palette) < len(labels):
        label = min((value for value in labels if value not in palette), key=lambda value: (
            -len({palette[n] for n in neighbours[value] if n in palette}),
            -len(neighbours[value]), value))
        used_neighbours = [palette[n] for n in sorted(neighbours[label]) if n in palette]
        possible = []
        for index, colour in enumerate(candidates):
            fill_distance = min((colour_distance(fills[colour], fills[other])
                                 for other in used_neighbours), default=200.)
            outline_distance = min((colour_distance(colour, other)
                                    for other in used_neighbours), default=200.)
            if fill_distance < MIN_ADJACENT_DELTA_E or outline_distance < MIN_OUTLINE_DELTA_E:
                continue
            global_distance = min((colour_distance(fills[colour], fills[other])
                                   for other in palette.values()), default=200.)
            possible.append(((usage[colour] == 0, fill_distance, global_distance,
                              outline_distance, -usage[colour], -index), colour))
        if not possible:
            raise ValueError(f'Cannot assign sufficiently distinct colours around {label}')
        colour = max(possible)[1]
        palette[label] = colour
        usage[colour] += 1
    return audit_colour_assignment(sources, palette)


def palette_for_sources(sources):
    return colour_assignment_for_sources(sources)['palette']


def _box_overlaps(first, second, padding=0):
    return not (first[2] + padding <= second[0]
                or second[2] + padding <= first[0]
                or first[3] + padding <= second[1]
                or second[3] + padding <= first[1])


def _text_width(draw, text, face):
    box = draw.textbbox((0, 0), text, font=face)
    return box[2] - box[0]


def _wrapped_lines(draw, text, face, width):
    """Wrap complete names without ellipses or omitted words."""
    lines = []
    line = ''
    for word in text.split():
        candidate = f'{line} {word}' if line else word
        if _text_width(draw, candidate, face) <= width:
            line = candidate
            continue
        if line:
            lines.append(line)
            line = ''
        # A long identifier must wrap too; never clip it to the panel edge.
        while word and _text_width(draw, word, face) > width:
            cut = 1
            while cut < len(word) and _text_width(draw, word[:cut + 1], face) <= width:
                cut += 1
            lines.append(word[:cut])
            word = word[cut:]
        line = word
    if line:
        lines.append(line)
    return lines or ['']


def _finite_pair(value, label, unit='metres'):
    if len(value) != 2:
        raise ValueError(f'{label} needs east and north {unit}')
    result = [float(number) for number in value]
    if not all(math.isfinite(number) for number in result):
        raise ValueError(f'{label} needs finite coordinates')
    return result


def _tile_label(value):
    tiles = float(value)
    return f'{tiles:.0f}' if tiles.is_integer() else f'{tiles:.3f}'.rstrip('0').rstrip('.')


def _badge_box(center, width, height):
    x, y = center
    return [x - width / 2, y - height / 2,
            x + width / 2, y + height / 2]


def _place_badge(anchor, width, height, occupied, bounds, side):
    """Find a deterministic nearby badge position distinct from other badges."""
    west, north, east, south = bounds
    # Try the card side first. The larger rings handle the four neighbouring
    # short connector pieces, whose anchors nearly coincide in oblique views.
    preferred = math.pi if side == 'left' else 0.
    for radius in (36, 66, 96, 126, 156, 192, 240, 300, 380):
        for turn in (0, -1, 1, -2, 2, -3, 3, 4):
            angle = preferred + turn * math.pi / 4
            center = [anchor[0] + radius * math.cos(angle),
                      anchor[1] + radius * math.sin(angle)]
            box = _badge_box(center, width, height)
            if box[0] < west or box[1] < north or box[2] > east or box[3] > south:
                continue
            if not any(_box_overlaps(box, other, padding=8) for other in occupied):
                return center, box
    raise ValueError('Cannot place nonoverlapping instance badges in the model viewport')


def draw_piece_callouts(canvas, camera, sources, *, view_offset=(0, 0),
                        panel_width=570, header_y=162, footer_y=None,
                        colour_assignment=None):
    """Draw exact menu names and source anchors on a full assembly image.

    Reserve ``panel_width`` pixels on each side of the full canvas before
    framing the model. ``camera`` describes only that central model viewport;
    ``view_offset`` is its upper-left pixel on ``canvas``. Every source needs
    ``label``, ``menu_name``, ``piece_id``, ``origin_m`` and a real source-model
    ``label_anchor_world_m=(east, north, height)``. All returned values can be
    serialized directly to JSON. There are no implicit origin/anchor fallbacks.
    Optional ``display_origin_tiles_en=(east, north)`` supplies nonnegative
    construction-origin coordinates in the review grid, without translating
    the physical geometry or its authoring origin. Generic callers that omit
    it retain authoring coordinates divided by 16 as their display coordinates.
    """
    sources = list(sources)
    if not sources:
        return {'schema_version': 1, 'instances': [], 'palette': {},
                'geometry_changed': False}
    colours = (colour_assignment_for_sources(sources) if colour_assignment is None else
               audit_colour_assignment(sources, colour_assignment['palette']))
    width, height = canvas.size
    footer_y = height - 108 if footer_y is None else float(footer_y)
    header_y = float(header_y)
    panel_width = float(panel_width)
    offset_x, offset_y = _finite_pair(view_offset, 'view_offset')
    if (panel_width < 220 or width <= 2 * panel_width + 100
            or footer_y <= header_y + 120):
        raise ValueError('Callouts need two reserved side panels and a positive-height label area')
    draw = ImageDraw.Draw(canvas)
    labels = set()
    prepared = []
    for source in sources:
        label, name = source.get('label'), source.get('menu_name')
        if not isinstance(label, str) or not label or label in labels:
            raise ValueError('Every callout needs a unique nonempty label')
        labels.add(label)
        if not isinstance(name, str) or not name.strip():
            raise ValueError(f'{label} needs its exact nonempty menu_name')
        if not isinstance(source.get('piece_id'), str) or not source['piece_id']:
            raise ValueError(f'{label} needs its exact piece_id')
        origin = _finite_pair(source['origin_m'], f'{label} origin_m')
        if 'display_origin_tiles_en' in source:
            display_origin = _finite_pair(source['display_origin_tiles_en'],
                                          f'{label} display_origin_tiles_en', 'tiles')
            if any(number < 0 for number in display_origin):
                raise ValueError(f'{label} display_origin_tiles_en needs nonnegative coordinates')
            display_origin_basis = 'explicit display_origin_tiles_en from source'
        else:
            display_origin = [number / 16 for number in origin]
            display_origin_basis = 'authoring origin_m divided by 16; no display-grid translation'
        anchor = [float(number) for number in source['label_anchor_world_m']]
        if len(anchor) != 3 or not all(math.isfinite(number) for number in anchor):
            raise ValueError(f'{label} needs a finite three-dimensional model anchor')
        rotation = float(source.get('rotation_ccw_degrees', 0))
        if not math.isfinite(rotation):
            raise ValueError(f'{label} needs a finite rotation')
        projected = camera.project_world(*anchor)
        point = [float(projected[0]) + offset_x, float(projected[1]) + offset_y]
        if not all(math.isfinite(number) for number in point):
            raise ValueError(f'{label} projected anchor is not finite')
        prepared.append({'source': source, 'label': label, 'menu_name': name,
                         'piece_id': source['piece_id'], 'origin_m': origin,
                         'display_origin_tiles_en': display_origin,
                         'display_origin_basis': display_origin_basis,
                         'rotation_ccw_degrees': rotation,
                         'anchor_world_m': anchor, 'source_anchor_pixel': point,
                         'colour': colours['palette'][label]})
    # Balance the number of cards, then sort each side by height. This ordering
    # remains deterministic when identical source models share a camera row.
    ordered = sorted(prepared, key=lambda item: (item['source_anchor_pixel'][0], item['label']))
    split = (len(ordered) + 1) // 2
    sides = {'left': ordered[:split], 'right': ordered[split:]}
    name_size = 22
    # Names stay at least 18px. Fail instead of silently truncating a name if
    # an unusually large scene cannot fit the explicit two-panel arrangement.
    card_gap = 12
    inset = 24
    card_width = panel_width - 2 * inset
    while name_size >= 18:
        face = font(name_size)
        heading_face = font(name_size + 2, True)
        detail_face = font(name_size - 1)
        line_height = name_size + 8
        for item in prepared:
            item['name_lines'] = _wrapped_lines(draw, item['menu_name'], face, card_width - 40)
            item['card_height'] = 30 + (name_size + 7) + len(item['name_lines']) * line_height + 2 * (name_size + 5)
        if all(sum(item['card_height'] for item in items) + max(0, len(items) - 1) * card_gap
               <= footer_y - header_y for items in sides.values()):
            break
        name_size -= 1
    if name_size < 18:
        raise ValueError('Full menu names do not fit at the minimum readable callout font size')
    occupied_badges = []
    rendered = []
    badge_face = font(name_size + 1, True)
    viewport_bounds = [max(panel_width + 8, offset_x + 6), max(header_y + 6, offset_y + 6),
                       min(width - panel_width - 8, offset_x + camera.width - 6),
                       min(footer_y - 6, offset_y + camera.height - 6)]
    if viewport_bounds[2] <= viewport_bounds[0] or viewport_bounds[3] <= viewport_bounds[1]:
        raise ValueError('The camera viewport does not fit between the callout panels')
    for side, items in sides.items():
        items.sort(key=lambda item: (item['source_anchor_pixel'][1], item['label']))
        total_height = sum(item['card_height'] for item in items)
        gap = max(card_gap, (footer_y - header_y - total_height) / max(1, len(items) - 1)) if len(items) > 1 else 0
        top = header_y
        for item in items:
            left = inset if side == 'left' else width - panel_width + inset
            box = [left, top, left + card_width, top + item['card_height']]
            badge_width = _text_width(draw, item['label'], badge_face) + 18
            badge_height = name_size + 15
            badge_center, badge_box = _place_badge(item['source_anchor_pixel'], badge_width,
                                                  badge_height, occupied_badges,
                                                  viewport_bounds, side)
            occupied_badges.append(badge_box)
            card_point = [box[2] if side == 'left' else box[0], (box[1] + box[3]) / 2]
            elbow_x = panel_width - 10 if side == 'left' else width - panel_width + 10
            leader = [card_point, [elbow_x, card_point[1]], badge_center,
                      item['source_anchor_pixel']]
            # A light halo keeps thin leaders legible against textured rails.
            draw.line([tuple(point) for point in leader], fill='#f7f9fb', width=8)
            draw.line([tuple(point) for point in leader], fill=item['colour'], width=4)
            ax, ay = item['source_anchor_pixel']
            draw.ellipse((ax - 4, ay - 4, ax + 4, ay + 4), fill='white', outline=item['colour'], width=3)
            item.update(side=side, card_bbox=box, badge_bbox=badge_box,
                        badge_center_pixel=badge_center, leader_points=leader,
                        badge_displacement_pixels=math.hypot(badge_center[0] - ax, badge_center[1] - ay))
            rendered.append(item)
            top = box[3] + gap
    # All lines are beneath all badges/cards, keeping each written label clear.
    for item in rendered:
        color, box = item['colour'], item['card_bbox']
        draw.rounded_rectangle(tuple(box), radius=10, fill='#ffffff', outline='#c5d0d6', width=2)
        draw.rounded_rectangle((box[0], box[1], box[0] + 7, box[3]), radius=3, fill=color)
        cursor_y = box[1] + 13
        draw.text((box[0] + 20, cursor_y), item['label'], fill=color, font=heading_face)
        cursor_y += name_size + 17
        for line in item['name_lines']:
            draw.text((box[0] + 20, cursor_y), line, fill='#172b42', font=face)
            cursor_y += line_height
        origin = item['display_origin_tiles_en']
        detail = f'Position X{_tile_label(origin[0])}, Y{_tile_label(origin[1])} tiles'
        item['position_label'] = detail
        draw.text((box[0] + 20, cursor_y + 2), detail, fill='#455b6c', font=detail_face)
        rotation = f'{item["rotation_ccw_degrees"]:g}'
        draw.text((box[0] + 20, cursor_y + name_size + 7), f'Rotation {rotation}° counterclockwise',
                  fill='#455b6c', font=detail_face)
        badge = item['badge_bbox']
        draw.rounded_rectangle(tuple(badge), radius=6, fill=color, outline='#ffffff', width=2)
        draw.text(tuple(item['badge_center_pixel']), item['label'], fill='#ffffff', font=badge_face, anchor='mm')
    evidence = []
    for item in sorted(rendered, key=lambda value: value['label']):
        evidence.append({key: value for key, value in item.items()
                         if key not in ('source', 'card_height')})
    return {'schema_version': 1, 'instances': evidence,
            'palette': colours['palette'], 'colour_assignment': colours,
            'leader_width_pixels': 4, 'leader_halo_width_pixels': 8,
            'name_font_pixels': name_size,
            'detail_font_pixels': name_size - 1,
            'view_offset': [offset_x, offset_y], 'panel_width': panel_width,
            'origin_meaning': 'origin_m is the normalized construction origin in authoring world metres; not an inferred mouse click anchor',
            'display_origin_meaning': 'display_origin_tiles_en locates that same construction origin in the review grid; explicit source coordinates use its southwest tile-centre origin, with no physical geometry translation',
            'anchor_meaning': 'exact projected source-model point; displaced badge joined by leader',
            'geometry_changed': False}
