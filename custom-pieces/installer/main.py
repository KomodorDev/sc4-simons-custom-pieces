"""Launch the self-contained installer, or run its offline packaging checks."""
from __future__ import annotations

import argparse
from importlib.util import module_from_spec, spec_from_file_location
import json
from pathlib import Path
import sys
import tempfile
import tomllib

sys.dont_write_bytecode = True


def runtime_root():
    if getattr(sys, "frozen", False):
        return Path(sys._MEIPASS) / "custom-pieces"
    return Path(__file__).resolve().parents[1]


def bootstrap(root):
    """Load every project module from the inspected, original source hierarchy."""
    root = Path(root).resolve()
    spec = spec_from_file_location("_scp_installer_bootstrap", root / "framework/scp/check_bootstrap.py")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)

    class RuntimePackages(module.SourcePackages):
        def find_spec(self, fullname, path=None, target=None):
            # Frozen importers and unrelated editable installations must not
            # supply a flattened geometry module with a different __file__.
            for prefix, directory in sorted(self.packages.items(), key=lambda row: -len(row[0])):
                if fullname != prefix and not fullname.startswith(prefix + "."):
                    continue
                relative = fullname[len(prefix):].lstrip(".").split(".") if fullname != prefix else []
                location = directory.joinpath(*relative)
                if (location / "__init__.py").is_file():
                    return spec_from_file_location(fullname, location / "__init__.py",
                                                   submodule_search_locations=[str(location)])
                if location.with_suffix(".py").is_file():
                    return spec_from_file_location(fullname, location.with_suffix(".py"))
            return None

    finder = RuntimePackages(root)
    finder.packages["scp_installer"] = root / "installer/scp_installer"
    sys.meta_path.insert(0, finder)
    sys.path[:0] = [str(root / "framework"), str(root / "installer")]
    return root


def metadata(root):
    filename = root / "installer/build-info.json"
    if filename.is_file():
        data = json.loads(filename.read_text(encoding="utf-8"))
        if data.get("bundled_native_game_resources") is not False:
            raise ValueError("The installer package has invalid distribution metadata.")
        return data
    if getattr(sys, "frozen", False):
        raise ValueError("The installer package is incomplete. Download and extract the complete ZIP.")
    project = tomllib.loads((root / "pyproject.toml").read_text(encoding="utf-8"))["project"]
    return {"schema_version": 1, "kind": "source-local-builder", "version": project["version"],
            "source_commit": None, "platform": "source-checkout", "experimental": True,
            "bundled_native_game_resources": False}


def verify_runtime(root):
    if (root / "installer/runtime-manifest.json").is_file():
        spec = spec_from_file_location("_scp_installer_bundle", root / "installer/build_bundle.py")
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        return module.verify_runtime(root)
    if getattr(sys, "frozen", False):
        raise ValueError("The installer package is incomplete. Extract the entire ZIP before opening it.")
    return {"status": "source-checkout", "frozen_package_verified": False}


def _emit(value, destination):
    text = json.dumps(value, indent=2) + "\n"
    if destination:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(text, encoding="utf-8")
    if sys.stdout is not None:
        sys.stdout.write(text)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Simon's Custom Pieces Installer")
    actions = parser.add_mutually_exclusive_group()
    actions.add_argument("--version", action="store_true")
    actions.add_argument("--self-test", action="store_true")
    actions.add_argument("--gui-smoke-test", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args(argv)
    try:
        root = bootstrap(runtime_root())
        info = metadata(root)
        verification = verify_runtime(root)
        if args.version:
            _emit({"status": "passed", **info, "runtime_verification": verification}, args.report)
            return 0
        if args.self_test:
            from scp_installer.service import self_test
            result = self_test(root)
            _emit({**result, "source_commit": info["source_commit"],
                   "runtime_verification": verification}, args.report)
            return 0
        from scp_installer.gui import run, smoke_test
        if args.gui_smoke_test:
            with tempfile.TemporaryDirectory(prefix="scp-installer-gui-check-") as temporary:
                result = smoke_test(root, info, Path(temporary).resolve())
            _emit({**result, "source_commit": info["source_commit"],
                   "runtime_verification": verification}, args.report)
            return 0
        run(root, info)
        return 0
    except Exception as error:
        result = {"status": "failed", "error": str(error)}
        if args.report or args.version or args.self_test or args.gui_smoke_test:
            _emit(result, args.report)
        else:
            # This fallback also works when a damaged package cannot import Tk.
            if sys.platform == "win32":
                import ctypes
                ctypes.windll.user32.MessageBoxW(None, str(error), "SCP Installer", 0x10)
            elif sys.stderr is not None:
                sys.stderr.write(str(error) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
