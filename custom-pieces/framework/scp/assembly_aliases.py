"""Add independent assembly selection states that reuse canonical construction resources."""
from __future__ import annotations

import hashlib
import re

from . import piece_menu_families
from .dbpf import require
from .rul0 import MARKER, ORDERING_END, _active_lines, _ring, ordering_span


SECTION = re.compile(rb'(?mi)^[ \t]*\[HighwayIntersectionInfo_0x([0-9a-f]{1,8})\]'
                     rb'[ \t]*(?:;[^\r\n]*)?(?=\r?$)')
COPY_FROM = re.compile(rb'(?mi)^[ \t]*CopyFrom[ \t]*=[ \t]*((?:0x)?[0-9a-f]{1,8})'
                       rb'(?=[ \t]*(?:;[^\r\n]*)?\r?$)')
STATE_STEP = 0x10000


def _states(root):
    return tuple(root + turn * STATE_STEP for turn in range(8))


def _rows(raw):
    rows = []
    for _, _, line in _active_lines(raw):
        if re.match(rb'(?:RotationRing|AddTypes)\s*=', line, re.I):
            normalized = re.sub(rb'^AddTypes', b'RotationRing', line, flags=re.I)
            rows.append(tuple(_ring(normalized.decode('ascii'))))
    return rows


def _sections(raw):
    """Read exact construction section bodies, excluding inter-section newlines."""
    matches = list(SECTION.finditer(raw))
    output = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(raw)
        output.append((int(match[1], 16), raw[match.end():end].rstrip(b'\r\n')))
    return output


def _restore(raw, composition):
    """Validate the generated spans and reconstruct the exact native RUL0."""
    require(isinstance(raw, bytes) and isinstance(composition, dict)
            and all(isinstance(composition.get(key), str) for key in (
                'ordering_insertion', 'suffix', 'base_sha256')),
            'Malformed assembly alias RUL0 composition')
    insertion = composition['ordering_insertion'].encode('ascii')
    suffix = composition['suffix'].encode('ascii')
    marker = MARKER.encode('ascii')
    require(suffix.startswith(marker) and raw.endswith(suffix) and raw.count(marker) == 1,
            'Assembly aliases require the exact generated RUL0 definitions')
    start, end = ordering_span(raw)
    require(insertion and raw.count(insertion) == 1 and insertion in raw[start:end],
            'Assembly aliases require the exact generated Ordering insertion')
    native = raw[:-len(suffix)].replace(insertion, b'', 1)
    require(hashlib.sha256(native).hexdigest() == composition['base_sha256'],
            'Assembly aliases did not restore the exact native RUL0')
    return insertion, suffix, native


def _canonical_bodies(raw, insertion, suffix, aliases):
    """Check declared roots and return original bodies by construction state."""
    require(isinstance(aliases, (tuple, list)) and all(
        isinstance(pair, (tuple, list)) and len(pair) == 2
        and all(type(root) is int and 0 < root <= 0xFFFF for root in pair)
        for pair in aliases), 'Malformed assembly construction aliases')
    current_rows = _rows(insertion)
    start, end = ordering_span(raw)
    occupied = {int(match[1], 16) for match in SECTION.finditer(raw)}
    occupied.update(state for row in _rows(raw[start:end]) for state in row)
    alias_states = [state for _, alias in aliases for state in _states(alias)]
    require(len(alias_states) == len(set(alias_states)) and not occupied.intersection(alias_states),
            'Assembly alias construction state already exists or is repeated')
    sections = _sections(suffix)
    bodies = dict(sections)
    require(len(bodies) == len(sections), 'Repeated canonical assembly construction section')
    for source, _ in aliases:
        states = _states(source)
        require(current_rows.count(states) == 1 and set(states) <= bodies.keys(),
                'Assembly alias source must have one complete canonical construction ring')
        for index, state in enumerate(states):
            body = bodies[state]
            copies = list(COPY_FROM.finditer(body))
            copy_lines = sum(bool(re.match(rb'CopyFrom\b', line, re.I))
                             for _, _, line in _active_lines(body))
            require(copy_lines == len(copies) <= 1
                    and (not copies or int(copies[0][1], 16) in states[:index]),
                    'Assembly alias source has a noncanonical construction reference')
    return bodies


def _append_rings(insertion, rings):
    newline = b'\r\n' if b'\r\n' in insertion else b'\n'
    end = ORDERING_END.encode('ascii')
    require(insertion.count(end) == 1, 'Assembly aliases require one Ordering end marker')
    return insertion.replace(end, newline.join(rings) + newline + end, 1)


