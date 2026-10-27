"""Generate separate illustrated piece and assembly inventories from manual records."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from .catalog import load_catalog, piece_cells
from .content import markdown_metadata, summarize_manual_record, _replace_generated
from .design_review import review_label
from .paths import project_root


def _status(directory):
    path=directory/'checks/manual-tests.json'
    if not path.is_file():return {'record_present':False,'summary':None}
    return {'record_present':True,'summary':summarize_manual_record(json.loads(path.read_text()))}


def _coverage(status,kind):
    if not status['record_present']:return '[ ] Unverified; record missing'
    counts=(status['summary'].get('journey_coverage', status['summary']['by_kind'].get(kind, {}))
            if kind == 'in_game_journey' else status['summary']['by_kind'].get(kind, {}))
    total=sum(counts.values())-counts.get('not_applicable',0)
    if not total:return 'Not applicable / no declared cases'
    passed=counts.get('passed',0)
    mark='[x]' if passed==total else '[ ]'
    return (f'{mark} {passed}/{total} passed; {counts.get("unverified",0)} unverified; '
            f'{counts.get("failed",0)} failed; {counts.get("stale",0)} stale')


def _heading(title,purpose):
    return [markdown_metadata(title,purpose,'players','catalogue').rstrip(),'',f'# {title}','',
        'Generated from each subject’s authoritative `checks/manual-tests.json`. Checked means every applicable listed current case passed. Preview review and correct rendering inside SimCity 4 are separate checks. A result covers only its named scope, rotation, and recorded environment. Legacy endpoint observations remain historical evidence in the subject checklist and do not establish current compatibility coverage.','']


def write_inventories(root):
    root=Path(root).resolve();catalog=load_catalog(root);written=[]
    for slug,domain in catalog['domains'].items():
        directory=root/domain['path']
        pieces=[piece for piece in catalog['pieces'] if piece['domain']==slug]
        assemblies=[item for item in catalog.get('_assemblies',[]) if item['domain']==slug]
        piece_rows=_heading(domain['name']+' — individual pieces','Find each separate menu button, one reusable type image, its connections, and current test coverage.')
        piece_rows += ['| Preview | Exact menu name / piece ID | Footprint; occupied | Design review | Preview reviewed | Renders correctly in game | Directed journey cases |',
                       '| --- | --- | --- | --- | --- | --- | --- |']
        piece_status={}
        for piece in pieces:
            local=directory/'00_pieces'/piece['id'];status=_status(local)
            file=local/'connections.json';conn=json.loads(file.read_text()) if file.is_file() else {}
            identifier=piece['id'];status.update({'ports':len(conn.get('ports',[])),'journeys':len(conn.get('journeys',[])),
                'path':identifier+'/README.md','preview':identifier+'/preview.png','thumbnail':identifier+'/preview-thumb.png',
                'manual_record':identifier+'/checks/manual-tests.json','design_review':piece.get('design_review')})
            piece_status[identifier]=status
            width,depth=piece['footprint']
            image=f'[![{piece["name"]}]({identifier}/preview-thumb.png)]({identifier}/preview.png)' if all((local/name).is_file() for name in ('preview.png','preview-thumb.png')) else 'Preview pending'
            review=piece.get('design_review')
            design=(f'[{review_label(piece)}]({identifier}/README.md#design-review): '+review['summary']) if review else 'No current design flag'
            piece_rows.append(f'| {image} | [{piece["name"]}]({identifier}/README.md)<br>`{identifier}` | '
                f'{width} × {depth}; {len(piece_cells(piece))} | {design} | {_coverage(status,"preview_review")} | '
                f'{_coverage(status,"in_game_render")} | {_coverage(status,"in_game_journey")} |')
        if not pieces:piece_rows+=['','No implemented pieces are registered in this domain.']
        assembly_rows=_heading(domain['name']+' — assembly blueprints','Find each documented multi-placement assembly, a clean preview, and its per-service test coverage.')
        assembly_rows+=['| Clean preview | Blueprint | Placements / types | Preview reviewed | Renders correctly in game | Directed journey cases |',
                        '| --- | --- | --- | --- | --- | --- |']
        assembly_status={}
        for assembly in assemblies:
            local=root/assembly['path'];status=_status(local)
            placements=assembly['scene'].get('placements',assembly['scene'].get('instances',[]))
            file=local/'connections.json';conn=json.loads(file.read_text()) if file.is_file() else {}
            identifier=assembly['id'];status.update({'path':identifier+'/README.md','placements':len(placements),
                'unique_piece_types':len({item['piece_id'] for item in placements}),'journeys':len(conn.get('journeys',[])),
                'manual_record':identifier+'/checks/manual-tests.json','preview':identifier+'/previews/preview.png'})
            assembly_status[identifier]=status
            image=f'[![{identifier}]({identifier}/previews/preview.png)]({identifier}/previews/preview.png)' if (local/'previews/preview.png').is_file() else 'Preview pending'
            assembly_rows.append(f'| {image} | [{identifier}]({identifier}/README.md) | {status["placements"]} / {status["unique_piece_types"]} | '
                f'{_coverage(status,"preview_review")} | {_coverage(status,"in_game_render")} | '
                f'{_coverage(status,"in_game_journey")} |')
        if not assemblies:assembly_rows+=['','No assembly blueprints are registered in this domain.']
        ids={piece['id'] for piece in pieces}
        sets={name:[identifier for identifier in members if identifier in ids] for name,members in catalog.get('piece_sets',{}).items() if any(identifier in ids for identifier in members)}
        overview=['## Inventories and collections', '',
                  f'- [Individual pieces: {len(pieces)} menu types](00_pieces/INVENTORY.md).',
                  f'- [Assembly blueprints: {len(assemblies)} '+('design' if len(assemblies)==1 else 'designs')+'](01_assemblies/INVENTORY.md).', '',
                  '<details>', '<summary>Named build collections</summary>', '',
                  'A collection selects existing piece types; it is not an additional piece or a one-click assembly.', '']
        overview += [f'- `{name}`: {len(members)} piece types.' for name,members in sets.items()]
        if not sets:overview += ['No named piece collections are registered in this domain.']
        overview += ['', '</details>', '']
        readme=directory/'README.md'
        if not readme.is_file():
            readme.write_text(markdown_metadata(domain['name'], 'Find this domain’s pieces, assemblies, and named selections.',
                                               'players', 'guide')+'# '+domain['name']+'\n')
        _replace_generated(readme,'COLLECTIONS','\n'.join(overview))
        (directory/'INVENTORY.md').unlink(missing_ok=True)
        overview_data={'schema_version':2,'purpose':'Generated domain navigation and collection membership; subject test records remain authoritative.',
            'version':catalog['version'],'domain':slug,'count':len(pieces),'assembly_count':len(assemblies),
            'piece_inventory':'00_pieces/inventory.json','assembly_inventory':'01_assemblies/inventory.json','piece_sets':sets}
        (directory/'inventory.json').write_text(json.dumps(overview_data,indent=2)+'\n')
        sections=((directory/'00_pieces',piece_rows,{'count':len(pieces),'pieces':pieces,'status':piece_status}),
                  (directory/'01_assemblies',assembly_rows,{'count':len(assemblies),'assemblies':assembly_status}))
        for target,rows,data in sections:
            target.mkdir(exist_ok=True)
            (target/'INVENTORY.md').write_text('\n'.join(rows)+'\n')
            data={'schema_version':2,'purpose':'Generated current subject index and manual coverage; authoritative results remain in each subject manual-tests.json.',
                  'version':catalog['version'],'domain':slug,**data}
            (target/'inventory.json').write_text(json.dumps(data,indent=2)+'\n')
            written.append(str((target/'INVENTORY.md').relative_to(root)))
    return {'written':written,'installed':False}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--root',type=Path,default=project_root())
    args=parser.parse_args();print(json.dumps(write_inventories(args.root),indent=2))

if __name__=='__main__':main()
