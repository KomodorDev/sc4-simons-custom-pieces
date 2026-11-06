"""Player-installer boundaries use disposable folders and synthetic archives."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = next(path for path in Path(__file__).resolve().parents if (path / "project.jsonc").is_file())
sys.path.insert(0, str(ROOT / "installer"))
from scp_installer import service
from scp.catalog import load_catalog
from scp import jsonc
from scp.dbpf import pack_dbpf
from scp.install import FOLDER, RUL0, NETWORK_INI


PARALLEL_B_RECIPES = {
    "highway_ddrhw_parallel_b_crossing",
    "highway_ddrhw_parallel_b_northwest_terminal",
    "highway_ddrhw_parallel_b_southeast_terminal",
    "highway_ddrhw_parallel_b_lower_exit_slip",
    "highway_ddrhw_parallel_b_lower_entry_slip",
    "highway_ddrhw_parallel_b_upper_exit_slip",
    "highway_ddrhw_parallel_b_upper_entry_slip",
    "highway_ddrhw_parallel_b_lower_exit_departure",
    "highway_ddrhw_parallel_b_lower_entry_departure",
    "highway_ddrhw_parallel_b_upper_exit_departure",
    "highway_ddrhw_parallel_b_upper_entry_departure",
    "highway_ddrhw_parallel_b_lower_exit_grade",
    "highway_ddrhw_parallel_b_lower_entry_grade",
    "highway_ddrhw_parallel_b_upper_exit_grade",
    "highway_ddrhw_parallel_b_upper_entry_grade",
}


class DiscoveryTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name).resolve()
        self.home = self.base / "home"
        self.documents = self.base / "Redirected Documents"
        self.plugins = self.documents / "SimCity 4/Plugins"
        self.plugins.mkdir(parents=True)
        self.game = self.make_game(self.base / "Steam/SimCity 4 Deluxe")

    def make_game(self, path):
        (path / "Apps").mkdir(parents=True)
        (path / "Apps/SimCity 4.exe").write_bytes(b"synthetic executable marker")
        (path / "SimCity_3.dat").write_bytes(b"synthetic core marker")
        (path / "Plugins").mkdir()
        return path

    def discover(self, selected, **kwargs):
        return service.discover_installation(selected, platform="win32", home=self.home,
                                             documents=self.documents, **kwargs)

    def test_game_folder_uses_redirected_user_plugins_and_scans_install_plugins(self):
        plan = self.discover(self.game)
        self.assertEqual(plan.plugins, self.plugins)
        self.assertEqual(plan.game_folder, self.game)
        self.assertEqual(plan.extra_plugins, (self.game / "Plugins",))

    def test_game_executable_or_apps_folder_selects_same_root(self):
        for path in (self.game / "Apps", self.game / "Apps/SimCity 4.exe"):
            with self.subTest(path=path):
                self.assertEqual(self.discover(path).plugins, self.plugins)

    def test_game_plugins_is_a_scan_root_not_the_install_destination(self):
        self.assertEqual(self.discover(self.game / "Plugins").plugins, self.plugins)

    def test_install_reports_missing_submenu_files_before_preparation(self):
        work = self.base / "install-work"
        with self.assertRaises(ValueError) as raised:
            service.run_install(ROOT, self.game, work, platform="win32", home=self.home,
                                documents=self.documents)
        for name in ("memo.submenus.dll", "SC4ResourceLoadingHooks.dll", "submenu-essentials.dat"):
            self.assertIn(name, str(raised.exception))
        self.assertFalse(work.exists())

    def test_submenu_files_use_both_plugins_roots_but_dlls_must_be_at_top_level(self):
        nested = self.plugins / "Dependencies"
        nested.mkdir()
        (nested / "submenu-essentials.dat").touch()
        (self.game / "Plugins/SC4ResourceLoadingHooks.dll").touch()
        submenu = nested / "MEMO.SUBMENUS.DLL"
        submenu.touch()
        plan = self.discover(self.game)
        with self.assertRaisesRegex(ValueError, r"memo\.submenus\.dll directly inside"):
            service._require_submenu_files(plan)
        submenu.rename(self.plugins / submenu.name)
        service._require_submenu_files(plan)

    def test_selected_data_plugins_uses_registered_game_without_writing_it(self):
        before = set(self.base.rglob("*"))
        with patch.object(service, "_registered_games", return_value=[self.game]):
            self.assertEqual(self.discover(self.plugins).plugins, self.plugins)
            self.assertEqual(self.discover(self.plugins.parent).game_folder, self.game)
        self.assertEqual(before, set(self.base.rglob("*")))

    def test_two_data_folders_are_not_silently_prioritized(self):
        alternate = self.documents / "SimCity 4 Windows/Plugins"
        alternate.mkdir(parents=True)
        with self.assertRaisesRegex(service.PlayerDataSelectionRequired, "Several player-data folders") as raised:
            self.discover(self.game)
        self.assertEqual(set(raised.exception.candidate_paths), {str(self.plugins), str(alternate)})

    def test_secondary_data_choice_retains_selected_steam_game_without_registry(self):
        alternate = self.documents / "SimCity 4 Windows/Plugins"
        alternate.mkdir(parents=True)
        with patch.object(service, "_registered_games", side_effect=AssertionError("The explicit game must be retained")):
            for selected_data in (alternate, alternate.parent):
                with self.subTest(selected_data=selected_data):
                    plan = self.discover(self.game, player_data=selected_data)
                    self.assertEqual(plan.game_folder, self.game)
                    self.assertEqual(plan.plugins, alternate)
                    self.assertEqual(plan.extra_plugins, (self.game / "Plugins",))

    def test_missing_default_data_can_be_supplied_from_another_drive(self):
        self.plugins.rmdir()
        alternate = self.base / "Another Drive/Player Data/Plugins"
        alternate.mkdir(parents=True)
        with self.assertRaises(service.PlayerDataSelectionRequired) as raised:
            self.discover(self.game)
        self.assertEqual(raised.exception.candidate_paths, [])
        self.assertEqual(self.discover(self.game, player_data=alternate).plugins, alternate)

    def test_secondary_choice_cannot_install_into_game_plugins(self):
        with self.assertRaisesRegex(ValueError, "player data, rather than"):
            self.discover(self.game, player_data=self.game / "Plugins")

    def test_secondary_choice_cannot_hide_a_nested_game_plugins_scan(self):
        nested = self.game / "Plugins/Player Data/Plugins"
        nested.mkdir(parents=True)
        with self.assertRaisesRegex(ValueError, "Plugins folders overlap"):
            self.discover(self.game, player_data=nested)

    def test_secondary_choice_must_be_an_existing_data_or_plugins_directory(self):
        invalid = self.base / "Unrelated Folder"
        invalid.mkdir()
        with self.assertRaisesRegex(ValueError, "has no Plugins folder"):
            self.discover(self.game, player_data=invalid)
        self.assertEqual(list(invalid.iterdir()), [])

    def test_failed_shell_documents_lookup_uses_secondary_data_folder_flow(self):
        with patch.object(service, "_documents", side_effect=ValueError("Windows could not locate Documents")):
            with self.assertRaises(service.PlayerDataSelectionRequired) as raised:
                service.discover_installation(self.game, platform="win32", home=self.home)
            self.assertEqual(raised.exception.candidate_paths, [])
            plan = service.discover_installation(self.game, platform="win32", home=self.home,
                                                player_data=self.plugins)
        self.assertEqual(plan.plugins, self.plugins)
        self.assertEqual(plan.game_folder, self.game)

    def test_explicit_data_selection_resolves_ambiguous_documents(self):
        (self.documents / "SimCity 4 Windows/Plugins").mkdir(parents=True)
        with patch.object(service, "_registered_games", return_value=[self.game]):
            self.assertEqual(self.discover(self.plugins).plugins, self.plugins)

    def test_missing_data_folder_does_not_create_plugins_in_game_directory(self):
        self.plugins.rmdir()
        with self.assertRaisesRegex(ValueError, "No player-data Plugins"):
            self.discover(self.game)
        self.assertEqual(list((self.game / "Plugins").iterdir()), [])

    def test_archive_without_windows_executable_is_not_a_supported_game(self):
        (self.game / "Apps/SimCity 4.exe").unlink()
        with patch.object(service, "_registered_games", return_value=[]):
            with self.assertRaisesRegex(ValueError, "Windows game files were not found"):
                self.discover(self.game)

    def test_native_mac_application_is_rejected_with_exact_scope(self):
        application = self.base / "SimCity 4.app"
        (application / "Contents/MacOS").mkdir(parents=True)
        with self.assertRaisesRegex(ValueError, "native macOS edition is not supported"):
            self.discover(application)

    def test_selected_wine_prefix_uses_its_own_game_and_user(self):
        prefix = self.base / "CrossOver/Bottles/SC4"
        game = self.make_game(prefix / "drive_c/Program Files/SimCity 4 Deluxe")
        plugins = prefix / "drive_c/users/player/Documents/SimCity 4/Plugins"
        plugins.mkdir(parents=True)
        plan = service.discover_installation(prefix, platform="darwin", home=self.home,
                                            documents=self.base / "no-host-documents")
        self.assertEqual(plan.game_folder, game)
        self.assertEqual(plan.plugins, plugins)
        self.assertEqual(plan.game_kind, "windows-under-wine")

    def test_wine_users_and_symlink_aliases_deduplicate(self):
        prefix = self.base / "Wine/SC4"
        game = self.make_game(prefix / "drive_c/Program Files/SimCity 4 Deluxe")
        user = prefix / "drive_c/users/player"
        plugins = user / "Documents/SimCity 4/Plugins"
        plugins.mkdir(parents=True)
        try:
            (user / "My Documents").symlink_to(user / "Documents", target_is_directory=True)
        except OSError:
            self.skipTest("Directory symlinks are unavailable for this user")
        plan = service.discover_installation(game, platform="darwin", home=self.home,
                                            documents=self.base / "no-host-documents")
        self.assertEqual(plan.plugins, plugins)

    def test_two_windows_games_in_selected_bottle_require_explicit_selection(self):
        prefix = self.base / "Wine/SC4"
        first = self.make_game(prefix / "drive_c/Program Files/SimCity 4 Deluxe")
        self.make_game(prefix / "drive_c/Program Files/Second SC4")
        with self.assertRaisesRegex(ValueError, "Several game installations"):
            self.discover(prefix)
        self.assertEqual(self.discover(first).game_folder, first)


class InstallerSelectionTests(unittest.TestCase):
    def test_all_implemented_selection_contains_disabled_standalone_and_all_members(self):
        catalog = load_catalog(ROOT)
        expected = [piece["id"] for piece in catalog["pieces"] if piece["status"] != "draft"]
        actual = service.all_implemented_ids(ROOT)
        self.assertEqual(actual, expected)
        self.assertIn("hsr-l2-over-road-l0-mixed-parallel-stack", actual)
        self.assertIn("hsr-l2-and-l4-two-track-curve-ramp-90deg-right", actual)
        highway = [piece for piece in catalog["pieces"] if piece["domain"] == "highway"
                   and piece["status"] != "draft"]
        self.assertTrue(highway)
        self.assertTrue(all(piece["id"] in actual for piece in highway))
        self.assertTrue(any(not piece["enabled_by_default"] for piece in highway))
        self.assertEqual(len(actual), len(expected))
        self.assertGreater(len(actual), len([piece for piece in catalog["pieces"] if piece["enabled_by_default"]]))

    def test_capabilities_use_finite_provider_recipes_for_both_domains(self):
        from scp_highway import native, ramp_paths, modular_ramps, modular_stamp, parallel_layout, y_junction_layout
        capabilities = service.implemented_recipes_by_domain()
        self.assertEqual(set(capabilities), {"high-speed-rail", "highway"})
        self.assertIsInstance(capabilities["highway"], frozenset)
        self.assertEqual(capabilities["highway"], {native.RECIPE, modular_stamp.RECIPE,
                                                 "highway_ddrhw_diagonal_ghsr_crossing",
                                                 "highway_ddrhw_orthogonal_l0_transition",
                                                 "highway_ddrhw_orthogonal_l0_transition_mirrored",
                                                 "highway_ddrhw_orthogonal_l0_transition_opposite_side",
                                                 "highway_ddrhw_orthogonal_l0_transition_opposite_side_mirrored",
                                                 "highway_ddrhw_orthogonal_l0_transition_lower_bend_right",
                                                 "highway_ddrhw_diagonal_l0_transition_a",
                                                 "highway_ddrhw_diagonal_l0_transition_mirrored_a",
                                                 "highway_ddrhw_diagonal_l0_transition_opposite_a",
                                                 "highway_ddrhw_diagonal_l0_transition_opposite_mirrored_a",
                                                 "highway_ddrhw_y_reversed_diagonal_stem_split",
                                                 "highway_ddrhw_y_reversed_diagonal_branch",
                                                 "highway_ddrhw_y_reversed_orthogonal_core",
                                                 "highway_ddrhw_diagonal_ghsr_crossing_alignment_b"} | {
            item["recipe"] for provider in (ramp_paths, modular_ramps, parallel_layout, y_junction_layout)
            for item in provider.module_catalog()["types"]} | PARALLEL_B_RECIPES)
        self.assertIn("hsr_diagonal_ghsr", capabilities["high-speed-rail"])

    def test_parallel_b_has_exactly_fifteen_finite_recipes_and_reaches_complete_selection(self):
        catalog = load_catalog(ROOT)
        identifiers = set(catalog["piece_sets"]["ddrhw-parallel-diamond-alignment-b"])
        pieces = [piece for piece in catalog["pieces"] if piece["id"] in identifiers]
        self.assertEqual(len(pieces), 15)
        self.assertEqual({piece["recipe"] for piece in pieces}, PARALLEL_B_RECIPES)
        capabilities = service.implemented_recipes_by_domain()["highway"]
        self.assertEqual({recipe for recipe in capabilities if recipe.startswith("highway_ddrhw_parallel_b_")},
                         PARALLEL_B_RECIPES)
        self.assertTrue(identifiers <= set(service.all_implemented_ids(ROOT)))

    def test_parallel_b_update_adds_fifteen_types_and_retains_the_previous_37_without_receipt_changes(self):
        catalog = load_catalog(ROOT)
        retained_assemblies = {"ddrhw-l1-and-l2-diagonal-avenue-diamond",
                               "ddrhw-l1-and-l2-diagonal-avenue-modular-diamond",
                               "ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond"}
        previous = {row["piece_id"] for assembly in catalog["_assemblies"]
                    if assembly["id"] in retained_assemblies for row in assembly["scene"]["placements"]}
        previous.update(catalog["piece_sets"]["ddrhw-diagonal-ghsr-crossing-alignments"])
        self.assertEqual(len(previous), 37)
        added = set(catalog["piece_sets"]["ddrhw-parallel-diamond-alignment-b"])
        self.assertEqual(len(added), 15)
        self.assertFalse(previous & added)
        receipt = {"piece_ids": sorted(previous)}
        original = deepcopy(receipt)
        plan = service.Installation(Path("game"), Path("Plugins"), (), "win32")
        with patch.object(service, "_owned", return_value=receipt), \
                patch("scp.install.install_build") as install:
            selection = service.installed_selection(ROOT, plan)
        self.assertTrue(previous | added <= set(selection))
        self.assertEqual(receipt, original)
        install.assert_not_called()

    def test_parallel_b_unknown_recipe_cannot_hide_behind_the_implemented_prefix(self):
        catalog = load_catalog(ROOT)
        for recipe in ("highway_ddrhw_parallel_b_unknown", "highway_ddrhw_parallel_b_crossing_extra",
                       "highway_ddrhw_parallel_b_upper_entry_grade_unimplemented"):
            with self.subTest(recipe=recipe):
                changed = deepcopy(catalog)
                piece = next(row for row in changed["pieces"] if row["id"] == "ddrhw-parallel-b-crossing")
                piece["recipe"] = recipe
                with patch.object(service, "load_catalog", return_value=changed):
                    with self.assertRaisesRegex(ValueError, "cannot prove an implementation.*ddrhw-parallel-b-crossing"):
                        service.all_implemented_ids(ROOT)

    def test_parallel_b_draft_exclusion_and_failed_placement_guard_remain_in_force(self):
        catalog = load_catalog(ROOT)
        changed = deepcopy(catalog)
        piece = next(row for row in changed["pieces"] if row["id"] == "ddrhw-parallel-b-crossing")
        piece.update(status="draft", recipe="highway_ddrhw_parallel_b_unimplemented")
        with patch.object(service, "load_catalog", return_value=changed):
            self.assertNotIn(piece["id"], service.all_implemented_ids(ROOT))
        changed = deepcopy(catalog)
        piece = next(row for row in changed["pieces"] if row["id"] == "ddrhw-parallel-b-crossing")
        piece["game_tests"]["placement"] = "failed"
        with patch.object(service, "load_catalog", return_value=changed):
            with self.assertRaisesRegex(ValueError, "failed placement"):
                service.all_implemented_ids(ROOT)

    def test_non_draft_record_with_no_implementation_blocks_complete_selection(self):
        catalog = deepcopy(load_catalog(ROOT))
        catalog["pieces"][0]["recipe"] = "missing_recipe"
        with patch.object(service, "load_catalog", return_value=catalog):
            with self.assertRaisesRegex(ValueError, "cannot prove an implementation"):
                service.all_implemented_ids(ROOT)

    def test_highway_prefix_or_another_domains_recipe_does_not_prove_implementation(self):
        catalog = load_catalog(ROOT)
        highway = next(piece for piece in catalog["pieces"] if piece["domain"] == "highway")
        hsr_recipe = next(piece["recipe"] for piece in catalog["pieces"]
                          if piece["domain"] == "high-speed-rail")
        for recipe in ("highway_ddrhw_compact_unimplemented", "highway_ddrhw_modular_unimplemented", "highway_ddrhw_parallel_unimplemented", hsr_recipe):
            with self.subTest(recipe=recipe):
                changed = deepcopy(catalog)
                next(piece for piece in changed["pieces"] if piece["id"] == highway["id"])["recipe"] = recipe
                with patch.object(service, "load_catalog", return_value=changed):
                    with self.assertRaisesRegex(ValueError, "cannot prove an implementation.*" + highway["id"]):
                        service.all_implemented_ids(ROOT)

    def test_unknown_domain_is_rejected_even_with_a_known_recipe(self):
        catalog = deepcopy(load_catalog(ROOT))
        catalog["pieces"][0]["domain"] = "unimplemented-domain"
        with patch.object(service, "load_catalog", return_value=catalog):
            with self.assertRaisesRegex(ValueError, "cannot prove an implementation"):
                service.all_implemented_ids(ROOT)

    def test_unknown_draft_recipe_stays_out_of_complete_selection(self):
        catalog = deepcopy(load_catalog(ROOT))
        draft = next(piece for piece in catalog["pieces"] if piece["domain"] == "highway")
        draft.update(status="draft", recipe="highway_ddrhw_compact_unimplemented")
        with patch.object(service, "load_catalog", return_value=catalog):
            self.assertNotIn(draft["id"], service.all_implemented_ids(ROOT))

    def test_failed_placement_guard_is_not_overridden(self):
        for domain in ("high-speed-rail", "highway"):
            with self.subTest(domain=domain):
                catalog = deepcopy(load_catalog(ROOT))
                next(piece for piece in catalog["pieces"] if piece["domain"] == domain)["game_tests"]["placement"] = "failed"
                with patch.object(service, "load_catalog", return_value=catalog):
                    with self.assertRaisesRegex(ValueError, "failed placement"):
                        service.all_implemented_ids(ROOT)

    def test_update_cannot_drop_an_installed_type_missing_from_new_source(self):
        plan = service.Installation(Path("game"), Path("Plugins"), (), "win32")
        with patch.object(service, "_owned", return_value={"piece_ids": ["retired-in-city"]}):
            with self.assertRaisesRegex(ValueError, "would remove installed pieces: retired-in-city"):
                service.installed_selection(ROOT, plan)

    def test_update_accepts_current_piece_selections_without_rewriting_receipts(self):
        plan = service.Installation(Path("game"), Path("Plugins"), (), "win32")
        expected = service.all_implemented_ids(ROOT)
        receipt = {"piece_ids": expected[:3]}
        previous = deepcopy(receipt)
        with patch.object(service, "_owned", return_value=receipt):
            self.assertEqual(service.installed_selection(ROOT, plan), expected)
        self.assertEqual(receipt, previous)

    def test_assembly_ids_are_not_accepted_as_installed_piece_identities(self):
        plan = service.Installation(Path("game"), Path("Plugins"), (), "win32")
        identifier = load_catalog(ROOT)["_assemblies"][0]["id"]
        with patch.object(service, "_owned", return_value={"piece_ids": [identifier]}):
            with self.assertRaisesRegex(ValueError, "would remove installed pieces: " + identifier):
                service.installed_selection(ROOT, plan)


class CaptureTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name).resolve()
        self.library = self.base / "library"
        self.library.mkdir()
        self.work = self.base / "work"
        self.work.mkdir()
        self.plugins = self.base / "Plugins"
        self.plugins.mkdir()
        self.game = self.base / "Game"
        self.game.mkdir()
        self.plan = service.Installation(self.game, self.plugins, (), "win32")
        self.key = (0x296678F7, 0x69668828, 0x00004B00)
        self.stored = b"audited stored resource"
        self.source = self.plugins / "NetworkAddonMod_BaseContent.dat"
        self.source.write_bytes(pack_dbpf({self.key: self.stored, (1, 2, 3): b"unrelated"}))
        self.expected = pack_dbpf({self.key: self.stored})
        audit = {"tgi": "296678f7-69668828-00004b00", "scope": {"archive": "<NAM>/NetworkAddonMod_BaseContent.dat"},
                 "matches": [{"stored_resource_sha256": hashlib.sha256(self.stored).hexdigest()}]}
        (self.library / "audit.json").write_text(json.dumps(audit))
        self.record = {"filename": "SCP_OrdinaryRoad_Path_Capture.dat", "audit": "audit.json",
                       "sha256": hashlib.sha256(self.expected).hexdigest()}
        self.catalog = {"_profile": {"files": {"ordinary_road": self.record}}}
        self.patch_catalog = patch.object(service, "load_catalog", return_value=self.catalog)
        self.patch_catalog.start()
        self.addCleanup(self.patch_catalog.stop)
        self.patch_pieces = patch.object(service, "select_pieces", return_value=[{"dependencies": ["ordinary_road"]}])
        self.patch_pieces.start()
        self.addCleanup(self.patch_pieces.stop)

    def prepare(self):
        return service.prepare_captures(self.library, self.plan, self.work, ["synthetic-piece"])

    def test_capture_keeps_only_exact_original_stored_resource_and_leaves_source(self):
        before = self.source.read_bytes()
        roots, records = self.prepare()
        found = list(roots[0].rglob(self.record["filename"]))
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0].read_bytes(), self.expected)
        self.assertEqual(self.source.read_bytes(), before)
        self.assertEqual(records[0]["sha256"], self.record["sha256"])
        self.assertEqual(json.loads((found[0].parent / "resource-audit.json").read_text())["capture"]["file"],
                         self.record["filename"])
        self.assertTrue(roots[0].is_relative_to(self.work / "local/captures"))
        self.assertFalse(roots[0].is_relative_to(self.plugins))

    def test_changed_resource_is_rejected_before_any_capture(self):
        self.source.write_bytes(pack_dbpf({self.key: b"changed"}))
        with self.assertRaisesRegex(ValueError, "exact supported ordinary_road resource"):
            self.prepare()
        self.assertFalse((self.work / "local").exists())

    def test_commented_audit_sources_preserve_capture_fingerprint_checks(self):
        audit = (self.library / "audit.json").read_text()
        (self.library / "audit.jsonc").write_text("// Migrated source audit.\n" + audit)
        self.record["audit"] = "audit.jsonc"
        roots, records = self.prepare()
        self.assertEqual(next(roots[0].rglob(self.record["filename"])).read_bytes(), self.expected)
        self.assertEqual(records[0]["sha256"], self.record["sha256"])
        self.source.write_bytes(pack_dbpf({self.key: b"changed"}))
        with self.assertRaisesRegex(ValueError, "exact supported ordinary_road resource"):
            self.prepare()

    def test_duplicate_source_archives_are_not_load_order_guessed(self):
        duplicate = self.plugins / "another" / self.source.name
        duplicate.parent.mkdir()
        duplicate.write_bytes(self.source.read_bytes())
        with self.assertRaisesRegex(ValueError, "found 2"):
            self.prepare()

    def test_existing_exact_capture_is_reused_without_duplicate_donor(self):
        (self.plugins / self.record["filename"]).write_bytes(self.expected)
        roots, records = self.prepare()
        self.assertEqual((roots, records), ([], []))
        self.assertFalse((self.work / "local").exists())

    def test_prebuilt_mode_rechecks_original_nam_resource_when_reusing_a_capture(self):
        (self.plugins / self.record["filename"]).write_bytes(self.expected)
        self.source.write_bytes(pack_dbpf({self.key: b"changed"}))
        with self.assertRaisesRegex(ValueError, "exact supported ordinary_road resource"):
            service.prepare_captures(self.library, self.plan, self.work, ["synthetic-piece"],
                                     verify_originals=True)
        self.assertFalse((self.work / "local").exists())

    def test_existing_modified_capture_is_never_overwritten(self):
        path = self.plugins / self.record["filename"]
        path.write_bytes(b"personal or changed input")
        with self.assertRaisesRegex(ValueError, "duplicated or differs"):
            self.prepare()
        self.assertEqual(path.read_bytes(), b"personal or changed input")

    def test_game_archive_source_is_read_from_selected_game_only(self):
        self.source.unlink()
        audit = json.loads((self.library / "audit.json").read_text())
        audit["scope"]["archive"] = "<Game>/SimCity_3.dat"
        source_bytes = pack_dbpf({self.key: self.stored})
        audit["matches"][0]["archive_sha256"] = hashlib.sha256(source_bytes).hexdigest()
        (self.library / "audit.json").write_text(json.dumps(audit))
        (self.game / "SimCity_3.dat").write_bytes(source_bytes)
        roots, _ = self.prepare()
        self.assertEqual(next(roots[0].rglob(self.record["filename"])).read_bytes(), self.expected)

    def test_game_archive_with_identical_resource_but_different_whole_hash_is_rejected(self):
        self.source.unlink()
        audited_archive = pack_dbpf({self.key: self.stored, (1, 2, 3): b"audited other resource"})
        changed_archive = pack_dbpf({self.key: self.stored, (1, 2, 3): b"different other resource"})
        audit = json.loads((self.library / "audit.json").read_text())
        audit["scope"]["archive"] = "<Game>/SimCity_3.dat"
        audit["matches"][0]["archive_sha256"] = hashlib.sha256(audited_archive).hexdigest()
        (self.library / "audit.json").write_text(json.dumps(audit))
        source = self.game / "SimCity_3.dat"
        source.write_bytes(changed_archive)
        with self.assertRaisesRegex(ValueError, "even when its pavement resource is identical"):
            self.prepare()
        self.assertFalse((self.work / "local").exists())
        self.assertEqual(source.read_bytes(), changed_archive)

    def test_existing_exact_capture_cannot_bypass_the_game_archive_fingerprint(self):
        self.source.unlink()
        audited_archive = pack_dbpf({self.key: self.stored, (1, 2, 3): b"audited game"})
        changed_archive = pack_dbpf({self.key: self.stored, (1, 2, 3): b"another game"})
        audit = json.loads((self.library / "audit.json").read_text())
        audit["scope"]["archive"] = "<Game>/SimCity_3.dat"
        audit["matches"][0]["archive_sha256"] = hashlib.sha256(audited_archive).hexdigest()
        (self.library / "audit.json").write_text(json.dumps(audit))
        source = self.game / "SimCity_3.dat"
        source.write_bytes(changed_archive)
        captured = self.plugins / self.record["filename"]
        captured.write_bytes(self.expected)
        with self.assertRaisesRegex(ValueError, "differs from the exact supported game archive"):
            self.prepare()
        self.assertFalse((self.work / "local").exists())
        self.assertEqual(captured.read_bytes(), self.expected)
        source.write_bytes(audited_archive)
        roots, records = self.prepare()
        self.assertEqual((roots, records), ([], []))
        self.assertFalse((self.work / "local").exists())

    def test_capture_final_archive_hash_is_independently_checked(self):
        self.record["sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "fingerprint differs"):
            self.prepare()


class OrchestrationTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name).resolve()
        self.plugins = self.base / "Plugins"
        self.plugins.mkdir()
        self.game = self.base / "Game"
        self.game.mkdir()
        self.extra = self.base / "GamePlugins"
        self.extra.mkdir()
        for name in ("memo.submenus.dll", "SC4ResourceLoadingHooks.dll", "submenu-essentials.dat"):
            (self.extra / name).write_bytes(b"synthetic submenu dependency")
        self.work = self.base / "Work"
        self.plan = service.Installation(self.game, self.plugins, (self.extra,), "win32")
        self.ids = ["first-piece", "second-piece"]
        self.audit = {"profile": "nam50-rhd", "donors": [
            {"filename": "NetworkAddonMod_Controller.dat", "sha256": "1" * 64,
             "path": str(self.extra / "NetworkAddonMod_Controller.dat")},
            {"filename": "SCP_OrdinaryRoad_Path_Capture.dat", "sha256": "2" * 64,
             "path": str(self.work / "local/captures/run/SCP_OrdinaryRoad_Path_Capture.dat")},
        ]}
        for patcher in (
                patch.object(service, "discover_installation", return_value=self.plan),
                patch.object(service, "installed_selection", return_value=self.ids),
                patch.object(service, "prepare_captures", return_value=([], []))):
            patcher.start()
            self.addCleanup(patcher.stop)

    def _prebuilt_runtime(self, *, payload_present=True):
        root = self.base / "Runtime"
        (root / "config").mkdir(parents=True)
        (root / "config/installer.jsonc").write_bytes((ROOT / "config/installer.jsonc").read_bytes())
        payload = root / "installer/prebuilt"
        payload.parent.mkdir()
        manifest = b'{"synthetic": true}'
        if payload_present:
            payload.mkdir()
            (payload / "manifest.json").write_bytes(manifest)
        info = {"schema_version": 1, "kind": "verified-prebuilt", "source_commit": "a" * 40,
                "prebuilt_payload_manifest_sha256": hashlib.sha256(manifest).hexdigest()}
        (root / "installer/build-info.json").write_text(json.dumps(info), encoding="utf-8")
        runtime = {"schema_version": 1, "kind": "verified-prebuilt-runtime", "source_commit": info["source_commit"]}
        (root / "installer/runtime-manifest.json").write_text(json.dumps(runtime), encoding="utf-8")
        return root, payload, info

    def test_prebuilt_install_bypasses_local_build_menus_and_geometry_verification(self):
        root, payload, info = self._prebuilt_runtime()
        capture_root, captures = self.work / "local/captures/run", [{"label": "ordinary_road"}]
        events = []
        with patch.object(service, "prepare_captures", return_value=([capture_root], captures)) as capture, \
                patch("scp.build.doctor", return_value=self.audit) as doctor, patch("scp.build.build_project") as build, \
                patch("scp.menu_experiment.build_assembly_menus") as menu, \
                patch("scp.build.verify_build") as verify, patch("scp.install.install_build") as local_install, \
                patch("scp.install.install_prebuilt",
                      return_value={"status": "installed", "backup_id": "synthetic"}) as install:
            result = service.run_install(root, self.game, self.work, progress=events.append)
        capture.assert_called_once_with(root, self.plan, self.work, self.ids, progress=events.append,
                                        cancel=None, verify_originals=True)
        doctor.assert_called_once_with(root, self.plugins, include=self.ids,
                                       extra_roots=[self.extra, capture_root])
        for local_stage in (build, menu, verify, local_install):
            local_stage.assert_not_called()
        install.assert_called_once_with(
            payload, self.plugins, self.work / "backups", extra_roots=[self.extra, capture_root],
            source_commit=info["source_commit"], expected_piece_ids=self.ids,
            expected_manifest_sha256=info["prebuilt_payload_manifest_sha256"],
            expected_profile={"id": "nam50-rhd", "donors": [
                {"filename": "NetworkAddonMod_Controller.dat", "sha256": "1" * 64},
                {"filename": "SCP_OrdinaryRoad_Path_Capture.dat", "sha256": "2" * 64},
            ]})
        self.assertEqual([event["phase"] for event in events], ["discover", "selection", "audit", "install", "complete"])
        self.assertEqual(events[-2]["distribution"], "verified-prebuilt")
        self.assertEqual(result["captures"], captures)
        self.assertEqual(result["piece_ids"], self.ids)
        saved = json.loads((self.work / "last-installation.json").read_text())
        self.assertEqual(saved["distribution"], "verified-prebuilt")
        self.assertEqual(saved["backup_id"], "synthetic")

    def test_prebuilt_package_without_payload_or_metadata_never_falls_back(self):
        root, _, info = self._prebuilt_runtime(payload_present=False)
        metadata = root / "installer/build-info.json"
        with patch.object(service, "prepare_install_build") as build, patch("scp.install.install_prebuilt") as install:
            with self.assertRaisesRegex(ValueError, "prebuilt piece payload is missing"):
                service.run_install(root, self.game, self.work)
            metadata.unlink()
            with self.assertRaisesRegex(ValueError, "missing its package metadata"):
                service.run_install(root, self.game, self.work)
            metadata.write_text(json.dumps({"schema_version": 1, "kind": "source-local-builder",
                                            "source_commit": info["source_commit"]}), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "metadata and runtime manifest disagree"):
                service.run_install(root, self.game, self.work)
        build.assert_not_called()
        install.assert_not_called()
        self.assertFalse(self.work.exists())

    def test_prebuilt_validation_failure_never_falls_back_or_records_success(self):
        root, _, _ = self._prebuilt_runtime()
        with patch.object(service, "prepare_install_build") as build, \
                patch("scp.build.doctor", return_value=self.audit), \
                patch("scp.install.install_prebuilt", side_effect=ValueError("payload hash mismatch")):
            with self.assertRaisesRegex(ValueError, "payload hash mismatch"):
                service.run_install(root, self.game, self.work)
        build.assert_not_called()
        self.assertFalse((self.work / "last-installation.json").exists())

    def test_prebuilt_compatibility_failure_stops_before_installing(self):
        root, _, _ = self._prebuilt_runtime()
        with patch("scp.build.doctor", side_effect=ValueError("native approach conflict")), \
                patch("scp.install.install_prebuilt") as install:
            with self.assertRaisesRegex(ValueError, "native approach conflict"):
                service.run_install(root, self.game, self.work)
        install.assert_not_called()
        self.assertFalse((self.work / "last-installation.json").exists())

    def test_complete_selection_and_explicit_roots_reach_every_existing_stage(self):
        events = []
        with patch("scp.build.doctor") as doctor, patch("scp.build.build_project") as build, \
                patch("scp.menu_experiment.build_assembly_menus") as menu, \
                patch("scp.install.install_build", return_value={"status": "installed", "backup_id": "synthetic"}) as install:
            result = service.run_install(ROOT, self.game, self.work, progress=events.append)
        for stage in (doctor, build):
            self.assertEqual(stage.call_args.kwargs["include"], self.ids)
            self.assertEqual(stage.call_args.kwargs["extra_roots"], [self.extra])
        expected_layouts = [
            {"domain_id": "high-speed-rail", "layout_id": "trumpet"},
            {"domain_id": "highway", "layout_id": "compact-diagonal-diamond"},
            {"domain_id": "highway", "layout_id": "modular-diagonal-diamond"},
            {"domain_id": "highway", "layout_id": "compact-modular-diagonal-diamond"},
            {"domain_id": "highway", "layout_id": "parallel-diagonal-diamond"},
            {"domain_id": "highway", "layout_id": "parallel-diagonal-diamond-alignment-b"},
            {"domain_id": "highway", "layout_id": "ddrhw-compact-diagonal-y-junction"},
            {"domain_id": "highway", "layout_id": "ddrhw-compact-diagonal-y-junction-reversed"},
        ]
        menu.assert_called_once()
        self.assertEqual(menu.call_args.kwargs["selections"], expected_layouts)
        self.assertEqual(menu.call_args.kwargs["extra_roots"], [self.extra])
        install.assert_called_once()
        self.assertEqual(install.call_args.args[0], menu.call_args.args[2])
        self.assertEqual(install.call_args.kwargs["extra_roots"], [self.extra])
        self.assertEqual(result["piece_ids"], self.ids)
        self.assertFalse(result["in_game_tested"])
        self.assertEqual(json.loads((self.work / "last-installation.json").read_text())["backup_id"], "synthetic")
        self.assertEqual(list(self.plugins.iterdir()), [])
        self.assertEqual(events[-2]["phase"], "install")
        self.assertFalse(events[-2]["cancellation_available"])

    def test_secondary_data_choice_is_forwarded_for_installation(self):
        chosen_data = self.base / "Explicit Player Data"
        with patch.object(service, "discover_installation", return_value=self.plan) as discover, \
                patch("scp.build.doctor"), patch("scp.build.build_project"), \
                patch("scp.menu_experiment.build_assembly_menus"), \
                patch("scp.install.install_build", return_value={"status": "installed", "backup_id": "synthetic"}):
            service.run_install(ROOT, self.game, self.work, player_data=chosen_data)
        self.assertEqual(discover.call_args.args, (self.game,))
        self.assertEqual(discover.call_args.kwargs["player_data"], chosen_data)

    def test_failed_build_never_calls_menu_or_installer(self):
        with patch("scp.build.doctor"), patch("scp.build.build_project", side_effect=ValueError("compiler rejected geometry")), \
                patch("scp.menu_experiment.build_assembly_menus") as menu, patch("scp.install.install_build") as install:
            with self.assertRaisesRegex(ValueError, "compiler rejected geometry"):
                service.run_install(ROOT, self.game, self.work)
        menu.assert_not_called()
        install.assert_not_called()
        self.assertEqual(list(self.plugins.iterdir()), [])

    def test_cancellation_after_build_never_calls_installer(self):
        stopped = [False]

        def build(*args, **kwargs):
            stopped[0] = True

        with patch("scp.build.doctor"), patch("scp.build.build_project", side_effect=build), \
                patch("scp.install.install_build") as install:
            with self.assertRaises(service.InstallationCancelled):
                service.run_install(ROOT, self.game, self.work, cancel=lambda: stopped[0])
        install.assert_not_called()
        self.assertEqual(list(self.plugins.iterdir()), [])

    def test_working_folder_must_not_overlap_any_scanned_plugins(self):
        for work in (self.plugins / "work", self.extra / "work", self.base):
            with self.subTest(work=work):
                with self.assertRaisesRegex(ValueError, "outside every Plugins"):
                    service.run_install(ROOT, self.game, work)

    def test_synthetic_self_test_checks_real_installation_and_rollback(self):
        result = service.self_test(ROOT)
        self.assertTrue(result["planar_geometry_runtime_checked"])
        self.assertTrue(result["real_receipt_install_and_rollback"])
        self.assertTrue(result["geometry_verification_mocked_for_synthetic_fixture"])
        self.assertFalse(result["live_game_modified"])
        self.assertEqual(result["implemented_pieces"], len(service.all_implemented_ids(ROOT)))
        self.assertEqual(result["assembly_menu_layouts"], 8)

    def test_synthetic_self_test_rejects_a_broken_bundled_triangulator(self):
        from shapely import GeometryCollection
        with patch("shapely.constrained_delaunay_triangles", return_value=GeometryCollection()):
            with self.assertRaisesRegex(ValueError, "boundary-and-hole triangulation"):
                service.self_test(ROOT)

    def test_undo_rejects_a_different_plugins_destination(self):
        self.work.mkdir()
        record = {"status": "installed", "backup_root": str(self.work / "backups"),
                  "installation": {"plugins": str(self.base / "Other Plugins")}}
        (self.work / "last-installation.json").write_text(json.dumps(record))
        with patch("scp.install.rollback_install") as rollback:
            with self.assertRaisesRegex(ValueError, "belongs to another Plugins"):
                service.undo_install(ROOT, self.game, self.work)
        rollback.assert_not_called()

    def test_undo_uses_saved_exact_transaction_and_capture_roots(self):
        self.work.mkdir()
        capture_root = self.work / "local/captures/earlier"
        record = {"status": "installed", "backup_root": str(self.work / "backups"),
                  "backup_id": "saved-exact-id", "extra_plugins": [str(self.extra), str(capture_root)],
                  "installation": {"plugins": str(self.plugins)}}
        (self.work / "last-installation.json").write_text(json.dumps(record))
        events = []
        with patch("scp.install.rollback_install", return_value={"status": "rolled_back"}) as rollback:
            service.undo_install(ROOT, self.game, self.work, progress=events.append)
        rollback.assert_called_once_with(self.plugins, self.work / "backups", "saved-exact-id",
                                         extra_roots=[self.extra, capture_root])
        self.assertEqual(json.loads((self.work / "last-installation.json").read_text())["status"], "rolled_back")
        self.assertEqual(events[0], {"phase": "undo", "cancellation_available": False})

    def test_undo_does_not_accept_a_backup_directory_injected_into_its_record(self):
        self.work.mkdir()
        record = {"status": "installed", "backup_root": str(self.base / "Somewhere Else"),
                  "installation": {"plugins": str(self.plugins)}, "extra_plugins": [str(self.extra)]}
        (self.work / "last-installation.json").write_text(json.dumps(record))
        with self.assertRaisesRegex(ValueError, "does not match"):
            service.undo_install(ROOT, self.game, self.work)

    def test_undo_cannot_omit_game_plugins_from_the_saved_conflict_scan(self):
        self.work.mkdir()
        record = {"status": "installed", "backup_root": str(self.work / "backups"),
                  "installation": {"plugins": str(self.plugins)}, "extra_plugins": []}
        (self.work / "last-installation.json").write_text(json.dumps(record))
        with patch("scp.install.rollback_install") as rollback:
            with self.assertRaisesRegex(ValueError, "recovery input folders do not match"):
                service.undo_install(ROOT, self.game, self.work)
        rollback.assert_not_called()


if __name__ == "__main__":
    unittest.main()
