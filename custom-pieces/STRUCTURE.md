---
title: "Framework structure and ownership"
summary: "Separate shared rules, network specifications, and individual subjects, and map maintained files and generated views to their owners."
audience: "Authors and maintainers"
document_type: "reference"
---

# Framework structure and ownership

Start with the [root README](README.md) to choose a task. Browse the [rail player guide](domains/high-speed-rail/README.md), [piece inventory](domains/high-speed-rail/00_pieces/INVENTORY.md), or [assembly inventory](domains/high-speed-rail/01_assemblies/INVENTORY.md) for current content. This page identifies where information belongs; the linked procedures explain how to change it.

## Markdown structure

```text
custom-pieces/
├── README.md                         Human starting page
├── AGENTS.md                         Short agent instructions
├── STRUCTURE.md                      File ownership and document conventions
├── docs/
│   ├── WORKFLOW_PIECE_CREATION.md          Create or revise one reusable piece
│   ├── WORKFLOW_ASSEMBLY_CREATION.md       Design a layout made from several pieces
│   ├── WORKFLOW_DOCUMENTATION_GENERATION.md Generate README/TESTING documents, artwork, exports, and cards
│   ├── CONNECTOR_METADATA.md              Meaning of connection data and matching rules
│   ├── INSTALLER.md                       Use the self-contained graphical installer
│   ├── AUTOMATIC_RELEASES.md              Understand GitHub checks, installer downloads, and local building
│   ├── BUILD_AND_INSTALL.md               Operate build, install, and package commands
│   ├── FRAMEWORK_ENGINEERING.md           Shared implementation contracts
│   ├── TESTING.md                         Interpret and record exact observations
│   ├── RELEASE.md                         Public distribution requirements
│   └── templates/                        Unregistered starter source, not catalogue content
├── domains/<domain>/
│   ├── README.md                     Player guide and generated navigation
│   ├── AGENTS.md                     Domain-specific agent instructions
│   ├── NETWORK_SPEC.md               Measured network facts and implementation map, where implemented
│   ├── 00_pieces/
│   │   ├── INVENTORY.md               Generated illustrated type catalogue
│   │   └── <piece>/
│   │       ├── README.md             Views, placement, and intrinsic movement matrix
│   │       └── TESTING.md            Scope, preparation, evidence, and exact checks; legacy guides can remain combined
│   └── 01_assemblies/
│       ├── INVENTORY.md               Generated illustrated assembly catalogue
│       └── <assembly>/
│           ├── README.md             Rebuilding instructions for this layout
│           └── TESTING.md            This layout's evidence and scoped checks
└── skills/network-assembly-design/
    └── SKILL.md                      Agent entry point linking the human procedures
```

The `00_` and `01_` prefixes keep pieces and assemblies first in a name-sorted folder view. Repeated instances share a reusable type and its canonical images; placement labels belong to the assembly.

## Three levels of documentation

A **domain** is one network family, such as high-speed rail. Shared procedures and rules live in `docs/`: the two creation workflows describe the sequence of work, the [documentation-generation workflow](docs/WORKFLOW_DOCUMENTATION_GENERATION.md) owns artwork and README production, [framework engineering](docs/FRAMEWORK_ENGINEERING.md) owns shared implementation contracts, and [connector metadata](docs/CONNECTOR_METADATA.md) owns boundary data and matching semantics.

An implemented domain’s `NETWORK_SPEC.md` contains its measured network values, audited donors, particular limitations, and implementation map. The [HSR specification](domains/high-speed-rail/NETWORK_SPEC.md) supplies those rail facts; the reserved highway domain has no implemented specification yet. Generic image, coordinate, and resource rules belong in the shared guides. A piece’s function and placement belong in its README; detailed dimensions, supports, route contracts, exceptions, and test evidence belong in its TESTING document, checks, and evidence. Legacy combined guides keep their existing content until intentionally migrated. An assembly’s placements and decisions belong with that assembly. Deliberate worked examples can remain in shared references with links to their authoritative sources.

Use the root README to select one workflow. Read technical references when that step needs their facts. `AGENTS.md` and `SKILL.md` route the task and preserve essential constraints; they link the detailed procedure instead of maintaining another copy.

