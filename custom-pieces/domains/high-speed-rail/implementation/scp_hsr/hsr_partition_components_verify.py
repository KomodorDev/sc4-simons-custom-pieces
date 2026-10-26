"""Independent literal and resource-fingerprint contracts for reusable HSR modules.

Local PATH files and every zoom of every local S3D must match the inspected
current-module baseline. Cells, ports, journeys and supports are literals;
this verifier never imports a layout or model writer to derive expectations.

Several interfaces cut a curve at a city-tile edge. They deliberately retain
its off-centre position and tangent instead of acquiring a fictitious native
straight collar. They require a matching custom continuation. Whole-assembly
checks prove continuity and geometry of the complete approved assembly.
"""
from __future__ import annotations

from functools import lru_cache
import hashlib
import json
import math

from scp.dbpf import require
from .directional_t_verify import _journeys, _world_triangles
from .hsr_mesh_verify import audit_bed_overlaps, audit_crossings, audit_supports
from .interchange_verify import S3D, PATH, EXEMPLAR, _encoded_routes, _graph, _models, _native_port_headings
from scp.models import parse_s3d
from scp.render_meshes import assert_render_budget

LOWER = 15.5
COMMON = {
    'kind': 'partition_component', 'min_height': LOWER, 'max_height': LOWER,
    'max_grade': 0., 'clearance_width_m': 5., 'minimum_clearance': 5.,
    'foundation_width_m': 1.3, 'minimum_support_spacing_m': 16.,
    'allow_same_edge': False, 'required_grade_separated_crossings': 0,
    'custom_curved_interfaces': True,
}

CONTRACTS = {}

# These additional partitions have native, straight cardinal connection ends.
# Their cell masks and heights remain independent literals, including the
# sparse flat junction around the two bottom cells of the separate climb.
CONTRACTS.update({
    'hsr_component_modular_south_junction': {
        **COMMON,
        'footprint': (3, 6), 'cost': 1400,
        'custom_curved_interfaces': False,
        'cells': [(0, 0), (2, 0), (0, 1), (2, 1),
                  (0, 2), (1, 2), (2, 2), (0, 3), (1, 3), (2, 3),
                  (0, 4), (1, 4), (2, 4), (1, 5)],
        'structural_cells': [(0, 4), (2, 4)],
        'ports': {'Sin': (18., -88., 15.5), 'Sout': (14., -88., 15.5),
                  'Nout': (18., -24., 15.5), 'Nin': (14., -24., 15.5),
                  'Rout': (32., 8., 15.5), 'Lin': (0., 8., 15.5)},
        'port_vectors': {'Sin': (0., 1.), 'Sout': (0., -1.),
                         'Nout': (0., 1.), 'Nin': (0., -1.),
                         'Rout': (0., 1.), 'Lin': (0., -1.)},
        'movements': [('Sin', 'Nout'), ('Nin', 'Sout'), ('Sin', 'Rout'), ('Lin', 'Sout')],
        'support_centres_xz': [(0., 0.), (32., 0.), (0., 16.), (32., 16.),
                               (16., 32.), (16., 48.), (16., 64.), (16., 80.)],
    },
    'hsr_component_modular_paired_climb': {
        **COMMON,
        'footprint': (1, 8), 'cost': 800,
        'custom_curved_interfaces': False,
        'min_height': 15.5, 'max_height': 30.5, 'max_grade': .156251,
        'cells': [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)],
        'structural_cells': [],
        'ports': {'Sin': (2., -120., 15.5), 'Sout': (-2., -120., 15.5),
                  'Nout': (2., 8., 30.5), 'Nin': (-2., 8., 30.5)},
        'port_vectors': {'Sin': (0., 1.), 'Sout': (0., -1.),
                         'Nout': (0., 1.), 'Nin': (0., -1.)},
        'movements': [('Sin', 'Nout'), ('Nin', 'Sout')],
        'support_centres_xz': [(0., 0.), (0., 16.), (0., 32.), (0., 48.),
                               (0., 64.), (0., 80.), (0., 96.), (0., 112.)],
    },
    'hsr_component_modular_crossing_core': {
        **COMMON,
        'footprint': (1, 1), 'cost': 100,
        'custom_curved_interfaces': False, 'min_height': 15.5, 'max_height': 30.5,
        'cells': [(0, 0)], 'structural_cells': [],
        'ports': {'Sin': (2., -8., 30.5), 'Sout': (-2., -8., 30.5),
                  'Nout': (2., 8., 30.5), 'Nin': (-2., 8., 30.5),
                  'Win': (-8., -2., 15.5), 'Wout': (-8., 2., 15.5),
                  'Eout': (8., -2., 15.5), 'Ein': (8., 2., 15.5)},
        'port_vectors': {'Sin': (0., 1.), 'Sout': (0., -1.),
                         'Nout': (0., 1.), 'Nin': (0., -1.),
                         'Win': (1., 0.), 'Wout': (-1., 0.),
                         'Eout': (1., 0.), 'Ein': (-1., 0.)},
        'movements': [('Sin', 'Nout'), ('Nin', 'Sout'), ('Win', 'Eout'), ('Ein', 'Wout')],
        'support_centres_xz': [(0., 0.)],
        'required_grade_separated_crossings': 4,
        'expected_crossings_xyz': [(-2., -2., 30.5, 15.5), (-2., 2., 30.5, 15.5),
                                   (2., -2., 30.5, 15.5), (2., 2., 30.5, 15.5)],
    },

})


