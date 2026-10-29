"""Read-only layout and generated-region checks shared by document writers.

Legacy guides retain their authored layout. Explicit current layouts also bind
chapter order, navigation, and each generated region to its owning chapter.
This module never creates documents, changes records, or checks game evidence.
"""
from pathlib import Path
import re

from .piece_matrix import LAYOUT_MARKER, SPLIT_LAYOUT_MARKER


ASSEMBLY_TESTING_LAYOUT_MARKER = '<!-- ASSEMBLY TESTING LAYOUT: 1 -->'
PIECE_TESTING_LAYOUT_MARKER = '<!-- PIECE TESTING LAYOUT: 1 -->'
TESTING_CHAPTERS = ('1. Test scope', '2. Test setup', '3. Software checks',
                    '4. Game checks', '5. Results and known issues', '6. Design history')
PIECE_README_CHAPTERS = ('1. Views', '2. Piece and placement', '3. Connection matrix')
ASSEMBLY_README_CHAPTERS = ('1. Views', '2. Pieces', '3. Placements', '4. Connection matrix')
TESTING_NAVIGATION = '[Testing ↗ (separate document)](TESTING.md)'
_BLOCKS = ('PIECE VIEWS', 'PIECE OVERVIEW', 'PIECE CONNECTION MATRIX',
           'CONNECTOR OVERVIEW', 'ASSEMBLY CONNECTION MATRIX',
           'CONNECTIONS', 'MANUAL SUMMARY', 'MANUAL CHECKS')


def _need(condition, message):
    if not condition:
        raise ValueError(message)


def generated_block_intervals(text, *, required=(), context='Document'):
    """Require one ordered pair per present block, with no crossing or nesting."""
    intervals = {}
    for name in dict.fromkeys((*_BLOCKS, *required)):
        begin, end = f'<!-- BEGIN {name} -->', f'<!-- END {name} -->'
        if name not in required and begin not in text and end not in text:
            continue
        _need(text.count(begin) == text.count(end) == 1 and text.index(begin) < text.index(end),
              context+' requires one ordered '+name+' block')
        intervals[name] = (text.index(begin), text.index(end)+len(end))
    ordered = sorted(intervals.values())
    _need(all(first[1] <= second[0] for first, second in zip(ordered, ordered[1:])),
          context+' generated blocks must not overlap or nest')
    return intervals


def _chapters(text, expected, context):
    found = list(re.finditer(r'^## (.+)$', text, re.M))
    count = 'three' if len(expected) == 3 else 'four' if len(expected) == 4 else 'six'
    _need([match.group(1) for match in found] == list(expected),
          context+' requires its '+count+' numbered chapters')
    return [match.start() for match in found]+[len(text)+1]


def _navigation(text, chapters, bounds, context, *, testing=False, kind=None):
    header = text[:bounds[0]]
    for chapter in chapters:
        target = chapter.replace('.', '').lower().replace(' ', '-')
        link = '['+chapter+'](#'+target+')'
        _need(header.count(link) == 1, context+' requires navigation '+link+' before its chapters')
    if testing:
        overview = '['+kind.capitalize()+' overview ↗ (README)](README.md)'
        _need(header.count(overview) == 1, context+' requires navigation '+overview+' before its chapters')
    else:
        _need(header.count(TESTING_NAVIGATION) == 1,
              context+' requires navigation '+TESTING_NAVIGATION+' before its chapters')


def _place(intervals, name, bounds, chapter, context):
    start, end = intervals[name]
    _need(bounds[chapter] < start < end < bounds[chapter+1],
          context+' requires one '+name+' block in chapter '+str(chapter+1))


def _testing(text, kind):
    context = ('Piece' if kind == 'piece' else 'Assembly')+' TESTING.md'
    marker = PIECE_TESTING_LAYOUT_MARKER if kind == 'piece' else ASSEMBLY_TESTING_LAYOUT_MARKER
    other = ASSEMBLY_TESTING_LAYOUT_MARKER if kind == 'piece' else PIECE_TESTING_LAYOUT_MARKER
    _need(text.count(marker) == 1 and other not in text,
          context+' layout marker must appear once, with the correct subject kind')
    bounds = _chapters(text, TESTING_CHAPTERS, context)
    _navigation(text, TESTING_CHAPTERS, bounds, context, testing=True, kind=kind)
    required = ('CONNECTIONS', 'MANUAL CHECKS')+(('MANUAL SUMMARY',) if kind == 'piece' else ())
    intervals = generated_block_intervals(text, required=required, context=context)
    _need(set(intervals) <= set(required), context+' contains a generated block owned by README.md')
    for name in required:
        _place(intervals, name, bounds, 0 if name == 'CONNECTIONS' else 4, context)
    _need(all(not start <= text.index(marker) < end for start, end in intervals.values()),
          context+' layout marker must stay outside generated blocks')


