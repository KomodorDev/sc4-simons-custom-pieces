"""Check saved SCP navigation and preservation of unrelated native menus."""
from pathlib import Path
import sys
import unittest

ROOT = next(path for path in Path(__file__).resolve().parents if (path / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))

from scp import transport_menu
from scp.catalog import load_catalog
from scp.dbpf import encode_exemplar, exemplar, pack_dbpf
from scp.menu import ICON, MENU_EXEMPLAR, TITLE
from scp.menu_experiment import _assembly_readme, _guide
from scp.menu_experiment_resources import ITEM_BUTTON_CLASS, ITEM_SUBMENU_PARENT_ID, _props, _set
from scp.verify import read_ltext, strict_dbpf
from test_menu_experiment import menu_resource


class TransportMenuTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = load_catalog(ROOT)
        cls.piece, cls.assembly, cls.rail = 0x6A47F901, 0x6A47FEE0, 0x6A47F902
        cls.source = {}
        for iid in (cls.piece, cls.assembly, cls.rail):
            base = menu_resource({'id': str(iid), 'name': str(iid), 'description': 'A fixture button.',
                                  'menu': {'id': f'{iid:08x}', 'order': 'ffffff00'}})
            key = (*MENU_EXEMPLAR, iid)
            record = exemplar(base[key])
            if iid != cls.rail:
                prop = _props(record)[0x4001]
                prop.update(id='0x00004005', values=[0])
            if iid == cls.assembly:
                _set(record, 0x8A2602BB, [cls.piece])
            base[key] = encode_exemplar(record)
            cls.source.update(base)
        cls.roster = {'highway': {'pieces': [cls.piece], 'assemblies': [cls.assembly]}}

    def test_saved_hierarchy_has_only_folders_at_native_and_scp_levels(self):
        output = strict_dbpf(pack_dbpf(transport_menu.arrange(self.source, self.roster)))
        root, pieces, assemblies = transport_menu.HIGHWAY
        expected = [(root, 0x31, 1, 'SCP'), (pieces, root, 1, 'Pieces'),
                    (assemblies, root, 1, 'Assemblies'), (self.piece, pieces, 2, None),
                    (self.assembly, assemblies, 2, None)]
        for iid, parent, kind, title in expected:
            props = _props(exemplar(output[*MENU_EXEMPLAR, iid]))
            self.assertEqual(props[ITEM_SUBMENU_PARENT_ID]['values'], [parent])
            self.assertEqual(props[ITEM_BUTTON_CLASS]['values'], [kind])
            if title:
                self.assertEqual(read_ltext(output[*TITLE, iid]), title)
        self.assertEqual(_props(exemplar(output[*MENU_EXEMPLAR, self.assembly]))[0x8A2602BB]['values'],
                         [self.piece])
        self.assertEqual({key: raw for key, raw in output.items() if key[2] == self.rail},
                         {key: raw for key, raw in self.source.items() if key[2] == self.rail})
        self.assertEqual(transport_menu.restore(output, self.roster), self.source)

    def test_saved_hierarchy_rejects_wrong_leaf_parent_or_navigation_icon(self):
        output = transport_menu.arrange(self.source, self.roster)
        key = (*MENU_EXEMPLAR, self.assembly)
        record = exemplar(output[key])
        _set(record, ITEM_SUBMENU_PARENT_ID, [transport_menu.HIGHWAY[1]])
        with self.assertRaisesRegex(ValueError, 'parent'):
            transport_menu.restore({**output, key: encode_exemplar(record)}, self.roster)
        root, pieces, _ = transport_menu.HIGHWAY
        with self.assertRaisesRegex(ValueError, 'icon'):
            transport_menu.restore({**output, (*ICON, root): output[*ICON, pieces]}, self.roster)
        with self.assertRaisesRegex(ValueError, 'Unlisted'):
            transport_menu.arrange(self.source, {'highway': {'pieces': [self.piece], 'assemblies': []}})

    def test_first_folder_order_preserves_archived_and_sibling_order(self):
        root, pieces, assemblies = transport_menu.HIGHWAY
        legacy = transport_menu.arrange(self.source, self.roster, version=1)
        current = transport_menu.arrange(self.source, self.roster)
        root_key = (*MENU_EXEMPLAR, root)
        self.assertEqual({key for key in current if current[key] != legacy[key]}, {root_key})

        def signed_order(menu, iid):
            [order] = _props(exemplar(menu[*MENU_EXEMPLAR, iid]))[0x8A2602B9]['values']
            return int.from_bytes(order.to_bytes(4, 'little'), 'little', signed=True)

        self.assertEqual(signed_order(legacy, root), -12)
        self.assertLess(signed_order(current, root), -255)  # Earliest audited NAM 50 Highway entry.
        self.assertLess(signed_order(current, pieces), signed_order(current, assemblies))
        self.assertEqual(transport_menu.restore(legacy, self.roster, version=1), self.source)
        with self.assertRaisesRegex(ValueError, 'order'):
            transport_menu.restore(legacy, self.roster)

    def test_both_domains_keep_independent_folder_chains_and_restore_originals(self):
        rail_assembly = 0x6A47FEF0
        rail_definition = {'id': 'fixture-rail-assembly', 'name': 'Rail assembly', 'description': 'Rail assembly.',
                           'menu': {'id': f'{rail_assembly:08x}', 'order': '7010fef0'}}
        source = {**self.source, **menu_resource(rail_definition)}
        for iid in (self.rail, rail_assembly):
            key = (*MENU_EXEMPLAR, iid)
            record = exemplar(source[key])
            _set(record, 0x4001, [0])
            if iid == rail_assembly:
                _set(record, 0x8A2602BB, [self.rail])
            source[key] = encode_exemplar(record)
        roster = {**self.roster, 'high-speed-rail': {'pieces': [self.rail], 'assemblies': [rail_assembly]}}
        output = strict_dbpf(pack_dbpf(transport_menu.arrange(source, roster)))
        root, pieces, assemblies = transport_menu.RAIL
        for iid, parent, kind, title in ((root, 0x29, 1, 'SCP'), (pieces, root, 1, 'Pieces'),
                                         (assemblies, root, 1, 'Assemblies'), (self.rail, pieces, 2, None),
                                         (rail_assembly, assemblies, 2, None)):
            props = _props(exemplar(output[*MENU_EXEMPLAR, iid]))
            self.assertEqual(props[ITEM_SUBMENU_PARENT_ID]['values'], [parent])
            self.assertEqual(props[ITEM_BUTTON_CLASS]['values'], [kind])
            self.assertEqual(props[0x4001]['values'], [0])
            self.assertNotIn(0x4005, props)
            if title:
                self.assertEqual(read_ltext(output[*TITLE, iid]), title)
        order = _props(exemplar(output[*MENU_EXEMPLAR, root]))[0x8A2602B9]['values'][0]
        self.assertLess(order - 0x100000000, -1717986919)  # Earliest measured NAM 50 Rail order.
        self.assertEqual(_props(exemplar(output[*MENU_EXEMPLAR, rail_assembly]))[0x8A2602BB]['values'], [self.rail])
        highway = transport_menu.arrange(self.source, self.roster)
        self.assertEqual({key: output[key] for key in highway if key[2] != self.rail},
                         {key: raw for key, raw in highway.items() if key[2] != self.rail})
        self.assertEqual(transport_menu.restore(output, roster), source)

    def test_rail_normal_build_keeps_empty_assemblies_leaf_and_unrelated_highway_entries(self):
        roster = {'high-speed-rail': {'pieces': [self.rail], 'assemblies': []}}
        output = transport_menu.arrange(self.source, roster)
        self.assertTrue(transport_menu.folder_keys(roster) <= output.keys())
        self.assertEqual({key: output[key] for key in self.source if key[2] != self.rail},
                         {key: raw for key, raw in self.source.items() if key[2] != self.rail})
        self.assertEqual(transport_menu.restore(output, roster), self.source)

    def test_rail_single_button_guide_uses_the_nested_path_only_when_declared(self):
        layout = {'assembly_id': 'fixture-assembly', 'cycle_button': {'title': 'Rail Assembly'}}
        members = [{'id': 'rail-piece', 'name': 'Rail Piece', 'domain': 'high-speed-rail'}]
        self.assertIn('Transportation → Rail → SCP → Assemblies', _guide(layout, members, nested=True).decode())
        self.assertIn('Open **Transportation → Rail**', _guide(layout, members).decode())
        self.assertIn(b'Transportation > Rail > SCP > Assemblies', _assembly_readme(layout, members, nested=True))
        self.assertNotIn(b'SCP > Assemblies', _assembly_readme(layout, members))

    def test_actual_catalog_enables_both_domains_and_reserves_disjoint_menu_folders(self):
        from scp import jsonc

        layouts = [layout for domain in ('high-speed-rail', 'highway')
                   for layout in jsonc.load(ROOT / f'domains/{domain}/menu-layout.jsonc')['layouts'].values()]
        self.assertFalse(any('cycle_submenu' in layout for layout in layouts))
        self.assertEqual(transport_menu.plan(self.catalog, self.catalog['pieces']),
                         {'schema_version': 2, 'domains': ['high-speed-rail', 'highway']})
        folders = set(transport_menu.HIGHWAY + transport_menu.RAIL)
        self.assertEqual(len(folders), 6)
        self.assertTrue(folders.isdisjoint(int(piece['menu']['id'], 16) for piece in self.catalog['pieces']))
        self.assertTrue(folders.isdisjoint(int(layout['cycle_button']['id'], 16) for layout in layouts))
