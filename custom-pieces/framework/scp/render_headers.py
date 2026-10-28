"""One caption contract for canonical piece views and connector overviews."""
from __future__ import annotations

import hashlib
import inspect
import math
import re

TITLE_INK = '#172b42'
SUBTITLE_INK = '#176eaf'
FACTS_INK = '#586a7e'


def piece_heading(source_title):
    """Add the piece label once without changing the registered menu name."""
    if not isinstance(source_title, str):
        raise ValueError('A piece render title needs a source-backed name')
    name = source_title.strip()
    prefix = 'Piece - '
    while name.startswith(prefix) or name == prefix.rstrip():
        name = name[len(prefix):].strip()
    if not name:
        raise ValueError('A piece render title needs a source-backed name')
    return prefix + name


def level_and_height(record):
    level = record.get('nominal_level')
    label = ('Level ' + level[1:] if isinstance(level, str) and level.lower().startswith('l')
             else level if isinstance(level, str) else 'Custom')
    return f"{label} ({record['path_height_m']:g} m)"


def piece_title(piece_id, records, source_name):
    """Use the same source-backed title in every view, without duplicate levels."""
    records = list(records)
    height_annotation = (r'\(\s*([+-]?(?:\d+(?:\.\d*)?|\.\d+)'
                         r'(?:[eE][+-]?\d+)?)\s*m\s*\)')
    canonical = ' — ' in source_name and re.search(height_annotation, source_name) is not None
    labels = sorted({level_and_height(record) for record in records})
    levels = {}
    for record in records:
        level = record.get('nominal_level')
        if isinstance(level, str) and level.lower().startswith('l'):
            levels.setdefault(level[1:], set()).add(level_and_height(record))
    consumed = set()
    def replace(match):
        choices = levels.get(match.group(1), set())
        if len(choices) == 1:
            label = next(iter(choices)); consumed.add(label)
            return label
        return match.group(0)
    # A source name can use either L2 or Level 2. Replace an existing height
    # annotation as well, so refreshed measured facts cannot leave a stale
    # height in the display title. The registered menu name remains separate.
    level_token = (r'\b(?:Level\s+|L)(\d+)\b'
                   r'(?:\s*\(\s*[+-]?(?:\d+(?:\.\d*)?|\.\d+)'
                   r'(?:[eE][+-]?\d+)?\s*m\s*\))?')
    title = re.sub(level_token, replace, source_name, flags=re.IGNORECASE)
    # Canonical names already distinguish Custom, Ground, and
    # each service. A measured 0 m pedestrian group must not append an extra
    # Custom label to an explicitly named Road Level 0 interface, for example.
    # Only consume heights actually written in the source-backed title; keep
    # any unrepresented verified height visible rather than guessing it away.
    annotated_heights = ({float(match.group(1)) for match in re.finditer(height_annotation, title)}
                         if canonical else set())
    represented = {level_and_height(record) for record in records
                   if record['path_height_m'] in annotated_heights}
    remaining = [label for label in labels
                 if label not in consumed and label not in title and label not in represented]
    return piece_heading(title + (' — ' + ' / '.join(remaining) if remaining else ''))


def title_records(resolved):
    """Extract only verified level/height facts needed by the common title."""
    records = []
    for group in resolved['groups']:
        heights = {member['endpoint_m'][2] for member in group['members']}
        if len(heights) != 1:
            raise ValueError('A title service group needs one measured height')
        records.append({'id': group['id'], 'nominal_level': (group.get('profile') or {}).get('nominal_level'),
                        'path_height_m': next(iter(heights))})
    return records


def view_caption(view_role='angled', azimuth=45., elevation=31.):
    """Name the actual camera; S3D +Z points south in world coordinates."""
    purposes = {'angled': 'Clean view', 'top': 'Clean view', 'connection-overview': 'Connection overview'}
    if view_role not in purposes:
        raise ValueError('A piece view purpose must be angled, top, or connection-overview')
    if not all(math.isfinite(value) for value in (azimuth, elevation)):
        raise ValueError('View angles must be finite')
    if abs(elevation - 90.) < 1e-8:
        direction = 'Top view, north up' if abs(azimuth % 360) < 1e-8 else f'Top view, camera azimuth {azimuth:g}°'
    else:
        compass = ('South', 'Southeast', 'East', 'Northeast', 'North', 'Northwest', 'West', 'Southwest')
        index = round((azimuth % 360) / 45) % 8
        direction = (compass[index] + ' view' if abs((azimuth-index*45+180)%360-180) < 1e-8
                     else f'Oblique view, camera azimuth {azimuth:g}°')
    return f'{purposes[view_role]} | {direction} | Authored orientation: 0°'


def grid_caption(local):
    reference = local['construction_reference']
    x, y = reference['local_tiles_en']
    location = f' / Piece reference: X{x:g}, Y{y:g}' if reference['caption_visible'] else ''
    return f'Independent local X/Y grid{location} / 1 tile = 16 m / Labels mark tile centres'


def _fit_font(draw, text, font_factory, size, width, bold):
    face = font_factory(size, bold)
    while draw.textlength(text, font=face) > width and size > 12:
        size -= 1; face = font_factory(size, bold)
    if draw.textlength(text, font=face) > width:
        raise ValueError('A render header exceeds the available width')
    return face, size


def draw_header(draw, captions, width, font_factory, *, margin=48, top=24):
    """Draw three consistently coloured rows; return exact placement evidence."""
    if len(captions) != 3:
        raise ValueError('A piece render header has exactly three rows')
    if piece_heading(captions[0]) != captions[0]:
        raise ValueError('A piece render header title needs exactly one Piece - prefix')
    if not captions[1].startswith(('Clean view | ', 'Connection overview | ')):
        raise ValueError('A piece render header second row must lead with its view purpose')
    scale = width / 2000
    y = top; rows = []
    for text, size, bold, colour in zip(captions, (44, 28, 27), (True, False, False),
                                       (TITLE_INK, SUBTITLE_INK, FACTS_INK)):
        face, pixels = _fit_font(draw, text, font_factory, max(12, round(size * scale)),
                                 width - 2 * margin, bold)
        draw.text((margin, y), text, font=face, fill=colour)
        bounds = draw.textbbox((margin, y), text, font=face)
        rows.append({'text': text, 'colour': colour, 'font_pixels': pixels, 'bold': bold,
                     'position': [margin, y], 'bounds': list(bounds)})
        y += round((54 if bold else 44) * scale)
    return {'captions': list(captions), 'rows': rows, 'bottom': max(y, rows[-1]['bounds'][3]) + round(16*scale),
            'title_occurrences': 1, 'scale_caption_in_header_only': True}


def header_settings():
    source = '\n'.join(inspect.getsource(function) for function in
                       (piece_heading, level_and_height, piece_title, title_records, view_caption, grid_caption, _fit_font, draw_header))
    return {'source_sha256': hashlib.sha256(source.encode()).hexdigest(),
            'row_colours': [TITLE_INK, SUBTITLE_INK, FACTS_INK],
            'rows': ['Piece - source-backed piece title', 'view purpose, camera, and authored orientation', 'local grid and scale'],
            'duplicate_grid_footer_visible': False}