## Markdown metadata

A **metadata header**, also called YAML front matter, is the block between `---` lines at the beginning of a Markdown file. Maintained shared guides, agent instructions, catalogues, and assembly documents use these four fields. Individual piece READMEs retain their existing subject format; imported documentation, private working reports, archived evidence, and disposable build copies are outside this editing policy.

| Field | Meaning |
| --- | --- |
| `title` | The document's human-readable name. |
| `summary` | A short explanation of what this document covers and when to use it. |
| `audience` | The intended readers, such as players, piece authors, or maintainers. |
| `document_type` | Its role, such as procedure, reference, catalogue, or agent instructions. |

These fields describe the document; piece and connector data retain their own authoritative JSON records. Keep each field on one physical line, and avoid repeating the summary in a separate `Purpose:` paragraph. `SKILL.md` retains its required top-level `name` and `description`; its four document fields live inside the supported `metadata` mapping. Generated catalogues obtain their headers from their generator, so regeneration preserves the convention.

## Source and data ownership

| Location | Purpose |
| --- | --- |
| `project.json`, domain `domain.json`, and `collections.json` | Explicit project/domain registries and named build selections. |
| Domain `menu-layout.json` | Assembly membership, component-cycle order, the single assembly-button presentation, and locally reserved IDs. Ordinary piece compilation supplies the inputs; [assembly-menu packaging](docs/BUILD_AND_INSTALL.md#prepare-the-assembly-menu) prepares every final assembly menu. |
| `config/allocations.json`, `config/profiles/`, and `config/release.json` | Identifier ownership, audited dependency contracts, and compiled-plugin release requirements. |
| `config/installer.json` | Experimental local-builder distribution policy, complete implemented-catalogue selection, assembly presentation, supported game profile, installer platforms, and release provenance requirements. It does not change `config/release.json` or manual observations. |
| `00_pieces/<piece>/piece.json`, plus `geometry.json` where needed | Definition, resource identities, and local geometry source for one reusable type. |
| `01_assemblies/<assembly>/assembly.json` | Placed instances, stable labels, positions, and rotations. |
| Subject `connections.json` | Intrinsic directional interfaces, permitted journeys, forbidden transfers, and resource fingerprints extracted from the subject's actual resources. Historical records can retain deprecated endpoint shortlists; current extraction does not discover neighbours. |
| Subject `connector-groups.jsonc` and optional domain `connector-profiles.json` | Authored connector associations and shared defaults; meanings and file versions belong to the [connector reference](docs/CONNECTOR_METADATA.md). |
| Subject `connector-data.json` | Generated resolved consumer data; generation and freshness belong to [documentation generation](docs/WORKFLOW_DOCUMENTATION_GENERATION.md). |
| `schemas/connector-*.schema.json`; `framework/scp/connector_metadata.py` and `jsonc.py` | Source-format rules, parsing, cross-file validation, and export. |
| Subject `checks/manual-tests.json` | Authoritative record of scoped observations; follow [TESTING](docs/TESTING.md). |
| Subject `checks/` and `evidence/` | Contracts, measurement rationale, and current verification/render evidence. |
| Subject `icon.png`, beside `piece.json` or `assembly.json` | Canonical four-state menu icon for that reusable piece or assembly button; icon encoding belongs to [framework engineering](docs/FRAMEWORK_ENGINEERING.md#icon-encoding-and-maintenance). |
| Subject `previews/` | Canonical documentation images: a piece's `preview.png`, `preview-thumb.png`, `preview-top.png` where present, and `connection-overview.png` where supported, or an assembly's complete-layout views. The [documentation-generation workflow](docs/WORKFLOW_DOCUMENTATION_GENERATION.md) owns their generation. |
| Subject `evidence/preview.json` and `evidence/preview-top.json` | Independent angled/top source, camera, local-grid, common-header, and image fingerprints; the generic selected-view renderer owns both. |
| Piece `previews/connection-overview.png` and `evidence/connection-overview.json` | Generated boundary cards and their separate provenance, documented in [documentation generation](docs/WORKFLOW_DOCUMENTATION_GENERATION.md). |
| Domain `assets/figures/` | Shared reference images explained in the player guide. |
| `docs/templates/` | Unregistered authoring examples. Copy and deliberately register a starter through its documented procedure; files here are not piece or assembly entries and reserve no game identities. |
| `framework/scp/` and `tests/` | Shared, transport-neutral tools and tests. |
| `installer/`, including `installer/scp_installer/service.py` | Graphical installer, self-contained bundle construction, publication checks, and orchestration of the existing resource audit, build, verification, assembly-menu, and receipt-based installation tools. |
| Domain `implementation/`, `tools/`, and `tests/`; assembly `tests/` | Network-specific generation and independent checks with their owning domain or layout. |
| `local/` | Private workstation settings, supported native inputs, and rebuildable working data. |
| `dist/` | Disposable builds and exports; source definitions and observations live with their owners. |

The repository-level `.github/workflows/installer-release.yml` checks the Windows x64 installer bundle. Pull requests produce review artifacts; accepted `main` pushes publish experimental installer prereleases only after the workflow's full test, packaged executable self-test, GUI startup smoke check, and archive checks pass. The [contributor workflow](https://github.com/KomodorDev/sc4-simons-custom-pieces/blob/dev/docs/GITHUB.md#automatic-installer-prereleases) owns that process, and the [installer guide](docs/INSTALLER.md) owns player steps. Downloadable installers contain the local builder and its runtime; native game resources are read and compiled on the user's computer.

## Generated views

For a new subject, use the [stage-by-stage creation checklist](docs/WORKFLOW_DOCUMENTATION_GENERATION.md#creation-checklist-and-output-files) to distinguish required and conditional files, authored inputs, generated outputs, and their producing commands. The source map above describes ownership; the checklist describes when each file must exist. The [small HSR assembly starter](docs/WORKFLOW_ASSEMBLY_CREATION.md#start-a-small-hsr-assembly-from-existing-pieces) demonstrates the separate plan, domain registration, menu registration, and first-population steps without allocating another reusable type.

A **generated section** sits between named HTML comment markers and is replaced by its generator. Keep authored explanations outside those markers. Subject summaries, intrinsic movement matrices, connection tables, checklists, and catalogues derive from their source records; edit those records or the owning generator. The numbered piece layout, `PIECE CONNECTION MATRIX`, `CONNECTOR OVERVIEW`, and related outputs follow [documentation generation](docs/WORKFLOW_DOCUMENTATION_GENERATION.md#piece-readme).

A **prose-only refresh** updates generated views without changing measured connection or observation bytes. Actual resource changes require extraction and relevant evidence refresh under [framework engineering](docs/FRAMEWORK_ENGINEERING.md#documentation-generation-and-observations). Preserve original backups and frozen evidence. Current evidence stays with the retained subject it verifies; explicitly deleted subjects do not retain obsolete compatibility copies.

Run `python3 -B custom-pieces/scp.py docs-check` from the repository root for the read-only catalogue and shared-guide structure/link check; use repeated `--piece EXACT-ID` or `--assembly EXACT-ID` selectors for a subject selection. Legacy guides are reported explicitly and retained. This check does not generate missing evidence, validate native game resources, or record a manual observation.

New or intentionally refreshed pieces and assemblies have README plus TESTING. A split piece README contains three numbered chapters and a separate Testing link; its TESTING document follows the [shared six-chapter layout](docs/WORKFLOW_DOCUMENTATION_GENERATION.md#required-piece-and-assembly-testing-layout). The markers are `<!-- PIECE README LAYOUT: 2 -->` and `<!-- PIECE TESTING LAYOUT: 1 -->`; legacy combined piece guides, including version 1, remain unchanged until explicitly migrated. The content generator preserves authored chapters during refresh. Keep shared procedures in `docs/`, and link their authoritative explanation. The [skill](skills/network-assembly-design/SKILL.md) routes agent tasks to those procedures.

Automatic compatibility discovery is outside the current library commands. A future consumer must use current, source-validated connector exports and keep its eligibility decisions, excluded-source reasons, pairwise candidates, and reports separate from the authored library. Consumer results do not become authored neighbour lists or required manual checkboxes in piece definitions. Unmigrated pieces retain their existing registration and build eligibility without being described as compatible or incompatible.
