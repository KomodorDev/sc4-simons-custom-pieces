"""Compose separate rotation-order and puzzle-definition deltas into native RUL0.

RotationRing properties belong to the existing [Ordering] section. Piece
definitions are appended separately; removing both additions restores every
original native byte, including comments and line endings.
"""
from __future__ import annotations

import hashlib
import re

from .dbpf import require

MARKER = '\r\n;BEGIN SIMONS CUSTOM PIECES - GENERATED; DO NOT EDIT\r\n'
ORDERING_BEGIN = ';BEGIN SIMONS CUSTOM PIECES ROTATIONS - GENERATED; DO NOT EDIT'
ORDERING_END = ';END SIMONS CUSTOM PIECES ROTATIONS'


def _active_lines(raw):
    offset = 0
    for line in raw.splitlines(keepends=True):
        active = line.split(b';', 1)[0].strip()
        yield offset, offset + len(line), active
        offset += len(line)


def ordering_span(raw: bytes) -> tuple[int, int]:
    """Locate the unique active Ordering body, ignoring commented fake headers."""
    headers = []
    for start, end, line in _active_lines(raw):
        match = re.fullmatch(rb'\[([^\]]+)\]', line)
        if match:
            headers.append((start, end, match[1].strip().lower()))
    found = [i for i, header in enumerate(headers) if header[2] == b'ordering']
    require(len(found) == 1, 'Native RUL0 requires exactly one [Ordering] section')
    index = found[0]
    return headers[index][1], headers[index + 1][0] if index + 1 < len(headers) else len(raw)


def _ring(line: str) -> list[int]:
    active = line.split(';', 1)[0].strip()
    match = re.fullmatch(r'RotationRing\s*=\s*(.+)', active, re.I)
    require(match is not None, 'Malformed RotationRing property')
    tokens = [token.strip() for token in match[1].split(',')]
    require(tokens and all(re.fullmatch(r'(?:0x)?[0-9a-f]{1,8}', token, re.I)
                           for token in tokens), 'Malformed RotationRing state identifier')
    return [int(token, 16) for token in tokens]


def split_rule_delta(delta: str) -> tuple[str, str]:
    """Separate one generator fragment without changing any definition bytes."""
    rings, definitions = [], []
    for line in delta.splitlines(keepends=True):
        active = line.split(';', 1)[0].strip()
        if active.lower().startswith('rotationring'):
            states = _ring(line)
            require(len(states) == len(set(states)) == 8,
                    'Each custom RotationRing requires eight unique states')
            rings.append(line.rstrip('\r\n'))
        else:
            require(not active.lower().startswith('addtypes'),
                    'Custom pieces must not extend a native type ring')
            require(not re.fullmatch(r'\[\s*ordering\s*\]', active, re.I),
                    'Piece fragments must not create another [Ordering] section')
            definitions.append(line)
    require(len(rings) == 1, 'Each selected piece must emit exactly one RotationRing')
    return rings[0], ''.join(definitions)


def compose_rul0(native: bytes, deltas: list[str]) -> tuple[bytes, dict]:
    """Insert independent custom rings and append unchanged definition fragments."""
    require(deltas, 'Controller composition requires at least one piece')
    require(MARKER.encode() not in native and ORDERING_BEGIN.encode() not in native,
            'Controller baseline already contains generated SCP additions')
    _, insertion_offset = ordering_span(native)
    rings, definitions = zip(*(split_rule_delta(delta) for delta in deltas))
    custom = [state for line in rings for state in _ring(line)]
    require(len(custom) == len(set(custom)), 'Custom RotationRing states overlap')
    native_states = set()
    for _, _, line in _active_lines(native):
        if line.lower().startswith(b'rotationring'):
            native_states.update(_ring(line.decode('ascii')))
    require(not native_states.intersection(custom), 'Custom RotationRing state already belongs to NAM')
    newline = '\r\n' if b'\r\n' in native else '\n'
    separator = '' if not insertion_offset or native[insertion_offset - 1:insertion_offset] in (b'\r', b'\n') else newline
    insertion = separator + ORDERING_BEGIN + newline + newline.join(rings) + newline + ORDERING_END + newline
    suffix = MARKER + '\r\n'.join(definitions)
    raw_insertion, raw_suffix = insertion.encode('ascii'), suffix.encode('ascii')
    result = native[:insertion_offset] + raw_insertion + native[insertion_offset:] + raw_suffix
    require(result[:-len(raw_suffix)].replace(raw_insertion, b'', 1) == native,
            'Controller additions must restore the exact native bytes')
    return result, {'base_sha256': hashlib.sha256(native).hexdigest(),
                    'ordering_insertion': insertion, 'suffix': suffix}


