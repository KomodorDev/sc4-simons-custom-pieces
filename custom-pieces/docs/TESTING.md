---
title: "Record and interpret test results"
summary: "Explain once how to read scoped checks and record an explicitly confirmed observation for any piece or assembly."
audience: "Players, testers, and authors"
document_type: "procedure"
---

# Record and interpret test results

A **piece** is one reusable menu type. An **assembly** is a layout made from placed copies. Read a piece's README or an assembly's TESTING page to find its exact checks. A **case** is one specific observation, such as a directed journey at a stated rotation and game environment. A pass for one case does not cover a different direction, transport, rotation, or platform.

## Piece validation and compatibility discovery

**Intrinsic validation** checks the piece itself: its actual compiled resources, internal routes, exposed boundary measurements, declared connector associations, and supported construction orientations. Run the owning saved-resource verifier and, for a migrated piece, its connector refresh/check. These operations do not need an automatically selected neighbour or a manual test of every possible pair.

**Compatibility discovery** is a separate Planner operation that compares complete shared boundaries of pieces with current, validated connector exports. It checks all required services and channels under one placement. Pieces without the new declarations are outside that operation's coverage; stale, missing, or invalid exports are excluded with a reason. Neither exclusion establishes incompatibility. Follow the [Planner instructions](../../scp-planner/README.md) to run discovery; do not use historical per-port counterpart shortlists as compatibility results.

Developer tests verify the generator and matching rules, while focused in-game observations investigate new behavior, changed game assumptions, or reported problems. Existing rendering, placement, journey, demolition, and save/reload records retain their particular scope. Public-release evidence remains governed by [RELEASE.md](RELEASE.md). No per-piece test-plan file or automatic all-pairs manual checklist is required.

## Investigate single-tile demolition and connected survivors

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

## Understand the displayed results

Individual-piece and assembly inventories use the same three evidence columns, calculated from each subject's own `checks/manual-tests.json`. A **directed journey** is one permitted movement from a particular entry to a particular exit; the reverse movement is a separate case. A **service** is the transport using that movement, such as HSR, Road, or pedestrians.

| Inventory column | Individual piece | Assembly |
| --- | --- | --- |
| Preview reviewed | Review each declared final image of the reusable type, including its angled, top, and connector-overview images where present. | Review each declared final image of the complete layout. |
| Renders correctly in game | Observe the placed type inside SimCity 4 at each declared supported construction orientation and under the recorded conditions. | Observe the complete placed layout inside SimCity 4 under the recorded conditions. |
| Directed journey cases | Observe each declared permitted entry → exit movement through the type, separately for each service and supported construction orientation. | Observe each declared permitted entry → exit movement through the complete layout, including its joins between pieces, separately for each service and declared orientation. |

A piece pass does not approve a complete assembly: its placement, joins, and end-to-end journeys still need their own evidence. An assembly pass covers only its recorded use of those pieces; it does not approve every other orientation or use of each reusable type. These three columns summarize declared cases, not every possible situation. Keep forbidden-transfer checks and other applicable checks in the subject's full checklist. Preview review, saved-resource validation, and in-game observation remain separate; generating artwork or validating a PATH resource cannot record a game pass.

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

Software checks, review of a rendered picture, and operation inside SimCity 4 are separate evidence. A successful build cannot tick a human rendering, connection, or journey case. Unused tracks without travel demand do not establish a traffic pass. For a real journey, provide matching station connections and demand, then use Route Query or observe traffic in the stated direction.

When reporting a software test run, state how many tests were **collected** (found by the test runner), **passed**, **failed**, and **skipped** (not executed). For example, `435 collected; 428 passed; 0 failed; 7 skipped` does not mean 435 passed. Give the skip reason and its coverage limit, such as `Seven connector-export tests require an unavailable older compiled build, so that build's export behavior was not checked.` Report any other outcomes separately; software counts do not change manual observation states.

## Record one observation

