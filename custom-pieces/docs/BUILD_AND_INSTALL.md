---
title: "Build, install and inspect SCP"
summary: "Explain the complete current build, installation, packaging and verification commands for human operators."
audience: "Players, authors, and maintainers"
document_type: "procedure"
---

# Build, install and inspect SCP


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

The Git checkout supplies maintained source, canonical artwork, schemas, tests, and recorded evidence. Follow the repository's [Python setup](../../README.md#prepare-python-and-run-the-tests) to create a virtual environment and install its dependencies. A **template** is an example file that each contributor copies and fills in for their own machine. A fresh checkout can run the portable test suites without a game installation; cases requiring native game resources or saved builds report explicit skips.

| Item | Provided in Git | Local use |
| --- | --- | --- |
| Workstation settings | [`config/local.example.json`](../config/local.example.json) | Copy to ignored `custom-pieces/local/settings.json`, then supply every active Plugins directory. |
| Supported NAM input identities | [`config/profiles/nam50-rhd.json`](../config/profiles/nam50-rhd.json) | The filenames and SHA-256 fingerprints identify the exact supported core archives. A fingerprint checks file contents; it is not a download or a substitute archive. |
| Python dependencies and package definitions | Root `requirements-ci.txt`, library requirements, and `pyproject.toml` | Install them in a newly created environment for this checkout. Do not copy an old environment. |
| Isolated native inputs | No game archives | Optional private copies under `custom-pieces/local/validation-inputs/` support repeatable texture and verification work. Keep their provenance with them. |
| Compiled builds, packages, and caches | No generated build templates | Generate them from source and matching NAM inputs. Existing `dist/` directories are convenient retained outputs, rather than prerequisites for starting source development. |

For native builds, each contributor supplies the supported NAM installation and uses the settings-copy commands in the next section. Keep real filesystem paths in the ignored settings file. An empty `extra_plugins` list is correct only when there are no additional active Plugins directories. The `doctor` command verifies the selected dependencies and checks identifier conflicts; do not change recorded dependency fingerprints merely to make a different installation pass.

An isolated input directory is useful but optional. Connector rendering prefers `local/validation-inputs/Plugins/` when it exists, so incomplete or outdated copies can affect checks. Some native tests also read `extra_plugins` from private settings even when `SCP_TEST_NAM_PLUGINS` selects another primary directory. That environment variable alone does not establish a fully isolated scan.

## Build a selected collection

Run these commands from the project folder containing `custom-pieces`. First type `python3 --version`; the printed version must be 3.11 or newer. On the first use of a source checkout, install the Python dependencies and register its shared and domain packages:

```sh
python3 -m pip install -r custom-pieces/requirements.txt
python3 -m pip install -e custom-pieces
```

The `-e` option registers the existing source folders, so later source edits remain visible to `python3 -m scp...` and `python3 -m scp_hsr...` commands. For 3D preview rendering, also run:

```sh
python3 -m pip install -r custom-pieces/requirements-preview.txt
```

1. List pieces and exact selection names:

   ```sh
   python3 custom-pieces/scp.py list
   ```

2. Record the Plugins folders, then check the installed NAM resources and identifier conflicts:

   Private `local/settings.json` records this computer's Plugins paths and is excluded from source exports. On a new computer, open Terminal in the project directory, type the following two commands, then open the resulting file in a text editor:

   ```sh
   mkdir -p custom-pieces/local
   cp custom-pieces/config/local.example.json custom-pieces/local/settings.json
   ```

   Replace `/absolute/path/to/user/Plugins` with the actual user Plugins folder. Put any additional active Plugins folders in the `extra_plugins` list; use an empty list (`[]`) when there are none. Save the file, then type:

   ```sh
   python3 custom-pieces/scp.py doctor
   ```

   Alternatively, pass `--plugins` and repeat `--extra-plugins` for each additional active Plugins folder. Select the actual Plugins directories, not an entire game installation or Wine `dosdevices` folder.

3. Build and verify the default selection listed by `scp.py list`:

   ```sh
   python3 custom-pieces/scp.py build --progress
   python3 custom-pieces/scp.py verify
   ```

4. Create a development ZIP:

   ```sh
   python3 custom-pieces/scp.py package
   ```

   The result is `custom-pieces/dist/Simons-Custom-Pieces-development.zip`. Building and packaging do not install the plugin.

To select both accepted T junctions instead, use:

```sh
python3 custom-pieces/scp.py build --set smooth-t-junctions --progress --output custom-pieces/dist/smooth-t-junctions
python3 custom-pieces/scp.py verify --output custom-pieces/dist/smooth-t-junctions
python3 custom-pieces/scp.py package --output custom-pieces/dist/smooth-t-junctions
```

Use `--set redesigned-junction-example` for the straight T alone or `--set redesigned-diagonal-junction-example` for the diagonal T alone. Repeat `--set` to combine named selections. Alternatively, repeat `--include EXACT-PIECE-ID` to select individual pieces. Explicit selections replace the default; do not combine `--set`, `--include`, and `--all` in one command. An unknown name fails instead of silently using another selection.

