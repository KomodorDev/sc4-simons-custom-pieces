"""Keep presentation qualifiers separate from accepted canonical assembly names."""
from pathlib import Path
import sys
import unittest

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp.assembly_presentation import canonical_cycle_title, validate_cycle_title
from scp.menu_experiment import _layout


class AssemblyPresentationTests(unittest.TestCase):
    def setUp(self):
        self.scene = {'title': 'DD RHW-4 — Parallel Diagonal Avenue Diamond'}
        self.button = {'id': '6a47fee2', 'order': 'fffffee2',
                       'title': 'SCP | ASSEMBLY | ' + self.scene['title'],
                       'description': 'Select reusable components.'}
        self.layout = {'assembly_id': 'fixture-diamond', 'member_order': 'first-use-in-assembly',
                       'cycle_button': self.button}

    def test_no_qualifier_keeps_exact_existing_title(self):
        before = self.scene.copy()
        self.assertEqual(canonical_cycle_title(self.scene['title']), self.button['title'])
        self.assertEqual(validate_cycle_title(self.scene, self.button), self.button['title'])
        self.assertEqual(self.scene, before)
        self.assertEqual(_layout(self.layout, 'highway'), self.layout)

    def test_explicit_label_appends_exactly_one_suffix_without_mutating_scene(self):
        before = self.scene.copy()
        button = {**self.button, 'variant_label': 'Alignment A',
                  'title': self.button['title'] + ' — Alignment A'}
        self.assertEqual(validate_cycle_title(self.scene, button), button['title'])
        self.assertEqual(canonical_cycle_title(self.scene['title'], variant_label='Alignment A'), button['title'])
        self.assertEqual(_layout({**self.layout, 'cycle_button': button}, 'highway')['cycle_button'], button)
        self.assertEqual(self.scene, before)

    def test_declared_label_does_not_allow_wrong_canonical_name_omitted_suffix_or_repeated_suffix(self):
        for title in ('SCP | ASSEMBLY | Different assembly — Alignment A',
                      self.button['title'], self.button['title'] + ' — Alignment A — Alignment A'):
            with self.subTest(title=title):
                with self.assertRaisesRegex(ValueError, 'canonical scene title'):
                    validate_cycle_title(self.scene, {**self.button, 'variant_label': 'Alignment A', 'title': title})
        with self.assertRaisesRegex(ValueError, 'duplicates'):
            canonical_cycle_title(self.scene['title'] + ' — Alignment B', variant_label='Alignment B')

    def test_invalid_labels_and_submenu_qualifier_are_rejected(self):
        for label in (None, False, 1, '', ' Alignment A', 'Alignment A ',
                      'Alignment  A', 'Alignment\nA', 'Alignment\tA', 'A|B', 'A — B', 'A' * 65):
            with self.subTest(label=label):
                button = {**self.button, 'variant_label': label}
                with self.assertRaisesRegex(ValueError, 'variant_label'):
                    _layout({**self.layout, 'cycle_button': button}, 'highway')
                with self.assertRaisesRegex(ValueError, 'variant_label'):
                    validate_cycle_title(self.scene, button)
        with self.assertRaisesRegex(ValueError, 'Menu presentation'):
            _layout({**self.layout, 'cycle_submenu': {**self.button, 'id': '6a47fee4',
                                                    'variant_label': 'Alignment A'}}, 'highway')


if __name__ == '__main__':
    unittest.main()