After creating or deliberately changing artwork, first run `python3 custom-pieces/scp.py observations refresh-images --piece EXACT-PIECE-ID` from the parent project directory, followed by `python3 custom-pieces/scp.py inventory`. Replace the identifier with the actual selected type. This gives each existing angled, top, and connector-overview PNG its own exact review scope without extracting routes, computing compatibility, changing game cases, or recording an approval. Follow the [final-artifact sequence](WORKFLOW_DOCUMENTATION_GENERATION.md#final-artifacts-and-packaging) for the complete generation and packaging order. A prose-only refresh intentionally preserves the observation record and cannot supply this missing image binding.

1. Open the piece README or assembly TESTING page and find `Test checklist`. Click the relevant check/service group, such as `Journey — hsr`, to open its rotation table. Locate the entry/exit or port pair, then click the matching exact-scope title below the table. Copy the case ID beside the required rotation, such as `90° CCW`; `CCW` means counterclockwise. Check its service, entry/exit or counterpart, relative position, rotation, and tested environment. For historical evidence, use its separately labeled section instead.
2. Perform that exact check. For a game observation, record the platform, game version, and NAM profile. Inspect the relevant rotation and direction; do not infer the other orientations.
3. In the subject's `checks` folder, copy `observation.example.json` to a new `observation.json`. The example is a blank template, not evidence. Set `case_id`, `result` (`passed` or `failed`), `reviewer`, `confirmed_at` (an ISO date such as `2026-10-20`), and `evidence` (screenshot paths or explicit observed facts). Fill all three environment fields for game cases.
4. Set `explicit_user_confirmation` to `true` only after the human user confirms that precise observation. An agent must not infer confirmation. Leave the supplied example unchanged.
5. Open Terminal in the project folder containing `custom-pieces`. On a new source checkout, follow [Build and install](BUILD_AND_INSTALL.md#build-a-selected-collection) to install Python dependencies and register the editable packages. Copy the subject-specific record command from its generated test section and run it. For the trumpet, it is:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/01_assemblies/straight-stem-trumpet-v4/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/01_assemblies/straight-stem-trumpet-v4/checks/observation.json
```

6. Read the result and reopen the piece README or assembly TESTING page. The command updates the authoritative JSON record, generated summaries, and inventories. Do not type checkmarks into Markdown.

For a justified not-applicable declaration, use `result: "not_applicable"` and provide a nonempty `reason`. A failing result should retain its actual description and evidence. The tool rejects a manual pass without explicit confirmation, identity, date, evidence, and required game environment.

## Data ownership and stale evidence

Each subject's `checks/manual-tests.json` is the sole observation record. It preserves exact case identities, dependencies, and evidence. `connections.json` records interfaces extracted from actual saved resources. The README, TESTING page, and inventories are generated views of those records. They are not separate result authorities.

Older records can contain `in_game_connection` cases generated from an arbitrary endpoint/counterpart shortlist. Current generation does not create those cases. To retire them from active coverage without extracting resources, recomputing compatibility, or recording a result, run from the parent project directory:

```sh
python3 custom-pieces/scp.py observations retire-connections --piece EXACT-PIECE-ID
```

Replace `EXACT-PIECE-ID` with a registered identifier. Repeat `--piece`, use `--assembly EXACT-ASSEMBLY-ID`, or use `--all` for all registered subjects. The operation preserves the other cases and their evidence. Legacy connection observations and explicit not-applicable declarations remain in historical coverage with their original identities and dependencies; they do not become complete-edge passes. Unobserved generated placeholders can be removed. Repeating the operation must make no further changes.

Only relevant changes invalidate a result: a preview review follows that image's bytes; a connection follows both subjects' relevant resources and relative pose; an assembly journey follows its traffic graph, placement, and simulator conditions. A new shortcut elsewhere in the connected traffic graph can change a journey beyond the directly edited route, so assess the complete relevant graph before carrying that result forward. Documentation edits, source relocations, and identical rebuilt resources do not by themselves invalidate a game observation. Original observations stay available when their current state becomes stale.

To regenerate prose from existing metadata without changing observations or rechecking DAT resources, follow [the generated-Markdown refresh procedure](WORKFLOW_DOCUMENTATION_GENERATION.md#refresh-generated-markdown-and-inventories). It owns that command, README generation, and inventory refresh; the observation-recording command above remains the way to record an explicitly confirmed test result.

Report actual scoped coverage, such as 7 of 12 applicable journey cases passed, rather than calling the whole subject verified. After actual resource changes, use the owning domain's extraction and verification tools before updating cases. The software/resource report and human observations must identify their real input fingerprints; neither can inherit an unrelated passing result. See [framework engineering](FRAMEWORK_ENGINEERING.md#documentation-generation-and-observations) for generator ownership and [release requirements](RELEASE.md) for publication evidence.
