"""Consume SCP's source-owned connector exports and compare piece placements."""

from .metadata import find_matches, load_pilot
from .discovery import discover_compatibility

__all__ = ["find_matches", "load_pilot", "discover_compatibility"]
