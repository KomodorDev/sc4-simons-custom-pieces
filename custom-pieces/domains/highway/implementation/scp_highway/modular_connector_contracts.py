"""Reviewed R40 endpoint/service facts from the first verified saved build.

Before capture, each endpoint was matched to modular_verify's independent literal
criteria. Native Avenue journeys retain their same-lane through paths; the two
additional terminal movements use only the adjacent outer lane at signed
(east+north)=11.2m. No candidate geometry or route writer is imported here.

Cards retain the exact orthogonal tangent at each terminal's circular socket.
The saved first/last chord's sampled tangent is recorded separately, with its
finite R40 chord deviation measured in the frozen evidence. Grade and measured
endpoint facts follow the shared six-/nine-decimal extraction convention.
"""

ACCEPTED_MANIFEST_SHA256 = '99d984feb1899a4c9de39e504997451b94dd6a4f2066fd1860525fd52d3e6144'
SAVED_PATH_EVIDENCE = 'domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/evidence/modular-ramp-saved-paths.json'
SAVED_PATH_EVIDENCE_SHA256 = '2e737c06d799f8cc6fa3e072947db1e20917340b621aad050e8c554c6bf44a30'
PORT_FIELDS = ('id', 'direction', 'engine_transport', 'edge', 'endpoint_m', 'sampled_tangent', 'tangent', 'grade', 'service_network', 'service_family', 'variant', 'role', 'channel_kind', 'traffic_modes', 'source_cell', 'channel_id')

