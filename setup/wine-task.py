from pathlib import Path
import os
import subprocess
import sys

APP = Path('/Users/simonhinterreiter/Applications/SimCity 4 Windows.app')
SUPPORT = APP / 'Contents/SharedSupport'
PREFIX = SUPPORT / 'prefix'
env = os.environ.copy()
env.update(
    WINEPREFIX=str(PREFIX), WINEARCH='win32', WINEDEBUG='-all',
    DYLD_FALLBACK_LIBRARY_PATH=f'{SUPPORT}/wine/lib32on64:{SUPPORT}/wine/lib:/usr/lib',
)
binary = SUPPORT / ('wine/bin/wineserver' if sys.argv[1] == '--server' else 'wine/bin/wine32on64')
arguments = sys.argv[2:] if sys.argv[1] == '--server' else sys.argv[1:]
raise SystemExit(subprocess.call([str(binary), *arguments], env=env))
