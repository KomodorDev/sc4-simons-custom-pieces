---
title: "SCP Planner agent entry point"
summary: "Keep Planner a consumer of the authoritative source library rather than a second owner of connector authoring, validation, or canonical artwork."
audience: "Coding agents"
document_type: "agent-instructions"
---

# SCP Planner agent entry point

- Read the parent instructions and [Planner README](README.md). Shared rules live in the library's [connector reference](../custom-pieces/docs/CONNECTOR_METADATA.md); README, rendering, export, and card procedures live in its [documentation-generation workflow](../custom-pieces/docs/WORKFLOW_DOCUMENTATION_GENERATION.md).
- Keep application adapters, interactive placement, candidate discovery, application tests, and private reports here. The library owns its JSONC reader, source schemas, semantic validation, authored declarations, measured connections, generated `connector-data.json`, canonical overview artwork, and provenance. Reuse those implementations and records; do not copy parsers or invent another extraction workflow.
- Read explicit registered paths through the adapter. Source binding and export freshness failures require the library's authoring/check procedure, not a copied hash or a geometry change made to satisfy the application.
- Preserve stable type, group, channel, cut, and member IDs; keep measured source ports as references. Store a separate instance ID, anchor position, and rotation for each placed copy. Do not write application placements into type definitions or alter saved assemblies.
- Compare complete shared boundaries under one placement, with exposed edges, coincident full tile-edge segments, opposing normals, explicit channel/cut relationships, and complementary permissions. Keep positions, headings, slopes, owned cells, routes, and models in the same placement frame. A shared corner alone is insufficient; do not ban a legitimate corner endpoint on a real shared edge.
- Use transport channel for a separately identifiable physical passage. Keep channels, cuts, directed route records, network services, engine classes, and traffic modes distinct. Source-backed associations and measured geometry control comparison; names and profile tokens do not.
- Keep pairwise metadata and owned-cell checks separate from full-scene fit, compiled evidence, physical seams and clearance, terrain construction, and game operation. Actual measured coverage remains the two HSR types; synthetic cases do not establish another compiled network family. Missing checks remain unverified.
- Keep private consumer reports and working renders under `local/`. Canonical connector cards belong beside each source piece and are regenerated through the library's `connectors refresh` command. Preserve original piece previews and manual observations. Write each Markdown prose paragraph on one physical source line.
