"""Load accepted parallel-diamond measurements for the shared connector engine.

The owning assembly stores decoded measurement facts, never proprietary PATH
payloads or resource-writer expectations. This adapter adds no route parser and
does not establish neighbouring compatibility or a human game observation.
"""
from __future__ import annotations

from copy import deepcopy
import math
from pathlib import Path
import re

from scp import jsonc
from scp.dbpf import require

ROOT = Path(__file__).resolve().parents[4]
REFERENCE = ('domains/highway/01_assemblies/'
             'ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/'
             'checks/accepted-connector-contracts.jsonc')
PREFIX = 'highway_ddrhw_parallel_'
_SHA = re.compile(r'[0-9a-f]{64}\Z')


def load_contracts(root=ROOT):
    """Read complete accepted facts without loading an ignored compiled build.

    Missing evidence is allowed during first implementation; it supplies no
    reviewed contract. Once authored, malformed or partial evidence fails.
    """
    path = Path(root) / REFERENCE
    if not path.is_file():
        return {}
    evidence = jsonc.load(path)
    require(evidence.get('schema_version') == 1
            and evidence.get('state') == 'accepted-independently-checked-saved-resources'
            and evidence.get('game_operation') == 'unverified',
            'Parallel connector measurements are not accepted saved-resource evidence')
    require(_SHA.fullmatch(evidence.get('source', {}).get('manifest_sha256', '')),
            'Parallel connector evidence lacks its accepted manifest fingerprint')
    contracts = deepcopy(evidence.get('contracts', {}))
    require(len(contracts) == 15 and all(recipe.startswith(PREFIX) for recipe in contracts),
            'Parallel connector evidence must cover all fifteen reusable types')
    for recipe, facts in contracts.items():
        cells = {tuple(cell) for cell in facts['cells']}
        hashes = facts['path_hashes_by_cell']
        require(len(cells) == len(facts['cells'])
                and len(hashes) == len(cells)
                and {tuple(cell) for cell, _digest in hashes} == cells
                and all(_SHA.fullmatch(digest) for _cell, digest in hashes),
                recipe + ': accepted canonical PATH fingerprints do not cover every owned cell')
        ports = {port['id']: port for port in facts['ports']}
        channels = {channel['id']: channel for channel in facts['channels']}
        components = {component['id']: component for component in facts['components']}
        require(ports and len(ports) == len(facts['ports'])
                and channels and len(channels) == len(facts['channels'])
                and components and len(components) == len(facts['components']),
                recipe + ': accepted connector identities are missing or duplicated')
        covered = []
        for channel in channels.values():
            require(channel['component_id'] in components and channel['ports'],
                    recipe + ': accepted physical channel has no owning component or ports')
            covered.extend(channel['ports'])
        require(len(covered) == len(set(covered)) and set(covered) == set(ports),
                recipe + ': physical channels do not cover each measured port exactly once')
        for port in ports.values():
            require(tuple(port['source_cell']) in cells and port['edge'] in range(4)
                    and port['direction'] in ('in', 'out') and port['engine_transport'] in (1, 2)
                    and port['channel_id'] in channels
                    and port['id'] in channels[port['channel_id']]['ports']
                    and math.isfinite(port['grade'])
                    and len(port['endpoint_m']) == 3
                    and all(math.isfinite(value) for value in port['endpoint_m']),
                    recipe + ': invalid accepted boundary measurement')
            for key in ('tangent', 'sampled_tangent'):
                require(len(port[key]) == 2 and all(math.isfinite(value) for value in port[key])
                        and abs(math.hypot(*port[key]) - 1.) <= 1e-9,
                        recipe + ': invalid accepted travel tangent')
        for key in ('movements', 'forbidden_transfers'):
            pairs = [tuple(pair) for pair in facts[key]]
            require(len(pairs) == len(set(pairs)) and all(
                first in ports and last in ports and ports[first]['direction'] == 'in'
                and ports[last]['direction'] == 'out' for first, last in pairs),
                recipe + ': invalid accepted directed transfer')
            facts[key] = pairs
        require(not set(facts['movements']).intersection(facts['forbidden_transfers']),
                recipe + ': permitted and forbidden transfers conflict')
        require(set(facts['movements']) | set(facts['forbidden_transfers']) == {
            (first['id'], last['id']) for first in ports.values() for last in ports.values()
            if first['direction'] == 'in' and last['direction'] == 'out'},
            recipe + ': accepted routing facts do not classify every directed transfer')
    return contracts


CONTRACTS = load_contracts()
