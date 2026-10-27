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

For a new or revised reusable piece, follow [WORKFLOW: Piece Creation](../../docs/WORKFLOW_PIECE_CREATION.md). For a layout made from several pieces, follow [WORKFLOW: Assembly Creation](../../docs/WORKFLOW_ASSEMBLY_CREATION.md); open piece authoring only for missing or changed modules. Generate or refresh README and TESTING documents, previews, connector exports, and cards through [WORKFLOW: Documentation Generation](../../docs/WORKFLOW_DOCUMENTATION_GENERATION.md). Read the owning domain's `AGENTS.md` and consult its `NETWORK_SPEC.md` for network-specific measurements and implementation entry points.

The library's [connector reference](../../docs/CONNECTOR_METADATA.md) owns boundary/channel definitions, coordinates, and permissions. [Framework engineering](../../docs/FRAMEWORK_ENGINEERING.md) owns shared implementation contracts. Any separate consumer must use the library's generated connector outputs rather than duplicate source parsing. A shared service name, height, or game class alone does not establish a complete connection.

Preserve approved geometry and game identities, distinguish types from instances, and use the user's exact-layout or bounded-redesign policy. Reuse independently useful types. Keep atomization decisions and version-specific resource evidence with their assembly, and finish integrated source checks before rendering concurrent geometry work; use the full assembly procedure for those contracts.

New or intentionally refreshed pieces use README plus TESTING, as assemblies do. Follow the [three-chapter README and intrinsic movement matrix](../../docs/WORKFLOW_DOCUMENTATION_GENERATION.md#piece-readme) and [shared six-chapter TESTING layout](../../docs/WORKFLOW_DOCUMENTATION_GENERATION.md#required-piece-and-assembly-testing-layout), using the migrated trumpet types linked there as current examples. The split markers are `<!-- PIECE README LAYOUT: 2 -->` and `<!-- PIECE TESTING LAYOUT: 1 -->`; legacy combined guides remain intact until explicitly migrated. Preserve authored text outside generated sections, exact observations, and source-backed connection data. Follow [TESTING](../../docs/TESTING.md) for observations; only explicit matching human confirmation records a manual pass. Building, installing, and publishing remain separate actions within the user’s authorization.

Apply the same [artwork folder ownership](../../docs/WORKFLOW_DOCUMENTATION_GENERATION.md#artwork-ownership-and-folders) to pieces and assemblies: `icon.png` beside the subject definition, documentation images in `previews/`, and provenance in `evidence/`. An assembly owns its button icon; repeated component placements reuse their piece types' artwork.
