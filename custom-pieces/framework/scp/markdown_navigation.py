"""Number maintained Markdown chapters and keep their local navigation current.

This formatter deliberately owns headings, legacy heading aliases, and its
marked navigation block only. Prose, tables, lists, front matter, and fenced
examples remain authored content. Subject-specific README and TESTING writers
keep their own layouts and do not call this module.
"""
from __future__ import annotations

from dataclasses import dataclass
from html import escape, unescape
from html.parser import HTMLParser
import re


NAVIGATION_BEGIN = '<!-- BEGIN DOCUMENT NAVIGATION -->'
NAVIGATION_END = '<!-- END DOCUMENT NAVIGATION -->'
_NUMBER = re.compile(r'^(?:\d+\.|\d+(?:\.\d+)+\.?)[ \t]+')
_HEADING = re.compile(r'^( {0,3})(#{1,6})([ \t]+)(.*)$')


@dataclass(frozen=True)
class MarkdownHeading:
    """One real ATX heading, with a one-based source line and unique fragment."""

    line: int
    level: int
    title: str
    slug: str


def _active_lines(lines):
    """Exclude YAML, HTML comments, and fences, including nested-list fences."""
    active = []
    front_matter = bool(lines and lines[0].lstrip('\ufeff').strip() == '---')
    fence = None
    comment = False
    for index, line in enumerate(lines):
        if front_matter:
            active.append(False)
            if index and line.strip() in ('---', '...'):
                front_matter = False
            continue
        if fence is not None:
            match = re.match(r'^[ \t]*(`{3,}|~{3,})(.*?)(?:\r?\n)?$', line)
            active.append(False)
            if (match and match[1][0] == fence[0] and len(match[1]) >= len(fence)
                    and not match[2].strip()):
                fence = None
            continue
        if not comment:
            match = re.match(r'^[ \t]*(`{3,}|~{3,})(.*?)(?:\r?\n)?$', line)
            if match:
                active.append(False)
                fence = match[1]
                continue
        # Standalone marker comments stay visible to the navigation remover.
        visible = line
        began_in_comment = comment
        if comment:
            end = visible.find('-->')
            if end < 0:
                active.append(False)
                continue
            visible = visible[end+3:]
            comment = False
        while '<!--' in visible:
            start = visible.index('<!--')
            end = visible.find('-->', start+4)
            if end < 0:
                comment = True
                visible = visible[:start]
                break
            visible = visible[:start]+visible[end+3:]
        if began_in_comment:
            active.append(False)
            continue
        active.append(not comment and (bool(visible.strip()) or line.strip() in
                                      (NAVIGATION_BEGIN, NAVIGATION_END)))
    return active


def _heading_parts(line):
    body = line.rstrip('\r\n')
    match = _HEADING.match(body)
    if match is None:
        return None
    title = match[4]
    closing = re.match(r'^(.*?)([ \t]+#+[ \t]*)$', title)
    if closing:
        title, suffix = closing.groups()
    else:
        title = title.rstrip(' \t')
        suffix = match[4][len(title):]
    return match[1]+match[2]+match[3], len(match[2]), title, suffix, line[len(body):]


def _plain_heading_text(title):
    title = re.sub(r'!?\[([^\]]+)\]\([^)]*\)', r'\1', title)
    return unescape(re.sub(r'<[^>]+>', '', title))


def heading_slug(title):
    """Return the base GitHub-style heading fragment, without duplicate suffixes."""
    return re.sub(r'[^\w\- ]', '', _plain_heading_text(title).lower()).replace(' ', '-')


def markdown_headings(text):
    """Read actual headings without treating front matter or examples as prose."""
    lines = text.splitlines(keepends=True)
    used, result = set(), []
    for index, active in enumerate(_active_lines(lines)):
        parts = _heading_parts(lines[index]) if active else None
        if parts is None:
            continue
        _, level, title, _, _ = parts
        base = heading_slug(title)
        slug, count = base, 0
        while slug in used:
            count += 1
            slug = base+'-'+str(count)
        used.add(slug)
        result.append(MarkdownHeading(index+1, level, title, slug))
    return result


class _ExplicitAnchors(HTMLParser):
    def __init__(self):
        super().__init__()
        self.anchors = set()

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if 'id' in values:
            self.anchors.add(values['id'])
        if tag == 'a' and 'name' in values:
            self.anchors.add(values['name'])


def _explicit_anchors(text):
    lines = text.splitlines(keepends=True)
    parser = _ExplicitAnchors()
    parser.feed(''.join(line if active else '\n'
                        for line, active in zip(lines, _active_lines(lines))))
    return parser.anchors


