"""Generate separate illustrated piece and assembly inventories from manual records."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from .catalog import load_catalog, piece_cells
from .content import markdown_metadata, summarize_manual_record, _replace_generated, _assembly_matrix_enabled
from .assembly_matrix import summarize_assembly_connection_matrix
from .design_review import review_label
from .paths import project_root


def _status(directory):
    path=directory/'checks/manual-tests.json'
    if not path.is_file():return {'record_present':False,'summary':None}
    return {'record_present':True,'summary':summarize_manual_record(json.loads(path.read_text()))}


def _coverage(status,kind):
    if not status['record_present']:return '[ ] Unverified; record missing'
    summary=status['summary']
    counts=(summary.get('journey_coverage',summary['by_kind'].get(kind,{}))
            if kind=='in_game_journey' else summary['by_kind'].get(kind,{}))
    total=sum(counts.values())-counts.get('not_applicable',0)
    if not total:return 'Not applicable / no declared cases'
    passed=counts.get('passed',0)
    mark='[x]' if passed==total else '[ ]'
    return (f'{mark} {passed}/{total} passed; {counts.get("unverified",0)} unverified; '
            f'{counts.get("failed",0)} failed; {counts.get("stale",0)} stale')


def _matrix_status(directory):
    if not _assembly_matrix_enabled(directory, {'kind': 'assembly'}):
        return {'available': False, 'reason': 'No connection matrix declared'}
    for name in ('connections.json', 'checks/manual-tests.json'):
        if not (directory/name).is_file():
            return {'available': False, 'reason': f'Unverified; {name} missing'}
    connections = json.loads((directory/'connections.json').read_text())
    record = json.loads((directory/'checks/manual-tests.json').read_text())
    return {'available': True, **summarize_assembly_connection_matrix(connections, record)}


def _matrix_coverage(summary, link):
    if not summary['available']:
        return summary['reason']
    parts = [f'[Open matrix]({link})']
    for key, label in (('saved_path', 'Saved PATH'), ('route_query', 'Route Query'),
                       ('visible_travel', 'Visible travel'), ('forbidden', 'Forbidden in game')):
        counts = summary['metrics'][key]
        total = sum(counts.values())
        if not total:
            continue
        text = f'{label}: {counts["confirmed"]}/{total} confirmed'
        if counts['failed']:
            text += f'; {counts["failed"]} failed'
        if counts['not_established']:
            text += f'; {counts["not_established"]} not established'
        parts.append(text)
    if len(parts) == 1:
        parts.append('No directional matrix entries declared')
    return '<br>'.join(parts)


def _heading(title,purpose,assembly=False):
    source = ('This inventory is generated from each assembly’s saved records. '
              'The source files and update procedure are explained under **Where the results come from** below. '
              if assembly else 'Generated from each subject’s authoritative `checks/manual-tests.json`. ')
    return [markdown_metadata(title,purpose,'players','catalogue').rstrip(),'',f'# {title}','',
        source+'Checked means every applicable listed current case passed. Preview review and correct rendering inside SimCity 4 are separate checks. A result covers only its named scope, rotation, and recorded environment. Legacy endpoint observations remain historical evidence in the subject checklist and do not establish current compatibility coverage.','']


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
                'path':identifier+'/README.md','preview':identifier+'/previews/preview.png','thumbnail':identifier+'/previews/preview-thumb.png',
                'manual_record':identifier+'/checks/manual-tests.json','design_review':piece.get('design_review')})
            piece_status[identifier]=status
            width,depth=piece['footprint']
            image=f'[![{piece["name"]}]({identifier}/previews/preview-thumb.png)]({identifier}/previews/preview.png)' if all((local/'previews'/name).is_file() for name in ('preview.png','preview-thumb.png')) else 'Preview pending'
            review=piece.get('design_review')
            design=(f'[{review_label(piece)}]({identifier}/README.md#design-review): '+review['summary']) if review else 'No current design flag'
            piece_rows.append(f'| {image} | [{piece["name"]}]({identifier}/README.md)<br>`{identifier}` | '
                f'{width} × {depth}; {len(piece_cells(piece))} | {design} | {_coverage(status,"preview_review")} | '
                f'{_coverage(status,"in_game_render")} | {_coverage(status,"in_game_journey")} |')
        if not pieces:piece_rows+=['','No implemented pieces are registered in this domain.']
        assembly_rows=_heading(domain['name']+' — assembly blueprints','Find each documented multi-placement assembly, a clean preview, and its per-service test coverage.',assembly=True)
        assembly_rows += [
            '## Legend', '',
            'An **assembly** is a complete layout made from reusable pieces. A **piece type** is one reusable component design; a **placement** is one copy of that type at a particular position and rotation.', '',
            '| Column | How to read it |',
            '| --- | --- |',
            '| Clean preview | A computer-rendered picture of the complete layout without component-name labels. Click it to open the full image. |',
            '| Blueprint | The assembly name. Click it to open the guide with its pictures, component list, and placement instructions. This is a layout to construct from components; each placement requires its own click. |',
            '| Placements / types | Total placed copies / number of different reusable piece types. For example, `5 / 3` means five copies using three types; repeated copies of one type count as several placements but only one type. These numbers do not count tiles or menu buttons. |',
            '| Preview reviewed | Recorded human reviews of the declared final assembly images. Each image has its own case; generating an image does not record its approval. |',
            '| Renders correctly in game | Recorded human checks that the complete placed layout looks correct inside SimCity 4 under the declared conditions. This checks appearance; the connection matrix separately reports traffic. |',
            '| Connection matrix summary | A summary of the results displayed in the blueprint’s entrance → exit matrix. Saved PATH, Route Query, visible travel, and forbidden-movement checks have separate totals. Click **Open matrix** to inspect those entries and their exact evidence. |', '',
            '### Where the results come from', '',
            '**Both appearance columns read `checks/manual-tests.json` inside the assembly’s folder.** This is the saved observation record:', '',
            '- **Preview reviewed** reads the `preview_review` cases.',
            '- **Renders correctly in game** reads the `in_game_render` cases.', '',
            '**`TESTING.md` displays the same saved observations. The inventory does not read its checkboxes.** Editing text or ticking a checkbox in `TESTING.md` does not update the observation record or the inventory results.', '',
            'The **Connection matrix summary** uses the same calculation as the README matrix. It combines the movements and current software evidence in `connections.json` with the results in `checks/manual-tests.json`; it does not read the rendered Markdown table.', '',
            'To update a human result, perform the exact check, obtain explicit human confirmation, and save that observation using the [recording procedure](../../../docs/TESTING.md#record-one-observation). In this repository, the recording command updates the saved record and refreshes `TESTING.md`, the README matrix, and the inventory. Regenerating documents alone does not record a pass.', '',
            '### How to read the results', '',
            'A **case** is one specific check. In the two review columns, `0/6 passed` means zero of six applicable current cases have a recorded pass. `[x]` means all applicable current cases passed; `[ ]` means that condition is not met. **Unverified** means no qualifying result is recorded, **failed** means an observation found a problem, and **stale** means relevant resources or conditions changed after the recorded result. Unverified does not mean failed. Explicit not-applicable cases and historical observations are excluded from these case fractions. `Not applicable / no declared cases` means there are no applicable cases to count, and `Unverified; record missing` means the observation record is absent; neither is a pass.', '',
            'The **connection matrix summary** counts displayed matrix entries for each check: **confirmed** matches ✅, **failed** matches ❌, and **not established** matches ?. An entry is confirmed only when all checks required for its declared orientations are current passes. Missing, stale, ambiguous, or not-applicable evidence leaves an entry not established. **Saved PATH** checks the saved traffic routes; **Route Query** uses the game’s route-inspection tool; **Visible travel** requires observing a vehicle complete the journey; and **Forbidden in game** checks that a prohibited movement stays unavailable. One software result can support several Saved PATH entries, so these are matrix-entry counts, not independent test-case counts. Game appearance stays in its own column. Open the blueprint’s **Testing** link for the detailed observations and checks outside the matrix.', '',
        ]
        assembly_rows+=['| Clean preview | Blueprint | Placements / types | Preview reviewed | Renders correctly in game | Connection matrix summary |',
                        '| --- | --- | --- | --- | --- | --- |']
        assembly_status={}
        for assembly in assemblies:
            local=root/assembly['path'];status=_status(local)
            placements=assembly['scene'].get('placements',assembly['scene'].get('instances',[]))
            file=local/'connections.json';conn=json.loads(file.read_text()) if file.is_file() else {}
            identifier=assembly['id'];status.update({'path':identifier+'/README.md','placements':len(placements),
                'unique_piece_types':len({item['piece_id'] for item in placements}),'journeys':len(conn.get('journeys',[])),
                'manual_record':identifier+'/checks/manual-tests.json','preview':identifier+'/previews/preview.png'})
            status['connection_matrix'] = _matrix_status(local)
            assembly_status[identifier]=status
            title=assembly['scene'].get('title')
            label=title.strip() if isinstance(title,str) and title.strip() else identifier
            label=label.replace('|','\\|').replace('\n',' ').replace('[','\\[').replace(']','\\]')
            image=f'[![{label}]({identifier}/previews/preview.png)]({identifier}/previews/preview.png)' if (local/'previews/preview.png').is_file() else 'Preview pending'
            assembly_rows.append(f'| {image} | [{label}]({identifier}/README.md) | {status["placements"]} / {status["unique_piece_types"]} | '
                f'{_coverage(status,"preview_review")} | {_coverage(status,"in_game_render")} | '
                f'{_matrix_coverage(status["connection_matrix"],identifier+"/README.md#4-connection-matrix")} |')
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
