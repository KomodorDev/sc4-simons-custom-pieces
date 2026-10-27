---
title: "Highway (reserved; no pieces implemented) \u2014 assembly blueprints"
summary: "Find each documented multi-placement assembly, a clean preview, and its per-service test coverage."
audience: "players"
document_type: "catalogue"
---

# Highway (reserved; no pieces implemented) — assembly blueprints

This inventory is generated from each assembly’s saved records. The source files and update procedure are explained under **Where the results come from** below. Checked means every applicable listed current case passed. Preview review and correct rendering inside SimCity 4 are separate checks. A result covers only its named scope, rotation, and recorded environment. Legacy endpoint observations remain historical evidence in the subject checklist and do not establish current compatibility coverage.

## Legend

An **assembly** is a complete layout made from reusable pieces. A **piece type** is one reusable component design; a **placement** is one copy of that type at a particular position and rotation.

| Column | How to read it |
| --- | --- |
| Clean preview | A computer-rendered picture of the complete layout without component-name labels. Click it to open the full image. |
| Blueprint | The assembly name. Click it to open the guide with its pictures, component list, and placement instructions. This is a layout to construct from components; each placement requires its own click. |
| Placements / types | Total placed copies / number of different reusable piece types. For example, `5 / 3` means five copies using three types; repeated copies of one type count as several placements but only one type. These numbers do not count tiles or menu buttons. |
| Preview reviewed | Recorded human reviews of the declared final assembly images. Each image has its own case; generating an image does not record its approval. |
| Renders correctly in game | Recorded human checks that the complete placed layout looks correct inside SimCity 4 under the declared conditions. This checks appearance; the connection matrix separately reports traffic. |
| Connection matrix summary | A summary of the results displayed in the blueprint’s entrance → exit matrix. Saved PATH, Route Query, visible travel, and forbidden-movement checks have separate totals. Click **Open matrix** to inspect those entries and their exact evidence. |

### Where the results come from

**Both appearance columns read `checks/manual-tests.json` inside the assembly’s folder.** This is the saved observation record:

- **Preview reviewed** reads the `preview_review` cases.
- **Renders correctly in game** reads the `in_game_render` cases.

**`TESTING.md` displays the same saved observations. The inventory does not read its checkboxes.** Editing text or ticking a checkbox in `TESTING.md` does not update the observation record or the inventory results.

The **Connection matrix summary** uses the same calculation as the README matrix. It combines the movements and current software evidence in `connections.json` with the results in `checks/manual-tests.json`; it does not read the rendered Markdown table.

To update a human result, perform the exact check, obtain explicit human confirmation, and save that observation using the [recording procedure](../../../docs/TESTING.md#record-one-observation). In this repository, the recording command updates the saved record and refreshes `TESTING.md`, the README matrix, and the inventory. Regenerating documents alone does not record a pass.

### How to read the results

A **case** is one specific check. In the two review columns, `0/6 passed` means zero of six applicable current cases have a recorded pass. `[x]` means all applicable current cases passed; `[ ]` means that condition is not met. **Unverified** means no qualifying result is recorded, **failed** means an observation found a problem, and **stale** means relevant resources or conditions changed after the recorded result. Unverified does not mean failed. Explicit not-applicable cases and historical observations are excluded from these case fractions. `Not applicable / no declared cases` means there are no applicable cases to count, and `Unverified; record missing` means the observation record is absent; neither is a pass.

The **connection matrix summary** counts displayed matrix entries for each check: **confirmed** matches ✅, **failed** matches ❌, and **not established** matches ?. An entry is confirmed only when all checks required for its declared orientations are current passes. Missing, stale, ambiguous, or not-applicable evidence leaves an entry not established. **Saved PATH** checks the saved traffic routes; **Route Query** uses the game’s route-inspection tool; **Visible travel** requires observing a vehicle complete the journey; and **Forbidden in game** checks that a prohibited movement stays unavailable. One software result can support several Saved PATH entries, so these are matrix-entry counts, not independent test-case counts. Game appearance stays in its own column. Open the blueprint’s **Testing** link for the detailed observations and checks outside the matrix.

| Clean preview | Blueprint | Placements / types | Preview reviewed | Renders correctly in game | Connection matrix summary |
| --- | --- | --- | --- | --- | --- |

No assembly blueprints are registered in this domain.
