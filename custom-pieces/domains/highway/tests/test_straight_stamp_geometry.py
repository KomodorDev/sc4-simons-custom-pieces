"""Check the physical face split, including shared concrete meshes and paint."""
from collections import Counter
from copy import deepcopy
import hashlib
from pathlib import Path
import struct
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'framework'), str(ROOT / 'domains/highway/implementation')]

from scp.models import pack_s3d, parse_s3d, validate_s3d
from scp.recipes import combine_meshes
from scp_highway.ramp_geometry import pack_road_model
from scp_highway.straight_stamp_geometry import matches_frozen_model, source_cells, split_model


def _model(triangles, name):
    model = parse_s3d(pack_road_model(triangles, 0x12345678))
    for mesh in model['meshes']:
        mesh['name'] = name
    return model


def _faces(model):
    result = Counter()
    for mesh in model['meshes']:
        vi, ii, pi, mi = mesh['frames'][0]
        vertices, indices = model['vertices'][vi]['data'], model['indices'][ii]['values']
        for kind, first, count in model['primitives'][pi]:
            for index in range(first, first + count, 3):
                triangle = tuple(vertices[20 * vertex:20 * (vertex + 1)] for vertex in indices[index:index + 3])
                result[model['materials'][mi]['raw'], triangle] += 1
    return result


class StraightStampGeometryTests(unittest.TestCase):
    def test_shared_concrete_mesh_keeps_the_ground_to_deck_pier_and_moves_the_bridge(self):
        pier = ((-.4, 0, -.4, .375, .5), (.4, 0, -.4, .375, .5), (.4, 15, -.4, .375, .5))
        bridge = ((4, 7.5, 1, .375, .5), (5, 8.890625, 1, .375, .5), (5, 8.890625, 2, .375, .5))
        paint = ((0, 7.51, 0, 1.375, .2), (1, 7.51, 0, 1.375, .8), (1, 7.51, 1, 1.375, .8))
        concrete = _model([pier, bridge], b'SCP NAM concrete\0')
        markings = _model([paint], b'SCP NAM highway\0')
        original = combine_meshes([(m, m['meshes'], (0., 0., 0.)) for m in (concrete, markings)])
        roles = split_model(pack_s3d(original), (4, -4))
        self.assertEqual(set(roles), {'stamp', 'lower-off'})
        self.assertEqual(sum(_faces(roles['stamp']).values()), 2)
        self.assertEqual(sum(_faces(roles['lower-off']).values()), 1)
        self.assertEqual(_faces(roles['stamp']) + _faces(roles['lower-off']), _faces(original))
        self.assertTrue(all(mesh['name'].startswith(b'SCP moved 4,-4 ') for mesh in roles['lower-off']['meshes']))
        kept_x = [struct.unpack_from('<f', v['data'], n)[0] for v in roles['stamp']['vertices']
                  for n in range(0, len(v['data']), 20)]
        self.assertLessEqual(max(kept_x), 1.0, 'Unused curved vertices must not inflate straight-stamp bounds')

    def test_a_paint_face_outside_the_native_corridor_cannot_be_kept_by_name(self):
        outside = ((-8, 7.51, -8, 1.375, .2), (-7, 7.51, -8, 1.375, .8), (-7, 7.51, -7, 1.375, .8))
        raw = pack_s3d(_model([outside], b'SCP NAM highway\0'))
        with self.assertRaisesRegex(ValueError, 'leaves the straight native corridor'):
            split_model(raw, (4, -4))


