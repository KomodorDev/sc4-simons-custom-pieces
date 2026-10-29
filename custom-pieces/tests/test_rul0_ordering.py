"""Verify section-aware rotation composition without generating track geometry.

Literal miniature controllers reproduce the original append-only defect and
exercise preservation of native syntax, comments, states and line endings.
No test reads or changes an installed Plugins directory.
"""
from __future__ import annotations

import hashlib
from pathlib import Path
import re
import sys
import unittest

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp.rul0 import compose_rul0, split_rule_delta
from scp.verify import RUL0, check_construction, check_rotation_ordering


# These are literal expected game states, independent of the controller writer.
STATES = [0xF800, 0x1F800, 0x2F800, 0x3F800,
          0x4F800, 0x5F800, 0x6F800, 0x7F800]
RING = 'RotationRing = F800, 1F800, 2F800, 3F800, 4F800, 5F800, 6F800, 7F800'
DEFINITIONS = ('[HighwayIntersectionInfo_0x0000F800]\r\n'
               'Piece = 0,0,0,0,0x7F500FF5\r\n'
               '[HighwayIntersectionInfo_0x0001F800]\r\n'
               'CopyFrom = 0x0000F800\r\nRotate = 1\r\n')
DELTA = RING + '\r\n' + DEFINITIONS
NATIVE = (b'; native comments and spacing must survive\r\n'
          b'; [Ordering]\r\n'
          b'[Ordering]\r\n'
          b'RotationRing = 0100, 10100, 20100, 30100 ; native ring\r\n'
          b'AddTypes = 0100\r\n'
          b'\r\n[Intersection Tile Types]\r\n'
          b'DefineType = 0x00000000,Road\r\n'
          b'[HighwayIntersectionInfo_0x00000100]\r\n'
          b'CopyFrom = 0x0103\r\n')


def saved_ring_scopes(raw):
    """Small test-owned scanner records actual section scope and raw ring text."""
    section, result = None, []
    for raw_line in raw.splitlines():
        line = raw_line.split(b';', 1)[0].strip()
        if line.startswith(b'[') and line.endswith(b']'):
            section = line[1:-1].strip().lower()
        elif re.match(rb'(?i)^rotationring\s*=', line):
            result.append((section, line))
    return result


