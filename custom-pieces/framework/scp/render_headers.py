"""One caption contract for canonical piece views and connector overviews."""
from __future__ import annotations

import hashlib
import inspect
import math
import re

TITLE_INK = '#172b42'
SUBTITLE_INK = '#176eaf'
FACTS_INK = '#586a7e'


def level_and_height(record):
    level = record.get('nominal_level')
    label = ('Level ' + level[1:] if isinstance(level, str) and level.lower().startswith('l')
             else level if isinstance(level, str) else 'Custom')
    return f"{label} ({record['path_height_m']:g} m)"


def piece_title(piece_id, records, source_name):
    """Use the same source-backed title in every view, without duplicate levels."""
    records = list(records)
    by_id = {record['id']: record for record in records}
    if piece_id == 'hsr-component-tight-paired-curve90-l4-to-mid':
        return ('HSR Tight Two-Track Corner — ' + level_and_height(by_id['curve-end-a'])
                + ' to ' + level_and_height(by_id['curve-end-b']))
    if piece_id == 'hsr-component-modular-crossing-core':
        return ('HSR Modular One-Tile Crossing — ' + level_and_height(by_id['upper-end-a'])
                + ' over ' + level_and_height(by_id['lower-end-a']))
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
    remaining = [label for label in labels if label not in consumed and label not in title]
    return title + (' — ' + ' / '.join(remaining) if remaining else '')


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
    if not all(math.isfinite(value) for value in (azimuth, elevation)):
        raise ValueError('View angles must be finite')
    if abs(elevation - 90.) < 1e-8:
        direction = 'Top view, north up' if abs(azimuth % 360) < 1e-8 else f'Top view, camera azimuth {azimuth:g}°'
    else:
        compass = ('South', 'Southeast', 'East', 'Northeast', 'North', 'Northwest', 'West', 'Southwest')
        index = round((azimuth % 360) / 45) % 8
        direction = (compass[index] + ' view' if abs((azimuth-index*45+180)%360-180) < 1e-8
                     else f'Oblique view, camera azimuth {azimuth:g}°')
    role = ' / Connection overview' if view_role == 'connection-overview' else ''
    return f'Reusable piece / {direction}{role} / Authored orientation: 0°'


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
                       (level_and_height, piece_title, title_records, view_caption, grid_caption, _fit_font, draw_header))
    return {'source_sha256': hashlib.sha256(source.encode()).hexdigest(),
            'row_colours': [TITLE_INK, SUBTITLE_INK, FACTS_INK],
            'rows': ['source-backed piece title', 'view and authored orientation', 'local grid and scale'],
            'duplicate_grid_footer_visible': False}