CONTRACTS = {
    'highway_ddrhw_modular_lower_exit_r40': {
        'reference_piece_id': 'ddrhw-modular-lower-exit-r40',
        'footprint': [2, 2],
        'cells': [[0, 1], [1, 0], [1, 1]],
        'path_hashes_by_cell': [[[1, 0], '41469cb48503b94f49483ac91e29dab089f2ae9b4b9310834f1f7cbc568ba1ed'], [[0, 1], '0355dfce500d54fa9d0f0bcf0d7b1d8d246ed1f55f4c3ba950b37c81ba0421ef'], [[1, 1], 'ac2e5d31dcca01d7d078fddf25887419f90168a5844e78111cb0b6450db11954']],
        'port_rows': [
            ('1-W-out-1', 'out', 1, 0, [-8.0, -12.231458, 0.0], [-1.0, 0.0], [-1.0, 0.0], 0.0, 'road', 'road', 'avenue-ground', 'primary', 'road-lane', ['car'], [0, 1], 'access-ramp-01'),
            ('1-E-in-2', 'in', 1, 2, [24.0, -10.207444, 6.745132], [-0.9793492239542134, -0.20217590741797095], [-0.9793492239542134, -0.20217590741797095], -0.226757443, 'road', 'road', 'access-ramp', 'primary', 'road-lane', ['car'], [1, 1], 'access-ramp-01'),
        ],
        'movements': [('1-E-in-2', '1-W-out-1')],
        'forbidden_transfers': [],
        'components': [{'id': 'access-ramp', 'network': 'road', 'construction_network': 'dirtroad'}],
        'channels': [{'id': 'access-ramp-01', 'component_id': 'access-ramp', 'kind': 'road-lane', 'traffic_modes': ['car'], 'ports': ['1-E-in-2', '1-W-out-1']}],
    },
    'highway_ddrhw_modular_lower_entry_r40': {
        'reference_piece_id': 'ddrhw-modular-lower-entry-r40',
        'footprint': [2, 2],
        'cells': [[0, 1], [1, 0], [1, 1]],
        'path_hashes_by_cell': [[[1, 0], 'ba3bb6d0755f4c29af2eae27ccf962aeaa20edff99b2efa8046b92dc6807e5cf'], [[0, 1], '41469cb48503b94f49483ac91e29dab089f2ae9b4b9310834f1f7cbc568ba1ed'], [[1, 1], 'e3b2892150a7a0e4a02427e47ab83e3fa4cd61fb3ccc23cff532bfda846bd95f']],
        'port_rows': [
            ('1-S-out-1', 'out', 1, 3, [10.207444, -24.0, 6.745132], [-0.20217590741797095, -0.9793492239542134], [-0.20217590741797095, -0.9793492239542134], 0.226757443, 'road', 'road', 'access-ramp', 'primary', 'road-lane', ['car'], [1, 1], 'access-ramp-01'),
            ('1-N-in-2', 'in', 1, 1, [12.231458, 8.0, 0.0], [0.0, -1.0], [0.0, -1.0], 0.0, 'road', 'road', 'avenue-ground', 'primary', 'road-lane', ['car'], [1, 0], 'access-ramp-01'),
        ],
        'movements': [('1-N-in-2', '1-S-out-1')],
        'forbidden_transfers': [],
        'components': [{'id': 'access-ramp', 'network': 'road', 'construction_network': 'dirtroad'}],
        'channels': [{'id': 'access-ramp-01', 'component_id': 'access-ramp', 'kind': 'road-lane', 'traffic_modes': ['car'], 'ports': ['1-S-out-1', '1-N-in-2']}],
    },
    'highway_ddrhw_modular_upper_exit_r40': {
        'reference_piece_id': 'ddrhw-modular-upper-exit-r40',
        'footprint': [3, 2],
        'cells': [[0, 0], [0, 1], [1, 0], [2, 0]],
        'path_hashes_by_cell': [[[0, 0], '91c924e3ade9c577a96570404fc665d92ab45bd58e20bf71e568a7bd978e5428'], [[1, 0], 'bbf8df4c494bacee64fbb54aed2ab2262dbc5e784db1dedf9025369d95f1c5bf'], [[2, 0], '10ffc66b0fce66c7ee9a9d1a4fbf0cb088da6630a721b51f25224d6a9255ce9a'], [[0, 1], 'f16e4c9738174264bd7ae33beb265fe3399130279b9a6a9cf37703f506bcd986']],
        'port_rows': [
            ('1-W-in-1', 'in', 1, 0, [-8.0, -8.142765, 12.25824], [0.927316971396647, 0.37427694900935327], [0.927316971396647, 0.37427694900935327], -0.296096203, 'road', 'road', 'access-ramp', 'primary', 'road-lane', ['car'], [0, 1], 'access-ramp-01'),
            ('1-E-out-2', 'out', 1, 2, [40.0, -3.768542, 0.0], [1.0, 0.0], [1.0, 0.0], 0.0, 'road', 'road', 'avenue-ground', 'primary', 'road-lane', ['car'], [2, 0], 'access-ramp-01'),
        ],
        'movements': [('1-W-in-1', '1-E-out-2')],
        'forbidden_transfers': [],
        'components': [{'id': 'access-ramp', 'network': 'road', 'construction_network': 'dirtroad'}],
        'channels': [{'id': 'access-ramp-01', 'component_id': 'access-ramp', 'kind': 'road-lane', 'traffic_modes': ['car'], 'ports': ['1-W-in-1', '1-E-out-2']}],
    },
    'highway_ddrhw_modular_upper_entry_r40': {
        'reference_piece_id': 'ddrhw-modular-upper-entry-r40',
        'footprint': [2, 3],
        'cells': [[0, 0], [0, 1], [0, 2], [1, 0]],
        'path_hashes_by_cell': [[[0, 0], '831efeef193070ade8a4b364a1d18f04a7bffc4cb72ef6b341f2cf15caa2d16a'], [[1, 0], '281d4b07ded29f5eb64acee69b6ce52912bd5aefb3c6ae51275346f9e2e0404a'], [[0, 1], 'e4c093f7ed603d109d2a2034ffdf316a508a57e3bbdd9f3db1e68400883fc0a7'], [[0, 2], '86dedcdf5acc5f2fda4cf6441617e43437dff2335e9457437d7c9d84a3fefc15']],
        'port_rows': [
            ('1-S-in-1', 'in', 1, 3, [3.768542, -40.0, 0.0], [0.0, 1.0], [0.0, 1.0], 0.0, 'road', 'road', 'avenue-ground', 'primary', 'road-lane', ['car'], [0, 2], 'access-ramp-01'),
            ('1-N-out-2', 'out', 1, 1, [8.142765, 8.0, 12.25824], [0.37427694900935327, 0.927316971396647], [0.37427694900935327, 0.927316971396647], 0.296096203, 'road', 'road', 'access-ramp', 'primary', 'road-lane', ['car'], [1, 0], 'access-ramp-01'),
        ],
        'movements': [('1-S-in-1', '1-N-out-2')],
        'forbidden_transfers': [],
        'components': [{'id': 'access-ramp', 'network': 'road', 'construction_network': 'dirtroad'}],
        'channels': [{'id': 'access-ramp-01', 'component_id': 'access-ramp', 'kind': 'road-lane', 'traffic_modes': ['car'], 'ports': ['1-N-out-2', '1-S-in-1']}],
    },
    'highway_ddrhw_modular_northwest_terminal_r40': {
        'reference_piece_id': 'ddrhw-modular-northwest-terminal-r40',
        'footprint': [3, 3],
        'cells': [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]],
        'path_hashes_by_cell': [[[0, 0], '82ec1e447b9d96193bb067bdda3164da265287a761eaa469d1e900464aebec66'], [[1, 0], 'e047d741789832d46d9a05ba18c99557a2d7a17acd0a18aa322d7dcf09d37856'], [[2, 0], '41469cb48503b94f49483ac91e29dab089f2ae9b4b9310834f1f7cbc568ba1ed'], [[0, 1], '8824ea81e7cbfeb4a2e6ba3d38973fc0928121d54777ea6e2c72cd24d3dfaa91'], [[1, 1], '93506078845a1bd496504f60c2a5769e4993e935a32c566431174ef40a4688f9'], [[2, 1], 'e7116f9abd8ec23408436ba0517c369b03fc26dddcef4032389916026790b88d'], [[0, 2], '41469cb48503b94f49483ac91e29dab089f2ae9b4b9310834f1f7cbc568ba1ed'], [[1, 2], 'a8eccef47280e7c41dfd15722129263416b20e766850ad2872ba5c08d6d50fb5'], [[2, 2], '82ec1e447b9d96193bb067bdda3164da265287a761eaa469d1e900464aebec66']],
        'port_rows': [
            ('1-W-in-1', 'in', 1, 0, [-8.0, -3.2, 0.0], [0.7071067811865475, -0.7071067811865475], [0.7071067811865475, -0.7071067811865475], 0.0, 'road', 'road', 'avenue-ground', 'primary', 'road-lane', ['car'], [0, 0], 'avenue-lane-04'),
            ('1-W-in-2', 'in', 1, 0, [-8.0, 3.2, 0.0], [0.7071067811865476, -0.7071067811865476], [0.7071067811865476, -0.7071067811865476], 0.0, 'road', 'road', 'avenue-ground', 'primary', 'road-lane', ['car'], [0, 0], 'avenue-lane-03'),
            ('1-N-out-3', 'out', 1, 1, [-3.2, 8.0, 0.0], [-0.7071067811865476, 0.7071067811865476], [-0.7071067811865476, 0.7071067811865476], 0.0, 'road', 'road', 'avenue-ground', 'primary', 'road-lane', ['car'], [0, 0], 'avenue-lane-02'),
            ('1-N-out-4', 'out', 1, 1, [3.2, 8.0, 0.0], [-0.7071067811865475, 0.7071067811865475], [-0.7071067811865475, 0.7071067811865475], 0.0, 'road', 'road', 'avenue-ground', 'primary', 'road-lane', ['car'], [0, 0], 'avenue-lane-01'),
            ('1-S-out-5', 'out', 1, 3, [12.231458, -40.0, 0.0], [0.003120334866088422, -0.9999951317433118], [0.0, -1.0], 0.0, 'road', 'road', 'avenue-ground', 'primary', 'road-lane', ['car'], [1, 2], 'avenue-ramp-02'),
            ('1-S-out-6', 'out', 1, 3, [28.8, -40.0, 0.0], [0.7071067811865478, -0.7071067811865474], [0.7071067811865478, -0.7071067811865474], 0.0, 'road', 'road', 'avenue-ground', 'primary', 'road-lane', ['car'], [2, 2], 'avenue-lane-04'),
            ('1-S-out-7', 'out', 1, 3, [35.2, -40.0, 0.0], [0.7071067811865477, -0.7071067811865475], [0.7071067811865477, -0.7071067811865475], 0.0, 'road', 'road', 'avenue-ground', 'primary', 'road-lane', ['car'], [2, 2], 'avenue-lane-03'),
            ('1-E-in-8', 'in', 1, 2, [40.0, -35.2, 0.0], [-0.7071067811865475, 0.7071067811865477], [-0.7071067811865475, 0.7071067811865477], 0.0, 'road', 'road', 'avenue-ground', 'primary', 'road-lane', ['car'], [2, 2], 'avenue-lane-02'),
            ('1-E-in-9', 'in', 1, 2, [40.0, -28.8, 0.0], [-0.7071067811865474, 0.7071067811865478], [-0.7071067811865474, 0.7071067811865478], 0.0, 'road', 'road', 'avenue-ground', 'primary', 'road-lane', ['car'], [2, 2], 'avenue-lane-01'),
            ('1-E-in-10', 'in', 1, 2, [40.0, -12.231458, 0.0], [-0.9999951317433118, 0.003120334866088422], [-1.0, 0.0], 0.0, 'road', 'road', 'avenue-ground', 'primary', 'road-lane', ['car'], [2, 1], 'avenue-ramp-01'),
            ('2-W-in-1', 'in', 2, 0, [-8.0, -7.3, 0.0], [0.7071067811865475, -0.7071067811865475], [0.7071067811865475, -0.7071067811865475], 0.0, 'pedestrian', 'pedestrian', 'avenue-sidewalk', 'primary', 'walkway', ['pedestrian'], [0, 0], 'avenue-walkway-02'),
            ('2-N-out-2', 'out', 2, 1, [7.3, 8.0, 0.0], [-0.7071067811865475, 0.7071067811865475], [-0.7071067811865475, 0.7071067811865475], 0.0, 'pedestrian', 'pedestrian', 'avenue-sidewalk', 'primary', 'walkway', ['pedestrian'], [0, 0], 'avenue-walkway-01'),
            ('2-S-out-3', 'out', 2, 3, [24.7, -40.0, 0.0], [0.7071067811865458, -0.7071067811865493], [0.7071067811865458, -0.7071067811865493], 0.0, 'pedestrian', 'pedestrian', 'avenue-sidewalk', 'primary', 'walkway', ['pedestrian'], [2, 2], 'avenue-walkway-02'),
            ('2-E-in-4', 'in', 2, 2, [40.0, -24.7, 0.0], [-0.7071067811865493, 0.7071067811865458], [-0.7071067811865493, 0.7071067811865458], 0.0, 'pedestrian', 'pedestrian', 'avenue-sidewalk', 'primary', 'walkway', ['pedestrian'], [2, 2], 'avenue-walkway-01'),
        ],
        'movements': [('1-E-in-10', '1-N-out-4'), ('1-E-in-8', '1-N-out-3'), ('1-E-in-9', '1-N-out-4'), ('1-W-in-1', '1-S-out-5'), ('1-W-in-1', '1-S-out-6'), ('1-W-in-2', '1-S-out-7'), ('2-E-in-4', '2-N-out-2'), ('2-W-in-1', '2-S-out-3')],
        'forbidden_transfers': [('1-E-in-10', '1-N-out-3'), ('1-E-in-10', '1-S-out-5'), ('1-E-in-10', '1-S-out-6'), ('1-E-in-10', '1-S-out-7'), ('1-E-in-10', '2-N-out-2'), ('1-E-in-10', '2-S-out-3'), ('1-E-in-8', '1-N-out-4'), ('1-E-in-8', '1-S-out-5'), ('1-E-in-8', '1-S-out-6'), ('1-E-in-8', '1-S-out-7'), ('1-E-in-8', '2-N-out-2'), ('1-E-in-8', '2-S-out-3'), ('1-E-in-9', '1-N-out-3'), ('1-E-in-9', '1-S-out-5'), ('1-E-in-9', '1-S-out-6'), ('1-E-in-9', '1-S-out-7'), ('1-E-in-9', '2-N-out-2'), ('1-E-in-9', '2-S-out-3'), ('1-W-in-1', '1-N-out-3'), ('1-W-in-1', '1-N-out-4'), ('1-W-in-1', '1-S-out-7'), ('1-W-in-1', '2-N-out-2'), ('1-W-in-1', '2-S-out-3'), ('1-W-in-2', '1-N-out-3'), ('1-W-in-2', '1-N-out-4'), ('1-W-in-2', '1-S-out-5'), ('1-W-in-2', '1-S-out-6'), ('1-W-in-2', '2-N-out-2'), ('1-W-in-2', '2-S-out-3'), ('2-E-in-4', '1-N-out-3'), ('2-E-in-4', '1-N-out-4'), ('2-E-in-4', '1-S-out-5'), ('2-E-in-4', '1-S-out-6'), ('2-E-in-4', '1-S-out-7'), ('2-E-in-4', '2-S-out-3'), ('2-W-in-1', '1-N-out-3'), ('2-W-in-1', '1-N-out-4'), ('2-W-in-1', '1-S-out-5'), ('2-W-in-1', '1-S-out-6'), ('2-W-in-1', '1-S-out-7'), ('2-W-in-1', '2-N-out-2')],
        'components': [{'id': 'avenue-mainline', 'network': 'road'}, {'id': 'avenue-walkways', 'network': 'pedestrian', 'construction_network': 'avenue'}],
        'channels': [{'id': 'avenue-lane-01', 'component_id': 'avenue-mainline', 'kind': 'road-lane', 'traffic_modes': ['car'], 'ports': ['1-E-in-9', '1-N-out-4']}, {'id': 'avenue-lane-02', 'component_id': 'avenue-mainline', 'kind': 'road-lane', 'traffic_modes': ['car'], 'ports': ['1-E-in-8', '1-N-out-3']}, {'id': 'avenue-walkway-01', 'component_id': 'avenue-walkways', 'kind': 'walkway', 'traffic_modes': ['pedestrian'], 'ports': ['2-E-in-4', '2-N-out-2']}, {'id': 'avenue-lane-03', 'component_id': 'avenue-mainline', 'kind': 'road-lane', 'traffic_modes': ['car'], 'ports': ['1-W-in-2', '1-S-out-7']}, {'id': 'avenue-lane-04', 'component_id': 'avenue-mainline', 'kind': 'road-lane', 'traffic_modes': ['car'], 'ports': ['1-W-in-1', '1-S-out-6']}, {'id': 'avenue-walkway-02', 'component_id': 'avenue-walkways', 'kind': 'walkway', 'traffic_modes': ['pedestrian'], 'ports': ['2-W-in-1', '2-S-out-3']}, {'id': 'avenue-ramp-01', 'component_id': 'avenue-mainline', 'kind': 'road-lane', 'traffic_modes': ['car'], 'ports': ['1-E-in-10']}, {'id': 'avenue-ramp-02', 'component_id': 'avenue-mainline', 'kind': 'road-lane', 'traffic_modes': ['car'], 'ports': ['1-S-out-5']}],
    },
    'highway_ddrhw_modular_southeast_terminal_r40': {
        'reference_piece_id': 'ddrhw-modular-southeast-terminal-r40',
        'footprint': [4, 4],
        'cells': [[0, 0], [0, 1], [1, 0], [1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]],
        'path_hashes_by_cell': [[[0, 0], '82ec1e447b9d96193bb067bdda3164da265287a761eaa469d1e900464aebec66'], [[1, 0], 'de59066cb6e1da112acfbd863e80f32ce877b0ca73865e095397b336d5950e7f'], [[0, 1], '5b53e2b7e406f019c9ffa09ee7ad48c6dbf21053647e1aa1cc501e9231d6ce10'], [[1, 1], '82ec1e447b9d96193bb067bdda3164da265287a761eaa469d1e900464aebec66'], [[2, 1], '3af6b555ed9afc335f20b248790700489f82ad4159bda0f1e01adb99773755d4'], [[3, 1], '41469cb48503b94f49483ac91e29dab089f2ae9b4b9310834f1f7cbc568ba1ed'], [[1, 2], 'd27b4365192ec55e45205327fe4d28819bef0cd363435abe5abb834eaf917314'], [[2, 2], '28614f0f9c75275f7bcae144582a05b05fee8e11276779f30a45dd2c132b3727'], [[3, 2], 'dc1c2dd3b45da20d4d57ce821953ff91fb99ff9495f00430983c6714121b548c'], [[1, 3], '41469cb48503b94f49483ac91e29dab089f2ae9b4b9310834f1f7cbc568ba1ed'], [[2, 3], '7a8149fa29f040fe6525a16c5918650f718c2559b1ddc4462f20a54e1cb9bd56'], [[3, 3], '82ec1e447b9d96193bb067bdda3164da265287a761eaa469d1e900464aebec66']],
        'port_rows': [
            ('1-W-in-1', 'in', 1, 0, [-8.0, -3.2, 0.0], [0.7071067811865475, -0.7071067811865475], [0.7071067811865475, -0.7071067811865475], 0.0, 'road', 'road', 'avenue-ground', 'primary', 'road-lane', ['car'], [0, 0], 'avenue-lane-04'),
            ('1-W-in-2', 'in', 1, 0, [-8.0, 3.2, 0.0], [0.7071067811865476, -0.7071067811865476], [0.7071067811865476, -0.7071067811865476], 0.0, 'road', 'road', 'avenue-ground', 'primary', 'road-lane', ['car'], [0, 0], 'avenue-lane-03'),
            ('1-N-out-3', 'out', 1, 1, [-3.2, 8.0, 0.0], [-0.7071067811865476, 0.7071067811865476], [-0.7071067811865476, 0.7071067811865476], 0.0, 'road', 'road', 'avenue-ground', 'primary', 'road-lane', ['car'], [0, 0], 'avenue-lane-02'),
            ('1-N-out-4', 'out', 1, 1, [3.2, 8.0, 0.0], [-0.7071067811865475, 0.7071067811865475], [-0.7071067811865475, 0.7071067811865475], 0.0, 'road', 'road', 'avenue-ground', 'primary', 'road-lane', ['car'], [0, 0], 'avenue-lane-01'),
            ('1-W-in-5', 'in', 1, 0, [8.0, -35.768542, 0.0], [0.9999951317433118, -0.0031203348661026486], [1.0, 0.0], 0.0, 'road', 'road', 'avenue-ground', 'primary', 'road-lane', ['car'], [1, 2], 'avenue-ramp-01'),
            ('1-N-out-6', 'out', 1, 1, [35.768542, -8.0, 0.0], [-0.0031203348661026486, 0.9999951317433118], [0.0, 1.0], 0.0, 'road', 'road', 'avenue-ground', 'primary', 'road-lane', ['car'], [2, 1], 'avenue-ramp-02'),
            ('1-S-out-7', 'out', 1, 3, [44.8, -56.0, 0.0], [0.7071067811865475, -0.7071067811865475], [0.7071067811865475, -0.7071067811865475], 0.0, 'road', 'road', 'avenue-ground', 'primary', 'road-lane', ['car'], [3, 3], 'avenue-lane-04'),
            ('1-S-out-8', 'out', 1, 3, [51.2, -56.0, 0.0], [0.7071067811865475, -0.7071067811865475], [0.7071067811865475, -0.7071067811865475], 0.0, 'road', 'road', 'avenue-ground', 'primary', 'road-lane', ['car'], [3, 3], 'avenue-lane-03'),
            ('1-E-in-9', 'in', 1, 2, [56.0, -51.2, 0.0], [-0.7071067811865475, 0.7071067811865475], [-0.7071067811865475, 0.7071067811865475], 0.0, 'road', 'road', 'avenue-ground', 'primary', 'road-lane', ['car'], [3, 3], 'avenue-lane-02'),
            ('1-E-in-10', 'in', 1, 2, [56.0, -44.8, 0.0], [-0.7071067811865475, 0.7071067811865475], [-0.7071067811865475, 0.7071067811865475], 0.0, 'road', 'road', 'avenue-ground', 'primary', 'road-lane', ['car'], [3, 3], 'avenue-lane-01'),
            ('2-W-in-1', 'in', 2, 0, [-8.0, -7.3, 0.0], [0.7071067811865475, -0.7071067811865475], [0.7071067811865475, -0.7071067811865475], 0.0, 'pedestrian', 'pedestrian', 'avenue-sidewalk', 'primary', 'walkway', ['pedestrian'], [0, 0], 'avenue-walkway-02'),
            ('2-N-out-2', 'out', 2, 1, [7.3, 8.0, 0.0], [-0.7071067811865475, 0.7071067811865475], [-0.7071067811865475, 0.7071067811865475], 0.0, 'pedestrian', 'pedestrian', 'avenue-sidewalk', 'primary', 'walkway', ['pedestrian'], [0, 0], 'avenue-walkway-01'),
            ('2-S-out-3', 'out', 2, 3, [40.7, -56.0, 0.0], [0.7071067811865475, -0.7071067811865475], [0.7071067811865475, -0.7071067811865475], 0.0, 'pedestrian', 'pedestrian', 'avenue-sidewalk', 'primary', 'walkway', ['pedestrian'], [3, 3], 'avenue-walkway-02'),
            ('2-E-in-4', 'in', 2, 2, [56.0, -40.7, 0.0], [-0.7071067811865475, 0.7071067811865475], [-0.7071067811865475, 0.7071067811865475], 0.0, 'pedestrian', 'pedestrian', 'avenue-sidewalk', 'primary', 'walkway', ['pedestrian'], [3, 3], 'avenue-walkway-01'),
        ],
        'movements': [('1-E-in-10', '1-N-out-4'), ('1-E-in-10', '1-N-out-6'), ('1-E-in-9', '1-N-out-3'), ('1-W-in-1', '1-S-out-7'), ('1-W-in-2', '1-S-out-8'), ('1-W-in-5', '1-S-out-7'), ('2-E-in-4', '2-N-out-2'), ('2-W-in-1', '2-S-out-3')],
        'forbidden_transfers': [('1-E-in-10', '1-N-out-3'), ('1-E-in-10', '1-S-out-7'), ('1-E-in-10', '1-S-out-8'), ('1-E-in-10', '2-N-out-2'), ('1-E-in-10', '2-S-out-3'), ('1-E-in-9', '1-N-out-4'), ('1-E-in-9', '1-N-out-6'), ('1-E-in-9', '1-S-out-7'), ('1-E-in-9', '1-S-out-8'), ('1-E-in-9', '2-N-out-2'), ('1-E-in-9', '2-S-out-3'), ('1-W-in-1', '1-N-out-3'), ('1-W-in-1', '1-N-out-4'), ('1-W-in-1', '1-N-out-6'), ('1-W-in-1', '1-S-out-8'), ('1-W-in-1', '2-N-out-2'), ('1-W-in-1', '2-S-out-3'), ('1-W-in-2', '1-N-out-3'), ('1-W-in-2', '1-N-out-4'), ('1-W-in-2', '1-N-out-6'), ('1-W-in-2', '1-S-out-7'), ('1-W-in-2', '2-N-out-2'), ('1-W-in-2', '2-S-out-3'), ('1-W-in-5', '1-N-out-3'), ('1-W-in-5', '1-N-out-4'), ('1-W-in-5', '1-N-out-6'), ('1-W-in-5', '1-S-out-8'), ('1-W-in-5', '2-N-out-2'), ('1-W-in-5', '2-S-out-3'), ('2-E-in-4', '1-N-out-3'), ('2-E-in-4', '1-N-out-4'), ('2-E-in-4', '1-N-out-6'), ('2-E-in-4', '1-S-out-7'), ('2-E-in-4', '1-S-out-8'), ('2-E-in-4', '2-S-out-3'), ('2-W-in-1', '1-N-out-3'), ('2-W-in-1', '1-N-out-4'), ('2-W-in-1', '1-N-out-6'), ('2-W-in-1', '1-S-out-7'), ('2-W-in-1', '1-S-out-8'), ('2-W-in-1', '2-N-out-2')],
        'components': [{'id': 'avenue-mainline', 'network': 'road'}, {'id': 'avenue-walkways', 'network': 'pedestrian', 'construction_network': 'avenue'}],
        'channels': [{'id': 'avenue-lane-01', 'component_id': 'avenue-mainline', 'kind': 'road-lane', 'traffic_modes': ['car'], 'ports': ['1-E-in-10', '1-N-out-4']}, {'id': 'avenue-lane-02', 'component_id': 'avenue-mainline', 'kind': 'road-lane', 'traffic_modes': ['car'], 'ports': ['1-E-in-9', '1-N-out-3']}, {'id': 'avenue-walkway-01', 'component_id': 'avenue-walkways', 'kind': 'walkway', 'traffic_modes': ['pedestrian'], 'ports': ['2-E-in-4', '2-N-out-2']}, {'id': 'avenue-lane-03', 'component_id': 'avenue-mainline', 'kind': 'road-lane', 'traffic_modes': ['car'], 'ports': ['1-W-in-2', '1-S-out-8']}, {'id': 'avenue-lane-04', 'component_id': 'avenue-mainline', 'kind': 'road-lane', 'traffic_modes': ['car'], 'ports': ['1-W-in-1', '1-S-out-7']}, {'id': 'avenue-walkway-02', 'component_id': 'avenue-walkways', 'kind': 'walkway', 'traffic_modes': ['pedestrian'], 'ports': ['2-W-in-1', '2-S-out-3']}, {'id': 'avenue-ramp-01', 'component_id': 'avenue-mainline', 'kind': 'road-lane', 'traffic_modes': ['car'], 'ports': ['1-W-in-5']}, {'id': 'avenue-ramp-02', 'component_id': 'avenue-mainline', 'kind': 'road-lane', 'traffic_modes': ['car'], 'ports': ['1-N-out-6']}],
    },
}

for _record in CONTRACTS.values():
    _record["ports"] = [dict(zip(PORT_FIELDS, row, strict=True)) for row in _record.pop("port_rows")]
del _record
