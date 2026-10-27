---
title: "SCP agent entry point"
summary: "Require the piece-versus-assembly decision and route authoring or maintenance to the shared workflow, owning network specification, and authoritative subject data."
audience: "Coding agents"
document_type: "agent-instructions"
---

# SCP agent entry point

- Write each Markdown prose paragraph on one physical source line. Let the viewer wrap; preserve structural and intentional breaks.
- Before allocating or implementing a new type, apply the [piece-versus-assembly decision](docs/WORKFLOW_PIECE_CREATION.md#0-decide-between-a-piece-and-an-assembly), even when the request calls the complete design a “piece.” Prefer reusable modules for complete complex junctions, announce the assembly delivery, and follow the assembly workflow. Model render-group packing is a separate technical check.
- Use [README.md](README.md) to select the creation or [documentation-generation workflow](docs/WORKFLOW_DOCUMENTATION_GENERATION.md), and [STRUCTURE.md](STRUCTURE.md) to locate its sources. For domain work, read the owning domain's short `AGENTS.md` and consult its `NETWORK_SPEC.md` where implemented. Use [network-assembly-design](skills/network-assembly-design/SKILL.md) for piece or assembly work.
- Every assembly uses one menu button with Tab/Shift+Tab cycling through its reusable components. Follow the [assembly menu policy](docs/WORKFLOW_ASSEMBLY_CREATION.md#terms-and-evidence) and [packaging step](docs/BUILD_AND_INSTALL.md#prepare-the-assembly-menu); each click places one component.
- Keep one README per piece; assemblies use README plus TESTING. Shared observation instructions live in [docs/TESTING.md](docs/TESTING.md). Do not add duplicate connection, checklist or helper Markdown pages.
- Edit maintained prose or the generator that owns its marked section. Authoritative JSON stores definitions, placements, connections and observations; generated inventories and checkboxes are views.
- Use the library-owned [connector reference](docs/CONNECTOR_METADATA.md) for source semantics and the [documentation-generation workflow](docs/WORKFLOW_DOCUMENTATION_GENERATION.md) for artwork, exports, and cards. Keep shared rules in `docs/`, network facts in the owning specification, and particular measurements with the piece or assembly. Consumer applications must use the library exports rather than duplicate source parsing. Follow the documented verification/extraction order and explicit coverage limits.
- Preserve game IDs, approved geometry and relevant evidence for retained subjects. Explicitly deleted subjects retain no retired definitions, artifacts or compatibility copies.
- Only explicit human confirmation changes manual observations. Software tests cannot tick game rendering, connection or journey cases. Preserve failed and stale results and their exact scope.
- Keep intrinsic piece validation and extraction separate from compatibility discovery, which is not supplied by the current library. Do not generate manual port/counterpart matrices or use legacy endpoint shortlists as complete-boundary matches. Any future discovery consumer must exclude unmigrated, missing, stale, or invalid connector inputs explicitly; it must not infer their compatibility or author missing metadata.
- Use [framework engineering](docs/FRAMEWORK_ENGINEERING.md) and [build/install](docs/BUILD_AND_INSTALL.md) for shared contracts. Keep one combined controller per installed selection; building, installing and publishing remain separate actions within the user's authorized scope.
