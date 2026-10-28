"""Entry-point isolation and checks that protect the graphical install flow."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = next(path for path in Path(__file__).resolve().parents if (path / 'project.json').is_file())
sys.path.insert(0, str(ROOT / 'installer'))
from scp_installer import ui_support


class InstallerEntryTests(unittest.TestCase):
    def test_version_reads_this_checkout_without_a_gui_or_game(self):
        with tempfile.TemporaryDirectory() as temporary:
            report = Path(temporary) / 'version.json'
            result = subprocess.run([sys.executable, '-B', str(ROOT / 'installer/main.py'),
                                     '--version', '--report', str(report)],
                                    cwd=temporary, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            value = json.loads(report.read_text())
            self.assertEqual(value['kind'], 'source-local-builder')
            self.assertFalse(value['bundled_native_game_resources'])
            self.assertTrue(value['experimental'])

    def test_offline_entry_exercises_real_owned_transaction_without_game_inputs(self):
        with tempfile.TemporaryDirectory() as temporary:
            report = Path(temporary) / 'self-test.json'
            result = subprocess.run([sys.executable, '-B', str(ROOT / 'installer/main.py'),
                                     '--self-test', '--report', str(report)],
                                    cwd=temporary, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            value = json.loads(report.read_text())
            self.assertEqual(value['status'], 'passed')
            self.assertEqual(value['implemented_pieces'], 166)
            self.assertTrue(value['real_receipt_install_and_rollback'])
            self.assertTrue(value['geometry_verification_mocked_for_synthetic_fixture'])
            self.assertFalse(value['live_game_modified'])

    def test_running_game_is_rejected_using_exact_process_name(self):
        processes = SimpleNamespace(stdout=b'"notepad.exe","100"\n"SimCity 4.exe","101"\n')
        with patch.object(ui_support.sys, 'platform', 'win32'), patch.object(ui_support.subprocess, 'run', return_value=processes):
            with self.assertRaisesRegex(ValueError, 'Close SimCity 4'):
                ui_support.require_game_closed()

    def test_unrelated_process_with_similar_name_does_not_block_installation(self):
        processes = SimpleNamespace(stdout=b'"my SimCity 4.exe notes.txt","100"\n"explorer.exe","101"\n')
        with patch.object(ui_support.sys, 'platform', 'win32'), patch.object(ui_support.subprocess, 'run', return_value=processes):
            ui_support.require_game_closed()

    def test_localized_non_utf8_process_output_preserves_game_detection(self):
        for running in (False, True):
            with self.subTest(running=running):
                output = b'"explorer.exe","100","Sitzung\x81","1","123\xa0K"\r\n'
                if running:
                    output += b'"SimCity4.exe","101","Sitzung\x81","1","123\xa0K"\r\n'
                processes = SimpleNamespace(stdout=output)
                with patch.object(ui_support.sys, 'platform', 'win32'), patch.object(ui_support.subprocess, 'run', return_value=processes):
                    if running:
                        with self.assertRaisesRegex(ValueError, 'Close SimCity 4'):
                            ui_support.require_game_closed()
                    else:
                        ui_support.require_game_closed()

    def test_failed_process_scan_stops_instead_of_assuming_game_is_closed(self):
        with patch.object(ui_support.sys, 'platform', 'win32'), patch.object(ui_support.subprocess, 'run', side_effect=OSError('unavailable')):
            with self.assertRaisesRegex(ValueError, 'could not check'):
                ui_support.require_game_closed()


if __name__ == '__main__':
    unittest.main()
