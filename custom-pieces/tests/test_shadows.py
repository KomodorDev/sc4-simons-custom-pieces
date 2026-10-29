"""Shadow container, projection, clipping, and actual-model regression checks."""
from __future__ import annotations

from pathlib import Path
import struct
import sys
import unittest
import json
import os
import hashlib
import zlib
from unittest.mock import patch

from PIL import Image

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp import jsonc
from scp.paths import local_settings
from scp.models import pack_s3d
from scp.dbpf import entries, decompress
from scp.shadows import (SHADOW, S3D, ZOOM_SIZES, build_shadows,
                         decode_shadow_fsh, encode_shadow_fsh,
                         rasterize_shadow, validate_piece_shadows)
from scp import shadows


from scp.test_support import plane


class ShadowTests(unittest.TestCase):
    def setUp(self):
        self.model = pack_s3d(plane())
        self.tile = 0x7F503000

    def test_five_native_containers_and_zoom_dimensions(self):
        resources = build_shadows(self.model, self.tile)
        self.assertEqual(set(resources), {(*SHADOW, self.tile + n) for n in range(5)})
        for zoom, size in enumerate(ZOOM_SIZES):
            raw = resources[*SHADOW, self.tile + zoom]
            self.assertEqual(raw[:4], b'SHPI')
            self.assertEqual(raw[12:20], b'GIMX0000')
            self.assertEqual(len(raw), 40 + size * size * 4)
            self.assertEqual(struct.unpack_from('<I', raw, 20)[0], 24)
            self.assertEqual(struct.unpack_from('<I', raw, 24)[0], ((16 + size * size * 4) << 8) | 0x7D)
            self.assertEqual(decode_shadow_fsh(raw).size, (size, size))

    def test_compressed_cache_preserves_original_fsh_bytes_and_reuses_evicted_hot_results(self):
        # Compute the previous uncached recipe through the public rasterizer.
        expected=tuple(encode_shadow_fsh(rasterize_shadow(self.model,size)) for size in ZOOM_SIZES)
        shadows._shadow_set.cache_clear()
        shadows._compressed_shadow_set.cache_clear()
        self.addCleanup(shadows._shadow_set.cache_clear)
        self.addCleanup(shadows._compressed_shadow_set.cache_clear)
        with patch.object(shadows,'_rasterize',wraps=shadows._rasterize) as rasterize:
            actual=shadows._shadow_set(self.model)
            self.assertEqual(actual,expected)
            self.assertEqual(rasterize.call_count,5)
            compressed=shadows._compressed_shadow_set(self.model)
            self.assertIsInstance(compressed,tuple)
            self.assertTrue(all(isinstance(raw,bytes) for raw in compressed))
            self.assertEqual(tuple(zlib.decompress(raw) for raw in compressed),expected)
            self.assertLess(sum(map(len,compressed)),sum(map(len,expected))//10)
            self.assertEqual(shadows._compressed_shadow_set.cache_info().maxsize,12288)
            # Eviction from the small hot cache must not rerun the rasterizer.
            shadows._shadow_set.cache_clear()
            self.assertEqual(shadows._shadow_set(bytes(bytearray(self.model))),expected)
            self.assertEqual(rasterize.call_count,5)
            changed=pack_s3d(plane(-5.,5.))
            self.assertNotEqual(shadows._shadow_set(changed),expected)
            self.assertEqual(rasterize.call_count,10)
            self.assertEqual(shadows._compressed_shadow_set.cache_info().misses,2)

    def test_verification_still_compares_actual_shadow_bytes_with_warm_caches(self):
        resources={(*S3D,self.tile+n):self.model for n in range(5)}
        resources.update(build_shadows(self.model,self.tile))
        validate_piece_shadows(resources,{'tile_ids':[self.tile]})
        key=(*SHADOW,self.tile+4)
        mask=decode_shadow_fsh(resources[key]).getchannel('A')
        mask.putpixel((64,64),0)
        resources[key]=encode_shadow_fsh(mask)
        with self.assertRaisesRegex(ValueError,'differs from actual S3D'):
            validate_piece_shadows(resources,{'tile_ids':[self.tile]})

    def test_native_bgra_pixel_order_and_coverage(self):
        coverage = Image.new('L', (8, 8), 0)
        coverage.putpixel((0, 0), 255)
        coverage.putpixel((1, 0), 64)
        raw = encode_shadow_fsh(coverage)
        self.assertEqual(raw[40:52], b'\0\0\0\xff\0\0\0\x40\xff\xff\xff\0')
        decoded = decode_shadow_fsh(raw)
        self.assertEqual(decoded.getpixel((0, 0)), (0, 0, 0, 255))
        self.assertEqual(decoded.getpixel((1, 0)), (0, 0, 0, 64))
        self.assertEqual(decoded.getpixel((2, 0)), (255, 255, 255, 0))

    def test_fixed_world_projection_retains_narrow_width_and_placement(self):
        mask = rasterize_shadow(self.model, 128)
        self.assertEqual(mask.getbbox(), (48, 0, 80, 128))
        # Pixel sampling at boundaries is antialiased; the occupied width
        # remains about 4/16 of a tile, rather than fitting every model to128px.
        self.assertAlmostEqual(sum(mask.tobytes()) / 255., 32 * 128, delta=32)
        shifted = rasterize_shadow(pack_s3d(plane(2., 6.)), 128)
        self.assertEqual(shifted.getbbox(), (80, 0, 112, 128))
        wide = rasterize_shadow(pack_s3d(plane(-7.5, 7.5)), 128)
        self.assertGreater(sum(wide.tobytes()), sum(mask.tobytes()) * 3)

    def test_height_does_not_translate_vertical_artwork(self):
        other_height = pack_s3d(plane(height=30.))
        self.assertEqual(build_shadows(self.model, self.tile), build_shadows(other_height, self.tile))

    def test_actual_triangles_rather_than_bounding_box_define_coverage(self):
        triangular = plane(-8., 8., -8., 8.)
        triangular['indices'][0]['values'] = (0, 1, 2)
        triangular['primitives'][0] = [(0, 0, 3)]
        mask = rasterize_shadow(pack_s3d(triangular), 128)
        self.assertEqual(mask.getpixel((120, 8)), 255)
        self.assertEqual(mask.getpixel((8, 120)), 0)
        self.assertAlmostEqual(sum(mask.tobytes()) / 255., 128 * 128 / 2, delta=160)

    def test_unused_vertices_and_unreferenced_index_ranges_do_not_cast(self):
        model = plane()
        vb = model['vertices'][0]
        vb['data'] += b''.join(struct.pack('<5f', *p, 0., 0.) for p in
                               [(-8., 15.5, -8.), (8., 15.5, -8.), (8., 15.5, 8.)])
        model['indices'][0]['values'] += (4, 5, 6)
        # PRIM still selects precisely the original six indices.
        self.assertEqual(build_shadows(pack_s3d(model), self.tile),
                         build_shadows(self.model, self.tile))

    def test_geometry_is_clipped_to_one_tile_without_rescaling(self):
        self.assertEqual(rasterize_shadow(pack_s3d(plane(-100., 100., -100., 100.)), 128).getextrema(), (255, 255))
        self.assertIsNone(rasterize_shadow(pack_s3d(plane(9., 12.)), 128).getbbox())

    def test_model_rotation_rotates_artwork(self):
        rotated = pack_s3d(plane(-8., 8., -2., 2.))
        a = rasterize_shadow(self.model, 128)
        b = rasterize_shadow(rotated, 128)
        self.assertEqual(a.transpose(Image.Transpose.TRANSPOSE).tobytes(), b.tobytes())

    def test_stale_shadow_is_rejected_using_actual_s3d(self):
        resources = {(*S3D, self.tile + n): self.model for n in range(5)}
        resources.update(build_shadows(self.model, self.tile))
        report = validate_piece_shadows(resources, {'tile_ids': [f'{self.tile:08x}']})
        self.assertTrue(report['silhouettes_match_actual_s3d_geometry'])
        self.assertFalse(report['native_projection_calibrated'])
        self.assertFalse(report['in_game_shadow_selection_tested'])
        resources[*S3D, self.tile + 4] = pack_s3d(plane(-5., 5.))
        with self.assertRaisesRegex(ValueError, 'differs from actual S3D'):
            validate_piece_shadows(resources, {'tile_ids': [f'{self.tile:08x}']})

    def test_extra_missing_shadow_and_missing_model_are_rejected(self):
        resources = {(*S3D, self.tile + n): self.model for n in range(5)}
        resources.update(build_shadows(self.model, self.tile))
        for key in ((*SHADOW, self.tile + 4), (*S3D, self.tile + 4)):
            changed = dict(resources)
            del changed[key]
            with self.assertRaises(ValueError):
                validate_piece_shadows(changed, {'tile_ids': [self.tile]})
        resources[*SHADOW, self.tile + 5] = resources[*SHADOW, self.tile + 4]
        with self.assertRaisesRegex(ValueError, 'closure'):
            validate_piece_shadows(resources, {'tile_ids': [self.tile]})

    def test_corrupt_headers_sizes_formats_and_offsets_are_rejected(self):
        valid = bytearray(build_shadows(self.model, self.tile)[*SHADOW, self.tile])
        for offset in (0, 4, 8, 12, 16, 20, 24, 25, 28, 30, 32, 38):
            raw = bytearray(valid)
            raw[offset] ^= 1
            with self.subTest(offset=offset), self.assertRaises(ValueError):
                decode_shadow_fsh(bytes(raw))
        with self.assertRaises(ValueError):
            decode_shadow_fsh(bytes(valid[:-1]))

    def test_invalid_models_and_allocation_are_rejected(self):
        with self.assertRaisesRegex(ValueError, 'zero low nibble'):
            build_shadows(self.model, self.tile + 1)
        model = plane()
        model['trailing'][0] = (b'PROP', b'PROP' + struct.pack('<II', 12, 1))
        with self.assertRaisesRegex(ValueError, 'transforms'):
            build_shadows(pack_s3d(model), self.tile)
        model = plane()
        model['vertices'][0]['data'] = b'\0\0\xc0\x7f' + model['vertices'][0]['data'][4:]
        with self.assertRaisesRegex(ValueError, 'Non-finite'):
            build_shadows(pack_s3d(model), self.tile)


class NativeShadowContainerTests(unittest.TestCase):
    def test_all_five_installed_native_shadow_containers_decode(self):
        """Optional primary-data check; only one profile-pinned file is read."""
        local = local_settings(ROOT)
        config = jsonc.loads(local.read_text()) if local.is_file() else {}
        plugins = os.environ.get('SCP_TEST_NAM_PLUGINS', config.get('plugins'))
        if not plugins or not Path(plugins).is_dir():
            self.skipTest('Audited NAM donors unavailable; set SCP_TEST_NAM_PLUGINS')
        donor = jsonc.loads((ROOT / 'config/profiles/nam50-rhd.jsonc').read_text())['files']['hsr']
        filename = donor['filename']
        candidates = list(Path(plugins).rglob(filename))
        self.assertEqual(len(candidates), 1)
        source = candidates[0].read_bytes()
        self.assertEqual(hashlib.sha256(source).hexdigest(), donor['sha256'])
        resources = entries(source)
        for zoom, size in enumerate(ZOOM_SIZES):
            raw = decompress(resources[*SHADOW, 0x5DD31500 + zoom])
            decoded = decode_shadow_fsh(raw)
            self.assertEqual(decoded.size, (size, size))
            self.assertIsNotNone(decoded.getchannel('A').getbbox())
            self.assertEqual(raw[:40], encode_shadow_fsh(Image.new('L', (size, size)))[:40])


if __name__ == '__main__':
    unittest.main()
