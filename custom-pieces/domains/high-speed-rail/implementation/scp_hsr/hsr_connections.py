"""HSR-family ownership and reviewed literal ports for metadata extraction.

The engine's monorail class 7 is the HSR family in these explicitly registered
rail pieces. Native ground paths at 1 m are the GHSR variant; height does not
turn any other engine class into HSR. Tram's class-3 UDI auxiliaries are never
advertised as ordinary railway service.
"""
from functools import lru_cache

@lru_cache(maxsize=1)
def _contracts():
    from .hsr_components_verify import CONTRACTS as components
    from .interchange_verify import CONTRACTS as interchanges
    from .rail_repair_verify import CONTRACTS as repairs
    from .directional_t_verify import CONTRACTS as straight
    from .directional_diagonal_t_verify import CONTRACTS as diagonal
    return {**components, **interchanges, **repairs, **straight, **diagonal}


def reviewed_contract(piece):
    recipe = piece['recipe']
    if recipe in _contracts():return _contracts()[recipe]
    from .rail_feature_verify import RECIPES, _ports
    if recipe in RECIPES:
        ports,movements = _ports(recipe)
        return {'ports': ports, 'movements': sorted(movements)}
    return None


def service_classifier(piece, engine_transport, height):
    if piece['recipe'] == 'rail_hsr_road_stack' and engine_transport in (1, 2):
        pedestrian = engine_transport == 2
        return {'service_network': 'pedestrian' if pedestrian else 'road',
                'service_family': 'pedestrian' if pedestrian else 'road',
                'variant': 'native-road-sidewalk' if pedestrian else 'ordinary-road',
                'role': 'primary',
                'classification_status': 'explicit native ordinary Road PATH audit 00004b00'}
    if engine_transport == 7:
        variant = 'ghsr' if abs(height-1.) < .001 else 'hsr'
        return {'service_network': variant, 'service_family': 'high-speed-rail',
                'variant': variant, 'role': 'primary',
                'classification_status': 'explicit_registered_HSR_family_engine7; variant from actual path elevation'}
    if engine_transport == 6:
        return {'service_network': 'tram', 'service_family': 'light-rail-tram',
                'variant': 'ground-tram', 'role': 'primary',
                'classification_status': 'actual_tram_engine6'}
    if engine_transport == 3 and piece['recipe'] == 'tram_under_hsr':
        return {'service_network': 'tram-udi', 'service_family': 'light-rail-tram',
                'variant': 'rail-based-udi', 'role': 'auxiliary',
                'classification_status': 'native_tram_related_UDI_auxiliary; not ordinary heavy rail'}
    return {'service_network': f'unresolved-engine-{engine_transport}', 'service_family': None,
            'variant': None, 'role': 'unresolved', 'classification_status': 'requires_explicit_domain_review'}