class RotationOrderingCompositionTests(unittest.TestCase):
    def test_composer_places_custom_ring_in_existing_ordering_and_definitions_at_end(self):
        actual, metadata = compose_rul0(NATIVE, [DELTA])
        scopes = saved_ring_scopes(actual)
        self.assertEqual([section for section, _ in scopes], [b'ordering', b'ordering'])
        self.assertEqual(scopes[0][1], b'RotationRing = 0100, 10100, 20100, 30100')
        self.assertEqual(scopes[1][1], RING.encode('ascii'))
        self.assertTrue(actual.endswith(DEFINITIONS.encode('ascii')))
        self.assertNotIn('RotationRing', metadata['suffix'])
        report = check_rotation_ordering(actual, [STATES])
        self.assertEqual(report, {'ordering_sections_checked': 1,
                                 'custom_rotation_rings_in_ordering': 1,
                                 'native_rotation_rings_preserved': 1})

    def test_removing_both_additions_restores_every_native_byte(self):
        for newline in (b'\r\n', b'\n'):
            native = NATIVE.replace(b'\r\n', newline)
            for terminated in (True, False):
                original = native if terminated else native.rstrip(b'\r\n')
                with self.subTest(newline=newline, terminated=terminated):
                    actual, metadata = compose_rul0(original, [DELTA])
                    suffix = metadata['suffix'].encode('ascii')
                    insertion = metadata['ordering_insertion'].encode('ascii')
                    self.assertTrue(actual.endswith(suffix))
                    body = actual[:-len(suffix)]
                    self.assertEqual(body.count(insertion), 1)
                    self.assertEqual(body.replace(insertion, b'', 1), original)
                    self.assertEqual(metadata['base_sha256'], hashlib.sha256(original).hexdigest())
                    # Preserve the native line-ending convention in its insertion.
                    self.assertEqual(insertion.count(b'\r\n') > 0, newline == b'\r\n')

    def test_ordering_at_end_without_final_newline_gets_a_separate_property_line(self):
        actual, metadata = compose_rul0(b'; header\n[Ordering]', [DELTA])
        self.assertIn(b'[Ordering]\n;BEGIN', actual)
        self.assertEqual(check_rotation_ordering(actual, [STATES])['custom_rotation_rings_in_ordering'], 1)
        self.assertTrue(metadata['ordering_insertion'].startswith('\n'))

    def test_commented_headers_do_not_hide_missing_ordering(self):
        for native in (b'; [Ordering]\n[Other]\n', b'[Other]\n; [Ordering]\n'):
            with self.subTest(native=native), self.assertRaisesRegex(ValueError, 'exactly one.*Ordering'):
                compose_rul0(native, [DELTA])

    def test_duplicate_active_ordering_headers_are_rejected(self):
        for header in (b'[Ordering]\r\n', b'  [oRdErInG] ; second active section\r\n'):
            with self.subTest(header=header), self.assertRaisesRegex(ValueError, 'exactly one.*Ordering'):
                compose_rul0(NATIVE + header, [DELTA])

    def test_active_header_case_whitespace_and_inline_comments_are_preserved(self):
        native = NATIVE.replace(b'[Ordering]\r\n', b'  [ oRdErInG ] ; active\r\n')
        actual, metadata = compose_rul0(native, [DELTA])
        self.assertIn(b'  [ oRdErInG ] ; active\r\n', actual)
        self.assertEqual(check_rotation_ordering(actual, [STATES])['ordering_sections_checked'], 1)
        self.assertEqual(actual[:-len(metadata['suffix'])].replace(
            metadata['ordering_insertion'].encode('ascii'), b'', 1), native)

    def test_native_ring_lengths_including_121_are_not_restricted_to_eight(self):
        for length in (2, 4, 6, 9, 12, 16, 32, 121):
            values = ', '.join(f'{0x200000 + i:X}' for i in range(length))
            native = ('[Ordering]\nRotationRing = ' + values + '\n[Other]\n').encode('ascii')
            with self.subTest(length=length):
                actual, _ = compose_rul0(native, [DELTA])
                report = check_rotation_ordering(actual, [STATES])
                self.assertEqual(report['native_rotation_rings_preserved'], 1)

    def test_custom_state_cannot_already_belong_to_native_ring(self):
        native = NATIVE.replace(b'0100, 10100, 20100, 30100', b'0100, F800')
        with self.assertRaisesRegex(ValueError, 'already belongs to NAM'):
            compose_rul0(native, [DELTA])

    def test_selected_pieces_cannot_share_any_rotation_state(self):
        # A second piece with an otherwise distinct ring shares just one state.
        second = DELTA.replace('F800', 'F801').replace('7F801', '7F800')
        with self.assertRaisesRegex(ValueError, 'states overlap'):
            compose_rul0(NATIVE, [DELTA, second])

    def test_selected_piece_must_have_exactly_eight_distinct_states(self):
        for ring in (RING.rsplit(',', 1)[0], RING + ', 8F800',
                     RING.replace('7F800', '6F800')):
            with self.subTest(ring=ring), self.assertRaisesRegex(ValueError, 'eight unique states'):
                compose_rul0(NATIVE, [ring + '\r\n' + DEFINITIONS])

    def test_malformed_or_duplicate_rotation_properties_are_rejected(self):
        for ring in (RING.replace('F800,', 'not-hex,', 1),
                     RING.replace('F800,', '0x100000000,', 1), RING + ',',
                     RING.replace('RotationRing =', 'RotationRing'),
                     RING + '\r\n' + RING):
            with self.subTest(ring=ring), self.assertRaises(ValueError):
                compose_rul0(NATIVE, [ring + '\r\n' + DEFINITIONS])

    def test_fragment_cannot_inject_ordering_or_modify_native_tab_ring(self):
        for injection in ('[Ordering]\r\n', '[ oRdErInG ] ; injected\r\n',
                          'AddTypes = F800\r\n', 'addtypes = F800\r\n'):
            with self.subTest(injection=injection), self.assertRaisesRegex(ValueError, 'Ordering|native type ring'):
                compose_rul0(NATIVE, [DELTA + injection])

    def test_split_delta_preserves_definition_text_and_ignores_comment_decoys(self):
        definitions = '; RotationRing = DECAFBAD\r\n' + DEFINITIONS + '; [Ordering]\r\n'
        ring, actual = split_rule_delta(RING + ' ; selected states\r\n' + definitions)
        self.assertEqual(ring, RING + ' ; selected states')
        self.assertEqual(actual, definitions)

    def test_composition_refuses_a_baseline_already_containing_scp_additions(self):
        actual, _ = compose_rul0(NATIVE, [DELTA])
        with self.assertRaisesRegex(ValueError, 'already contains generated SCP'):
            compose_rul0(actual, [DELTA])