Use a named selection or individual `--include` options to build a smaller development candidate; `--all` selects every current piece. To build all current reusable components, run:

```sh
python3 custom-pieces/scp.py build --set hsr-all-components --progress --output custom-pieces/dist/hsr-all-components
python3 custom-pieces/scp.py verify --output custom-pieces/dist/hsr-all-components
```

## Rebuild generated development outputs

If you need a complete replacement for an existing installation, rebuild all retained types, rather than assuming the default selection contains them:

```sh
python3 custom-pieces/scp.py build --all --progress --output custom-pieces/dist/current
python3 custom-pieces/scp.py verify --output custom-pieces/dist/current
```

Run these commands from the repository root. Building and verification do not install anything. The installer rejects a replacement that omits an installed piece, so a smaller default build is not automatically a replacement for a larger installed selection. A rebuild must be checked against the intended source and inputs; it does not inherit manual game approval from an older build.

The optional saved-resource checks for the V4 assembly use a separate build, which can be prepared deliberately when needed:

```sh
python3 custom-pieces/scp.py build --set hsr-straight-stem-trumpet-v4 --progress --output custom-pieces/dist/straight-stem-trumpet-v4
python3 custom-pieces/scp.py verify --output custom-pieces/dist/straight-stem-trumpet-v4
```

Keep original evidence and archived builds intact when they are needed to interpret recorded observations. Neither a new clone nor a fresh build requires copying old review workspaces, disposable reports, or Python caches into the active checkout.

## Install, remove, or roll back a test build

Use a disposable city. Save and quit SimCity 4 first. Keep backups outside all Plugins folders. For example:

```sh
python3 custom-pieces/scp.py install --output custom-pieces/dist/smooth-t-junctions --backup-root "$HOME/Documents/Simons Custom Pieces Backups"
```

The installer checks exact NAM fingerprints and current files. It prints a `backup_id`; save that value if you may need rollback. Start the game, open **Transportation → Rail**, and hover over a teal **SCP** button to read its full title. Click the button; use **Home** or **End** to rotate; click clear terrain once to place the piece. **Tab** and **Shift+Tab** select the next or previous type in a declared construction family. Normal SCP builds give each type its own family, so Tab does not provide a catalogue of other SCP types. Directional pieces repeat four proper rotations across their eight rotation states so reflection cannot silently reverse travel direction.

Existing sc4pac DLL shortcuts are supported when each points to a regular Windows DLL inside an explicitly scanned Plugins folder. A DLL is a Windows code library. The installer leaves these shortcuts and their targets intact. Linked folders, linked game-resource archives, broken links, and DLL shortcuts pointing outside the scanned folders remain blocked.

Join only matching track width, direction, height, and endpoint shape. Extend narrow tracks with matching SCP fillers and use split/merge pieces to connect them to native two-track lines. A route crossing another route inside the same tile needs a combined crossing containing both paths; placing an upper track on an occupied tile can replace its lower track.

To restore a snapshot, replace `BACKUP-ID-FROM-INSTALL` with the printed value:

```sh
python3 custom-pieces/scp.py rollback --backup-root "$HOME/Documents/Simons Custom Pieces Backups" --backup-id BACKUP-ID-FROM-INSTALL
```

To remove the managed plugin:

```sh
python3 custom-pieces/scp.py uninstall --backup-root "$HOME/Documents/Simons Custom Pieces Backups"
```

Removal checks its ownership receipt and saves a snapshot first. The tools do not edit city files or NAM's original archives.

## Try the trumpet menu experiment

This optional experiment presents the fourteen unique reusable types in `straight-stem-trumpet-v4` in two ways: **SCP | TEST | Trumpet V4 - cycle parts** selects the first component and uses Tab/Shift+Tab to change types; **SCP | TEST | Trumpet V4 - individual parts** opens a submenu containing one named button per type. Each individual button should start on its named type, and Tab then follows the same shared family. Home/End rotate the current type. Neither entry point places the complete assembly.

The domain's [menu-layout.json](../domains/high-speed-rail/menu-layout.json) owns the experimental presentation names, locally reserved IDs, and assembly selection. Piece definitions retain their permanent IDs and capabilities. The type order follows first use in the assembly's placement plan, with repeated copies appearing only once. Normal builds do not read this opt-in layout and keep their existing menu arrangement.

From the project directory, build from an existing verified selection that contains the assembly's components and every installed SCP type you need to retain. The commands below use `dist/current` for that selection; the experiment preserves its types and changes only the menu archive and the controller's generated ordering rows:

```sh
python3 custom-pieces/scp.py menu-test --source custom-pieces/dist/current --output custom-pieces/dist/trumpet-menu-test
python3 custom-pieces/scp.py verify --output custom-pieces/dist/trumpet-menu-test
python3 custom-pieces/scp.py package --output custom-pieces/dist/trumpet-menu-test --destination custom-pieces/dist/trumpet-menu-test.zip
```

