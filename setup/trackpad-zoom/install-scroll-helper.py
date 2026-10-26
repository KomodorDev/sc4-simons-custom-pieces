from pathlib import Path
import datetime
import hashlib
import json
import os
import plistlib
import shlex
import shutil
import subprocess

project = Path(__file__).resolve().parents[2]
folder = project / 'setup/trackpad-zoom'
staged = project / 'setup/pinch-zoom'
app = Path('/Users/simonhinterreiter/Applications/SimCity 4 Windows.app/Contents')
info = app / 'Info.plist'
installed = app / 'Resources/SC4TrackpadZoom.dylib'
runtime = Path('/Users/simonhinterreiter/Documents/SimCity 4 Windows/Setup logs/Trackpad Zoom status.json')
expected = 'b7fb40bd0210daa9876a8f083a696d936b68bff71a89c0a2c85400bec5a59bc8'
assert hashlib.sha256((staged / 'SC4TrackpadZoom.dylib').read_bytes()).hexdigest() == expected
assert subprocess.run(['pgrep', '-fi', '[S]imCity 4.exe'], capture_output=True).returncode == 1, 'Game is running'
p = plistlib.loads(info.read_bytes())
assert p.get('CLI Custom Commands') == '', 'Unexpected custom launch settings'
assert not (app / 'Resources/SC4PinchZoom.dylib').exists(), 'Old pinch helper still installed'
backup = folder / 'before-scroll'
backup.mkdir(exist_ok=True)
assert not (backup / 'Info.plist').exists(), 'Already installed; inspect state first'
shutil.copy2(info, backup / 'Info.plist')
profile = Path('/Users/simonhinterreiter/Documents/SimCity 4 Windows/Plugins')
for name in ['SC4GraphicsOptions.ini', 'SC4RenderServices.ini']:
    shutil.copy2(profile / name, backup / name)
shutil.copy2(app / 'drive_c/launch-sc4.bat', backup / 'launch-sc4.bat')
for name in ['SC4TrackpadZoom.m', 'SC4TrackpadZoom.dylib', 'sc4-trackpad-test', 'scroll-integration-harness.m', 'scroll-integration-harness']:
    shutil.copy2(staged / name, folder / name)
runtime.parent.mkdir(exist_ok=True)
shutil.copy2(folder / 'SC4TrackpadZoom.dylib', installed.with_suffix('.dylib.new'))
os.replace(installed.with_suffix('.dylib.new'), installed)
command = ('export SC4_TRACKPAD_ENABLED=1 SC4_TRACKPAD_STATUS=' + shlex.quote(str(runtime)) +
           ' DYLD_INSERT_LIBRARIES=' + shlex.quote(str(installed)) +
           '"${DYLD_INSERT_LIBRARIES:+:$DYLD_INSERT_LIBRARIES}";')
p['CLI Custom Commands'] = command
info.write_bytes(plistlib.dumps(p, sort_keys=False))
assert plistlib.loads(info.read_bytes())['CLI Custom Commands'] == command
assert hashlib.sha256(installed.read_bytes()).hexdigest() == expected
record = dict(status='Installed; actual game startup and user gesture test pending',
              installed_at=datetime.datetime.now().astimezone().isoformat(),
              installed_library=str(installed), sha256=expected,
              cli_custom_commands=command, original_cli_custom_commands='',
              runtime_status_file=str(runtime), pinch_control=False,
              intended_behavior='One vertical wheel step per two-finger swipe; vertical momentum suppressed',
              isolated_tests='Gesture/proxy tests, production controller integration, and real main-loop startup passed',
              game_runtime_verified=False, user_gesture_verified=False)
(folder / 'installation-status.json').write_text(json.dumps(record, indent=2) + '\n')
print('Scroll-only helper installed. Pinch absent. Graphics and performance settings preserved.')
