"""Reader-facing assembly movement evidence, enabled by an explicit README block."""
from html import escape


ASSEMBLY_CONNECTION_MATRIX = 'ASSEMBLY CONNECTION MATRIX'
MARKER = ASSEMBLY_CONNECTION_MATRIX


def _text(value):
    return escape(str(value), quote=False).replace('|', '&#124;').replace('\n', ' ')


def _port_label(port):
    identifier = port['id']
    network = port.get('service_network', 'unresolved')
    network_name = {'hsr': 'HSR', 'ghsr': 'GHSR', 'monorail': 'Monorail', 'road': 'Road',
                    'tram': 'Tram', 'pedestrians': 'Pedestrians'}.get(network, network)
    explicit_label = next((port[key] for key in ('display_label', 'display_name', 'name', 'label')
                           if isinstance(port.get(key), str) and port[key].strip()), None)
    cardinal, separator, suffix = identifier.partition('.')
    direction = {'in': 'entrance', 'out': 'exit'}.get(port.get('direction'), 'port')
    cardinal_name = {'N': 'North', 'E': 'East', 'S': 'South', 'W': 'West'}.get(cardinal)
    friendly = explicit_label or (f'{cardinal_name} {direction}'
                                  if cardinal_name and separator and suffix == port.get('direction') else identifier)
    label = f'**{_text(network_name)} · {_text(friendly)}**<br>`{_text(identifier)}`'
    if port.get('variant') and port['variant'] != network:
        label += f'<br>Variant: {_text(port["variant"])}'
    if port.get('role', 'primary') != 'primary':
        label += f'<br>Role: {_text(port["role"])}'
    return label


def _orientation_key(scope):
    return (scope.get('rotation_ccw_degrees'), bool(scope.get('construction_transposed', False)))


def _manual_states(connections, record):
    states = record.get('manual_check_orientations')
    if states is None:
        states = connections.get('supported_orientations', record.get('supported_orientations'))
    if states is None:
        return [(angle, False) for angle in (0, 90, 180, 270)]
    keys = [_orientation_key(state) for state in states]
    if (not keys or len(set(keys)) != len(keys)
            or any(type(angle) is not int or angle not in (0, 90, 180, 270) for angle, _ in keys)):
        raise ValueError('Matrix requires unique declared proper orientation states')
    return keys


def _linked(label, cases):
    if not cases:
        return label
    return f'[{label}](TESTING.md#case-{cases[0]["id"]})'


def _coverage(cases, states, fingerprints):
    """Summarize exact required cases; details remain in the linked testing record."""
    from .content import case_state

    by_state = {}
    for case in cases:
        key = _orientation_key(case['scope'])
        if key in states:
            by_state.setdefault(key, []).append(case)
    current = []
    incomplete = False
    for state in states:
        matches = by_state.get(state, [])
        if len(matches) != 1:
            incomplete = True
        current.extend(matches)
    values = [case_state(case, fingerprints) for case in current]
    label = '❌' if 'failed' in values else '✅' if not incomplete and all(value == 'passed' for value in values) else '?'
    # Open a current failing/pending case before an unrelated successful one.
    order = {'failed': 0, 'stale': 1, 'unverified': 2, 'not_applicable': 3, 'passed': 4}
    current.sort(key=lambda case: order.get(case_state(case, fingerprints), 5))
    return _linked(label, current)


def _software_path_status(connections, record, fingerprints):
    from .content import case_state

    subject_id = record['subject']['id']
    cases = [case for case in record['cases'] if case['kind'] == 'software_connectivity'
             and case.get('scope', {}).get('subject_id') == subject_id]
    extraction = connections.get('software_status', {}).get('path_extraction', 'unverified')
    if len(cases) != 1:
        failed = extraction == 'failed' or any(case_state(case, fingerprints) == 'failed' for case in cases)
        return _linked('❌' if failed else '?', cases), False
    case = cases[0]
    state = case_state(case, fingerprints)
    # A nominal check without the graph dependency cannot prove this movement set.
    if f'graph:{subject_id}' not in case.get('dependencies', {}):
        return _linked('❌' if state == 'failed' or extraction == 'failed' else '?', cases), False
    passed = state == extraction == 'passed'
    symbol = '❌' if state == 'failed' or extraction == 'failed' else '✅' if passed else '?'
    return _linked(symbol, cases), passed


def _journeys_for_pair(connections, entrance, exit_port):
    result = []
    for journey in connections.get('journeys', []):
        if (journey.get('entry_port', journey.get('from_port')) != entrance['id']
                or journey.get('exit_port', journey.get('to_port')) != exit_port['id']):
            continue
        service, role = journey.get('service_network'), journey.get('role', 'primary')
        if (service is None or service != entrance.get('service_network')
                or service != exit_port.get('service_network')
                or role != entrance.get('role', 'primary') or role != exit_port.get('role', 'primary')):
            continue
        if 'variant' in journey and any(port.get('variant') != journey['variant'] for port in (entrance, exit_port)):
            continue
        result.append(journey)
    return result


