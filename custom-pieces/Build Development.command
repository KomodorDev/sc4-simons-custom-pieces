#!/bin/zsh
# Purpose: Double-clickable macOS launcher: audit, build and package; never installs the plugin.
set -eu
cd -- "${0:A:h}"
python3 scp.py doctor
python3 scp.py build --progress
python3 scp.py package
print 'Development package created. No game files were installed.'
read -r '?Press Return to close this window.'
