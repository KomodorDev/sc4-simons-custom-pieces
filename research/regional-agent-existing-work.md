# Existing SC4 regional automation work

Research checked 7 September 2026. Read-only web/source inspection; no code installed or run in the game. “Released” below means the author publishes implementation/binaries, not that we have verified it under the user's Wine installation.

## Finding

I found no publicly documented, ready-to-use agent that understands a regional development brief and autonomously builds, terraforms and maintains a heavily modded SC4 region. Searches included SC4/SimCity 4 + AI, agent, bot, automation and MCP, plus GitHub repository search. This is a search result, not proof none exists. Several surprisingly substantial building blocks do exist, including actual regional automation, a live JSON telemetry DLL and an MCP server for assets.

## Most relevant implementations

| Project | Evidence and maturity | Reusable capability | Gap against the requested regional agent |
|---|---|---|---|
| [SC4 Network Game Command](https://github.com/0xC0000054/sc4-network-game-command) | Public C# sample client, created and last pushed 10 August 2026; author tested Windows digital release. One commit, no GitHub release observed. | Connect to SC4's built-in HTTP/TCP command listener on port 50020 after enabling `-NetCommandGenerator:enabled`. Commands return values; one connection at a time. | Thin command client, no city planning/state model. Author warns commands can crash/hang the game. Wine not established. The sample needs .NET 10; the wire protocol need not require that particular client. |
| [SC4 command documentation](https://github.com/0xC0000054/sc4-game-command-documentation) | Work in progress, created 9 August and pushed 1 September 2026. | Documents lots, networks, zones, elevation, camera, screenshots, city/region loading, speed and saves. | Incomplete/unknown parameters; listed commands can be unimplemented. Not a certified gameplay API. |
| [Lua test scripts](https://github.com/0xC0000054/sc4-lua-test-scripts) | Repository created 16 April 2026, updated 9 August. Actual checked tree contains one example: AutoLoadCityTestScript.lua. | Load a city after region initialization; wait/yield on engine messages. Run via startup argument or ExecuteScript. | Example and scripting substrate, not a whole-city generator or AI. |
| [Region Sync / SC4 Region Update](https://community.simtropolis.com/files/file/37590-region-sync/) | Released 1.0 on 31 August 2026. [Detailed project report](https://github.com/RacoonsInATrenchcoat/SC4-Region-Update/blob/main/docs/project-summary.md) says full seven-tile, multiple-pass/traversal tests completed. | Enumerate established cities, load each, wait until ready, simulate a chosen number of months, pause, save, exit, repeat. Default 12 months × two passes. A diagnostic planner computes edge adjacency. | Does not build anything or select a goal-dependent visit order. Unique city names required. Popups/disasters need intervention; watchdog cannot detect a modal freeze that stops its subscribed messages. |
| [SimCity 4 Web Interface plug-in](https://github.com/dsalzner/simcity4-webinterface-plugin) | v0.0.3 released 29 April 2024; last push same day. Source and binary release. | Live JSON at `http://127.0.0.1:9030/state`; city identity, RCI supplies/populations, income/expense metrics, water pollution. Browser graphs as a second screen. Month-end pause and pause on deficit. | No construction, regional map or terrain. Existing source has telemetry defects requiring audit before reuse. |
| [dbpf-mcp](https://github.com/caspervg/dbpf-mcp) | Created 26 May, pushed 15 August 2026; six commits seen. Implemented Kotlin/JVM MCP stdio server with tests; JDK 21. | Index/search installed assets, inspect named exemplar properties, SC4PATHS, textures and metadata; export JSON/images and write supported DBPF resources. | Asset/mod authoring MCP, not live gameplay control or a complete semantic savegame decoder. Useful as a content catalogue for choosing station/hospital/lot IDs. |
| [SimCity Atlas](https://github.com/nishantmodak/simcity-atlas/blob/main/README.md) | Published 7 September 2026, the day of this research. Agent skill, prompts, Python/Node generators, downloadable example regions. Explicit prerelease limits. | Generate regional terrain from elevation/geographic data; preserve shared city edges; optional experimental native tree records. | Author explicitly says it does not play the simulation or build developed cities. Structural checks passed; forest rendering and save/reopen persistence unverified; prepared primarily for Steam/Mac. |
| [SC4Parser](https://github.com/Killeroo/SC4Parser) | Since 2020; last push 27 May 2024. .NET Standard 2.0 library. | Savegame extraction: buildings, terrain and network subfiles 1/2 listed fully implemented. | Bridges, lots and region-view records partial. Saved state only, not live state. |
| [SC4Cartographer](https://github.com/Killeroo/SC4Cartographer) | Released map generator; latest release v1.1.0 27 February 2021, last repo push 4 January 2024. | Convert SC4 saves to map images, built on SC4Parser. | Visualization, not agent control; coverage inherits parser limitations. |
| [sebamarynissen/sc4](https://github.com/sebamarynissen/sc4) | Maintained CLI since June 2019; last push 12 February 2026. | Save modifications, growify placed buildings, historic flag, optimal pipe layout, asset/submenu tooling. | Offline modifications do not satisfy visible live construction. Its bulk lot-plop test workflow can produce lots that crash on querying/bulldozing, so should not be treated as a safe city-building API. |
| [Region Census](https://github.com/0xC0000054/sc4-region-census) | v1.0.1 released 27 February 2024; last push November 2024. | Region-wide RCI totals and per-city CSV export; source demonstrates correct region enumeration. | Regional census only, not a complete terrain/traffic/utility export. |

Repository dates came from read-only GitHub repository/release API responses on the research date; source links above identify the primary projects.

## Details that materially change the design

### Real construction commands, with limits

[App commands](https://github.com/0xC0000054/sc4-game-command-documentation/blob/main/commands/Maxis/AppCommands.md) documents:

- `PlaceNetwork <network type> <x1> <y1> <x2> <y2>`.
- `PlaceZone <zone type> <x1> <y1> <x2> <y2>`.
- `PlaceLot <lot exemplar IID> <cell x> <cell z> <facing> <use plop effects> <unknown Boolean>`.
- `SetViewTarget cell <x> <z>` or `position <x> <y> <z>`.
- `TakeSnapshot <output filename> [x1,y1,x2,y2]`.
- `PlaceNetworkIntersection` is explicitly unimplemented. Do not infer a working intersection operation just from its name.

[City commands](https://github.com/0xC0000054/sc4-game-command-documentation/blob/main/commands/Maxis/CityCommands.md) includes SetAltitude, SetCellAltitude, SetCityEstablished, SetCityName, and speed/save tools. Syntax exists, but costs, validity checks, NAM overrides and developed-lot consequences still need local experiments.

### Region Sync is the strongest lifecycle precedent

The [detailed report](https://github.com/RacoonsInATrenchcoat/SC4-Region-Update/blob/main/docs/project-summary.md) explains important implementation results:

- Only the loaded city simulates. Other cities supply saved information; this is not concurrent regional simulation.
- Utility and economic/commute effects settle differently, and visit order can affect outcomes when shared resources are scarce.
- It counts actual new-month events, not guessed elapsed real time.
- It waits for ConnectionsReady and verifies loaded identity.
- City exit is deferred outside the simulation callback, because immediate teardown within that callback crashes.
- It does not have a reliable convergence signal; use bounded passes and measured tolerances in our eventual design.

The repository README is stale and claims implementation has not started. Its detailed report, source, published release and author release page supersede that status. Claims such as “crash-safe by construction” in the report should not be repeated as guarantees.

### Live JSON already exists, but requires correction

The [web interface's source](https://github.com/dsalzner/simcity4-webinterface-plugin/blob/main/src/cMessageLoggerCOMDirector.cpp) maps `ytdExpenses` to `GetEstIncome` and `estIncome` to `GetYTDExpenses` (lines 116 and 118 at inspected main); those fields appear swapped. It also casts budget values to `int`. A new bridge should reuse the idea, verify every field against the game UI and keep the correct numeric widths. The older [author article](https://www.dennissalzner.de/gamemods/2024/03/31/So-SimCity4Plugins.html) describes unreliable pause; the later repository release history says v0.0.2 improves it by pausing on the next month. Avoid presenting the old note as the latest release state.

## Related AI mayor work, in a different game

[Hallucinating Splines](https://github.com/andrewedunn/hallucinating-splines) is a concrete AI-mayor project with REST API, MCP, city state, tool placement, simulation steps, public maps, history charts and action logs. Created February 2026. It uses **Micropolis**, the open-source classic SimCity engine, not SimCity 4. It is a good reference for the agent interaction/observability design, but its game adapter cannot drive SC4 and it has no NAM/HSR/SC4-region support. The inspected repository provides source and a linked public service; I did not create an account/city or independently test play.

This separates three different accomplishments often conflated in search results: an AI that authors SC4 terrain files, an MCP that edits SC4 assets, and an AI that actually plays a different SimCity-derived engine. None is the requested complete SC4 regional operator.
