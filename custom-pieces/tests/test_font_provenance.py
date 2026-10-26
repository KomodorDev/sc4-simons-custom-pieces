"""Fingerprint real Pillow fallback fonts without relying on workstation fonts."""
import hashlib
import io
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

from PIL import ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'framework'))
try:
    from scp import preview
except ModuleNotFoundError:
    preview = None


@unittest.skipIf(preview is None, 'NumPy preview dependency is unavailable')
class FontProvenanceTests(unittest.TestCase):
    def test_renderer_records_actual_builtin_font_bytes_when_path_is_in_memory(self):
        face = ImageFont.load_default()
        self.assertIsInstance(face.path, io.BytesIO)
        expected = {'name': list(face.getname()),
                    'file_sha256': hashlib.sha256(face.path.getvalue()).hexdigest()}
        with patch.object(preview, 'font', return_value=face):
            settings = preview.renderer_settings()
        self.assertEqual(settings['fonts'], [expected, expected])

    def test_memory_font_hash_tracks_loaded_bytes_without_moving_or_reopening_stream(self):
        raw = ImageFont.load_default().font_bytes
        stream = io.BytesIO(raw)
        face = ImageFont.truetype(stream, 24)
        stream.seek(7)
        first = preview.font_fingerprint(face)
        self.assertEqual(stream.tell(), 7)
        stream.close()
        self.assertEqual(preview.font_fingerprint(face), first)
        changed = ImageFont.truetype(io.BytesIO(raw + b'\0'), 24)
        self.assertEqual(changed.getname(), face.getname())
        self.assertNotEqual(preview.font_fingerprint(changed)['file_sha256'], first['file_sha256'])

    def test_file_fonts_retain_existing_record_shape_and_exact_file_hash(self):
        raw = ImageFont.load_default().font_bytes
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / 'original.ttf'
            path.write_bytes(raw)
            face = ImageFont.truetype(str(path), 24)
            expected = {'name': list(face.getname()), 'file_sha256': hashlib.sha256(raw).hexdigest()}
            self.assertEqual(preview.font_fingerprint(face), expected)
            self.assertEqual(preview.font_fingerprint(ImageFont.truetype(io.BytesIO(raw), 24)), expected)


if __name__ == '__main__':
    unittest.main()