def _remove_navigation(lines):
    active = _active_lines(lines)
    result, start, separator = [], None, False
    for index, line in enumerate(lines):
        if separator:
            separator = False
            if not line.strip():
                continue
        marker = line.strip() if active[index] else None
        if marker == NAVIGATION_BEGIN:
            if start is not None:
                raise ValueError('Document navigation blocks must not nest')
            start = index
        elif marker == NAVIGATION_END:
            if start is None:
                raise ValueError('Document navigation END has no BEGIN')
            start = None
            # Consume only the separator that this formatter writes itself.
            separator = True
        elif start is None:
            result.append(line)
    if start is not None:
        raise ValueError('Document navigation BEGIN has no END')
    return result


def _body_start(lines):
    """Find the position after the title and any required subject layout markers."""
    for heading in markdown_headings(''.join(lines)):
        if heading.level == 1:
            position = heading.line
            while position < len(lines):
                line = lines[position].strip()
                if line and re.fullmatch(r'<!-- [A-Z][A-Z0-9 ]* LAYOUT: \d+ -->', line) is None:
                    break
                position += 1
            return position
    if lines and lines[0].lstrip('\ufeff').strip() == '---':
        for index, line in enumerate(lines[1:], 1):
            if line.strip() in ('---', '...'):
                return index+1
    return 0


def _insert_overview(lines, newline):
    headings = markdown_headings(''.join(lines))
    first_section = next((heading for heading in headings if heading.level > 1), None)
    if first_section is not None and first_section.level == 2:
        return lines
    position = _body_start(lines)
    while position < len(lines) and not lines[position].strip():
        position += 1
    prefix = [] if position == 0 or not lines[position-1].strip() else [newline]
    lines[position:position] = prefix+['## Overview'+newline, newline]
    return lines


def _navigation_label(title):
    # Nested links cannot appear inside another Markdown link label.
    return _plain_heading_text(title).replace('[', r'\[').replace(']', r'\]')


def format_markdown_navigation(text):
    """Return numbered H2–H6 headings and an H2-only navigation row.

    H1 titles stay unnumbered. A document with no chapter, or a child heading
    before its first chapter, receives an Overview chapter. Existing heading
    fragments survive as explicit aliases unless the same heading or an authored
    anchor already supplies that fragment. An old fragment that would silently
    point to a different final heading is rejected. Applying the formatter twice
    has no further effect.
    """
    newline = '\r\n' if '\r\n' in text else '\n'
    if text and not text.endswith(('\n', '\r')):
        text += newline
    lines = _insert_overview(_remove_navigation(text.splitlines(keepends=True)), newline)
    original = markdown_headings(''.join(lines))
    counters = [0]*5
    for heading in original:
        if heading.level == 1:
            continue
        depth = heading.level-2
        if depth and not counters[depth-1]:
            raise ValueError('Heading on line '+str(heading.line)+' skips its H'
                             +str(heading.level-1)+' parent: '+heading.title)
        counters[depth] += 1
        counters[depth+1:] = [0]*(4-depth)
        number = '.'.join(str(value) for value in counters[:depth+1])
        title = number+('. ' if depth == 0 else ' ')+_NUMBER.sub('', heading.title)
        prefix, _, _, suffix, ending = _heading_parts(lines[heading.line-1])
        lines[heading.line-1] = prefix+title+suffix+ending
    final_text = ''.join(lines)
    final = markdown_headings(final_text)
    destinations = {heading.slug: heading for heading in final}
    anchors = _explicit_anchors(final_text) | {heading.slug for heading in final}
    aliases = {}
    for old, new in zip(original, final):
        if old.slug != new.slug and old.slug in destinations:
            conflicting = destinations[old.slug]
            raise ValueError('Cannot preserve heading fragment #'+old.slug+' from "'
                             +old.title+'" (line '+str(old.line)+'): numbering would retarget it to "'
                             +conflicting.title+'" (line '+str(conflicting.line)+')')
        if old.slug != new.slug and old.slug not in anchors:
            aliases[old.line-1] = '<a id="'+escape(old.slug, quote=True)+'"></a>'+newline+newline
            anchors.add(old.slug)
    lines = [aliases.get(index, '')+line for index, line in enumerate(lines)]
    # Alias insertion can make a list item contain several physical lines.
    lines = ''.join(lines).splitlines(keepends=True)
    position = _body_start(lines)
    while position < len(lines) and not lines[position].strip():
        position += 1
    prefix = [] if position == 0 or not lines[position-1].strip() else [newline]
    links = ' · '.join('['+_navigation_label(heading.title)+'](#'+heading.slug+')'
                       for heading in final if heading.level == 2)
    lines[position:position] = prefix+[
        NAVIGATION_BEGIN+newline, links+newline, NAVIGATION_END+newline, newline]
    return ''.join(lines).rstrip('\r\n')+newline
