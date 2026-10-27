"""Authoritative manual observations and derived, portable content views.

Manual results are observations of exact cases under stated game conditions.
Generators create unverified cases; they cannot infer a human pass from an
image, software report, former checkbox, or a manifest's game_tests fields.
Only record_user_result accepts manual observations, and requires an explicit
user confirmation plus a reviewer, date, evidence and test environment.
"""
from __future__ import annotations

from collections import Counter
from copy import deepcopy
from datetime import datetime
import hashlib
import json
import math
import os
from pathlib import Path
import re
import shlex

STATES = ('unverified', 'passed', 'failed', 'stale', 'not_applicable')
ROTATIONS = (0, 90, 180, 270)
MANUAL_KINDS = frozenset({
    'preview_review', 'in_game_render', 'in_game_placement', 'in_game_connection',
    'in_game_journey', 'in_game_route_query', 'in_game_visible_travel',
    'in_game_forbidden_transfer', 'in_game_demolition', 'in_game_save_reload',
})
JOURNEY_KINDS = frozenset({'in_game_journey', 'in_game_route_query', 'in_game_visible_travel'})
SOFTWARE_KINDS = frozenset({'software_resources', 'software_connectivity'})
RESOURCE_KINDS = {
    0x5ad0e817: 'model', 0x296678f7: 'path', 0x6534284a: 'exemplar',
    0xea5118b0: 'effect', 0x2026960b: 'text', 0x856ddbac: 'icon',
}
_SHA = re.compile(r'[0-9a-f]{64}')


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def markdown_metadata(title, summary, audience, document_type):
    """Return deterministic YAML frontmatter with four JSON-quoted string values."""
    values = (title, summary, audience, document_type)
    _require(all(isinstance(value, str) and value.strip() for value in values),
             'Markdown metadata values must be nonempty strings')
    fields = zip(('title', 'summary', 'audience', 'document_type'), values)
    # JSON strings are valid YAML quoted scalars. Escaping non-ASCII separators
    # also keeps every field on one physical source line without losing data.
    return '---\n' + ''.join(f'{key}: {json.dumps(value)}\n' for key, value in fields) + '---\n\n'


def split_markdown_metadata(text):
    """Split leading frontmatter from its body, retaining the exact header bytes."""
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].rstrip('\r\n') != '---':
        return '', text
    for index, line in enumerate(lines[1:], 1):
        if line.rstrip('\r\n') == '---':
            offset = sum(len(item) for item in lines[:index + 1])
            while offset < len(text) and text[offset] in '\r\n':
                offset += 1
            return text[:offset], text[offset:]
    raise ValueError('Markdown metadata needs a closing --- delimiter')