class SavedControllerRotationScopeTests(unittest.TestCase):
    def test_append_only_original_bug_fails_even_when_all_eight_states_exist(self):
        broken = NATIVE + b'\r\n; generated delta\r\n' + DELTA.encode('ascii')
        self.assertIn(RING.encode('ascii'), broken)
        with self.assertRaisesRegex(ValueError, 'outside.*Ordering'):
            check_rotation_ordering(broken, [STATES])

    def test_ring_before_any_header_and_under_puzzle_header_are_rejected(self):
        for raw in (RING.encode('ascii') + b'\r\n' + NATIVE,
                    NATIVE + b'\r\n' + RING.encode('ascii')):
            with self.subTest(raw=raw[-100:]), self.assertRaisesRegex(ValueError, 'outside.*Ordering'):
                check_rotation_ordering(raw, [STATES])

    def test_comment_decoys_cannot_count_as_real_custom_ring_or_ordering(self):
        for raw in (NATIVE + b'; ' + RING.encode('ascii') + b'\r\n',
                    b'; [Ordering]\n' + RING.encode('ascii') + b'\n'):
            with self.subTest(raw=raw[-100:]), self.assertRaisesRegex(ValueError, 'selected pieces|outside.*Ordering'):
                check_rotation_ordering(raw, [STATES])

    def test_saved_duplicate_ring_duplicate_state_or_native_overlap_is_rejected(self):
        actual, metadata = compose_rul0(NATIVE, [DELTA])
        for injection in (RING, 'RotationRing = F801, F801', 'RotationRing = 0100, 123456'):
            changed = actual.replace(metadata['ordering_insertion'].encode('ascii'),
                                     metadata['ordering_insertion'].encode('ascii') +
                                     injection.encode('ascii') + b'\r\n')
            with self.subTest(injection=injection), self.assertRaisesRegex(ValueError, 'more than one|repeated'):
                check_rotation_ordering(changed, [STATES])

    def test_saved_ring_must_match_selected_state_membership_and_order(self):
        actual, _ = compose_rul0(NATIVE, [DELTA])
        for replacement in (RING.rsplit(',', 1)[0], RING.replace('7F800', '8F800'),
                            RING.replace('F800, 1F800', '1F800, F800', 1)):
            changed = actual.replace(RING.encode('ascii'), replacement.encode('ascii'))
            with self.subTest(replacement=replacement), self.assertRaisesRegex(ValueError, 'selected pieces'):
                check_rotation_ordering(changed, [STATES])

    def test_saved_duplicate_active_ordering_is_rejected(self):
        actual, _ = compose_rul0(NATIVE, [DELTA])
        with self.assertRaisesRegex(ValueError, 'exactly one active.*Ordering'):
            check_rotation_ordering(actual + b'\r\n[Ordering]\r\n', [STATES])

    def test_saved_malformed_rotation_identifiers_are_rejected(self):
        actual, _ = compose_rul0(NATIVE, [DELTA])
        for replacement in (RING.replace('7F800', 'xyz'), RING + ',',
                            RING.replace('RotationRing =', 'RotationRing :')):
            changed = actual.replace(RING.encode('ascii'), replacement.encode('ascii'))
            with self.subTest(replacement=replacement), self.assertRaisesRegex(ValueError, 'Malformed RotationRing'):
                check_rotation_ordering(changed, [STATES])

    def test_rehashed_manifest_cannot_legitimize_moving_insertion_under_puzzle(self):
        actual, metadata = compose_rul0(NATIVE, [DELTA])
        insertion = metadata['ordering_insertion'].encode('ascii')
        suffix = metadata['suffix'].encode('ascii')
        # Move the exact declared insertion after native puzzle definitions.
        # Native restoration and the matching resource digest still succeed.
        broken = actual[:-len(suffix)].replace(insertion, b'', 1) + insertion + suffix
        self.assertEqual(broken[:-len(suffix)].replace(insertion, b'', 1), NATIVE)
        rehashed_manifest = {'overlay': {'rul0': metadata},
                             'files': [{'sha256': hashlib.sha256(broken).hexdigest(),
                                        'bytes': len(broken)}]}
        # Supply all eight section identifiers so section-scope validation,
        # rather than missing puzzle definitions, rejects this portable input.
        missing_clones = ''.join(f'[HighwayIntersectionInfo_0x{state:08X}]\r\n'
                                 for state in STATES[2:]).encode('ascii')
        broken += missing_clones
        rehashed_manifest['overlay']['rul0'] = dict(metadata, suffix=(suffix + missing_clones).decode('ascii'))
        rehashed_manifest['files'][0].update(sha256=hashlib.sha256(broken).hexdigest(), bytes=len(broken))
        with self.assertRaisesRegex(ValueError, 'outside.*Ordering'):
            check_construction({RUL0: broken}, [{'puzzle_id': 'F800'}], rehashed_manifest, {})

    def test_old_metadata_without_an_ordering_insertion_requires_rebuild(self):
        suffix = '\r\n; old generated fragment\r\n' + DELTA
        broken = NATIVE + suffix.encode('ascii')
        manifest = {'overlay': {'rul0': {'base_sha256': hashlib.sha256(NATIVE).hexdigest(),
                                         'suffix': suffix}}}
        with self.assertRaisesRegex(ValueError, 'missing.*Ordering.*rebuild'):
            check_construction({RUL0: broken}, [{'puzzle_id': 'F800'}], manifest, {})


if __name__ == '__main__':
    unittest.main()
