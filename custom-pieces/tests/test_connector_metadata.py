"""Source-owned declarations, measured boundaries, and consumer exports agree."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scp import jsonc
from scp.connector_metadata import (ConnectorDataError, build_exports, load_exports, load_library,
    resolve_profiles, validate_piece, validate_structure, _schema, write_exports)
from scp.export import public_files

ROOT = Path(__file__).resolve().parents[1]
DOMAIN = ROOT/'domains/high-speed-rail'
IDS = ['hsr-component-modular-crossing-core', 'hsr-component-tight-paired-curve90-l4-to-mid']
BUILD = ROOT/'dist/straight-stem-trumpet'


def bound_source_names(values):
    names = set().union(*(set(value['source_binding']['files']) for value in values.values()))
    names.update(value['source_binding']['compiled_build']+'/manifest.json' for value in values.values())
    return names


class ConnectorSourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = load_library(ROOT, IDS)
        cls.profiles = resolve_profiles(jsonc.load(DOMAIN/'connector-profiles.json'))

    def validate(self, mutate):
        piece = deepcopy(self.report['pieces'][IDS[0]])
        mutate(piece)
        return validate_piece(piece['piece'], piece['connections'], piece['metadata'], self.profiles)

    def test_schema_rejects_extra_fields_missing_purpose_and_invalid_ids(self):
        for mutate in (lambda p:p['metadata'].update(extra=True),
                       lambda p:p['metadata'].pop('purpose'),
                       lambda p:p['metadata']['groups'][0]['members'][0].update(id='Upper End A')):
            with self.subTest(mutate=mutate), self.assertRaises(ValueError):
                self.validate(mutate)

    def test_duplicate_keys_rejected_even_after_comments(self):
        with self.assertRaisesRegex(ValueError, 'Duplicate JSON key'):
            jsonc.loads('{"direction":"in", // hidden override\n "direction":"out"}')
        self.assertEqual(jsonc.loads('{"url":"https://example.test/a/*b*/"}'), {'url':'https://example.test/a/*b*/'})

    def test_forbidden_and_permitted_journeys_cannot_conflict(self):
        def mutate(p):
            j=p['connections']['journeys'][0]
            p['connections']['forbidden_transfers'].append({'from_port':j['entry_port'],'to_port':j['exit_port']})
        with self.assertRaisesRegex(ValueError, 'contradictory'):
            self.validate(mutate)

    def test_channel_coverage_and_member_permissions_are_checked(self):
        for mutate in (
            lambda p:p['metadata']['groups'][0]['members'][0].update(channel_id='missing-channel'),
            lambda p:p['metadata']['groups'][0]['members'][0].update(traffic_modes=['car']),
            lambda p:p['metadata']['channels'].append({'id':'unused-channel','kind':'rail','traffic_modes':['monorail']})):
            with self.subTest(mutate=mutate), self.assertRaises(ValueError):
                self.validate(mutate)

    def test_profiles_are_optional_not_required_physical_geometry(self):
        result=self.validate(lambda p:[g.pop('profile_id') for g in p['metadata']['groups']])
        self.assertEqual(len(result['groups']),4)
        for g in result['groups']:
            self.assertNotIn('expected_deck_width_m',g['profile'])
            self.assertEqual(g['profile']['path_height_m'],g['members'][0]['endpoint_m'][2])

    def test_unexpected_schema_rules_fail_explicitly(self):
        with self.assertRaisesRegex(ValueError,'unsupported schema keyword'):
            validate_structure('anything', {'type':'string','maxLength':2})

    def test_native_path_11_absence_is_preserved_and_invalid_compatibility_types_rejected(self):
        from scp.verify import parse_paths
        route = parse_paths(b'SC4PATHS\n1.1\n1\n0\n0\n7\n1\n2\n0\n2\n2,-8,15.5\n2,8,15.5\n')['routes'][0]
        self.assertIsNone(route['compatibility'])
        value = {**route, 'id': 'native-11', 'cell': [0, 0], 'tile_id': '12340000',
                 'engine_transport': route['transport'], 'entry_edge': route['entry'], 'exit_edge': route['exit']}
        value = json.loads(json.dumps(value))
        schema = _schema('connector-data.schema.json')['properties']['routes']['items']
        validate_structure(value, schema)
        for compatibility in (0, 1):
            validate_structure({**value, 'compatibility': compatibility}, schema)
        for compatibility in ('0', True, 1.5, [], {}):
            with self.subTest(compatibility=compatibility), self.assertRaises(ValueError):
                validate_structure({**value, 'compatibility': compatibility}, schema)

    def test_channels_follow_real_journeys_not_member_number_suffixes(self):
        for piece in self.report['pieces'].values():
            members={m['id']:m for g in piece['groups'] for m in g['members']}
            for journey in piece['journeys']:
                first,last=members[journey['entry_port']],members[journey['exit_port']]
                self.assertEqual(first['channel_id'],last['channel_id'])
                self.assertNotEqual(first['id'].rsplit('-',1)[-1],last['id'].rsplit('-',1)[-1])

    def test_resolved_facts_exclude_legacy_neighbour_shortlists_without_mutating_sources(self):
        original = deepcopy(self.report['pieces'][IDS[0]])
        connections = original['connections']
        legacy = {
            'compatible_counterparts': [{'piece_id': 'unrelated-legacy-neighbour'}],
            'transposed_compatible_counterparts': [],
            'candidate_counterpart_count': 999,
            'counterpart_list_scope': 'Old endpoint shortlist',
        }
        for port in connections['ports']:
            port.update(deepcopy(legacy))
        before = deepcopy(connections)
        resolved = validate_piece(original['piece'], connections, original['metadata'], self.profiles)
        self.assertEqual(connections, before)
        for port in resolved['connections']['ports'] + [member for group in resolved['groups'] for member in group['members']]:
            self.assertFalse(set(legacy).intersection(port))
        self.assertEqual(resolved['journeys'], original['journeys'])

    def test_source_exports_include_contract_reader_schemas_and_jsoncs(self):
        names={relative.as_posix() for relative,_ in public_files(ROOT)}
        for name in ['docs/CONNECTOR_METADATA.md','docs/WORKFLOW_DOCUMENTATION_GENERATION.md','framework/scp/jsonc.py',
                     'framework/scp/connector_metadata.py','schemas/connector-groups.schema.json',
                     'schemas/connector-data.schema.json','schemas/connector-profiles.schema.json']:
            self.assertIn(name,names)
        from scp.catalog import load_catalog
        expected = {
            f'domains/{piece["domain"]}/00_pieces/{piece["id"]}/connector-groups.jsonc'
            for piece in load_catalog(ROOT)['pieces']
            if (ROOT/f'domains/{piece["domain"]}/00_pieces/{piece["id"]}/connector-groups.jsonc').is_file()
        }
        self.assertEqual({name for name in names if name.endswith('/connector-groups.jsonc')}, expected)
        self.assertTrue({f'domains/high-speed-rail/00_pieces/{identifier}/connector-groups.jsonc' for identifier in IDS} <= expected)


@unittest.skipUnless((BUILD/'manifest.json').is_file(), 'Needs the saved, protected two-piece build')
class ConnectorExportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.values=build_exports(ROOT,IDS,BUILD)

    def test_export_is_repeatable_and_read_only(self):
        selected=[DOMAIN/'00_pieces'/slug/name for slug in IDS for name in ('piece.json','connections.json','connector-groups.jsonc','checks/manual-tests.json')]
        before={p:hashlib.sha256(p.read_bytes()).hexdigest() for p in selected}
        self.assertEqual(self.values,build_exports(ROOT,IDS,BUILD))
        self.assertEqual(before,{p:hashlib.sha256(p.read_bytes()).hexdigest() for p in selected})

    def test_full_curve_geometry_retains_interior_heights(self):
        value=self.values[IDS[1]]
        self.assertEqual(len(value['routes']),14)
        self.assertGreater(sum(len(r['points']) for r in value['routes']),1000)
        heights=[p[2] for r in value['routes'] for p in r['points']]
        self.assertEqual((min(heights),max(heights)),(23.,30.5))
        self.assertTrue(any(24<h<30 for h in heights))
        self.assertEqual(set(value['endpoint_route_refs']),{m['id'] for g in value['resolved_piece']['groups'] for m in g['members']})
        low=next(g for g in value['resolved_piece']['groups'] if g['id']=='curve-end-b')
        self.assertIsNone(low['profile']['nominal_level'])
        self.assertTrue(all(m['grade_outward']==0 for g in value['resolved_piece']['groups'] for m in g['members']))

    def test_consumer_rejects_changed_sources_and_changed_export_geometry(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary)
            names=bound_source_names(self.values)
            for name in names:
                target=root/name;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes((ROOT/name).read_bytes())
            write_exports(root,self.values)
            report=load_exports(root,IDS)
            self.assertEqual(report['counts']['ports'],12)
            path=root/'domains/high-speed-rail/00_pieces'/IDS[1]/'connector-data.json'
            bad=json.loads(path.read_text());bad['routes'][0]['points'][0][2]+=1
            path.write_text(json.dumps(bad))
            with self.assertRaisesRegex(ValueError,'content fingerprint'):
                load_exports(root,IDS)
            write_exports(root,self.values)
            source=root/'domains/high-speed-rail/connector-profiles.json'
            source.write_text(source.read_text()+'\n')
            with self.assertRaisesRegex(ValueError,'stale exported source'):
                load_exports(root,IDS)

    def test_consumer_rejects_removed_bindings_and_invalid_route_references(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary)
            names=bound_source_names(self.values)
            for name in names:
                target=root/name;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes((ROOT/name).read_bytes())
            for defect in ('bindings','references','duplicates'):
                values=deepcopy(self.values)
                value=values[IDS[0]]
                if defect=='bindings':
                    name=next(name for name in value['source_binding']['files'] if name.endswith('/piece.json'))
                    value['source_binding']['files']={name:value['source_binding']['files'][name]}
                elif defect=='references':
                    member=next(iter(value['endpoint_route_refs']))
                    value['endpoint_route_refs'][member]=['nonexistent-route']
                else:
                    value['routes'].append(deepcopy(value['routes'][0]))
                from scp.connector_metadata import _canonical, _sha
                value['content_sha256']=_sha(_canonical({k:v for k,v in value.items() if k!='content_sha256'}))
                write_exports(root,values)
                with self.subTest(defect=defect), self.assertRaises(ValueError):
                    load_exports(root,IDS)
            # Reviewed contract helpers are inputs even when the adapter is unchanged.
            write_exports(root,self.values)
            helper=next(name for name in names if name.endswith('/hsr_components_verify.py'))
            (root/helper).write_text((root/helper).read_text()+'\n')
            with self.assertRaisesRegex(ValueError,'stale exported source'):
                load_exports(root,IDS)

    def test_published_schemas_check_actual_exports(self):
        for value in self.values.values():
            validate_structure(value,_schema('connector-data.schema.json'))

    def test_documentation_handoff_keeps_export_fresh_but_compiled_manifest_mutations_fail(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for name in bound_source_names(self.values):
                target = root/name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes((ROOT/name).read_bytes())
            write_exports(root, self.values)
            manifest_path = root/self.values[IDS[0]]['source_binding']['compiled_build']/'manifest.json'
            original = json.loads(manifest_path.read_text())
            manifest = deepcopy(original)
            manifest['documentation'] = [{'path': 'docs/current.png', 'sha256': 'a'*64, 'bytes': 23}]
            manifest_path.write_text(json.dumps(manifest, indent=1)+'\n')
            self.assertEqual(load_exports(root, IDS)['counts']['ports'], 12)
            for key in ('files', 'pieces', 'overlay', 'dependency_audit', 'profile'):
                manifest = deepcopy(original)
                if isinstance(manifest[key], list):
                    manifest[key] = list(reversed(manifest[key])) + [{'unexpected': True}]
                else:
                    manifest[key]['unexpected'] = True
                manifest_path.write_text(json.dumps(manifest))
                with self.subTest(key=key), self.assertRaises(ConnectorDataError) as error:
                    load_exports(root, IDS)
                self.assertEqual(error.exception.code, 'stale_export')

    def test_discovery_receives_structured_missing_stale_and_invalid_failures(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            names = bound_source_names(self.values)
            for defect, expected in [('missing_export', 'missing_export'),
                                     ('missing_source', 'missing_source'),
                                     ('stale_source', 'stale_source'),
                                     ('stale_export', 'stale_export'),
                                     ('invalid_export', 'invalid_export')]:
                with self.subTest(defect=defect):
                    for name in names:
                        target = root/name
                        target.parent.mkdir(parents=True, exist_ok=True)
                        target.write_bytes((ROOT/name).read_bytes())
                    write_exports(root, self.values)
                    export = root/'domains/high-speed-rail/00_pieces'/IDS[0]/'connector-data.json'
                    if defect == 'missing_export':
                        export.unlink()
                    elif defect == 'missing_source':
                        name = next(name for name in names if name.endswith('.dat'))
                        (root/name).unlink()
                    elif defect == 'stale_source':
                        source = root/'domains/high-speed-rail/00_pieces'/IDS[0]/'piece.json'
                        source.write_text(source.read_text()+'\n')
                    elif defect == 'stale_export':
                        source = root/'domains/high-speed-rail/connector-profiles.json'
                        source.write_text(source.read_text()+'\n')
                    else:
                        export.write_text('{ invalid json')
                    with self.assertRaises(ConnectorDataError) as error:
                        load_exports(root, IDS)
                    self.assertEqual(error.exception.code, expected)
