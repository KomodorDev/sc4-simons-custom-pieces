"""Portable negative controls for the approved west-straight extraction.

Expectations come from frozen saved-resource facts, never a preceding DAT.
Synthetic resources exercise rejection paths; actual mesh/profile acceptance
remains part of the independent native assembly audit.
"""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from scp.track_paths import _parse_paths, encode_paths
from scp_hsr.directional_t_verify import _journeys
from scp_hsr.hsr_components_layout import component_layout
from scp_hsr.hsr_components_verify import CONTRACTS
from scp_hsr.hsr_trumpet_verify import CONTRACT, key, rotate
from scp_hsr.hsr_merge_extraction_verify import (
    FROZEN_FILES, HISTORY, MERGE_ID, ROOT, SEAM_MODEL_SHA256, STRAIGHT_ID,
    audit_collar_sections, audit_journeys_and_supports, audit_native_seam, audit_replacement_paths,
    audit_unchanged_archives, audit_world_resources, frozen_baseline,
)


def paired_routes():
    return [dict(transport=7, entry=3, exit=1, junction=False, role='synthetic',
                 points=[(2., -8., 15.5), (2., 8., 15.5)]),
            dict(transport=7, entry=1, exit=3, junction=False, role='synthetic',
                 points=[(-2., 8., 15.5), (-2., -8., 15.5)])]


def synthetic_world():
    """A complete 105-cell resource inventory, without private game assets."""
    tiles, expected = {}, []
    ordinary = {'path': encode_paths(paired_routes()),
                **{f'model_{zoom}': b'synthetic model' for zoom in range(5)},
                **{f'shadow_{zoom}': b'synthetic shadow' for zoom in range(5)}}
    for column in range(105):
        position = (-112.+16.*column, 0.)
        merging = position in ((32., 0.), (48., 0.), (64., 0.), (80., 0.), (96., 0.))
        old_cell = (int((position[0]-32.)/16.), 0) if merging else (0, 0)
        piece_id = MERGE_ID if merging else STRAIGHT_ID
        rotation = 0 if merging else 3
        resources = dict(ordinary)
        expected.append({'world_east_north_m': list(position), 'piece_id': piece_id,
            'cell': list(old_cell), 'rotation_quarter_turns_ccw': rotation,
            'resources_sha256': {name: hashlib.sha256(raw).hexdigest() for name, raw in resources.items()}})
        cell = (old_cell[0]-1, 0) if merging else old_cell
        if position == (32., 0.):
            piece_id, cell, rotation = STRAIGHT_ID, (0, 0), 3
        tiles[position] = {'piece_id': piece_id, 'cell': cell, 'rotation': rotation,
                          'instance_id': 'P26' if position == (32., 0.) else 'P07',
                          'resources': resources}
    return tiles, {'world_cells': expected}


def source_world():
    """Encode current authored routes; compare them with independently saved facts."""
    domain = ROOT/'domains/high-speed-rail'
    scene = json.loads((domain/'01_assemblies/straight-stem-trumpet/assembly.json').read_text())
    records, supports, occupied = [], [], []
    for placement in scene['placements']:
        piece = json.loads((domain/'00_pieces'/placement['piece_id']/'piece.json').read_text())
        turns, origin = placement['rotation_degrees_ccw']//90, placement['origin_m']
        for cell, data in component_layout(piece['recipe']).items():
            east, north, _ = rotate((16.*cell[0], -16.*cell[1], 0.), turns)
            centre = east+origin[0], north+origin[1]
            occupied.append(centre)
            if not data['routes']:
                continue
            for route in _parse_paths(encode_paths(data['routes'])):
                points = []
                for point in route['points']:
                    east, north, height = rotate(point, turns)
                    points.append(key((east+centre[0], north+centre[1], height)))
                records.append(((placement['instance_id'], *cell),
                                {**route, 'instance_id': placement['instance_id']}, points))
        for east, south in CONTRACTS[piece['recipe']]['support_centres_xz']:
            east, north, _ = rotate((east, -south, 0.), turns)
            supports.append((east+origin[0], north+origin[1]))
    return scene, occupied, _journeys(records, CONTRACT), supports


