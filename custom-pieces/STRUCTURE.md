---
title: "Framework structure and ownership"
summary: "Separate shared rules, network specifications, and individual subjects, and map maintained files and generated views to their owners."
audience: "Authors and maintainers"
document_type: "reference"
---

# Framework structure and ownership

<!-- BEGIN DOCUMENT NAVIGATION -->
[1. Markdown structure](#1-markdown-structure) · [2. Three levels of documentation](#2-three-levels-of-documentation) · [3. Markdown metadata](#3-markdown-metadata) · [4. Markdown heading numbering and navigation](#4-markdown-heading-numbering-and-navigation) · [5. Source and data ownership](#5-source-and-data-ownership) · [6. Generated views](#6-generated-views)
<!-- END DOCUMENT NAVIGATION -->

Start with the [library README](README.md) to choose a task. The repository README, one directory above the library in a full clone, covers source checkout, Python setup, and contributing. Browse the [rail player guide](domains/high-speed-rail/README.md), [piece inventory](domains/high-speed-rail/00_pieces/INVENTORY.md), or [assembly inventory](domains/high-speed-rail/01_assemblies/INVENTORY.md) for current content. This page identifies where information belongs; the linked procedures explain how to change it.

<a id="markdown-structure"></a>

## 1. Markdown structure

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
│   ├── NAMING_CONVENTIONS.md              Folder identifiers, readable names, and migration rules
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
└── skills/network-piece-and-assembly-design/
    └── SKILL.md                      Agent execution checklist and workflow links
```

The `00_` and `01_` prefixes keep pieces and assemblies first in a name-sorted folder view. Repeated instances share a reusable type and its canonical images; placement labels belong to the assembly.

<a id="three-levels-of-documentation"></a>

## 2. Three levels of documentation

A **domain** is one network family, such as high-speed rail. Shared procedures and rules live in `docs/`: the two creation workflows describe the sequence of work, the [naming conventions](docs/NAMING_CONVENTIONS.md) own folder identifiers and readable piece and assembly names, the [documentation-generation workflow](docs/WORKFLOW_DOCUMENTATION_GENERATION.md) owns artwork and README production, [framework engineering](docs/FRAMEWORK_ENGINEERING.md) owns shared implementation contracts, and [connector metadata](docs/CONNECTOR_METADATA.md) owns boundary data and matching semantics.

An implemented domain’s `NETWORK_SPEC.md` contains its measured network values, audited donors, particular limitations, and implementation map. The [HSR specification](domains/high-speed-rail/NETWORK_SPEC.md) supplies those rail facts; the reserved highway domain has no implemented specification yet. Generic image, coordinate, and resource rules belong in the shared guides. A piece’s function and placement belong in its README; detailed dimensions, supports, route contracts, exceptions, and test evidence belong in its TESTING document, checks, and evidence. Legacy combined guides keep their existing content until intentionally migrated. An assembly’s placements and decisions belong with that assembly. Deliberate worked examples can remain in shared references with links to their authoritative sources.

Use the library README to select one workflow. Read technical references when that step needs their facts. `AGENTS.md` supplies the rules that apply to work in its directory, and `SKILL.md` supplies the agent's task-selection and completion checklist. The detailed human procedure remains in its owning workflow.

### 2.1 Document names and reading order

The **entry point** is the first document for a particular reader or task. A **workflow** gives an ordered procedure. A **reference** supplies facts when a procedure needs them. Keep these roles distinct so a reader can continue a selected task without repeatedly returning to another entry point.

| File or location | Purpose and reader | When to open it |
| --- | --- | --- |
| Repository `README.md` | Project introduction, checkout, Python environment, and contributor links. | Start here for a new clone or development environment. |
| Library `README.md` | Content browsing and the human task-to-workflow index. | Choose the piece, assembly, documentation, or maintenance task once. |
| Domain `README.md` and `INVENTORY.md` | Player placement/menu guidance and generated content catalogues. | Browse types, understand their use, or select existing assembly members. |
| `AGENTS.md` at repository, library, and domain levels | Instructions and constraints for coding agents working in that directory. | Apply the relevant parent and domain instructions; do not restart task selection when a child file links to a parent already read. |
| `skills/<skill-name>/SKILL.md` | Agent execution checklist: identify the task, gather its inputs, follow the human workflow, and report its verified outputs. | Use for piece and assembly design. Human authors can open the workflow directly. |
| `docs/WORKFLOW_<TASK>.md` | The authoritative ordered procedure for that task. | Follow the selected workflow, opening linked references at the step that needs them. |
| `STRUCTURE.md` | Document conventions, file locations, and ownership. | Find where information belongs or decide how to name a document. |
| `docs/NAMING_CONVENTIONS.md` | Folder identifiers and readable names for pieces and assemblies. | Name a new subject or plan an explicitly scoped name migration. |
| Domain `NETWORK_SPEC.md` | Measured network facts and the domain implementation map. | Find actual interfaces, donor inputs, and implementation entry points. |
| Other topic guides under `docs/` | Shared references or focused operator procedures, such as connector semantics, build commands, observations, and release requirements. | Read the topic required by the current workflow step. |
| Subject `README.md` and `TESTING.md` | One piece's or assembly's usage, exact checks, evidence, and limits. | Inspect an existing subject or document the one being authored. |

Preserve the established role filenames `README.md`, `AGENTS.md`, `SKILL.md`, `STRUCTURE.md`, `NETWORK_SPEC.md`, `INVENTORY.md`, and `TESTING.md`. Their directories identify their scope. Name additional shared guides with a descriptive uppercase topic and underscores, such as `CONNECTOR_METADATA.md`; use `WORKFLOW_` only for an ordered authoring procedure. Give every maintained document a specific human-readable title. Ordinary guides use the same title in their metadata; skills follow the compatible header exception below. In particular, the repository introduction and library workflow index should have distinct titles even though both files are named `README.md`.

Keep one authoritative owner for each detailed rule. A skill may link to human procedures, but it must also state the agent's task inputs, execution order, and completion report; copying the procedure or merely sending the reader back to another router adds no useful step. Domain instructions add network-specific constraints and continue the selected workflow. Keep current chapter links and aliases when reorganizing maintained content, and preserve imported documentation and frozen evidence.

<a id="markdown-metadata"></a>

## 3. Markdown metadata

A **metadata header**, also called YAML front matter, is the block between `---` lines at the beginning of a Markdown file. Maintained shared guides, agent instructions, catalogues, and assembly documents use these four fields. Skills use the compatible flat header described below. Individual piece READMEs retain their existing subject format; imported documentation, private working reports, archived evidence, and disposable build copies are outside this editing policy.

| Field | Meaning |
| --- | --- |
| `title` | The document's human-readable name. |
| `summary` | A short explanation of what this document covers and when to use it. |
| `audience` | The intended readers, such as players, piece authors, or maintainers. |
| `document_type` | Its role, such as procedure, reference, catalogue, or agent instructions. |

These fields describe the document; piece and connector data retain their own authoritative JSON records. Keep each field on one physical line, and avoid repeating the summary in a separate `Purpose:` paragraph. Generated catalogues obtain their headers from their generator, so regeneration preserves the convention.

`SKILL.md` is a format exception: keep a flat header with the skill's required `name` and `description`, using quoted string values just like ordinary guide fields. The `name` matches its containing folder, and the first-level Markdown title gives its human-readable name. The description supplies its purpose and scope. State the audience and document type in a brief body line below the chapter navigation. Do not add the four ordinary document fields as unsupported top-level skill keys or duplicate them inside a nested `metadata` object; the flat header avoids presenting a nested object in the document's metadata panel. Preserve any other supported skill fields when an actual skill capability needs them.

For this library's piece and assembly skill, the header is:

```yaml
---
name: "network-piece-and-assembly-design"
description: "Design, revise, atomize, document, and verify reusable SimCity 4 network pieces and multi-piece assemblies through the library's measured authoring workflows."
---
```

<a id="markdown-heading-numbering-and-navigation"></a>

## 4. Markdown heading numbering and navigation

A **heading** labels a section of a document. In Markdown source, one `#` introduces the document title, two introduce a chapter, three introduce a subsection, and each additional `#` introduces one deeper level. Apply the following convention to maintained repository documentation, shared guides, agent instructions, skills, domain guides, and catalogues. Piece and assembly manuals keep their existing subject layouts during the current shared-document migration; preserve their content and update them only through an explicitly requested subject migration or refresh. Imported third-party documentation, original backup snapshots, frozen evidence, private working reports, and disposable build copies remain outside this formatting policy.

1. Keep one unnumbered first-level title, such as `# Framework structure and ownership`. Keep YAML front matter above that title. Introductory paragraphs, metadata fields, and the navigation paragraph do not receive chapter numbers of their own.
2. Number every second-level chapter consecutively from **1**, using a period and a space after the number: `## 1. Prepare the sources`, `## 2. Build the piece`, and `## 3. Check the result`. A prerequisite or decision chapter is chapter 1; do not start a document at 0. Numbering follows document order and does not restart midway through a file.
3. Number subsections by their parent chapter, followed by a period and the subsection number: `### 2.1 Select the inputs` and `### 2.2 Build the output`. A deeper subsection extends that number, such as `#### 2.2.1 Inspect the build receipt`. Reset each child counter to 1 under a new parent, keep heading levels consecutive, and do not add a trailing period to a subsection number.
4. Put a navigation paragraph immediately below the title and any required layout marker, before the introduction. Link every second-level chapter once, in document order, with the exact numbered chapter title as the link text. Separate links with ` · ` on one physical source line, matching the established piece and assembly README navigation. Do not add subsection links or a separate numbered Contents chapter. A necessary link to another document, such as a subject's separate TESTING document, may follow the chapter links with an explicit label.
5. Link navigation entries to the anchors derived from the numbered headings. An **anchor** identifies a position inside a page; `#2-build-the-piece` selects `## 2. Build the piece`. When changing an existing heading, preserve an explicit anchor that already identifies it, or add an HTML alias immediately before it for the old heading anchor, so existing links remain usable. New navigation uses the numbered heading anchor; an alias is not an additional chapter or navigation entry.
6. Treat example headings inside fenced code blocks, literal commands, quoted source material, and frozen evidence as content rather than document structure. Keep list numbering separate from heading numbering. Section numbers do not rename files, folders, piece identifiers, assembly identifiers, or placement labels.
7. For generated catalogues or generated sections, change the owning generator so regeneration retains chapter numbers, subsection numbers, navigation, and preserved anchors. Keep authored explanations outside generated markers, and verify the generated result instead of applying a formatting change only to a disposable output.

For example, this document has two linked chapters, two subsections inside chapter 2, and one deeper subsection. Its title and introduction remain unnumbered, and its navigation links only the chapters:

```markdown
# Example guide

[1. Prepare the sources](#1-prepare-the-sources) · [2. Build the piece](#2-build-the-piece)

This introduction explains when to use the guide.

## 1. Prepare the sources

Check the source records before building.

<a id="build-the-piece"></a>
## 2. Build the piece

### 2.1 Select the inputs

Choose the exact piece identifier.

### 2.2 Build the output

Run the documented build command.

#### 2.2.1 Inspect the build receipt

Check the receipt before continuing.
```

The alias `build-the-piece` in this example preserves a link written before chapter 2 acquired its number. Keep any existing section aliases needed by current local or external references when maintaining a real document.

<a id="source-and-data-ownership"></a>

## 5. Source and data ownership

| Location | Purpose |
| --- | --- |
| `project.json`, domain `domain.json`, and `collections.json` | Explicit project/domain registries and named build selections. |
| Domain `menu-layout.json` | Assembly membership, component-cycle order, the single assembly-button presentation, and locally reserved IDs. Ordinary piece compilation supplies the inputs; [assembly-menu packaging](docs/BUILD_AND_INSTALL.md#8-prepare-the-assembly-menu) prepares every final assembly menu. |
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
| Subject `icon.png`, beside `piece.json` or `assembly.json` | Canonical four-state menu icon for that reusable piece or assembly button; icon encoding belongs to [framework engineering](docs/FRAMEWORK_ENGINEERING.md#91-icon-encoding-and-maintenance). |
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

<a id="generated-views"></a>

## 6. Generated views

For a new subject, use the [stage-by-stage creation checklist](docs/WORKFLOW_DOCUMENTATION_GENERATION.md#3-creation-checklist-and-output-files) to distinguish required and conditional files, authored inputs, generated outputs, and their producing commands. The source map above describes ownership; the checklist describes when each file must exist. The [small HSR assembly starter](docs/WORKFLOW_ASSEMBLY_CREATION.md#12-start-a-small-hsr-assembly-from-existing-pieces) demonstrates the separate plan, domain registration, menu registration, and first-population steps without allocating another reusable type.

A **generated section** sits between named HTML comment markers and is replaced by its generator. Keep authored explanations outside those markers. Subject summaries, intrinsic movement matrices, connection tables, checklists, and catalogues derive from their source records; edit those records or the owning generator. The numbered piece layout, `PIECE CONNECTION MATRIX`, `CONNECTOR OVERVIEW`, and related outputs follow [documentation generation](docs/WORKFLOW_DOCUMENTATION_GENERATION.md#121-piece-readme).

A **prose-only refresh** updates generated views without changing measured connection or observation bytes. Actual resource changes require extraction and relevant evidence refresh under [framework engineering](docs/FRAMEWORK_ENGINEERING.md#11-documentation-generation-and-observations). Preserve original backups and frozen evidence. Current evidence stays with the retained subject it verifies; explicitly deleted subjects do not retain obsolete compatibility copies.

Run `python3 -B custom-pieces/scp.py docs-check` from the repository root for the read-only catalogue and shared-guide structure/link check; use repeated `--piece EXACT-ID` or `--assembly EXACT-ID` selectors for a subject selection. Legacy guides are reported explicitly and retained. This check does not generate missing evidence, validate native game resources, or record a manual observation.

New subjects and guides deliberately migrated to the split layout have README plus TESTING. A split piece README contains three numbered chapters and a separate Testing link; its TESTING document follows the [shared six-chapter layout](docs/WORKFLOW_DOCUMENTATION_GENERATION.md#123-required-piece-and-assembly-testing-layout). The markers are `<!-- PIECE README LAYOUT: 2 -->` and `<!-- PIECE TESTING LAYOUT: 1 -->`; legacy combined piece guides, including version 1, remain unchanged until explicitly migrated. The content generator preserves authored chapters during refresh. Keep shared procedures in `docs/`, and link their authoritative explanation. The [skill](skills/network-piece-and-assembly-design/SKILL.md) routes agent tasks to those procedures.

Automatic compatibility discovery is outside the current library commands. A future consumer must use current, source-validated connector exports and keep its eligibility decisions, excluded-source reasons, pairwise candidates, and reports separate from the authored library. Consumer results do not become authored neighbour lists or required manual checkboxes in piece definitions. Unmigrated pieces retain their existing registration and build eligibility without being described as compatible or incompatible.