def add_aliases(raw, composition, aliases, *, terminal_bodies=None):
    """Append aliases and temporary standalone rings before assembly ordering.

    Each pair identifies a canonical root and a distinct new root. The only
    copied fields that change are references between the copied states, plus
    the domain-owned root body edit for an explicitly selected terminal.
    """
    terminal_bodies = terminal_bodies or {}
    require(terminal_bodies.keys() <= {alias for _, alias in aliases},
            'Assembly terminal body has no construction alias')
    if not aliases:
        return raw, composition
    insertion, suffix, _ = _restore(raw, composition)
    bodies = _canonical_bodies(raw, insertion, suffix, aliases)
    rings, sections = [], []
    for source, alias in aliases:
        remap = dict(zip(_states(source), _states(alias)))
        rings.append(('RotationRing = ' + ', '.join(f'{state:X}' for state in remap.values())).encode('ascii'))
        for original, copied in remap.items():
            body = bodies[original]
            if copied == alias and alias in terminal_bodies:
                body = terminal_bodies[alias](body)
            if reference := COPY_FROM.search(body):
                target = remap[int(reference[1], 16)]
                body = body[:reference.start(1)] + f'0x{target:X}'.encode('ascii') + body[reference.end(1):]
            sections.append(f'[HighwayIntersectionInfo_0x{copied:08X}]'.encode('ascii') + body)
    expanded_order = _append_rings(insertion, rings)
    expanded_suffix = suffix + b'\r\n' + b'\r\n\r\n'.join(sections) + b'\r\n'
    expanded = raw[:-len(suffix)].replace(insertion, expanded_order, 1) + expanded_suffix
    metadata = {**composition, 'ordering_insertion': expanded_order.decode('ascii'),
                'suffix': expanded_suffix.decode('ascii')}
    family_key = piece_menu_families.KEY
    if family_key in composition:
        _, plain = piece_menu_families._restore(raw, composition)
        previous = _append_rings(plain['ordering_insertion'].encode('ascii'), rings)
        expanded_plain = expanded.replace(expanded_order, previous, 1)
        metadata[family_key] = {**composition[family_key],
                                'previous_ordering_insertion': previous.decode('ascii'),
                                'previous_controller_sha256': hashlib.sha256(expanded_plain).hexdigest()}
    return expanded, metadata


def verify_aliases(original_raw, original_composition, final_raw, final_composition, aliases,
                   *, terminal_bodies=None):
    """Inspect saved alias definitions and prove all original bytes recover."""
    terminal_bodies = terminal_bodies or {}
    require(terminal_bodies.keys() <= {alias for _, alias in aliases},
            'Assembly terminal verifier has no construction alias')
    old_order, old_suffix, old_native = _restore(original_raw, original_composition)
    order, suffix, native = _restore(final_raw, final_composition)
    require(native == old_native and suffix.startswith(old_suffix),
            'Assembly aliases changed the native or canonical construction bytes')
    originals = _canonical_bodies(original_raw, old_order, old_suffix, aliases)
    extra = suffix[len(old_suffix):]
    definitions = _sections(extra)
    expected_states = [state for _, alias in aliases for state in _states(alias)]
    require([state for state, _ in definitions] == expected_states,
            'Saved assembly alias definitions differ from their declared construction states')
    if aliases:
        require(extra == b'\r\n' + b'\r\n\r\n'.join(
            f'[HighwayIntersectionInfo_0x{state:08X}]'.encode('ascii') + body
            for state, body in definitions) + b'\r\n',
            'Unexpected bytes among the saved assembly alias definitions')
    else:
        require(not extra, 'Unexpected assembly alias definitions')
    saved = dict(definitions)
    saved_rows = _rows(order)
    for source, alias in aliases:
        alias_states = _states(alias)
        require([row for row in saved_rows if set(row).intersection(alias_states)] == [alias_states],
                'Saved assembly alias does not have one exact eight-state Ordering row')
        inverse = dict(zip(alias_states, _states(source)))
        for copied, original in inverse.items():
            original_body, copied_body = originals[original], saved[copied]
            canonical = COPY_FROM.search(original_body)
            reference = COPY_FROM.search(copied_body)
            if canonical is None:
                if copied == alias and alias in terminal_bodies:
                    require(reference is None, 'Assembly terminal unexpectedly copies another root')
                    terminal_bodies[alias](original_body, copied_body)
                    continue
                require(copied_body == original_body,
                        'Assembly alias changed a canonical construction body')
                continue
            require(reference is not None and inverse.get(int(reference[1], 16)) == int(canonical[1], 16)
                    and reference[1] == f'0x{int(reference[1], 16):X}'.encode('ascii')
                    and copied_body[:reference.start(1)] == original_body[:canonical.start(1)]
                    and copied_body[reference.end(1):] == original_body[canonical.end(1):],
                    'Assembly alias changed a canonical construction reference or body')