def collar_surfaces(*, bed_gap=0., parapet_gap=0.):
    """Simple continuous saved-style slabs and walls, with optional true slits."""
    surfaces = [(14.01067, [(-7.5, 7.5)]),
                (16.189326, [(-7.5, 6.247), (6.247+bed_gap, 7.5)] if bed_gap else [(-7.5, 7.5)]),
                (16.98933, [(-7.5, -5.9965477), (5.9965477, 7.358746),
                             (7.358746+parapet_gap, 7.5)] if parapet_gap
                 else [(-7.5, -5.9965477), (5.9965477, 7.5)])]
    triangles = []
    for height, intervals in surfaces:
        for low, high in intervals:
            vertices = [(40., height, -low, 0., 0.), (56., height, -low, 1., 0.),
                        (56., height, -high, 1., 1.), (40., height, -high, 0., 1.)]
            triangles.extend(((vertices[0], vertices[1], vertices[2]),
                              (vertices[0], vertices[2], vertices[3])))
    return triangles


class MergeExtractionPreservationTests(unittest.TestCase):
    def test_frozen_facts_need_no_predecessor_archive_and_cannot_be_rehashed(self):
        baseline = frozen_baseline()
        self.assertEqual((len(baseline['world_cells']), len(baseline['pieces']), len(baseline['journeys'])),
                         (105, 13, 6))
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            for name in FROZEN_FILES:
                (directory/name).write_bytes((HISTORY/name).read_bytes())
            name = 'checks-resources-before-merge-west-tail-extraction.json'
            baseline['world_cells'][0]['resources_sha256']['path'] = '0'*64
            (directory/name).write_text(json.dumps(baseline))
            with self.assertRaisesRegex(ValueError, 'frozen baseline differs'):
                frozen_baseline(directory)

    def test_source_recomposition_keeps_six_saved_journeys_all_cells_and_supports(self):
        scene, occupied, journeys, supports = source_world()
        self.assertEqual(len(scene['placements']), 26)
        self.assertEqual(len(occupied), len(set(occupied)))
        self.assertEqual(set(occupied), {tuple(row['world_east_north_m']) for row in frozen_baseline()['world_cells']})
        report = audit_journeys_and_supports(journeys, supports, frozen_baseline())
        self.assertEqual(report['complete_journey_counts_and_point_hashes_identical'], 6)
        self.assertEqual(report['support_positions_preserved'], 74)
        placements = {row['instance_id']: row for row in scene['placements']}
        self.assertEqual((placements['P07']['origin_m'], placements['P26']['origin_m'],
                          placements['P26']['rotation_degrees_ccw']), ([48., 0.], [32., 0.], 270))

    def test_changed_journey_point_missing_journey_and_moved_support_are_rejected(self):
        _, _, journeys, supports = source_world()
        baseline = frozen_baseline()
        changed = deepcopy(journeys)
        movement = next(iter(changed))
        changed[movement][1] = tuple(value+.001 if index == 0 else value
                                    for index, value in enumerate(changed[movement][1]))
        with self.assertRaisesRegex(ValueError, 'complete assembly journey'):
            audit_journeys_and_supports(changed, supports, baseline)
        changed.pop(movement)
        with self.assertRaisesRegex(ValueError, 'six complete assembly journeys'):
            audit_journeys_and_supports(changed, supports, baseline)
        moved = list(supports)
        moved[0] = moved[0][0]+.001, moved[0][1]
        with self.assertRaisesRegex(ValueError, 'support positions'):
            audit_journeys_and_supports(journeys, moved, baseline)

    def test_only_two_model_cells_may_change_and_retained_paths_and_shadows_stay_exact(self):
        tiles, baseline = synthetic_world()
        self.assertEqual(audit_world_resources(tiles, baseline)['unchanged_world_cells_all_resources_exact'], 103)
        changes = [((64., 0.), 'model_0', 'outside the replacement'),
                   ((48., 0.), 'path', 'retained saved PATH'),
                   ((48., 0.), 'shadow_0', 'retained seam shadow'),
                   ((32., 0.), 'model_0', 'existing standard straight')]
        for position, resource, message in changes:
            with self.subTest(position=position, resource=resource):
                changed = deepcopy(tiles)
                changed[position]['resources'][resource] += b'changed'
                with self.assertRaisesRegex(ValueError, message):
                    audit_world_resources(changed, baseline)
        tiles.pop((64., 0.))
        with self.assertRaisesRegex(ValueError, '105 occupied world cells'):
            audit_world_resources(tiles, baseline)

    def test_wrong_retained_local_mapping_and_replacement_pose_are_rejected(self):
        tiles, baseline = synthetic_world()
        tiles[64., 0.]['cell'] = (2, 0)
        with self.assertRaisesRegex(ValueError, 'retained world-cell mapping'):
            audit_world_resources(tiles, baseline)
        tiles, baseline = synthetic_world()
        tiles[32., 0.]['rotation'] = 0
        with self.assertRaisesRegex(ValueError, 'rotated P26 straight'):
            audit_world_resources(tiles, baseline)

    def test_replacement_flow_and_exact_world_coordinates_are_independent_literals(self):
        tile = {'rotation': 3, 'resources': {'path': encode_paths(paired_routes())}}
        self.assertEqual(audit_replacement_paths(tile)['replacement_decoded_routes_identical'], 2)
        routes = paired_routes()
        routes[0]['points'][0] = (2.001, -8., 15.5)
        tile['resources']['path'] = encode_paths(routes)
        with self.assertRaisesRegex(ValueError, 'world PATH geometry or direction'):
            audit_replacement_paths(tile)

    def test_other_archives_and_retained_active_merge_ids_cannot_change(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            pieces, saved = {}, []
            for identifier in [MERGE_ID, *[f'fixture-{number}' for number in range(12)]]:
                raw = identifier.encode()
                piece = {'id': identifier, 'recipe': identifier.replace('-', '_'), 'asset_file': identifier+'.dat'}
                pieces[identifier] = piece
                (directory/piece['asset_file']).write_bytes(raw)
                saved.append({**piece, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()})
            pieces[MERGE_ID].update(cells=[[column, 0] for column in range(4)],
                                   tile_ids=[f'7f585{column}00' for column in range(1, 5)])
            build, baseline = {'path': directory, 'pieces': pieces}, {'pieces': saved}
            self.assertEqual(audit_unchanged_archives(build, baseline)['unchanged_complete_archives_exact'], 12)
            pieces[MERGE_ID]['tile_ids'][0] = '7f585000'
            with self.assertRaisesRegex(ValueError, 'retained active cell resource IDs'):
                audit_unchanged_archives(build, baseline)
            pieces[MERGE_ID]['tile_ids'][0] = '7f585100'
            (directory/'fixture-0.dat').write_bytes(b'changed archive')
            with self.assertRaisesRegex(ValueError, 'unaffected archive'):
                audit_unchanged_archives(build, baseline)

    def test_a_candidate_cannot_supply_its_own_seam_model_acceptance_hash(self):
        self.assertEqual(SEAM_MODEL_SHA256, '59e736b92ef86c5cd6d0e69e94b5e93bc84bb09b832d906353ae685346e391c0')
        tile = {'resources': {f'model_{zoom}': b'unapproved seam' for zoom in range(5)}}
        with self.assertRaisesRegex(ValueError, 'independently bounded normalization'):
            audit_native_seam({(48., 0.): tile})

    def test_continuous_collar_surfaces_pass_independent_sections(self):
        report = audit_collar_sections(collar_surfaces())
        self.assertEqual(report['collar_horizontal_sections_checked'], 87)
        self.assertEqual(report['collar_section_stations_checked'], 29)

    def test_small_bed_gap_is_rejected_even_with_native_endpoints_unchanged(self):
        with self.assertRaisesRegex(ValueError, 'collar has a gap or invalid profile'):
            audit_collar_sections(collar_surfaces(bed_gap=.000407))

    def test_parapet_cracks_below_and_above_old_profile_tolerance_are_rejected(self):
        for width in (.00002, .000053):
            with self.subTest(gap_m=width), self.assertRaisesRegex(
                    ValueError, 'collar has a gap or invalid profile'):
                audit_collar_sections(collar_surfaces(parapet_gap=width))


if __name__ == '__main__':
    unittest.main()