The output directory must not already exist. Choose a new descriptive test-build name for another run. The builder verifies the original selection, checks the new presentation IDs against active Plugins, preserves every component DAT and NetworkINI, and packages the original manifest and two original archives as proof outside the installable folder. Those reference archives use `.proof` filenames so the game cannot discover them as additional plugins. The experimental verifier reconstructs the original build for the normal strict verification, then checks the exact allowed menu/controller changes and actual encoded submenu properties and type order. Experimental packages retain this frozen evidence and do not support `--refresh-docs` or public release. Building and packaging do not install anything.

The game needs Submenus DLL, its documented dependencies, and `submenu-essentials.dat`; [the upstream instructions](https://github.com/memo33/submenus-dll#installation) own those requirements. The builder does not install DLLs. After saving and fully quitting SimCity 4, install the complete candidate through the existing receipt-based installer:

```sh
python3 custom-pieces/scp.py install --output custom-pieces/dist/trumpet-menu-test --backup-root "$HOME/Documents/Simons Custom Pieces Backups"
```

Save the returned `backup_id`. Open a disposable city, open **Transportation → Rail**, and test both named entries. Read `docs/menu-experiment/README.md` inside the build for the exact type order and controls; its adjacent `game-checks.json` lists the unverified observations at packaging time. Check both presentations of the first type, every individual starting type, forward and reverse cycling, rotation, cancellation, placement, and save/reload. Static validation cannot prove the game's handling of two presentations sharing one construction target. Record actual failures or explicit successes with the installed build fingerprint and game/DLL environment; do not infer piece traffic or complete-assembly approval from menu behavior. Restore the previous complete selection with the [rollback command](#install-remove-or-roll-back-a-test-build) and saved backup ID.

## Project files and future additions

See [STRUCTURE.md](../STRUCTURE.md) for the full source map.

Create an unfinished entry with:

```sh
python3 custom-pieces/scp.py scaffold --domain high-speed-rail --id my-new-crossing --name "My New Crossing" --width 1 --depth 2
```

The scaffold creates a disabled **draft** and allocates its local identifiers. It does not invent geometry or traffic paths. Implement generation, independent checks, icon, preview, and joining documentation before marking it experimental. The [authoring guide](WORKFLOW_PIECE_CREATION.md) explains each step.

A **DAT** is the game's archive of models, traffic paths, menu records, and other resources. Every build combines all selected pieces into one coordinated controller overlay, one SCP menu archive, and one DAT per piece. Output is staged and verified before a managed build is replaced. Do not remove a piece DAT manually from a build; rebuild its intended selection so menus and rules stay consistent. Builds refuse arbitrary output folders and identifier collisions. Installation receipts, backups, and rollback protect managed files.

## Check and prepare distribution

For a local candidate whose final README, artwork, and connector exports are ready, follow the [final-artifact procedure](WORKFLOW_DOCUMENTATION_GENERATION.md#final-artifacts-and-packaging), then package its existing verified build with current documentation. Replace `BUILD_NAME` with that build directory:

```sh
python3 custom-pieces/scp.py package --output custom-pieces/dist/BUILD_NAME --destination custom-pieces/dist/BUILD_NAME-current-docs.zip --refresh-docs
```

The command preserves the input build and its compiled resources, and writes the current portable documentation plus matching hashes into the ZIP. Omitting `--refresh-docs` deliberately packages the original build-time documentation snapshot. Packaging remains separate from publication and records no game observation.

```sh
python3 custom-pieces/scp.py check --scope all
python3 custom-pieces/scp.py release-check --all
python3 custom-pieces/scp.py source-package
```

Real-NAM tests run when their supported local inputs are available; skipped cases must be reported as skips. Software checks inspect encoded traffic paths, models, walls, supports, references, construction rules, and packaging. Actual placement, traffic, long-car overhang, terrain, shadows, demolition, and save/reload still need game testing for the exact packaged bytes.

The source ZIP excludes private settings, build output, NAM binaries, caches, and backups. It is a development export. Public binary release remains blocked until public identifier allocation, NAM-derived asset permission, game/platform tests, and publication materials are recorded. See [RELEASE.md](RELEASE.md). No build or packaging command uploads anything to Simtropolis.

Reusable component names describe their function and level. Their standalone pictures use a local **(X0,Y0)** grid at **0°**, without assembly P-labels. The current [V4 guide](../domains/high-speed-rail/01_assemblies/straight-stem-trumpet-v4/README.md) shows **14 unique type pictures** and a separate **26-placement** table. Its six assembly views retain the fixed global X/Y grid and P-labels. Build it with `--set hsr-straight-stem-trumpet-v4`; earlier trumpet definitions and their exclusive pieces are no longer part of the current source.


Read [TESTING.md](TESTING.md) to record a real preview or game observation. Checkboxes are generated from scoped JSON records; do not edit them directly.
