---
title: "Simon's Custom Pieces"
summary: "Choose the piece, assembly, documentation, or maintenance workflow and find the current SimCity 4 content."
audience: "Players, piece authors, assembly designers, and maintainers"
document_type: "entry-point"
---

# Simon's Custom Pieces

HSR means High Speed Rail; GHSR means Ground High Speed Rail. High-speed rail is the implemented domain; Highway is reserved for future work. Open the [rail player guide](domains/high-speed-rail/README.md), [illustrated piece inventory](domains/high-speed-rail/00_pieces/INVENTORY.md), or [assembly inventory](domains/high-speed-rail/01_assemblies/INVENTORY.md) to browse current content and status.

A **piece** is one reusable menu type. An **assembly** places copies of types into a complete layout. A **collection** selects existing types for a build; it does not place a whole assembly. Teal PART icons identify building blocks; purple PNP icons identify implemented complete one-click junctions. The [menu legend](docs/BUILD_AND_INSTALL.md#recognize-scp-menu-icons) defines every code.

| I want to… | Open |
| --- | --- |
| Find, connect, and rotate rail pieces | [Rail player guide](domains/high-speed-rail/README.md) |
| Rebuild the modular trumpet | [Trumpet V4 README](domains/high-speed-rail/01_assemblies/straight-stem-trumpet-v4/README.md) |
| Build, inspect, or install the plugin | [Build and install](docs/BUILD_AND_INSTALL.md) |
| Read or record a test result | [Testing and observations](docs/TESTING.md) |
| Understand the folder structure | [Structure and ownership](STRUCTURE.md) |
| Create or revise one reusable piece | [WORKFLOW: Piece Creation](docs/WORKFLOW_PIECE_CREATION.md) |
| Design or extend an assembly | [WORKFLOW: Assembly Creation](docs/WORKFLOW_ASSEMBLY_CREATION.md) |
| Understand connector data and complete shared boundaries | [Connector metadata](docs/CONNECTOR_METADATA.md) |
| Compute connection candidates and inspect excluded metadata coverage | [Separate Planner compatibility discovery](../scp-planner/README.md) |
| Generate README files, renders, connector exports, and cards | [WORKFLOW: Documentation Generation](docs/WORKFLOW_DOCUMENTATION_GENERATION.md) |
| Look up measured HSR/GHSR values and their implementation | [High-speed rail network specification](domains/high-speed-rail/NETWORK_SPEC.md) |
| Maintain shared code or classify a crossing | [Framework engineering](docs/FRAMEWORK_ENGINEERING.md) |
| Prepare a future public release | [Release requirements](docs/RELEASE.md) |

For authoring, start with the relevant creation workflow and follow its documentation-generation step. Consult the network specification for that network's measured values and the framework reference for shared implementation details. To refresh an existing README or picture, start directly with the documentation-generation workflow.

Each piece has one README with its previews, connections, and generated checks. Each assembly has a complete building README and a separate TESTING page. The underlying `checks/manual-tests.json` is the sole observation record. Software checks and model pictures do not confirm game behaviour; confirmed results remain tied to their exact resources, directions, rotations, and environment. Building, installing, and publishing are separate actions.

Connector-generation coverage currently consists of the two [worked HSR examples](docs/CONNECTOR_METADATA.md#8-examples-the-two-existing-hsr-pieces). The [Planner](../scp-planner/README.md) consumes current validated exports in a separate compatibility search and reports older, missing, stale, or invalid inputs as excluded. Piece validation does not compute a neighbour list or create an automatic port/counterpart manual checklist. Planner's full browser interface remains unfinished.