def _journey_cases(record, journey, kind):
    required = {'subject_id': record['subject']['id'], 'journey_id': journey['id'],
                'service_network': journey.get('service_network'), 'role': journey.get('role', 'primary'),
                'entry_port': journey.get('entry_port', journey.get('from_port')),
                'exit_port': journey.get('exit_port', journey.get('to_port'))}
    return [case for case in record['cases'] if case['kind'] == kind
            and all(case.get('scope', {}).get(key) == value for key, value in required.items())]


def _forbidden_pair(connections, entrance, exit_port):
    return any(item.get('from_port') == entrance['id'] and item.get('to_port') == exit_port['id']
               and item.get('from_service', entrance.get('service_network')) == entrance.get('service_network')
               and item.get('to_service', exit_port.get('service_network')) == exit_port.get('service_network')
               for item in connections.get('forbidden_transfers', []))


def _forbidden_cases(record, connections, entrance, exit_port):
    transfers = [item for item in connections.get('forbidden_transfers', [])
                 if item.get('from_port') == entrance['id'] and item.get('to_port') == exit_port['id']
                 and item.get('from_service', entrance.get('service_network')) == entrance.get('service_network')
                 and item.get('to_service', exit_port.get('service_network')) == exit_port.get('service_network')]
    return [case for case in record['cases'] if case['kind'] == 'in_game_forbidden_transfer'
            and case.get('scope', {}).get('subject_id') == record['subject']['id']
            and case.get('scope', {}).get('forbidden_transfer') in transfers]


def render_assembly_connection_matrix(connections, record):
    """Render declared entry/exit movements without inferring compatible neighbours."""
    from .content import _expanded_record, connectivity_fingerprints

    record = _expanded_record(record)
    subject_id = record.get('subject', {}).get('id')
    if record.get('subject', {}).get('kind') != 'assembly' or connections.get('subject_id', subject_id) != subject_id:
        raise ValueError('Assembly matrix inputs must describe the same assembly')
    fingerprints = dict(record.get('fingerprints', {}))
    fingerprints.update(connections.get('source', {}).get('resource_fingerprints', {}))
    fingerprints.update(connectivity_fingerprints(subject_id, connections))
    states = _manual_states(connections, record)
    entrances = [port for port in connections.get('ports', []) if port.get('direction') == 'in']
    exits = [port for port in connections.get('ports', []) if port.get('direction') == 'out']
    identifiers = [port['id'] for port in connections.get('ports', [])]
    if len(set(identifiers)) != len(identifiers):
        raise ValueError('Matrix port identifiers must be unique')
    appearance_cases = [case for case in record['cases'] if case['kind'] == 'in_game_render'
                        and case.get('scope', {}).get('subject_id') == subject_id
                        and not any(key in case.get('scope', {}) for key in ('journey_id', 'service_network', 'role'))]
    appearance = _coverage(appearance_cases, states, fingerprints)
    path_status, _ = _software_path_status(connections, record, fingerprints)
    lines = ['## Connection matrix', '',
             'Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.', '',
             f'**Game appearance:** {appearance} — the complete assembly’s appearance in the game, checked separately from its journeys.', '',
             '**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [TESTING](TESTING.md#test-checklist).', '']
    if not entrances or not exits:
        lines += ['No directional entrance/exit matrix is declared for this assembly.', '']
        return '\n'.join(lines)
    lines += ['| Entrance ↓ / Exit → | ' + ' | '.join(_port_label(port) for port in exits) + ' |',
              '| --- | ' + ' | '.join('---' for _ in exits) + ' |']
    for entrance in entrances:
        cells = []
        for exit_port in exits:
            journeys = _journeys_for_pair(connections, entrance, exit_port)
            forbidden = _forbidden_pair(connections, entrance, exit_port)
            if journeys and forbidden:
                raise ValueError('A matrix movement is both permitted and forbidden')
            parts = []
            if journeys:
                for journey in journeys:
                    if len(journeys) > 1:
                        parts.append(f'Journey: `{_text(journey["id"])}`')
                    query = _coverage(_journey_cases(record, journey, 'in_game_route_query'), states, fingerprints)
                    travel = _coverage(_journey_cases(record, journey, 'in_game_visible_travel'), states, fingerprints)
                    travel_label = 'Visible train travel' if journey.get('service_network') in ('hsr', 'ghsr') else 'Visible travel'
                    parts += [f'**Saved PATH:** {path_status}', f'**Route Query:** {query}', f'**{travel_label}:** {travel}']
            elif forbidden:
                negative = _coverage(_forbidden_cases(record, connections, entrance, exit_port), states, fingerprints)
                parts = ['**Forbidden**', f'**Saved PATH:** {path_status}', f'In-game check: {negative}']
            else:
                parts = ['**Saved PATH:** ?', '**Route Query:** ?', '**Visible travel:** ?']
            cells.append('<br>'.join(parts))
        lines.append('| ' + _port_label(entrance) + ' | ' + ' | '.join(cells) + ' |')
    lines += ['', 'Source: [connections.json](connections.json).', '']
    return '\n'.join(lines)
