"""ID aliases preserve frozen proofs without relaxing poses or resource hashes."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

from scp.subject_identity import canonical_subject_id
from scp_hsr import hsr_trumpet_verify as physical
from scp_hsr import hsr_trumpet_border_verify as border
from scp_hsr.hsr_trumpet_rework_verify import read_rework_record
from scp_hsr_tools import verify_hsr_trumpet as trumpet


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


class IdentityEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / 'config').mkdir()
        shutil.copyfile(trumpet.ROOT / 'config/subject-id-migration.jsonc',
                        self.root / 'config/subject-id-migration.jsonc')
        self.old = 'hsr-component-lower-paired-straight'
        self.current = canonical_subject_id(self.old, root=self.root)
        self.assembly_id = canonical_subject_id('straight-stem-trumpet', kind='assembly', root=self.root)
        self.directory = self.root / 'domains/high-speed-rail/01_assemblies' / self.assembly_id
        (self.directory / 'checks').mkdir(parents=True)

    def scene(self):
        return {
            'construction_rectangle_tiles': [2, 1], 'occupied_tiles': 2,
            'external_ports': {'west': [-8., 0., 15.5]},
            'coordinate_system': {'origin_world_m': [0., 0.], 'tile_size_m': 16.,
                                  'display_tile_centres_bounds_en': [0, 1, 0, 0],
                                  'construction_bounds_world_m': [-8., 24., -8., 8.]},
            'placements': [{'piece_id': self.old, 'origin_m': [0., 0.], 'rotation_degrees_ccw': 0},
                           {'piece_id': self.old, 'origin_m': [16., 0.], 'rotation_degrees_ccw': 0}],
        }

    def frozen(self):
        scene = self.scene()
        layout = physical.physical_layout(scene)
        record = {'schema_version': 1, 'assembly_id': 'straight-stem-trumpet',
                  'layout': layout, 'layout_sha256': digest(layout)}
        path = self.directory / 'checks/layout.json'
        path.write_text(json.dumps(record, indent=2) + '\n')
        current = deepcopy(scene)
        for placement in current['placements']:
            placement['piece_id'] = self.current
        return path, current

    def test_old_layout_aliases_match_without_changing_frozen_bytes(self):
        path, scene = self.frozen()
        original = path.read_bytes()
        result = physical.audit_approved_layout(scene, self.assembly_id, root=self.root)
        self.assertEqual(result['layout_sha256'], json.loads(original)['layout_sha256'])
        self.assertEqual(result['reviewed_placements_preserved'], 2)
        self.assertEqual(path.read_bytes(), original)

    def test_aliases_do_not_hide_unknown_owners_or_changed_physical_facts(self):
        _, scene = self.frozen()
        mutations = []
        for field, value in (('piece_id', 'unknown-track'), ('origin_m', [0.001, 0.]),
                             ('rotation_degrees_ccw', 90)):
            candidate = deepcopy(scene)
            candidate['placements'][0][field] = value
            mutations.append(candidate)
        for field, value in (('occupied_tiles', 3), ('construction_rectangle_tiles', [3, 1]),
                             ('external_ports', {'west': [-8.001, 0., 15.5]})):
            candidate = deepcopy(scene)
            candidate[field] = value
            mutations.append(candidate)
        candidate = deepcopy(scene)
        candidate['coordinate_system']['origin_world_m'][0] = .001
        mutations.append(candidate)
        for candidate in mutations:
            with self.subTest(candidate=candidate), self.assertRaises(ValueError):
                physical.audit_approved_layout(candidate, self.assembly_id, root=self.root)

    def test_frozen_hash_and_assembly_identity_still_fail_closed(self):
        path, scene = self.frozen()
        record = json.loads(path.read_text())
        record['layout']['placements'][0]['piece_id'] = self.current
        path.write_text(json.dumps(record))
        with self.assertRaisesRegex(ValueError, 'malformed or changed'):
            physical.audit_approved_layout(scene, self.assembly_id, root=self.root)
        path, scene = self.frozen()
        record = json.loads(path.read_text())
        record['assembly_id'] = 'unknown-layout'
        path.write_text(json.dumps(record))
        with self.assertRaises(ValueError):
            physical.audit_approved_layout(scene, self.assembly_id, root=self.root)

    def test_historical_snapshot_and_current_layout_use_same_strict_adapter(self):
        for integrated in (False, True):
            source = (trumpet.ASSEMBLY if integrated else
                      trumpet.ASSEMBLY / trumpet.SNAPSHOT_RELATIVE)
            target = self.directory if integrated else self.directory / trumpet.SNAPSHOT_RELATIVE
            (target / 'checks').mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source / 'checks/layout.json', target / 'checks/layout.json')
            original = (target / 'checks/layout.json').read_bytes()
            scene = json.loads((source / 'assembly.json').read_text())
            for placement in scene['placements']:
                placement['piece_id'] = canonical_subject_id(placement['piece_id'], root=self.root)
            with patch.object(trumpet, 'ROOT', self.root), patch.object(trumpet, 'ASSEMBLY', self.directory):
                trumpet.audit_approved_layout(scene, current_border_integration=integrated)
                changed = deepcopy(scene)
                changed['placements'][0]['origin_m'][0] += .001
                with self.assertRaisesRegex(ValueError, 'approved positions'):
                    trumpet.audit_approved_layout(changed, current_border_integration=integrated)
            self.assertEqual((target / 'checks/layout.json').read_bytes(), original)

    def test_literal_historical_contracts_remain_unchanged(self):
        path = trumpet.ASSEMBLY / 'checks/junction-rework.json'
        original = path.read_bytes()
        read_rework_record(path, root=trumpet.ROOT, require_completed=False)
        self.assertEqual(path.read_bytes(), original)
        retirement = (trumpet.ASSEMBLY / border.PARENT_RETIREMENT_RELATIVE).read_bytes()
        self.assertEqual(json.loads(retirement), border.parent_retirement_record())
        frozen = border.frozen_inputs()
        integration = json.loads((trumpet.ASSEMBLY / 'checks/border-piece-integration.json').read_text())
        self.assertEqual(integration['policy'], border.integration_policy(frozen))

    def test_piece_identity_alias_keeps_numeric_resource_and_filename_constraints(self):
        historical = deepcopy(border.CORE_IDENTITY)
        current = deepcopy(historical)
        current['id'] = canonical_subject_id(historical['id'])
        current['asset_file'] = str(Path(historical['asset_file']).with_name('SCP_' + current['id'] + '.dat'))
        expected = border.piece_identity(historical)
        self.assertEqual(border.piece_identity(current), expected)
        for field, value in (('puzzle_id', 'ffff'), ('tile_ids', ['ffffffff']),
                             ('asset_file', 'different-directory/SCP_' + current['id'] + '.dat')):
            changed = deepcopy(current)
            changed[field] = value
            self.assertNotEqual(border.piece_identity(changed), expected)
        changed = deepcopy(current)
        changed['menu']['id'] = 'ffffffff'
        self.assertNotEqual(border.piece_identity(changed), expected)

    def test_world_owner_alias_does_not_hide_changed_resource_bytes_or_cell_pose(self):
        position = (0., 0.)
        payload = {'model_0': b'original saved model'}
        candidate = {position: {'piece_id': self.current, 'cell': (0, 0), 'rotation': 0,
                                'resources': payload}}
        descriptor = {'world_cells': [{'world_east_north_m': list(position), 'piece_id': self.old,
                       'cell': [0, 0], 'rotation_quarter_turns_ccw': 0,
                       'resources_sha256': {name: hashlib.sha256(raw).hexdigest()
                                            for name, raw in payload.items()}}], 'actual_tile_triangles': 0}
        with patch.object(trumpet, 'expected_occupied_cells', return_value=1), \
                patch.object(trumpet, 'REPLACEMENTS', {}), patch.object(trumpet, 'triangle_count', return_value=0):
            trumpet.audit_current_world_tiles(candidate, descriptor)
            for field, value in (('piece_id', 'unknown-track'), ('cell', (1, 0)), ('rotation', 1),
                                 ('resources', {'model_0': b'changed saved model'})):
                changed = deepcopy(candidate)
                changed[position][field] = value
                with self.subTest(field=field), self.assertRaises(ValueError):
                    trumpet.audit_current_world_tiles(changed, descriptor)


if __name__ == '__main__':
    unittest.main()
