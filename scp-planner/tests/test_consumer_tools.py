"""Keep Planner launchers thin and preserve frozen evidence without concealing edits."""
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

PLANNER = Path(__file__).resolve().parents[1]


def tool(name):
    spec = importlib.util.spec_from_file_location(name, PLANNER / 'tools' / (name+'.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ConsumerToolTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.audit, cls.renderer = tool('run_metadata_pilot'), tool('render_metadata_pilot')

    def test_compiled_audit_delegates_without_copying_archive_or_path_parsers(self):
        returned = {'manifest_sha256': 'digest', 'pieces': {'p': {'routes': [1], 'endpoint_route_refs': {'m': [1]}, 'actual_path_facts': 'passed'}}}
        source = SimpleNamespace(verify_compiled=lambda *args: returned)
        with patch('scp_planner._source.source_module', return_value=source):
            result = self.audit.verify_compiled(Path('/library'), Path('/library/build'), {})
        self.assertEqual(result['pieces']['p'], {'actual_path_facts': 'passed'})
        self.assertEqual(returned['pieces']['p']['routes'], [1])

    def test_frozen_snapshot_reports_only_explicitly_authorized_changes(self):
        names = ['domains/high-speed-rail/00_pieces/example/README.md',
                 'domains/high-speed-rail/connector-profiles.json',
                 'domains/high-speed-rail/domain.json',
                 'domains/high-speed-rail/00_pieces/example/piece.json']
        with tempfile.TemporaryDirectory(prefix='scp-consumer-snapshot-') as temporary:
            root = Path(temporary)
            planner = root / 'planner'
            (planner / 'local/pilot').mkdir(parents=True)
            (planner / 'pilot.json').write_text(json.dumps({'pieces': ['example']}))
            frozen = {}
            for name in names:
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('before')
                frozen[name] = hashlib.sha256(path.read_bytes()).hexdigest()
            snapshot = planner / 'local/pilot/source-snapshot.json'
            snapshot.write_text(json.dumps({'files': frozen}))
            before = snapshot.read_bytes()
            for name in names[:-1]:
                (root / name).write_text('authorized after')
            with patch.object(self.audit, 'PLANNER', planner):
                report = self.audit.check_preserved_inputs(root)
                self.assertEqual(report['existing_files_checked'], 1)
                self.assertEqual(set(report['authorized_generated_readme_changes']), {names[0]})
                self.assertEqual(set(report['authorized_connector_definition_changes']), set(names[1:3]))
                for values in report['authorized_connector_definition_changes'].values():
                    self.assertNotEqual(values['before_sha256'], values['current_sha256'])
                (root / names[-1]).write_text('unexpected geometry definition change')
                with self.assertRaises(ValueError):
                    self.audit.check_preserved_inputs(root)
            self.assertEqual(snapshot.read_bytes(), before)

    def test_render_launcher_delegates_to_canonical_piece_outputs(self):
        calls = []
        renderer = SimpleNamespace(render_overviews=lambda *args, **kwargs: calls.append((args, kwargs)) or {'pieces': {}})
        with patch.object(self.renderer, 'source_module', return_value=renderer), patch.object(sys, 'argv', ['render_metadata_pilot.py']), patch('builtins.print'):
            self.renderer.main()
        self.assertEqual(len(calls), 1)
        self.assertIsNone(calls[0][1]['output_root'])
        self.assertEqual(calls[0][1]['domain_id'], 'high-speed-rail')

    def test_render_launcher_rejects_recreating_old_maintained_planner_assets(self):
        old = str(PLANNER / 'docs/assets/connector-metadata')
        with patch.object(sys, 'argv', ['render_metadata_pilot.py', '--output', old]), patch('sys.stderr'), self.assertRaises(SystemExit) as caught:
            self.renderer.main()
        self.assertEqual(caught.exception.code, 2)


if __name__ == '__main__':
    unittest.main()
