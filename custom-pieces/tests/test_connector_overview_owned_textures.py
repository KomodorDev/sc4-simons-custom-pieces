"""Connector overviews use verified piece FSH bytes without an installation."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import struct
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "framework"))

from PIL import Image

from scp import connector_metadata, connector_overview, preview
from scp.dbpf import pack_dbpf
from scp.export import compiled_manifest_sha256
from scp.models import pack_s3d
from scp.shadows import encode_shadow_fsh
from scp.test_support import plane


TEXTURE_ID = 0x7F5D1000
TEXTURE_KEY = (0x7AB50E44, 0x1ABE787D, TEXTURE_ID)


class ConnectorOverviewOwnedTextureTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="scp-overview-owned-texture-")
        self.addCleanup(temporary.cleanup)
        self.workspace = Path(temporary.name)
        self.plugins = self.workspace / "Plugins"
        self.plugins.mkdir()
        self.library = preview.TextureLibrary(self.plugins)
        self.model = plane()
        self.model["materials"][0]["textures"] = [TEXTURE_ID]
        self.raw = encode_shadow_fsh(Image.new("L", (8, 8), 255))
        self.built = {"authored_texture_ids": ["7f5d1000"]}

    def resolve(self, resources, built=None):
        return connector_overview._overview_textures(
            self.library, self.model, self.built if built is None else built, resources)

    def test_saved_fsh_decodes_without_searching_the_empty_plugins_directory(self):
        with patch.object(preview.read_dbpf, "index_plugins",
                          side_effect=AssertionError("Saved texture must not need installed files")):
            textures, provenance = self.resolve({TEXTURE_KEY: self.raw})

        self.assertEqual(list(self.plugins.iterdir()), [])
        self.assertIsNone(self.library.index)
        self.assertEqual(set(textures), {TEXTURE_ID})
        self.assertEqual(textures[TEXTURE_ID].shape, (8, 8, 4))
        self.assertTrue((textures[TEXTURE_ID] == [0., 0., 0., 1.]).all())
        self.assertFalse(textures[TEXTURE_ID].flags.writeable)
        self.assertEqual(provenance, [{
            "instance": "7f5d1000", "fsh_sha256": hashlib.sha256(self.raw).hexdigest(),
            "size": [8, 8], "source": "piece-dat",
        }])

    def test_missing_declared_fsh_is_rejected_before_installed_fallback(self):
        with patch.object(self.library, "for_model", wraps=self.library.for_model) as load:
            with self.assertRaisesRegex(ValueError, "piece-owned overview texture is missing.*7f5d1000"):
                self.resolve({})
        load.assert_not_called()

    def test_matching_instance_under_the_shadow_group_is_not_an_owned_surface_fsh(self):
        wrong_group = (TEXTURE_KEY[0], 0x2BC2759A, TEXTURE_ID)
        with self.assertRaisesRegex(ValueError, "piece-owned overview texture is missing.*7f5d1000"):
            self.resolve({wrong_group: self.raw})

    def test_every_declared_fsh_is_required_even_if_the_model_does_not_sample_it(self):
        built = {"authored_texture_ids": ["7f5d1000", "7f5d1001"]}
        with self.assertRaisesRegex(ValueError, "piece-owned overview texture is missing.*7f5d1001"):
            self.resolve({TEXTURE_KEY: self.raw}, built)

    def test_cached_fsh_cannot_hide_a_missing_resource_in_the_next_piece(self):
        self.resolve({TEXTURE_KEY: self.raw})
        with self.assertRaisesRegex(ValueError, "piece-owned overview texture is missing.*7f5d1000"):
            self.resolve({})

    def test_different_saved_bytes_cannot_reuse_a_cached_texture_instance(self):
        self.resolve({TEXTURE_KEY: self.raw})
        changed = encode_shadow_fsh(Image.new("L", (8, 8), 0))
        with self.assertRaisesRegex(ValueError, "Cached texture 7f5d1000 differs"):
            self.resolve({TEXTURE_KEY: changed})
        self.assertEqual(self.library.provenance[TEXTURE_ID]["fsh_sha256"],
                         hashlib.sha256(self.raw).hexdigest())

    def test_legacy_pieces_retain_the_exact_no_owned_resources_call(self):
        expected_textures, expected_provenance = self.resolve({TEXTURE_KEY: self.raw})
        for built in ({}, {"authored_texture_ids": []}):
            with self.subTest(built=built):
                with patch.object(self.library, "for_model", wraps=self.library.for_model) as load:
                    textures, provenance = self.resolve({}, built)
                load.assert_called_once_with(self.model)
                self.assertIs(textures[TEXTURE_ID], expected_textures[TEXTURE_ID])
                self.assertEqual(provenance, expected_provenance)

    def overview_fixture(self, *, declared=True, saved=True, saved_raw=None):
        """Create a portable saved DAT and freshness evidence, without native inputs.

        The synthetic image and empty boundary list isolate texture freshness;
        this fixture makes no claim about connector geometry or a game result.
        All checked files, fonts, manifest facts, DAT bytes, and texture hashes
        are real, and the freshness checker is not mocked.
        """
        identifier = "synthetic-owned-texture"
        root = self.workspace / "library"
        framework = root / "framework/scp"
        framework.mkdir(parents=True)
        for module in (connector_metadata, connector_overview):
            source = Path(module.__file__)
            (framework / source.name).write_bytes(source.read_bytes())
        directory = root / "domains/synthetic/00_pieces" / identifier
        (directory / "evidence").mkdir(parents=True)
        (directory / "previews").mkdir()
        image = directory / "previews/connection-overview.png"
        Image.new("RGB", (8, 8), "white").save(image)
        model = plane()
        material = (struct.pack("<IBBBBHIBB", 0, 0, 0, 0, 0, 0, 0, 0, 1)
                    + struct.pack("<IBBBBHHB", TEXTURE_ID, 0, 0, 0, 0, 0, 0, 1) + b"\0")
        model["materials"] = [{"raw": material, "textures": [TEXTURE_ID]}]
        preview_id = 0x7F5D1FF5
        resources = {(*preview.S3D, preview_id): pack_s3d(model)}
        if saved:
            resources[TEXTURE_KEY] = self.raw if saved_raw is None else saved_raw
        build = root / "dist/synthetic"
        build.mkdir(parents=True)
        dat = build / "piece.dat"
        dat.write_bytes(pack_dbpf(resources))
        built = {"id": identifier, "asset_file": "piece.dat", "preview_id": f"{preview_id:08x}"}
        if declared:
            built.update(self.built)
        manifest = {"pieces": [built]}
        manifest_path = build / "manifest.json"
        manifest_path.write_text(json.dumps(manifest))
        sha = lambda raw: hashlib.sha256(raw).hexdigest()
        texture = {"instance": "7f5d1000", "fsh_sha256": sha(self.raw), "size": [8, 8]}
        if declared:
            texture["source"] = "piece-dat"
        fonts = [preview.font_fingerprint(face) for face in (
            preview.font(connector_overview.BODY_SIZE),
            preview.font(connector_overview.BODY_SIZE, True),
            connector_overview.mono_font(connector_overview.BODY_SIZE, preview.font))]
        evidence = {
            "schema_version": 1, "piece_id": identifier,
            "file": "previews/connection-overview.png", "output_sha256": sha(image.read_bytes()),
            "source_inputs": {}, "shared_framework_sources": {},
            "generator_sha256": sha(Path(connector_overview.__file__).read_bytes()),
            "metadata_resolver_sha256": sha(Path(connector_metadata.__file__).read_bytes()),
            "source_manifest": manifest_path.relative_to(root).as_posix(),
            "compiled_manifest_sha256": compiled_manifest_sha256(manifest),
            "source_dat": dat.relative_to(root).as_posix(), "source_dat_sha256": sha(dat.read_bytes()),
            "source_preview_id": f"{preview_id:08x}", "textures": [texture],
            "figure_typography": {"fonts": fonts}, "renderer": preview.renderer_settings(),
            "conventions": [], "groups": [], "boundary_cards": [],
        }
        text = connector_overview.markdown_overview(evidence)
        evidence["selectable_markdown_sha256"] = sha(text.encode())
        (directory / "README.md").write_text("# Synthetic texture fixture\n\n" + text)
        (directory / "evidence/connection-overview.json").write_text(json.dumps(evidence))
        return root, identifier

    def verify_fixture(self, root, identifier):
        return connector_metadata.verify_overview(root, identifier, domain_id="synthetic", plugins=self.plugins)

    def test_freshness_checker_reads_owned_fsh_from_the_recorded_dat_without_installation(self):
        root, identifier = self.overview_fixture()
        with patch.object(preview.read_dbpf, "index_plugins",
                          side_effect=AssertionError("Freshness must use the saved texture")):
            result = self.verify_fixture(root, identifier)
        self.assertEqual(result["status"], "passed")
        self.assertEqual(list(self.plugins.iterdir()), [])

    def test_freshness_checker_rejects_declared_texture_missing_from_the_recorded_dat(self):
        root, identifier = self.overview_fixture(saved=False)
        with self.assertRaisesRegex(ValueError, "piece-owned overview texture is missing.*7f5d1000"):
            self.verify_fixture(root, identifier)

    def test_freshness_checker_rejects_changed_saved_texture_even_with_current_dat_binding(self):
        changed = encode_shadow_fsh(Image.new("L", (8, 8), 0))
        root, identifier = self.overview_fixture(saved_raw=changed)
        with self.assertRaisesRegex(ValueError, "stale overview texture inputs"):
            self.verify_fixture(root, identifier)

    def test_freshness_checker_preserves_installed_texture_lookup_for_legacy_pieces(self):
        root, identifier = self.overview_fixture(declared=False, saved=False)
        (self.plugins / "synthetic-texture.dat").write_bytes(pack_dbpf({TEXTURE_KEY: self.raw}))
        self.assertEqual(self.verify_fixture(root, identifier)["status"], "passed")


if __name__ == "__main__":
    unittest.main()