def _number(value):
    return int(value, 16) if isinstance(value, str) else int(value)


def _fingerprints(resources, spec, kind):
    """Check directly keyed current-module resource fingerprints."""
    contract = CONTRACTS[spec['recipe']]
    expected = MODULE_TILE_FINGERPRINTS[spec['recipe']]
    checked = 0
    for (column, row), tile in zip(contract['cells'], spec['tile_ids']):
        source = expected[column, row]
        prefix, digest = (PATH, source[1]) if kind == 'PATH' else (S3D, source[0])
        for zoom in range(1 if kind == 'PATH' else 5):
            raw = resources[*prefix, _number(tile)+zoom]
            require(hashlib.sha256(raw).hexdigest() == digest,
                    f'HSR module changed its frozen module {kind} bytes at cell {(column, row)}, zoom {zoom}')
            checked += 1
    return checked


def audit_partition_climb(journeys):
    """Check the literal 128 m paired rise, including exact flat end collars.

    This independently stated profile has 8 m flat ends and 16 m easing
    sections. It does not obtain expected heights from a model writer.
    """
    def expected_height(north):
        travel = north+112.
        if travel <= 0.:
            fraction = 0.
        elif travel >= 112.:
            fraction = 1.
        elif travel < 16.:
            fraction = travel*travel/3072.
        elif travel > 96.:
            fraction = 1.-(112.-travel)**2/3072.
        else:
            fraction = (travel-8.)/96.
        return 15.5+15.*fraction

    contract = CONTRACTS['hsr_component_modular_paired_climb']
    require(set(journeys) == set(contract['movements']),
            'Partition climb lacks its two opposite-direction journeys')
    checked, flat = 0, 0
    for movement, points in journeys.items():
        source, target = movement
        require(math.dist(points[0], contract['ports'][source]) <= 2e-6 and
                math.dist(points[-1], contract['ports'][target]) <= 2e-6,
                'Partition climb journey has reversed or displaced native ends')
        direction = 1. if source == 'Sin' else -1.
        lateral = 2. if direction > 0. else -2.
        require(all(abs(point[0]-lateral) <= 2e-6 for point in points),
                'Partition climb departs from its native straight track offsets')
        require(all((b[1]-a[1])*direction > 0. and (b[2]-a[2])*direction >= -2e-6
                    for a, b in zip(points, points[1:])),
                'Partition climb reverses its forward station or monotonic height')
        for _, north, height in points:
            require(abs(height-expected_height(north)) <= 2e-6,
                    'Partition climb differs from its independent eased height profile')
            checked += 1
            if north <= -112.+2e-6 or north >= -2e-6:
                expected = 15.5 if north < -56. else 30.5
                require(abs(height-expected) <= 2e-6,
                        'Partition climb lacks its exact eight-metre flat end collar')
                flat += 1
    return {'paired_climb_profile_samples_checked': checked,
            'paired_climb_flat_collar_samples_checked': flat,
            'paired_climb_horizontal_length_m': 128.,
            'paired_climb_rise_m': 15., 'paired_climb_flat_collar_m': 8.}


