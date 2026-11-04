"""Read JSON with // and /* */ comments while preserving JSON error locations.

Only comments are removed. Trailing commas, hash comments and non-JSON numeric
constants remain invalid; quoted text and escaped characters remain unchanged.
"""
import json
from pathlib import Path
import re


def strip_comments(source):
    """Replace comment characters with spaces, retaining every newline and index."""
    if not isinstance(source, str):
        raise TypeError("JSONC source must be text")
    result = list(source)
    index, quoted, escaped = 0, False, False
    while index < len(source):
        char = source[index]
        if quoted:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                quoted = False
            index += 1
            continue
        if char == '"':
            quoted = True
            index += 1
            continue
        if char == "#":
            raise json.JSONDecodeError("Hash comments are not supported", source, index)
        marker = source[index:index+2]
        if marker not in ("//", "/*"):
            index += 1
            continue
        first = index
        if marker == "//":
            index += 2
            while index < len(source) and source[index] not in "\r\n":
                index += 1
        else:
            end = source.find("*/", index+2)
            if end == -1:
                raise json.JSONDecodeError("Unterminated block comment", source, first)
            index = end+2
        for position in range(first, index):
            if source[position] not in "\r\n":
                result[position] = " "
    return "".join(result)


def _invalid_constant(value):
    raise ValueError(f"Non-JSON numeric constant: {value}")


def _unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def loads(source):
    """Parse commented JSON with otherwise strict JSON syntax and numeric values."""
    return json.loads(strip_comments(source), parse_constant=_invalid_constant, object_pairs_hook=_unique_pairs)


def load(path):
    """Read one UTF-8 JSONC file; never write or change its comments."""
    return loads(Path(path).read_text(encoding="utf-8"))


def _metadata(value, name):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"JSONC {name} must be nonempty text")
    return value


def _leading_header(source):
    """Return an existing complete metadata prefix, without changing its bytes."""
    stripped = strip_comments(source)
    length = len(stripped) - len(stripped.lstrip())
    prefix = source[:length]
    fields = {}
    comments = re.finditer(r'//[^\r\n]*|/\*.*?\*/', prefix, re.DOTALL)
    for comment in comments:
        field = re.fullmatch(r'//\s*(title|summary):\s*(.*?)\s*', comment.group())
        if field is None:
            continue
        name, encoded = field.groups()
        if name in fields:
            raise ValueError(f"Duplicate JSONC {name} metadata")
        fields[name] = _metadata(json.loads(encoded), name)
    if fields and set(fields) != {'title', 'summary'}:
        raise ValueError("JSONC metadata requires both title and summary")
    return prefix if fields else None


def document(value, *, source=None, title=None, summary=None):
    """Serialize a document, retaining an existing valid leading comment header.

    Supplied metadata is used for new or headerless documents. Only the leading
    comment prefix is retained; generators own and rewrite their JSON payload.
    """
    header = _leading_header(source) if source is not None else None
    if header is None:
        title, summary = _metadata(title, 'title'), _metadata(summary, 'summary')
        header = (f'// title: {json.dumps(title, ensure_ascii=False)}\n'
                  f'// summary: {json.dumps(summary, ensure_ascii=False)}\n')
    return header + json.dumps(value, indent=2, allow_nan=False) + '\n'


def dumps(value, *, title, summary):
    """Serialize commented JSON with mandatory human-readable metadata."""
    return document(value, title=title, summary=summary)


def dump(path, value, *, title=None, summary=None):
    """Write UTF-8 JSONC, preserving an existing valid metadata prefix."""
    path = Path(path)
    source = path.read_text(encoding='utf-8') if path.is_file() else None
    text = document(value, source=source, title=title, summary=summary)
    if source != text:
        path.write_text(text, encoding='utf-8')


def export(source, destination):
    """Emit deterministic strict JSON for a consumer that cannot read comments."""
    source, destination = Path(source), Path(destination)
    if source.resolve() == destination.resolve():
        raise ValueError("JSONC export must not replace its authoritative source")
    raw = (json.dumps(load(source), indent=2, allow_nan=False) + '\n').encode('utf-8')
    if not destination.is_file() or destination.read_bytes() != raw:
        destination.write_bytes(raw)
    return destination


def main(argv=None):
    """Convert a source to strict JSON without sending it to an external API."""
    import argparse
    import sys
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args(argv)
    if args.output is not None:
        export(args.source, args.output)
    else:
        sys.stdout.write(json.dumps(load(args.source), indent=2, allow_nan=False) + '\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