def with_feature_sequence(controller: bytes, composition: dict,
                          base_states: list[int]) -> tuple[bytes, dict]:
    """Opt a previously composed controller into one shared Tab family.

    ``base_states`` names at least two existing generated rotation-row roots,
    in the desired feature order. Home/End retain each exact eight-state row;
    Tab/Shift-Tab move between rows. All buttons entering these same states
    share that family, including buttons starting at a nonfirst member.

    Only the marked SCP Ordering insertion changes. Native rules, appended
    definitions, game identifiers, and unrelated generated rows remain exact.
    The returned metadata records both insertions and the prior controller
    digest, so callers can independently undo and inspect the experiment.
    Normal composition and its verification contract remain unchanged.
    """
    require(isinstance(controller, bytes) and isinstance(composition, dict),
            'Feature sequence requires controller bytes and composition metadata')
    require('feature_sequence' not in composition,
            'Controller already has a feature sequence; start from its original build')
    require(isinstance(base_states, (list, tuple)) and len(base_states) >= 2,
            'Feature sequence requires at least two explicit base states')
    require(all(isinstance(state, int) and not isinstance(state, bool)
                and 0 <= state <= 0xFFFFFFFF for state in base_states),
            'Feature sequence base states must be unsigned 32-bit integers')
    require(len(set(base_states)) == len(base_states),
            'Feature sequence repeats a base state')
    fields = [composition.get(key) for key in
              ('base_sha256', 'ordering_insertion', 'suffix')]
    require(all(isinstance(value, str) and value for value in fields),
            'Feature sequence requires complete composition metadata')
    digest, insertion, suffix = fields
    require(re.fullmatch(r'[0-9a-f]{64}', digest) is not None,
            'Composition baseline digest is malformed')
    try:
        raw_insertion, raw_suffix = insertion.encode('ascii'), suffix.encode('ascii')
        controller.decode('ascii')
    except UnicodeError as error:
        raise ValueError('Feature sequence controller and metadata must be ASCII') from error
    require(suffix.startswith(MARKER) and controller.count(MARKER.encode()) == 1
            and controller.count(ORDERING_BEGIN.encode()) == 1
            and controller.count(ORDERING_END.encode()) == 1,
            'Feature sequence requires unique complete SCP composition markers')
    require(controller.endswith(raw_suffix), 'Controller suffix differs from composition metadata')
    body = controller[:-len(raw_suffix)]
    require(body.count(raw_insertion) == 1,
            'Controller has a missing or nonunique generated Ordering insertion')
    start = body.index(raw_insertion)
    ordering_start, ordering_end = ordering_span(controller)
    require(ordering_start <= start and start + len(raw_insertion) <= ordering_end,
            'Generated feature sequence must be inside the active Ordering section')
    native = body.replace(raw_insertion, b'', 1)
    require(hashlib.sha256(native).hexdigest() == digest,
            'Controller does not restore its exact native baseline')
    require(MARKER.encode() not in native and ORDERING_BEGIN.encode() not in native,
            'Restored baseline contains generated SCP additions')

    lines = insertion.splitlines(keepends=True)
    begin = [i for i, line in enumerate(lines) if line.strip() == ORDERING_BEGIN]
    end = [i for i, line in enumerate(lines) if line.strip() == ORDERING_END]
    require(len(begin) == len(end) == 1 and begin[0] < end[0]
            and all(not line.strip() for line in lines[:begin[0]])
            and end[0] == len(lines) - 1,
            'Generated Ordering insertion has malformed rotation markers')
    rows, seen = {}, set()
    for index in range(begin[0] + 1, end[0]):
        states = _ring(lines[index])
        require(len(states) == len(set(states)) == 8,
                'Each generated feature row requires eight unique states')
        require(not seen.intersection(states), 'Generated rotation rows overlap')
        seen.update(states)
        rows[states[0]] = (index, states)
    require(rows, 'Generated Ordering insertion has no rotation rows')
    require(all(state in rows for state in base_states),
            'Feature sequence contains an unknown or noncanonical rotation-row root')

    native_states = set()
    native_start, native_end = ordering_span(native)
    for _, _, active in _active_lines(native[native_start:native_end]):
        if re.match(rb'(?:RotationRing|AddTypes)\b', active, re.I):
            normalized = re.sub(rb'^AddTypes\b', b'RotationRing', active, flags=re.I)
            native_states.update(_ring(normalized.decode('ascii')))
    require(not native_states.intersection(seen),
            'Generated feature state already belongs to a native rotation or type ring')
    definitions = {}
    for _, _, active in _active_lines(controller):
        match = re.fullmatch(rb'\[HighwayIntersectionInfo_0x([0-9a-f]{1,8})\]', active, re.I)
        if match:
            state = int(match[1], 16)
            definitions[state] = definitions.get(state, 0) + 1
    selected_rows = [rows[state][1] for state in base_states]
    require(all(definitions.get(state) == 1 for row in selected_rows for state in row),
            'Feature sequence requires one construction definition for every selected state')

    selected_indices = {rows[state][0] for state in base_states}
    first = min(selected_indices)
    replacement = []
    for index, line in enumerate(lines):
        if index == first:
            for order, state in enumerate(base_states):
                original = lines[rows[state][0]]
                keyword = 'RotationRing' if order == 0 else 'AddTypes'
                replacement.append(re.sub(r'^(\s*)RotationRing\b',
                                          lambda match: match[1] + keyword,
                                          original, count=1, flags=re.I))
        if index not in selected_indices:
            replacement.append(line)
    updated_insertion = ''.join(replacement)
    updated = body.replace(raw_insertion, updated_insertion.encode('ascii'), 1) + raw_suffix
    require(updated[:-len(raw_suffix)].replace(updated_insertion.encode('ascii'), b'', 1) == native,
            'Feature sequence must preserve every native byte')
    metadata = dict(composition, ordering_insertion=updated_insertion,
                    feature_sequence={'schema_version': 1, 'base_states': list(base_states),
                                      'rotation_rows': selected_rows, 'shared_tab_family': True,
                                      'previous_ordering_insertion': insertion,
                                      'previous_controller_sha256': hashlib.sha256(controller).hexdigest()})
    return updated, metadata
