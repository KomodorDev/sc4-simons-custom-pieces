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
│   ├── WORKFLOW_DOCUMENTATION_GENERATION.md Generate README files, artwork, exports, and cards
│   ├── CONNECTOR_METADATA.md              Meaning of connection data and matching rules
│   ├── BUILD_AND_INSTALL.md               Operate build, install, and package commands
│   ├── FRAMEWORK_ENGINEERING.md           Shared implementation contracts
│   ├── TESTING.md                         Interpret and record exact observations
│   └── RELEASE.md                         Public distribution requirements
├── domains/<domain>/
│   ├── README.md                     Player guide and generated navigation
│   ├── AGENTS.md                     Domain-specific agent instructions
│   ├── NETWORK_SPEC.md               Measured network facts and implementation map, where implemented
│   ├── 00_pieces/
│   │   ├── INVENTORY.md               Generated illustrated type catalogue
│   │   └── <piece>/README.md          Piece-specific manual and generated checks
│   └── 01_assemblies/
│       ├── INVENTORY.md               Generated illustrated assembly catalogue
│       └── <assembly>/
│           ├── README.md             Rebuilding instructions for this layout
│           └── TESTING.md            This layout's evidence and scoped checks
└── skills/network-assembly-design/
    └── SKILL.md                      Agent entry point linking the human procedures
```

The `00_` and `01_` prefixes keep pieces and assemblies first in a name-sorted folder view. Repeated instances share a reusable type and its canonical images; placement labels belong to the assembly. Planner has its own [README](../scp-planner/README.md) and consumes library exports.

## Three levels of documentation

A **domain** is one network family, such as high-speed rail. Shared procedures and rules live in `docs/`: the two creation workflows describe the sequence of work, the [documentation-generation workflow](docs/WORKFLOW_DOCUMENTATION_GENERATION.md) owns artwork and README production, [framework engineering](docs/FRAMEWORK_ENGINEERING.md) owns shared implementation contracts, and [connector metadata](docs/CONNECTOR_METADATA.md) owns boundary data and matching semantics.

An implemented domain's `NETWORK_SPEC.md` contains its measured network values, audited donors, particular limitations, and implementation map. The [HSR specification](domains/high-speed-rail/NETWORK_SPEC.md) supplies those rail facts; the reserved highway domain has no implemented specification yet. Generic image, coordinate, and resource rules belong in the shared guides. A piece's particular dimensions, supports, route contracts, and exceptions belong with its existing README, checks, and evidence; an assembly's placements and decisions belong with that assembly. Deliberate worked examples can remain in shared references with links to their authoritative sources.

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
| Optional domain `menu-layout.json` | Explicitly selected menu experiments, assembly membership policy, presentation names, and locally reserved presentation IDs; normal builds keep their existing menu layout. See [the menu experiment](docs/BUILD_AND_INSTALL.md#try-the-trumpet-menu-experiment). |
| `config/allocations.json`, `config/profiles/`, and `config/release.json` | Identifier ownership, audited dependency contracts, and release requirements. |
| `00_pieces/<piece>/piece.json`, plus `geometry.json` where needed | Definition, resource identities, and local geometry source for one reusable type. |
| `01_assemblies/<assembly>/assembly.json` | Placed instances, stable labels, positions, and rotations. |
| Subject `connections.json` | Intrinsic directional interfaces, permitted journeys, forbidden transfers, and resource fingerprints extracted from the subject's actual resources. Historical records can retain deprecated endpoint shortlists; current extraction does not discover neighbours. |
| Subject `connector-groups.jsonc` and optional domain `connector-profiles.json` | Authored connector associations and shared defaults; meanings and file versions belong to the [connector reference](docs/CONNECTOR_METADATA.md). |
| Subject `connector-data.json` | Generated resolved consumer data; generation and freshness belong to [documentation generation](docs/WORKFLOW_DOCUMENTATION_GENERATION.md). |
| `schemas/connector-*.schema.json`; `framework/scp/connector_metadata.py` and `jsonc.py` | Source-format rules, parsing, cross-file validation, and export. |
| Subject `checks/manual-tests.json` | Authoritative record of scoped observations; follow [TESTING](docs/TESTING.md). |
| Subject `checks/` and `evidence/` | Contracts, measurement rationale, and current verification/render evidence. |
| Subject `preview.png`, `preview-thumb.png`, `preview-top.png` where present, and `icon.png`; assembly `previews/` | Canonical type artwork and layout views under the [documentation-generation workflow](docs/WORKFLOW_DOCUMENTATION_GENERATION.md); icon encoding belongs to [framework engineering](docs/FRAMEWORK_ENGINEERING.md#icon-encoding-and-maintenance). |
| Subject `evidence/preview.json` and `evidence/preview-top.json` | Independent angled/top source, camera, local-grid, common-header, and image fingerprints; the generic selected-view renderer owns both. |
| Subject `connection-overview.png` and `evidence/connection-overview.json` | Generated boundary cards and provenance, documented in [documentation generation](docs/WORKFLOW_DOCUMENTATION_GENERATION.md). |
| Domain `assets/figures/` | Shared reference images explained in the player guide. |
| `framework/scp/` and `tests/` | Shared, transport-neutral tools and tests. |
| Domain `implementation/`, `tools/`, and `tests/`; assembly `tests/` | Network-specific generation and independent checks with their owning domain or layout. |
| `local/` | Private workstation settings, supported native inputs, and rebuildable working data. |
| `dist/` | Disposable builds and exports; source definitions and observations live with their owners. |

## Generated views

A **generated section** sits between named HTML comment markers and is replaced by its generator. Keep authored explanations outside those markers. Subject summaries, connection tables, checklists, and catalogues derive from their source records; edit those records or the owning generator. The `CONNECTOR OVERVIEW` block and its related outputs follow [documentation generation](docs/WORKFLOW_DOCUMENTATION_GENERATION.md).

A **prose-only refresh** updates generated views without changing measured connection or observation bytes. Actual resource changes require extraction and relevant evidence refresh under [framework engineering](docs/FRAMEWORK_ENGINEERING.md#documentation-generation-and-observations). Preserve original backups and frozen evidence. Current evidence stays with the retained subject it verifies; explicitly deleted subjects do not retain obsolete compatibility copies.

A piece has one README, and an assembly has README plus TESTING. Keep shared procedures in `docs/`, and link their authoritative explanation. The [skill](skills/network-assembly-design/SKILL.md) routes agent tasks to those procedures.

Compatibility discovery is a separate Planner consumer operation over current, source-validated connector exports. Its eligibility, excluded-source reasons, pairwise candidates, and reports belong in `scp-planner/`; they do not become authored neighbour lists or required manual checkboxes in piece definitions. Unmigrated pieces retain their existing registration and build eligibility without being described as compatible or incompatible by that discovery operation.