def materialize(root, *, baseline=None, build=None, piece_ids=None):
    """Extract captured non-draft pieces intrinsically, then refresh only them.

    Uncaptured legacy records remain read-only context for deliberately
    affected assemblies. No counterpart catalogue is generated or attached.
    Explicit piece IDs must be unique, implemented, and captured; consume
    their iterable once and validate the complete selection before writes.
    That exact scope refreshes only selected pieces and reports assembly,
    class-view, and inventory refreshes as deferred.
    """
    import json
    from pathlib import Path
    from scp.catalog import load_catalog
    from scp.connectivity import piece_connectivity, orientation_states_from_rules
    from scp.content import fingerprint
    from scp.dbpf import entries, decompress
    from scp.verify import parse_rules
    root = Path(root).resolve()
    catalog = load_catalog(root)
    pieces = {piece['id']:piece for piece in catalog['pieces']}
    selected = {key:value for key,value in pieces.items()
                if value['domain']=='high-speed-rail' and value.get('status') != 'draft'}
    if piece_ids is not None:
        if isinstance(piece_ids, (str, bytes)):
            raise ValueError('Extraction piece IDs must be an iterable of exact identifiers')
        wanted = tuple(piece_ids)
        if (not wanted or not all(isinstance(identifier, str) and identifier for identifier in wanted)
                or len(wanted) != len(set(wanted)) or not set(wanted) <= selected.keys()):
            raise ValueError('Extraction selection contains empty, duplicate, draft, or unknown HSR piece IDs')
        selected = {identifier: selected[identifier] for identifier in wanted}
    records, rule_cache = {}, {}
    if baseline is not None:
        source_root = Path(baseline).resolve()
        sources = json.loads((source_root/'baseline.json').read_text())['pieces']
        source_manifest = None
    else:
        source_root = Path(build).resolve()
        source_manifest = json.loads((source_root/'manifest.json').read_text())
        sources = {piece['id']:{'piece':piece,'file':piece['asset_file']}
                   for piece in source_manifest['pieces'] if piece_ids is None or piece['id'] in selected}
    if piece_ids is not None and not selected.keys() <= sources.keys():
        missing = ', '.join(sorted(selected.keys() - sources.keys()))
        raise ValueError('Selected HSR extraction pieces are absent from the supplied capture: '+missing)
    def construction(item):
        manifest = source_manifest
        if manifest is None:
            name = item.get('source_build')
            if name not in rule_cache:
                file = root/'dist'/str(name)/'manifest.json'
                rule_cache[name] = json.loads(file.read_text()) if file.is_file() else None
            manifest = rule_cache[name]
        if manifest is None:return None
        controller = manifest.get('overlay',{}).get('rul0',{})
        suffix = controller.get('suffix')
        if not suffix:return None
        ordering = controller.get('ordering_insertion','')
        rings,sections = parse_rules(ordering+suffix)
        puzzle = int(item['piece']['puzzle_id'],16)
        wanted = [puzzle+slot*0x10000 for slot in range(8)]
        return {'rotation_ring':next((ring for ring in rings if ring[0]==puzzle),[]),
                'rotation_ring_section':'Ordering' if ordering else 'unverified generator fragment',
                'sections':{f'{key:08x}':sections[key] for key in wanted if key in sections}}
    for identifier,piece in selected.items():
        if identifier not in sources:
            continue
        item = sources[identifier]
        # Resource IDs and reserved occupied cells must still match this source.
        for key in ('tile_ids','preview_id','footprint','cells'):
            if piece.get(key)!=item['piece'].get(key):raise ValueError(f'{identifier}: {key} differs from actual source definition')
        resources = {key:decompress(value) for key,value in entries((source_root/item['file']).read_bytes()).items()}
        record = piece_connectivity(piece,resources,contract=reviewed_contract(piece),service_classifier=service_classifier)
        rules=construction(item)
        if rules is not None:
            record['supported_orientations']=orientation_states_from_rules(rules,piece['puzzle_id'])
            record['source']['resource_fingerprints']['construction:'+identifier]=fingerprint(rules)
            record['source']['construction_basis']='Actual emitted per-piece rule sections from the verified source build record'
            for port in record['ports']:port['resource_keys'].append('construction:'+identifier)
        else:
            record['source']['construction_basis']='unavailable; manual observations must await a current build rule fingerprint'
        records[identifier]=record
    from scp.content import refresh_catalog_content
    refresh_options = {'scope_to_changed': True} if piece_ids is not None else {}
    result = refresh_catalog_content(root, records=records, changed_piece_ids=frozenset(records), **refresh_options)
    return {**result, 'extracted_piece_ids': sorted(records),
            'skipped_draft_piece_ids': sorted(identifier for identifier, piece in pieces.items()
                                             if piece['domain'] == 'high-speed-rail' and piece.get('status') == 'draft'),
            'counterpart_matching_performed': False}



def main():
    import argparse,json
    from pathlib import Path
    from scp.paths import project_root
    parser=argparse.ArgumentParser(description='Refresh actual-resource connectivity and authoritative manual-check views.')
    parser.add_argument('--root',type=Path,default=project_root())
    source=parser.add_mutually_exclusive_group(required=True)
    source.add_argument('--baseline',type=Path,help='Explicit local capture with baseline.json and per-piece DATs')
    source.add_argument('--build',type=Path,help='Current verified build; unchanged uncaptured pieces use their portable metadata')
    parser.add_argument('--piece', action='append', dest='piece_ids',
                        help='Extract only this captured non-draft HSR type; repeat for several changed types')
    args=parser.parse_args()
    print(json.dumps(materialize(args.root,baseline=args.baseline,build=args.build,piece_ids=args.piece_ids),indent=2))

if __name__=='__main__':main()
