# SimCity 4 Windows mod download baseline

Prepared on 6 September 2026. These files are downloaded only. No installer or mod has been executed, and no existing game files have been changed.

| Component | Version | File | Bytes |
| --- | --- | --- | ---: |
| Network Addon Mod | 50 | NetworkAddonMod_Setup_Version50.zip | 821,645,763 |
| NAM DLL, standalone spare | 1.3.1 | NAM-dll-1.3.1.zip | 70,994 |
| SC4Fix | r8 / rev8 | SC4Fix.dll | 118,784 |
| CPU Options | 1.0.2 | SC4CPUOptions-v1.0.2.zip | 55,757 |
| Graphics Options | 1.4.0 | SC4GraphicsOptions-v1.4.0.zip | 81,938 |
| Microsoft Visual C++ v14, x86 | 14.51.36247.0 | vc_redist.x86.exe | 6,941,536 |
| Microsoft Visual C++ VS2022 channel, x86 | 14.44.35211.0 | vc_redist.x86-vs2022.exe | 13,953,392 |
| Resource Loading Hooks | 2.0.1 | SC4ResourceLoadingHooks-v2.0.1.zip | 59,263 |

The JSON manifest records stable original download links, source release pages, exact byte counts, and SHA-256 hashes. ZIP integrity checks passed. The three author-published GitHub hashes available for NAM, NAM DLL and Graphics Options match the downloads. The full NAM archive contains the same NAM.dll as the standalone 1.3.1 archive; install only one copy.

## Installation notes for the parent setup task

The intended game is the GOG Windows digital edition, executable version 1.1.641, inside Porting Kit. A Wine prefix is the isolated folder containing one simulated Windows installation. The 32-bit game needs the x86 Visual C++ runtime installed into that same prefix. Installing a Mac runtime or an ARM64/x64-only runtime elsewhere does not provide its x86 libraries. The current Microsoft runtime requires Windows 10 or 11 compatibility. Porting Kit-specific compatibility must still be tested.

### NAM 50

Extract the archive before use. Its contents are the Java installer, NAM.dll, instructions, 4gb_patch.exe, a Windows x64 Java MSI, and a documentation link. NAM requires the Windows digital 1.1.641 game and Visual C++ 2022+ x86. Native Aspyr Mac editions cannot load NAM.dll. A Java runtime is needed for the installer; the bundled MSI is a Windows installer, not a native Mac Java installer. If running the Java installer on macOS, explicitly choose the Windows game's Plugins destination rather than the existing native Mac Plugins folder. Place NAM.dll directly at the top level of one Plugins folder. NAM.ini is optional. The 4GB patch remains recommended, though NAM 50 no longer strictly requires it. After launch, NAM.log reports DLL status and whether the 4GB patch is present. NAM's release notes mention Resource Loading Hooks DLL for tunnel-portal exemplar patches; version 2.0.1 has now been downloaded here for that dependency.

Sources: [NAM 50 release](https://github.com/NAMTeam/Network-Addon-Mod/releases/tag/50), [installation documentation](https://www.sc4nam.com/docs/getting-started/installation/), [NAM DLL 1.3.1](https://github.com/NAMTeam/nam-dll/releases/tag/1.3.1).

### SC4Fix r8

Copy SC4Fix.dll into a Plugins folder. Version r8 writes SC4Fix.log into the game's installation folder; it no longer changes the title bar. The log identifies loaded version 8 and the detected game version. The Windows resource version inside the downloaded r8 DLL still says 1.0.0.7; that is stale metadata, not evidence that the wrong asset was downloaded. GitHub labels r8 as a pre-release; the community distribution lists r8 as current.

Source: [author's r8 release](https://github.com/nsgomez/sc4fix/releases/tag/rev8).

### CPU Options 1.0.2

Copy its DLL and INI into the installation Plugins folder. It replaces older SC4SingleCPU and SC4CPUPriority DLLs; avoid duplicates. It defaults to restricting SC4 threads to one CPU core and using AboveNormal priority. Version 1.0.2 limits affinity for SC4 threads rather than restricting all process threads, potentially helping graphics-driver performance. Existing CPUCount/CPUPriority arguments override corresponding defaults. Verify SC4CPUOptions.log beside the DLL.

Source: [CPU Options release](https://github.com/0xC0000054/sc4-cpu-options/releases/tag/v1.0.2).

### Graphics Options 1.4.0

Copy its DLL and INI into the installation Plugins folder. Defaults in the original archive are DirectX, 1920x1080, 32-bit color, fullscreen and intro enabled. For an initial controlled test, consider WindowMode=Windowed and EnableIntroVideo=false after preserving the original INI. DirectX uses SC4's DirectX 7 renderer; dimensions exceeding 2048 require an appropriate graphics wrapper. Hardware rendering under the selected Wine engine still needs testing. Verify SC4GraphicsOptions.log beside the DLL. The package has not been reconfigured here.

Source: [Graphics Options release](https://github.com/0xC0000054/sc4-graphics-options/releases/tag/v1.4.0).

### Microsoft runtime

The installer was obtained from https://aka.ms/vc14/vc_redist.x86.exe, which resolved to Microsoft's download.visualstudio.microsoft.com host. Its embedded file and product version is 14.51.36247.0. The x86 architecture matches SC4 and its DLLs, even though the host Mac is Apple Silicon. If Porting Kit offers a supported vcrun2022 installation operation for the same prefix, use its documented workflow; an arbitrary Wine-native DLL override list has not been prepared. No claim has been made that the newest runtime installer is already verified under the selected Wine engine.

Source: [Microsoft runtime downloads](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist).

For inspected NAM 50 installer defaults and the older Wine CX19 runtime assessment, see [NAM50-options-and-Wine-notes.md](NAM50-options-and-Wine-notes.md).
