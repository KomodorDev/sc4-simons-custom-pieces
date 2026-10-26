"""Inspect opt-in shared Tab families without reading installed game files."""
from __future__ import annotations

import copy
import hashlib
from pathlib import Path
import re
import sys
import unittest

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp.rul0 import MARKER, ORDERING_BEGIN, ORDERING_END, compose_rul0, with_feature_sequence


NATIVE = (b'; literal native baseline\r\n[Ordering]\r\n'
          b'RotationRing = 100, 10100, 20100, 30100\r\n'
          b'AddTypes = 101, 10101, 20101, 30101\r\n'
          b'[HighwayIntersectionInfo_0x00000100]\r\nPiece = native\r\n')


def fragment(root):
    states = [root + (index << 16) for index in range(8)]
    return ('RotationRing = ' + ', '.join(f'{state:X}' for state in states) + '\r\n'
            + ''.join(f'[HighwayIntersectionInfo_0x{state:08X}]\r\n'
                      f'CopyFrom = 0x{root:08X}\r\n' for state in states))


def saved_rows(raw):
    """Independent tiny scanner reads both kinds of saved ordering row."""
    section, result = None, []
    for raw_line in raw.splitlines():
        active = raw_line.split(b';', 1)[0].strip()
        if active.startswith(b'[') and active.endswith(b']'):
            section = active[1:-1].lower()
        match = re.fullmatch(rb'(RotationRing|AddTypes)\s*=\s*(.+)', active, re.I)
        if match:
            result.append((section, match[1].decode(),
                           [int(token, 16) for token in match[2].split(b',')]))
    return result


def rewrite_insertion(raw, metadata, insertion):
    changed = raw.replace(metadata['ordering_insertion'].encode(), insertion.encode(), 1)
    return changed, dict(metadata, ordering_insertion=insertion)


