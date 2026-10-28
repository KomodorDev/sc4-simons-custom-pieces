---
title: "Install SCP without Python"
summary: "Download the experimental Windows installer, select the game folder, and build and install the complete implemented catalogue locally."
audience: "Players"
document_type: "procedure"
---

# Install SCP without Python

The **SCP Installer** includes the programs needed to build and install Simon's Custom Pieces. You do not need Python, Git, a terminal, or a separate resource-capture tool. It builds from your own installed SimCity 4 and Network Addon Mod (NAM) resources; the download does not include those resources.

The installer selects **every implemented piece in its bundled catalogue**, currently **168 experimental types**, and prepares the trumpet's assembly button. **Experimental** means the software checks do not establish correct operation inside the game. Existing failed, stale, and unverified observations remain visible in the [piece inventory](../domains/high-speed-rail/00_pieces/INVENTORY.md) and [assembly inventory](../domains/high-speed-rail/01_assemblies/INVENTORY.md). Check a subject's guide and testing record before using it in an important city.

## 1. Check the game installation

Install SimCity 4 Deluxe and NAM before running SCP. The currently audited game profile is **SimCity 4 Deluxe for Windows, version 1.1.641, NAM 50, and right-hand traffic**. Right-hand traffic means vehicles drive on the right. The installer checks exact resource fingerprints, meaning identifiers calculated from file contents, rather than accepting a NAM version label alone.

The download runs on **64-bit Windows with an Intel or AMD processor**. The [profile](../config/profiles/nam50-rhd.json) records the supported game resources. The installer cannot add a missing game, install NAM, or convert an unsupported game profile automatically.

Close SimCity 4 before installing or updating SCP. Keep a backup of any city you intend to use for experimental pieces. Building can take some time because the installer generates the complete catalogue on your computer; the progress display identifies the current stage.

## 2. Download the matching ZIP

Open the repository's [Releases page](https://github.com/KomodorDev/sc4-simons-custom-pieces/releases), and choose the intended **SCP Installer — experimental** prerelease. A **prerelease** is a downloadable development version, rather than a claim that every piece has passed game testing. If no installer prerelease is listed, the release workflow has not produced an installer yet; the repository's **Source code** ZIP is a different download and requires the developer setup.

Download **`SCP-Installer-windows-x64-<commit>.zip`**. This contains the Windows installer executable and its runtime.

`<commit>` is the first 12 characters of the source revision recorded on that release. The ZIP has a matching `.zip.sha256` file, and the release includes a bundle index and installer self-test report tied to its exact source revision. A SHA-256 checksum detects different bytes; it does not establish game compatibility or replace publisher signing.

Right-click the downloaded ZIP, select **Extract All…**, choose a destination, and select **Extract**. Open the extracted directory, and double-click **SCP Installer.exe**. Keep its accompanying `_internal` directory beside the executable; it contains the bundled runtime.

### First-launch operating-system approval

