# Native macOS cache builder for SC4 Plop and Paint

Built on 7 September 2026 for this Apple Silicon Mac. This helper scans installed game assets and creates the browsing data and preview pictures used by the Windows game DLL. The game DLL itself remains the author's original Windows release.

## Ready-to-run files

- `bin/SC4PlopAndPaintCacheBuilder`: native Mach-O 64-bit ARM64 executable, approximately 3 MB.
- `bin/PropertyMapper.xml`: the exact mapping file extracted from the official v0.10.2 Windows installer.
- The helper needs only macOS system libraries and frameworks at runtime. Homebrew, Wine, and the Windows x64 Visual C++ runtime are not needed to run this compiled helper.
- Run it with `bin` as the working directory so it can find `PropertyMapper.xml`.

The source change described below makes its version label `v0.10.2-dirty`. This identifies the local compatibility patch; it does not indicate a failed or unfinished build.

## Running against the Windows game profile

Close SimCity 4 first, then run:

```sh
cd '/Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/plop-and-paint-native/bin'
./SC4PlopAndPaintCacheBuilder --scan \
  --game '/Users/simonhinterreiter/Applications/SimCity 4 Windows.app/Contents/SharedSupport/prefix/drive_c/GOG Games/SimCity 4 Deluxe Edition' \
  --plugins '/Users/simonhinterreiter/Documents/SimCity 4 Windows/Plugins' \
  --locale English \
  --render-thumbnails \
  --thumbnail-size 44
```

`--game` points to the folder containing the original SimCity data files and its installation `Plugins` folder. `--plugins` is the user's Windows mod folder. The helper scans both and writes its results into the user folder. There is no separate output-directory option. `--render-thumbnails` enables previews of models without existing icons. The allowed thumbnail size is 22–176 pixels; the author defaults to 44. Match this to `ThumbnailDisplaySize` in the game mod's INI file.

Outputs are `lots.cbor`, `props.cbor`, `flora.cbor`, `lot_thumbnails.bin`, `prop_thumbnails.bin`, and `flora_thumbnails.bin` when data for each category is available. Rebuild after adding or removing game assets. The helper does not write city saves.

## Source provenance

- Main source: <https://github.com/caspervg/sc4-plop-and-paint>, tag `v0.10.2`, commit `494d9542b2fd93c57a97a22deb1750eb17d3f837`.
- All submodules checked out to the release's pinned commits; recorded in `source-submodules.txt`.
- Dependencies built from the author's bundled vcpkg manifest, baseline `cc73782a88db48af17f8bfb8328d4cab3d4c246f`, ARM64 macOS triplet. The same pinned reflect-cpp 0.23.0 serializes the Windows and Mac cache files.
- Build tools: Apple Clang 16.0.0, CMake 4.4.3 and Ninja 1.13.2. CMake and Ninja were installed through Homebrew for this task.

## Local compiler compatibility patch

The release's DBPFKit submodule uses floating-point `std::from_chars`, which the C++ standard library bundled with this Mac's Apple Clang 16 does not implement. The first build therefore failed in `vendor/DBPFKit/src/RUL0.cpp`.

Only that floating-point conversion was replaced with the equivalent `fast_float::from_chars` function. The integer conversions, cache schemas, game-asset parsing code used by the cache builder, and Windows DLL are unchanged. The replacement library is the author's official fast_float v8.2.10 source at <https://github.com/fastfloat/fast_float>, commit `34164f547b7df3f5d794ff67e9f885c36819ebfc`. It is a header-only build dependency and adds no runtime installation.

The exact two-line change is saved as `apple-clang16-fast-float.patch`. Its header include directory was passed through CMake's `CMAKE_CXX_FLAGS` setting. Both repositories and their licence files are retained here.

## Compatibility and validation

- `--help` and `--version` exit successfully.
- Upstream DBPFKit tests: 35 test cases, 254 assertions passed, including floating-point parser tests.
- Upstream cache/entity tests: 26 test cases, 107 assertions passed, including CBOR serialization and deserialization.
- `ctest`: both registered suites passed; see `tests.log`.
- `file` confirms ARM64. `otool -L` confirms all runtime dependencies are macOS system libraries or frameworks.
- Source inspection confirms that persisted cache entities contain object IDs and game data, with no Mac source-file paths for the Windows DLL to resolve. Scanning paths are internal to the helper.
- The thumbnail file format uses explicit 16-, 32-, and 64-bit fields; Apple ARM64 and Windows x86 both use little-endian byte order. The data formats match the release DLL by source inspection. In-game verification remains the main installation task's responsibility.

The builder was not run against the live game profile during this isolated build task.

## Checksums

SHA-256:

```text
e2eb58e61e63c6185189652f0e997b29d1b6c7944c326a723def7aab68161b4b  bin/SC4PlopAndPaintCacheBuilder
738ac8718e979e1b8d125aa4a92e4d4e6dafeea92203273517edf870fd2c3379  bin/PropertyMapper.xml
```

Full configure, dependency-build, compilation, and test logs are retained beside this document. The source and build tree use approximately 805 MB; the runnable `bin` folder is approximately 4.1 MB.
