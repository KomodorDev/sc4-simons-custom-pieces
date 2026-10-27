---
title: "Build, install, and inspect SCP"
summary: "Explain local prerequisites, private inputs, and the complete build, installation, packaging, and verification workflow."
audience: "Players, authors, and maintainers"
document_type: "procedure"
---

# Build, install, and inspect SCP


An expandable **SimCity 4 network-piece plugin**, version **0.6.0.dev1**. Each selected piece has its own **SCP** button in **Transportation → Rail**. Teal **PART** icons identify individual building pieces; purple **PNP** icons identify complete one-click junctions. Network and piece-type abbreviations are explained [below](#recognize-scp-menu-icons). The current trumpet is a modular assembly; its complete one-click construction is blocked by measured tile-address collisions with the current tools. New complete complex interchanges are delivered as modular rebuilding blueprints, each with its own guide and named placement renders. The two existing accepted smooth T PNP pieces remain available. NAM remains a dependency. These are experimental development pieces. Software checks and compiled-model previews do not establish game operation. The construction checks account for runtime tile addresses and empty borders in the four diagonal S-curves. Simtropolis publication has not been performed.

## Current pieces and assembly design

The [rail player guide](../domains/high-speed-rail/README.md) explains network levels, matching approaches and the main piece families. Browse the [illustrated pieces](../domains/high-speed-rail/00_pieces/INVENTORY.md) or [assembly blueprints](../domains/high-speed-rail/01_assemblies/INVENTORY.md) for current types, pictures and scoped status. Named collections and their current counts are in the player guide. The [trumpet rebuilding guide](../domains/high-speed-rail/01_assemblies/straight-stem-trumpet-v4/README.md) identifies every module, position and rotation.

Use the [assembly workflow](WORKFLOW_ASSEMBLY_CREATION.md) to agree on a schematic, inventory compatible types, build missing useful modules and review actual compiled grid renders. The [engineering reference](FRAMEWORK_ENGINEERING.md#mixed-network-ownership) owns mixed-network classification. Complete complex interchanges use documented modular blueprints; the existing accepted smooth-T buttons remain PNP types.

Use [WORKFLOW: Documentation Generation](WORKFLOW_DOCUMENTATION_GENERATION.md) to produce README files, previews, connector exports, and cards from the appropriate verified inputs; the [connector reference](CONNECTOR_METADATA.md) defines the connection data.

## Recognize SCP menu icons

Open **Transportation → Rail** and hover over a button beginning **SCP |** to read its full name and description. Teal **PART** means one independently placeable building block. Purple **PNP** means an implemented complete junction placed with one click. PNP does not mean game operation has passed testing. A collection or assembly guide does not create a complete-interchange button.

| Network code |Meaning |
| --- | --- |
| **HSR** | Elevated high-speed rail, including the additional upper levels. |
| **GSR** | Ground high-speed rail (GHSR); the shorter code fits the small icon. |
| **MIX** | A crossing or transition involving both HSR and GHSR. |
| **TRAM** | The HSR/ground-tram crossing. |

| Type code | Meaning |
| --- | --- |
| **STR** | Straight track. |
| **DIA** | Diagonal track. |
| **CRV** | Curve, including S-curves and curves that change height. |
| **SPL** / **MRG** | Split / merge. |
| **JCT** | A combined split-and-merge or fork connection. |
| **RMP** | Ramp or height transition. |
| **XNG** | Crossing. |
| **SWI** | Switch or scissors crossover. |
| **ADP** | Adapter between track arrangements. |
| **T** | Complete smooth full T junction. |

The exact angle, height, handedness and footprint remain in the full name and tooltip; the small code is a browsing aid. The revised scissors retain their small green check beside the silhouette and their names still end in **Revised**. Recorded design-review warnings remain in titles and tooltips.

## Prepare local development inputs

The Git checkout supplies maintained source, canonical artwork, schemas, tests, and recorded evidence. A **template** is an example file that each contributor copies and fills in for their own machine. A fresh checkout can run portable tests without a game installation; cases requiring native game resources or saved builds report explicit skips.

### Python setup for a checkout or source ZIP

Install Python 3.11 or newer from the [official Python downloads](https://www.python.org/downloads/) if it is not already available. CI uses Python 3.11. A **virtual environment** keeps this project's Python packages separate from other installations. Create a new environment for each checkout; do not copy an old environment or rely on an editable installation pointing at another checkout.

For a Git checkout, open a terminal in the directory containing `custom-pieces/`. A source ZIP also contains `custom-pieces/`; extract it, then open a terminal in the directory directly containing that folder. These instructions are included in the source ZIP and do not require the repository's separate root README or CI files. On macOS, open Terminal; on Windows, open PowerShell; on Linux, open your terminal application.

On macOS or Linux, create and activate the environment:

```sh
python3 -m venv .venv
source .venv/bin/activate
```

On Windows, use PowerShell:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

With the environment active, the following commands work on all three systems:

```sh
python --version
python -m pip install -r custom-pieces/requirements-preview.txt
python -m pip install -e custom-pieces
python -B custom-pieces/scp.py check --scope all --verbose
```

The version must be 3.11 or newer. The requirements install Pillow for images and NumPy for numerical rendering; no separate rendering executable is required. `-e` registers the source in this checkout, so later module commands use these files. A Git checkout can additionally install its root `requirements-ci.txt` to use CI's exact dependency pins, then run `python -B tools/run_tests.py`. Those two root files are not included in the library-only source ZIP.

All later Python commands in this guide assume that the environment remains active and that you are in the directory containing `custom-pieces/`. The macOS double-click launcher uses `python3` from its command search path; it does not automatically activate `.venv`. Use the terminal commands here when selecting the new environment explicitly.

### Native game inputs and supported baseline

The Python tools can run on macOS, Linux, and Windows. The audited game profile is **SimCity 4 Deluxe version 1.1.641 for Windows, with NAM 50 and right-hand traffic**. Right-hand traffic means vehicles drive on the right. The profile does not establish support for the native macOS game port. See the [NAM Team's official installation instructions](https://www.sc4nam.com/docs/getting-started/installation/) for obtaining NAM and its installer, DLL, and game requirements.

A NAM version label alone does not prove that its files match this project's audited inputs. The four core archive filenames and SHA-256 fingerprints are recorded under the `controller`, `hsr`, `urail`, and `glr` keys in [`config/profiles/nam50-rhd.json`](../config/profiles/nam50-rhd.json). Additional entries, such as `ordinary_road` and `ordinary_road_texture`, are optional captured inputs required only by pieces that declare those dependencies. A **fingerprint** identifies exact file contents. `doctor` checks the selected dependency files and identifier conflicts; it does not inspect the game executable or certify a game platform. Do not change a recorded fingerprint merely to make a different installation pass.

| Item | Provided in Git | Local use |
| --- | --- | --- |
| Workstation settings | [`config/local.example.json`](../config/local.example.json) | Copy to ignored `custom-pieces/local/settings.json`, then supply every active Plugins directory. |
| Supported NAM input identities | [`config/profiles/nam50-rhd.json`](../config/profiles/nam50-rhd.json) | Supply the matching four core archives from your own NAM installation, plus any optional captured dependencies required by your selected pieces. |
| Python dependencies and package definitions | Library requirements and `pyproject.toml` | Install them in a newly created environment for this checkout. |
| Isolated native inputs | No game archives | Optional private copies under `custom-pieces/local/validation-inputs/` support repeatable texture and verification work. Follow the [preparation procedure](#optional-isolated-native-inputs). |
| Compiled builds, packages, and caches | No generated build templates | Generate them from source and matching NAM inputs. Existing `dist/` directories are convenient retained outputs, rather than prerequisites for starting source development. |

For native builds, use the settings-copy command in the next section. Keep real filesystem paths in that ignored settings file. An empty `extra_plugins` list is correct only when there are no additional active Plugins directories. Builds and native tests need writable output and operating-system temporary directories; their storage and runtime depend on the selected pieces.

## Build a selected collection

Run these commands from the project folder containing `custom-pieces`. First type `python --version`; the printed version must be 3.11 or newer. Complete the environment setup above first. For a build-only environment, the minimum dependency and package commands are:

```sh
python -m pip install -r custom-pieces/requirements.txt
python -m pip install -e custom-pieces
```

The `-e` option registers the existing source folders, so later source edits remain visible to `python -m scp...` and `python -m scp_hsr...` commands. For 3D preview rendering, also run:

```sh
python -m pip install -r custom-pieces/requirements-preview.txt
```

1. List pieces and exact selection names:

   ```sh
   python custom-pieces/scp.py list
   ```

2. Record the Plugins folders, then check the installed NAM resources and identifier conflicts:

   Private `local/settings.json` records this computer's Plugins paths and is excluded from source exports. From the directory containing `custom-pieces/`, run this command in the active environment, then open `custom-pieces/local/settings.json` in a plain-text editor:

   ```sh
   python -c "from pathlib import Path; p=Path('custom-pieces/local/settings.json'); p.parent.mkdir(parents=True, exist_ok=True); p.open('x', encoding='utf-8').write(Path('custom-pieces/config/local.example.json').read_text(encoding='utf-8'))"
   ```

   The command creates the private directory and settings file. If the file already exists, it stops with `FileExistsError` and leaves your settings intact; open that existing file instead.

   Replace `/absolute/path/to/user/Plugins` with the actual user Plugins folder. In JSON, a Windows path can use forward slashes, for example `C:/Users/YourName/Documents/SimCity 4/Plugins`; replace `YourName` and the remaining folders with your actual path. Put any additional active Plugins folders in the `extra_plugins` list; use an empty list (`[]`) when there are none. Save the file, then type:

   ```sh
   python custom-pieces/scp.py doctor
   ```

   Alternatively, pass `--plugins` and repeat `--extra-plugins` for each additional active Plugins folder. Select the actual Plugins directories, not an entire game installation or Wine `dosdevices` folder.

3. Build and verify the default selection listed by `scp.py list`:

   ```sh
   python custom-pieces/scp.py build --progress
   python custom-pieces/scp.py verify
   ```

4. Create a development ZIP:

   ```sh
   python custom-pieces/scp.py package
   ```

   The result is `custom-pieces/dist/Simons-Custom-Pieces-development.zip`. Building and packaging do not install the plugin.

To select both accepted T junctions instead, use:

```sh
python custom-pieces/scp.py build --set smooth-t-junctions --progress --output custom-pieces/dist/smooth-t-junctions
python custom-pieces/scp.py verify --output custom-pieces/dist/smooth-t-junctions
python custom-pieces/scp.py package --output custom-pieces/dist/smooth-t-junctions
```

Use `--set redesigned-junction-example` for the straight T alone or `--set redesigned-diagonal-junction-example` for the diagonal T alone. Repeat `--set` to combine named selections. Alternatively, repeat `--include EXACT-PIECE-ID` to select individual pieces. Explicit selections replace the default; do not combine `--set`, `--include`, and `--all` in one command. An unknown name fails instead of silently using another selection.

Use a named selection or individual `--include` options to build a smaller development candidate; `--all` selects every current piece. To build all current reusable components, run:

```sh
python custom-pieces/scp.py build --set hsr-all-components --progress --output custom-pieces/dist/hsr-all-components
python custom-pieces/scp.py verify --output custom-pieces/dist/hsr-all-components
```

## Optional isolated native inputs

This is an optional private copy of selected game archives. Ordinary builds can read the installed Plugins directories directly. An isolated copy is useful for repeatable checks or rendering without scanning unrelated mods; it does not replace a game installation or establish game compatibility.

### Prepare a new private copy

1. Complete the private Plugins settings and run `doctor` as described above. Locate the four core archives under the profile's `controller`, `hsr`, `urail`, and `glr` keys within those configured Plugins directories. This six-file preparation procedure does not require every optional entry in the profile's `files` table. If more than one candidate exists, resolve the ambiguity before copying anything.
2. For the current HSR overview work, also locate `High Speed Rail_Textures.dat` and `NetworkAddonMod_GroundLightRail_Plugin_Textures.dat`. These are texture providers. Their full-file fingerprints are not declared by the public core profile, and `doctor` does not certify them. Preserve which source files you selected; later rendering and freshness checks still need their exact texture inputs.
3. Create a new private directory. This command stops if the `Plugins` directory already exists:

   ```sh
   python -c "from pathlib import Path; Path('custom-pieces/local/validation-inputs/Plugins').mkdir(parents=True)"
   ```

4. In Finder or File Explorer, copy the selected archive files into that new `Plugins` directory. Leave the original installed files where they are. Copy only the four core files and the two texture providers listed above for this six-file set.
5. Print each source and copied file's fingerprint using the command below. Replace the last quoted argument with the file you are checking, and repeat for all six files. Source and copied fingerprints must agree. For each of the four core files, also compare the result with its `sha256` in the public NAM profile.

   ```sh
   python -c "import hashlib, sys; from pathlib import Path; p=Path(sys.argv[1]); print(hashlib.sha256(p.read_bytes()).hexdigest(), p.name)" "custom-pieces/local/validation-inputs/Plugins/NetworkAddonMod_Controller.dat"
   ```

6. After those comparisons pass, record the selected private files with this command. It creates `sources.json` once and refuses to overwrite an existing record:

   ```sh
   python -c "import hashlib, json; from pathlib import Path; r=Path('custom-pieces/local/validation-inputs'); files=[{'file':p.name, 'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted((r/'Plugins').glob('*.dat'))]; (r/'sources.json').open('x', encoding='utf-8').write(json.dumps({'purpose':'Private copied input fingerprints; not a new compatibility approval.', 'files':files}, indent=2)+chr(10))"
   ```

This record stores fingerprints of the copied files; it is not another compatibility baseline and does not approve different archives. Keep the directory, its record, and all game binaries out of Git. Never replace an existing fingerprint record just to conceal changed inputs.

If a selected piece declares optional captured dependencies, prepare them separately by following that piece's README before building it. For example, [HSR above parallel Road](../domains/high-speed-rail/00_pieces/blind-hsr-road-stack/README.md#native-inputs-and-source-reproduction) needs two narrow ordinary-Road captures in addition to the core inputs. These captures are separate files with their own pinned profile hashes and source-audit records. Do not copy a full unrelated Road override into the six-file directory or change the core-copy procedure to require optional inputs for every piece. Pass the prepared capture directory explicitly through `--extra-plugins` when building or checking that selected piece.

### Transfer an existing private copy

Copy the complete `custom-pieces/local/validation-inputs/` directory, including `Plugins/` and the existing `sources.json`, into the same relative location in the new checkout. Run the following command from the directory containing `custom-pieces/`. It checks every recorded file against the original record, rejects filenames containing a directory, and compares only the four core records (`controller`, `hsr`, `urail`, and `glr`) with the public NAM profile. Optional piece-specific capture entries are not required by this core transfer check. Any mismatch produces an unsuccessful exit:

```sh
python -c "import hashlib, json; from pathlib import Path; r=Path('custom-pieces/local/validation-inputs'); files=json.loads((r/'sources.json').read_text(encoding='utf-8'))['files']; bad=[f['file'] for f in files if not Path(f['file']).name==f['file'] or not hashlib.sha256((r/'Plugins'/f['file']).read_bytes()).hexdigest()==f['sha256']]; recorded={f['file']:f['sha256'] for f in files}; profile=json.loads(Path('custom-pieces/config/profiles/nam50-rhd.json').read_text(encoding='utf-8'))['files']; core=[profile[key] for key in ('controller','hsr','urail','glr')]; baseline=[f['filename'] for f in core if not recorded.get(f['filename'])==f['sha256']]; print('Changed or unsafe records:', bad, 'Missing or mismatched core inputs:', baseline); raise SystemExit(1 if bad or baseline else 0)"
```

A missing file or unreadable record is a failure to investigate. The two texture providers remain private captured inputs, rather than entries in the public core baseline. Transfer any separate optional capture directory only when the selected piece requires it, and verify those captures against their own pinned profile hashes and source-audit records. Preserve the old directories until the transfer has been checked.

### Select isolated inputs explicitly

Connector rendering prefers `local/validation-inputs/Plugins/` when it exists. Incomplete or outdated copies can therefore affect checks even while live Plugins settings are correct. Some native tests also read `extra_plugins` from private settings when `SCP_TEST_NAM_PLUGINS` selects another primary directory; that environment variable alone does not establish a fully isolated scan.

For isolated native checks, use a separate test checkout. Set its private `plugins` value to the full path of its copied `local/validation-inputs/Plugins/`, and set `extra_plugins` to `[]`. Ensure that `SCP_PLUGINS` and `SCP_TEST_NAM_PLUGINS` are unset or select that same directory. Run the normal native checks there. Do not change the working installation's scan roots merely to obtain a passing report.

Rendering records the actual fonts, Pillow, NumPy, and renderer inputs. The renderer uses system Arial and Menlo where available, with fallback fonts otherwise. A different machine can therefore report stale artwork without a missing dependency. Follow the [documentation-generation workflow](WORKFLOW_DOCUMENTATION_GENERATION.md) to investigate or deliberately refresh presentation; do not rewrite evidence fingerprints to bypass a mismatch.

## Rebuild generated development outputs

If you need a complete replacement for an existing installation, rebuild all retained types, rather than assuming the default selection contains them:

```sh
python custom-pieces/scp.py build --all --progress --output custom-pieces/dist/current
python custom-pieces/scp.py verify --output custom-pieces/dist/current
```

Run these commands from the repository root. Building and verification do not install anything. The installer rejects a replacement that omits an installed piece, so a smaller default build is not automatically a replacement for a larger installed selection. A rebuild must be checked against the intended source and inputs; it does not inherit manual game approval from an older build.

The optional saved-resource checks for the V4 assembly use a separate build, which can be prepared deliberately when needed:

```sh
python custom-pieces/scp.py build --set hsr-straight-stem-trumpet-v4 --progress --output custom-pieces/dist/straight-stem-trumpet-v4
python custom-pieces/scp.py verify --output custom-pieces/dist/straight-stem-trumpet-v4
```

Keep original evidence and archived builds intact when they are needed to interpret recorded observations. Neither a new clone nor a fresh build requires copying old review workspaces, disposable reports, or Python caches into the active checkout.

## Install, remove, or roll back a test build

Use a disposable city. Save and quit SimCity 4 first. Keep backups outside all Plugins folders. In the commands below, replace `/absolute/path/to/SCP Backups` with a real backup directory, keep the quotation marks, and use the same directory for rollback. On Windows, a full path can use a drive letter, such as `C:/SCP Backups`. For example:

```sh
python custom-pieces/scp.py install --output custom-pieces/dist/smooth-t-junctions --backup-root '/absolute/path/to/SCP Backups'
```

The installer checks exact NAM fingerprints and current files. It prints a `backup_id`; save that value if you may need rollback. Start the game, open **Transportation → Rail**, and hover over a teal **SCP** button to read its full title. Click the button; use **Home** or **End** to rotate; click clear terrain once to place the piece. **Tab** and **Shift+Tab** select the next or previous type in a declared construction family. Normal SCP builds give each type its own family, so Tab does not provide a catalogue of other SCP types. Directional pieces repeat four proper rotations across their eight rotation states so reflection cannot silently reverse travel direction.

Existing sc4pac DLL shortcuts are supported when each points to a regular Windows DLL inside an explicitly scanned Plugins folder. A DLL is a Windows code library. The installer leaves these shortcuts and their targets intact. Linked folders, linked game-resource archives, broken links, and DLL shortcuts pointing outside the scanned folders remain blocked.

Join only matching track width, direction, height, and endpoint shape. Extend narrow tracks with matching SCP fillers and use split/merge pieces to connect them to native two-track lines. A route crossing another route inside the same tile needs a combined crossing containing both paths; placing an upper track on an occupied tile can replace its lower track.

To restore a snapshot, replace `BACKUP-ID-FROM-INSTALL` with the printed value:

```sh
python custom-pieces/scp.py rollback --backup-root '/absolute/path/to/SCP Backups' --backup-id BACKUP-ID-FROM-INSTALL
```

To remove the managed plugin:

```sh
python custom-pieces/scp.py uninstall --backup-root '/absolute/path/to/SCP Backups'
```

Removal checks its ownership receipt and saves a snapshot first. The tools do not edit city files or NAM's original archives.

## Try the trumpet menu experiment

This optional experiment presents the fourteen unique reusable types in `straight-stem-trumpet-v4` in two ways: **SCP | TEST | Trumpet V4 - cycle parts** selects the first component and uses Tab/Shift+Tab to change types; **SCP | TEST | Trumpet V4 - individual parts** opens a submenu containing one named button per type. Each individual button should start on its named type, and Tab then follows the same shared family. Home/End rotate the current type. Neither entry point places the complete assembly.

The domain's [menu-layout.json](../domains/high-speed-rail/menu-layout.json) owns the experimental presentation names, locally reserved IDs, and assembly selection. Piece definitions retain their permanent IDs and capabilities. The type order follows first use in the assembly's placement plan, with repeated copies appearing only once. Normal builds do not read this opt-in layout and keep their existing menu arrangement.

From the project directory, build from an existing verified selection that contains the assembly's components and every installed SCP type you need to retain. The commands below use `dist/current` for that selection; the experiment preserves its types and changes only the menu archive and the controller's generated ordering rows:

```sh
python custom-pieces/scp.py menu-test --source custom-pieces/dist/current --output custom-pieces/dist/trumpet-menu-test
python custom-pieces/scp.py verify --output custom-pieces/dist/trumpet-menu-test
python custom-pieces/scp.py package --output custom-pieces/dist/trumpet-menu-test --destination custom-pieces/dist/trumpet-menu-test.zip
```

The output directory must not already exist. Choose a new descriptive test-build name for another run. The builder verifies the original selection, checks the new presentation IDs against active Plugins, preserves every component DAT and NetworkINI, and packages the original manifest and two original archives as proof outside the installable folder. Those reference archives use `.proof` filenames so the game cannot discover them as additional plugins. The experimental verifier reconstructs the original build for the normal strict verification, then checks the exact allowed menu/controller changes and actual encoded submenu properties and type order. Experimental packages retain this frozen evidence and do not support `--refresh-docs` or public release. Building and packaging do not install anything.

The game needs Submenus DLL, its documented dependencies, and `submenu-essentials.dat`; [the upstream instructions](https://github.com/memo33/submenus-dll#installation) own those requirements. The builder does not install DLLs. After saving and fully quitting SimCity 4, install the complete candidate through the existing receipt-based installer:

```sh
python custom-pieces/scp.py install --output custom-pieces/dist/trumpet-menu-test --backup-root '/absolute/path/to/SCP Backups'
```

Save the returned `backup_id`. Open a disposable city, open **Transportation → Rail**, and test both named entries. Read `docs/menu-experiment/README.md` inside the build for the exact type order and controls; its adjacent `game-checks.json` lists the unverified observations at packaging time. Check both presentations of the first type, every individual starting type, forward and reverse cycling, rotation, cancellation, placement, and save/reload. Static validation cannot prove the game's handling of two presentations sharing one construction target. Record actual failures or explicit successes with the installed build fingerprint and game/DLL environment; do not infer piece traffic or complete-assembly approval from menu behavior. Restore the previous complete selection with the [rollback command](#install-remove-or-roll-back-a-test-build) and saved backup ID.

## Project files and future additions

See [STRUCTURE.md](../STRUCTURE.md) for the full source map.

Create an unfinished entry with:

```sh
python custom-pieces/scp.py scaffold --domain high-speed-rail --id my-new-crossing --name "My New Crossing" --width 1 --depth 2
```

The scaffold creates a disabled **draft** and allocates its local identifiers. It does not invent geometry or traffic paths. Implement generation, independent checks, icon, preview, and joining documentation before marking it experimental. The [authoring guide](WORKFLOW_PIECE_CREATION.md) explains each step.

A **DAT** is the game's archive of models, traffic paths, menu records, and other resources. Every build combines all selected pieces into one coordinated controller overlay, one SCP menu archive, and one DAT per piece. Output is staged and verified before a managed build is replaced. Do not remove a piece DAT manually from a build; rebuild its intended selection so menus and rules stay consistent. Builds refuse arbitrary output folders and identifier collisions. Installation receipts, backups, and rollback protect managed files.

## Check and prepare distribution

For a local candidate whose final README, artwork, and connector exports are ready, follow the [final-artifact procedure](WORKFLOW_DOCUMENTATION_GENERATION.md#final-artifacts-and-packaging), then package its existing verified build with current documentation. Replace `BUILD_NAME` with that build directory:

```sh
python custom-pieces/scp.py package --output custom-pieces/dist/BUILD_NAME --destination custom-pieces/dist/BUILD_NAME-current-docs.zip --refresh-docs
```

The command preserves the input build and its compiled resources, and writes the current portable documentation plus matching hashes into the ZIP. Omitting `--refresh-docs` deliberately packages the original build-time documentation snapshot. Packaging remains separate from publication and records no game observation.

```sh
python custom-pieces/scp.py check --scope all
python custom-pieces/scp.py release-check --all
python custom-pieces/scp.py source-package
```

Real-NAM tests run when their supported local inputs are available; skipped cases must be reported as skips. Software checks inspect encoded traffic paths, models, walls, supports, references, construction rules, and packaging. Actual placement, traffic, long-car overhang, terrain, shadows, demolition, and save/reload still need game testing for the exact packaged bytes.

The source ZIP excludes private settings, build output, NAM binaries, caches, and backups. It is a development export. Public binary release remains blocked until public identifier allocation, NAM-derived asset permission, game/platform tests, and publication materials are recorded. See [RELEASE.md](RELEASE.md). No build or packaging command uploads anything to Simtropolis.

Reusable component names describe their function and level. Their standalone pictures use a local **(X0,Y0)** grid at **0°**, without assembly P-labels. The current [V4 guide](../domains/high-speed-rail/01_assemblies/straight-stem-trumpet-v4/README.md) shows **14 unique type pictures** and a separate **26-placement** table. Its six assembly views retain the fixed global X/Y grid and P-labels. Build it with `--set hsr-straight-stem-trumpet-v4`; earlier trumpet definitions and their exclusive pieces are no longer part of the current source.


Read [TESTING.md](TESTING.md) to record a real preview or game observation. Checkboxes are generated from scoped JSON records; do not edit them directly.
