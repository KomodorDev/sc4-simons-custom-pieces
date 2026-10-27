---
title: "High Speed Rail and Ground High Speed Rail \u2014 assembly blueprints"
summary: "Find each documented multi-placement assembly, a clean preview, and its per-service test coverage."
audience: "players"
document_type: "catalogue"
---

# High Speed Rail and Ground High Speed Rail — assembly blueprints

Generated from each subject’s authoritative `checks/manual-tests.json`. Checked means every applicable listed current case passed. Preview review and correct rendering inside SimCity 4 are separate checks. A result covers only its named scope, rotation, and recorded environment. Legacy endpoint observations remain historical evidence in the subject checklist and do not establish current compatibility coverage.

## Legend

An **assembly** is a complete layout made from reusable pieces. A **piece type** is one reusable component design; a **placement** is one copy of that type at a particular position and rotation.

| Column | How to read it |
| --- | --- |
| Clean preview | A computer-rendered picture of the complete layout without component-name labels. Click it to open the full image. |
| Blueprint | The assembly name. Click it to open the guide with its pictures, component list, and placement instructions. This is a layout to construct from components; each placement requires its own click. |
| Placements / types | Total placed copies / number of different reusable piece types. For example, `26 / 14` means 26 copies using 14 types; repeated copies of one type count as several placements but only one type. These numbers do not count tiles or menu buttons. |
| Preview reviewed | Recorded human reviews of the declared final assembly images. Each image has its own case; generating an image does not record its approval. |
| Renders correctly in game | Recorded human checks that the complete placed layout looks correct inside SimCity 4 under the declared conditions. This checks appearance; journey checks separately test traffic. |
| Directed journey cases | Recorded in-game checks for permitted entry → exit movements through the complete layout and its joins. The reverse direction, different transport services, and declared rotations have separate cases. One movement can require more than one check. |

A **case** is one specific check. For example, six directed routes with separate Route Query (the game’s route-inspection tool) and visible-travel checks produce 12 cases. Open the blueprint, then its **Testing** link, to see the exact cases and any additional checks that these three summary columns do not include.

**Results:** `0/6 passed` means zero of six applicable current cases have a recorded pass. `[x]` means all applicable current cases passed; `[ ]` means that condition is not met. **Unverified** means no qualifying result is recorded, **failed** means an observation found a problem, and **stale** means relevant resources or conditions changed after the recorded result. Unverified does not mean failed. Explicit not-applicable cases and historical observations are excluded from the fraction. `Not applicable / no declared cases` means there are no applicable cases to count, and `Unverified; record missing` means the observation record is absent; neither is a pass.

| Clean preview | Blueprint | Placements / types | Preview reviewed | Renders correctly in game | Directed journey cases |
| --- | --- | --- | --- | --- | --- |
| [![Straight-stem HSR trumpet](straight-stem-trumpet/previews/preview.png)](straight-stem-trumpet/previews/preview.png) | [Straight-stem HSR trumpet](straight-stem-trumpet/README.md) | 26 / 14 | [ ] 0/6 passed; 6 unverified; 0 failed; 0 stale | [ ] 0/1 passed; 1 unverified; 0 failed; 0 stale | [ ] 0/12 passed; 12 unverified; 0 failed; 0 stale |
