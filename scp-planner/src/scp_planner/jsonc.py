"""Compatibility imports for the source-owned JSONC reader; no local parser copy."""
from ._source import source_module

_reader = source_module('jsonc')
strip_comments = _reader.strip_comments
loads = _reader.loads
load = _reader.load

__all__ = ['strip_comments', 'loads', 'load']
