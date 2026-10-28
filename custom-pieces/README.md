---
title: "Simon's Custom Pieces"
summary: "Choose the piece, assembly, documentation, or maintenance workflow and find the current SimCity 4 content."
audience: "Players, piece authors, assembly designers, and maintainers"
document_type: "entry-point"
---

# Simon's Custom Pieces

HSR means High Speed Rail; GHSR means Ground High Speed Rail. High-speed rail is the implemented domain; Highway is reserved for future work. Open the [rail player guide](domains/high-speed-rail/README.md), [illustrated piece inventory](domains/high-speed-rail/00_pieces/INVENTORY.md), or [assembly inventory](domains/high-speed-rail/01_assemblies/INVENTORY.md) to browse current content and status.

A **piece** is one reusable component type. An **assembly** places copies of types into a complete layout. Every assembly has one menu button: **Tab** selects the next component, **Shift+Tab** selects the previous one, and each click places the selected component. A **collection** selects existing types for a build; it does not place a whole assembly. Teal PART icons identify building blocks; purple PNP icons identify implemented complete one-click junctions. The [menu legend](docs/BUILD_AND_INSTALL.md#recognize-scp-menu-icons) defines every code.

| I want to… | Open |
| --- | --- |
| Find, connect, and rotate rail pieces | [Rail player guide](domains/high-speed-rail/README.md) |
| Rebuild the modular trumpet | [Trumpet README](domains/high-speed-rail/01_assemblies/straight-stem-trumpet/README.md) |
| Install all implemented pieces without Python | [Graphical installer for Windows](docs/INSTALLER.md) |
| Build, inspect, or install the plugin | [Build and install](docs/BUILD_AND_INSTALL.md) |
| Read or record a test result | [Testing and observations](docs/TESTING.md) |
| Understand the folder structure | [Structure and ownership](STRUCTURE.md) |
| Create or revise one reusable piece | [WORKFLOW: Piece Creation](docs/WORKFLOW_PIECE_CREATION.md) |
| Design or extend an assembly | [WORKFLOW: Assembly Creation](docs/WORKFLOW_ASSEMBLY_CREATION.md) |
| Understand connector data and complete shared boundaries | [Connector metadata](docs/CONNECTOR_METADATA.md) |
| Generate README and TESTING documents, renders, connector exports, and cards | [WORKFLOW: Documentation Generation](docs/WORKFLOW_DOCUMENTATION_GENERATION.md) |
| Check which source files and outputs a new subject needs | [Creation checklist and producing commands](docs/WORKFLOW_DOCUMENTATION_GENERATION.md#creation-checklist-and-output-files) |
| Look up measured HSR/GHSR values and their implementation | [High-speed rail network specification](domains/high-speed-rail/NETWORK_SPEC.md) |
| Maintain shared code or classify a crossing | [Framework engineering](docs/FRAMEWORK_ENGINEERING.md) |
| Understand installer releases and compiled-plugin requirements | [Release requirements](docs/RELEASE.md) |

For authoring, start with the relevant creation workflow and follow its documentation-generation step. Use the [creation checklist](docs/WORKFLOW_DOCUMENTATION_GENERATION.md#creation-checklist-and-output-files) for staged file requirements, and the [small assembly starter](docs/WORKFLOW_ASSEMBLY_CREATION.md#start-a-small-hsr-assembly-from-existing-pieces) for a runnable registration example using existing types. Consult the network specification for that network's measured values and the framework reference for shared implementation details. To refresh an existing README or picture, start directly with the documentation-generation workflow. From the repository root, `python3 -B custom-pieces/scp.py docs-check` checks current documentation without changing it; its [scope and limits](docs/WORKFLOW_DOCUMENTATION_GENERATION.md#check-documentation-without-changing-it) are separate from build and game checks.

New or intentionally refreshed pieces use a three-chapter README for views, placement, and the intrinsic connection matrix, plus a separate six-chapter TESTING document for scope, setup, software checks, game checks, results, and design history. Assemblies also have an overview README and separate TESTING document. Legacy combined piece guides retain their layout until intentionally migrated. The underlying `checks/manual-tests.json` is the sole observation record; the Markdown displays it. Software checks and model pictures do not confirm game behaviour; confirmed results remain tied to their exact resources, directions, rotations, and environment. Building, installing, and publishing are separate actions.

Connector-generation coverage currently consists of fifteen piece types: all [thirteen reusable trumpet types](domains/high-speed-rail/01_assemblies/straight-stem-trumpet/README.md#2-pieces), **[HSR Paired Quarter-Turn Level 2 to Level 4](domains/high-speed-rail/00_pieces/blind-hsr-rise-quarter-turn/README.md)**, and **[HSR above parallel Road with two side pillars and paved sidewalks](domains/high-speed-rail/00_pieces/blind-hsr-road-stack/README.md)**. Each has an intrinsic movement matrix, canonical angled and top pictures, connector declaration, resolved export, and boundary cards. The trumpet’s reusable types demonstrate the current split README/TESTING layout; the two blind authoring examples retain their version-1 combined guides until explicitly refreshed. The original detailed [worked HSR examples](docs/CONNECTOR_METADATA.md#8-examples-the-two-existing-hsr-pieces) remain examples within this subset; the other rail catalogue types are not covered by this migration. The fan and merge add measured oblique single-channel cuts with undeclared section origins; their ordinary paired ends retain explicit centred sections. Their exports describe each piece's intrinsic connector facts; the library does not currently supply automatic compatibility discovery. Older, missing, stale, or invalid connector inputs do not establish compatibility or incompatibility. Piece validation does not compute a neighbour list or create an automatic port/counterpart manual checklist.