def _json(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def fingerprint(value):
    """Hash bytes or explicit semantic data, never source paths or timestamps."""
    raw = value if isinstance(value, bytes) else _json(value).encode('utf8')
    return hashlib.sha256(raw).hexdigest()


def _sha_map(value):
    _require(isinstance(value, dict) and all(isinstance(key, str) and key
             and isinstance(digest, str) and _SHA.fullmatch(digest)
             for key, digest in value.items()), 'Fingerprints must map stable resource keys to SHA-256 strings')
    return dict(sorted(value.items()))


def resource_fingerprints(subject_id, resources, construction=None):
    """Fingerprint decompressed resources individually, independent of filenames.

    Resource IDs are (type, group, instance) integer tuples. The construction
    argument is this subject's actual emitted rules (not a full controller).
    A different ZIP/DAT name, JSON formatting or documentation does not change
    these hashes. Callers may add dependency texture hashes by stable key.
    """
    _require(isinstance(subject_id, str) and subject_id, 'Subject ID is required')
    result = {}
    for tgi, raw in resources.items():
        _require(isinstance(tgi, tuple) and len(tgi) == 3
                 and all(type(value) is int and 0 <= value <= 0xffffffff for value in tgi),
                 'Resource identity must be an integer TGI triple')
        _require(isinstance(raw, bytes), 'Fingerprint decompressed resource bytes')
        kind = RESOURCE_KINDS.get(tgi[0], 'resource')
        if tgi[0] == 0x7ab50e44:
            kind = 'shadow' if tgi[1] == 0x2bc2759a else 'texture'
        result[f'{kind}:{subject_id}:'+ '-'.join(f'{value:08x}' for value in tgi)] = fingerprint(raw)
    if construction is not None:
        result[f'construction:{subject_id}'] = fingerprint(construction)
    return _sha_map(result)


def _case_identifier(kind, scope):
    # IDs depend on case meaning, never descriptions, filenames or current hashes.
    return kind+'-'+fingerprint(scope)[:20]


def _dependencies(keys, fingerprints):
    return {key: fingerprints[key] for key in sorted(set(keys)) if key in fingerprints}


def _port_semantics(port):
    keys = ('id', 'service_network', 'variant', 'role', 'engine_transport',
            'engine_transport_classes', 'direction', 'endpoint_m', 'tangent',
            'grade', 'connection_class', 'profile', 'lane_spacing_m')
    return {key: port[key] for key in keys if key in port}


def connectivity_fingerprints(subject_id, connections):
    """Hash routing/interface facts without prose, links or preview filenames."""
    result = {}
    for port in connections.get('ports', []):
        result[f'interface:{subject_id}:{port["id"]}'] = fingerprint(_port_semantics(port))
    journeys = [{key: item[key] for key in ('id', 'service_network', 'role', 'entry_port',
                 'exit_port', 'from_port', 'to_port', 'placements', 'engine_transport_classes')
                 if key in item} for item in connections.get('journeys', [])]
    result[f'graph:{subject_id}'] = fingerprint({
        'journeys': journeys,
        'forbidden_transfers': [{key:item[key] for key in ('from_port','to_port','from_service','to_service') if key in item}
                                for item in connections.get('forbidden_transfers', [])],
    })
    return result


def _new_case(kind, description, scope, dependencies, *, applicability='applicable', reason=None):
    case = {'id': _case_identifier(kind, scope), 'kind': kind,
            'description': description, 'scope': deepcopy(scope),
            'applicability': applicability, 'dependencies': _sha_map(dependencies),
            'observations': []}
    if reason is not None:
        case['not_applicable_reason'] = reason
    return case


def _orientation_scopes(connections):
    states = connections.get('supported_orientations')
    if states is None:
        return [{'rotation_ccw_degrees': angle} for angle in ROTATIONS]
    _require(isinstance(states,list) and states, 'Supported orientation states must be nonempty')
    result=[]
    for state in states:
        angle=state.get('rotation_ccw_degrees')
        transposed=state.get('construction_transposed')
        _require(type(angle) is int and angle in ROTATIONS and type(transposed) is bool,
                 'Orientation needs a proper rotation and explicit construction transpose flag')
        scope={'rotation_ccw_degrees':angle}
        # Keep the original four proper-rotation case identities unchanged.
        if transposed:scope['construction_transposed']=True
        _require(scope not in result, 'Duplicate supported orientation state')
        result.append(scope)
    return result


def new_manual_record(subject_id, subject_kind, connections, fingerprints, preview_hashes=None, *,
                      split_journey_observations=False):
    """Generate applicable cases at actual supported orientations, unverified.

    Software, image review, and actual game rendering have separate cases.
    Endpoint candidate lists do not generate manual compatibility coverage.
    An opted-in assembly records Route Query and visible travel independently;
    existing generic journey observations never become either new result.
    """
    _require(subject_kind in ('piece', 'assembly'), 'Subject kind must be piece or assembly')
    _require(type(split_journey_observations) is bool, 'Split journey observations must be a boolean')
    _require(not split_journey_observations or subject_kind == 'assembly',
             'Split journey observations are an assembly documentation opt-in')
    _require(connections.get('subject_id', subject_id) == subject_id, 'Connection metadata belongs to another subject')
    values = _sha_map(fingerprints)
    orientations = _orientation_scopes(connections)
    values.update(connectivity_fingerprints(subject_id, connections))
    images = _sha_map(preview_hashes or {})
    image_values = {f'image:{subject_id}:{key}': value for key, value in images.items()}
    values.update(image_values)
    resource_keys = [key for key in values if (subject_kind == 'assembly' or f':{subject_id}:' in key or key.endswith(':'+subject_id)) and key.split(':', 1)[0] in
                     ('model', 'path', 'construction', 'exemplar', 'effect', 'shadow', 'texture', 'resource', 'assembly_pose')]
    traffic_keys = [key for key in values if (subject_kind == 'assembly' or f':{subject_id}:' in key or key.endswith(':'+subject_id)) and key.split(':', 1)[0] in ('path', 'construction', 'graph', 'interface', 'assembly_pose')]
    visual_keys = [key for key in values if (subject_kind == 'assembly' or f':{subject_id}:' in key or key.endswith(':'+subject_id)) and key.split(':', 1)[0] in ('model', 'shadow', 'texture', 'effect', 'assembly_pose')]
    cases = [
        _new_case('software_resources', 'Verify the actual compiled resources and construction rules.',
                  {'subject_id': subject_id}, _dependencies(resource_keys, values)),
        _new_case('software_connectivity', 'Verify the declared directed journeys and forbidden transfers.',
                  {'subject_id': subject_id}, _dependencies(traffic_keys, values)),
    ]
    for image_key in sorted(image_values):
        cases.append(_new_case('preview_review', 'Inspect this exact preview for tracks, walls, piers, seams and shadows.',
            {'subject_id': subject_id, 'image_key': image_key}, {image_key: image_values[image_key]}))
    if not image_values:
        # Missing artwork remains a visible pending check, never an automatic N/A or pass.
        cases.append(_new_case('preview_review', 'Supply and review a current complete model preview.',
                               {'subject_id': subject_id, 'image_key': None}, {}))
    for orientation in orientations:
        scope = {'subject_id': subject_id, **orientation}
        for kind, description in (
                ('in_game_render', 'Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.'),
                ('in_game_placement', 'Place this piece or complete blueprint and inspect every occupied tile.'),
                ('in_game_demolition', 'Bulldoze the complete placement and inspect the cleared area.'),
                ('in_game_save_reload', 'Save, quit, reload and inspect the placement and its paths.')):
            keys = visual_keys if kind == 'in_game_render' else resource_keys
            cases.append(_new_case(kind, description, scope, _dependencies(keys, values)))
    # Legacy endpoint/counterpart cases remain readable and recordable, but
    # an endpoint shortlist cannot establish a complete-boundary test scope.
    for journey in connections.get('journeys', []):
        for orientation in orientations:
            scope = {'subject_id': subject_id, 'journey_id': journey['id'],
                     'service_network': journey.get('service_network'),
                     'role': journey.get('role', 'primary'),
                     'entry_port': journey.get('entry_port', journey.get('from_port')),
                     'exit_port': journey.get('exit_port', journey.get('to_port')),
                     **orientation}
            journey_checks = (
                ('in_game_route_query', 'Use Route Query in SimCity 4 to confirm this directed journey for its service network.'),
                ('in_game_visible_travel', 'Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.'),
            ) if split_journey_observations else (
                ('in_game_journey', 'Run the declared journey in this direction using its service network.'),
            )
            for kind, description in journey_checks:
                cases.append(_new_case(kind, description, scope, _dependencies(traffic_keys, values)))
    for transfer in connections.get('forbidden_transfers', []):
        for orientation in orientations:
            scope = {'subject_id': subject_id, 'forbidden_transfer': deepcopy(transfer),
                     **orientation}
            cases.append(_new_case('in_game_forbidden_transfer', 'Confirm this undeclared transfer is unavailable.',
                                   scope, _dependencies(traffic_keys, values)))
    record = {'schema_version': 1, 'purpose': 'Authoritative explicit observations for individually scoped manual and software checks.', 'subject': {'id': subject_id, 'kind': subject_kind},
              'authority': 'Explicit user observations; generated Markdown is a read-only view.',
              'state_policy': 'Unverified, passed, failed, stale; not applicable is an explicit separate declaration.',
              'rotation_policy': ('Actual emitted rules support four proper rotations and four distinct construction-transposed states; each has separate manual coverage. Counterpart reflection is never assumed.'
                  if any(scope.get('construction_transposed') for scope in orientations) else
                  'Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.'),
              'supported_orientations': deepcopy(connections.get('supported_orientations',orientations)),
              'environment_policy': 'Every result applies only to its recorded platform, game version and NAM profile.',
              'fingerprints': dict(sorted(values.items())), 'cases': cases}
    validate_manual_record(record)
    return record


def _expanded_record(record):
    """Resolve shared dependency tables for helpers without changing the caller."""
    output=deepcopy(record)
    sets=output.get('dependency_sets',{})
    for case in output.get('cases',[])+output.get('removed_cases',[]):
        if 'dependency_ref' in case:
            _require(case['dependency_ref'] in sets,'Case refers to a missing dependency set')
            case['dependencies']=deepcopy(sets[case['dependency_ref']])
            expected=_case_fingerprint(case)
            _require(case.get('dependency_snapshot')==expected,'Stored case dependency snapshot differs from actual shared fingerprints')
            del case['dependency_ref'];del case['dependency_snapshot']
    output.pop('dependency_sets',None)
    return output


def compact_manual_record(record):
    """Store each identical granular dependency map once per subject record."""
    output=_expanded_record(record);sets={}
    for case in output.get('cases',[])+output.get('removed_cases',[]):
        dependencies=case['dependencies'];key=fingerprint(dependencies)
        sets.setdefault(key,dependencies)
        case['dependency_snapshot']=_case_fingerprint(case)
        case['dependency_ref']=key
        del case['dependencies']
    output['dependency_sets']=sets
    return output


def validate_manual_record(record):
    record = _expanded_record(record)
    _require(record.get('schema_version') == 1, 'Unsupported manual-test record schema')
    subject = record.get('subject', {})
    _require(subject.get('kind') in ('piece', 'assembly') and subject.get('id'), 'Invalid manual-test subject')
    _sha_map(record.get('fingerprints', {}))
    seen = set()
    for case in record.get('cases', []):
        _require(case.get('kind') in MANUAL_KINDS | SOFTWARE_KINDS, 'Unknown manual/software check kind')
        _require(case.get('id') == _case_identifier(case['kind'], case.get('scope', {})), 'Case ID differs from its exact scope')
        _require(case['id'] not in seen, 'Repeated manual-test case ID')
        seen.add(case['id'])
        _require(case.get('applicability') in ('applicable', 'not_applicable'), 'Invalid applicability')
        if case['applicability'] == 'not_applicable':
            _require(bool(case.get('not_applicable_reason', '').strip()), 'Not-applicable checks need an explicit reason')
        _sha_map(case.get('dependencies', {}))
        _require(all(record['fingerprints'].get(key)==value for key,value in case.get('dependencies',{}).items()),
                 'Case dependencies differ from the authoritative current resource inventory; regenerate the record')
        for observation in case.get('observations', []):
            _validate_observation(case, observation)
    _require(isinstance(record.get('cases'), list), 'Manual-test cases must be a list')
    return True


def _validate_observation(case, observation):
    _require(observation.get('result') in ('passed', 'failed'), 'Observations record passed or failed, never computed states')
    _require(isinstance(observation.get('reviewer'), str) and observation['reviewer'].strip(), 'Observation needs a named reviewer')
    _require(isinstance(observation.get('confirmed_at'), str), 'Observation needs a date')
    try:
        datetime.fromisoformat(observation['confirmed_at'].replace('Z', '+00:00'))
    except ValueError as error:
        raise ValueError('Observation date must be ISO-8601') from error
    _require(bool(observation.get('evidence')) and all(isinstance(item, str) and item.strip()
             for item in observation['evidence']), 'Observation needs evidence paths or explicit observation notes')
    _require(bool(_SHA.fullmatch(observation.get('dependency_fingerprint', ''))), 'Observation needs its exact dependency fingerprint')
    if case['kind'] in MANUAL_KINDS:
        _require(observation.get('authority') == 'user' and
                 observation.get('confirmation_method') == 'explicit_user_confirmation',
                 'A manual pass/failure needs explicit user confirmation')
        environment = observation.get('environment', {})
        if case['kind'] != 'preview_review':
            _require(all(isinstance(environment.get(key), str) and environment[key].strip()
                         for key in ('platform', 'game_version', 'nam_profile')),
                     'In-game observations require platform, game_version and nam_profile')
    else:
        _require(observation.get('authority') == 'software', 'Software cases require software evidence, not a human checkbox')


def _find_case(record, case_id):
    matches = [case for case in record['cases'] if case['id'] == case_id]
    if not matches:
        matches = [case for case in record.get('removed_cases', []) if case['id'] == case_id]
    _require(len(matches) == 1, 'Unknown or repeated manual-test case')
    return matches[0]


def _case_fingerprint(case, fingerprints=None):
    if 'dependencies' not in case:
        _require(fingerprints is None, 'Expand shared case dependencies before comparing a different resource map')
        return case['dependency_snapshot']
    keys = case['dependencies']
    values = case['dependencies'] if fingerprints is None else {
        key: fingerprints.get(key, '<missing>') for key in keys}
    return fingerprint({'scope': case['scope'], 'dependencies': values,
                        'applicability': case['applicability']})


def record_user_result(record, case_id, result, *, explicit_user_confirmation,
                       reviewer, confirmed_at, evidence, environment=None, note=''):
    """Record only the particular observation explicitly confirmed by the user.

    This API is not called by content/build/render generators. An integration
    may invoke it only when relaying an actual user observation, never to turn
    a generated preview, software success or elapsed time into user approval.
    """
    _require(explicit_user_confirmation is True, 'Explicit user confirmation is required')
    output = _expanded_record(record)
    case = _find_case(output, case_id)
    _require(case['kind'] in MANUAL_KINDS, 'User observations cannot mark a software case')
    _require(case['applicability'] == 'applicable', 'A not-applicable case cannot be passed')
    _require(bool(case['dependencies']), 'Cannot record a result without actual relevant resource/image fingerprints')
    _require(not case.get('missing_dependencies'), 'Cannot record a result while relevant counterpart resource fingerprints are missing')
    if case['kind'] == 'in_game_connection':
        _require(case['scope'].get('counterpart') is not None, 'A connection observation requires a concrete counterpart')
    observation = {'result': result, 'authority': 'user',
                   'confirmation_method': 'explicit_user_confirmation',
                   'reviewer': reviewer, 'confirmed_at': confirmed_at,
                   'evidence': list(evidence), 'environment': dict(environment or {}),
                   'note': note, 'dependency_fingerprint': _case_fingerprint(case)}
    _validate_observation(case, observation)
    case['observations'].append(observation)
    validate_manual_record(output)
    return output


def record_software_result(record, case_id, result, *, verifier, checked_at, evidence):
    """Store an actual software report without changing any human check."""
    output = _expanded_record(record)
    case = _find_case(output, case_id)
    _require(case['kind'] in SOFTWARE_KINDS, 'Software cannot mark a manual check')
    _require(bool(case['dependencies']), 'Software result requires actual dependency fingerprints')
    observation = {'result': result, 'authority': 'software', 'reviewer': verifier,
                   'confirmed_at': checked_at, 'evidence': list(evidence), 'environment': {},
                   'dependency_fingerprint': _case_fingerprint(case)}
    _validate_observation(case, observation)
    case['observations'].append(observation)
    validate_manual_record(output)
    return output


def case_state(case, fingerprints=None, environment=None):
    """Compute one current state; environment filters never borrow another platform's pass."""
    if case['applicability'] == 'not_applicable':
        return 'not_applicable'
    observations = case.get('observations', [])
    if environment is not None:
        observations = [item for item in observations if all(
            item.get('environment', {}).get(key) == value for key, value in environment.items())]
    if not observations:
        return 'unverified'
    observation = observations[-1]
    if observation['dependency_fingerprint'] != _case_fingerprint(case, fingerprints):
        return 'stale'
    return observation['result']


def refresh_manual_record(previous, generated):
    """Refresh generated cases; retain applicable observations and their old hashes.

    A deleted case is retained as historical evidence under removed_cases,
    never counted as current coverage. Changes to comments or source paths do
    not alter a case dependency fingerprint; actual changed resources do.
    """
    previous, generated = _expanded_record(previous), _expanded_record(generated)
    validate_manual_record(previous)
    validate_manual_record(generated)
    _require(previous['subject'] == generated['subject'], 'Cannot merge records for different subjects')
    output = deepcopy(generated)
    old = {case['id']: case for case in previous['cases']}
    current_ids = {case['id'] for case in output['cases']}
    for case in output['cases']:
        if case['id'] in old:
            case['observations'] = deepcopy(old[case['id']].get('observations', []))
            if old[case['id']]['applicability'] == 'not_applicable':
                case['applicability'] = 'not_applicable'
                case['not_applicable_reason'] = old[case['id']]['not_applicable_reason']
            if old[case['id']].get('not_applicable_declaration'):
                case['not_applicable_declaration'] = deepcopy(old[case['id']]['not_applicable_declaration'])
    removed = deepcopy(previous.get('removed_cases', []))
    removed += [deepcopy(case) for case_id, case in old.items()
                if case_id not in current_ids and _has_case_history(case)
                and not any(item['id'] == case_id for item in removed)]
    if removed:
        output['removed_cases'] = removed
    validate_manual_record(output)
    return output


def _has_case_history(case):
    return bool(case.get('observations') or case.get('not_applicable_declaration')
                or case.get('applicability') == 'not_applicable')


def retire_connection_cases(record):
    """Remove legacy active endpoint cases without regenerating any other case.

    Retain each remaining raw case and every fingerprint/dependency table.
    Observed and explicitly inapplicable legacy cases move intact to history.
    """
    validate_manual_record(record)
    output = deepcopy(record)
    retired = [case for case in output['cases'] if case['kind'] == 'in_game_connection']
    output['cases'] = [case for case in output['cases'] if case['kind'] != 'in_game_connection']
    history = output.get('removed_cases', [])
    by_id = {case['id']: case for case in history}
    for case in retired:
        if not _has_case_history(case):
            continue
        if case['id'] in by_id:
            _require(by_id[case['id']] == case, 'Conflicting legacy case already exists in history')
        else:
            history.append(case)
            by_id[case['id']] = case
    if history:
        output['removed_cases'] = history
    validate_manual_record(output)
    return output


def summarize_manual_record(record, fingerprints=None, environment=None):
    record = _expanded_record(record)
    validate_manual_record(record)
    fingerprints = record['fingerprints'] if fingerprints is None else fingerprints
    by_kind = {}
    current = [case for case in record['cases'] if case['kind'] != 'in_game_connection']
    for case in current:
        counts = by_kind.setdefault(case['kind'], Counter({state: 0 for state in STATES}))
        counts[case_state(case, fingerprints, environment)] += 1
    totals = Counter({state: 0 for state in STATES})
    for counts in by_kind.values():
        totals.update(counts)
    aggregate = {}
    if any(kind in by_kind for kind in JOURNEY_KINDS-{'in_game_journey'}):
        journey_coverage = Counter({state: 0 for state in STATES})
        for kind in JOURNEY_KINDS:
            journey_coverage.update(by_kind.get(kind, {}))
        # Preserve the shape of every subject that has not opted into split checks.
        aggregate['journey_coverage'] = dict(journey_coverage)
    return {'total': len(current), 'states': dict(totals),
            'by_kind': {key: dict(value) for key, value in sorted(by_kind.items())},
            **aggregate,
            'environment_filter': environment,
            'coverage_scope': 'Only the current explicitly listed scopes, rotations, and recorded environments; legacy endpoint observations are historical evidence, not current compatibility coverage.'}


def _md(value):
    return str(value).replace('|', '\\|').replace('\n', ' ')


_CHECK_NAMES = {
    'software_resources': 'Compiled resources', 'software_connectivity': 'Directed routing graph',
    'preview_review': 'Preview review', 'in_game_render': 'In-game rendering',
    'in_game_placement': 'Placement', 'in_game_connection': 'Connection',
    'in_game_journey': 'Journey', 'in_game_route_query': 'Route Query',
    'in_game_visible_travel': 'Visible travel', 'in_game_forbidden_transfer': 'Forbidden transfer',
    'in_game_demolition': 'Demolition', 'in_game_save_reload': 'Save and reload',
}


def _readable(value):
    """Render small scope facts as prose; never paste an opaque JSON blob."""
    if isinstance(value, dict):
        return '; '.join(str(key).replace('_', ' ')+': '+_readable(item) for key, item in value.items())
    if isinstance(value, (tuple, list)):
        return '['+', '.join(_readable(item) for item in value)+']'
    if value is None:
        return 'Unspecified'
    return str(value)


def _scope_label(scope):
    parts = []
    for key, label in (('service_network', 'Service'), ('role', 'role'), ('port_id', 'port'),
                       ('direction', 'direction'), ('journey_id', 'journey'),
                       ('entry_port', 'entry'), ('exit_port', 'exit')):
        if key in scope:
            parts.append(label+': '+_readable(scope[key]))
    if 'counterpart' in scope:
        target = scope['counterpart']
        parts.append(('counterpart: '+target.get('piece_id', '?')+' / '+target.get('port_id', '?'))
                     if target else 'counterpart: not established')
        if target:
            parts.append('canonical pose: '+_readable({key:value for key,value in target.items()
                         if key not in ('piece_id', 'port_id')}))
    if 'image_key' in scope:
        parts.append('Image: '+_readable(scope['image_key']))
    if 'forbidden_transfer' in scope:
        parts.append(_readable(scope['forbidden_transfer']))
    handled = {'subject_id', 'rotation_ccw_degrees', 'construction_transposed',
               'counterpart_rotation_ccw_degrees', 'counterpart_reference_offset_m',
               'counterpart_reference_offset_tiles_en', 'counterpart', 'image_key',
               'forbidden_transfer', 'service_network', 'role', 'port_id', 'direction',
               'journey_id', 'entry_port', 'exit_port'}
    parts.extend(key.replace('_', ' ')+': '+_readable(value) for key,value in scope.items() if key not in handled)
    return '; '.join(parts) or 'Whole subject'


def _manual_service_label(scope):
    """Choose a browsing group without changing any exact stored case scope."""
    if 'forbidden_transfer' in scope:
        transfer = scope['forbidden_transfer']
        return ' → '.join(str(transfer.get(side+'_service') or 'Unspecified service')
                          for side in ('from', 'to'))
    if 'service_network' in scope:
        return str(scope['service_network'] or 'Unspecified service')
    return 'Images' if 'image_key' in scope else 'Whole subject'


def _manual_state_counts(cases, fingerprints=None):
    counts = Counter(case_state(case, fingerprints) for case in cases)
    return ', '.join(state.replace('_', ' ')+': '+str(counts[state]) for state in STATES if counts[state])


def _manual_attention_index(current, history, fingerprints):
    """Keep every current or historical failed/stale case outside disclosures."""
    rows = []
    for cases, coverage, inputs in ((current, 'Current', fingerprints),
                                     (history, 'Historical', None)):
        for case in cases:
            state = case_state(case, inputs)
            if state not in ('failed', 'stale'):
                continue
            scope = case['scope']
            orientation = str(scope['rotation_ccw_degrees'])+'°'+(' T' if scope.get('construction_transposed') else '') if 'rotation_ccw_degrees' in scope else 'General'
            label = _CHECK_NAMES.get(case['kind'], case['kind'])+' — '+_scope_label(scope)
            rows.append('| '+state+' | '+coverage+' | '+_md(label)+' | '+orientation+' | '
                        f'<a href="#case-{case["id"]}"><code>{case["id"]}</code></a> |')
    if not rows:
        return []
    return ['### Failed and stale cases', '',
            'These cases remain visible while the detailed groups are collapsed. Historical cases retain their stored dependency snapshots and are outside current coverage.', '',
            '| State | Coverage | Exact check / scope | Rotation | Case details |',
            '| --- | --- | --- | --- | --- |', *rows, '']


def render_manual_checklist(record, fingerprints=None, *, directory=None):
    """Render collapsible kind/service matrices and exact cases/observations.

    Rows group only identical non-orientation scope. Every rotation, transpose,
    neighbour, pose, service, and observation remains individually addressable.
    Failed and stale cases also appear outside the collapsed current groups.
    """
    record = _expanded_record(record)
    fingerprints = record['fingerprints'] if fingerprints is None else fingerprints
    summary = summarize_manual_record(record, fingerprints)
    current = [case for case in record['cases'] if case['kind'] != 'in_game_connection']
    orientations = sorted({(case['scope']['rotation_ccw_degrees'], bool(case['scope'].get('construction_transposed')))
                           for case in current if 'rotation_ccw_degrees' in case['scope']},
                          key=lambda item: (item[1], item[0]))
    headings = [str(angle)+'°'+(' T' if transpose else '') for angle, transpose in orientations]
    groups = {}
    pose_keys = {'rotation_ccw_degrees', 'construction_transposed', 'counterpart_rotation_ccw_degrees',
                 'counterpart_reference_offset_m', 'counterpart_reference_offset_tiles_en'}
    for case in current:
        scope = {key:value for key,value in case['scope'].items() if key not in pose_keys}
        key = (case['kind'], _json(scope))
        groups.setdefault(key, {'scope':scope, 'cases':[]})['cases'].append(case)
    history = {case['id']:case for case in record.get('removed_cases', [])}
    history.update({case['id']:case for case in record['cases']
                    if case['kind'] == 'in_game_connection' and _has_case_history(case)})
    lines = ['## Test checklist', '',
             'Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.', '',
             '**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.', '',
             record['rotation_policy'], '',
             'Current totals: '+', '.join(f'{state}: {summary["states"][state]}' for state in STATES)+'.', '']
    lines += _manual_attention_index(current, history.values(), fingerprints)
    if directory is not None:
        lines += _manual_workflow(directory, record)
    lines += ['### Detailed current checks', '',
              'Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.', '']
    sections = {}
    for (kind, _), group in groups.items():
        sections.setdefault((kind, _manual_service_label(group['scope'])), []).append(group)
    for (kind, service), scope_groups in sections.items():
        label = _CHECK_NAMES.get(kind, kind.replace('_', ' ').title())
        cases = [case for group in scope_groups for case in group['cases']]
        count = str(len(cases))+' case'+('s' if len(cases) != 1 else '')
        attention = any(case_state(case, fingerprints) in ('failed', 'stale') for case in cases)
        lines += ['<details open>' if attention else '<details>', '<summary>'+_md(label+' — '+service+' — '+count+'; '+_manual_state_counts(cases, fingerprints))+'</summary>', '',
                  '| Check / exact scope | '+ ' | '.join(['General', *headings])+' |',
                  '| --- | '+ ' | '.join('---' for _ in range(len(headings)+1))+' |']
        details = []
        for group in scope_groups:
            cells = {}
            for case in group['cases']:
                scope = case['scope']
                orientation = (scope['rotation_ccw_degrees'], bool(scope.get('construction_transposed'))) if 'rotation_ccw_degrees' in scope else None
                _require(orientation not in cells, 'Manual matrix would merge distinct cases')
                state = case_state(case, fingerprints)
                mark = '[x]' if state == 'passed' else ('N/A' if state == 'not_applicable' else '[ ]')
                cells[orientation] = f'<a href="#case-{case["id"]}">{mark} {state.replace("_", " ")}</a>'
            scope_label = _scope_label(group['scope'])
            lines.append('| **'+_md(label)+'**<br>'+_md(scope_label)+' | '+' | '.join(cells.get(item, '—') for item in [None, *orientations])+' |')
            attention = any(case_state(case, fingerprints) in ('failed', 'stale') for case in group['cases'])
            details += ['', '<details open>' if attention else '<details>', '<summary>'+_md(label+' — '+scope_label)+'</summary>', '']
            for case in group['cases']:
                details += _case_details(case, fingerprints)
            details += ['</details>', '']
        lines += ['', *details, '</details>', '']
    for legacy, title in ((True, 'Legacy connection history'), (False, 'Historical cases outside current coverage')):
        cases = [case for case in history.values() if (case['kind'] == 'in_game_connection') == legacy]
        if cases:
            lines += ['', '### '+title, '',
                      'These exact historical scopes, observations, and N/A declarations are retained as evidence. They do not count towards current required coverage or establish a complete-boundary join. Historical states use their stored dependency snapshots.', '']
            for case in cases:
                attention = case_state(case) in ('failed', 'stale')
                lines += ['<details open>' if attention else '<details>', '<summary>'+_md(_CHECK_NAMES.get(case['kind'], case['kind'])+' — '+_scope_label(case['scope']))+'</summary>', '']
                lines += _case_details(case)
                lines += ['</details>', '']
    return '\n'.join(lines)+'\n'


def _case_details(case, fingerprints=None):
    scope = case['scope']
    orientation = str(scope['rotation_ccw_degrees'])+'° CCW'+(' with construction Transpose' if scope.get('construction_transposed') else '') if 'rotation_ccw_degrees' in scope else 'General'
    lines = [f'<a id="case-{case["id"]}"></a>', '',
             '**'+orientation+': '+case_state(case, fingerprints).replace('_', ' ')+'** — `'+case['id']+'`.', '',
             case['description'], '', 'Scope: '+_scope_label(scope)+'.', '']
    pose = {key:scope[key] for key in ('counterpart_rotation_ccw_degrees', 'counterpart_reference_offset_m', 'counterpart_reference_offset_tiles_en') if key in scope}
    if pose:
        lines += ['Counterpart pose: '+_readable(pose)+'.', '']
    if case.get('missing_dependencies'):
        lines += ['Missing evidence dependencies: '+_readable(case['missing_dependencies'])+'.', '']
    if case.get('not_applicable_reason'):
        lines += ['Not applicable: '+case['not_applicable_reason'], '']
    if case.get('not_applicable_declaration'):
        lines += ['Declaration: '+_readable(case['not_applicable_declaration'])+'.', '']
    if case.get('observations'):
        lines += ['Recorded observations (chronological; the state above checks the relevant dependency snapshot):', '']
        lines += ['- '+_readable({key:value for key,value in observation.items() if key != 'dependency_fingerprint'})
                  for observation in case['observations']]
        lines += ['']
    else:
        lines += ['No observation recorded.', '']
    return lines


def render_connections(connections, *, piece_link=None, include_purpose=True):
    """Generate human connection/journey tables from the same machine record."""
    lines = ['## Connections and journeys', '']
    if include_purpose:
        lines += ['Purpose: describe intrinsic directional interfaces and permitted service journeys.', '']
    lines += [
             'Generated from [connections.json](connections.json). Coordinates are canonical east, north and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.', '',
             ('Supported placement states: '+', '.join(str(state['rotation_ccw_degrees'])+'° CCW'+(' with construction Transpose' if state.get('construction_transposed') else '') for state in connections.get('supported_orientations',[{'rotation_ccw_degrees':angle} for angle in ROTATIONS]))+'. Each state has its own declared manual scope.'), '',
             'A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.', '',
             'A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.json) for shared route-interface membership.', '',
             '| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |',
             '| --- | --- | --- | --- | --- |']
    for port in connections.get('ports', []):
        service = f'{port.get("service_network", "unresolved")} / {port.get("engine_transport", port.get("engine_transport_classes", []))} / {port.get("role", "primary")}'
        geometry = f'{port.get("endpoint_m", [])}; {port.get("tangent", [])}; {port.get("grade", "unresolved")}'
        lines.append(f'| `{port["id"]}` | {_md(service)} | {_md(port.get("direction", port.get("directions", [])))} | {_md(geometry)} | `{port.get("connection_class", "unresolved")}` |')
    lines += ['', '### Directed journeys', '', '| Service | Entry → exit | Role |', '| --- | --- | --- |']
    for journey in connections.get('journeys', []):
        lines.append(f'| {_md(journey.get("service_network", "unresolved"))} | `{journey.get("entry_port", journey.get("from_port"))}` → `{journey.get("exit_port", journey.get("to_port"))}` | {_md(journey.get("role", "primary"))} |')
    lines += ['', '### Forbidden transfers', '']
    transfers=connections.get('forbidden_transfers', [])
    if transfers:
        lines += ['| From service / port | To service / port | Reason |', '| --- | --- | --- |']
        ports={port['id']:port for port in connections.get('ports',[])}
        reasons={
            'not reachable in actual saved PATH graph': 'No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified.',
            'not reachable in actual saved assembly graph': 'No directed route exists between these ports in the saved assembly transport paths. In-game confirmation remains unverified.',
        }
        for transfer in transfers:
            ends=[]
            for side in ('from','to'):
                identifier=transfer.get(side+'_port')
                service=transfer.get(side+'_service') or ports.get(identifier,{}).get('service_network') or 'Unresolved service'
                ends.append(_md(service)+' / '+('`'+_md(identifier)+'`' if identifier else 'Unspecified port'))
            basis=transfer.get('reason') or transfer.get('basis')
            reason=reasons.get(basis,basis or 'No reason has been established; this transfer requires review.')
            lines.append('| '+' | '.join([*ends,_md(reason)])+' |')
    if not connections.get('forbidden_transfers'):
        lines.append('No additional forbidden-transfer cases are declared beyond the directed graph; no extra transfers are implied.')
    lines += ['', 'Review the test checklist for the exact tested cases and environments.', '']
    return '\n'.join(lines)


def _replace_generated(path, name, content, *, append=True):
    """Replace exactly one named block, leaving every authored byte outside it."""
    path = Path(path)
    text = path.read_text() if path.is_file() else ''
    start, end = f'<!-- BEGIN {name} -->', f'<!-- END {name} -->'
    block = start+'\n\n'+content.rstrip()+'\n\n'+end
    if start not in text and end not in text:
        if not append:
            return False
        text = text.rstrip()+'\n\n'+block+'\n'
    else:
        _require(text.count(start) == text.count(end) == 1 and text.index(start) < text.index(end),
                 name+' markers must be one ordered pair')
        before, tail = text.split(start, 1)
        _, after = tail.split(end, 1)
        text = before+block+after
    path.write_text(text)
    return True


def _remove_generated(path, name):
    """Remove a superseded generated block without removing authored prose."""
    path = Path(path)
    if not path.is_file():
        return False
    text = path.read_text()
    start, end = f'<!-- BEGIN {name} -->', f'<!-- END {name} -->'
    if start not in text and end not in text:
        return False
    _require(text.count(start) == text.count(end) == 1 and text.index(start) < text.index(end),
             name+' markers must be one ordered pair')
    before, tail = text.split(start, 1)
    _, after = tail.split(end, 1)
    path.write_text(before+after)
    return True


def _assembly_matrix_enabled(directory, subject):
    """Opt in only an assembly with its explicit README matrix marker pair."""
    if subject['kind'] != 'assembly':
        return False
    readme = Path(directory)/'README.md'
    if not readme.is_file():
        return False
    from .assembly_matrix import MARKER
    text = readme.read_text()
    start, end = f'<!-- BEGIN {MARKER} -->', f'<!-- END {MARKER} -->'
    if start not in text and end not in text:
        return False
    _require(text.count(start) == text.count(end) == 1 and text.index(start) < text.index(end),
             MARKER+' markers must be one ordered pair')
    return True


def update_manual_summary(path, record):
    """Replace or append the status block; preserve the authored guide."""
    summary = summarize_manual_record(record)
    target = 'TESTING.md#test-checklist' if record['subject']['kind'] == 'assembly' else '#test-checklist'
    rows = ['## Manual status', '', f'Generated from [the exact test cases]({target}) and [authoritative observations](checks/manual-tests.json).', '']
    labels = (('preview_review', 'Preview review'), ('in_game_render', 'In-game rendering'),
              ('in_game_journey', 'Directed journeys'))
    for kind, title in labels:
        counts = (summary.get('journey_coverage', summary['by_kind'].get(kind, {})) if kind == 'in_game_journey'
                  else summary['by_kind'].get(kind, {}))
        if not any(counts.values()):
            continue
        total = sum(counts.values())-counts.get('not_applicable', 0)
        passed = counts.get('passed', 0)
        if not total:
            rows.append(f'- {title}: all declared cases are explicitly N/A; no pass is implied.')
            continue
        rows.append(f'- [{"x" if total and passed == total else " "}] {title}: {passed}/{total} applicable cases passed; '
                    f'{counts.get("failed", 0)} failed, {counts.get("stale", 0)} stale.')
    expanded = _expanded_record(record)
    if any(case['kind'] == 'in_game_connection' and _has_case_history(case)
           for case in expanded['cases']+expanded.get('removed_cases', [])):
        history_target = 'TESTING.md#legacy-connection-history' if record['subject']['kind'] == 'assembly' else '#legacy-connection-history'
        rows += ['', f'[Legacy connection history]({history_target}) is retained separately and contributes no current required coverage.']
    rows += ['', 'These observations cover only the named services, directions, poses, rotations, and recorded platforms.']
    return _replace_generated(path, 'MANUAL SUMMARY', '\n'.join(rows))


def _piece_overview(directory, subject):
    from .design_review import review_label
    rows = [subject.get('description', ''), '', f'Exact reusable identifier: `{subject["id"]}`.', '']
    if subject.get('footprint'):
        width, depth = subject['footprint']
        rows += [f'Footprint: **{width} × {depth} tiles**. Exact menu name: **{subject.get("name", subject["id"])}**.', '']
    rows += ['Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.', '',
             '- [Connections and journeys](#connections-and-journeys)', '- [Test checklist](#test-checklist)', '']
    review = subject.get('design_review')
    if review:
        rows += ['### Design review', '', '**'+review_label(subject)+'** — '+review['summary'], '']
        rows += ['- '+reason for reason in review.get('reasons', [])]
        if review.get('evidence'):
            try:
                from .paths import project_root
                evidence = Path(os.path.relpath(project_root(directory)/review['evidence'], Path(directory).resolve())).as_posix()
                rows += ['', '[Design-review evidence]('+evidence+').']
            except ValueError:
                rows += ['', 'Evidence reference: `'+review['evidence']+'`.']
        rows += ['']
    if (Path(directory)/'preview.png').is_file():
        rows += [f'![{subject.get("name", subject["id"])}](preview.png)', '']
    if (Path(directory)/'preview-top.png').is_file():
        rows += [f'![{subject.get("name", subject["id"])} — top view](preview-top.png)', '']
    return '\n'.join(rows)


def piece_preview_hashes(directory):
    """Bind each delivered full-size piece image to its own review case."""
    directory = Path(directory)
    return {role: fingerprint((directory/name).read_bytes())
            for name, role in (('preview.png', 'canonical-southeast'),
                               ('preview-top.png', 'canonical-top'),
                               ('connection-overview.png', 'connection-overview'))
            if (directory/name).is_file()}


def subject_preview_hashes(directory, subject_kind):
    """Identify current delivered image roles without reading game resources."""
    if subject_kind == 'piece':
        return piece_preview_hashes(directory)
    _require(subject_kind == 'assembly', 'Subject kind must be piece or assembly')
    view_roles = {'preview.png': 'clean-southeast', 'overview-top.png': 'clean-top',
                  'named-southeast.png': 'named-southeast', 'named-northwest.png': 'named-northwest',
                  'named-top.png': 'named-top', 'tile-ownership.png': 'tile-ownership'}
    return {view_roles.get(path.name, path.stem): fingerprint(path.read_bytes())
            for path in sorted((Path(directory)/'previews').glob('*.png'))
            if not path.stem.endswith('-thumb')}


def refresh_image_reviews(record, preview_hashes):
    """Bind final images without regenerating any game or software case.

    Preserve raw non-image case objects, old dependency tables, observations,
    and meaningful removed-image history. Updated bytes make only the affected
    image's earlier observation stale; a new image never acquires a pass.
    """
    validate_manual_record(record)
    output = deepcopy(record)
    subject_id = output['subject']['id']
    images = {f'image:{subject_id}:{role}': digest for role, digest in _sha_map(preview_hashes).items()}
    output['fingerprints'].update(images)
    previous = _expanded_record(record)
    old_images = {case['id']: case for case in previous.get('removed_cases', [])
                  + previous['cases'] if case['kind'] == 'preview_review'}
    cases = [_new_case('preview_review', 'Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.',
                      {'subject_id': subject_id, 'image_key': key}, {key: digest})
             for key, digest in sorted(images.items())]
    if not cases:
        cases = [_new_case('preview_review', 'Supply and review a current complete model preview.',
                           {'subject_id': subject_id, 'image_key': None}, {})]
    for case in cases:
        if case['id'] in old_images:
            old = old_images[case['id']]
            case['observations'] = deepcopy(old.get('observations', []))
            for key in ('applicability', 'not_applicable_reason', 'not_applicable_declaration'):
                if key in old:
                    case[key] = deepcopy(old[key])
    current_ids = {case['id'] for case in cases}
    history = [deepcopy(case) for case in output.get('removed_cases', []) if case['id'] not in current_ids]
    historical_ids = {case['id'] for case in history}
    for case in output['cases']:
        if (case['kind'] == 'preview_review' and case['id'] not in current_ids
                and case['id'] not in historical_ids and _has_case_history(case)):
            history.append(deepcopy(case))
    # Compact only the new image cases. Existing raw case references and their
    # shared tables stay intact, including intentionally retired legacy data.
    generated = compact_manual_record({**previous, 'fingerprints': output['fingerprints'],
                                       'cases': cases, 'removed_cases': []})
    output.setdefault('dependency_sets', {}).update(generated['dependency_sets'])
    output['cases'] = [case for case in output['cases'] if case['kind'] != 'preview_review'] + generated['cases']
    if history:
        output['removed_cases'] = history
    else:
        output.pop('removed_cases', None)
    validate_manual_record(output)
    return output


def _write_subject_views(directory, subject, connections, record, piece_link=None):
    directory = Path(directory)
    readme = directory/'README.md'
    if not readme.is_file():
        title = subject.get('name', subject['id'])
        if subject['kind'] == 'piece':
            readme.write_text(f'# {title}\n\nPurpose: explain this reusable piece and its connections and test coverage.\n')
        else:
            readme.write_text(markdown_metadata(title, 'Explain this assembly, its connections, and its test coverage.',
                                                'players', 'guide')+f'# {title}\n')
    if subject['kind'] == 'piece':
        text = readme.read_text()
        metadata, body = split_markdown_metadata(text)
        # Exact legacy generated prefix only; authored examples appended outside
        # its summary are retained. Unknown authored openings are never erased.
        prefix = '\n'.join([f'# {subject.get("name", subject["id"])}', '', 'Purpose: explain this reusable type, show its exact preview and expose its connection and manual-test coverage.', '', subject.get('description', ''), '',
                 f'Exact reusable identifier: `{subject["id"]}`.', '',
                 '- [Connections and directed journeys](CONNECTIONS.md)', '- [Authoritative manual checks](checks/MANUAL_TESTS.md)', ''])
        if (directory/'preview.png').is_file():
            prefix += '\n'+f'![{subject.get("name", subject["id"])}](preview.png)'+'\n'
        if body.startswith(prefix):
            overview='<!-- BEGIN PIECE OVERVIEW -->\n\n'+_piece_overview(directory,subject).rstrip()+'\n\n<!-- END PIECE OVERVIEW -->\n\n'
            purpose = '' if re.search(r'(?m)^summary\s*:\s*\S', metadata) else 'Purpose: explain this reusable piece, its matching connections and current test coverage.\n\n'
            readme.write_text(metadata+f'# {subject.get("name", subject["id"])}\n\n'+purpose+overview+body[len(prefix):].lstrip('\n'))
        _replace_generated(readme, 'PIECE OVERVIEW', _piece_overview(directory, subject))
    matrix_enabled = _assembly_matrix_enabled(directory, subject)
    if matrix_enabled:
        from .assembly_matrix import MARKER, render_assembly_connection_matrix
        _remove_generated(readme, 'MANUAL SUMMARY')
        _remove_generated(readme, 'CONNECTIONS')
        _replace_generated(readme, MARKER, render_assembly_connection_matrix(connections, record), append=False)
    else:
        update_manual_summary(readme, record)
        _replace_generated(readme, 'CONNECTIONS', render_connections(connections, piece_link=piece_link,
                                                                   include_purpose=subject['kind'] == 'piece'))
    testing = directory/'TESTING.md' if subject['kind'] == 'assembly' else readme
    if not testing.is_file():
        title = f'Testing: {subject["id"]}'
        testing.write_text(markdown_metadata(title, 'Inspect this assembly’s exact checks, resource evidence, and explicit human observations.',
                                             'contributors', 'reference')+f'# {title}\n')
    if matrix_enabled:
        _replace_generated(testing, 'CONNECTIONS', render_connections(connections, piece_link=piece_link,
                                                                    include_purpose=False))
    _replace_generated(testing, 'MANUAL CHECKS', render_manual_checklist(record, directory=directory))
    for obsolete in (directory/'CONNECTIONS.md', directory/'checks/MANUAL_TESTS.md', directory/'checks/README.md'):
        obsolete.unlink(missing_ok=True)


def write_subject_content(directory, subject, connections, fingerprints, *, preview_hashes=None,
                          write_readme=False, piece_link=None, refresh_metadata=True):
    """Write portable metadata and compact views; never record a human pass.

    ``write_readme`` remains accepted for callers; authored README content is
    always preserved while the named generated blocks are refreshed.
    """
    directory = Path(directory)
    checks = directory/'checks'
    checks.mkdir(parents=True, exist_ok=True)
    record_path = checks/'manual-tests.json'
    matrix_enabled = _assembly_matrix_enabled(directory, subject)
    if not refresh_metadata:
        _require(record_path.is_file(), 'No authoritative manual record for '+subject['id'])
        generated=json.loads(record_path.read_text())
        validate_manual_record(generated)
    else:
        generated = new_manual_record(subject['id'], subject['kind'], connections, fingerprints, preview_hashes,
                                      split_journey_observations=matrix_enabled)
        if record_path.exists():
            generated = refresh_manual_record(json.loads(record_path.read_text()), generated)
        (directory/'connections.json').write_text(json.dumps(connections, indent=2, allow_nan=False)+'\n')
        record_path.write_text(json.dumps(compact_manual_record(generated), indent=2, allow_nan=False)+'\n')
    _write_subject_views(directory, subject, connections, generated, piece_link)
    return {'subject': generated['subject'], 'summary': summarize_manual_record(generated),
            'files': ['connections.json', 'README.md', 'checks/manual-tests.json', 'checks/observation.example.json']+
                     (['TESTING.md'] if subject['kind'] == 'assembly' else [])}


def declare_not_applicable(record, case_id, *, explicit_user_confirmation, reviewer,
                           confirmed_at, reason):
    """Declare an exact case inapplicable without counting it as a pass."""
    _require(explicit_user_confirmation is True, 'Explicit user confirmation is required')
    _require(isinstance(reason,str) and reason.strip(), 'Not-applicable checks need an explicit reason')
    _require(isinstance(reviewer,str) and reviewer.strip(), 'A declaration needs a reviewer')
    try:datetime.fromisoformat(confirmed_at.replace('Z','+00:00'))
    except (ValueError,AttributeError) as error:raise ValueError('Declaration date must be ISO-8601') from error
    output=_expanded_record(record);case=_find_case(output,case_id)
    case['applicability']='not_applicable';case['not_applicable_reason']=reason
    case['not_applicable_declaration']={'authority':'user','confirmation_method':'explicit_user_confirmation',
                                      'reviewer':reviewer,'confirmed_at':confirmed_at,'reason':reason}
    validate_manual_record(output)
    return output


def record_observation_file(record_path, observation_path):
    """Apply one user-authored observation file and refresh only its derived views."""
    record_path,observation_path=Path(record_path),Path(observation_path)
    record=json.loads(record_path.read_text());request=json.loads(observation_path.read_text())
    common={key:request.get(key) for key in ('explicit_user_confirmation','reviewer','confirmed_at')}
    if request.get('result')=='not_applicable':
        output=declare_not_applicable(record,request['case_id'],reason=request.get('reason'),**common)
    else:
        output=record_user_result(record,request['case_id'],request.get('result'),evidence=request.get('evidence',[]),
                                  environment=request.get('environment'),note=request.get('note',''),**common)
    record_path.write_text(json.dumps(compact_manual_record(output),indent=2,allow_nan=False)+'\n')
    directory=record_path.parent.parent
    readme=directory/'README.md'
    if _assembly_matrix_enabled(directory, output['subject']):
        connections = json.loads((directory/'connections.json').read_text())
        _write_subject_views(directory, output['subject'], connections, output)
    else:
        if readme.is_file():update_manual_summary(readme,output)
        testing=directory/'TESTING.md' if output['subject']['kind']=='assembly' else readme
        _replace_generated(testing,'MANUAL CHECKS',render_manual_checklist(output,directory=directory))
    for obsolete in (record_path.parent/'MANUAL_TESTS.md',record_path.parent/'README.md'):
        obsolete.unlink(missing_ok=True)
    refreshed = False
    try:
        from .paths import project_root
        from .inventory import write_inventories
        root = project_root(record_path)
    except ValueError:
        root = None
    if root is not None:
        write_inventories(root);refreshed = True
    return {'subject':output['subject'],'case_id':request['case_id'],
            'state':case_state(_find_case(output,request['case_id'])),
            'authority':'explicit_user_observation','inventory_refresh_required':not refreshed}


def _manual_workflow(directory, record):
    """Return a short local command; shared recording instructions live once."""
    candidates = [case for case in record['cases'] if case['kind'] in MANUAL_KINDS
                  and case['kind'] != 'in_game_connection']
    if not candidates:
        return []
    checks=Path(directory)/'checks'
    checks.mkdir(parents=True, exist_ok=True)
    example=next((case for case in candidates if case['kind'] in JOURNEY_KINDS), candidates[0])
    request={'purpose':'Copy this template to a separate observation file and fill it only after the user confirms the exact case.',
             'case_id':example['id'],'result':'passed','explicit_user_confirmation':False,
             'reviewer':'','confirmed_at':'','evidence':[],
             'environment':{'platform':'','game_version':'','nam_profile':''},'note':''}
    example_path=checks/'observation.example.json'
    # Keep an existing user-facing example stable during prose-only refreshes.
    if not example_path.is_file() or json.loads(example_path.read_text()).get('case_id') not in {case['id'] for case in candidates}:
        example_path.write_text(json.dumps(request,indent=2)+'\n')
    try:
        from .paths import project_root
        source_root=project_root(directory)
        relative=checks.resolve().relative_to(source_root.parent).as_posix()
        guide=Path(os.path.relpath(source_root/'docs/TESTING.md',Path(directory).resolve())).as_posix()
        location=f'From the repository folder containing `{source_root.name}`, run after filling `checks/observation.json` and explicitly confirming the exact observation:'
        command='python3 -m scp.content record --record '+shlex.quote(relative+'/manual-tests.json')+' --observation '+shlex.quote(relative+'/observation.json')
    except ValueError:
        guide='docs/TESTING.md'
        location='From this subject folder, run after filling `checks/observation.json` and explicitly confirming the exact observation:'
        command='python3 -m scp.content record --record checks/manual-tests.json --observation checks/observation.json'
    return ['### Record an observation', '',
            f'Follow the [shared testing guide]({guide}); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.', '',
            location, '', '```sh', command, '```', '']


def main():
    import argparse
    parser=argparse.ArgumentParser(description='Record one explicitly confirmed user observation; never infer manual passes.')
    sub=parser.add_subparsers(dest='command',required=True)
    command=sub.add_parser('record')
    command.add_argument('--record',required=True,type=Path)
    command.add_argument('--observation',required=True,type=Path)
    refresh=sub.add_parser('refresh',help='Regenerate views from current portable metadata; does not verify changed DATs')
    refresh.add_argument('--root',required=True,type=Path)
    retire=sub.add_parser('retire-connections',help='Retire legacy endpoint cases without resource extraction or regenerating remaining cases')
    retire.add_argument('--root',required=True,type=Path)
    retire.add_argument('--piece',action='append',default=[])
    retire.add_argument('--assembly',action='append',default=[])
    retire.add_argument('--all',dest='all_subjects',action='store_true')
    images=sub.add_parser('refresh-images',help='Bind current delivered images without extracting resources or changing game cases')
    images.add_argument('--root',required=True,type=Path)
    images.add_argument('--piece',action='append',default=[])
    images.add_argument('--assembly',action='append',default=[])
    images.add_argument('--all',dest='all_subjects',action='store_true')
    args=parser.parse_args()
    if args.command == 'record':
        result=record_observation_file(args.record,args.observation)
    elif args.command == 'retire-connections':
        result=retire_connection_cases_in_catalog(args.root,piece_ids=args.piece,
            assembly_ids=args.assembly,all_subjects=args.all_subjects)
    elif args.command == 'refresh-images':
        result=refresh_image_reviews_in_catalog(args.root,piece_ids=args.piece,
            assembly_ids=args.assembly,all_subjects=args.all_subjects)
    else:
        result=refresh_catalog_content(args.root)
    print(json.dumps(result,indent=2))



def retire_connection_cases_in_catalog(root, *, piece_ids=None, assembly_ids=None, all_subjects=False):
    """Retire selected legacy checklists using existing records only.

    Preflight the entire selection before writing. Resource measurements,
    retained case objects, dependencies, and other subjects remain untouched.
    """
    from .catalog import load_catalog
    root=Path(root).resolve();catalog=load_catalog(root)
    pieces={piece['id']:piece for piece in catalog['pieces']}
    assemblies={item['id']:item for item in catalog.get('_assemblies', [])}
    selected_pieces=set(piece_ids or ());selected_assemblies=set(assembly_ids or ())
    _require(type(all_subjects) is bool, 'all_subjects must be a boolean')
    _require(not (all_subjects and (selected_pieces or selected_assemblies)), 'Choose --all or explicit subject selectors')
    _require(all_subjects or selected_pieces or selected_assemblies, 'Select --all, --piece, or --assembly explicitly')
    _require(selected_pieces <= pieces.keys(), 'Unknown piece selection: '+', '.join(sorted(selected_pieces-pieces.keys())))
    _require(selected_assemblies <= assemblies.keys(), 'Unknown assembly selection: '+', '.join(sorted(selected_assemblies-assemblies.keys())))
    if all_subjects:
        selected_pieces=set(pieces);selected_assemblies=set(assemblies)
    selected=[(root/catalog['domains'][pieces[key]['domain']]['path']/'00_pieces'/key,
               {**pieces[key],'kind':'piece'}) for key in sorted(selected_pieces)]
    selected += [(root/assemblies[key]['path'],{'id':key,'kind':'assembly'}) for key in sorted(selected_assemblies)]
    pending=[];skipped=[]
    for directory,subject in selected:
        path=directory/'checks/manual-tests.json'
        if not path.is_file():
            skipped.append(subject['id']);continue
        previous=json.loads(path.read_text())
        _require(previous['subject']=={'id':subject['id'],'kind':subject['kind']}, 'Manual record belongs to another subject: '+subject['id'])
        output=retire_connection_cases(previous)
        connections=json.loads((directory/'connections.json').read_text())
        pending.append((directory,subject,path,previous,output,connections))
    results=[]
    for directory,subject,path,previous,output,connections in pending:
        if output != previous:
            path.write_text(json.dumps(output,indent=2,allow_nan=False)+'\n')
        _write_subject_views(directory,subject,connections,output)
        results.append({'subject':output['subject'],
            'retired':len(previous['cases'])-len(output['cases']),
            'archived':len(output.get('removed_cases', []))-len(previous.get('removed_cases', [])),
            'record_changed':output != previous})
    return {'subjects':results,'skipped_missing_records':skipped,'resource_extraction':False,
            'inventory_refresh_required':bool(results),'installed_plugins_changed':False}


def refresh_image_reviews_in_catalog(root, *, piece_ids=None, assembly_ids=None, all_subjects=False):
    """Explicitly attach final image hashes to selected existing manual records.

    Preflight the full selection before writing. This is deliberately separate
    from prose refresh, actual-resource extraction, and compatibility discovery.
    """
    from .catalog import load_catalog
    root = Path(root).resolve()
    catalog = load_catalog(root)
    pieces = {piece['id']: piece for piece in catalog['pieces']}
    assemblies = {item['id']: item for item in catalog.get('_assemblies', [])}
    selected_pieces, selected_assemblies = set(piece_ids or ()), set(assembly_ids or ())
    _require(type(all_subjects) is bool, 'all_subjects must be a boolean')
    _require(not (all_subjects and (selected_pieces or selected_assemblies)), 'Choose --all or explicit subject selectors')
    _require(all_subjects or selected_pieces or selected_assemblies, 'Select --all, --piece, or --assembly explicitly')
    _require(selected_pieces <= pieces.keys(), 'Unknown piece selection: '+', '.join(sorted(selected_pieces-pieces.keys())))
    _require(selected_assemblies <= assemblies.keys(), 'Unknown assembly selection: '+', '.join(sorted(selected_assemblies-assemblies.keys())))
    if all_subjects:
        selected_pieces, selected_assemblies = set(pieces), set(assemblies)
    selected = [(root/catalog['domains'][pieces[key]['domain']]['path']/'00_pieces'/key,
                 {**pieces[key], 'kind': 'piece'}) for key in sorted(selected_pieces)]
    selected += [(root/assemblies[key]['path'], {'id': key, 'kind': 'assembly'})
                 for key in sorted(selected_assemblies)]
    pending, skipped = [], []
    for directory, subject in selected:
        path = directory/'checks/manual-tests.json'
        if not path.is_file():
            _require(all_subjects, 'Extract this subject before binding its images: '+subject['id'])
            skipped.append(subject['id'])
            continue
        previous = json.loads(path.read_text())
        _require(previous['subject'] == {'id': subject['id'], 'kind': subject['kind']},
                 'Manual record belongs to another subject: '+subject['id'])
        connections = json.loads((directory/'connections.json').read_text())
        images = subject_preview_hashes(directory, subject['kind'])
        output = refresh_image_reviews(previous, images)
        pending.append((directory, subject, path, previous, output, connections, images))
    results = []
    for directory, subject, path, previous, output, connections, images in pending:
        if output != previous:
            path.write_text(json.dumps(output, indent=2, allow_nan=False)+'\n')
        _write_subject_views(directory, subject, connections, output)
        results.append({'subject': output['subject'], 'image_roles': sorted(images),
                        'record_changed': output != previous, 'summary': summarize_manual_record(output)})
    return {'subjects': results, 'skipped_missing_records': skipped, 'resource_extraction': False,
            'compatibility_discovery': False, 'manual_observations_added': 0,
            'game_and_software_cases_changed': False, 'inventory_refresh_required': bool(results),
            'installed_plugins_changed': False}


def refresh_catalog_content(root, *, records=None, changed_piece_ids=None, scope_to_changed=False):
    """Refresh all views from portable metadata; this does not verify new DATs.

    A build/source extractor supplies records after actual resource changes.
    Without records, only derived views are refreshed. Explicit changed IDs
    scope metadata writes to those pieces and assemblies using them; cached
    records supply read-only assembly context. Omit changed IDs for a full
    refresh. Drafts without extracted records are skipped.

    Opt-in scope_to_changed reads and refreshes only the changed pieces. It
    reports affected assemblies and global class/inventory views as deferred,
    without reading their existing records or any unselected piece records.
    """
    from .catalog import load_catalog
    from .connectivity import assembly_connectivity
    from .inventory import write_inventories
    root=Path(root).resolve();catalog=load_catalog(root)
    pieces={piece['id']:piece for piece in catalog['pieces']}
    piece_directories={identifier:root/catalog['domains'][piece['domain']]['path']/'00_pieces'/identifier
                       for identifier,piece in pieces.items()}
    metadata_refresh=records is not None
    known={} if records is None else dict(records)
    _require(known.keys() <= pieces.keys(), 'Extracted records contain unregistered pieces')
    changed=set(pieces) if changed_piece_ids is None else set(changed_piece_ids)
    _require(not scope_to_changed or changed_piece_ids is not None,
             'Scoped refresh requires explicit changed piece IDs')
    _require(changed <= pieces.keys(), 'Changed piece IDs contain unregistered pieces')
    if metadata_refresh and changed_piece_ids is not None:
        _require(changed <= known.keys(), 'Every changed piece needs a freshly extracted record')
    assemblies=catalog.get('_assemblies',[])
    needed=set(pieces)
    deferred_assembly_ids=[]
    if scope_to_changed:
        deferred_assembly_ids=sorted(assembly['id'] for assembly in assemblies if changed & {
            item['piece_id'] for item in assembly['scene'].get('placements',assembly['scene'].get('instances',[]))})
        assemblies=[]
        needed=changed
        known={identifier:record for identifier,record in known.items() if identifier in needed}
    skipped=[]
    for identifier,piece in pieces.items():
        if identifier not in needed:
            continue
        if identifier not in known:
            file=piece_directories[identifier]/'connections.json'
            if file.is_file():
                known[identifier]=json.loads(file.read_text())
            else:
                skipped.append(identifier)
    subjects=[]
    for identifier in sorted(changed & known.keys()):
        piece=pieces[identifier];directory=piece_directories[identifier]
        if not metadata_refresh and not (directory/'checks/manual-tests.json').is_file():
            skipped.append(identifier);continue
        images=piece_preview_hashes(directory)
        subjects.append(write_subject_content(directory,{**piece,'kind':'piece'},known[identifier],
                            known[identifier].get('source',{}).get('resource_fingerprints',{}),
                            preview_hashes=images,write_readme=True,refresh_metadata=metadata_refresh))
    assembly_results=[]
    for assembly in assemblies:
        directory=root/assembly['path']
        placements=assembly['scene'].get('placements',assembly['scene'].get('instances',[]))
        dependencies={item['piece_id'] for item in placements}
        if changed_piece_ids is not None and not (dependencies & changed):
            continue
        if metadata_refresh and not dependencies <= known.keys():
            skipped.append(assembly['id']);continue
        if not metadata_refresh and not all((directory/name).is_file() for name in ('connections.json','checks/manual-tests.json')):
            skipped.append(assembly['id']);continue
        record=(assembly_connectivity(assembly['id'],assembly['scene'],known,pieces) if metadata_refresh else
                json.loads((directory/'connections.json').read_text()))
        images=subject_preview_hashes(directory, 'assembly')
        assembly_results.append(write_subject_content(directory,{'id':assembly['id'],'kind':'assembly'},record,
            record.get('source',{}).get('resource_fingerprints',{}),preview_hashes=images,
            write_readme=False,refresh_metadata=metadata_refresh))
    for slug,domain in catalog['domains'].items():
        if scope_to_changed or not metadata_refresh or not any(pieces[key]['domain']==slug for key in changed):
            continue
        classes={}
        for identifier,piece in pieces.items():
            if piece['domain']!=slug or identifier not in known:continue
            for port in known[identifier]['ports']:
                classes.setdefault(port['connection_class'],{'ports':[],
                    'physical_profile_status':'unreviewed; membership alone establishes no game result'})['ports'].append(
                    {'piece_id':identifier,'port_id':port['id']})
        file=root/domain['path']/'connection-classes.json'
        file.write_text(json.dumps({'schema_version':1,
            'purpose':'Shared classes derived from actual encoded route interfaces; membership does not establish physical fit or game compatibility.',
            'classes':classes},indent=2)+'\n')
    deferred=({'inventory_refresh_required':bool(subjects or assembly_results),
               'connection_classes_refresh_required':bool(metadata_refresh and subjects),
               'deferred_assembly_ids':deferred_assembly_ids} if scope_to_changed else {})
    return {**deferred, 'pieces':len(subjects),'assemblies':len(assembly_results),
            'ports':sum(len(value['ports']) for value in known.values()),
            'journeys':sum(len(value['journeys']) for value in known.values()),
            'case_count':sum(item['summary']['total'] for item in subjects+assembly_results),
            'changed_piece_ids':sorted(changed & known.keys()),'skipped_missing_records':sorted(set(skipped)),
            'all_new_manual_cases_unverified':all(
                sum(counts.values())==counts.get('unverified',0)
                for item in subjects+assembly_results
                for kind,counts in item['summary']['by_kind'].items() if kind in MANUAL_KINDS),
            'inventory':{} if scope_to_changed else write_inventories(root),'installed_plugins_changed':False}

if __name__=='__main__':main()
