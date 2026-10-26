"""Read JSON with // and /* */ comments while preserving JSON error locations.

Only comments are removed. Trailing commas, hash comments and non-JSON numeric
constants remain invalid; quoted text and escaped characters remain unchanged.
"""
import json
from pathlib import Path


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
