"""Read-only catalogue documentation checks; never extract or record evidence."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

from .catalog import load_catalog
from .markdown_navigation import (NAVIGATION_BEGIN, NAVIGATION_END,
                                  _active_lines, _body_start, _navigation_label, markdown_headings)


def check_shared_document_navigation(text):
    """Check maintained guides without rewriting authored prose or legacy anchors."""
    headings = markdown_headings(text)
    errors = []

    def error(line, message):
        errors.append({'line': line, 'error': message})

    titles = [heading for heading in headings if heading.level == 1]
    if len(titles) != 1:
        error(titles[1].line if len(titles) > 1 else 1,
              'Shared Markdown needs exactly one unnumbered H1 document title')
    for title in titles:
        if re.match(r'^(?:\d+\.|\d+(?:\.\d+)+\.?)(?:\s|$)', title.title):
            error(title.line, 'The H1 document title must be unnumbered')
    if titles and headings[0] != titles[0]:
        error(headings[0].line, 'The H1 document title must precede all chapters')

    chapters = [heading for heading in headings if heading.level == 2]
    if not chapters:
        error(titles[0].line if titles else 1,
              'Shared Markdown needs at least one numbered H2 chapter, starting with 1.')
    counters = [0] * 5
    for heading in headings:
        if heading.level == 1:
            continue
        depth = heading.level - 2
        missing_parent = depth and not counters[depth - 1]
        counters[depth] += 1
        counters[depth + 1:] = [0] * (4 - depth)
        if missing_parent:
            error(heading.line, 'H'+str(heading.level)+' heading skips its H'
                  +str(heading.level - 1)+' parent: '+heading.title)
            continue
        number = '.'.join(str(value) for value in counters[:depth + 1])
        token = number + ('.' if depth == 0 else '')
        if not re.fullmatch(re.escape(token) + r'[ \t]+\S.*', heading.title):
            suffix = ('; subsection numbers have no trailing period' if depth else '')
            error(heading.line, 'Expected H'+str(heading.level)+' heading numbered '
                  +token+' followed by its title'+suffix+': '+heading.title)

    lines = text.splitlines(keepends=True)
    active = _active_lines(lines)
    begins = [index for index, line in enumerate(lines)
              if active[index] and line.strip() == NAVIGATION_BEGIN]
    ends = [index for index, line in enumerate(lines)
            if active[index] and line.strip() == NAVIGATION_END]
    if len(begins) != 1 or len(ends) != 1:
        error((begins[0] + 1) if begins else (titles[0].line + 1 if titles else 1),
              'Shared Markdown needs exactly one DOCUMENT NAVIGATION block with one BEGIN and one END')
        return errors
    start, end = begins[0], ends[0]
    if end <= start:
        error(end + 1, 'DOCUMENT NAVIGATION END must follow its BEGIN')
        return errors
    if titles and start != _body_start(lines):
        error(start + 1, 'DOCUMENT NAVIGATION must appear immediately after the H1 title and any required layout markers, separated only by blank lines')
    if end != start + 2:
        error(start + 1, 'DOCUMENT NAVIGATION must contain exactly one physical line of chapter links')
    else:
        expected = ' · '.join('['+_navigation_label(heading.title)+'](#'+heading.slug+')'
                              for heading in chapters)
        if lines[start + 1].strip() != expected:
            error(start + 2, 'DOCUMENT NAVIGATION must link every H2 chapter with its exact label and fragment, in chapter order, and contain no subsection links')
    return errors


def _without_fences(text):
    lines, fence = [], None
    for line in text.splitlines(keepends=True):
        match = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if match and (fence is None or match[1][0] == fence[0] and len(match[1]) >= len(fence)):
            fence = match[1] if fence is None else None
            lines.append('\n')
        else:
            lines.append(line if fence is None else '\n')
    return ''.join(lines)


class _HTMLLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.anchors = [], []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.anchors.append(attrs['id'])
        if tag == 'a' and 'name' in attrs:
            self.anchors.append(attrs['name'])
        for attribute in ('href', 'src'):
            if attribute in attrs:
                self.links.append((self.getpos()[0], attrs[attribute]))


def _markdown(text):
    text = _without_fences(text)
    parser = _HTMLLinks()
    parser.feed(text)
    anchors, duplicates = set(parser.anchors), Counter(parser.anchors)
    seen = Counter()
    for heading in re.findall(r'^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$', text, re.M):
        heading = re.sub(r'!?\[([^\]]+)\]\([^)]*\)', r'\1', heading)
        heading = re.sub(r'<[^>]+>', '', heading)
        slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        count = seen[slug]
        anchors.add(slug + ('-'+str(count) if count else ''))
        seen[slug] += 1
    links = list(parser.links)
    # Keep line numbers while ignoring code samples that merely illustrate links.
    references = {}
    for match in re.finditer(r'^ {0,3}\[([^\]]+)\]:\s*(<[^>]+>|\S+)', text, re.M):
        references[match[1].casefold()] = match[2].strip('<>')
    for line_number, line in enumerate(text.splitlines(), 1):
        line = re.sub(r'`+[^`]*`+', '', line)
        for match in re.finditer(r'\]\((<[^>]+>|[^)\s]+)(?:\s+"[^"]*")?\)', line):
            links.append((line_number, match[1].strip('<>')))
        for match in re.finditer(r'!?\[([^\]]+)\]\[([^\]]*)\]', line):
            key = (match[2] or match[1]).casefold()
            if key in references:
                links.append((line_number, references[key]))
    return anchors, links, sorted(key for key, count in duplicates.items() if count > 1)


def check_local_links(paths, *, boundary):
    """Check local Markdown/HTML targets and anchors without network access."""
    boundary = Path(boundary).resolve()
    cache, errors, checked = {}, [], 0
    def parsed(path):
        if path not in cache:
            cache[path] = _markdown(path.read_text(encoding='utf-8'))
        return cache[path]
    for source in sorted(set(Path(path).resolve() for path in paths)):
        anchors, links, duplicates = parsed(source)
        for anchor in duplicates:
            errors.append({'file': source.relative_to(boundary).as_posix(), 'line': 1,
                           'error': 'Duplicate explicit anchor: '+anchor})
        for line, url in links:
            parts = urlsplit(url)
            if parts.scheme or parts.netloc:
                continue
            checked += 1
            target = (source.parent/unquote(parts.path)).resolve() if parts.path else source
            reason = None
            if not target.is_relative_to(boundary):
                reason = 'Local link leaves the checkout: '+url
            elif not target.is_file():
                reason = 'Missing local file: '+url
            elif parts.fragment and target.suffix.lower() == '.md' and unquote(parts.fragment) not in parsed(target)[0]:
                reason = 'Missing Markdown anchor: '+url
            if reason:
                errors.append({'file': source.relative_to(boundary).as_posix(), 'line': line, 'error': reason})
    return {'checked_links': checked, 'errors': errors}


def check_documentation(root, *, piece_ids=None, assembly_ids=None):
    """Check current subject pairs and explicitly report retained legacy guides."""
    from .document_validation import validate_subject_documents
    root = Path(root).resolve()
    catalog = load_catalog(root)
    pieces = {piece['id']: piece for piece in catalog['pieces']}
    assemblies = {assembly['id']: assembly for assembly in catalog['_assemblies']}
    selected = piece_ids is not None or assembly_ids is not None
    piece_ids = list(dict.fromkeys(piece_ids or ([] if selected else pieces)))
    assembly_ids = list(dict.fromkeys(assembly_ids or ([] if selected else assemblies)))
    unknown = sorted(set(piece_ids)-pieces.keys()) + sorted(set(assembly_ids)-assemblies.keys())
    if unknown:
        raise ValueError('Unknown documentation subject: '+', '.join(unknown))
    subjects = []
    for identifier in piece_ids:
        piece = pieces[identifier]
        directory = root/catalog['domains'][piece['domain']]['path']/'00_pieces'/identifier
        subjects.append((directory, {**piece, 'kind': 'piece'}))
    subjects += [(root/assemblies[identifier]['path'], {'id': identifier, 'kind': 'assembly'})
                 for identifier in assembly_ids]
    reports, errors, documents = [], [], []
    for directory, subject in subjects:
        try:
            report = validate_subject_documents(directory, subject)
            reports.append(report)
        except ValueError as error:
            errors.append({'subject': subject['id'], 'error': str(error)})
            continue
        if report['layout'] in ('legacy', 'pending'):
            continue
        documents += [directory/name for name in report['files']]
        if subject.get('status') == 'draft':
            continue
        required = ['icon.png', 'connections.json', 'checks/manual-tests.json', 'checks/observation.example.json']
        if subject['kind'] == 'piece':
            required += ['previews/preview.png', 'previews/preview-thumb.png', 'evidence/preview.json']
            if any((directory/name).is_file() for name in ('connector-groups.jsonc', 'connector-data.json')):
                required += ['connector-groups.jsonc', 'connector-data.json',
                             'previews/connection-overview.png', 'evidence/connection-overview.json']
        for name in required:
            if not (directory/name).is_file():
                errors.append({'subject': subject['id'], 'error': 'Missing implemented-subject file: '+name})
    # Shared maintained instructions are checked on the default catalogue run.
    if not selected:
        shared = [root/name for name in ('README.md', 'STRUCTURE.md', 'AGENTS.md')]
        shared += list((root/'docs').glob('*.md'))
        shared += list((root/'skills').glob('*/SKILL.md'))
        for domain in catalog['domains'].values():
            directory = root/domain['path']
            shared += [directory/name for name in ('README.md', 'AGENTS.md', 'NETWORK_SPEC.md',
                                                  '00_pieces/INVENTORY.md', '01_assemblies/INVENTORY.md')
                       if (directory/name).is_file()]
        # Source archives and portable tests can put the self-contained library
        # under any directory name. Only a real checkout has repository guides.
        if root.name == 'custom-pieces' and (root.parent/'.git').exists():
            shared += [root.parent/name for name in ('README.md', 'AGENTS.md', 'docs/GITHUB.md')]
        for path in shared:
            errors += [{'file': path.relative_to(root.parent).as_posix(), **item}
                       for item in check_shared_document_navigation(path.read_text(encoding='utf-8'))]
        documents += shared
    links = check_local_links(documents, boundary=root.parent)
    errors += links['errors']
    return {'all_passed': not errors, 'subjects_checked': len(subjects),
            'current_layouts': sum(row['layout'] not in ('legacy', 'pending') for row in reports),
            'legacy_subjects': [row['subject'] for row in reports if row['layout'] == 'legacy'],
            'pending_subjects': [row['subject'] for row in reports if row['layout'] == 'pending'],
            'documents_checked': len(set(documents)), 'local_links_checked': links['checked_links'],
            'errors': errors, 'manual_game_results_changed': False, 'installed': False}
