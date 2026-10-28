"""Independent exact retained-cell pins for the nine-tile paired fan core.

These literal fingerprints identify the independently approved full fan DAT
54086c7a5423f0d121d732d1b8081c1984e0663afb3d3c8a4604cdcc5b43c797
and are independent of the new core writer. Verification needs no predecessor DAT.
"""
from __future__ import annotations

import hashlib
from scp.dbpf import require
from scp.track_paths import PATH, S3D

CORE_RECIPE = 'hsr_component_l2_paired_fan_compact_core'
SOURCE_DAT_SHA256 = '54086c7a5423f0d121d732d1b8081c1984e0663afb3d3c8a4604cdcc5b43c797'
PINS = {(2, 0): {'old_cell': (3, 2),
          'model_sha256': '230192de5c90345fed778582d976c9dc2c6102052768887fcd1b92e36962a41f',
          'path_sha256': '730f3e37d3f9913457e486377b77ed235d744c4ec63272e53daf2ff56a779f1f',
          'shadow_sha256': ('6ac0f3b42c3dbdaf9306fca1c252cfaa234797241ed1f1f08d4b389645bee367',
                            '24635a47b5716859bb34c89d7a0b91af96f32007b3921207de9db6ee907721bc',
                            '0d615ad4e834e295c67b500a20094e6d155151fc348752302d499746014669a3',
                            '254bac6aa670ce47724b77fa582a73e1ba12e6d1efa5caaa2fc978ab6a97c1dc',
                            'fe978d10b8d814b6ed4dae2d12312a7a7169daec530e3ffe6b91df9dd8240f5d')},
 (1, 1): {'old_cell': (2, 3),
          'model_sha256': 'a5fa9d8f8ab186b7cda574ea6cc7c1539e756a4aee759de4dbebd4202a0701b3',
          'path_sha256': '41469cb48503b94f49483ac91e29dab089f2ae9b4b9310834f1f7cbc568ba1ed',
          'shadow_sha256': ('3129f50b6a7b41c58e3d115e08584a7736e12e0bdac8892dab1aa0f9427146e1',
                            '78de091fda28f0f020a1539c515e4a8953bf159351bd74a5f287a530a74ebe36',
                            '830f1aec7d95981fbc0437a848d4ad3ad34eaf0a89c072e7187747394145ea71',
                            '8979596bf7305ed92c0f1f091b673fae49fc8d5d6f4d369d573508f8e7466836',
                            'e04dd666811758166868c821d9ac421e1e1d1651a64297679d41fcafc526175f')},
 (2, 1): {'old_cell': (3, 3),
          'model_sha256': '02b6aaaaffa6c07ad253e2c45efbb6b6709dbd64cce12672f3ce80556f29549a',
          'path_sha256': '16d4a4c57486aedf001496e5a4d0ec20b66bb3d9df2ee37bdee4eb5cd0ed152a',
          'shadow_sha256': ('6a156bfd3207f6b49dbe9c824d3626f39b9223834276c74154e41d0a4c05d505',
                            'ff6899740fd3c4286ec28ed24efd72936eb25fff5c5b0fcf4f690355dd0f08d1',
                            '2499afcfbf1d59f85f68be82183db419063bc8428e8aea3ebebf3b56db5dc4fe',
                            'bfc0f3c5b1394309a28dc7ce703d4ccb698387aac3d2826761826b0012622b8f',
                            'b46242127386547f88c575fa3227e1ef2368207ddbc0758635bf8bd5aff474c8')},
 (3, 1): {'old_cell': (4, 3),
          'model_sha256': '8d7a29768be30c12b9325315608b46c26ab01c3b2b0af46d8ca20913315beb91',
          'path_sha256': '41469cb48503b94f49483ac91e29dab089f2ae9b4b9310834f1f7cbc568ba1ed',
          'shadow_sha256': ('346404e4cdcf4fb0444d344e3f1b184af4a64a69019d70453b7589574213f4cc',
                            '4b507c5edbabb8830023c36914cb1fa3003537e11001d6ee733d15a2b1c60f70',
                            'da5c54e4e5815de7edc6e020dd54613d95cfd9399d04d9c46a2e8e7ae24c5095',
                            '4e779bb793c0a3fe73b4efa648fa4881d8f6b03a92940ee20e7f52f40c4ef8cf',
                            'dd1748336dcc18735a141841439ebd8a822fdd252b8b59261f11f1f6a242289e')},
 (0, 2): {'old_cell': (1, 4),
          'model_sha256': '11b6d8dfa48e526a81b63ab02d265aac0fb18a4469ab1764a99b601671f9d861',
          'path_sha256': 'bb6d40d7ac8962529b7d1d6aa614dae1b1310148f1d467b70228ae1bea077744',
          'shadow_sha256': ('ed0ba1eefc04281bf996deb1232813b9558913b90abc91fb7e11a681049554f2',
                            'fbb068b8caf2806262bebef1417022f53f0b22e5c239e4467d6b55aee5686a3c',
                            'c06d0c65f9535805e2727a0f1fdb79898060c51cc8f84a75d31340b681a27b93',
                            '53c3402b65bd29015e44fc0cdb57e9c1584336230d0cf776dad2f9d06f8f5a78',
                            '23a05e74545f5d976f6d65df393bdda87a5452fd0d0f0553e55c77847e3d9e2d')},
 (1, 2): {'old_cell': (2, 4),
          'model_sha256': '168096349e13a0ddba30abed76d838438cb291c5c8d431c882ee6c82ff21f2a8',
          'path_sha256': '7dc91b6f8de0341ecd0a0d97cc4264d6e805916c0899bac6f23e6c919adcb0d2',
          'shadow_sha256': ('2c0d9ffdfdfb363e8f7cd88cee95e39664955fcb4657f567b6bdaf4348dfd5ef',
                            '86cccc9e9464a59bc890fd4e2bdab6cba9561eaae3461deb4dbed49c41ee3c58',
                            '1edd0a2b6b70d3a665a9deea89c48e6456c94e801b7002f8a6c97ce24a04aac5',
                            '057c6f7e812a2ea8aeb3aea0e926c334d3275d627dc0e408e91d3a93c6302481',
                            '7b8f09e5e977b667682de971945c8d4d4b8356301ddb41f9a71cf89b3b5c1af8')},
 (2, 2): {'old_cell': (3, 4),
          'model_sha256': '9d37cd0b6e61bfbc83bd97260323faee18f9a5e0368195e33af5c43afa1f3ca6',
          'path_sha256': '26739a95ef096cba8e8f9147580bfa48ea8ca5126f42b5d798e4d91371d3f849',
          'shadow_sha256': ('c6b53ea9cd8423c8b6d9b414dfa07725224b220c2971392223dd09180a2bac9f',
                            'd07109aced729a5bc41bfcb4d8dab376d51701e9a54fc7b69fcf05550ea23a83',
                            'e74ddc662e3ddd40d5c905476d68d2f67824ab3a9aa8fa24f1a6b12210aceeeb',
                            '2b370c1af360ec8224333257b5513f9506ab2904e901f1c920c053205b8148bf',
                            'ee40c799eb9bb7466a074e6e2a949699da39453d87d1797bed24b71c8f7f3451')},
 (3, 2): {'old_cell': (4, 4),
          'model_sha256': '1e8f1c0ab0bbd3b7baa150f760d732612a0a912950962a711cdf0cf7bd4fd088',
          'path_sha256': '298339d654160ce8b59169483543a1b69f39c11aaf01be7ae368634ce3c5ed1d',
          'shadow_sha256': ('3473a448ba3caecfbbc5494caea1dc5a4975dcd5d53e28c0d82b8cedb1208f05',
                            'e222e57b410f84c94dbd0ba861ecf8a951a64186e377fc184412fbc69ba75418',
                            '1709c673ef50b707d3cbd9854dd7a1eeb5dd21ad25d97aa44f772f95684740a3',
                            'a371304c00a8ca2a1056de147f5525453c9f3bb59c24c619f2d714de31d64c7e',
                            '6f1a5e2db927be39c74d33566915bb5ae98fc13b7195f48fd7ec2f6af87f2aa1')},
 (4, 2): {'old_cell': (5, 4),
          'model_sha256': '572309b6cdac484c51482d880aaad9ee351d29afda3483825856e18e5a209727',
          'path_sha256': '4436273bd66af492acca9f7ef9c384a2213a4a42300dbbeb55997896d321c580',
          'shadow_sha256': ('240ae21a7b115e7fccc5cf9754db8af002e90455173fa56a79d122ab3c00b2c6',
                            'cdeef00e6c6fa881bfd55f908f8083649b03bc07739d011fd048b7ed1bdb8efd',
                            '7fe7b830ca5a59e311ff07c930075c51a2fdded221fa679a99f25358534d2d47',
                            'f5120868fff198ba623794791112b9341e0892a0991369c8deec14b32b86fde9',
                            'f3d3e3121defe91896318368b340e8697e33287bec2ce92edc434b6711584fce')}}