class FeatureSequenceTests(unittest.TestCase):
    def setUp(self):
        self.raw, self.metadata = compose_rul0(NATIVE, [fragment(root) for root in
                                                       (0xF800, 0xF801, 0xF802, 0xF803)])

    def test_requested_order_forms_one_family_and_preserves_all_rotation_states(self):
        actual, metadata = with_feature_sequence(self.raw, self.metadata, [0xF802, 0xF800])
        rows = saved_rows(actual)
        self.assertEqual([row[1] for row in rows],
                         ['RotationRing', 'AddTypes', 'RotationRing', 'AddTypes',
                          'RotationRing', 'RotationRing'])
        self.assertEqual([row[2][0] for row in rows], [0x100, 0x101, 0xF802, 0xF800, 0xF801, 0xF803])
        self.assertTrue(all(row[0] == b'ordering' for row in rows))
        for row, root in zip(rows[2:], (0xF802, 0xF800, 0xF801, 0xF803)):
            self.assertEqual(row[2], [root + (i << 16) for i in range(8)])
        self.assertEqual(metadata['feature_sequence']['rotation_rows'], [row[2] for row in rows[2:4]])
        self.assertTrue(metadata['feature_sequence']['shared_tab_family'])

    def test_native_definitions_and_original_controller_are_exactly_recoverable(self):
        before_metadata = copy.deepcopy(self.metadata)
        for newline in (b'\r\n', b'\n'):
            original, composition = compose_rul0(NATIVE.replace(b'\r\n', newline),
                                                 [fragment(0xF800), fragment(0xF801)])
            actual, metadata = with_feature_sequence(original, composition, (0xF801, 0xF800))
            suffix = metadata['suffix'].encode()
            insertion = metadata['ordering_insertion'].encode()
            self.assertTrue(actual.endswith(suffix))
            self.assertEqual(actual[:-len(suffix)].replace(insertion, b'', 1),
                             NATIVE.replace(b'\r\n', newline))
            restored = actual.replace(insertion, metadata['feature_sequence']['previous_ordering_insertion'].encode(), 1)
            self.assertEqual(restored, original)
            self.assertEqual(hashlib.sha256(restored).hexdigest(),
                             metadata['feature_sequence']['previous_controller_sha256'])
            self.assertEqual(metadata['suffix'], composition['suffix'])
            self.assertEqual(metadata['base_sha256'], composition['base_sha256'])
        self.assertEqual(self.metadata, before_metadata)

    def test_all_four_modules_keep_exact_definitions_and_unrelated_native_family(self):
        actual, metadata = with_feature_sequence(self.raw, self.metadata, [0xF803, 0xF802, 0xF801, 0xF800])
        self.assertEqual(actual[-len(self.metadata['suffix']):], self.raw[-len(self.metadata['suffix']):])
        self.assertEqual(saved_rows(actual)[:2], saved_rows(NATIVE))
        self.assertEqual([row[1] for row in saved_rows(actual)[2:]],
                         ['RotationRing', 'AddTypes', 'AddTypes', 'AddTypes'])
        self.assertEqual(metadata['feature_sequence']['base_states'], [0xF803, 0xF802, 0xF801, 0xF800])

    def test_unknown_root_or_a_member_rotation_cannot_select_a_module(self):
        for roots in ([0xF800, 0xFFFF], [0xF800, 0x1F801]):
            with self.subTest(roots=roots), self.assertRaisesRegex(ValueError, 'unknown or noncanonical'):
                with_feature_sequence(self.raw, self.metadata, roots)

    def test_duplicate_wrong_type_empty_or_single_member_inputs_fail(self):
        for roots in ([], [0xF800], [0xF800, 0xF800], 'F800,F801', None,
                      [0xF800, 'F801'], [0xF800, True], [0xF800, -1], [0xF800, 0x100000000]):
            with self.subTest(roots=roots), self.assertRaises(ValueError):
                with_feature_sequence(self.raw, self.metadata, roots)

    def test_incomplete_or_malformed_metadata_fails(self):
        for patch in ({'base_sha256': None}, {'base_sha256': 'xyz'}, {'suffix': ''},
                      {'ordering_insertion': None}, {'suffix': 'non-ASCII \u00e9'}):
            with self.subTest(patch=patch), self.assertRaises(ValueError):
                with_feature_sequence(self.raw, dict(self.metadata, **patch), [0xF800, 0xF801])
        for raw, metadata in ((self.raw.decode(), self.metadata), (self.raw, None)):
            with self.subTest(metadata=metadata), self.assertRaises(ValueError):
                with_feature_sequence(raw, metadata, [0xF800, 0xF801])

    def test_tampered_native_bytes_suffix_and_generated_insertion_fail(self):
        for raw in (self.raw.replace(b'Piece = native', b'Piece = changed'),
                    self.raw + b'; changed',
                    self.raw.replace(b'RotationRing = F800', b'RotationRing = FFFF')):
            with self.subTest(raw=raw[:70]), self.assertRaises(ValueError):
                with_feature_sequence(raw, self.metadata, [0xF800, 0xF801])

    def test_markers_must_be_complete_unique_and_exact(self):
        for old, new in ((ORDERING_BEGIN, '; unrelated begin'), (ORDERING_END, '; unrelated end'),
                         (ORDERING_BEGIN, ORDERING_BEGIN + '\r\n' + ORDERING_BEGIN)):
            changed, metadata = rewrite_insertion(self.raw, self.metadata,
                                                  self.metadata['ordering_insertion'].replace(old, new))
            with self.subTest(old=old, new=new), self.assertRaisesRegex(ValueError, 'markers'):
                with_feature_sequence(changed, metadata, [0xF800, 0xF801])
        suffix = self.metadata['suffix'].replace(MARKER, '\r\n; wrong suffix marker\r\n')
        changed = self.raw[:-len(self.metadata['suffix'])] + suffix.encode()
        with self.assertRaisesRegex(ValueError, 'markers'):
            with_feature_sequence(changed, dict(self.metadata, suffix=suffix), [0xF800, 0xF801])

    def test_preexisting_addtypes_or_malformed_generated_row_is_rejected(self):
        original = self.metadata['ordering_insertion']
        for replacement in ('AddTypes = F800', 'RotationRing = bad-state',
                            'RotationRing = F800, F800'):
            insertion = original.replace('RotationRing = F800', replacement, 1)
            changed, metadata = rewrite_insertion(self.raw, self.metadata, insertion)
            with self.subTest(replacement=replacement), self.assertRaises(ValueError):
                with_feature_sequence(changed, metadata, [0xF800, 0xF801])

    def test_generated_rows_cannot_share_states(self):
        insertion = self.metadata['ordering_insertion'].replace('7F801', '7F800')
        changed, metadata = rewrite_insertion(self.raw, self.metadata, insertion)
        with self.assertRaisesRegex(ValueError, 'rows overlap'):
            with_feature_sequence(changed, metadata, [0xF800, 0xF801])

    def test_collision_with_native_addtypes_is_rejected(self):
        native = NATIVE.replace(b'AddTypes = 101,', b'AddTypes = F800,')
        raw, metadata = compose_rul0(native, [fragment(0xF800), fragment(0xF801)])
        with self.assertRaisesRegex(ValueError, 'native rotation or type ring'):
            with_feature_sequence(raw, metadata, [0xF800, 0xF801])

    def test_every_selected_state_requires_one_saved_construction_definition(self):
        for old, new in (('[HighwayIntersectionInfo_0x0007F801]', '; missing state'),
                         ('CopyFrom = 0x0000F801\r\n',
                          '[HighwayIntersectionInfo_0x0007F801]\r\n')):
            suffix = self.metadata['suffix'].replace(old, new, 1)
            raw = self.raw[:-len(self.metadata['suffix'])] + suffix.encode()
            with self.subTest(old=old), self.assertRaisesRegex(ValueError, 'one construction definition'):
                with_feature_sequence(raw, dict(self.metadata, suffix=suffix), [0xF800, 0xF801])

    def test_insertion_cannot_be_moved_outside_ordering_even_with_matching_metadata(self):
        insertion = self.metadata['ordering_insertion'].encode()
        suffix = self.metadata['suffix'].encode()
        moved = self.raw[:-len(suffix)].replace(insertion, b'', 1) + insertion + suffix
        with self.assertRaisesRegex(ValueError, 'inside.*Ordering'):
            with_feature_sequence(moved, self.metadata, [0xF800, 0xF801])

    def test_repeated_opt_in_requires_original_build(self):
        actual, metadata = with_feature_sequence(self.raw, self.metadata, [0xF800, 0xF801])
        with self.assertRaisesRegex(ValueError, 'already has a feature sequence'):
            with_feature_sequence(actual, metadata, [0xF800, 0xF801])


if __name__ == '__main__':
    unittest.main()
