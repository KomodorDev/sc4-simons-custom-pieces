"""The highway's canonical roles preserve actual staged bytes and view order."""
import importlib.util
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    'compact_assembly_renderer', ROOT / 'domains/highway/tools/render_compact_assembly.py')
renderer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(renderer)


class CompactAssemblyRendererTests(unittest.TestCase):
    def test_canonical_roles_copy_exact_staged_bytes_in_readme_order(self):
        roles = (
            ('overview-top.png', 'top-clean-xy.png'),
            ('preview.png', 'southeast-clean-xy.png'),
            ('named-top.png', 'top-xy.png'),
            ('named-southeast.png', 'southeast-xy.png'),
            ('named-northwest.png', 'northwest-xy.png'),
            ('tile-ownership.png', 'placement-plan-xy.png'),
        )
        staged = []
        with TemporaryDirectory() as temporary:
            directory = Path(temporary)
            for number, (_canonical, suffix) in enumerate(reversed(roles)):
                raw = f'unchanged rendered bytes {number}'.encode('ascii')
                name = f'fixture-{suffix}'
                (directory / name).write_bytes(raw)
                staged.append({'file': name, 'sha256': renderer.sha(raw), 'size': [2800, 2600]})
            images, mapping = renderer.canonical_images({'images': staged}, directory, 'fixture')
            self.assertEqual([image['file'] for image in images], [role[0] for role in roles])
            for image, pair in zip(images, mapping):
                self.assertEqual((directory / image['file']).read_bytes(),
                                 (directory / image['staged_file']).read_bytes())
                self.assertEqual(pair, {'staged_file': image['staged_file'],
                                       'canonical_file': image['file'], 'sha256': image['sha256']})
            self.assertEqual([image['file'] for image in staged],
                             [f'fixture-{suffix}' for _canonical, suffix in reversed(roles)])

    def test_changed_staged_bytes_cannot_be_relabelled_with_an_old_hash(self):
        with TemporaryDirectory() as temporary:
            directory = Path(temporary)
            name = 'fixture-top-clean-xy.png'
            (directory / name).write_bytes(b'changed bytes')
            report = {'images': [{'file': name, 'sha256': renderer.sha(b'old bytes')}]}
            with self.assertRaisesRegex(ValueError, 'changed the rendered bytes'):
                renderer.canonical_images(report, directory, 'fixture')


if __name__ == '__main__':
    unittest.main()
