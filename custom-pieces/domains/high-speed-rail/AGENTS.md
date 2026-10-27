---
title: "High-speed rail agent entry point"
summary: "Route HSR/GHSR, tram-crossing, and rail assembly work to shared workflows and the measured network specification."
audience: "Coding agents"
document_type: "agent-instructions"
---

# High-speed rail agent entry point

1. Read the [framework router](../../AGENTS.md) and [rail player guide](README.md).
2. Use the [assembly-design skill](../../skills/network-assembly-design/SKILL.md) to select the shared creation or documentation workflow. Consult the [network specification](NETWORK_SPEC.md) for native rail levels, profiles, donor resources, rail-specific limits, and implementation entry points. Shared coordinates, model budgets, and addressing belong to [framework engineering](../../docs/FRAMEWORK_ENGINEERING.md).
3. Start from the owning piece or assembly README and TESTING documents; legacy combined piece guides remain valid until deliberately migrated. New or refreshed pieces follow the shared three-chapter README and six-chapter TESTING standard. Reusable geometry belongs in `00_pieces/`; placements and complete-layout contracts belong in `01_assemblies/<assembly-id>/`.
4. Preserve approved track positions, height, supports and identities during organization work. A real curved tail or physical branch wing is not an ordinary straight tile. The trumpet's exact-layout contract lives with its assembly.
5. Edit authoritative JSON or its generator. Piece connection/test sections and inventories are generated views. Only explicit matching human observations may create manual checkmarks; follow the [observation guide](../../docs/TESTING.md).
6. For connector work, follow the shared [rules](../../docs/CONNECTOR_METADATA.md) and [generation procedure](../../docs/WORKFLOW_DOCUMENTATION_GENERATION.md). Keep reviewed rail classification and channel associations with this domain, and reuse shared framework tooling.
