"""Enable or disable the verified, temporary NAM Diagonal Bridge Enabler.

The source DAT files stay outside Plugins. Only this helper's symlink is
created/removed. No city saves or other plugins are edited.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

PROFILE = Path('/Users/simonhinterreiter/Documents/SimCity 4 Windows')
TOOLS = PROFILE / 'Diagonal Bridge Tools'
PAYLOAD = TOOLS / 'Temporary Files'
ACTIVE = PROFILE / 'Plugins' / '~Diagonal Bridge Enabler (Temporary Files)'


def active_state():
    if ACTIVE.is_symlink():
        if ACTIVE.resolve() != PAYLOAD.resolve():
            raise RuntimeError('The bridge folder points somewhere unexpected. Nothing was changed.')
        return True
    if ACTIVE.exists():
        raise RuntimeError('A separate bridge folder already exists in Plugins. Nothing was changed.')
    return False


def verify_payload():
    manifest_path = TOOLS / 'payload-sha256.json'
    if not manifest_path.is_file():
        raise RuntimeError('The Diagonal Bridge Enabler download has not been installed yet.')
    expected = json.loads(manifest_path.read_text())
    actual_names = {p.name for p in PAYLOAD.iterdir() if p.is_file()}
    if actual_names != set(expected):
        raise RuntimeError('The bridge tool files differ from the verified installation. Nothing was changed.')
    for name, digest in expected.items():
        p = PAYLOAD / name
        data = p.read_bytes()
        if data[:4] != b'DBPF' or hashlib.sha256(data).hexdigest() != digest:
            raise RuntimeError('A bridge tool file has changed. Nothing was changed.')


def require_game_closed():
    processes = subprocess.run(['/bin/ps', '-axo', 'comm='], capture_output=True, text=True, check=True).stdout
    for process in processes.splitlines():
        if 'simcity 4.exe' in process.lower() or 'simcity4.exe' in process.lower():
            raise RuntimeError('Save your city, quit SimCity 4 completely, then open this tool again. The game must restart to change bridge mode.')


def main():
    action = sys.argv[1] if len(sys.argv) == 2 else 'status'
    if action not in {'enable', 'disable', 'status'}:
        raise RuntimeError('Choose enable, disable, or status.')
    enabled = active_state()
    if action == 'status':
        print('Diagonal bridge construction mode is ON.' if enabled else 'Normal play: water and normal road slopes are ON.')
        return
    require_game_closed()
    if action == 'enable':
        verify_payload()
        if not enabled:
            ACTIVE.symlink_to(PAYLOAD, target_is_directory=True)
        print('Diagonal bridge construction mode is ready.\n\nStart SimCity 4 Windows. Water will be temporarily lowered and roads will stay level. Pause the city and build your bridge.\n\nWhen finished: save, quit the game, and open Restore Normal Water before playing normally.')
    else:
        if enabled:
            ACTIVE.unlink()
        print('Normal play is restored.\n\nStart SimCity 4 Windows to see normal water and road slopes. Your saved bridges remain.')


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