def _tiles(spec):
    require(spec['recipe'] == CORE_RECIPE, 'Retained fan-core pins require their own recipe')
    cells = [tuple(cell) for cell in spec['cells']]
    require(cells == list(PINS), 'Fan core must retain exactly its nine independently pinned cells')
    require(len(spec['tile_ids']) == len(cells), 'Fan core tile list is incomplete')
    return {cell: int(tile, 16) for cell, tile in zip(cells, spec['tile_ids'])}


def audit_retained_core_paths(resources, spec):
    tiles = _tiles(spec)
    for cell, tile in tiles.items():
        raw = resources[*PATH, tile]
        require(hashlib.sha256(raw).hexdigest() == PINS[cell]['path_sha256'],
                f'Fan core changed an approved retained PATH: {cell}')
    return {'exact_retained_path_cells_checked': len(tiles)}


def audit_retained_core_resources(resources, spec):
    report = audit_retained_core_paths(resources, spec)
    tiles = _tiles(spec)
    for cell, tile in tiles.items():
        for zoom in range(5):
            model = resources[*S3D, tile+zoom]
            require(hashlib.sha256(model).hexdigest() == PINS[cell]['model_sha256'],
                    f'Fan core reshaped an approved retained model: {cell}, zoom={zoom}')
            shadow = resources[0x7ab50e44, 0x2bc2759a, tile+zoom]
            require(hashlib.sha256(shadow).hexdigest() == PINS[cell]['shadow_sha256'][zoom],
                    f'Fan core changed an approved retained shadow: {cell}, zoom={zoom}')
    return {**report, 'exact_retained_model_zoom_resources_checked': len(tiles)*5,
            'exact_retained_shadow_zoom_resources_checked': len(tiles)*5,
            'retained_geometry_and_uv_bytes_unchanged': True,
            'original_fan_local_to_core_offset_cells': [1, 2],
            'retained_fan_source_dat_sha256': SOURCE_DAT_SHA256}