def audit_partition_native_collars(journeys, contract):
    """Measure eight straight, flat metres across however many PATH chords.

    A newly selected boundary can divide an old straight into 0.5 m samples.
    The physical collar requirement concerns their total straight length,
    rather than requiring the first stored segment alone to be eight metres.
    """
    checked = 0
    for movement, points in journeys.items():
        for label, samples, sign in ((movement[0], points, 1.),
                                      (movement[1], list(reversed(points)), -1.)):
            vector = contract['port_vectors'][label]
            norm = math.hypot(*vector)
            direction = tuple(sign*value/norm for value in vector)
            first, distance = samples[0], 0.
            for a, b in zip(samples, samples[1:]):
                length = math.dist(a[:2], b[:2])
                take = min(length, 8.-distance)
                endpoint = tuple(a[i]+take*(b[i]-a[i])/length for i in range(3))
                expected = (first[0]+(distance+take)*direction[0],
                            first[1]+(distance+take)*direction[1], first[2])
                require(math.dist(endpoint, expected) <= 2e-6,
                        'Partition native end lacks eight straight flat metres')
                distance += take
                if distance >= 8.-2e-6:
                    break
            require(distance >= 8.-2e-6, 'Partition native end is shorter than its eight-metre collar')
            checked += 1
    return {'native_straight_eight_metre_collars_checked': checked}


def check_partition_paths(resources, spec):
    contract = CONTRACTS[spec['recipe']]
    fingerprints = _fingerprints(resources, spec, 'PATH')
    records = _encoded_routes(resources, spec, contract)
    ports, movements = _graph(records, contract)
    headings = _native_port_headings(records, contract)
    journeys = _journeys(records, contract)
    maximum_grade = max((abs(b[2]-a[2])/math.dist(a[:2], b[:2])
                         for _, _, points in records for a, b in zip(points, points[1:])), default=0.)
    report = {
        'tile_count': len(contract['cells']), 'encoded_routes_checked': len(records),
        'external_ports_checked': ports, 'permitted_movements_checked': movements,
        'unique_complete_journeys_checked': len(journeys), 'rotations_checked': 4,
        'exact_3d_cell_seams': True, 'all_encoded_tracks_used_by_intended_journeys': True,
        'unwanted_u_turns': False, 'unwanted_cross_level_transfers': False,
        'maximum_encoded_grade': maximum_grade,
        'native_port_heights_m': sorted({point[2] for point in contract['ports'].values()}),
        'literal_port_tangents_checked': len(headings),
        'frozen_module_path_files_checked': fingerprints,
        'frozen_module_recipe': spec['recipe'],
        'frozen_module_source_dat_sha256': MODULE_SOURCE_DAT_SHA256[spec['recipe']],
        'all_module_local_path_bytes_unchanged': True,
        'custom_curved_interfaces_require_matching_continuation': contract['custom_curved_interfaces'],
        'curve_quality_scope': 'Exact approved module samples retained; assembled routes have independent curve-quality audits.',
        'collision_free_operation_claimed': False,
    }
    report.update(audit_crossings(journeys, contract))
    if not contract['custom_curved_interfaces']:
        report.update(audit_partition_native_collars(journeys, contract))
    if spec['recipe'] == 'hsr_component_modular_paired_climb':
        report.update(audit_partition_climb(journeys))
    return report


def check_partition_models(resources, spec):
    keys = {(*S3D, _number(spec['preview_id']))}
    for tile in map(_number, spec['tile_ids']):
        keys.update({(*S3D, tile+zoom) for zoom in range(5)})
        keys.update({(*PATH, tile), (*EXEMPLAR, tile)})
    immutable = tuple((key, resources[key]) for key in sorted(keys))
    return json.loads(_cached_models(json.dumps(spec, sort_keys=True, separators=(',', ':')), immutable))


