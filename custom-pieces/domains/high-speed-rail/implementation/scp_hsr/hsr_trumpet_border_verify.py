"""Current border-piece integration, separate from frozen redesign evidence.

Every selected archive is independently fixed before assembly capture. The
current fan core and recessed-web straight preserve the accepted fan profile;
its two PATH encodings are checked against exact directed straight geometry.
Frozen historical records retain their original inputs and verification scope.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json
from pathlib import Path

from scp.dbpf import require
from scp.verification_fixtures import resource_descriptor
from .assembly_inspection import _world_triangles, sha256, number
from .hsr_merge_extraction_verify import (
    REPLACEMENT, SEAM, SUPPORTS_SHA256, audit_collar_sections,
)
from .hsr_trumpet_rework_verify import (
    CURRENT_LAYOUT, ROUTE_MOVEMENT_POLICY, audit_recorded_route_movement,
    _projected_tile_intersection_area, _tile_intersection_surface_area,
)

ROOT = next(path for path in Path(__file__).resolve().parents if (path/'project.json').is_file())
ASSEMBLY_RELATIVE = Path('domains/high-speed-rail/01_assemblies/straight-stem-trumpet')
SNAPSHOT_RELATIVE = Path('evidence/design-history/before-border-piece-integration')
SNAPSHOT_INDEX_SHA256 = '081bb2475ef153d0b6df13d9d1bb21bf190f6cd8a427ad56f654728a1661cbd4'
STANDALONE_REVISIONS_SHA256 = '94c4679fed3b33cc0af14fe5f8734d752b1c7d180c0ae73df5c7d4496b516163'
CURRENT_TILE_TRIANGLES = 715251
INITIAL_INTEGRATION_MANIFEST_SHA256 = '4e3787d481cc6399286e617c67501495af709206066c5ff4c2fb02a8a775927b'
CURRENT_EMPTY_PROOF_SHA256 = 'cadf3903c371af113a7b8d655953659e0ec09d4ef5c862bd9bf9c91ab054be60'
CURRENT_MODEL_SCOPE_AUDIT_SHA256 = '245640cfe92b71a24a557bf7c71edd32048c0bd466d210eff7f45d9b91a8a6a0'
CURRENT_JOIN_AND_ROUTES_SHA256 = '40b07c5aa44c458e58bce854dd7aa812c9ebf7d990b2122b990eeabea89efb82'
REPAIRED_ARCHIVES = {
    'hsr-component-l2-short-mainline-diverge-core': 'd2666cde677ef29a179e4fc30e6cd1cbd1d4d617f931b4939bdeebea1704a300',
    'hsr-component-l2-paired-fan-compact-join': '54086c7a5423f0d121d732d1b8081c1984e0663afb3d3c8a4604cdcc5b43c797',
    'hsr-component-modular-south-junction': 'b650626efc9c0fb40b68d726348def8dffe8db22dadd748f191b9ed15b6882bb',
    'hsr-component-l2-short-opposed-merge-core': '14b9c18738ef1daa652f5834f2d4bf78a824d0894f974574288cab5bd264be4d',
}
IDENTITY_FIELDS = ('id', 'recipe', 'puzzle_id', 'menu', 'effect_name', 'preview_id',
                   'tile_ids', 'cells', 'footprint', 'orientation_count', 'orientation_policy',
                   'ports', 'movements', 'component', 'structural_cells', 'shadow_mappings', 'asset_file')
ACCEPTED_WEDGE_SHADOW_TRANSITION = {'piece_id': 'hsr-component-modular-south-junction',
 'accepted_wedge_geometry_sha256': 'd0c24a85209a56f0ac3e924b3f66e9ee291fd8362e65726c975b1033eaf3066a',
 'accepted_wedge_dat_sha256': '9515ce33d06dbfbede515bb7d0c0a9224140b30b3f5ac97c696d9a2bf7c43a2b',
 'current_approved_dat_sha256': 'b650626efc9c0fb40b68d726348def8dffe8db22dadd748f191b9ed15b6882bb',
 'original_wedge_comparison_sha256': 'a946a2856ff8fab56987eb1c2644979ae6385bfa6d59c07c8faaf0feb17d9511',
 'resources': [{'local_cell': [0, 2],
                'zoom': 0,
                'resource_id': '7ab50e44-2bc2759a-7f58c020',
                'before_sha256': 'd3c6b3ac823ff1654d422a9d14da86a51a01ec34b78039ed3d45db1eaba779e8',
                'after_sha256': 'f6cb95bee4e184d9fcf4be8b93465e0a4e34381945c5b5aa0429c5a4f5ff9458'},
               {'local_cell': [0, 2],
                'zoom': 1,
                'resource_id': '7ab50e44-2bc2759a-7f58c021',
                'before_sha256': '6f131fd4e602dd9fc15e204a89c51d15708291a897ea80e941f7a16e1e73ea03',
                'after_sha256': 'ea440da7cd408340ceb20a15aee9ea2ad13c0cfccaa5c22a76d3b9334906cd90'},
               {'local_cell': [0, 2],
                'zoom': 2,
                'resource_id': '7ab50e44-2bc2759a-7f58c022',
                'before_sha256': '338197ea17732a1ab6ff931440a6721c8aacfe2dae6c8db95cd9d79cf42588c2',
                'after_sha256': 'f25e6d85f92aef1efcfd5e72dc3326060b63d4d6b7c095d8b3073bb087d6ec29'},
               {'local_cell': [0, 2],
                'zoom': 3,
                'resource_id': '7ab50e44-2bc2759a-7f58c023',
                'before_sha256': '98f9f93de4a29175f8446e0cf27cf01f11226496c40fec133eade23670e8780f',
                'after_sha256': 'd12b790d8f47d9ae10a59468054394b79d01b7dbdf6ef74ebb06fbd48dc04f68'},
               {'local_cell': [0, 2],
                'zoom': 4,
                'resource_id': '7ab50e44-2bc2759a-7f58c024',
                'before_sha256': '0c5ca68aa70f001eb050efdc49d0c237342b0c361bd0a39c112a831485a1158d',
                'after_sha256': '63d2b36e4d519d1b824e6f4aff5fb740a1b0a6ce0da2f9c476963d3c916e0127'},
               {'local_cell': [1, 2],
                'zoom': 0,
                'resource_id': '7ab50e44-2bc2759a-7f58c120',
                'before_sha256': '0d5cfe575e9fded2408b3caec5ef531e1bc116b23d07396c1ac68150e0602b79',
                'after_sha256': 'f90b3523f771466c684395d4349aa42ab129a3d103dd01b5d8cc1045f2c10ac2'},
               {'local_cell': [1, 2],
                'zoom': 1,
                'resource_id': '7ab50e44-2bc2759a-7f58c121',
                'before_sha256': '47638667e9907b567a30d914c390f37edd8fae601f0c247d0e284c6a1b00a12f',
                'after_sha256': 'bc179cf4daab39338259ce310c79eb635211b7ba2d85532acd8a0bfb32eb1409'},
               {'local_cell': [1, 2],
                'zoom': 2,
                'resource_id': '7ab50e44-2bc2759a-7f58c122',
                'before_sha256': 'd3fe50cacab77b419c59a15e194582b35e2ca10a74136d721d73e98d0be935d8',
                'after_sha256': '0e292d77b191303bbbb5b2a8f6b38db2fbaf2d1cee0e433c470829355d1893dd'},
               {'local_cell': [1, 2],
                'zoom': 3,
                'resource_id': '7ab50e44-2bc2759a-7f58c123',
                'before_sha256': '4b7dd6ba0ec14aeb9242eb5b30da0e720d443fbdb4e5930dd7472f7635d9ba8c',
                'after_sha256': 'f22537853e4049367871bedd85d3a62cd1112cb0d960241d915dc61fbddf08ab'},
               {'local_cell': [1, 2],
                'zoom': 4,
                'resource_id': '7ab50e44-2bc2759a-7f58c124',
                'before_sha256': '33f2f60a70dc39d256c3db6d04a25b12b96cb6a2b1b1c9aa944b83044bc8be72',
                'after_sha256': 'a69fb0276cf8d1284cf6594ecbed6dec30c83926e95b22dcd78647a943862b73'},
               {'local_cell': [2, 2],
                'zoom': 0,
                'resource_id': '7ab50e44-2bc2759a-7f58c220',
                'before_sha256': 'fca62d0dc9a2061c1e59aab5d149a98593989b26dd785afedd1e578e2008ca9a',
                'after_sha256': '216a5a926c141e6a0788a061c31f085ec12230a833cb94db68bf02b6cf892ac9'},
               {'local_cell': [2, 2],
                'zoom': 1,
                'resource_id': '7ab50e44-2bc2759a-7f58c221',
                'before_sha256': '400756b43e41fbd2c63f8c2d3c39ddced3ec82c37ff03ce8a3fd6995feb2415b',
                'after_sha256': 'f90e7c0a5531b4aecd6ac9afd4221eb11fc5f2c4833de83c57310cd8ff2b5826'},
               {'local_cell': [2, 2],
                'zoom': 2,
                'resource_id': '7ab50e44-2bc2759a-7f58c222',
                'before_sha256': '0664237c3267e0cee2909a383ddff572df86421f6d5e1463a5bac47a06235e83',
                'after_sha256': '54d2f1753cb0b039f9529f8f8fb3a8059683bdf5186312dca83eae36e31288ad'},
               {'local_cell': [2, 2],
                'zoom': 3,
                'resource_id': '7ab50e44-2bc2759a-7f58c223',
                'before_sha256': '287c2d82d979b67d48a019825e1cb47d7815157a84a4fb4e9678b502d3af01d2',
                'after_sha256': 'a7d7b0e34ab05946116a9cd33c73b1b0b3d195aafb0d3ffdbefe6aa1db4a9dc4'},
               {'local_cell': [2, 2],
                'zoom': 4,
                'resource_id': '7ab50e44-2bc2759a-7f58c224',
                'before_sha256': 'b15d62a9a4701f21534677e4ec178d8becfed519fce3774643fe4c6c28a90b5f',
                'after_sha256': '9fd2999a9f6f4fd1f2672ed8d95bb7b0b61ef87ecce472a77a4125d146a0b1ab'}]}
CORE_ID = 'hsr-component-l2-paired-fan-compact-core'
FULL_FAN_ID = 'hsr-component-l2-paired-fan-compact-join'
STRAIGHT_ID = 'hsr-component-l2-paired-straight-recessed-web'
CURRENT_INTEGRATION_LAYOUT = '5bcb0546c645a95f5cfdcc77134362047ba98af42320395a57160f14d26c670e'
CORE_ARCHIVE_SHA256 = '7e0bfa1104cf42f55aa8e193ad97ff69b457da044861346f5e7e51222db9e3dd'
CORE_SOURCE_INPUTS = {'piece.json': '69339858ff584deeacc8934ab845b55947d977147c865077d52540b612ce548f',
 'geometry.json': '8ee99c79beec4dc3f45fcc8419a19910d025c76e9e3ddc4ef0a12bde97ef5874'}
STRAIGHT_ARCHIVE_SHA256 = '7330c6abb5ee5f5c36897530c252e971d9943843d0ddc03cd22a3fd3ecb92375'
STRAIGHT_SOURCE_INPUTS = {'piece.json': '7a2437293a85c2a0b5fd8153d9bdaab196c66b23721927f02b21aae650656096',
 'geometry.json': '520858866e0bebbfc24e4e7af67a735c2d2d784e3fc32702817e3a48896ffb28'}
STRAIGHT_IDENTITY = {'id': 'hsr-component-l2-paired-straight-recessed-web',
 'recipe': 'hsr_component_l2_paired_straight_recessed_web',
 'puzzle_id': 'f829',
 'menu': {'id': '6a47f829', 'order': '7012f829', 'style': 'hsr-component-l2-paired-straight-recessed-web'},
 'effect_name': 'preview_scp_f829________001',
 'preview_id': '7f586ff5',
 'tile_ids': ['7f586000'],
 'cells': [[0, 0]],
 'footprint': [1, 1],
 'orientation_count': 8,
 'orientation_policy': 'rotate-only-preserve-direction',
 'ports': {'N': {'in': [-2.0, 8.0, 15.5], 'out': [2.0, 8.0, 15.5]},
           'S': {'in': [2.0, -8.0, 15.5], 'out': [-2.0, -8.0, 15.5]}},
 'movements': [['N', 'S'], ['S', 'N']],
 'component': {'custom_curved_interfaces': False,
               'kind': 'partition_component',
               'support_centers': [[0.0, 0.0]],
               'support_foundation_width': 1.3,
               'support_min_spacing': 16.0},
 'structural_cells': [],
 'shadow_mappings': [{'rotation': 0, 'source': '7f586000', 'tile': '7f586000'}],
 'asset_file': 'zzz_Simons_Custom_Pieces/20_Pieces/SCP_hsr-component-l2-paired-straight-recessed-web.dat'}
STRAIGHT_PATH_SHA256 = '41dfafc4ef2c1cf41cf838382b088cafe3bbe704b88dc4ee3e220d6cd7c748ef'
FAN_CORE_ATOMIZATION_SHA256 = '4a8ed74719cad1fa58c4cebc545ecb9be20d97fca68fe6ad5f4afeebccffb181'
EXTRACTED_STANDALONE_EVIDENCE = {'hsr-component-l2-paired-fan-compact-core': {'evidence/fan-core-extraction.json': 'd3f422393ddbab0972115bfef16e97996c9a30ff582c17767cc519e2252c1868'},
 'hsr-component-l2-paired-straight-recessed-web': {'evidence/straight-extraction.json': '9320f6a0ae56efd8046d39069f45f8fcb5431ab183ff22acfb22d687934b55df'}}
FAN_ATOMIZATION_INPUTS = {'evidence/fan-atomization-review.json': '4a8ed74719cad1fa58c4cebc545ecb9be20d97fca68fe6ad5f4afeebccffb181',
 'evidence/fan-atomization-audit.py': '9137ed3e99662273e6d0601b8dd5302542b057df6005acf482c3b67cf0c212bc',
 'previews/fan-atomization-review.png': '6c1e5c8ce2525ddaba604557352b8111deee1529206774c19bbb332850a8bab5',
 'previews/fan-atomization-review.svg': 'bf807e35f8b69db49aee956edb1493364dc24fe9eb44c0697b12d42b92f247d3',
 'evidence/fan-core-parts-build.json': '8f233c16164fc8055014d173181d8cd829ffb3fb8f69962885eba62c9b560fee'}
CORE_IDENTITY = {'id': 'hsr-component-l2-paired-fan-compact-core',
 'recipe': 'hsr_component_l2_paired_fan_compact_core',
 'puzzle_id': 'f7a8',
 'menu': {'id': '6a47f7a8', 'order': '7012f7a8', 'style': 'hsr-component-l2-paired-fan-compact-core'},
 'effect_name': 'preview_scp_f7a8________001',
 'preview_id': '7f505ff5',
 'tile_ids': ['7f505200',
              '7f505110',
              '7f505210',
              '7f505310',
              '7f505020',
              '7f505120',
              '7f505220',
              '7f505320',
              '7f505420'],
 'cells': [[2, 0], [1, 1], [2, 1], [3, 1], [0, 2], [1, 2], [2, 2], [3, 2], [4, 2]],
 'footprint': [5, 3],
 'orientation_count': 8,
 'orientation_policy': 'rotate-only-preserve-direction',
 'ports': {'N': {'in': [30.0, 8.0, 15.5], 'out': [34.0, 8.0, 15.5]},
           'W': {'out': [6.3985185522168635, -40.0, 15.5]},
           'E': {'in': [57.60148144778313, -40.0, 15.5]}},
 'movements': [['N', 'W'], ['E', 'N']],
 'component': {'kind': 'partition_component',
               'support_centers': [[32.0, 0.0], [32.0, -16.0], [16.0, -32.0], [48.0, -32.0]],
               'support_foundation_width': 1.3,
               'support_min_spacing': 16.0,
               'custom_curved_interfaces': True},
 'structural_cells': [[1, 1], [3, 1]],
 'shadow_mappings': [{'tile': '7f505200', 'source': '7f505200', 'rotation': 0},
                     {'tile': '7f505110', 'source': '7f505110', 'rotation': 0},
                     {'tile': '7f505210', 'source': '7f505210', 'rotation': 0},
                     {'tile': '7f505310', 'source': '7f505310', 'rotation': 0},
                     {'tile': '7f505020', 'source': '7f505020', 'rotation': 0},
                     {'tile': '7f505120', 'source': '7f505120', 'rotation': 0},
                     {'tile': '7f505220', 'source': '7f505220', 'rotation': 0},
                     {'tile': '7f505320', 'source': '7f505320', 'rotation': 0},
                     {'tile': '7f505420', 'source': '7f505420', 'rotation': 0}],
 'asset_file': 'zzz_Simons_Custom_Pieces/20_Pieces/SCP_hsr-component-l2-paired-fan-compact-core.dat'}
CORE_RETAINED_TILE_RESOURCES_SHA256 = 'e3b8be70dc59ffa82021710110dc5017bd74ce3268197f2ae051e4a87d27005b'
PRESERVED_COMPLETE_JOURNEY_GEOMETRY = {'E_in>S_out': {'coalesced_points': 1484,
                'coalesced_points_sha256': 'b385b30465cca66aed6b43d68cb6dc29192dd64c82f57af74bed3befe4027640'},
 'E_in>W_out': {'coalesced_points': 2,
                'coalesced_points_sha256': 'af3c934ce6cfbcf2ca860a2f6aa86d684e94bdc400f7e418e9a7d4f0d2d48adc'},
 'S_in>E_out': {'coalesced_points': 526,
                'coalesced_points_sha256': 'feeacb3ad53e4de1f0e990ea7adcef7b958fb751d71334e815f4ce80fe27abb6'},
 'S_in>W_out': {'coalesced_points': 1484,
                'coalesced_points_sha256': '55a3cb46293bb9649918d768f740c6a4a45586cf3d6e08db74982a1335b6f9e0'},
 'W_in>E_out': {'coalesced_points': 2,
                'coalesced_points_sha256': 'c7a7c143ae90dd4a395eb0cb4827f0927bb21b2163875284d621a716b144e4d7'},
 'W_in>S_out': {'coalesced_points': 526,
                'coalesced_points_sha256': '75031f110c3f4cd0a84bc0681f04d40b22701b5603f2aafdb1cd4350cb4248ee'}}
SOURCE_INPUTS = {'hsr-component-l2-paired-fan-compact-join': {'piece.json': '72a02fb797fa076dd834f23046c2e5cdc61cdea86274290ece98e3522cfaa559',
                                              'geometry.json': 'd5366120c1f9c38b8b1eccc7fc8927dabb6e28d8ba1dd08427ed4e0b1c74aa0b'},
 'hsr-component-l2-short-mainline-diverge-core': {'piece.json': '95aa45f59da86eb6c547526f3796a7c91f2a21bd7d0e27724448dd192924290a',
                                                  'geometry.json': 'cba97aca000381fee6d99dce0e63cf35d6be467b57b4e4b0b2db82ef4001cd9c'},
 'hsr-component-l2-short-opposed-merge-core': {'piece.json': '931d14cfe38efaf3aa0dd8aeebdcb5444b5e2b9386ab65d39a752bf58dd439f5',
                                               'geometry.json': '61083be80c1a6d067e4bd05e6434d5eb110b4485bd77452cfa671cad0cb9f6e9'},
 'hsr-component-l2-shortened-departure-curve': {'piece.json': 'cec83605e98877457b2bde84976689e113b95ed1f783d0cb6ad7a84e36e429e8',
                                                'geometry.json': '7ed9e49ca138d574844feab776efc773103b929e3847604034827c43b5a722e2'},
 'hsr-component-l2-shortened-return-curve': {'piece.json': '668ace6a67fef74c1609816ec75868d526dcd15b0de60bbc6c9e16a9285de8f9',
                                             'geometry.json': '0f04d613c74b98134ffd4466be454f3ac6cd646ecf424dab0d45e676ba1b2ef7'},
 'hsr-component-lower-oneway-straight': {'piece.json': '6a3d5332a6610e2b81a51494bd4f1d23abd89f60959ea200ded91370fc00987d'},
 'hsr-component-lower-paired-straight': {'piece.json': 'e9d39b4cc65ed2e60527cc99be2b57c47eb7fe3bbcbec1a3419f2239af4b6265'},
 'hsr-component-modular-crossing-core': {'piece.json': '0087e27275a2c11ee126ce4254ded8a1f22eb18fe7448ae2b7062a4ef7a2a90f',
                                         'geometry.json': '8a5cfc5a7b58063453447b47d525527dd58a3a46446173ae6c87d6f7e5fd2940'},
 'hsr-component-modular-paired-climb': {'piece.json': '0d67af67113bdf0d99fac71f74ff35c6f9e1d5596f5e2480e55a88d23cfe04e3',
                                        'geometry.json': '0ffa98fb47a7040d8cd3ca7d6b1666aaa9e1c56e41515e8ec058569a36236601'},
 'hsr-component-modular-south-junction': {'piece.json': '71beee10351c0d7e9cc20a5900c94ec7dec3737ddceaf7629a6a0286799114b0',
                                          'geometry.json': 'fda2275ea4013c2e9333e3904fc8e5f96de483ce12982c7d45e2fc4d3485ef5e'},
 'hsr-component-tight-paired-curve90-l4-to-mid': {'piece.json': '7967dbcd0bb8d434b5d7370774ab335a2c57616acf7014df2bd7dc6753147b01'},
 'hsr-component-tight-paired-curve90-mid-to-l2': {'piece.json': '02c1f5df59cead74c201b86f9af24d09f382e6199f305809dfbb4ea9572feb33'},
 'hsr-component-upper-paired-straight': {'piece.json': 'be891f6d7797899c98adcd21b88973903ca8e71b1bcab3c65c4f39f6bae368e3'}}


def canonical_sha256(value):
    return sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode())


def frozen_inputs(root=ROOT):
    """Check every retained pre-integration byte before using its facts."""
    snapshot = Path(root)/ASSEMBLY_RELATIVE/SNAPSHOT_RELATIVE
    index_raw = (snapshot/'index.json').read_bytes()
    require(sha256(index_raw) == SNAPSHOT_INDEX_SHA256,
            'Trumpet border integration frozen snapshot index differs')
    files = json.loads(index_raw)['files']
    require(len(files) == 47, 'Trumpet border integration frozen snapshot inventory differs')
    for item in files:
        require(sha256((snapshot/item['path']).read_bytes()) == item['sha256'],
                'Trumpet border integration frozen snapshot file differs: '+item['path'])
    return {'snapshot': snapshot,
            'descriptor': resource_descriptor(snapshot/'checks/resources.json'),
            'manifest': json.loads((snapshot/'evidence/audited-build-manifest.json').read_text()),
            'ledger': json.loads((snapshot/'checks/atomization.json').read_text()),
            'scene': json.loads((snapshot/'assembly.json').read_text())}


def audit_source_inputs(root=ROOT):
    """Bind original authorship, both extracted pieces, and seven historical rows."""
    for identifier, files in SOURCE_INPUTS.items():
        folder = Path(root)/'domains/high-speed-rail/00_pieces'/identifier
        for relative, digest in files.items():
            require(sha256((folder/relative).read_bytes()) == digest,
                    'Trumpet border integration current source input differs: '+identifier+'/'+relative)
    ledger = json.loads((Path(root)/ASSEMBLY_RELATIVE/'checks/atomization.json').read_text())
    require(canonical_sha256(ledger.get('subsequent_piece_revisions')) == STANDALONE_REVISIONS_SHA256,
            'Trumpet border integration changes its seven standalone history rows')
    for identifier, inputs in ((CORE_ID, CORE_SOURCE_INPUTS), (STRAIGHT_ID, STRAIGHT_SOURCE_INPUTS)):
        require(inputs, 'Trumpet extracted piece awaits its final independently verified source pins: '+identifier)
        folder = Path(root)/'domains/high-speed-rail/00_pieces'/identifier
        for relative, digest in inputs.items():
            require(sha256((folder/relative).read_bytes()) == digest,
                    'Trumpet extracted piece source input differs: '+identifier+'/'+relative)
    require(isinstance(FAN_CORE_ATOMIZATION_SHA256, str)
            and sha256((Path(root)/ASSEMBLY_RELATIVE/'evidence/fan-atomization-review.json').read_bytes()) == FAN_CORE_ATOMIZATION_SHA256,
            'Trumpet fan atomization awaits or differs from its independently reviewed profile and cap decision')
    require(EXTRACTED_STANDALONE_EVIDENCE, 'Trumpet extracted pieces await their final standalone evidence pins')
    for identifier, inputs in EXTRACTED_STANDALONE_EVIDENCE.items():
        for relative, digest in inputs.items():
            require(sha256((Path(root)/'domains/high-speed-rail/00_pieces'/identifier/relative).read_bytes()) == digest,
                    'Trumpet extracted piece standalone evidence differs: '+identifier+'/'+relative)
    require(FAN_ATOMIZATION_INPUTS, 'Trumpet fan atomization awaits final replay and drawing pins')
    for relative, digest in FAN_ATOMIZATION_INPUTS.items():
        require(sha256((Path(root)/ASSEMBLY_RELATIVE/relative).read_bytes()) == digest,
                'Trumpet fan atomization evidence, replay source, or drawing differs: '+relative)
    return {**deepcopy(SOURCE_INPUTS), CORE_ID: deepcopy(CORE_SOURCE_INPUTS),
            STRAIGHT_ID: deepcopy(STRAIGHT_SOURCE_INPUTS)}


def piece_identity(piece):
    return {name: piece[name] for name in IDENTITY_FIELDS if name in piece}


def expected_archives(frozen):
    require(isinstance(CORE_ARCHIVE_SHA256, str) and len(CORE_ARCHIVE_SHA256) == 64,
            'Trumpet fan core awaits its final independently verified standalone DAT')
    expected = {piece['id']: piece['sha256'] for piece in frozen['descriptor']['pieces']
                if piece['id'] != FULL_FAN_ID}
    expected.update({key: value for key, value in REPAIRED_ARCHIVES.items() if key != FULL_FAN_ID})
    require(isinstance(STRAIGHT_ARCHIVE_SHA256, str) and len(STRAIGHT_ARCHIVE_SHA256) == 64,
            'Trumpet recessed-web straight awaits its independently verified standalone DAT')
    expected[CORE_ID] = CORE_ARCHIVE_SHA256
    expected[STRAIGHT_ID] = STRAIGHT_ARCHIVE_SHA256
    return expected


def expected_current_placements(frozen):
    """Apply only the three independently reviewed P06 replacement poses."""
    original = next(item for item in frozen['scene']['placements'] if item['label'] == 'P06')
    core = deepcopy(original)
    name = 'HSR Level 2 Compact Paired Fan Core'
    core.update(name=name+' at P06', piece_id=CORE_ID, recipe='hsr_component_l2_paired_fan_compact_core',
                origin_m=[80., 48.], menu_name=name, display_origin_m=[192., 256.],
                display_origin_tiles_en=[12., 16.])
    extras = []
    for label, north, display_y in (('P06A', 80., 18.), ('P06B', 64., 17.)):
        straight = deepcopy(original)
        straight.update(name='HSR Level 2 Paired Straight with Recessed Web at '+label, instance_id=label, label=label,
                        piece_id=STRAIGHT_ID, recipe='hsr_component_l2_paired_straight_recessed_web',
                        origin_m=[112., north], menu_name='HSR Level 2 Paired Straight with Recessed Web',
                        display_origin_m=[224., north+208.], display_origin_tiles_en=[14., display_y])
        extras.append(straight)
    result = []
    for placement in frozen['scene']['placements']:
        result.extend([*extras, core] if placement['label'] == 'P06' else [deepcopy(placement)])
    return result


def integration_policy(frozen):
    cells = [row['world_east_north_m'] for row in frozen['descriptor']['world_cells']
             if row['piece_id'] in REPAIRED_ARCHIVES]
    return {'allowed_model_piece_ids': sorted([key for key in REPAIRED_ARCHIVES if key != FULL_FAN_ID]+[CORE_ID, STRAIGHT_ID]),
            'allowed_changed_placements': ['P01', 'P04', 'P06', 'P06A', 'P06B', 'P07', 'P08'],
            'allowed_model_world_cells_east_north_m': sorted(cells),
            'unchanged_complete_archives': 9, 'unchanged_world_cells': 68,
            'unchanged_world_path_sets': 103, 'exact_recessed_web_straight_path_substitutions': 2,
            'unchanged_world_shadow_sets': 102,
            'accepted_wedge_shadow_transition': deepcopy(ACCEPTED_WEDGE_SHADOW_TRANSITION),
            'complete_directed_journey_geometries_preserved': 6, 'support_positions_preserved': 74,
            'retained_piece_and_resource_identities_preserved': True,
            'new_core_identity': deepcopy(CORE_IDENTITY),
            'new_recessed_web_straight_identity': deepcopy(STRAIGHT_IDENTITY),
            'fan_core_atomization_decision_sha256': FAN_CORE_ATOMIZATION_SHA256,
            'fan_atomization_evidence': deepcopy(FAN_ATOMIZATION_INPUTS),
            'extracted_piece_standalone_evidence': deepcopy(EXTRACTED_STANDALONE_EVIDENCE),
            'profile_scope': 'Preserve the accepted recessed structural web and original northern transition; canonical open straight excludes the original northern end cap only as explicitly recorded in the atomization decision.',
            'new_core_retained_tile_payload_sha256': CORE_RETAINED_TILE_RESOURCES_SHA256,
            'fan_core_rebase_old_cell_offset': [1, 2],
            'full_fan_retained_in_library_unchanged': True,
            'old_full_fan_approved_archive_sha256': REPAIRED_ARCHIVES[FULL_FAN_ID],
            'independently_approved_current_archives': expected_archives(frozen)}


def _core_tile_payload(resources, piece):
    result = []
    for cell, tile in zip(piece['cells'], piece['tile_ids']):
        iid = number(tile)
        hashes = {'path': sha256(resources[0x296678f7, 0xa966883f, iid])}
        for zoom in range(5):
            hashes['model_'+str(zoom)] = sha256(resources[0x5ad0e817, 0xbadb57f1, iid+zoom])
            hashes['shadow_'+str(zoom)] = sha256(resources[0x7ab50e44, 0x2bc2759a, iid+zoom])
        result.append({'old_cell': [cell[0]+1, cell[1]+2], 'new_cell': cell,
                       'resources_sha256': hashes})
    return result


def _world_identity(old):
    if old['piece_id'] != FULL_FAN_ID:
        return old['piece_id'], old['cell'], old['rotation_quarter_turns_ccw'], None
    if old['cell'] == [3, 0]:
        return STRAIGHT_ID, [0, 0], 0, 'P06A'
    if old['cell'] == [3, 1]:
        return STRAIGHT_ID, [0, 0], 0, 'P06B'
    return CORE_ID, [old['cell'][0]-1, old['cell'][1]-2], 0, 'P06'


def audit_border_scope(tiles, build, scene, *, root=ROOT):
    """Preserve exact approved DATs and permit only the two reviewed extractions."""
    frozen = frozen_inputs(root)
    audit_source_inputs(root)
    baseline = frozen['descriptor']
    old_pieces = {piece['id']: piece for piece in frozen['manifest']['pieces']}
    approved = expected_archives(frozen)
    require(set(build['pieces']) == set(approved) and len(approved) == 14,
            'Trumpet border integration changes its fourteen selected piece identities')
    require(scene['placements'] == expected_current_placements(frozen),
            'Trumpet fan atomization changes an unapproved placement or its metadata')
    archive_records = {piece['id']: piece for piece in baseline['pieces']}
    shadow_transitions = {item['resource_id']: item for item in ACCEPTED_WEDGE_SHADOW_TRANSITION['resources']}
    for identifier, piece in build['pieces'].items():
        identity = (CORE_IDENTITY if identifier == CORE_ID else STRAIGHT_IDENTITY
                    if identifier == STRAIGHT_ID else piece_identity(old_pieces[identifier]))
        require(piece_identity(piece) == identity,
                'Trumpet border integration changes a permanent piece identity: '+identifier)
        saved = build['resources'](piece)
        require(saved['sha256'] == approved[identifier],
                'Trumpet border integration archive differs from independently approved bytes: '+identifier)
        if identifier == CORE_ID:
            require(canonical_sha256(_core_tile_payload(saved['resources'], piece)) == CORE_RETAINED_TILE_RESOURCES_SHA256,
                    'Trumpet new fan core changes a retained model, PATH, shadow, or local-cell mapping')
            continue
        if identifier == STRAIGHT_ID:
            require(isinstance(STRAIGHT_PATH_SHA256, str)
                    and sha256(saved['resources'][0x296678f7, 0xa966883f, number(piece['tile_ids'][0])]) == STRAIGHT_PATH_SHA256,
                    'Trumpet recessed-web straight PATH differs from its approved saved encoding')
            audit_straight_path_geometry(saved['resources'][0x296678f7, 0xa966883f, number(piece['tile_ids'][0])])
            continue
        hashes = {'-'.join(f'{part:08x}' for part in tgi): sha256(raw)
                  for tgi, raw in saved['resources'].items()}
        old_hashes = archive_records[identifier]['resource_sha256']
        require(set(hashes) == set(old_hashes),
                'Trumpet border integration changes an archive resource identity inventory')
        for tgi, digest in old_hashes.items():
            if tgi.startswith('5ad0e817-'):
                continue
            transition = shadow_transitions.get(tgi) if identifier == ACCEPTED_WEDGE_SHADOW_TRANSITION['piece_id'] else None
            expected_digest = transition['after_sha256'] if transition is not None else digest
            require(transition is None or digest == transition['before_sha256'],
                    'Trumpet accepted wedge shadow transition predecessor differs')
            require(hashes[tgi] == expected_digest,
                    'Trumpet border integration changes a retained non-model resource')
    expected = {tuple(row['world_east_north_m']): row for row in baseline['world_cells']}
    require(len(tiles) == len(expected) == 105 and set(tiles) == set(expected),
            'Trumpet border integration changes the 105 occupied world cells')
    straight_path = STRAIGHT_PATH_SHA256
    changed = []
    for position, old in expected.items():
        tile = tiles[position]
        identifier, cell, turns, label = _world_identity(old)
        require(tile['piece_id'] == identifier and list(tile['cell']) == cell and tile['rotation'] == turns
                and (label is None or tile['instance_id'] == label),
                'Trumpet fan atomization changes a world owner, local cell, or rotation')
        piece = build['pieces'][identifier]
        saved = build['resources'](piece)['resources']
        iid = number(piece['tile_ids'][piece['cells'].index(cell)])
        expected_payload = {'path': saved[0x296678f7, 0xa966883f, iid]}
        for zoom in range(5):
            expected_payload['model_'+str(zoom)] = saved[0x5ad0e817, 0xbadb57f1, iid+zoom]
            expected_payload['shadow_'+str(zoom)] = saved[0x7ab50e44, 0x2bc2759a, iid+zoom]
        require(tile['resources'] == expected_payload,
                'Trumpet placed resources differ from their exact independently approved DAT')
        hashes = {name: sha256(raw) for name, raw in tile['resources'].items()}
        require(set(hashes) == set(old['resources_sha256']),
                'Trumpet border integration changes a placed resource inventory')
        expected_path = straight_path if label in ('P06A', 'P06B') else old['resources_sha256']['path']
        require(hashes['path'] == expected_path,
                'Trumpet fan atomization changes a PATH outside its two exact recessed-web substitutions')
        for zoom in range(5):
            name = 'shadow_'+str(zoom); digest = old['resources_sha256'][name]
            transition = next((item for item in ACCEPTED_WEDGE_SHADOW_TRANSITION['resources']
                               if old['piece_id'] == ACCEPTED_WEDGE_SHADOW_TRANSITION['piece_id']
                               and item['local_cell'] == old['cell'] and item['zoom'] == zoom), None)
            require(transition is None or digest == transition['before_sha256'],
                    'Trumpet accepted wedge world-shadow predecessor differs')
            require(hashes[name] == (transition['after_sha256'] if transition is not None else digest),
                    'Trumpet border integration changes an unapproved shadow')
        if old['piece_id'] not in REPAIRED_ARCHIVES:
            require(hashes == old['resources_sha256'],
                    'Trumpet border integration changes resources outside its reviewed 37 cells')
        elif hashes != old['resources_sha256']:
            changed.append(list(position))
    policy = integration_policy(frozen)
    require(len(policy['allowed_model_world_cells_east_north_m']) == 37,
            'Trumpet border integration model scope differs from its reviewed 37 cells')
    return {'status': 'passed', **policy,
            'actual_model_changed_world_cells_east_north_m': sorted(changed),
            'all_fourteen_archives_match_independent_prior_approval': True,
            'retained_nine_core_tiles_exact_at_all_five_zooms': True,
            'retained_world_PATH_and_shadow_payloads_preserved_except_scoped_transitions': True}


def strictly_coalesced_points(points):
    """Remove only exactly collinear subdivisions without changing any curve."""
    result = []
    for point in points:
        result.append(tuple(point))
        while len(result) >= 3:
            a, b, c = result[-3:]
            u = tuple(b[index]-a[index] for index in range(3))
            v = tuple(c[index]-b[index] for index in range(3))
            if all(u[(index+1)%3]*v[(index+2)%3] == u[(index+2)%3]*v[(index+1)%3]
                   for index in range(3)) and sum(u[index]*v[index] for index in range(3)) >= 0.:
                result.pop(-2)
            else:
                break
    return result


def audit_current_journey_geometry(journeys):
    actual = {'>'.join(movement): {'coalesced_points': len(strictly_coalesced_points(points)),
              'coalesced_points_sha256': canonical_sha256(strictly_coalesced_points(points))}
              for movement, points in sorted(journeys.items())}
    require(actual == PRESERVED_COMPLETE_JOURNEY_GEOMETRY,
            'Trumpet fan atomization changes a complete directed journey geometry')
    return {'complete_directed_journey_geometries_preserved': 6,
            'normalization': 'Only exact collinear intermediate points; no angular or positional tolerance.',
            'complete_journey_geometry_fingerprints': actual}


def audit_current_native_seam(tiles):
    """Retain all six join sections and all 87 original collar sections."""
    from .hsr_atomic_components_verify import _section_intervals
    for position, station in ((REPLACEMENT, 40.-.00000075), (SEAM, 40.+.00000075)):
        triangles = list(_world_triangles(tiles, {position}))
        for height, expected in ((16.189326, [(-7.5, 7.5)]), (14.01067, [(-7.5, 7.5)]),
                                 (16.98933, [(-7.5, -5.9965477), (5.9965477, 7.5)])):
            actual = _section_intervals(triangles, 'east', station, height, 0.)
            require(len(actual) == len(expected) and all(
                abs(a-c) <= .00005 and abs(b-d) <= .00005
                for (a, b), (c, d) in zip(actual, expected)),
                    'Trumpet border integration native joining profile differs')
    return {'actual_native_joining_sections_checked': 6, 'native_profile_tolerance_m': .00005,
            'complete_current_models_independently_pinned': True,
            **audit_collar_sections(_world_triangles(tiles, {SEAM}))}


def audit_preserved_current_journeys(journeys, supports, *, root=ROOT):
    normalized = sorted([round(float(east), 6), round(float(north), 6)] for east, north in supports)
    require(len(normalized) == len({tuple(point) for point in normalized}) == 74
            and canonical_sha256(normalized) == SUPPORTS_SHA256,
            'Trumpet fan atomization changes the seventy-four support positions')
    return {**audit_current_journey_geometry(journeys),
            'support_positions_preserved': 74, 'support_positions_sha256': SUPPORTS_SHA256}


def read_border_integration_record(path=None, *, descriptor=None, root=ROOT, initial_manifest_raw=None):
    """Require a completed current integration with its own exact source scope."""
    assembly = Path(root)/ASSEMBLY_RELATIVE
    path = assembly/'checks/border-piece-integration.json' if path is None else Path(path)
    descriptor = resource_descriptor(assembly/'checks/resources.json') if descriptor is None else descriptor
    raw = path.read_bytes(); record = json.loads(raw)
    require(sha256(raw) == descriptor.get('border_piece_integration_sha256'),
            'Trumpet current border integration record fingerprint differs')
    frozen = frozen_inputs(root)
    require(record.get('schema_version') == 1 and record.get('assembly_id') == 'straight-stem-trumpet'
            and record.get('status') == 'passed', 'Trumpet border integration is not completed')
    require(record.get('baseline_snapshot') == {'directory': SNAPSHOT_RELATIVE.as_posix(),
            'index_sha256': SNAPSHOT_INDEX_SHA256}, 'Trumpet border integration baseline differs')
    require(record.get('policy') == integration_policy(frozen),
            'Trumpet border integration changes its independently approved scope')
    require(record.get('source_inputs') == audit_source_inputs(root)
            and record.get('standalone_revisions_sha256') == STANDALONE_REVISIONS_SHA256,
            'Trumpet border integration source or standalone history binding differs')
    require(record.get('layout_sha256') == CURRENT_INTEGRATION_LAYOUT == descriptor.get('layout_sha256')
            and record.get('scene_sha256') == sha256((assembly/'assembly.json').read_bytes()),
            'Trumpet border integration scene or layout binding differs')
    expected = expected_archives(frozen)
    require({piece['id']: piece['sha256'] for piece in descriptor['pieces']} == expected,
            'Trumpet current descriptor differs from independently approved archive bytes')
    compiled = record.get('compiled_audit', {})
    require(type(CURRENT_TILE_TRIANGLES) is int and CURRENT_TILE_TRIANGLES > 0,
            'Trumpet current integration awaits an independently measured final triangle total')
    if initial_manifest_raw is None:
        initial_manifest_raw = (assembly/'evidence/border-piece-integration-initial-build-manifest.json').read_bytes()
    require(isinstance(INITIAL_INTEGRATION_MANIFEST_SHA256, str)
            and compiled.get('manifest_sha256') == sha256(initial_manifest_raw) == INITIAL_INTEGRATION_MANIFEST_SHA256,
            'Trumpet current integration initial audit manifest differs')
    require(compiled.get('archive_sha256') == expected
            and compiled.get('world_cells_sha256') == canonical_sha256(descriptor['world_cells'])
            and compiled.get('journeys_sha256') == canonical_sha256(descriptor['journeys'])
            and compiled.get('encoded_fragments') == descriptor.get('encoded_fragments') == 166
            and compiled.get('actual_tile_triangles') == descriptor.get('actual_tile_triangles') == CURRENT_TILE_TRIANGLES
            and compiled.get('occupied_cells') == 105 and compiled.get('placements') == 28
            and compiled.get('component_types_checked') == 14 and compiled.get('support_positions') == 74
            and compiled.get('proper_rotations_checked') == 4 and compiled.get('complete_journeys_checked') == 6
            and compiled.get('all_independent_physical_checks_passed') is True,
            'Trumpet border integration compiled audit differs from its exact current resource contract')
    proof = deepcopy(record.get('current_empty_structural_cell_proof', {}))
    audit_current_removed_cell_evidence(proof)
    proof.pop('source_build_manifest_sha256', None)
    require(isinstance(CURRENT_EMPTY_PROOF_SHA256, str)
            and canonical_sha256(proof) == CURRENT_EMPTY_PROOF_SHA256
            and canonical_sha256(record.get('current_model_scope_audit')) == CURRENT_MODEL_SCOPE_AUDIT_SHA256
            and canonical_sha256(record.get('current_merge_join_and_preserved_routes')) == CURRENT_JOIN_AND_ROUTES_SHA256,
            'Trumpet current integration changes independently measured preservation proofs')
    require(record.get('historical_standalone_rows_rewritten') is False
            and record.get('manual_or_game_observations_added') is False
            and record.get('rendering_checked_by_this_record') is False
            and record.get('installed') is False,
            'Trumpet border integration overstates its verification scope')
    return record


def audit_straight_path_geometry(raw):
    """Keep every route flag and its exact directed line through both ports."""
    from scp.track_paths import _parse_paths
    expected = [
        {'transport': 7, 'class': 0, 'entry': 1, 'exit': 3, 'junction': 0,
         'points': [(-2., 8., 15.5), (-2., -8., 15.5)]},
        {'transport': 7, 'class': 0, 'entry': 3, 'exit': 1, 'junction': 0,
         'points': [(2., -8., 15.5), (2., 8., 15.5)]},
    ]
    actual = [{**route, 'points': strictly_coalesced_points(route['points'])}
              for route in _parse_paths(raw)]
    require(actual == expected,
            'Trumpet extracted straight changes directed PATH geometry or route flags')
    return {'exact_directed_straight_routes': 2, 'all_route_flags_preserved': True}


def audit_current_route_movement(current, accepted, journeys):
    """Keep the frozen envelope after only exact collinear PATH subdivision."""
    geometry = audit_current_journey_geometry(journeys)
    audit_recorded_route_movement(current)
    audit_recorded_route_movement(accepted)
    guard = ROUTE_MOVEMENT_POLICY['floating_point_guard_m']
    for actual, baseline in zip(current['journeys'], accepted['journeys']):
        require(all(actual.get(name) == baseline.get(name) for name in
                    ('movement', 'baseline_points_sha256'))
                and max(actual['lower_bound_m'], baseline['lower_bound_m'])
                    <= min(actual['upper_bound_m'], baseline['upper_bound_m'])+2.*guard,
                'Trumpet extracted straight changes the frozen route-movement envelope')
    return {'exact_continuous_geometry_preserved': geometry,
            'original_continuous_distance_intervals_overlap': True,
            'historical_raw_point_hashes_preserved_as_original_facts': True}


def prove_current_removed_structural_cells(build, *, root=ROOT):
    """Inspect every saved core model and preview against all four open holes."""
    import math
    import struct
    from scp.models import parse_s3d
    from scp.render_meshes import _triangles

    frozen = frozen_inputs(root)
    original = json.loads((frozen['snapshot']/'checks/junction-rework.json').read_text())
    removed = sorted(map(tuple, original['removed_world_cells_east_north_m']))
    require(removed == [(64., 16.), (96., 48.), (128., 48.), (160., 16.)],
            'Trumpet current empty-cell scope changes the four historical holes')
    spec = build['pieces'][CORE_ID]
    saved = build['resources'](spec)
    resources = saved['resources']
    require(piece_identity(spec) == CORE_IDENTITY and saved['sha256'] == CORE_ARCHIVE_SHA256,
            'Trumpet empty-cell proof requires the independently approved exact core DAT')
    cells = []
    for east, north in removed:
        local = (int((east-80.)/16.), int((48.-north)/16.))
        require([east, north] == [80.+16.*local[0], 48.-16.*local[1]]
                and list(local) not in spec['cells'],
                'Trumpet removed structural cell is owned by the current core')
        for support_east, support_north in spec['component']['support_centers']:
            owner = (math.floor((support_east+8.)/16.), math.floor((-support_north+8.)/16.))
            require(owner != local, 'Trumpet current core still owns a support in a removed cell')
        cells.append({'local_cell': list(local), 'world_east_north_m': [east, north],
            'positive_area_intersections_by_zoom': [0]*5, 'preview_positive_area_intersections': 0,
            'positive_surface_intersections_by_zoom': [0]*5, 'preview_positive_surface_intersections': 0,
            'path_source_cell_absent': True, 'owned_support_absent': True})
    models = [(number(tile)+zoom, zoom, 16.*cell[0], 16.*cell[1], False)
              for cell, tile in zip(spec['cells'], spec['tile_ids']) for zoom in range(5)]
    models.append((number(spec['preview_id']), 0, 0., 0., True))
    require({tgi for tgi in resources if tgi[0] == 0x5ad0e817}
            == {(0x5ad0e817, 0xbadb57f1, iid) for iid, *_ in models}
            and {tgi for tgi in resources if tgi[0] == 0x296678f7}
            == {(0x296678f7, 0xa966883f, number(tile)) for tile in spec['tile_ids']},
            'Trumpet current core retains an unexpected model or PATH resource')
    checked = []
    for iid, zoom, east, south, preview in models:
        raw = resources[0x5ad0e817, 0xbadb57f1, iid]
        model = parse_s3d(raw)
        count = 0
        for mesh in model['meshes']:
            for frame in set(tuple(item) for item in mesh['frames']):
                for raw_triangle in _triangles(model, frame):
                    points = [struct.unpack_from('<3f', vertex) for vertex in raw_triangle]
                    translated = [(p[0]+east, p[1], p[2]+south) for p in points]
                    projected = [(p[0], p[2]) for p in translated]
                    count += 1
                    for cell in cells:
                        column, row = cell['local_cell']
                        bounds = (16.*column-8., 16.*row-8., 16.*column+8., 16.*row+8.)
                        require(_projected_tile_intersection_area(projected, bounds) == 0.
                                and _tile_intersection_surface_area(translated, bounds) == 0.,
                                'Trumpet current core has saved surface inside a removed structural cell')
        checked.append({'resource_id': f'5ad0e817-badb57f1-{iid:08x}', 'zoom': zoom,
            'preview': preview, 'triangles_checked': count, 'sha256': sha256(raw)})
    geometry = Path(root)/'domains/high-speed-rail/00_pieces'/CORE_ID/'geometry.json'
    proof = {'source_fan_geometry_sha256': sha256(geometry.read_bytes()),
             'source_build_manifest_sha256': build['manifest_sha256'],
             'source_dat_sha256': saved['sha256'], 'core_origin_east_north_m': [80., 48.],
             'manifest_scope': 'Exact manifest at this actual current core projection audit; later documentation-only changes do not change the pinned DAT/model bytes.',
             'projection_rule': 'No positive 3D surface area or X/Z projection inside the open removed tile; exact tile borders are allowed.',
             'checked_model_resources': checked, 'cells': cells}
    audit_current_removed_cell_evidence(proof)
    return proof


def audit_current_removed_cell_evidence(proof):
    """Keep the current rebasing distinct from the frozen full-fan proof."""
    expected = {(-1, 2): [64., 16.], (1, 0): [96., 48.],
                (3, 0): [128., 48.], (5, 2): [160., 16.]}
    require(proof.get('core_origin_east_north_m') == [80., 48.]
            and proof.get('source_dat_sha256') == CORE_ARCHIVE_SHA256
            and proof.get('source_fan_geometry_sha256') == CORE_SOURCE_INPUTS.get('geometry.json')
            and len(proof.get('checked_model_resources', [])) == 46
            and proof.get('projection_rule') == 'No positive 3D surface area or X/Z projection inside the open removed tile; exact tile borders are allowed.',
            'Trumpet current removed-cell proof omits the exact core source or model scope')
    cells = proof.get('cells', [])
    require(len(cells) == 4 and {tuple(item['local_cell']) for item in cells} == set(expected),
            'Trumpet current removed-cell proof changes its local holes')
    for item in cells:
        require(item['world_east_north_m'] == expected[tuple(item['local_cell'])]
                and item.get('positive_area_intersections_by_zoom') == [0]*5
                and item.get('positive_surface_intersections_by_zoom') == [0]*5
                and item.get('preview_positive_area_intersections') == 0
                and item.get('preview_positive_surface_intersections') == 0
                and item.get('path_source_cell_absent') is True
                and item.get('owned_support_absent') is True,
                'Trumpet current removed cell contains saved geometry, a PATH, or a support')
    return {'removed_cells_proved_empty': 4, 'actual_saved_core_model_resources_checked': 46,
            'all_five_actual_native_model_zooms_checked': True, 'core_origin_east_north_m': [80., 48.]}
