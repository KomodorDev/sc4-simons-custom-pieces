---
title: "Project documentation conventions"
summary: "Preserve the user's Markdown source-formatting preference across project guides and documentation generators."
audience: "Coding agents"
document_type: "agent-instructions"
---

# Project documentation conventions

- Write each prose paragraph on one physical source line. Let the editor or viewer wrap it to the available screen width; do not insert line breaks at a fixed character count.
- Apply the shared Markdown metadata convention in [custom-pieces/STRUCTURE.md](custom-pieces/STRUCTURE.md#markdown-metadata) to maintained non-piece guides, agent instructions, skills, catalogues, and assembly documents in the library and Planner. Preserve compatible skill front matter and generated headers; leave individual piece manuals and frozen/imported evidence in their existing format.
- Separate paragraphs with blank lines. Preserve the required structure and intentional breaks in headings, lists, tables, code blocks, quoted material and embedded markup.
- Documentation generators must emit the same paragraph style. Python source may wrap string literals for readability as long as the generated Markdown paragraph stays on one line.
- For Git and GitHub work, use [the repository workflow](docs/GITHUB.md). Preserve the existing local working paths and ignored game inputs; keep maintained source, canonical artwork, and evidence in Git. Run `python3 -B tools/run_tests.py` for the shared library and Planner checks, report skips accurately, and keep building, installing, and publishing separate.
- Preserve original backup snapshots, imported third-party documentation and frozen evidence. Apply formatting changes to maintained documents and current generated views.
- For custom-piece work, also read [custom-pieces/AGENTS.md](custom-pieces/AGENTS.md).
- The custom-piece library owns connector authoring, source schemas and validation, generated exports, and canonical artwork. Read [its connector reference](custom-pieces/docs/CONNECTOR_METADATA.md) for data meanings and [documentation-generation workflow](custom-pieces/docs/WORKFLOW_DOCUMENTATION_GENERATION.md) for README files, renders, exports, and cards. Shared rules live above domains in `custom-pieces/docs/`; network measurements live in the owning `NETWORK_SPEC.md`, where implemented. SCP Planner consumes those exports and owns application placement and reports; do not create a second authoring or measurement workflow there.
