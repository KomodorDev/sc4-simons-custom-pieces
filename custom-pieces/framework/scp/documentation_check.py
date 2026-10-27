"""Read-only catalogue documentation checks; never extract or record evidence."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

from .catalog import load_catalog


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
        documents += [root/name for name in ('README.md', 'STRUCTURE.md', 'AGENTS.md')]
        documents += list((root/'docs').glob('*.md'))
        documents += list((root/'skills').glob('*/SKILL.md'))
        for domain in catalog['domains'].values():
            directory = root/domain['path']
            documents += [directory/name for name in ('README.md', 'AGENTS.md', 'NETWORK_SPEC.md')
                          if (directory/name).is_file()]
    links = check_local_links(documents, boundary=root.parent)
    errors += links['errors']
    return {'all_passed': not errors, 'subjects_checked': len(subjects),
            'current_layouts': sum(row['layout'] not in ('legacy', 'pending') for row in reports),
            'legacy_subjects': [row['subject'] for row in reports if row['layout'] == 'legacy'],
            'pending_subjects': [row['subject'] for row in reports if row['layout'] == 'pending'],
            'documents_checked': len(set(documents)), 'local_links_checked': links['checked_links'],
            'errors': errors, 'manual_game_results_changed': False, 'installed': False}
