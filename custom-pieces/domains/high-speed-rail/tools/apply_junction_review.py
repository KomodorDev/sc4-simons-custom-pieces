#!/usr/bin/env python3
"""Validate saved rail review flags and refresh current subject documentation."""
from collections import Counter
import json
from pathlib import Path
import sys

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.jsonc').is_file())
sys.path.insert(0, str(ROOT / 'framework'))
from scp import jsonc
from scp.catalog import load_catalog
from scp.content import refresh_catalog_content
from scp.design_review import LABELS


SUMMARIES = {
    'clustered-supports': 'Closely spaced pillars need a support-consolidation review.',
}


def validate_saved_review(review, known):
    """Reject inconsistent saved evidence before changing a piece or collection."""
    records = review['pieces']
    ids = [record['id'] for record in records]
    if len(ids) != len(set(ids)) or not set(ids) <= known.keys():
        raise ValueError('Review evidence contains duplicate or unknown current piece IDs')
    if any(known[slug].get('domain') != 'high-speed-rail' for slug in ids):
        raise ValueError('Rail review evidence contains another domain\'s piece')
    counts = Counter(record['verdict'] for record in records)
    if not set(counts) <= {'no-objection-recorded', *LABELS}:
        raise ValueError('Review evidence contains an unknown verdict')
    for record in records:
        if (type(record['flag_recommended']) is not bool
                or record['flag_recommended'] != (record['verdict'] in LABELS)):
            raise ValueError('Review flag and verdict disagree for '+record['id'])
        if record['flag_recommended'] and (not record['reasons'] or not all(
                isinstance(reason, str) and reason.strip() for reason in record['reasons'])):
            raise ValueError('Flagged review needs explicit reasons for '+record['id'])
    flagged = [record for record in records if record['flag_recommended']]
    if (review['reviewed_piece_count'] != len(records)
            or review['flagged_piece_count'] != len(flagged)
            or review['verdict_counts'] != dict(counts)):
        raise ValueError('Review evidence counts disagree with its current piece records')
    by_verdict = {verdict: [record['id'] for record in flagged if record['verdict'] == verdict]
                  for verdict in LABELS}
    expected = {verdict: ids for verdict, ids in by_verdict.items() if ids}
    recorded = {verdict: ids for verdict, ids in review['flagged_piece_ids_by_verdict'].items() if ids}
    if recorded != expected:
        raise ValueError('Review verdict selections disagree with its current piece records')
    return {'flagged': [record['id'] for record in flagged], 'counts': dict(counts),
            'by_verdict': by_verdict}


def apply_saved_review(root):
    """Apply existing observations, then refresh READMEs and both inventories.

    This does not review new geometry, regenerate model resources or create a
    separate Markdown catalogue. Unflagged records clear only flags associated
    with the same saved build; unrelated observations remain intact.
    """
    root = Path(root).resolve()
    domain = root / 'domains/high-speed-rail'
    review = jsonc.load(domain / 'junction-design-review.jsonc')
    collection_file = domain / 'collections.jsonc'
    collections = jsonc.load(collection_file)
    known = {piece['id']: piece for piece in load_catalog(root)['pieces']}
    result = validate_saved_review(review, known)
    for record in review['pieces']:
        slug = record['id']
        path = domain / '00_pieces' / slug / 'piece.json'
        piece = json.loads(path.read_text())
        if record['flag_recommended']:
            summary = next((SUMMARIES[code] for code in record['reason_codes']
                            if code in SUMMARIES), record['reasons'][0])
            piece['design_review'] = {
                'status': record['verdict'], 'summary': summary,
                'reasons': record['reasons'], 'reason_codes': record['reason_codes'],
                'reviewed_build': review['source_build_version'],
                'evidence': 'domains/high-speed-rail/junction-design-review.json',
            }
        elif piece.get('design_review', {}).get('reviewed_build') == review['source_build_version']:
            # A newer independent review must survive an older saved observation.
            piece.pop('design_review', None)
        updated = json.dumps(piece, indent=2) + '\n'
        if path.read_text() != updated:
            path.write_text(updated)
    selections = collections['collections']
    selections['flagged-junctions'] = result['flagged']
    for status, selection in (
            ('needs-redesign', 'junctions-needing-redesign'),
            ('review-needed', 'junctions-needing-review')):
        ids = result['by_verdict'][status]
        if ids:
            selections[selection] = ids
        else:
            selections.pop(selection, None)
    jsonc.dump(collection_file, collections)
    load_catalog(root)
    views = refresh_catalog_content(root)
    return {'flagged': len(result['flagged']), 'counts': result['counts'],
            'documentation': views, 'game_models_changed': False, 'installed': False}


def main():
    print(json.dumps(apply_saved_review(ROOT), indent=2))


if __name__ == '__main__':
    main()
