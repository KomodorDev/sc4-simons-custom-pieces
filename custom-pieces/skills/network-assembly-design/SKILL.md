---
name: network-assembly-design
description: Design, atomize, document, and verify reusable SimCity 4 SCP pieces and multi-piece assemblies, including connections, coordinate-based review, and human-confirmed test records.
metadata:
  title: "Network assembly design"
  summary: "Route creation and documentation tasks to shared workflows and network specifications while preserving source geometry, reusable identities, and scoped evidence."
  audience: "Coding agents"
  document_type: "skill"
---

# Network assembly design

For a new or revised reusable piece, follow [WORKFLOW: Piece Creation](../../docs/WORKFLOW_PIECE_CREATION.md). For a layout made from several pieces, follow [WORKFLOW: Assembly Creation](../../docs/WORKFLOW_ASSEMBLY_CREATION.md); open piece authoring only for missing or changed modules. Generate or refresh README files, previews, connector exports, and cards through [WORKFLOW: Documentation Generation](../../docs/WORKFLOW_DOCUMENTATION_GENERATION.md). Read the owning domain's `AGENTS.md` and consult its `NETWORK_SPEC.md` for network-specific measurements and implementation entry points.

The library's [connector reference](../../docs/CONNECTOR_METADATA.md) owns boundary/channel definitions, coordinates, and permissions. [Framework engineering](../../docs/FRAMEWORK_ENGINEERING.md) owns shared implementation contracts. Any separate consumer must use the library's generated connector outputs rather than duplicate source parsing. A shared service name, height, or game class alone does not establish a complete connection.

Preserve approved geometry and game identities, distinguish types from instances, and use the user's exact-layout or bounded-redesign policy. Reuse independently useful types. Keep atomization decisions and version-specific resource evidence with their assembly, and finish integrated source checks before rendering concurrent geometry work; use the full assembly procedure for those contracts.

Keep one README per piece and README plus TESTING per assembly. Preserve authored text outside generated sections and source-backed connection data. Follow [TESTING](../../docs/TESTING.md) for observations; only explicit matching human confirmation records a manual pass. Building, installing, and publishing remain separate actions within the user's authorization.
