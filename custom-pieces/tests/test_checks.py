"""Isolated check runs must import every package from the selected checkout."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


BOOTSTRAP = Path(__file__).resolve().parents[1]/'framework/scp/check_bootstrap.py'


class SourcePackageIsolationTests(unittest.TestCase):
    def test_declared_tool_package_wins_over_another_checkout(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            local = root/'domains/probe/tools'
            local.mkdir(parents=True)
            (local/'__init__.py').write_text('VALUE = "selected checkout"\n')
            (local/'helper.py').write_text('VALUE = "selected helper"\n')
            (root/'pyproject.toml').write_text(
                '[tool.setuptools.package-dir]\nprobe_tools = "domains/probe/tools"\n')
            other = root/'other-checkout/probe_tools'
            other.mkdir(parents=True)
            (other/'__init__.py').write_text('raise RuntimeError("wrong checkout")\n')
            tests = root/'tests'
            tests.mkdir()
            (tests/'test_origin.py').write_text(
                'import unittest\nfrom pathlib import Path\n'
                'import probe_tools\nfrom probe_tools import helper\n'
                'class Origin(unittest.TestCase):\n'
                ' def test_origin(self):\n'
                '  self.assertEqual(probe_tools.VALUE, "selected checkout")\n'
                '  self.assertEqual(helper.VALUE, "selected helper")\n'
                f'  self.assertEqual(Path(probe_tools.__file__).parent, Path({str(local)!r}).resolve())\n')
            env = dict(os.environ, PYTHONPATH=str(other.parent))
            result = subprocess.run([sys.executable, '-B', str(BOOTSTRAP), str(root),
                                     'discover', '-s', str(tests), '-q'],
                                    cwd=root, env=env, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn('Ran 1 test', result.stderr)

    def test_package_mapping_cannot_escape_selected_root(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)/'library'
            root.mkdir()
            (root/'pyproject.toml').write_text(
                '[tool.setuptools.package-dir]\nprobe_tools = "../outside"\n')
            result = subprocess.run([sys.executable, '-B', str(BOOTSTRAP), str(root),
                                     'discover', '-s', str(root)],
                                    capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('Invalid source package directory', result.stderr)