class FrozenAuthoredVertexFormatTests(unittest.TestCase):
    def setUp(self):
        face = ((0., 7.5, 0., .25, .5), (1., 7.5, 0., .5, .5),
                (0., 7.5, -1., .25, .75))
        authored = _model([face], b'SCP NAM highway\0')
        native = _model([face], b'Native DD road\0')
        self.current = combine_meshes([(m, m['meshes'], (0., 0., 0.)) for m in (native, authored)])
        self.legacy = deepcopy(self.current)
        self.legacy['vertices'][1]['format'] = 2
        self.raw = pack_s3d(self.current)
        self.old_raw = pack_s3d(self.legacy)
        self.frozen = hashlib.sha256(self.old_raw).hexdigest()
        self.path = b'SC4PATHS\r\n1.2\r\n0\r\n0\r\n0\r\n'

    def test_only_the_serialized_authored_word_is_reconstructed_and_live_bytes_remain_exact(self):
        self.assertTrue(matches_frozen_model(self.old_raw, self.frozen))
        self.assertTrue(matches_frozen_model(self.raw, self.frozen))
        self.assertNotEqual(hashlib.sha256(self.raw).hexdigest(), self.frozen)
        changed = [i for i, (old, new) in enumerate(zip(self.old_raw, self.raw)) if old != new]
        self.assertEqual(len(changed), 3)
        self.assertEqual(pack_s3d(self.current), self.raw)
        self.assertEqual(parse_s3d(self.raw)['vertices'][0]['format'], 0x80004001)
        self.assertTrue(matches_frozen_model(self.raw, hashlib.sha256(self.raw).hexdigest()))

    def test_xyz_uv_material_indices_names_flags_and_native_words_remain_hash_bound(self):
        for kind in ('XYZ', 'UV', 'material', 'index', 'name', 'flags', 'native-word'):
            changed = deepcopy(self.current)
            if kind in ('XYZ', 'UV'):
                data = bytearray(changed['vertices'][1]['data'])
                struct.pack_into('<f', data, 0 if kind == 'XYZ' else 12, .125)
                changed['vertices'][1]['data'] = bytes(data)
            elif kind == 'material':
                data = bytearray(changed['materials'][1]['raw'])
                data[4] ^= 1
                changed['materials'][1]['raw'] = bytes(data)
            elif kind == 'index':
                changed['indices'][1]['values'] = (1, 0, 2)
            elif kind == 'name':
                changed['meshes'][1]['name'] = b'SCP NAM ramp\0'
            elif kind == 'flags':
                changed['vertices'][1]['flags'] = 1
            else:
                changed['vertices'][0]['format'] = 2
            with self.subTest(kind=kind):
                self.assertFalse(matches_frozen_model(pack_s3d(changed), self.frozen))
        self.assertFalse(matches_frozen_model(self.raw+b'changed', self.frozen))

    def test_native_named_and_shared_native_buffers_cannot_use_authored_reconstruction(self):
        changed = deepcopy(self.current)
        changed['meshes'][1]['name'] = b'Native other road\0'
        frozen = deepcopy(changed)
        frozen['vertices'][1]['format'] = 2
        self.assertFalse(matches_frozen_model(pack_s3d(changed), hashlib.sha256(pack_s3d(frozen)).hexdigest()))
        shared = deepcopy(self.current)
        alias = deepcopy(shared['meshes'][0])
        alias['frames'] = [(1, 0, 0, 0)]
        shared['meshes'].append(alias)
        validate_s3d(shared)
        frozen = deepcopy(shared)
        frozen['vertices'][1]['format'] = 2
        self.assertFalse(matches_frozen_model(pack_s3d(shared), hashlib.sha256(pack_s3d(frozen)).hexdigest()))

    def test_moved_authored_meshes_match_their_exact_historical_hash_only(self):
        changed = deepcopy(self.current)
        changed['meshes'][1]['name'] = b'SCP moved -3,5 SCP NAM concrete\0'
        frozen = deepcopy(changed)
        frozen['vertices'][1]['format'] = 2
        self.assertTrue(matches_frozen_model(pack_s3d(changed), hashlib.sha256(pack_s3d(frozen)).hexdigest()))

    def _source_cells(self, raw=None, path=None, *, inherited=False):
        raw = self.raw if raw is None else raw
        path = self.path if path is None else path
        records = [{'source_piece_id': 'fixture', 'source_local_cell': [i, 0],
                    'source_world_cell': [i, -2], 'model_sha256': self.frozen,
                    'path_sha256': hashlib.sha256(self.path).hexdigest()} for i in range(27)]
        if inherited:
            records[0]['inherited_model_sha256'] = self.frozen
        compiled = [((i, 0), raw, path) for i in range(27)]
        with patch('scp_highway.modular_stamp.reference', return_value={'cells': records}), \
                patch('scp.jsonc.load', return_value={'id': 'fixture'}), \
                patch('scp_highway.ramp_paths.compile_module', return_value=compiled), \
                patch('scp_highway.native.build_crossing_channels',
                      return_value=[((0, 0), self.old_raw, self.path)]):
            return source_cells({})

    def _assert_source_mismatch(self, error, resource, expected, raw):
        message = str(error.exception)
        self.assertIn('accepted source changed before straight-stamp face partition', message)
        self.assertIn(f'fixture {resource} at source cell (0, 0), world cell (0, -2)', message)
        self.assertIn(f'Expected SHA-256 {expected}', message)
        self.assertIn(f'actual SHA-256 {hashlib.sha256(raw).hexdigest()}', message)

    def test_complete_source_guard_accepts_packed_correction_and_rejects_model_and_path_changes(self):
        result = self._source_cells()
        self.assertEqual(len(result), 27)
        self.assertTrue(all(value == (self.raw, self.path) for value in result.values()))
        for offset, label in ((0, 'XYZ'), (12, 'UV')):
            changed = deepcopy(self.current)
            data = bytearray(changed['vertices'][1]['data'])
            struct.pack_into('<f', data, offset, .125)
            changed['vertices'][1]['data'] = bytes(data)
            raw = pack_s3d(changed)
            with self.subTest(kind=label):
                with self.assertRaises(ValueError) as error:
                    self._source_cells(raw=raw)
                self._assert_source_mismatch(error, 'model', self.frozen, raw)
        path = self.path + b'changed\r\n'
        with self.assertRaises(ValueError) as error:
            self._source_cells(path=path)
        self._assert_source_mismatch(error, 'traffic PATH', hashlib.sha256(self.path).hexdigest(), path)

    def test_inherited_apron_guard_reports_its_fingerprint_before_using_the_pristine_model(self):
        result = self._source_cells(inherited=True)
        self.assertEqual(result[(0, -2)], (self.old_raw, self.path))
        raw = self.raw + b'changed'
        with self.assertRaises(ValueError) as error:
            self._source_cells(raw=raw, inherited=True)
        self._assert_source_mismatch(error, 'inherited Avenue apron model', self.frozen, raw)

    def test_all_saved_zooms_preview_and_projection_keep_their_frozen_byte_binding(self):
        from scp.track_paths import PATH, S3D
        from scp_highway import modular_partition_verify as audit
        from scp_highway import modular_assembly_verify as assembly
        piece = {'id': 'fixture', 'recipe': 'fixture', 'geometry_key': 'modular-stamp',
                 'cells': [[0, 0]], 'footprint': [1, 1], 'tile_ids': ['70000000'],
                 'preview_id': '70000ff5'}
        expected = {key: piece[key] for key in ('recipe', 'geometry_key', 'cells', 'footprint')}
        expected.update(cell_resources=[{'cell': [0, 0], 'model_sha256': self.frozen,
            'path_sha256': hashlib.sha256(self.path).hexdigest()}], preview_sha256=self.frozen)
        resources = {(*S3D, 0x70000000+zoom): self.raw for zoom in range(5)}
        resources[*S3D, 0x70000ff5] = self.raw
        resources[*PATH, 0x70000000] = self.path
        owners = {(0, 0): {'piece_id': piece['id'], 'geometry_key': 'modular-stamp',
                           'tile': 0x70000000, 'local_cell': (0, 0)}}
        with patch.object(audit, 'reviewed_models', return_value={'pieces': {piece['id']: expected}}):
            report = audit.validate_reviewed_models(resources, piece)
            self.assertEqual(len(report['authored_vertex_format_corrected_resources']), 6)
            provenance = assembly._frozen_stamp_provenance(owners, {piece['id']: resources})
            self.assertTrue(provenance[0]['descriptor_only_match'])
            self.assertEqual(provenance[0]['frozen_model_sha256'], self.frozen)
            self.assertEqual(provenance[0]['model_sha256'], hashlib.sha256(self.raw).hexdigest())
            for key in resources:
                changed = {**resources, key: resources[key]+b'changed'}
                with self.subTest(resource=key), self.assertRaises(ValueError):
                    audit.validate_reviewed_models(changed, piece)


if __name__ == '__main__':
    unittest.main()