@lru_cache(maxsize=16)
def _cached_models(spec_json, immutable):
    spec, resources = json.loads(spec_json), dict(immutable)
    contract = CONTRACTS[spec['recipe']]
    models = _fingerprints(resources, spec, 'S3D')
    paths = _fingerprints(resources, spec, 'PATH')
    # These inspect the actual saved geometry: model/material integrity,
    # bounds, PATH-to-visible-bed fit, full train clearance, preview assembly,
    # bed overlap and all nine underside contact points of each support.
    report = _models(resources, spec, contract=contract)
    triangles = _world_triangles(resources, spec, contract)
    report.update(audit_bed_overlaps(triangles))
    report.update(audit_supports(triangles, contract))
    budgets = [assert_render_budget(parse_s3d(raw)) for key, raw in immutable if key[:2] == S3D]
    report.update(
        frozen_module_model_zooms_checked=models,
        frozen_module_path_files_checked=paths,
        frozen_module_recipe=spec['recipe'],
        frozen_module_source_dat_sha256=MODULE_SOURCE_DAT_SHA256[spec['recipe']],
        all_module_local_model_bytes_unchanged=True,
        all_module_local_path_bytes_unchanged=True,
        render_budget_models_checked=len(budgets), render_group_budget_checked=True,
        full_width_bed_validation_scope='Every local mesh and train path matches the current reusable-module baseline; complete assembled corridor coverage is checked separately.',
        custom_curve_ends_reswept=False,
    )
    return json.dumps(report, sort_keys=True, separators=(',', ':'))


# Current reusable-module fingerprints: local cell -> (S3D SHA-256, PATH SHA-256).
# These literals require no fixture, geometry source or writer at verification time.
MODULE_SOURCE_DAT_SHA256 = {'hsr_component_modular_south_junction': '6865dc3ae6351373381342721a6ca42daa00e753905245f700733e1f7d4b79ca',
 'hsr_component_modular_paired_climb': '8d8ea57041c48c32a45331d7ec67f61a80ad03783cc69bc1e13074bb69ecab5c',
 'hsr_component_modular_crossing_core': '2f160319a2fa5d299b9e1957d7f41cfa355e943134b345aae9e8abacdfa4b3da'}

