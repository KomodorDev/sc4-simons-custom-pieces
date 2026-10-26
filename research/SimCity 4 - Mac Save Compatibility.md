# SimCity 4: Mac 64-bit save compatibility with Windows 32-bit

Investigated 7 September 2026. This was a feasibility investigation, not a conversion. No city save, plugin, game setting, or game installation was changed.

## Finding

No established tool was found that converts a complete developed Aspyr 64-bit Mac city to the Windows 32-bit save format. A custom converter is a possible research project; success and completeness are unproven. Terrain recovery has stronger evidence: East Valley's elevation data is readable, and community testing has previously recovered terrain from other Mac saves using SC4Mapper. A regenerated terrain map does not preserve the developed city.

## Local evidence

Inspected `/Users/simonhinterreiter/Documents/SimCity 4/Regions/New York/City - East Valley.sc4`, selected because it is the largest save in the original Mac profile. The user has not explicitly identified this as the intended target city.

The file is 70,968,453 bytes. Its outer format is ordinary DBPF version 1 with 175 entries. DBPF is a container: one file containing multiple separate sections of game data. Reading this container is not the same as understanding all the city data inside it.

Comparing decompressed records against a Windows Tegel save reveals a concrete internal difference:

| Detail | Mac East Valley | Windows Tegel |
|---|---|---|
| First building record length | 86 bytes | 82 bytes |
| Object reference starting at byte offset 8 | 8 bytes, value `0x0000600003E00010` | 4 bytes, value `0x0E026018` |
| Following version words | 2 and 4, at offset 16 | 2 and 4, at offset 12 |

A byte is a unit of stored data. An object reference links one saved game object to another. An offset is a position counted from the start of a record. Because the Mac reference occupies four extra bytes, later information starts at a different position. The first Mac lot record also has an eight-byte reference and a version field at offset 16. These examples establish an incompatibility; they do not establish that all other differences have been identified.

The main terrain section, identified as `A9DD6FF4-E98F9525-00000001`, successfully decompresses to 264,198 bytes: a two-byte version value of 2 and a 257 × 257 grid of 32-bit elevation values. All 66,049 elevations are finite; values range from approximately 282.0435 to 311.1935. Reading this grid is verified. Writing and loading a recovered Windows city is not yet tested.

East Valley's copy in `setup/backups/SimCity 4 Mac - 2026-09-06` has an identical SHA-256 fingerprint to the active Mac file. SHA-256 is a content fingerprint used to compare files. This backup preserves the same Mac-format save; it is not a recovered earlier 32-bit revision.

## Public evidence

1. [Save editor author smf_16's explanation, 9 September 2021](https://community.simtropolis.com/forums/topic/761062-switching-from-mac-to-windows-version-with-wineskin/?comment=1760531&do=findComment): a converter would require understanding the full save structure. This supports substantial engineering work, not a claim that conversion is inherently impossible.
2. [Current sc4 save editor](https://github.com/sebamarynissen/sc4): existing editing functions provide useful groundwork, but no complete Mac64-to-Windows32 conversion command was found. Its [pointer representation](https://github.com/sebamarynissen/sc4/blob/main/src/core/pointer.ts) and [save context](https://github.com/sebamarynissen/sc4/blob/main/src/core/savegame-context.ts) use 32-bit object references. Its [Savegame.create implementation](https://github.com/sebamarynissen/sc4/blob/main/src/core/savegame.ts) explicitly notes that full save generation is incomplete.
3. [SC4Parser](https://github.com/Killeroo/SC4Parser): reads the container and selected sections, including terrain, buildings and some networks. Other sections are partial or unimplemented. This is a basis for analysis, not a complete converter.
4. [First-hand terrain recovery test, July 2020](https://community.simtropolis.com/forums/topic/759452-mac-cities-on-windows-pc-not-showing-up/): CorinaMarie could read the Mac terrain with Mapper and regenerate usable terrain tiles, but the two developed test cities were removed.
5. [SC4Mapper-2026](https://github.com/caspervg/SC4Mapper-2026): modernized terrain import/export tool. Its [region implementation](https://github.com/caspervg/SC4Mapper-2026/blob/master/src/sc4mapper/region.py) writes elevation data into blank city templates. Its ability to run on a Mac does not imply full Mac-save conversion.

## Possible next work

For a complete-city conversion investigation:

1. Work on a separate copy of a selected city, keeping original and backup untouched.
2. Compare very small, controlled Mac and Windows saves. A controlled save contains a deliberately limited set of known objects, making format differences easier to identify.
3. Build a translator for known record types and consistently map object references. Simply truncating every eight-byte number is not a valid conversion strategy: many numbers are not references, and references must remain consistent throughout the file.
4. Cover the remaining simulation sections, record lengths and integrity checks. Assess unknown sections explicitly instead of silently copying incompatible records.
5. Test the output in an isolated Windows profile with matching content. A successful test must include loading, visible city checks, simulation, saving, and reopening. Merely displaying the region preview does not prove the city works.

For terrain-only recovery, extract the verified height grid and generate a new empty Windows-compatible city. This would preserve land elevations, not buildings, transport networks, population, money, or simulation history. It has not yet been carried out here.

The installed 4 GB memory patch changes how much memory the Windows executable can address. It does not translate save records. A separate older backup saved before using the 64-bit Mac edition could be a different route, but no such developed East Valley backup was established in this investigation.