The executable is not signed with a publisher certificate, so Windows may display an unrecognized-app warning. Confirm that you downloaded the intended asset from this repository's release. On a SmartScreen dialog that offers them, select **More info**, inspect the application name, and select **Run anyway** if you trust the download. Managed computers can prevent this option. Keep Windows Security enabled; see [Microsoft's explanation of app reputation](https://learn.microsoft.com/windows/apps/package-and-deploy/smartscreen-reputation).

## 3. Select the game folder

Select **Choose game folder…**, navigate to the game installation, and select that folder. This is the folder containing the original game data, including **SimCity_3.dat**. It is different from your save-game and Plugins folders. For a Windows installation, look for the directory containing the game's `Apps` directory and `SimCity_1.dat`, `SimCity_2.dat`, and `SimCity_3.dat` files. Select that directory, rather than the `Apps` directory itself.

The **Plugins folder** is the directory that the game loads add-ons from. It normally sits under the user's SimCity 4 documents directory, and must already contain the supported NAM installation. After you select **Install**, the installer searches known locations and displays the detected Plugins directory while preparing the build. If several player-data folders exist or no default Plugins directory is found, installation stops and reveals **Choose Plugins folder…**. Select that button, choose the actual SimCity 4 player-data directory or its `Plugins` directory, and select **Install** again. The installer keeps your original game-folder choice and verifies the additional selection before changing anything inside Plugins.

The installer reads the installed NAM archives and the game's `SimCity_3.dat`, checks them against the recorded profile and resource audits, and creates the Road dependencies it needs automatically in its own working directory. You do not need to extract resources or prepare capture DAT files yourself. The source archives remain unchanged. Missing, changed, ambiguous, or conflicting inputs stop installation with an explanation.

## 4. Install and find the pieces

Check that the selected game folder is correct, then select **Install**. Leave the application open while it discovers Plugins, checks inputs, builds all implemented types, verifies the saved resources, prepares the assembly menu, and installs the verified result. A failed check stops the operation; it does not count as a successful installation. Select **Open log** to inspect the detailed progress or reported problem. **Cancel** requests a stop after the current build step; it becomes unavailable when the final installation transaction begins.

When the installer reports success, start SimCity 4 and open **Transportation → Rail**. Individual pieces have buttons beginning **SCP |**. The trumpet's 14 reusable types share one **SCP | ASSEMBLY | HSR Trumpet** button: **Tab** selects the next type, **Shift+Tab** selects the previous one, and each click places one component. Follow the [trumpet guide](../domains/high-speed-rail/01_assemblies/straight-stem-trumpet/README.md) to construct its 28 placements. Selecting the assembly button does not place the entire layout at once. Other implemented types retain their individual buttons.

The managed installation lives in **`zzz_Simons_Custom_Pieces` inside the selected Plugins folder**. It contains one combined SCP controller, one menu, the selected piece resources, and an ownership receipt. The receipt identifies the files the installer owns. Keep it intact. The installer's logs, builds, and backups stay under **`%LOCALAPPDATA%/SimonsCustomPieces/Installer`**, outside Plugins. `%LOCALAPPDATA%` is Windows' private application-data location for your user account; paste that complete path into File Explorer's address bar to open it. The installer does not replace NAM's original archives or modify city files.

## 5. Update, remove, or resolve a stopped installation

To update, close the game, download the intended newer installer, extract it, and select the same game and Plugins locations. The installer verifies the existing ownership receipt, saves a backup, and replaces the managed installation only after the new build passes its checks. It refuses to overwrite unknown or edited files and refuses an update that silently removes previously installed piece types. Keep the installer's application-data directory if you need its logs or backup.

To reverse the latest successful installation, close the game, open the installer, select the same game folder, and select **Undo last installation**. Read the confirmation, and select **Yes** to restore the previous managed SCP installation. If SCP was absent before that installation, undo removes its managed folder. The button is available when the installer has a saved transaction record; it does not offer a history of arbitrary versions. Existing file and backup checks can stop an undo if their contents have changed.

Before an undo removes any piece types, remove those placed pieces from every city that uses them, and save those cities. Removing the resources first can leave saved cities referring to pieces that are no longer present. The [source workflow provides receipt-based uninstall and rollback commands](BUILD_AND_INSTALL.md#install-remove-or-roll-back-a-test-build) for maintainers who need other removal or recovery operations.

If installation stops, read the reported filename and reason. A resource fingerprint mismatch means the file differs from the audited profile; replacing the expected hash would bypass the check. A controller conflict means another loaded add-on supplies the same shared rules; it requires deliberate reconciliation. An ownership error means the existing SCP directory cannot be safely replaced. Preserve the reported log, and open a [repository issue](https://github.com/KomodorDev/sc4-simons-custom-pieces/issues) with the installer release, operating system, game edition, NAM version, and exact error. Remove personal filesystem paths from a log before posting it publicly.

## What a successful installer check establishes

The release workflow builds the Windows installer, runs the packaged executable's self-test and GUI startup smoke check, records the source revision and archive checksums, and creates an experimental prerelease after an accepted `main` update. A **GUI startup smoke check** briefly opens and closes the application to check that the window can start; it does not install anything or play the game. The installer then builds and verifies your local resource files. Neither operation plays SimCity 4, approves a software preview, changes a manual observation, reserves public game identifiers, or clears redistribution of compiled NAM-derived resources. Those remain separate [release requirements](RELEASE.md).
