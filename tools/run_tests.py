"""Run every library test suite against this checkout's source."""
from __future__ import annotations

from pathlib import Path
import shlex
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    if sys.version_info < (3, 11):
        print("Tests require Python 3.11 or newer.", file=sys.stderr)
        return 1
    try:
        import PIL
        import numpy
    except ImportError as error:
        print(f"Missing test dependency: {error}", file=sys.stderr)
        print(
            "Install the complete test dependencies with: "
            f"{shlex.join([sys.executable, '-m', 'pip', 'install', '-r', str(ROOT / 'requirements-ci.txt')])}",
            file=sys.stderr,
        )
        return 1

    print(f"Python {sys.version.split()[0]}, Pillow {PIL.__version__}, and NumPy {numpy.__version__}", flush=True)
    print(
        "Tests that need unavailable NAM files or a staged game build report explicit skips. "
        "Software tests do not record manual game observations.",
        flush=True,
    )
    command = [sys.executable, "-B", "custom-pieces/scp.py", "check", "--scope", "all", "--verbose"]
    print(f"\nLibrary (framework, domains, and assemblies): {shlex.join(command)}", flush=True)
    result = subprocess.run(command, cwd=ROOT, check=False)
    if result.returncode:
        print("\nFailed test suites: Library", file=sys.stderr)
        return result.returncode
    print("\nAll test suites passed. Review the explicit skips above for unavailable game inputs.", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
