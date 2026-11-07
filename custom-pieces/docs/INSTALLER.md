---
title: "Install SCP without Python"
summary: "Select Plugins, install the finished SCP catalogue with the compact Windows installer, or prepare a verified review package."
audience: "Players"
document_type: "procedure"
---

# Install SCP without Python

<!-- BEGIN DOCUMENT NAVIGATION -->
[1. Check the game installation](#1-check-the-game-installation) · [2. Download the matching ZIP](#2-download-the-matching-zip) · [3. Select the Plugins folder](#3-select-the-plugins-folder) · [4. Install and find the pieces](#4-install-and-find-the-pieces) · [5. Update, remove, or resolve a stopped installation](#5-update-remove-or-resolve-a-stopped-installation) · [6. What a successful installer check establishes](#6-what-a-successful-installer-check-establishes) · [7. Prepare a prebuilt installer for review](#7-prepare-a-prebuilt-installer-for-review)
<!-- END DOCUMENT NAVIGATION -->

The **SCP Installer** installs Simon's Custom Pieces. You do not need Python, Git, a terminal, or a separate resource-capture tool to use it. A **prebuilt installer** includes the finished SCP game files and checks that you have the exact game and Network Addon Mod (NAM) files they require. Its compact Windows application copies those finished files into the Plugins folder you select. A separate source-builder installer remains available for developer checks and creates game files from the installed game and NAM.

The installer selects **every implemented piece in its bundled catalogue** and prepares the Rail trumpet and Highway assembly buttons. **Experimental** means the software checks do not establish correct operation inside the game. Existing failed, stale, and unverified observations remain visible in the [library inventories](../README.md). Check a subject's guide and testing record before using it in an important city.

## 1. Check the game installation

Install SimCity 4 Deluxe and NAM before running SCP. The currently audited game profile is **SimCity 4 Deluxe for Windows, version 1.1.641, NAM 50, and right-hand traffic**. Right-hand traffic means vehicles drive on the right. The installer checks exact resource fingerprints, meaning identifiers calculated from file contents, rather than accepting a NAM version label alone.

The download runs on **64-bit Windows with an Intel or AMD processor**. The [profile](../config/profiles/nam50-rhd.jsonc) records the supported game resources. The installer cannot add a missing game, install NAM, or convert an unsupported game profile automatically.

Close SimCity 4 before installing or updating SCP. Keep a backup of any city you intend to use for experimental pieces. The prebuilt installer checks and copies the finished catalogue without generating its models, traffic paths, menus, or controller on your computer. The progress display identifies the current stage.

## 2. Download the matching ZIP

Open the repository's [Releases page](https://github.com/KomodorDev/sc4-simons-custom-pieces/releases), and choose the intended **SCP Installer — experimental** prerelease. A **prerelease** is a downloadable development version, rather than a claim that every piece has passed game testing. If no installer prerelease is listed, the release workflow has not produced an installer yet; the repository's **Source code** ZIP is a different download and requires the developer setup.

Download **`SCP-Installer-windows-x64-<commit>.zip`** for a published installer. A prebuilt release includes `release-record.json` among its GitHub assets. If you are reviewing a locally prepared candidate, use the private **`SCP-Installer-Prebuilt-Review-windows-x64-<commit>.zip`**. Both prebuilt ZIP types contain the Windows application, its bundled Python runtime, the finished SCP files, compact generated installation data, brief launcher instructions in `README.txt`, and required license notices. That data records the selected pieces, dependency checks, and package fingerprints. Repository guides, previews, development evidence, authoring tools, geometry libraries, and test suites stay in the repository and are excluded from the player download.

`<commit>` is the first 12 characters of the source revision recorded on that release. The ZIP has a matching `.zip.sha256` file, and the release includes a bundle index and installer self-test report tied to its exact source revision. A SHA-256 checksum detects different bytes; it does not establish game compatibility or replace publisher signing.

Right-click the downloaded ZIP, select **Extract All…**, keep the proposed destination under Downloads or choose another destination, and select **Extract**. Open the extracted directory, open **SCP Installer**, and double-click **SCP Installer.exe**. Keep its accompanying `_internal` directory beside the executable; it contains the bundled runtime and finished files. Extract the entire ZIP before opening the application.

For the audited catalogue, a rebuilt download of approximately **360 MB plus the application and its runtime** is an estimate. The finished game files account for most of that size. Read the actual asset size on the release page for the measured download size. Release checks enforce an extraction-path budget and extract the prebuilt ZIP under a realistic Windows Downloads destination before testing the extracted application.

<a id="first-launch-operating-system-approval"></a>

### 2.1 First-launch operating-system approval

The executable is not signed with a publisher certificate, so Windows may display an unrecognized-app warning. Confirm that you downloaded the intended asset from this repository's release. On a SmartScreen dialog that offers them, select **More info**, inspect the application name, and select **Run anyway** if you trust the download. Managed computers can prevent this option. Keep Windows Security enabled; see [Microsoft's explanation of app reputation](https://learn.microsoft.com/windows/apps/package-and-deploy/smartscreen-reputation).

<a id="3-select-the-game-folder"></a>

## 3. Select the Plugins folder

The **Plugins folder** is the directory that the game loads add-ons from. Select the existing player-data Plugins folder that you actually use, with the supported NAM installation already present. Its usual location is `Documents\SimCity 4\Plugins`; redirected Documents folders, including OneDrive locations, can use another path.

1. Select **Choose Plugins folder…** in the installer.
2. In the folder-selection window, open your actual SimCity 4 player-data directory, select **Plugins**, and select **Select Folder**. You may also select the player-data directory that contains Plugins. Select the folder used by your game, rather than creating an empty Plugins folder elsewhere.
3. Check the selected path shown in the installer, and select **Install**. The installer searches Windows' registered game locations for the original game files.
4. If the installer cannot identify one game installation, it displays **Choose game folder…**. Select that button, navigate to the original game directory containing `Apps`, `SimCity_1.dat`, `SimCity_2.dat`, and `SimCity_3.dat`, and select **Select Folder**. Select the containing directory, rather than `Apps` itself. Your Plugins selection is retained. Select **Install** again.

The installer reads the installed NAM archives and the original game archives required by its bundled catalogue. These include `SimCity_3.dat` for Road inputs and `SimCity_4.dat` for adaptive Avenue inputs. A sunlight capture from `SimCity_1.dat` is required only when a selected piece enables model-shadow carriers and declares that dependency. The current GHSR/DD RHW Alignments A and B and all fifteen parallel-diamond components disable those carriers and require no sunlight capture; see [the conditional input rule](BUILD_AND_INSTALL.md#34-prepare-the-parallel-highway-sunlight-input-for-source-builds).

A **dependency capture** is a small DAT containing required resources read from the original game or NAM. Compact generated installation data tells the installer which original files and resources to verify. Where needed, the installer creates these private dependency captures automatically in its working directory, outside Plugins. It does not rebuild the finished SCP catalogue. You do not need a resource-extraction tool, and the original archives remain unchanged. Missing, changed, ambiguous, or conflicting required inputs stop installation with an explanation.

For a developer source-builder installer, the first button remains **Choose game folder…**. Select the original game directory described in step 4. If the installer then asks for player data, select **Choose Plugins folder…**, select the existing player-data or Plugins folder, and select **Install** again. This developer mode performs the full catalogue build.

## 4. Install and find the pieces

Before selecting **Install**, copy `memo.submenus.dll` and `SC4ResourceLoadingHooks.dll` directly into either the game's Plugins folder or the player-data Plugins folder. Use Resource Loading Hooks version 2.0.1 or later. Place `submenu-essentials.dat` anywhere under either Plugins folder. These files let the game display the Rail and Highway SCP folders. The installer checks that the files are in the expected locations. [Submenus DLL installation instructions](https://github.com/memo33/submenus-dll#installation)

Check that the selected Plugins folder is correct, then select **Install**. The installer verifies the packaged files, checks the local dependencies and conflicts, backs up the previous SCP installation, and installs the finished pieces, menus, and controller. A failed check stops installation. Select **Open log** to inspect progress or a reported problem. **Cancel** requests a stop at the next checkpoint and becomes unavailable when the final installation transaction begins.

When the installer reports success, start SimCity 4. For standalone rail pieces, open **Transportation → Rail → SCP → Pieces**. For the trumpet, open **Transportation → Rail → SCP → Assemblies** and click **SCP | ASSEMBLY | HSR — Trumpet — Straight Stem**. The cycle contains 14 ordinary component selections and three terminal selections. Press **Tab** for the next selection or **Shift+Tab** for the previous one, and click once to place the selected component. Follow the placement table for the 26 positions. [Trumpet guide](../domains/high-speed-rail/01_assemblies/hsr-trumpet-straight-stem/README.md)

For standalone highway pieces, open **Transportation → Highways → SCP → Pieces**. For the diamond and Compact Y assembly buttons, open **Transportation → Highways → SCP → Assemblies**. Each assembly button has its own component cycle. [Menu layout and dependencies](BUILD_AND_INSTALL.md#81-required-scp-folder-layout)

The managed installation lives in **`zzz_Simons_Custom_Pieces` inside the selected Plugins folder**. It contains one combined SCP controller, one menu, the selected piece resources, and an ownership receipt. The receipt identifies the files the installer owns. Keep it intact. The installer's logs, dependency captures, transaction records, and backups stay under **`%LOCALAPPDATA%/SimonsCustomPieces/Installer`**, outside Plugins. `%LOCALAPPDATA%` is Windows' private application-data location for your user account; paste that complete path into File Explorer's address bar to open it. The installer does not replace NAM's original archives or modify city files.

## 5. Update, remove, or resolve a stopped installation

To update, close the game, download the intended newer installer, extract it, and select the same Plugins folder. Supply the same game directory if requested. The installer accepts existing receipts from earlier supported installers, verifies the owned files, saves a backup, and replaces the managed installation only after the new packaged files pass their checks. It refuses to overwrite unknown or edited files and refuses an update that silently removes previously installed piece types. Keep the installer's application-data directory if you need its logs or backup.

To reverse the latest successful installation, close the game, open the installer, select the same Plugins folder, supply the game directory if requested, and select **Undo last installation**. Read the confirmation, and select **Yes** to restore the previous managed SCP installation. If SCP was absent before that installation, undo removes its managed folder. The button is available when the installer has a saved transaction record; it does not offer a history of arbitrary versions. Existing file and backup checks can stop an undo if their contents have changed.

Before an undo removes any piece types, remove those placed pieces from every city that uses them, and save those cities. Removing the resources first can leave saved cities referring to pieces that are no longer present. The [source workflow provides receipt-based uninstall and rollback commands](BUILD_AND_INSTALL.md#7-install-remove-or-roll-back-a-test-build) for maintainers who need other removal or recovery operations.

A [30 October 2026 test](TESTING.md#6-existing-saves-after-piece-removal) confirmed that affected plots could be cleared after upgrading to a version that omitted their old piece resources. Visual artifacts were present before bulldozing and were gone afterward. This is a scoped cleanup result; it does not establish traffic operation or behavior after saving and reopening. Keep the precaution above and back up the complete region and matching old plugin before experimenting with removed types.

If installation stops, read the reported filename and reason. A resource fingerprint mismatch means the file differs from the audited profile; replacing the expected hash would bypass the check. A controller conflict means another loaded add-on supplies the same shared rules; it requires deliberate reconciliation. An ownership error means the existing SCP directory cannot be safely replaced. Preserve the reported log, and open a [repository issue](https://github.com/KomodorDev/sc4-simons-custom-pieces/issues) with the installer release, operating system, game edition, NAM version, and exact error. Remove personal filesystem paths from a log before posting it publicly. If the message includes **WinError 5**, preserve the complete error and the exact failing path in your private diagnostic copy; the error number alone does not establish its cause.

<a id="what-a-successful-installer-check-establishes"></a>

## 6. What a successful installer check establishes

The [release workflow](AUTOMATIC_RELEASES.md) packages the prebuilt Windows installer on GitHub after the Mac verifies the game assets. A **GUI startup smoke check** briefly opens and closes the application to check that the window can start. The packaged self-test exercises installation and Undo on disposable data. Packaging checks exclude development content from the prebuilt download, enforce a maximum extracted path length, and extract the complete ZIP under a realistic Windows Downloads destination. The extracted executable then runs its self-test and GUI startup check. These checks establish the tested package and destination; they do not explain an earlier unlogged Windows failure. Game observations, public identifier reservations, and redistribution permission remain separate [release requirements](RELEASE.md).

## 7. Prepare a prebuilt installer for review

A **payload** is the finished set of files the installer copies into Plugins. The preparation command generates the models, shadows, traffic paths, menus, and one combined controller from the exact supported inputs. It runs the existing saved-resource and assembly checks before exporting the install files and their fingerprints. The combined controller is prepared once against the pinned NAM controller fingerprint. The installer checks that the player's controller matches and installs SCP's overlay in its own folder.

1. Start from a clean, committed checkout of the library and prepare its Python environment. Open a terminal at the repository root. Identify the supported game folder containing `SimCity_3.dat` and the player's Plugins folder containing NAM. [Python setup instructions](https://github.com/KomodorDev/sc4-simons-custom-pieces/blob/dev/README.md#2-prepare-python-and-run-the-tests)
2. Run the command below. Replace `<game folder>` and `<player Plugins>` with those two paths, keeping the quotation marks. Both output directories are under the ignored private `local/` directory. Choose a new payload directory for a later build. The command reports the full source commit and the payload location when the export passes.

   ```sh
   python -B custom-pieces/installer/prepare_payload.py --game-folder "<game folder>" --player-data "<player Plugins>" --work-dir custom-pieces/local/prebuilt-work --output custom-pieces/local/prebuilt-payload
   ```

3. On a 64-bit Windows machine with an Intel or AMD processor, check out the same source commit and copy the prepared payload to a private directory. Run the following commands from the repository root. Replace `<full commit>` with the 40-character source commit reported in step 2, and replace `<payload directory>` with the path to the copied payload. The build command checks the source revision, package contents, packaged self-test, and application startup before producing the review ZIP.

   ```powershell
   python -m pip install -r custom-pieces/requirements-installer.txt
   python -B custom-pieces/installer/build_bundle.py build --output custom-pieces/local/prebuilt-windows --source-commit "<full commit>" --platform windows-x64 --prebuilt-payload "<payload directory>"
   ```

4. Extract the **SCP-Installer-Prebuilt-Review** ZIP and follow chapters 1 through 5 using a disposable Windows installation of the supported profile. Leave the normal Downloads extraction destination in place, and confirm extraction completes. Verify a first installation, a repeat installation, an update from the previous supported installer, and **Undo last installation** using disposable data. Confirm that failed dependency, checksum, and conflict checks preserve the existing installation. Record the exact Windows version, extraction destination, elapsed times, and results, and confirm the log contains the prebuilt verification and installation stages. Keep the ZIP and compiled payload private during review. [Public release requirements](RELEASE.md#5-gates-for-a-public-package)
