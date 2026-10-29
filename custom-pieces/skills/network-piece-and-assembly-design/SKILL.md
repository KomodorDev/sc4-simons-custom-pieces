---
name: "network-piece-and-assembly-design"
description: "Design, revise, atomize, document, and verify reusable SimCity 4 network pieces and multi-piece assemblies through the library's measured authoring workflows."
---

<a id="network-assembly-design"></a>

<a id="piece-and-assembly-design"></a>

# Network piece and assembly design

<!-- BEGIN DOCUMENT NAVIGATION -->
[1. Choose the workflow and record the inputs](#1-choose-the-workflow-and-record-the-inputs) · [2. Run the selected workflow](#2-run-the-selected-workflow) · [3. Verify and hand over](#3-verify-and-hand-over)
<!-- END DOCUMENT NAVIGATION -->

**Audience:** Coding agents. **Document type:** Skill.

<a id="choose-a-workflow-and-subject-names"></a>

<a id="1-choose-a-workflow-and-subject-names"></a>

## 1. Choose the workflow and record the inputs

Use this skill as the agent's execution checklist. The linked workflows contain the human procedures and detailed rules; follow the relevant one rather than reading every guide first. Apply the parent and owning domain's `AGENTS.md` instructions already in scope. Keep a workflow that has already been selected, and continue from the current stage instead of returning through README or other routers.

| Task | Inputs to establish | First actionable step |
| --- | --- | --- |
| New reusable piece | Domain, intended function, external interfaces, footprint, and existing types considered. | Apply the [piece-versus-assembly decision](../../docs/WORKFLOW_PIECE_CREATION.md#1-decide-between-a-piece-and-an-assembly), then follow piece creation if a new reusable type is justified. |
| Change an existing piece | Exact registered ID, current README/TESTING, definition, recipe, and requested change. | Use the [existing-piece route](../../docs/WORKFLOW_PIECE_CREATION.md); preserve its identities and skip new allocation. |
| New or changed assembly | Intended movements, member types, placement plan, connection heights, and exact-layout or redesign scope. | Follow [assembly creation](../../docs/WORKFLOW_ASSEMBLY_CREATION.md#2-establish-the-brief-and-draw-a-rough-layout-in-chat). For a new HSR layout using existing members, use its [registration starter](../../docs/WORKFLOW_ASSEMBLY_CREATION.md#12-start-a-small-hsr-assembly-from-existing-pieces) after establishing the brief and connection plan. |
| Review further splitting | Exact subject and source version, actual routes, candidate boundaries, and physical obstacles. | Follow the [atomization procedure and required drawing](../../docs/WORKFLOW_ASSEMBLY_CREATION.md#16-atomize-to-the-smallest-useful-reusable-module); an analysis-only review does not allocate another subject. |
| Refresh only existing prose, pictures, or connector outputs | Exact subject, requested output, and whether game resources changed. | Go directly to [documentation refresh scope](../../docs/WORKFLOW_DOCUMENTATION_GENERATION.md#1-choose-the-refresh-scope); do not restart creation, allocation, or layout design. |

Record these inputs in the task's working brief, reusing decisions and authorization already supplied by the user. For a new subject, choose its folder identifier and readable name through [naming conventions](../../docs/NAMING_CONVENTIONS.md) before registration. For an existing subject, preserve its registered identifiers unless their migration is explicitly in scope. Consult the domain's `NETWORK_SPEC.md` when a step needs measured network facts or implementation entry points.

<a id="preserve-sources-and-evidence"></a>

<a id="2-preserve-sources-and-evidence"></a>

## 2. Run the selected workflow

1. Identify which definition, placement plan, source generator, and checks own the requested change. Use the [source map](../../STRUCTURE.md#5-source-and-data-ownership) when ownership is unclear. For an assembly, open piece creation only for missing or changed member types; repeated placements reuse one type.
2. Follow the selected workflow's implementation and independent-check stages before rendering its result. Preserve the user's exact-layout or bounded-redesign scope, retained geometry, stable identities, and frozen evidence. For parallel geometry work, integrate and check sources before rendering the combined assembly; [assembly coordination](../../docs/WORKFLOW_ASSEMBLY_CREATION.md#17-persist-atomization-decisions-and-coordinate-parallel-work) owns that handoff.
3. For a real resource change, finish saved-resource verification and the owning extraction route before regenerating connector outputs. Use the [connector reference](../../docs/CONNECTOR_METADATA.md) for authored boundary/channel meanings, and [framework engineering](../../docs/FRAMEWORK_ENGINEERING.md) for shared implementation contracts. Keep unchanged measurements and original manual observations intact during a presentation refresh.
4. At the documentation stage, use the [creation checklist](../../docs/WORKFLOW_DOCUMENTATION_GENERATION.md#3-creation-checklist-and-output-files) to finish required source files, artwork, README/TESTING chapters, and evidence. Inspect generated pictures and authored instructions; a pending scaffold or valid file layout is an unfinished handoff. Follow the workflow's final packaging stage after the documentation is final.

If required native inputs, an implementation adapter, or a matching verified build is unavailable, identify that exact dependency. Complete work that does not depend on it, and report the remaining stage explicitly. Do not substitute a copied example's measurements, a rendering, or a different source version for the missing evidence.

<a id="generate-documentation-and-artwork"></a>

<a id="3-generate-documentation-and-artwork"></a>

## 3. Verify and hand over

For the completed source candidate, run the [documentation check](../../docs/WORKFLOW_DOCUMENTATION_GENERATION.md#31-check-documentation-without-changing-it), the applicable domain and saved-resource checks, and the repository test command required by `AGENTS.md`. Report checks actually executed, their results, and explicit skips. Documentation checks establish structure and links; they do not establish game operation. Use [TESTING](../../docs/TESTING.md) only for matching human-confirmed observations, and preserve original observations when changed image-review cases need rebinding.

Hand over the exact subject ID and readable name, the changed sources and authored documents, the relevant canonical pictures, the verified build or package if produced, and the remaining evidence limits. For an assembly, include the reusable-type list and placement mapping. State whether the result is source-only, compiled and checked, installed, or game-tested, and identify any incomplete stage. Building, installing, and publishing remain separate actions within the user's authorization; only the human maintainer merges a pull request.
