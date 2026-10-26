#!/bin/sh
set -eu
cd "$(dirname "$0")"

bundle='Rebuild SimCity Content.app'
mkdir -p "$bundle/Contents/MacOS"
cp Info.plist "$bundle/Contents/Info.plist"
/usr/bin/xcrun swiftc -swift-version 5 -target arm64-apple-macos12.0 -O \
    -vfsoverlay swift-overlay.json -Xcc -ivfsoverlay -Xcc swift-overlay.json \
    -module-cache-path module-cache -framework AppKit -framework Foundation \
    main.swift ReadableProgress.swift -o "$bundle/Contents/MacOS/RebuildSimCityContent"
# Finder metadata on this newly generated bundle is not allowed in a code signature.
/usr/bin/xattr -d com.apple.FinderInfo "$bundle" 2>/dev/null || true
/usr/bin/codesign --force --sign - "$bundle"
/usr/bin/codesign --verify --deep --strict "$bundle"
/usr/bin/plutil -lint "$bundle/Contents/Info.plist"
/usr/bin/file "$bundle/Contents/MacOS/RebuildSimCityContent"
