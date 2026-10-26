# CAM runtime and overlap audit — 7 September 2026

This is a read-only audit of the active installation. Only audit reports and official download archives in this directory were written. No game files, package selections, saves, or settings were changed by this audit.

## Runtime findings

The existing game is the Windows GOG 1.1.641 x86 edition in Wine 4.12.1/CX19. Microsoft VC++ 2022 x86 is already installed. The game-specific Microsoft math API forwarder installed for Plop and Paint remains in Apps.

Seven additional official DLL releases were inspected: CustomBudgetDepartments 1.1, SC4LuaExtensions 1.5, AdvancedWaterManagement 1.0, SC4LegalizeGamblingUpgrade 1.0, SC4CustomOrdinanceHost 1.0.1, memo.lua-sandbox 1.0, and SC4MoreBuildingStyles 3.6.1. All are x86 (PE machine 0x14c). Every directly imported function was found in the current Apps/system32 PE export tables. See `dll-import-audit.json`.

This static check does not verify Wine behavior or dynamically resolved functions. Confirm successful loading with fresh logs after installation. The official authors generally require Windows 10+ or Linux and GOG/digital game 641; they do not promise this old macOS Wine engine is supported.

## Conflicting or superseded fixes

`fix-overlap-audit.json` compares real decompressed DBPF entries from SIM 4.0.1 and the installed independent fixes. Compression-directory entries were omitted from overlap results.

- **IHT Jobs Fix:** change global variant to `CAM=yes` and let sc4pac update. The package's CAM variant installs no files because CAM supplies its own correction.
- **Spaceport Fix:** archive/remove the manual DAT. Its reward building exemplar (6534284a-8a3858d8-03840000) overrides SIM's CAM_Rewards_Building.dat when loaded afterward. The SIM version supplies different CAM-balanced jobs, maintenance, power, water and other properties. The independently installed fix would revert those properties. The user has no existing Space Ports/cities.
- **Opera House Fix:** remove `mz:opera-house-fix` through sc4pac. Its query/UI, language, Lua, blocker, legacy building and lot records overlap SIM's integrated implementation. Several payloads differ and load later; the legacy Opera building capacity is 25,000 in the standalone file versus 119,800 in SIM. The user has no existing Opera Houses/cities, so retaining a legacy standalone fix is unnecessary.
- **HippoTank Demand Fix:** archive/remove the manual file from the game's installation Plugins. Its Medical Clinic, Solar Plant and Nuclear Plant exemplars overlap SIM's Maxis blocker exemplars. SIM deliberately removes their menu icons and has its own replacement buildings. In the current location the installation Plugins load before user Plugins, so SIM wins, but retaining the obsolete file serves no purpose and moving it later could reactivate blocked originals.
- **SC4Fix, CPU Options and Graphics Options:** no direct documented incompatibility with these CAM packages was found. Keep the existing working versions and settings; this is not a claim of exhaustive binary-patch compatibility.

## Installation and post-installation items

1. Use CAM=yes/current, with Controller 3.1.1, SIM 4.0.1 and Ordinances 3.3.0. The user confirmed no existing Windows cities. Current CAM requires a new region for users previously playing without CAM.
2. Retain sc4pac's folder ordering: CAM/SIM in 050-load-first, Ordinances in 140-ordinances, supporting mods in 150-mods. Do not re-add the excluded `CAM_Maxis_Ordinance_Overhaul_Mod.dat` from the Ordinances archive: official package metadata excludes it as duplicate content.
3. Keep only one active copy of each DLL at Plugins root. SIM's ZIP also contains AdvancedWaterManagement.dll; its separate managed DLL package supplies the active copy.
4. If sc4pac installs `SC4LegalizeGamblingUpgrade_sc4pacnew.ini`, activate it as `SC4LegalizeGamblingUpgrade.ini` while preserving an existing user file if present. Shipped defaults use `[GamblingOrdinance]`, base income 250, wealth factors .02/.03/.05 and crime multiplier 1.20. The archive README mistakenly mentions a CityLottery section and 500; follow the actual INI/source defaults.
5. Lua Sandbox defaults are suitable for this installed set. It is incompatible with DAMN, BSC Regional Tracking and Cori Reports; none is documented as installed. Its restrictions target Lua scripts, not Plop and Paint's native C++ cache handling.
6. SIM depends on Save Warning. That intentionally disables combined Save & Exit/Save & Quit. Teach the user to save first, wait for completion, then exit without another save. Existing Auto Save can remain.
7. Rebuild Plop and Paint content caches after all mod additions/removals, with the game closed, so the new CAM buildings and hospitals appear in the overlay.
8. Check new DLL logs and existing Plop and Paint/Render Services after a normal launch. For AdvancedWaterManagement, Query UI Hooks is already installed and is required. Preserve the existing Wine math-forwarder override and runtimes.

## Downloads

`downloads/provenance.json` records exact official URLs, SHA256 values and local filenames for SIM, CAM Controller, CAM Ordinances and all seven audited DLL archives. Downloads were staged unchanged.

No publicly hosted SC4Evermore alternative for Universal Commercial CAP Fix was found. Its current public author download is on Simtropolis. Do not substitute an unrelated or unverified mirror.

## Primary sources

- [CAM package metadata](https://github.com/memo33/sc4pac/blob/main/src/yaml/cam/colossus-addon-mod.yaml)
- [SIM package metadata](https://github.com/memo33/sc4pac/blob/main/src/yaml/cam/cam-corefile.yaml)
- [Ordinances package metadata](https://github.com/memo33/sc4pac/blob/main/src/yaml/cam/cam-ordinances.yaml)
- [IHT variant metadata](https://github.com/memo33/sc4pac/blob/main/src/yaml/heinbloed4711/hi-tech-missing-high-wealth-jobs.yaml)
- [SIM 4.0.1 author page](https://www.sc4evermore.com/index.php/downloads/download/45-colossus-addon-mod-cam/414-sc4-system-integration-module-sim)
- [Custom Budget Departments](https://github.com/0xC0000054/sc4-custom-budget-departments)
- [Lua Extensions](https://github.com/0xC0000054/sc4-lua-extensions)
- [Advanced Water Management](https://github.com/0xC0000054/sc4-advanced-water-management)
- [Gambling Upgrade](https://github.com/0xC0000054/sc4-legalize-gambling-ordinance-upgrade)
- [Custom Ordinance Host](https://github.com/0xC0000054/sc4-custom-ordinance-host)
- [Lua Sandbox](https://github.com/memo33/sc4-lua-sandbox-dll)
- [More Building Styles](https://github.com/0xC0000054/sc4-more-building-styles)
