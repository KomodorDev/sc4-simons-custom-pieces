"""Source-bound directed counterpart of the accepted compact DD RHW Y.

Only travel order and native engine lane classes change here. Physical road
and support authoring remains a separate input, and this module does not
accept either a source review or a saved build on its author's authority.
"""
from copy import deepcopy
from functools import lru_cache
import hashlib
import math
from pathlib import Path

from scp import jsonc
from scp.dbpf import require

ROOT = Path(__file__).resolve().parents[4]
ORIGINAL = ROOT/'domains/highway/01_assemblies/ddrhw-compact-diagonal-y-junction'
SUBJECT = ROOT/'domains/highway/01_assemblies/ddrhw-compact-diagonal-y-junction-reversed'
ORIGINAL_GEOMETRY_SHA256 = '8857eae50b01d3f5c15c5b47b43319de0e72c733d5cf331bb29e14f27af6d9b3'
ORIGINAL_REVIEW_SHA256 = 'ee77cc626e5fff20950fa86e477e2cef4eb412cb5aa01650a800b65cfacd5557'
NAMES = ('A-B', 'B-A', 'A-C', 'C-A', 'B-C', 'C-B')


def derive_report(geometry_bytes, review_bytes):
    """Derive six reversed journeys from the exact frozen original inputs."""
    require(hashlib.sha256(geometry_bytes).hexdigest() == ORIGINAL_GEOMETRY_SHA256
            and hashlib.sha256(review_bytes).hexdigest() == ORIGINAL_REVIEW_SHA256,
            'Reversed Y requires the exact frozen original source and review')
    original = jsonc.loads(geometry_bytes.decode('utf-8'))
    review = jsonc.loads(review_bytes.decode('utf-8'))
    require(review.get('passed') is True
            and review.get('source', {}).get('design_geometry_sha256') == ORIGINAL_GEOMETRY_SHA256
            and set(original['routes']) == set(NAMES),
            'Reversed Y original source lacks its frozen independent review')
    routes, metadata, measurements = {}, {}, {}
    for name in NAMES:
        source_name = '-'.join(reversed(name.split('-')))
        source = original['route_metadata'][source_name]
        points = deepcopy(list(reversed(original['routes'][source_name])))
        routes[name] = points
        metadata[name] = {
            'from_arm': source['to_arm'], 'to_arm': source['from_arm'],
            'from_deck': source['to_deck'], 'to_deck': source['from_deck'],
            'from_lane': 1-source['to_lane'], 'to_lane': 1-source['from_lane'],
            'engine_transport': source['engine_transport'], 'compatibility': source['compatibility'],
        }
        grades = [(last[2]-first[2])/math.dist(first[:2], last[:2])
                  for first, last in zip(points, points[1:])]
        measurements[name] = {**deepcopy(original['route_measurements'][source_name]),
            'minimum_signed_grade': min(grades), 'maximum_signed_grade': max(grades),
            'original_physical_source_route': source_name,
            'measurement_scope': 'Inherited absolute diagnostics; signed grades recomputed from reversed finite source chords'}
    sockets = deepcopy(original['native_socket_members'])
    for socket in sockets:
        socket['native_tile_id'] = '57530000' if socket['arm'] == 'C' else '57530200'
        if socket['arm'] == 'C':
            socket['native_clockwise_quarter_turns'] = 1
        for member in socket['members']:
            member['lane'] = 1-member['lane']
            member['direction'] = ('core-to-native' if member['direction'] == 'native-to-core'
                                   else 'native-to-core')
            member['unit_travel_tangent_enh'] = [-value for value in member['unit_travel_tangent_enh']]
    return {
        'schema_version': 1,
        'title': 'Compact diagonal DD RHW Y: reversed travel source candidate',
        'variant': 'reversed', 'state': 'author-derived-source-candidate',
        'scope': 'Reverse all six complete original directed lane polylines, retain their exact physical loci, and swap native lane classes; this is not source or saved-model acceptance.',
        'coordinate_frame': original['coordinate_frame'],
        'source_provenance': {
            'original_geometry': 'domains/highway/01_assemblies/ddrhw-compact-diagonal-y-junction/evidence/design-geometry.jsonc',
            'original_geometry_sha256': ORIGINAL_GEOMETRY_SHA256,
            'original_independent_review': 'domains/highway/01_assemblies/ddrhw-compact-diagonal-y-junction/evidence/source-verification.jsonc',
            'original_independent_review_sha256': ORIGINAL_REVIEW_SHA256,
            'derivation': 'For journey X-Y, reverse original Y-X points; swap endpoint arms and decks, and set each native lane class to one minus its original class.',
            'original_physical_geometry_changed': False,
        },
        'parameters': deepcopy(original['parameters']),
        'experimental_maximum_grade': original['experimental_maximum_grade'],
        'projection_bounds': deepcopy(original['projection_bounds']),
        'native_socket_members': sockets, 'route_metadata': metadata,
        'routes': routes, 'route_measurements': measurements,
        'unverified': ['Fresh reversed native physical collars and texture phases',
                       'Actual owned model mask, saved physical solids, and support contacts',
                       'Independent source review and saved-build verification',
                       'New-variant game placement, appearance, traffic, and save/reload'],
    }


@lru_cache(maxsize=1)
def _checked_report(report_bytes, geometry_bytes, review_bytes):
    actual = jsonc.loads(report_bytes.decode('utf-8'))
    require(actual == derive_report(geometry_bytes, review_bytes),
            'Maintained reversed source differs from its frozen directed derivation')
    return actual


def source_report():
    """Read current bytes and return a defensive copy of the bound candidate."""
    return deepcopy(_checked_report((SUBJECT/'evidence/design-geometry.jsonc').read_bytes(),
        (ORIGINAL/'evidence/design-geometry.jsonc').read_bytes(),
        (ORIGINAL/'evidence/source-verification.jsonc').read_bytes()))


def source_routes():
    report = source_report()
    return [{'id': name, 'points': deepcopy(report['routes'][name]), 'transport': 1,
             'lane': report['route_metadata'][name]['from_lane'], 'junction': False}
            for name in NAMES]