MODULE_TILE_FINGERPRINTS = {'hsr_component_modular_south_junction': {(0, 0): ('0f8c0cf6878b9a9e6b489b5fc018a92179184d79162d4339360196ad9d79ec43',
                                                   '9ef50ace2d8f98b5718172ce20148ef63fd04382821c6f8978b5dd61ab84041a'),
                                          (2, 0): ('61fe1b4ddeaf846f52e3779859e212399b97a8c97f9ad1d46fb4583119a169c6',
                                                   '96aaed124a444580a0f28d7f8f55cc8d66775be3841fceb5a13ff2a78650a0a3'),
                                          (0, 1): ('9aef806727bea00fe908dd4bd7e7bfe6184a2b944f04d67f0b75d6d21af776ca',
                                                   '4a1ff37f92144e7203c00e0ec8ce154bae022a7c4c6e38333b1ed61de4ab33fe'),
                                          (2, 1): ('b226af1a8240bac60a9af81fd4a306f94b49ae651070425e5f03c062d5c327dd',
                                                   '539ae1321bc013a4be32763822114bd0f5133a008cb3f82c8a4ea481bd9fefe6'),
                                          (0, 2): ('5658b783b1c414aaf7452ecdd3eccb0d208d12fa3497f633a20635fc22ac86cc',
                                                   'ed2a2544e09b01494183e666ff7eba86fda3170a00b532d4eb6afc99cc85a9a2'),
                                          (1, 2): ('859cb2e1d73804803d3a76ebce89a64bee86b2dd09e9c8c4a09f3da0b40dae4e',
                                                   'a843f5f6246499f582076500d0d72c2f65b58f462187b86b1260fbba799a6194'),
                                          (2, 2): ('4ecc705638ce4d1ed32381d9065eac4db873dd6665d65d2af86621ae190696c1',
                                                   '4b405030208a18f79f4dfd40db9177742d111c3aa560a505e8b817c726c7b2a9'),
                                          (0, 3): ('36296490f4afc12bde43a0e40fa6ee1164297eb77cb440d846d17e75c63a3d55',
                                                   '538f2d3de32668efc611434a734abcd49112e4247ef4982938ca65727f7684da'),
                                          (1, 3): ('207f129523646a25bac80c76297529c48ccd5897e45d41c15032a5fd4219edc6',
                                                   '633f6abdadd63f9b0977e184c8ce3645dd29e605749e2801a5bcf5ac3f8ebf1f'),
                                          (2, 3): ('d688b44d98b4c49194e97dbd40e962b492500fa9bbd6f1c07b1a6183333b3400',
                                                   'f1c7870216ddec17a487a3bed91b275c235780ef3210935d197fe21257152e43'),
                                          (0, 4): ('01996dcdd494c7f5cb05395d66c10e7a95c67a6379011d3b39406bb9fc4f8504',
                                                   '41469cb48503b94f49483ac91e29dab089f2ae9b4b9310834f1f7cbc568ba1ed'),
                                          (1, 4): ('1e6b19453b3c3f4d1fa0aefe6f4b9f136b0affe60d87b0eb7fbab89890fe5838',
                                                   '349274fb078b2ed1948642972e7c2306c02067556bc09ef357329ce34cd24619'),
                                          (2, 4): ('7b48a785f888af4c8a246cc7d77f3016ddc1dc5db08f8f6ec12e3f413ffc0ed7',
                                                   '41469cb48503b94f49483ac91e29dab089f2ae9b4b9310834f1f7cbc568ba1ed'),
                                          (1, 5): ('8887325ab85752c9cf440d686ed62f083d2479994be74179cb4ecd15ba137553',
                                                   '718c29252f13505858ec875e440e11967a82b21235adaed2fd3f8e6f200b2e58')},
 'hsr_component_modular_paired_climb': {(0, 0): ('d243591330d1322b721671cab5334add8683c3d149258d2d732affdef9adaae7',
                                                 'ed203af6257bd1b00e4b126b6a138cd08f7480b24a5cc0a08407442799c46f84'),
                                        (0, 1): ('c4bfb8f7a6def3fcf9765843d11cf3b31b007ce90f3226804e26003fbbd1bbc3',
                                                 'f10c96fbee444a41ab7a92a3b6e99df830d3df3e31aae2aef3e7ad1424e4646f'),
                                        (0, 2): ('43b0f7f4ec030afd6f4bd007a205eaa0065aa91b68d69bed10c4fbb90e415330',
                                                 'b04ec129e91032230a13766fc528579e076ed0fd9530e393eeb8ee993f25407c'),
                                        (0, 3): ('24ca864b4543a8254aaa6463b1138f82f0418ed9840b00c867fa2678158a3746',
                                                 'fac4f2c6e2ab1815fe9951283d5aaa1e9345f3a3cf168b249705dc0e4b485e25'),
                                        (0, 4): ('535728622168c28f9ac1aa746fe3ace7c43bc62b14b2b5c77a8583d72f2e6b78',
                                                 '69a4bb0456f555d10146c4f10b4cbbd40246a8c52902292624b58d38b400bfa8'),
                                        (0, 5): ('8517bb6ab11ea353027a24c6ca542d001ffec33e376c49dae28caac2bdd49b37',
                                                 'acb413d82af05515eff005878cd516b2047879997cf0ca48611435af1b5aeb40'),
                                        (0, 6): ('e21c31b5a239c334737734798eee48b27f8ec25b98e1316a495d6b49bc6f0b47',
                                                 '54915476a6a95c1589a79c4d27bc292e510c456b06c9995dafc1adcd6ce88eaa'),
                                        (0, 7): ('9e26f108f04fcb3def7dd15e9c0b16ac26f2f0d6e20bbcd4fa502afffb6a8de6',
                                                 '49aafbad70dd9180ca28f1eaeccfe96f5294c69e5bf12e1b64775dc78e6c82bf')},
 'hsr_component_modular_crossing_core': {(0, 0): ('0dbb4b8e8e9f94956f9aa55369dda1d12b283a02e0126027066e87e56da61478',
                                                  '7ef7b86a409932a67aafd7d6dec0a41a52c411b40a22ed129ff26ec52ece23c3')}}
