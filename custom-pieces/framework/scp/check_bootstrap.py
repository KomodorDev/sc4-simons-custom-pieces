"""Run tests against the selected source tree's declared package directories.

This entry point avoids a global editable installation resolving tool packages
from another checkout. It is intentionally invoked by file path using Python.
"""
from importlib.abc import MetaPathFinder
from importlib.util import spec_from_file_location
from pathlib import Path
import sys
import tomllib
import unittest


class SourcePackages(MetaPathFinder):
    def __init__(self, root):
        self.root = Path(root).resolve()
        project = tomllib.loads((self.root/'pyproject.toml').read_text())
        declared = project['tool']['setuptools']['package-dir']
        self.packages = {}
        for name, relative in declared.items():
            directory = (self.root/relative).resolve()
            if not directory.is_relative_to(self.root) or not (directory/'__init__.py').is_file():
                raise ValueError(f'Invalid source package directory: {name} -> {relative}')
            self.packages[name] = directory

    def find_spec(self, fullname, path=None, target=None):
        directory = self.packages.get(fullname)
        if directory is None:
            return None
        return spec_from_file_location(fullname, directory/'__init__.py',
                                       submodule_search_locations=[str(directory)])


def main(argv=None):
    arguments = list(sys.argv[1:] if argv is None else argv)
    if not arguments:
        raise ValueError('Expected the selected library root before unittest arguments')
    finder = SourcePackages(arguments.pop(0))
    # Keep stdlib and dependencies available while forcing every declared
    # project package, including differently named tools directories, local.
    sys.meta_path.insert(0, finder)
    unittest.main(module=None, argv=['unittest', *arguments])


if __name__ == '__main__':
    main()