def _piece_readme(text):
    context = 'Split piece README'
    bounds = _chapters(text, PIECE_README_CHAPTERS, context)
    _navigation(text, PIECE_README_CHAPTERS, bounds, context)
    required = ('PIECE VIEWS', 'PIECE OVERVIEW', 'PIECE CONNECTION MATRIX')
    intervals = generated_block_intervals(text, required=required, context=context)
    _need(set(intervals) <= {*required, 'CONNECTOR OVERVIEW'},
          'Split piece guide keeps testing blocks in TESTING.md')
    for name, chapter in zip(required, range(3)):
        _place(intervals, name, bounds, chapter, context)
    if 'CONNECTOR OVERVIEW' in intervals:
        _place(intervals, 'CONNECTOR OVERVIEW', bounds, 2, context)
        _need(intervals['PIECE CONNECTION MATRIX'][1] <= intervals['CONNECTOR OVERVIEW'][0],
              context+' connection overview must follow its connection matrix')
    _need(text.index(SPLIT_LAYOUT_MARKER) < bounds[0]
          and all(not start <= text.index(SPLIT_LAYOUT_MARKER) < end for start, end in intervals.values()),
          context+' layout marker must precede chapters and stay outside generated blocks')


def _assembly_readme(text):
    context = 'Assembly README'
    bounds = _chapters(text, ASSEMBLY_README_CHAPTERS, context)
    _navigation(text, ASSEMBLY_README_CHAPTERS, bounds, context)
    intervals = generated_block_intervals(text, required=('ASSEMBLY CONNECTION MATRIX',), context=context)
    _need(set(intervals) == {'ASSEMBLY CONNECTION MATRIX'}, context+' keeps testing blocks in TESTING.md')
    start, end = intervals['ASSEMBLY CONNECTION MATRIX']
    # The matrix renderer owns the fourth H2 heading itself. Its BEGIN marker
    # therefore precedes that heading, rather than sitting below it.
    heading_start = bounds[3]
    prefix = text[start+len('<!-- BEGIN ASSEMBLY CONNECTION MATRIX -->'):heading_start]
    _need(bounds[2] < start < heading_start < end < bounds[4] and not prefix.strip(),
          context+' requires its matrix block to own only chapter 4')


def validate_subject_documents(directory, subject, *, allow_missing=False):
    """Validate one current or retained legacy pair without writing anything.

    Writers allow missing files because their pure scaffold supplies them later.
    Existing marked parts are still checked before that creation. A catalogue
    checker uses the default to reject missing documents in an opted-in pair.
    Local file and anchor resolution deliberately belongs to the caller: a
    generated view can temporarily reference cases that the writer will update.
    """
    _need(subject.get('kind') in ('piece', 'assembly'), 'Unknown document subject kind')
    directory = Path(directory)
    documents = {name: (directory/name).read_text() for name in ('README.md', 'TESTING.md')
                 if (directory/name).is_file()}
    for name, text in documents.items():
        generated_block_intervals(text, context=name)
    readme, testing = documents.get('README.md'), documents.get('TESTING.md')
    identity = {'id': subject['id'], 'kind': subject['kind']}
    if subject['kind'] == 'piece':
        _need(testing is None or ASSEMBLY_TESTING_LAYOUT_MARKER not in testing,
              'Piece TESTING.md cannot use an assembly layout marker')
        counts = [readme.count(marker) if readme is not None else 0
                  for marker in (LAYOUT_MARKER, SPLIT_LAYOUT_MARKER)]
        _need(sum(counts) <= 1, 'Piece layout marker must occur once, with one version')
        current = bool(counts[1]) or readme is None or (testing is not None and PIECE_TESTING_LAYOUT_MARKER in testing)
        if current:
            if readme is not None:
                _need(counts == [0, 1], 'Split piece README layout marker must appear once')
                _piece_readme(readme)
            if testing is not None:
                _testing(testing, 'piece')
        elif counts[0]:
            # Version 1 retains its inline layout, but its existing writer
            # requires these six regions. Check them during batch preflight,
            # rather than failing after earlier selected subjects changed.
            generated_block_intervals(readme, required=('PIECE VIEWS', 'PIECE OVERVIEW',
                'PIECE CONNECTION MATRIX', 'MANUAL SUMMARY', 'CONNECTIONS', 'MANUAL CHECKS'),
                context='Numbered piece guide')
        layout = 'piece-split-v2' if current else 'legacy'
    else:
        _need(readme is None or not any(marker in readme for marker in (LAYOUT_MARKER, SPLIT_LAYOUT_MARKER)),
              'Assembly README cannot use a piece layout marker')
        _need(testing is None or PIECE_TESTING_LAYOUT_MARKER not in testing,
              'Assembly TESTING.md cannot use a piece layout marker')
        marker_count = testing.count(ASSEMBLY_TESTING_LAYOUT_MARKER) if testing is not None else 0
        current = bool(marker_count) or (readme is not None and re.findall(r'^## (.+)$', readme, re.M)
                                        == list(ASSEMBLY_README_CHAPTERS)) or not documents
        if current:
            if readme is not None:
                _assembly_readme(readme)
            if testing is not None:
                _testing(testing, 'assembly')
        layout = 'assembly-numbered-v1' if current else 'legacy'
    if current and len(documents) < 2:
        _need(allow_missing, 'Missing '+', '.join(name for name in ('README.md', 'TESTING.md') if name not in documents)
              +' for '+subject['id'])
        layout = 'pending'
    return {'subject': identity, 'layout': layout, 'files': list(documents)}
