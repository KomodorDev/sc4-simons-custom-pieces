---
title: "Record and interpret test results"
summary: "Explain once how to read scoped checks and record an explicitly confirmed observation for any piece or assembly."
audience: "Players, testers, and authors"
document_type: "procedure"
---

# Record and interpret test results

<!-- BEGIN DOCUMENT NAVIGATION -->
[1. Piece validation and compatibility discovery](#1-piece-validation-and-compatibility-discovery) · [2. Investigate single-tile demolition and connected survivors](#2-investigate-single-tile-demolition-and-connected-survivors) · [3. Understand the displayed results](#3-understand-the-displayed-results) · [4. Record one observation](#4-record-one-observation) · [5. Data ownership and stale evidence](#5-data-ownership-and-stale-evidence) · [6. Existing saves after piece removal](#6-existing-saves-after-piece-removal)
<!-- END DOCUMENT NAVIGATION -->

A **piece** is one reusable menu type. An **assembly** is a layout made from placed copies. Read the subject’s TESTING document to find its exact checks; a legacy combined piece guide keeps those checks in its README until deliberately migrated. A **case** is one specific observation, such as a directed journey at a stated rotation and game environment. A pass for one case does not cover a different direction, transport, rotation, or platform.

New subjects and guides deliberately migrated to the split layout follow the shared [six-chapter TESTING layout](WORKFLOW_DOCUMENTATION_GENERATION.md#123-required-piece-and-assembly-testing-layout). Use chapter 1 for exact scope and technical connections, chapter 2 for preparation, chapter 3 for software checks, chapter 4 for game actions, chapter 5 for known issues and the generated checklist, and chapter 6 for design history. Split pieces also keep their generated manual summary in chapter 5. Their three-chapter README links each matrix result to `TESTING.md#case-…`. This guide owns the common recording procedure; each subject supplies its exact conditions, case links, and recording command. Existing version-1 and unmarked combined guides retain their test sections until explicitly migrated.

<a id="piece-validation-and-compatibility-discovery"></a>

## 1. Piece validation and compatibility discovery

**Intrinsic validation** checks the piece itself: its actual compiled resources, internal routes, exposed boundary measurements, declared connector associations, and supported construction orientations. Run the owning saved-resource verifier and, for a migrated piece, its connector refresh/check. These operations do not need an automatically selected neighbour or a manual test of every possible pair.

**Compatibility discovery** means finding candidate joins by comparing complete shared boundaries of pieces with current, validated connector exports. The current library does not supply an automatic discovery operation. A future consumer must check all required services and channels under one placement and explicitly exclude unmigrated, stale, missing, or invalid inputs. Exclusion does not establish incompatibility. Do not use historical per-port counterpart shortlists as compatibility results.

Developer tests verify generators and source-validation rules, while focused in-game observations investigate new behavior, changed game assumptions, or reported problems. Existing rendering, placement, journey, demolition, and save/reload records retain their particular scope. Public-release evidence remains governed by [RELEASE.md](RELEASE.md). The split piece TESTING document contains the subject’s plan and results; do not add another test-plan helper or an automatic all-pairs manual checklist.

<a id="investigate-single-tile-demolition-and-connected-survivors"></a>

## 2. Investigate single-tile demolition and connected survivors

**Demolition** means removing a placed network tile with the game's bulldozer. A **connected survivor** is a neighbouring piece that shares the network with the removed piece and whose own occupied tiles were not selected for removal. A **disconnected control** is an otherwise comparable copy with no network connection to the demolition site. These distinguish a local removal problem from a change spreading along the connected network.

The existing generated `in_game_demolition` case asks for removal of the complete placement and inspection of the cleared area. Its case ID, observations, and coverage remain unchanged. An old pass for that case does not establish that deleting one tile preserves connected neighbours. Likewise, an ordinary save/reload pass does not establish persistence after demolition. For a reported partial-deletion problem, keep the focused regression results in a separate bug record bound to the exact tested build; do not rename the old case, expand its pass, or generate a catalogue-wide counterpart matrix.

1. Use a disposable test city. Record the candidate build's manifest SHA-256, which identifies its exact manifest bytes, and the actual platform, game version, NAM profile, and relevant DLL versions. Keep the installed candidate unchanged for the run. Close the game before changing installed files between candidates.
2. Reproduce the reported connected layout. At minimum, place a target piece **A** and a compatible neighbour **B** with a real shared network connection. Place a comparable copy **C** separately, with at least eight empty tiles between its occupied footprint and the connected group, and confirm that no other network links them. Eight tiles is the chosen control spacing for this procedure; it does not establish the engine's maximum update distance. Record each exact piece ID, placement reference, rotation, construction-transposed state where supported, and menu entry point. A drawing or top-view screenshot should identify A, B, C, and the intended deletion tile.
3. Inspect and capture the baseline before removal. Confirm that A, B, and C show their expected custom models. If checking paths, record the particular Route Query or traffic observation separately; appearance alone does not prove a working journey.
4. Click the bulldozer tool, move the cursor over one recorded occupied tile of A, and click once. Do not drag a removal area across B. Record the selected tile relative to A's reference position and whether the game removes one tile or A's whole footprint; whole-footprint removal can be the intended behavior of a multi-tile puzzle piece.
5. Inspect B, the rest of the connected group, and C immediately. Record which surviving pieces change, whether they show the base network such as Monorail, and whether any occupied tile of those pieces was actually removed. Keep the immediate failure evidence before attempting repairs. A changed model does not by itself establish that the saved network or its paths changed.
6. Re-place A at exactly its original reference position and construction orientation, using the recorded entry point. Inspect the survivors and C again, and record whether the original appearance returns. If placement is blocked, record that result and the remaining tiles; do not silently clear additional tiles and call the original layout repaired.
7. Save this disposable test city, quit the game completely, reopen it with the same installed candidate, and reload that city. Inspect the same pieces again. Record whether the observed damage or repair persists. A result after re-placement covers that repaired state; if persistence of the unrepaired failure also matters, test it from a separately preserved failing state and label the two states explicitly.
8. Test complete-placement removal independently from a fresh baseline when that existing demolition case is relevant. Keep its evidence separate from the single-tile procedure. When comparing a proposed fix with an earlier build, repeat the same layout, selected tile, actions, and environment from the same baseline, and bind each result to its own manifest. Do not use an already damaged city as the only control.

The focused record must distinguish the baseline, immediate removal, re-placement, and reload outcomes, and retain the connected/disconnected comparison. Record observed facts even when the exact deleted piece or environment is still unknown; leave missing facts explicit. A report of “only connected pieces changed after one-tile deletion” is valuable evidence, but it does not identify every affected piece, orientation, or menu entry point. Only explicit human confirmation can record a pass or failure, and a passing reproduction covers only the tested layout and conditions. Software resource validation cannot complete these game checks.

<a id="understand-the-displayed-results"></a>

## 3. Understand the displayed results

The **Preview reviewed** and **Renders correctly in game** columns read each subject's authoritative `checks/manual-tests.json`: image approval uses `preview_review` cases, and game appearance uses `in_game_render` cases. `TESTING.md` displays the same recorded observations; neither the inventory nor the README matrix reads results back from Markdown. A **directed journey** is one permitted movement from a particular entry to a particular exit; the reverse movement is separate. A **service** is the transport using that movement, such as HSR, Road, or pedestrians.

| Inventory column | Individual piece | Assembly |
| --- | --- | --- |
| Preview reviewed | Review each declared final image of the reusable type, including its angled, top, and connector-overview images where present. | Review each declared final image of the complete layout. |
| Renders correctly in game | Observe the placed type inside SimCity 4 at each declared supported construction orientation and under the recorded conditions. | Observe the complete placed layout inside SimCity 4 under the recorded conditions. |
| Directed journey cases / Connection matrix summary | Directed journey cases count the declared in-game checks through the type, separately for each service and supported construction orientation. | Connection matrix summary reports the entries displayed in the README matrix, with separate totals for Saved PATH, Route Query, visible travel, and forbidden movements in game. |

A piece pass does not approve a complete assembly: its placement, joins, and end-to-end journeys still need their own evidence. An assembly pass covers only its recorded use of those pieces; it does not approve every other orientation or use of each reusable type. These columns summarize their declared scope, not every possible situation. The subject's full checklist retains the detailed observations and additional checks, such as placement, demolition, and save/reload. Preview review, saved-resource validation, and in-game observation remain separate; generating artwork or validating a PATH resource cannot record a game pass.

The assembly connection summary uses the same movement definitions, evidence, required orientations, and status rules as the README matrix. `connections.json` supplies the declared movements and current resource/graph fingerprints, and `checks/manual-tests.json` supplies the recorded results. Each total counts the matrix entries displaying that check: confirmed matches ✅, failed matches ❌, and not established matches ?. Missing cases, stale evidence, duplicate matches, and not-applicable declarations cannot turn a matrix entry green. These counts are not numbers of independent software tests: several Saved PATH entries can share one software-connectivity result. Whole-assembly game appearance stays outside these movement totals. An assembly without a declared README matrix has no matrix summary; a missing input remains explicitly unverified.

| State | Meaning |
| --- | --- |
| `[x] passed` | A matching current observation explicitly confirmed the case. |
| `[ ] unverified` | No qualifying result has been recorded. |
| `[ ] failed` | A qualifying observation found a problem. |
| `[ ] stale` | Relevant resources or conditions changed after the observation; the original evidence is retained. |
| Not applicable | An explicit declaration with a reason, separate from a pass. |

The checklist starts with current totals and collapsed **check/service groups**, such as `Journey — hsr` or `Forbidden transfer — hsr → road`. A group is a browsing aid, not a combined observation. Its title reports its exact case count and state counts, including failures and stale results. Click the group title to reveal a table with a separate column for each rotation. Click an exact-scope title below that table to reveal its case IDs, counterpart poses, and recorded reviewer/environment information. `General` means that the case has no rotation; `T` identifies a distinct construction-transposed state, where the construction rules support one. Opposite directions and HSR, tram, or other services stay distinct.

**Forbidden transfers** are directed movements that the declared graph does not permit. Their groups use the service pair, such as `hsr → road`; every individual port pair and rotation remains in the table and detailed cases. Grouping does not remove cases, change their scope, or record a pass. A successful software graph check cannot confirm these in-game observations.

Any failed or stale cases also appear in a table above the groups, with their exact scope, rotation, and case link. Their matching groups and exact scopes start expanded so those links lead to visible details. Historical failures and stale observations are labeled `Historical` and stay outside current totals; their expanded cases appear in separate sections below the current groups. A design warning is also separate from a test result: valid encoded files can still have awkward geometry.

Software checks, review of a rendered picture, and operation inside SimCity 4 are separate evidence. A successful build cannot tick a human rendering, connection, or journey case. Unused routes without travel demand do not establish a traffic pass. For a real journey, provide matching outside connections and the applicable travel demand. Record Route Query and visible-travel observations separately when the declared test plan requires both; one does not establish the other.

When reporting a software test run, use the test runner's actual totals and labels. Report failures, errors, skips, and any other outcomes explicitly; give skip reasons and their coverage limits. This project's `unittest` runner can count skipped classes and individual **subtests** (checks inside one test method) differently from the headline `Ran N tests` count. Do not calculate a passed count by subtracting skip reports from that headline, or relabel the headline as passed or collected. For example, `884 reported tests; 76 skip reports; no failures or errors` preserves what the runner actually reported without inventing a passed total. If a runner supplies separate collected and passed totals, use them as supplied. Software counts do not change manual observation states.

<a id="record-one-observation"></a>

## 4. Record one observation

After creating or deliberately changing artwork, first run `python3 custom-pieces/scp.py observations refresh-images --piece EXACT-PIECE-ID` from the parent project directory, followed by `python3 custom-pieces/scp.py inventory`. Replace the identifier with the actual selected type. This gives each existing angled, top, and connector-overview PNG its own exact review scope without extracting routes, computing compatibility, changing game cases, or recording an approval. Follow the [final-artifact sequence](WORKFLOW_DOCUMENTATION_GENERATION.md#13-final-artifacts-and-packaging) for the complete generation and packaging order. A prose-only refresh intentionally preserves the observation record and cannot supply this missing image binding.

1. Open the subject’s TESTING page and find `Test checklist`; for a legacy combined piece guide, use that section in its README. Click the relevant check/service group, such as `Journey — hsr`, to open its rotation table. Locate the entry/exit or port pair, then click the matching exact-scope title below the table. Copy the case ID beside the required rotation, such as `90° CCW`; `CCW` means counterclockwise. Check its service, entry/exit or counterpart, relative position, rotation, and tested environment. For historical evidence, use its separately labeled section instead.
2. Perform that exact check. For a game observation, record the platform, game version, and NAM profile. Inspect the relevant rotation and direction; do not infer the other orientations.
3. In the subject's `checks` folder, copy `observation.example.json` to a new `observation.json`. The example is a blank template, not evidence. Set `case_id`, `result` (`passed` or `failed`), `reviewer`, `confirmed_at` (an ISO date such as `2026-10-20`), and `evidence` (screenshot paths or explicit observed facts). Fill all three environment fields for game cases.
4. Set `explicit_user_confirmation` to `true` only after the human user confirms that precise observation. An agent must not infer confirmation. Leave the supplied example unchanged.
5. Open Terminal in the project folder containing `custom-pieces`. On a new source checkout, follow [Build and install](BUILD_AND_INSTALL.md#4-build-a-selected-collection) to install Python dependencies and register the editable packages. Copy the subject-specific record command from its generated test section and run it. For the trumpet, it is:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/01_assemblies/hsr-trumpet-straight-stem/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/01_assemblies/hsr-trumpet-straight-stem/checks/observation.json
```

6. Read the result and reopen the subject’s TESTING page, or the README test section of a legacy combined piece guide. The command updates the authoritative JSON record, generated summaries, and inventories. Do not type checkmarks into Markdown.

For a justified not-applicable declaration, use `result: "not_applicable"` and provide a nonempty `reason`. A failing result should retain its actual description and evidence. The tool rejects a manual pass without explicit confirmation, identity, date, evidence, and required game environment.

<a id="data-ownership-and-stale-evidence"></a>

## 5. Data ownership and stale evidence

Each subject's `checks/manual-tests.json` is the sole observation record. It preserves exact case identities, dependencies, and evidence. `connections.json` records interfaces extracted from actual saved resources. The README, TESTING page, and inventories are generated views of those records. They are not separate result authorities.

An experiment involving a saved city and several removed types can have a separate shared record under `docs/evidence/`, as in [chapter 6](#6-existing-saves-after-piece-removal). Such a record preserves its particular human report and build identities; it does not update individual piece or assembly cases.

Older records can contain `in_game_connection` cases generated from an arbitrary endpoint/counterpart shortlist. Current generation does not create those cases. To retire them from active coverage without extracting resources, recomputing compatibility, or recording a result, run from the parent project directory:

```sh
python3 custom-pieces/scp.py observations retire-connections --piece EXACT-PIECE-ID
```

Replace `EXACT-PIECE-ID` with a registered identifier. Repeat `--piece`, use `--assembly EXACT-ASSEMBLY-ID`, or use `--all` for all registered subjects. The operation preserves the other cases and their evidence. Legacy connection observations and explicit not-applicable declarations remain in historical coverage with their original identities and dependencies; they do not become complete-edge passes. Unobserved generated placeholders can be removed. Repeating the operation must make no further changes.

Only relevant changes invalidate a result: a preview review follows that image's bytes; a connection follows both subjects' relevant resources and relative pose; an assembly journey follows its traffic graph, placement, and simulator conditions. A new shortcut elsewhere in the connected traffic graph can change a journey beyond the directly edited route, so assess the complete relevant graph before carrying that result forward. Documentation edits, source relocations, and identical rebuilt resources do not by themselves invalidate a game observation. Original observations stay available when their current state becomes stale.

To regenerate prose from existing metadata without changing observations or rechecking DAT resources, follow [the generated-Markdown refresh procedure](WORKFLOW_DOCUMENTATION_GENERATION.md#124-refresh-generated-markdown-and-inventories). It owns that command, README generation, and inventory refresh; the observation-recording command above remains the way to record an explicitly confirmed test result.

Report actual scoped coverage, such as 7 of 12 applicable journey cases passed, rather than calling the whole subject verified. After actual resource changes, use the owning domain's extraction and verification tools before updating cases. The software/resource report and human observations must identify their real input fingerprints; neither can inherit an unrelated passing result. See [framework engineering](FRAMEWORK_ENGINEERING.md#11-documentation-generation-and-observations) for generator ownership and [release requirements](RELEASE.md) for publication evidence.

## 6. Existing saves after piece removal

Removing a piece type from the installed plugin can leave previously placed tiles referring to resources that are no longer available. A **saved tile reference** is one tile's stored resource identifier; several tile references can belong to one placed piece. This experiment concerns clearing those affected tiles after the old resources have been removed.

On **30 October 2026**, the player reported successful clearance of the affected area after installing **`installer-a2c842ca62ae`**. **Visual artifacts were present**, but the player could empty the plots previously occupied by pieces absent from the new mod. The [authoritative observation record](evidence/missing-piece-upgrade-20261030.jsonc) preserves the exact report, installed-build fingerprint, preparation audits, and coverage limits. It is a public summary of existing private evidence and this human report, rather than a new game test.

| Check | Recorded result |
| --- | --- |
| Existing affected area reachable and clearable after the upgrade | Confirmed by the player's successful cleanup report. |
| Visual appearance during the reported test | Visual artifacts reported; their exact appearance and persistence were not specified. |
| Test preparation | The retained-piece city copy contained 18 saved tile references to removed resources; the separately cleaned control contained none. |
| Separate control-city game result | Not individually described in the report. |
| Traffic operation and save/reload after cleanup | Not separately confirmed. |
| Other cities, removed resources, and construction orientations | Outside this observation's scope. |

This result establishes successful cleanup in the reported experiment. It does not establish artifact-free rendering or general safety when removing piece resources. Keep the existing [installation and rollback precautions](BUILD_AND_INSTALL.md#7-install-remove-or-roll-back-a-test-build): preserve an untouched region backup and the matching old plugin, use disposable city copies, and close the game before changing installed files. Removing placed pieces while their old resources are still installed remains the precaution for ordinary updates or reversals.
