---
title: "High-speed rail agent additions"
summary: "Apply HSR/GHSR, tram-crossing, and rail assembly requirements alongside the selected shared workflow and measured network specification."
audience: "Coding agents"
document_type: "agent-instructions"
---

<a id="high-speed-rail-agent-entry-point"></a>

# High-speed rail agent additions

<!-- BEGIN DOCUMENT NAVIGATION -->
[1. Domain workflow](#1-domain-workflow)
<!-- END DOCUMENT NAVIGATION -->

<a id="domain-workflow"></a>

## 1. Domain workflow

1. Apply the parent [library instructions](../../AGENTS.md) and continue the selected shared workflow; these domain additions do not require restarting workflow selection. Consult the [rail player guide](README.md) for placement and menu use.
2. Consult the [network specification](NETWORK_SPEC.md) for native rail levels, profiles, donor resources, rail-specific limits, and implementation entry points. Shared coordinates, model budgets, and addressing belong to [framework engineering](../../docs/FRAMEWORK_ENGINEERING.md).
3. For an existing subject, open its README and TESTING documents; legacy combined piece guides remain valid until deliberately migrated. New piece guides and deliberately migrated legacy guides follow the shared three-chapter README and six-chapter TESTING standard. Reusable geometry belongs in `00_pieces/`; placements and complete-layout contracts belong in `01_assemblies/<assembly-id>/`.
4. Preserve approved track positions, height, supports, and identities during organization work. A real curved tail or physical branch wing is not an ordinary straight tile. The trumpet's exact-layout contract lives with its assembly. For a junction border repair, follow the [ballast-curve guidance](NETWORK_SPEC.md#51-junction-borders-following-ballast-curves), including the continuous top and inside wall, unchanged train clearance, and saved-model regression checks.
5. Edit authoritative JSON or its generator. Piece connection/test sections and inventories are generated views. Only explicit matching human observations may create manual checkmarks; follow the [observation guide](../../docs/TESTING.md).
6. For connector work, follow the shared [rules](../../docs/CONNECTOR_METADATA.md) and [generation procedure](../../docs/WORKFLOW_DOCUMENTATION_GENERATION.md). Keep reviewed rail classification and channel associations with this domain, and reuse shared framework tooling.
