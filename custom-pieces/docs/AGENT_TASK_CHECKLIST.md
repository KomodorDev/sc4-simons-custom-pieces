---
title: "Agent task checklist and handoff gate"
summary: "Adapt a reusable execution checklist to the selected workflow, track requirements and current evidence, and audit every item before handing over work."
audience: "Coding agents and reviewers"
document_type: "template"
---

# Agent task checklist and handoff gate

<!-- BEGIN DOCUMENT NAVIGATION -->
[1. Adapt and maintain the checklist](#1-adapt-and-maintain-the-checklist) · [2. Scope, instructions, and authorization](#2-scope-instructions-and-authorization) · [3. Investigation and design](#3-investigation-and-design) · [4. Implementation and source data](#4-implementation-and-source-data) · [5. Compiled resources and runtime behavior](#5-compiled-resources-and-runtime-behavior) · [6. Documentation, artwork, and generated outputs](#6-documentation-artwork-and-generated-outputs) · [7. Tests, evidence, and integrated review](#7-tests-evidence-and-integrated-review) · [8. Packaging, installation, and publication](#8-packaging-installation-and-publication) · [9. Final handoff gate](#9-final-handoff-gate)
<!-- END DOCUMENT NAVIGATION -->

This is the shared **execution checklist**: a working record of what an agent must do for one task. Adapt it to the selected workflow before implementation, update it during work, and audit every retained item before handoff. It does not replace the owning procedures, create permission for external actions, or supply game observations. The subject's `checks/manual-tests.json` remains the sole authority for human-confirmed game results under [TESTING](TESTING.md).

## 1. Adapt and maintain the checklist

### 1.1 Create one working copy

Keep one task checklist in the existing working brief or task plan. For a file that survives a resumed chat, use an ignored copy under `custom-pieces/local/task-checklists/`; do not add a second checklist page to every piece or assembly. Keep this shared template unchanged when recording an individual task's progress. Promote durable findings to their owning README, TESTING document, network specification, or evidence record, rather than making the working checklist another source of product facts.

To create a private file from the repository root, replace `example-task` with a descriptive task name and run the following command. On Windows, use `python` if that is the active environment's Python command. The command refuses to overwrite an existing file; reopen an existing task's copy when continuing its work.

```sh
python3 -c "from pathlib import Path; destination = Path('custom-pieces/local/task-checklists/example-task.md'); destination.parent.mkdir(parents=True, exist_ok=True); destination.open('x', encoding='utf-8').write(Path('custom-pieces/docs/AGENT_TASK_CHECKLIST.md').read_text(encoding='utf-8'))"
```

### 1.2 Fill the brief and tailor the work

Replace the following fields in the working copy. An **acceptance condition** is an observable result that shows a requirement was met. An **evidence reference** identifies the actual file, command result, image inspection, or scoped human observation supporting that condition.

| Field | Task-specific value |
| --- | --- |
| Task and intended outcome | Fill in the user's requested result. |
| Selected workflow and current stage | Link the owning procedure and record where work begins. |
| Subjects and scope | Exact IDs, files, domains, affected shared consumers, and exclusions. |
| Source baseline and current candidate | Branch, commit or source fingerprint, and build/package identity when applicable. |
| Preserved constraints | Accepted geometry, IDs, observations, artifacts, and user preferences. |
| Assembly modularity goals, when applicable | Useful module boundaries, extension points, intended future uses, and the evidence needed for each compatibility claim. |
| Existing authorization | Actions already authorized; any action whose authorization is genuinely missing. |
| Alignment order and approval, when applicable | First alignment, exact review candidate, agreed delivery stage, matching user acceptance reference or `WAITING`, and deferred other alignment. |
| Required delivery stage | Analysis, source change, verified build, installed candidate, game-tested result, or publication. |
| Working record and evidence locations | Task plan/checklist location and actual reports; keep private paths private. |
| Dependencies and pending decisions | Required input, responsible actor, next action, and the work that can proceed independently. |

Map every user requirement to concrete checklist items. Split a broad requirement into separately verifiable actions when needed, and add rows for requirements that this template does not cover. Preserve new user corrections and accepted decisions in this map during the task.

| Requirement | Concrete acceptance condition | Checklist item IDs | Current evidence or unresolved dependency |
| --- | --- | --- | --- |
| R1: replace with the actual requirement | Replace with a measurable result. | Replace with actual IDs. | Fill during work. |

Use chapters 2, 7, and 9 for every task. Select the other chapters according to the actual change: prose uses the relevant documentation rows; artwork adds image review; piece implementation adds source and saved-resource checks; assembly design or substantial revision adds atomization, expandability, future usefulness, member, and whole-layout checks under [the assembly reuse procedure](WORKFLOW_ASSEMBLY_CREATION.md#162-check-expandability-and-future-reuse); a reported bug adds reproduction and regression work; packaging, installation, and publication each apply only within their own scope and authorization. A prose-only task does not need geometry generation or a game installation merely to fill this template. Keep an explicit applicability record for omitted chapters or item ranges, with a scope-based reason; do not silently delete inconvenient requirements.

### 1.3 Track state and evidence honestly

The item IDs below remain stable in the working copy. Replace generic actions with the exact subjects, commands, outputs, and acceptance conditions. Append the state and evidence to each applicable row as it progresses. A checked box means the item has a reviewed resolution; its label must distinguish completed work from a justified exclusion.

| State | Checkbox and required meaning |
| --- | --- |
| `TODO` or `IN PROGRESS` | Keep `[ ]`. The acceptance condition is not yet established. |
| `DONE` | Use `[x]` only after the action is completed and its current evidence supports the stated scope. |
| `N/A` | Use `[x]` only with a concrete reason that the action does not apply to the authorized task. This records an exclusion, never a test pass. |
| `WAITING`, `FAILED`, or `STALE` | Keep `[ ]`, identify the dependency or failure, and name the next action. These states cannot close an applicable completion requirement. |

Examples: `- [x] E03 — DONE: inspected the actual final top-view PNG; evidence: the subject's current render record.` and `- [x] G04 — N/A: this task requests source documentation only; no installable package is being delivered.` A missing native input is `WAITING`, not `N/A` when the requested result requires that input. A skipped test remains a skip: the command-execution row may be done once its real results are recorded, while any required coverage missing from that run remains open separately. A shared recipe change requires assessing every affected subject, even if the user named only one assembly.

Update the checklist at stage boundaries, after delegated work returns, and before resuming from a saved brief. Reopen dependent rows whenever source, geometry, generated output, documentation, build bytes, or the tested environment changes in a way that invalidates their evidence. Use the owning workflow's freshness rules to decide the affected scope; do not repeat unrelated checks or invalidate game observations solely because prose changed. The final gate is a required agent review, not an automated CLI enforcement mechanism.

## 2. Scope, instructions, and authorization

- [ ] A01 — Restate the intended result and required delivery stage; map every user requirement and correction to acceptance conditions.
- [ ] A02 — Read the applicable repository, library, and domain instructions; continue the selected workflow at its current stage.
- [ ] A03 — Identify the authoritative source, generator, derived views, and evidence owner for each changed output using [STRUCTURE](../STRUCTURE.md#5-source-and-data-ownership).
- [ ] A04 — Inspect the existing branch, worktree, and local changes; preserve user work and choose the Git route under the [repository workflow](https://github.com/KomodorDev/sc4-simons-custom-pieces/blob/dev/docs/GITHUB.md).
- [ ] A05 — Record retained IDs, accepted geometry or layout, platform/profile, frozen evidence, and other constraints that the task must preserve.
- [ ] A06 — Adapt the applicable checklist sections, document exclusions, add task-specific items, and establish an executable order with dependencies.
- [ ] A07 — Reuse existing user authorization and available context; identify genuinely missing decisions without asking again for authorized routine work.
- [ ] A08 — Separate source work, building, installation, publication, external messages, and human-only merging; add only the stages requested or implied by the task.
- [ ] A09 — Give parallel contributors clear source ownership, dependencies, expected evidence, and an integration point; plan to review the combined result.
- [ ] A10 — When two alignment variants are needed, record [Alignment A first unless the user requests another order](WORKFLOW_PIECE_CREATION.md#alignment-production-order), the exact first candidate and agreed delivery stage, and the user's matching acceptance reference before producing the other alignment. Reuse existing matching acceptance; a general request for both variants, software checks, previews, and agent reviews do not supply it. Keep the other alignment `WAITING` until acceptance, including in delegated work.

## 3. Investigation and design

Apply the [piece workflow](WORKFLOW_PIECE_CREATION.md) or [assembly workflow](WORKFLOW_ASSEMBLY_CREATION.md) where the task needs actual design or implementation. For a prose or presentation refresh, start with the [documentation scope](WORKFLOW_DOCUMENTATION_GENERATION.md#1-choose-the-refresh-scope).

- [ ] B01 — Inspect the existing subject, implementation, observations, and known failures before proposing a change; separate facts, assumptions, and unknowns.
- [ ] B02 — For a reported defect, preserve its exact reported scope and failed candidate; reproduce it when possible, and distinguish reproduction from an inferred cause.
- [ ] B03 — Inspect the exact supported donor resources, versions, and joining interfaces; record input fingerprints and discovery limits instead of substituting a similar example.
- [ ] B04 — Apply the piece-versus-assembly and reuse decisions; justify any new type, allocation, or coordinated block.
- [ ] B05 — Establish intended and forbidden movements, directions, levels, footprint, supports, overhangs, and keep-clear space under the chosen layout.
- [ ] B06 — For requested atomization, provide the required coordinate-labelled line drawing, candidate cuts, measured obstacles, and persisted decisions.
- [ ] B07 — Preserve the accepted design in exact-layout work; record any authorized redesign bound and its actual measured effect separately.
- [ ] B08 — Choose the smallest useful experiment or regression that distinguishes the suspected cause; state which game or engine behavior it cannot establish.
- [ ] B09 — For assembly design or substantial revision, review atomization into independently useful modules; justify retained coordinated blocks, compare distinct types, placements, owned cells, overhangs, and support reservations, and preserve any required drawing and cut decisions through [the atomization workflow](WORKFLOW_ASSEMBLY_CREATION.md#16-atomize-to-the-smallest-useful-reusable-module).
- [ ] B10 — Establish future usefulness for each proposed reusable type with concrete alternate uses, existing candidates, or explicitly missing adapters; explain its independent function and benefit beyond one placement label under [the reuse procedure](WORKFLOW_ASSEMBLY_CREATION.md#162-check-expandability-and-future-reuse).
- [ ] B11 — Define the assembly's intended extension or replacement points, complete required interfaces, source-backed geometry standards, construction method, and usable surrounding space; separate verified options, conditional proposals, and unknowns without expanding the authorized design.
- [ ] B12 — For diagonal crossings, measure the required grid alignments separately from rotation; compare both adjacent ground-line positions while preserving the existing upper network's axis, deck directions, and native half sequence under [the alignment procedure](WORKFLOW_PIECE_CREATION.md#56-cover-diagonal-grid-alignments). Record the staged production order under A10; measuring both positions does not authorize producing the second alignment before user acceptance of the first.

## 4. Implementation and source data

- [ ] C01 — Edit the owning source or generator; preserve permanent IDs and the accepted geometry, scope, and data outside the change.
- [ ] C02 — Implement every required behavior and mode, plus relevant invalid-input and failure behavior; remove pending scaffold prose for completed functionality.
- [ ] C03 — Allocate and register only justified new types or resources; check collisions, modeled cells, runtime addresses, and controller ownership.
- [ ] C04 — Follow JSONC and Markdown conventions; update schemas, readers, writers, references, exports, and meaningful validation together when their contracts change.
- [ ] C05 — Keep shared mechanisms in the framework, measurements in the domain specification, and subject-specific contracts with the subject.
- [ ] C06 — Preserve original backup snapshots, frozen evidence, and human observations; assess stale dependencies without rewriting their historical outcomes.
- [ ] C07 — Add or adjust meaningful regression coverage for changed behavior, including a relevant failing control; do not invent tests for unchanged prose or mirror implementation details.
- [ ] C08 — Integrate delegated changes before final verification, and inspect the combined diff for conflicts, omissions, and unrelated edits.
- [ ] C09 — Evaluate all consumers affected by shared code or data changes; adapt the scope map and downstream checklist items accordingly.

## 5. Compiled resources and runtime behavior

Use [framework engineering](FRAMEWORK_ENGINEERING.md), the owning `NETWORK_SPEC.md`, and the independent domain verifier for exact limits. Apply only the mechanisms present in the selected subject.

- [ ] D01 — Build the intended selection from the actual current source and supported native inputs; identify the resulting manifest and saved DATs.
- [ ] D02 — Independently decode the saved resources and verify exact IDs, references, resource closure, collision checks, construction rules, and reversible shared-controller additions.
- [ ] D03 — Check actual models, texture references, render-group budgets, zooms, preview offsets, shadows, and required prop properties against the owning contract.
- [ ] D04 — Check every required directed traffic route and forbidden movement, including ground services, elevated levels, stops, lane metadata, and complete joining boundaries.
- [ ] D05 — Check saved paths against actual placed surfaces and complete support solids, including swept clearance between samples and model overhangs across cells.
- [ ] D06 — Verify all four proper rotations and any separately supported poses; distinguish them from reflection, camera rotation, and cursor-preview appearance.
- [ ] D07 — For adaptive ground with elevated traffic, check the selected active PATH, its height-retention setting, ground routes, and every elevated level under the [runtime-height procedure](WORKFLOW_PIECE_CREATION.md#54-preserve-adaptive-ground-artwork-beneath-elevated-models).
- [ ] D08 — Verify actual T21/prop selection and rotation requirements; keep sidewalk artwork, pedestrian routing, decorative geometry, and elevated traffic as separate mechanisms.
- [ ] D09 — Check the whole assembly's ownership, physical seams, supports, and end-to-end journeys after checking its members; individual piece passes cannot close this item.
- [ ] D10 — Compare affected and protected saved resources against the baseline; establish the claimed change and preservation scope from their actual bytes or measured geometry.
- [ ] D11 — For an implemented or claimed compatible extension or rearrangement, independently check the selected placed example's complete boundaries, traffic permissions, geometry, ownership, supports, keep-clear space, and construction in its claimed poses; preserve the base assembly's required journeys and restrictions, and keep hypothetical uses unverified.
- [ ] D12 — Verify each currently authorized diagonal grid alignment in all four proper rotations, including models, active PATHs, tile cuts, owned cells, construction flags, native helpers, previews, shadows, and adaptive ground where present; prove the original alignment's claimed preservation scope. Keep the other alignment's verification deferred until A10's user acceptance is recorded and that variant is produced, then compare both implemented phases. Repeated rotation states do not supply a missing alignment.

## 6. Documentation, artwork, and generated outputs

Follow [documentation generation](WORKFLOW_DOCUMENTATION_GENERATION.md), including its output checklist and final-artifact order. Preserve unchanged measurements and pictures when the requested scope does not require regeneration.

- [ ] E01 — Finish required saved-resource verification and owning extraction before refreshing measurements, source-bound connection declarations, exports, and cards.
- [ ] E02 — Refresh affected generated views, observation dependencies, and inventories through their owners; preserve exact observations and distinguish stale results from current evidence.
- [ ] E03 — Generate only the required final images from the correct compiled inputs, and inspect the actual PNGs for complete geometry, legibility, clipping, and consistent presentation.
- [ ] E04 — For an assembly, match the required reference view order, legends, badges, and annotations; verify translucent construction overlays, owned-tile outlines, and actual piece projections including overhang.
- [ ] E05 — Check required standalone views, menu icons, component thumbnails, connection cards, image paths, and current provenance against the requested scope.
- [ ] E06 — Complete authored README/TESTING content outside generated blocks; supply exact placement, menu, rotation, connection, and test instructions with genuine limitations.
- [ ] E07 — Update the owning workflow or reference when a reusable lesson changes future authoring decisions; link to it rather than duplicating a competing rule.
- [ ] E08 — Check metadata, numbered headings, navigation, one-line prose paragraphs, portable public paths, Oxford commas, and local links.
- [ ] E09 — Preserve all unknown, failed, and stale human observations; obtain explicit matching confirmation before recording a manual pass.
- [ ] E10 — Freeze the required documentation and artwork before the final candidate or packaging step; account for any later change through the owning freshness procedure.
- [ ] E11 — Record decisions about module usefulness, extension instructions, exact compatible types where established, missing adapters, and evidence limits in the existing subject documentation and atomization records; show which future assembly uses are proposals, combinations checked by software, or human-confirmed results.

## 7. Tests, evidence, and integrated review

- [ ] F01 — Run the relevant scoped checks and every check required by the applicable instructions, including `python3 -B tools/run_tests.py` where required by the repository rules.
- [ ] F02 — Run `python3 -B custom-pieces/scp.py docs-check`; use the unselected check when shared guides change, and retain its actual result.
- [ ] F03 — Run applicable native/saved-resource, connector, assembly, and regression checks against the final candidate; record unavailable mandatory inputs as unresolved work.
- [ ] F04 — Record commands, source/build identities, actual runner totals, failures, errors, skips, and coverage limits; never turn a skipped class or test into a pass.
- [ ] F05 — Resolve agent-actionable failures within the authorized task, rerun the affected checks after repairs, and preserve evidence needed to interpret earlier failures.
- [ ] F06 — Review the integrated result against every requirement and retained constraint, including delegated work; use an independent review where it materially adds confidence.
- [ ] F07 — Verify that every claimed result still matches the final source, resource bytes, artwork, pose, environment, and scope relevant to that claim; reopen stale rows.
- [ ] F08 — Separate software results, image inspection, Route Query, actual moving traffic, placement, and save/reload observations; record only the evidence actually obtained.
- [ ] F09 — For game retests, keep the reported configuration in the first comparison, test required directions/levels/rotations, and distinguish existing placements from fresh controls under the [update-placement policy](BUILD_AND_INSTALL.md#71-decide-whether-an-update-needs-fresh-placement).
- [ ] F10 — For diagonal crossings, plan separate game cases for both adjacent grid alignments on prebuilt native approaches and for supported dragging outward, and execute only the currently authorized alignment's cases. Keep the other alignment's cases `WAITING` until A10's acceptance gate is met and that variant is produced; do not mark them `N/A` or passed. Require actual moving traffic through every level and service, with alignment, rotation, construction order, Route Query, and visible travel recorded separately. Candidate acceptance does not supply game observations.

## 8. Packaging, installation, and publication

Use [build and install](BUILD_AND_INSTALL.md) for the exact commands. Treat each stage separately; producing an artifact does not establish its installation or operation.

- [ ] G01 — Select every intended retained type for a replacement build, and verify the resulting resource selection rather than relying on a smaller default set.
- [ ] G02 — For assembly delivery, prepare its required single-button component cycle from the final documented normal source build; verify preserved payloads and frozen proof.
- [ ] G03 — Package the correct candidate using its supported documentation-refresh policy; inspect the actual archive, manifests, member closure, hashes, and portable contents.
- [ ] G04 — For authorized installation, confirm the actual game is closed, preserve the previous receipt and installation, and use the standard backup-based installer.
- [ ] G05 — Verify the installed receipt and actual files against the checked candidate, and verify that the backup contains the expected prior installation.
- [ ] G06 — Confirm the relevant native donors, DLLs, unrelated owned files, and other protected inputs remain consistent with the intended installation change.
- [ ] G07 — Give exact game entry points and focused test actions, explain restart versus fresh placement, and keep human game checks pending until confirmed.
- [ ] G08 — Publish or send external messages only within the existing authorization and applicable release rules; report the actual destination and artifact identity if performed.
- [ ] G09 — Preserve needed review artifacts and snapshots; clean up only disposable resources whose removal is in scope, and leave human-only PR merges to the user.

## 9. Final handoff gate

### 9.1 Audit every item before reporting completion

Re-read the user's current request and the adapted checklist immediately before handoff. A complete handoff requires every applicable item to be `DONE` with current evidence and every exclusion to have a reviewed `N/A` reason. There must be no unexplained blank checkbox, silently removed requirement, unresolved agent-actionable failure, or unsupported success claim. A clean Git status and a finished subagent message do not establish this gate by themselves.

- [ ] H01 — Map every requirement and latest user correction to its implemented result and acceptance evidence; confirm that scope was not quietly reduced.
- [ ] H02 — Audit all item and section applicability decisions; missing required inputs, lack of time, and desired extra confidence are not interchangeable with non-applicability.
- [ ] H03 — Resolve every applicable agent-executable item; keep failed, waiting, and stale requirements open rather than ticking them for a tidy checklist.
- [ ] H04 — Inspect the final changed files, staged diff when committing, scope, public privacy, generated-output freshness, and absence of unintended changes.
- [ ] H05 — Confirm required checks apply to this final candidate, with real skips and remaining coverage limits disclosed; reopen affected items after any subsequent edit.
- [ ] H06 — Confirm each build, package, installation, publication, and game-operation claim has evidence for that exact stage and artifact.
- [ ] H07 — Review pending external/human checks individually; identify the responsible actor, missing input or action, exact candidate, and observable completion condition.
- [ ] H08 — Save the current working checklist and put durable findings and authoritative game observations in their existing owners; reference that evidence here without creating a competing observation record.
- [ ] H09 — Prepare a self-contained handoff stating the outcome, changed outputs, checks and limits, delivery stage, and any exact next actions required.
- [ ] H11 — For assembly design or substantial revision, audit atomization, expandability, and future usefulness explicitly: every retained block or new type has a reason, intended extensions have usable interfaces and space, and every reuse/compatibility claim has current evidence or an honest proposal label. This review does not authorize redesigning unchanged accepted subjects.
- [ ] H10 — Record the final gate decision below after the preceding audit, and close this audit row together with that record; do not mark the task complete while other applicable requirements remain open.

### 9.2 Record the gate decision

| Field | Required final value in the working copy |
| --- | --- |
| Candidate audited | Exact source/commit, build/package, and installed identity where applicable. |
| Item accounting | Actual `DONE`, `N/A`, and open counts or explicit item IDs, including omitted-section exclusions. |
| Requirement coverage | Evidence for each acceptance condition, with unresolved requirements named. |
| Checks and coverage | Real command outcomes, skip reasons, review scope, and evidence references. |
| Gate result | `COMPLETE` only when every applicable requirement is resolved; otherwise `INCOMPLETE — TEST HANDOFF` or `INCOMPLETE — DEPENDENCY HANDOFF`. |
| Outstanding work | For each open item: actor/input, next action, exact artifact, and how to verify completion. Use `none` only when true. |
| Final audit | Who reviewed the checklist, when, and where its current working copy is retained. |

An incomplete handoff is a truthful exception report, not task completion. Use it only when remaining work actually depends on external input, human game observations, or an action outside current authorization; finish all independent authorized work first. For example, an installed experimental candidate can be ready for the user's traffic test while its game checks remain open. State that stage explicitly, retain those open items for continuation, and never relabel them `N/A` or infer a game pass to satisfy the gate. This template adds no new approval requirement for actions the user has already authorized.

For the user-required [staged alignment gate](WORKFLOW_PIECE_CREATION.md#alignment-production-order), distinguish a completed first-alignment review candidate from completion of the full two-alignment family. Record the first candidate's finished stage and the other alignment's `WAITING` dependency on explicit user acceptance in the gate table. Do not claim the family is complete or produce the deferred alignment to close its rows. Reuse matching acceptance already recorded under A10, and preserve independent pending game checks.
